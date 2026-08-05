#!/usr/bin/env python3
"""Diagnostic trace for main_v7.11.py's unit_action scheduler.

Monkeypatches unit_action (via before/after diff of the `tasks` dict, so we
know exactly which (task_key, tile) got claimed on every call) and _agent
(to reset a per-turn call-order counter + stash day/hour) WITHOUT altering
game-affecting logic -- the original functions still run untouched, we just
observe their effects.

Tracks, per (farmer=idx0, hand=idx1..N) call-order slot:
  - total move / work / pass counts (sanity check vs the known 66/32/2% split)
  - "retarget" events: a slot was walking toward tile T last turn (didn't
    arrive), and this turn's movement claim is a DIFFERENT tile -- i.e. the
    walk was abandoned before completion.
  - who "stole" a target: turns where a slot's tracked target disappeared
    from the shed tasks entirely between our two observations (claimed by
    a different slot in the same turn) vs cases where the unit itself just
    changed its mind (new tile became nearer / different category won).
"""
import importlib.util
import sys
from collections import defaultdict

MOD_PATH = "main_v7.13.py"

spec = importlib.util.spec_from_file_location("main_v711_trace", MOD_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

orig_unit_action = mod.unit_action
orig_agent = mod._agent

call_idx = [0]
cur_day = [0]
cur_hour = [0]

# idx -> (task_key, tile) unit was walking toward as of its last call
committed = {}

stats = {
    "moves": 0, "works": 0, "passes": 0, "idle_drift": 0,
    "retarget": 0,       # target changed before arrival
    "continued": 0,      # kept walking toward the same target
    "new_commit": 0,     # had no prior commitment, picked a fresh target
    "arrived_worked": 0, # arrived (pos==target) and did the work action
}
retarget_examples = []
work_by_key = defaultdict(int)


def wrapped_unit_action(pos, tasks, seeds, day, task_order, unit_id=None, locked_tiles=frozenset()):
    idx = call_idx[0]
    call_idx[0] += 1

    before = {k: set(v) for k, v in tasks.items()}
    op = orig_unit_action(pos, tasks, seeds, day, task_order, unit_id=unit_id, locked_tiles=locked_tiles)
    after = {k: set(v) for k, v in tasks.items()}

    removed = None  # (task_key, tile)
    for k in before:
        diff = before[k] - after[k]
        if diff:
            removed = (k, next(iter(diff)))
            break

    verb_ops = {"WATER", "HARVEST", "DIG", "PLANT"}
    prior = committed.get(idx)

    if op and op[0] in verb_ops:
        stats["works"] += 1
        work_by_key[op[0]] += 1
        stats["arrived_worked"] += 1
        committed.pop(idx, None)
    elif op and op[0] == "PASS":
        stats["passes"] += 1
        committed.pop(idx, None)
    elif op:  # movement direction string, e.g. ["EAST"]
        stats["moves"] += 1
        if removed is None:
            # No task claimed at all -- idle drift toward shed fallback.
            stats["idle_drift"] += 1
            committed.pop(idx, None)
        else:
            key, tile = removed
            if prior is None:
                stats["new_commit"] += 1
            elif prior == (key, tile):
                stats["continued"] += 1
            else:
                stats["retarget"] += 1
                if len(retarget_examples) < 25:
                    retarget_examples.append({
                        "idx": idx, "day": cur_day[0], "hour": cur_hour[0],
                        "pos": pos, "prior": prior, "new": (key, tile),
                    })
            committed[idx] = (key, tile)
    else:
        committed.pop(idx, None)

    return op


def wrapped_agent(obs):
    call_idx[0] = 0
    cur_day[0] = obs.get("day")
    cur_hour[0] = obs.get("hour")
    return orig_agent(obs)


mod.unit_action = wrapped_unit_action
mod._agent = wrapped_agent

if __name__ == "__main__":
    from kaggle_environments import make

    opponent = sys.argv[1] if len(sys.argv) > 1 else "starter"
    turns = int(sys.argv[2]) if len(sys.argv) > 2 else 720
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else None

    env = make("kaggriculture", configuration={"episodeSteps": turns}, debug=True)
    if seed is not None:
        env.info = {"seed": seed}
    env.run([mod.agent, opponent])

    final = env.steps[-1]
    print(f"\n=== {turns} turns vs {opponent} ===")
    for i, s in enumerate(final):
        print(f"  Player {i}: reward={s.reward}, status={s.status}")

    total_calls = stats["moves"] + stats["works"] + stats["passes"]
    print(f"\n--- unit_action call breakdown ({total_calls} calls) ---")
    print(f"  moves : {stats['moves']:6d} ({100*stats['moves']/total_calls:.1f}%)")
    print(f"  works : {stats['works']:6d} ({100*stats['works']/total_calls:.1f}%)  breakdown: {dict(work_by_key)}")
    print(f"  passes: {stats['passes']:6d} ({100*stats['passes']/total_calls:.1f}%)")

    print(f"\n--- movement claim breakdown ({stats['moves']} moves) ---")
    print(f"  idle_drift (no task at all)      : {stats['idle_drift']:6d}")
    print(f"  new_commit (fresh target)        : {stats['new_commit']:6d}")
    print(f"  continued (same target as before): {stats['continued']:6d}")
    print(f"  retarget  (abandoned prior target): {stats['retarget']:6d}")
    denom = stats['new_commit'] + stats['continued'] + stats['retarget']
    if denom:
        print(f"  retarget rate among committed moves: {100*stats['retarget']/denom:.1f}%")

    print("\n--- sample retarget events ---")
    for e in retarget_examples[:15]:
        print(f"  day={e['day']:2d} hr={e['hour']:2d} slot={e['idx']} pos={e['pos']} "
              f"prior={e['prior']} -> new={e['new']}")
