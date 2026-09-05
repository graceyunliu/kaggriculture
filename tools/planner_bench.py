#!/usr/bin/env python3
"""planner_bench.py -- per-day planner test without full games, per
docs/SPEC-planner-from-tape.md section 3.

Usage:
  python3 tools/planner_bench.py candidates/P.py evolve/expert/H32_s1/ [--days 5-9] [--verbose]

For each ledger day: reconstructs an engine state from day_XX.json's state_h0 (seat 0 =
the tape's snapshot; seat 1 = a fresh empty farm, PASS every step), injects the tape's HIRE
orders at the same hours (hand count is controlled, same as the tape), runs 24 interpreter
steps with the candidate agent (a fresh module import per day), and scores coverage/travel/
idle/eod against the tape's ledger for that day.

Note on the RNG / seed check the spec asks for: kaggriculture's _end_of_day draws its RNG as
random.Random((seed * 1_000_003) ^ day) -- keyed only on (seed, day), not on cumulative game
history. So as long as env.info["seed"] is set to the ledger's seed (stored per-day by
tape_days.py) and state_h0 is reproduced exactly, end-of-day randomness (weed spawns, shop
unlocks) reproduces exactly for that one day, independent of how day 0..d-1 played out. This
is what makes the self-consistency check (3a) a real test of planner_bench's reconstruction,
not a coincidence.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402
import tape_days as td  # noqa: E402

MOVES = td.MOVES
LOGISTICS = td.LOGISTICS


def load_ledger_days(ledger_dir, day_spec):
    files = sorted(Path(ledger_dir).glob("day_*.json"))
    days = [json.load(open(f)) for f in files]
    if day_spec:
        if "-" in day_spec:
            lo, hi = (int(x) for x in day_spec.split("-"))
            days = [d for d in days if lo <= d["day"] <= hi]
        else:
            want = {int(x) for x in day_spec.split(",")}
            days = [d for d in days if d["day"] in want]
    return days


def build_state(mod, defaults, ledger_day, board_size=10):
    """Reconstruct a 2-seat engine state at hour 0 of this day from the ledger snapshot."""
    seed = ledger_day.get("seed", 1)
    day = ledger_day["day"]
    h0 = ledger_day["state_h0"]
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)

    farm0 = copy.deepcopy(h0["farm"])
    private0 = copy.deepcopy(h0["private"])
    farm1 = mod._new_farm(board_size, 3000)
    private1 = mod._new_private()
    market = copy.deepcopy(h0["market"])
    town = copy.deepcopy(h0["town"])

    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": day * 24}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    farms = [farm0, farm1]
    for i in range(2):
        obs = state[i].observation
        obs.farms = farms
        obs.market = market
        obs.town = town
        obs.day = day
        obs.hour = 0
        obs.player = i
        obs.private = private0 if i == 0 else private1
    return state, env, farms


def run_candidate_day(agent_path, ledger_day, mod, defaults, opponent_pass=True):
    state, env, farms = build_state(mod, defaults, ledger_day)
    agent = me.load_agent(agent_path)  # fresh module import -> clean module-level state
    farm0 = [farms[0]]
    hour_log = []
    orig_apply = mod._apply_unit_action
    orig_eod = mod._end_of_day
    eod_snapshot = {}

    def patched_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity=100):
        if farm is not farm0[0]:
            return orig_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)
        pos = None
        if idx == 0:
            pos = tuple(farm["farmer"])
        elif idx - 1 < len(farm["hands"]):
            pos = tuple(farm["hands"][idx - 1])
        tile_before = copy.deepcopy(farm["tiles"][pos[1]][pos[0]]) if pos else None
        inv_before = dict(private["inventories"][idx]) if idx < len(private["inventories"]) else {}
        orig_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)
        tile_after = farm["tiles"][pos[1]][pos[0]] if pos else None
        inv_after = private["inventories"][idx] if idx < len(private["inventories"]) else {}
        hour_log.append((idx, pos, list(action) if isinstance(action, list) else action,
                          tile_before, copy.deepcopy(tile_after), inv_before, dict(inv_after)))

    def patched_eod(state, env, day):
        farm = farm0[0]
        unfed = sum(1 for row in farm["tiles"] for t in row
                    if isinstance(t, dict) and "animal" in t and not t.get("fed_today"))
        unwatered = sum(1 for row in farm["tiles"] for t in row
                         if isinstance(t, dict) and t.get("kind") == "PLANT" and not t.get("watered_today"))
        eod_snapshot["stats"] = {"unfed": unfed, "unwatered_plants": unwatered}
        eod_snapshot["animals_before"] = sum(1 for row in farm["tiles"] for t in row
                                              if isinstance(t, dict) and "animal" in t)
        eod_snapshot["weeds_before"] = sum(1 for row in farm["tiles"] for t in row
                                            if isinstance(t, dict) and t.get("kind") == "WEED")
        return orig_eod(state, env, day)

    mod._apply_unit_action = patched_apply
    mod._end_of_day = patched_eod

    day = ledger_day["day"]
    hires_by_hour = {h: n for h, n in ledger_day.get("hands_hired", [])}
    cand_day = {"day": day, "actions": {}, "chores_done": {}, "market": [], "money": [], "shed": [],
                "failed": [], "hands_hired": []}
    limitation = None
    try:
        for hour in range(24):
            farm = farms[0]
            priv0 = state[0].observation.private
            cand_day["money"].append(farm["money"])
            cand_day["shed"].append(dict(priv0["shed"]))
            hands_before = len(farm["hands"])

            obs0 = me._fast_copy(state[0].observation)
            obs0["step"] = day * 24 + hour
            try:
                act0 = agent(obs0, me._fast_copy(env.configuration))
            except Exception:
                act0 = {}
            if not isinstance(act0, dict):
                act0 = {}
            mkt = [o for o in (act0.get("market") or []) if not (isinstance(o, list) and o and o[0] == "HIRE")]
            n_hire = hires_by_hour.get(hour, 0)
            mkt = (["HIRE"] * 0 + [["HIRE"]] * n_hire) + mkt
            mkt = mkt[:10]
            act0["market"] = mkt
            state[0].action = act0

            if opponent_pass:
                nhands1 = len(farms[1]["hands"])
                state[1].action = {"farmer": ["PASS"], "hands": [["PASS"]] * nhands1, "market": []}

            hour_log.clear()
            state = mod.interpreter(state, env)
            for s in state:
                s.observation.step = day * 24 + hour + 1

            hands_after = len(farms[0]["hands"])
            if hands_after > hands_before:
                cand_day["hands_hired"].append([hour, hands_after - hands_before])
            for o in mkt:
                cand_day["market"].append([hour, o])

            for idx, pos, action, tile_before, tile_after, inv_before, inv_after in hour_log:
                op = action[0] if isinstance(action, list) and action else None
                kind = td.classify(action, tile_before)
                cid = f"{kind}:{pos[0]},{pos[1]}" if (kind is not None and pos is not None) else None
                cand_day["actions"].setdefault(idx, []).append([hour, list(pos) if pos else None, action, cid])
                if kind is not None:
                    if td.action_done(mod, op, tile_before, tile_after, inv_before, inv_after):
                        cand_day["chores_done"].setdefault(cid, [hour, idx])
                    else:
                        cand_day["failed"].append([hour, idx, action, td.failure_reason(op, tile_before, inv_before)])
    finally:
        mod._apply_unit_action = orig_apply
        mod._end_of_day = orig_eod

    stats = eod_snapshot.get("stats", {"unfed": 0, "unwatered_plants": 0})
    cur_animals = sum(1 for row in farms[0]["tiles"] for t in row if isinstance(t, dict) and "animal" in t)
    cur_weeds = sum(1 for row in farms[0]["tiles"] for t in row if isinstance(t, dict) and t.get("kind") == "WEED")
    escaped = max(0, eod_snapshot.get("animals_before", cur_animals) - cur_animals)
    new_weeds = max(0, cur_weeds - eod_snapshot.get("weeds_before", cur_weeds))
    cand_day["eod"] = dict(stats, escaped=escaped, new_weeds=new_weeds)
    return cand_day


def score_day(tape_day, cand_day):
    hard = set(tape_day.get("chores_hard_h0", []))
    allc = set(tape_day.get("chores_available_h0", []))
    tape_done = set(tape_day["chores_done"].keys())
    cand_done = set(cand_day["chores_done"].keys())

    tape_hard_done = tape_done & hard
    cand_hard_done = cand_done & hard
    coverage_hard = (len(cand_hard_done) / len(tape_hard_done)) if tape_hard_done else 1.0

    tape_all_done = tape_done & allc
    cand_all_done = cand_done & allc
    coverage_all = (len(cand_all_done) / len(tape_all_done)) if tape_all_done else 1.0

    moves = work = idle = turns = 0
    for idx, acts in cand_day["actions"].items():
        for hour, pos, action, cid in acts:
            turns += 1
            op = action[0] if isinstance(action, list) and action else None
            if op == "PASS":
                idle += 1
            elif op in MOVES:
                moves += 1
            elif op in LOGISTICS:
                pass
            else:
                work += 1
    travel = moves / work if work else None
    idle_frac = idle / turns if turns else 0.0

    eod_delta = {}
    for k in ("escaped", "new_weeds", "unfed", "unwatered_plants"):
        eod_delta[k] = cand_day["eod"].get(k, 0) - tape_day["eod"].get(k, 0)

    missing_hard = sorted(tape_hard_done - cand_hard_done)
    missing_all = sorted(tape_all_done - cand_all_done)
    return {
        "day": tape_day["day"], "coverage_hard": coverage_hard, "coverage_all": coverage_all,
        "travel": travel, "idle": idle_frac, "eod_delta": eod_delta,
        "failed": len(cand_day["failed"]), "tape_hard_done": len(tape_hard_done),
        "cand_hard_done": len(cand_hard_done), "tape_all_done": len(tape_all_done),
        "cand_all_done": len(cand_all_done), "missing_hard": missing_hard, "missing_all": missing_all,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("ledger_dir")
    ap.add_argument("--days", default=None, help="e.g. 5-9 or 3,7,12")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    mod, defaults = me.load_engine("master")
    days = load_ledger_days(a.ledger_dir, a.days)
    if not days:
        print("no ledger days found", file=sys.stderr)
        sys.exit(2)

    print(f"planner_bench: {a.agent} vs ledger {a.ledger_dir} ({len(days)} days)")
    print("note: end-of-day RNG is keyed on (seed, day) only (kaggriculture._end_of_day), so "
          "per-day reconstruction from state_h0 reproduces exact end-of-day randomness "
          "independent of days 0..d-1 -- no known RNG limitation for this bench.")

    rows = []
    fail_day = False
    for ld in days:
        cand_day = run_candidate_day(a.agent, ld, mod, defaults)
        row = score_day(ld, cand_day)
        rows.append(row)
        if row["coverage_hard"] < 0.95 or row["eod_delta"]["new_weeds"] > 0:
            fail_day = True
        print(f"  day {row['day']:>2}: cov_hard={row['coverage_hard']:.2f} "
              f"({row['cand_hard_done']}/{row['tape_hard_done']})  cov_all={row['coverage_all']:.2f} "
              f"({row['cand_all_done']}/{row['tape_all_done']})  travel={row['travel']!s:>6}  "
              f"idle={row['idle']:.2f}  failed={row['failed']}  eod_delta={row['eod_delta']}")
        if a.verbose and row["missing_hard"]:
            tile_lookup = {}
            for y, rowt in enumerate(ld["state_h0"]["farm"]["tiles"]):
                for x, t in enumerate(rowt):
                    tile_lookup[f"{x},{y}"] = t
            print(f"    missing hard: {row['missing_hard']}")
            for cid in row["missing_hard"]:
                pos = cid.split(":", 1)[1]
                print(f"      {cid}: tile={tile_lookup.get(pos)}")

    n = len(rows)
    print(f"TOTAL over {n} days: mean cov_hard={sum(r['coverage_hard'] for r in rows)/n:.3f}  "
          f"mean cov_all={sum(r['coverage_all'] for r in rows)/n:.3f}  "
          f"total failed={sum(r['failed'] for r in rows)}  "
          f"total eod new_weeds delta={sum(r['eod_delta']['new_weeds'] for r in rows)}")
    sys.exit(1 if fail_day else 0)


if __name__ == "__main__":
    main()
