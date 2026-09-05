#!/usr/bin/env python3
"""bench_day_dump.py -- side-by-side per-unit hourly (pos, action) dump for one ledger day,
tape vs candidate agent. Imports (does not copy/modify) run_candidate_day/load_ledger_days
from tools/planner_bench.py.

Usage:
  python3 tools/bench_day_dump.py candidates/P.py evolve/expert/H32_s1/ --day 23
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import mini_engine as me  # noqa: E402
import planner_bench as pb  # noqa: E402


def animal_tiles_visited_by_multiple(actions_by_unit):
    """Count distinct (x,y) animal-tile positions that >1 unit visited during the day."""
    from collections import defaultdict
    pos_units = defaultdict(set)
    for idx, entries in actions_by_unit.items():
        for entry in entries:
            hour, pos, action = entry[0], entry[1], entry[2]
            cid = entry[3] if len(entry) > 3 else None
            if pos is None:
                continue
            if cid and (cid.startswith("feed:") or cid.startswith("care:") or cid.startswith("harvest_animal:")):
                pos_units[tuple(pos)].add(idx)
    return {p: units for p, units in pos_units.items() if len(units) > 1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("ledger_dir")
    ap.add_argument("--day", type=int, required=True)
    a = ap.parse_args()

    mod, defaults = me.load_engine("master")
    days = pb.load_ledger_days(a.ledger_dir, str(a.day))
    if not days:
        print("day not found", file=sys.stderr)
        sys.exit(2)
    ld = days[0]

    cand_day = pb.run_candidate_day(a.agent, ld, mod, defaults)

    print(f"=== day {a.day}: tape vs {a.agent} ===\n")
    tape_units = sorted(ld["actions"].keys(), key=lambda k: int(k))
    cand_units = sorted(cand_day["actions"].keys())

    print("--- TAPE ---")
    for u in tape_units:
        entries = ld["actions"][u]
        line = " ".join(f"h{h}:{tuple(p) if p else p}:{act[0] if act else act}" for h, p, act, cid in entries)
        print(f"unit {u}: {line}")

    print("\n--- CANDIDATE ---")
    for u in cand_units:
        entries = cand_day["actions"][u]
        line = " ".join(f"h{h}:{tuple(p) if p else p}:{act[0] if act else act}" for h, p, act, cid in entries)
        print(f"unit {u}: {line}")

    tape_multi = animal_tiles_visited_by_multiple(ld["actions"])
    cand_multi = animal_tiles_visited_by_multiple(cand_day["actions"])
    print(f"\nanimal tiles visited by >1 unit -- tape: {len(tape_multi)} {list(tape_multi.keys())}")
    print(f"animal tiles visited by >1 unit -- candidate: {len(cand_multi)} {list(cand_multi.keys())}")


if __name__ == "__main__":
    main()
