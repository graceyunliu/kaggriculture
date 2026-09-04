#!/usr/bin/env python3
"""Measure hard-chore completion directly against the ladder engine.

Hard chores are snapshotted at hour 0 and identified by kind + board position:
  * FEED for every animal (the strict rule in SPEC section 4)
  * WATER for a plant already unwatered one day
  * WATER for MELON during the protected day-6 through day-10 yield window

Successful FEED/WATER operations are observed inside the engine action handler, so
hour-23 work is counted before the end-of-day refresh clears ``*_today`` fields.

Examples:
  python3 evolve/trace_chores.py candidates/P.py candidates/V3_12.py --seeds 1-5
  python3 evolve/trace_chores.py candidates/E1.py candidates/V3_12.py --seeds 1-5 --json
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}
WORK = {"PLANT", "WATER", "HARVEST", "FERTILIZE", "DIG", "BUILD_COOP", "BUILD_PASTURE",
        "FEED", "COLLECT_FERTILIZER", "CARE", "PLACE", "PICKUP", "DROP"}


def _tile_items(farm):
    for y, row in enumerate(farm["tiles"]):
        for x, tile in enumerate(row):
            if isinstance(tile, dict):
                yield (x, y), tile


def _hard_chores(farm, day):
    chores = set()
    for pos, tile in _tile_items(farm):
        if "animal" in tile:
            chores.add(("feed", pos))
        elif tile.get("kind") == "PLANT" and not tile.get("watered_today"):
            age = day - tile.get("planted_day", day)
            if tile.get("consecutive_unwatered", 0) >= 1:
                chores.add(("water", pos))
            elif tile.get("crop") == "MELON" and 6 <= age <= 10 and tile.get("yield_units", 0) < 6:
                chores.add(("water", pos))
    return chores


def run(agent_a, agent_b, seed, engine="master"):
    mod, defaults = me.load_engine(engine)
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(agent_a), me.load_agent(agent_b)]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for item in state:
        item.observation.step = 0

    days = [[], []]
    active = [None, None]
    errors = [0, 0]
    step = 0
    steps = int(cfg["episodeSteps"])
    original_apply = mod._apply_unit_action
    original_refresh_plants = mod._daily_refresh_plants
    farms_ref = [None]

    def logged_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity=100):
        pid = 0 if farm is farms_ref[0][0] else 1
        units = [tuple(farm["farmer"])] + [tuple(p) for p in farm["hands"]]
        pos = units[idx] if idx < len(units) else None
        verb = action[0] if isinstance(action, (list, tuple)) and action else "PASS"
        tile = farm["tiles"][pos[1]][pos[0]] if pos is not None else None
        before = None
        if verb == "FEED" and isinstance(tile, dict):
            before = tile.get("fed_today", False)
        elif verb == "WATER" and isinstance(tile, dict):
            before = tile.get("watered_today", False)
        original_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)
        if active[pid] is not None and pos is not None:
            after_tile = farm["tiles"][pos[1]][pos[0]]
            succeeded = (verb == "FEED" and not before and isinstance(after_tile, dict) and after_tile.get("fed_today")) or \
                        (verb == "WATER" and not before and isinstance(after_tile, dict) and after_tile.get("watered_today"))
            key = (verb.lower(), pos)
            if succeeded and key in active[pid]["enumerated"]:
                active[pid]["completed"].add(key)

    mod._apply_unit_action = logged_apply

    def logged_refresh_plants(farm, current_day, turns_per_day):
        pid = 0 if farm is farms_ref[0][0] else 1
        doomed = set()
        for pos, tile in _tile_items(farm):
            if tile.get("kind") == "PLANT" and not tile.get("watered_today") \
                    and tile.get("consecutive_unwatered", 0) + 1 >= 2:
                doomed.add(pos)
        original_refresh_plants(farm, current_day, turns_per_day)
        if active[pid] is not None:
            active[pid]["water_losses"].update(
                pos for pos in doomed
                if isinstance(farm["tiles"][pos[1]][pos[0]], dict)
                and farm["tiles"][pos[1]][pos[0]].get("kind") == "WEED")

    mod._daily_refresh_plants = logged_refresh_plants
    try:
        while True:
            obs0 = state[0].observation
            farms_ref[0] = obs0.farms
            day, hour = int(obs0.day), int(obs0.hour)
            if hour == 0:
                for pid in range(2):
                    chores = _hard_chores(obs0.farms[pid], day)
                    active[pid] = {"day": day, "enumerated": chores, "completed": set(),
                                   "animals_start": {p for p, t in _tile_items(obs0.farms[pid]) if "animal" in t},
                                   "plants_start": {p for p, t in _tile_items(obs0.farms[pid]) if t.get("kind") == "PLANT"},
                                   "water_losses": set(), "moves": 0, "work": 0}
            acts = []
            for pid in range(2):
                obs = copy.deepcopy(state[pid].observation)
                obs["step"] = step
                try:
                    act = agents[pid](obs, copy.deepcopy(env.configuration))
                except Exception:  # agent exceptions are part of the verdict
                    errors[pid] += 1
                    act = {}
                act = act if isinstance(act, dict) else {}
                state[pid].action = act
                acts.append(act)
                ops = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
                n_units = 1 + len(obs0.farms[pid]["hands"])
                for op in (ops + [["PASS"]] * n_units)[:n_units]:
                    verb = op[0] if isinstance(op, (list, tuple)) and op else "PASS"
                    if verb in MOVES:
                        active[pid]["moves"] += 1
                    elif verb in WORK:
                        active[pid]["work"] += 1
            closing_day = hour == int(cfg["turnsPerDay"]) - 1
            state = mod.interpreter(state, env)
            step += 1
            for item in state:
                item.observation.step = step
            if closing_day:
                for pid in range(2):
                    row = active[pid]
                    animals_after = {p for p, t in _tile_items(state[0].observation.farms[pid]) if "animal" in t}
                    weeds_after = {p for p, t in _tile_items(state[0].observation.farms[pid]) if t.get("kind") == "WEED"}
                    total = len(row["enumerated"])
                    completed = len(row["completed"])
                    days[pid].append({"day": row["day"], "hard_enumerated": total,
                                      "hard_completed": completed,
                                      "completion_rate": completed / total if total else 1.0,
                                      "escaped_animals": len(row["animals_start"] - animals_after),
                                      "crops_lost_to_missed_water": len(row["water_losses"]),
                                      "moves": row["moves"], "work_actions": row["work"],
                                      "travel_per_work": row["moves"] / row["work"] if row["work"] else 0.0})
            if all(item.status == "DONE" for item in state) or step >= steps:
                break
    finally:
        mod._apply_unit_action = original_apply
        mod._daily_refresh_plants = original_refresh_plants
    return {"seed": seed, "errors": errors, "players": days}


def summarize(runs, pid=0):
    rows = [row for run in runs for row in run["players"][pid]]
    enum = sum(r["hard_enumerated"] for r in rows)
    done = sum(r["hard_completed"] for r in rows)
    moves = sum(r["moves"] for r in rows)
    work = sum(r["work_actions"] for r in rows)
    return {"hard_enumerated": enum, "hard_completed": done,
            "completion_rate": done / enum if enum else 1.0,
            "escaped_animals": sum(r["escaped_animals"] for r in rows),
            "crops_lost_to_missed_water": sum(r["crops_lost_to_missed_water"] for r in rows),
            "moves": moves, "work_actions": work,
            "travel_per_work": moves / work if work else 0.0,
            "agent_errors": sum(run["errors"][pid] for run in runs)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a")
    ap.add_argument("b")
    ap.add_argument("--seeds", default="1-5", help="range (1-5) or comma list (1,3,5)")
    ap.add_argument("--engine", default="master")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--daily", action="store_true", help="print the evaluated agent's per-day rows")
    args = ap.parse_args()
    if "-" in args.seeds:
        lo, hi = (int(x) for x in args.seeds.split("-", 1))
        seeds = list(range(lo, hi + 1))
    else:
        seeds = [int(x) for x in args.seeds.split(",")]
    runs = [run(args.a, args.b, seed, args.engine) for seed in seeds]
    result = {"a": str(args.a), "b": str(args.b), "seeds": seeds,
              "a_summary": summarize(runs, 0), "b_summary": summarize(runs, 1), "runs": runs}
    if args.json:
        print(json.dumps(result, indent=2))
        return
    if args.daily:
        print("seed day hard done rate escapes water_loss travel/work")
        for item in runs:
            for row in item["players"][0]:
                print("%4d %3d %4d %4d %5.1f%% %7d %10d %11.2f" %
                      (item["seed"], row["day"], row["hard_enumerated"], row["hard_completed"],
                       100 * row["completion_rate"], row["escaped_animals"],
                       row["crops_lost_to_missed_water"], row["travel_per_work"]))
    for label, key in ((Path(args.a).name, "a_summary"), (Path(args.b).name, "b_summary")):
        s = result[key]
        print("%s: hard %d/%d (%.1f%%), escapes %d, water-loss weeds %d, travel/work %.2f, errors %d" %
              (label, s["hard_completed"], s["hard_enumerated"], 100 * s["completion_rate"],
               s["escaped_animals"], s["crops_lost_to_missed_water"], s["travel_per_work"], s["agent_errors"]))


if __name__ == "__main__":
    main()
