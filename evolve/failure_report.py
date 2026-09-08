#!/usr/bin/env python3
"""Population-wide failure taxonomy report (AGE-332).

Aggregates the `failure_profile` column across candidates: which failure class accounts for the
most dev_margin loss this run/island, weighted by classification confidence (classify_from_pattern
and classify_from_exec_summary are weaker signal than classify_trajectory -- see evolve/classify.py
-- so a raw count would overstate their share).

IMPORTANT: dev_margin is only comparable *within* one yardstick (same frontier) -- see db.py's own
comment on db.alive(). Without --frontier, this mixes candidates scored against different frontiers
(e.g. an old V3_12 run and a current H32 run) into one "total dev_margin loss" number, which is
meaningless -- always pass --frontier once more than one yardstick's worth of candidates exist in
the DB (list them with `SELECT DISTINCT frontier FROM runs`).

    python3 evolve/failure_report.py --frontier candidates/H32.py [--run RUN_ID] [--island c1]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "evolve"))
import db as db_mod  # noqa: E402


def collect(db, run_id=None, island=None, frontier=None):
    """Return list of (key, primary_class, confidence, dev_margin, island, source) for every
    candidate with a failure_profile. Pass `frontier` to restrict to one yardstick -- dev_margin
    is not comparable across different frontiers (see module docstring)."""
    q = "SELECT c.key, c.failure_profile, c.dev_margin, c.island FROM candidates c"
    args = []
    where = ["c.failure_profile IS NOT NULL"]
    if frontier:
        q += " JOIN runs r ON r.run_id = c.run_id"
        where.append("r.frontier=?")
        args.append(frontier)
    if run_id:
        where.append("c.run_id=?")
        args.append(run_id)
    if island:
        where.append("c.island=?")
        args.append(island)
    q += " WHERE " + " AND ".join(where)
    out = []
    for row in db.conn.execute(q, args):
        try:
            profile = json.loads(row["failure_profile"])
        except (TypeError, ValueError):
            continue
        cls = profile.get("primary_class")
        if not cls:
            continue
        conf = 0.0
        for c in profile.get("classes", []):
            if c["class"] == cls:
                conf = c.get("confidence", 0.0)
                break
        out.append((row["key"], cls, conf, row["dev_margin"], row["island"], profile.get("source")))
    return out


def aggregate(rows):
    """Group by primary_class: candidate count, confidence-weighted count, and summed dev_margin
    loss (only candidates with a negative dev_margin count as a "loss" for this class)."""
    agg = defaultdict(lambda: {"n": 0, "weighted_n": 0.0, "loss_sum": 0.0})
    total_loss = 0.0
    for key, cls, conf, dev_margin, island, source in rows:
        a = agg[cls]
        a["n"] += 1
        a["weighted_n"] += conf
        if dev_margin is not None and dev_margin < 0:
            a["loss_sum"] += -dev_margin
            total_loss += -dev_margin
    return agg, total_loss


def aggregate_by_island(rows):
    by_island = defaultdict(list)
    for r in rows:
        by_island[r[4] or "unknown"].append(r)
    return {island: aggregate(rs) for island, rs in by_island.items()}


def print_report(rows):
    if not rows:
        print("no candidates with a failure_profile yet.")
        return
    agg, total_loss = aggregate(rows)
    print(f"{len(rows)} classified candidates, {total_loss:,.0f} total dev_margin loss attributed.\n")
    for cls, a in sorted(agg.items(), key=lambda kv: kv[1]["loss_sum"], reverse=True):
        share = (a["loss_sum"] / total_loss * 100) if total_loss else 0.0
        print(f"  {cls:18s} {share:5.1f}% of dev margin loss  "
              f"({a['n']} candidates, confidence-weighted {a['weighted_n']:.1f})")
    print("\nby island:")
    for island, (iagg, iloss) in sorted(aggregate_by_island(rows).items()):
        top = max(iagg.items(), key=lambda kv: kv[1]["loss_sum"], default=(None, None))
        if top[0] is None:
            continue
        print(f"  {island:10s} largest class: {top[0]:18s} "
              f"({top[1]['loss_sum']:,.0f} loss, {top[1]['n']} candidates)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", dest="run_id", default=None)
    ap.add_argument("--island", default=None)
    ap.add_argument("--frontier", default=None,
                     help="restrict to one yardstick (dev_margin isn't comparable across frontiers)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    db = db_mod.DB()
    if not args.frontier:
        frontiers = [r["frontier"] for r in db.conn.execute("SELECT DISTINCT frontier FROM runs")]
        if len(frontiers) > 1:
            print(f"WARNING: {len(frontiers)} different frontiers in the DB ({', '.join(Path(f).name for f in frontiers if f)}) "
                  f"-- mixing their dev_margin into one total is meaningless. Pass --frontier to pick one.\n", file=sys.stderr)
    rows = collect(db, run_id=args.run_id, island=args.island, frontier=args.frontier)
    if args.json:
        agg, total_loss = aggregate(rows)
        print(json.dumps({"total_loss": total_loss, "n": len(rows),
                           "classes": {k: v for k, v in agg.items()}}, indent=2))
        return
    print_report(rows)


if __name__ == "__main__":
    main()
