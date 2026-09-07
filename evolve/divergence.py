#!/usr/bin/env python3
"""Divergence detection over stored trajectory summaries (AGE-331).

Given two candidates' `trajectory_summary` rows (evaluated on the same frontier/seeds, see
cascade.TRAJ_SEEDS), find the first day their trajectories diverge and which metric led.

    python3 evolve/divergence.py --a KEY1 --b KEY2
    python3 evolve/divergence.py --a KEY1 --b KEY2 --json

Generalizes the day-walk in trace.diagnose() (which only looks at net worth, on raw per-seed
traces) to walk every field in the stored summary and report a leading indicator per metric.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "evolve"))
import db as db_mod  # noqa: E402
from trace import SUMMARY_FIELDS  # noqa: E402

# Fraction-of-scale threshold per metric before a gap counts as "diverged" (metric-specific because
# cash/sales live in dollars while hands/animals are small counts). Falls back to DEFAULT_FRAC.
DEFAULT_FRAC = 0.25
SCALE_FLOOR = {  # minimum absolute gap regardless of frac, so near-zero-scale metrics aren't noisy
    "cash": 500, "sales_rev": 200, "buys_cost": 200, "missed_feed": 2, "missed_water": 5,
    "escapes": 1, "hands": 1, "work_turns": 5, "travel_per_task": 0.3, "idle_turns": 5,
    "chores_enumerated": 3, "chores_completed": 3, "animals": 1, "plants": 2, "land": 1,
}


def _scale(a_vals, b_vals):
    vals = [abs(v) for v in a_vals + b_vals if v is not None]
    return max(vals) if vals else 0.0


def divergence(summary_a, summary_b, fields=None, frac=DEFAULT_FRAC, hold_days=3):
    """Walk day 0..min(n_days)-1 for each field; a field "diverges" on the first day its |a-b| gap
    exceeds max(frac*scale, SCALE_FLOOR[field]) and holds (same sign) for `hold_days` consecutive days.
    Returns {"divergence_day", "leading_indicator", "diverging_metrics": [{metric, day, gap, direction}]}."""
    fields = fields or SUMMARY_FIELDS
    n = min(summary_a.get("n_days", 0), summary_b.get("n_days", 0))
    diverging = []
    for f in fields:
        a_vals, b_vals = summary_a.get(f) or [], summary_b.get(f) or []
        if len(a_vals) < n or len(b_vals) < n:
            continue
        thresh = max(frac * _scale(a_vals[:n], b_vals[:n]), SCALE_FLOOR.get(f, 0))
        if thresh <= 0:
            continue
        gaps = [(a_vals[d] - b_vals[d]) if a_vals[d] is not None and b_vals[d] is not None else 0.0
                for d in range(n)]
        for d in range(n):
            window = gaps[d:d + hold_days]
            if len(window) < hold_days:
                break
            sign = 1 if gaps[d] > 0 else -1
            if all(sign * g >= thresh for g in window):
                diverging.append({"metric": f, "day": d, "gap": round(gaps[d], 2),
                                   "direction": "a_ahead" if sign > 0 else "b_ahead"})
                break
    diverging.sort(key=lambda x: x["day"])
    return {
        "divergence_day": diverging[0]["day"] if diverging else None,
        "leading_indicator": diverging[0]["metric"] if diverging else None,
        "diverging_metrics": diverging,
    }


def load_summary(db, key):
    row = db.get(key)
    if not row:
        raise SystemExit(f"no candidate with key {key!r}")
    raw = row.get("trajectory_summary")
    if not raw:
        raise SystemExit(f"candidate {key!r} has no trajectory_summary (not alive, or predates AGE-331)")
    return json.loads(raw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True, help="candidate key A")
    ap.add_argument("--b", required=True, help="candidate key B")
    ap.add_argument("--frac", type=float, default=DEFAULT_FRAC)
    ap.add_argument("--hold-days", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    db = db_mod.DB()
    sa, sb = load_summary(db, args.a), load_summary(db, args.b)
    res = divergence(sa, sb, frac=args.frac, hold_days=args.hold_days)
    if args.json:
        print(json.dumps(res, indent=2))
        return
    if res["divergence_day"] is None:
        print(f"{args.a} vs {args.b}: no sustained divergence found (frac={args.frac}, hold_days={args.hold_days}).")
    else:
        print(f"{args.a} vs {args.b}: diverge from day {res['divergence_day']}, "
              f"leading indicator = {res['leading_indicator']}")
        for m in res["diverging_metrics"]:
            print(f"  day {m['day']:>2}  {m['metric']:20s} gap {m['gap']:+,.2f}  ({m['direction']})")


if __name__ == "__main__":
    main()
