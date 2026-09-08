#!/usr/bin/env python3
"""Recompute failure_profile for existing candidates under the current classify.RULES (AGE-332
follow-up). Needed whenever RULES thresholds are recalibrated (see evolve/calibrate_rules.py) --
without this, candidates classified before a recalibration keep their stale profile forever, since
cascade.py only classifies a candidate once, at the point it reaches that stage.

    python3 evolve/reclassify.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import db as db_mod  # noqa: E402
import classify as classify_mod  # noqa: E402


def reclassify_row(row):
    """Same precedence cascade.py itself uses: trajectory > exec_summary > pattern > none."""
    if row.get("trajectory_summary"):
        return classify_mod.classify_trajectory(json.loads(row["trajectory_summary"]), dev_margin=row.get("dev_margin"))
    if row.get("exec_summary"):
        return classify_mod.classify_from_exec_summary(json.loads(row["exec_summary"]), row.get("diagnosis") or "")
    if row.get("status") == "dead_pattern" and row.get("note"):
        return classify_mod.classify_from_pattern(row["note"])
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    db = db_mod.DB()
    rows = db.all()
    changed = 0
    for row in rows:
        new_profile = reclassify_row(row)
        if new_profile is None:
            continue
        old_raw = row.get("failure_profile")
        old_primary = json.loads(old_raw).get("primary_class") if old_raw else None
        new_raw = json.dumps(new_profile)
        if old_raw == new_raw:
            continue
        changed += 1
        note = f"{row['key']}: {old_primary} -> {new_profile.get('primary_class')}"
        print(("[dry-run] would update " if args.dry_run else "updated ") + note)
        if not args.dry_run:
            db.update(row["key"], failure_profile=new_raw)
    print(f"\n{changed}/{len(rows)} candidates {'would change' if args.dry_run else 'updated'}")


if __name__ == "__main__":
    main()
