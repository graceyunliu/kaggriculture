#!/usr/bin/env python3
"""Diagnostic trace for main_v7.15.py's unit_action scheduler (round 2:
priority-preemptible locking).

Adapted from trace_v713_movement.py. Same before/after diff-of-`tasks`
instrumentation to measure move/work/pass split and retarget rate, PLUS a
new metric round 1 didn't have: time-to-first-response for urgent_water
tasks specifically, since that's the exact thing v7.13's unconditional
locking broke (urgent work sitting unaddressed behind a low-priority lock).

"Response" = the turn a tile is first CLAIMED by some unit_action call
(i.e. it disappears from the live `tasks["urgent_water"]` set as an
immediate on-tile action or as a fresh/continued movement target) counted
from the turn it was first observed pending in `tasks["urgent_water"]`.
Turn granularity is one global counter incremented per _agent() call (one
per game hour), not day/hour wall time, so it's robust to day rollovers.
"""
import importlib.util
import sys
from collections import defaultdict

MOD_PATH = sys.argv[4] if len(sys.argv) > 4 else "main_v7.15.py"

spec = importlib.util.spec_from_file_location("main_v715_trace", MOD_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

orig_unit_action = mod.unit_action
orig_agent = mod._agent

call_idx = [0]
cur_day = [0]
cur_hour = [0]
turn_counter = [0]

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

# --- urgent_water response-time tracking ---
pending_urgent_since = {}   # tile -> turn first observed pending
urgent_response_times = []  # list of turns-elapsed-until-claimed
urgent_still_pending_at_end = {}


def _track_urgent_appearance(tasks):
    uw = tasks.get("urgent_water", ())
    t = turn_counter[0]
    for tile in uw:
        if tile not in pending_urgent_since:
            pending_urgent_since[tile] = t


def wrapped_unit_action(pos, tasks, seeds, day, task_order, unit_id=None, locked_tiles=frozenset()):
    idx = call_idx[0]
    call_idx[0] += 1

    _track_urgent_appearance(tasks)
    before = {k: set(v) for k, v in tasks.items()}
    op = orig_unit_action(pos, tasks, seeds, day, task_order, unit_id=unit_id, locked_tiles=locked_tiles)
    after = {k: set(v) for k, v in tasks.items()}

    removed = None  # (task_key, tile)
    for k in before:
        diff = before[k] - after[k]
        if diff:
            removed = (k, next(iter(diff)))
            break

    if removed is not None and removed[0] == "urgent_water":
        tile = removed[1]
        start = pending_urgent_since.pop(tile, None)
        if start is not None:
            urgent_response_times.append(turn_counter[0] - start)

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
    turn_counter[0] += 1
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
    print(f"\n=== {turns} turns vs {opponent} (module={MOD_PATH}) ===")
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

    print(f"\n--- urgent_water time-to-first-response ({len(urgent_response_times)} tiles claimed) ---")
    if urgent_response_times:
        rt = sorted(urgent_response_times)
        n = len(rt)
        mean_rt = sum(rt) / n
        p50 = rt[n // 2]
        p90 = rt[int(n * 0.9)] if n > 1 else rt[0]
        print(f"  mean turns-to-claim: {mean_rt:.2f}   median: {p50}   p90: {p90}   max: {max(rt)}")
        dist = defaultdict(int)
        for v in rt:
            dist[v] += 1
        print(f"  distribution (turns_elapsed: count): {dict(sorted(dist.items()))}")
    else:
        print("  (no urgent_water tiles were ever claimed -- check instrumentation)")
    print(f"  still-pending-unclaimed at match end: {len(pending_urgent_since)}")
    if pending_urgent_since:
        still_ages = [turn_counter[0] - t for t in pending_urgent_since.values()]
        print(f"  their ages at end (turns pending): min={min(still_ages)} max={max(still_ages)} mean={sum(still_ages)/len(still_ages):.1f}")
