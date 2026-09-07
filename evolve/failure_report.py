#!/usr/bin/env python3
"""Population-wide failure taxonomy report (AGE-332).

Aggregates the `failure_profile` column across candidates: which failure class accounts for the
most dev_margin loss this run/island, weighted by classification confidence (classify_from_pattern
and classify_from_exec_summary are weaker signal than classify_trajectory -- see evolve/classify.py
-- so a raw count would overstate their share).

    python3 evolve/failure_report.py [--run RUN_ID] [--island c1]
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


def collect(db, run_id=None, island=None):
    """Return list of (key, primary_class, confidence, dev_margin, island, source) for every
    candidate with a failure_profile."""
    q = "SELECT key, failure_profile, dev_margin, island FROM candidates WHERE failure_profile IS NOT NULL"
    args = []
    if run_id:
        q += " AND run_id=?"
        args.append(run_id)
    if island:
        q += " AND island=?"
        args.append(island)
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
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    db = db_mod.DB()
    rows = collect(db, run_id=args.run_id, island=args.island)
    if args.json:
        agg, total_loss = aggregate(rows)
        print(json.dumps({"total_loss": total_loss, "n": len(rows),
                           "classes": {k: v for k, v in agg.items()}}, indent=2))
        return
    print_report(rows)


if __name__ == "__main__":
    main()
