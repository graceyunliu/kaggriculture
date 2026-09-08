#!/usr/bin/env python3
"""Calibration check for evolve/classify.py's RULES thresholds (AGE-332 follow-up).

The thresholds in RULES were picked from RULES.md's cross-codebase comparisons (our dispatcher
vs. the frontier opponent tapes -- a different codebase entirely). Applied *within* our own
candidate population, where every candidate shares the same chassis/dispatcher, an absolute
threshold borrowed from that comparison can end up true for 100% (or 0%) of candidates -- directionally
right but useless as a discriminator. This script checks, for each metric a RULES threshold reads,
whether it actually separates high-dev_margin candidates from low ones in the *current* DB population,
and reports the current threshold's fire rate + suggests a data-derived alternative.

    python3 evolve/calibrate_rules.py --frontier candidates/H32.py [--metric missed_water_total]

Read-only: does not modify RULES. Recalibration is a judgment call (see the printed correlation and
sample size before trusting a suggested threshold) -- apply changes to classify.py by hand.

IMPORTANT: dev_margin (and therefore any correlation/split computed here) is only comparable within
one yardstick -- always pass --frontier once the DB holds candidates scored against more than one
frontier (same reasoning as failure_report.py; check with `SELECT DISTINCT frontier FROM runs`).
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import db as db_mod  # noqa: E402
from classify import RULES  # noqa: E402


def _sum(series):
    return sum(v for v in (series or []) if v is not None)


def _final(series):
    vals = [v for v in (series or []) if v is not None]
    return vals[-1] if vals else None


def _window_mean(series, lo, hi):
    vals = [v for v in (series or [])[lo:hi + 1] if v is not None]
    return sum(vals) / len(vals) if vals else None


def _at(series, day):
    vals = series or []
    return vals[day] if day < len(vals) and vals[day] is not None else None


# metric name -> (extractor(summary) -> float|None, current threshold path in RULES, higher_is_worse)
METRICS = {
    "missed_water_total": (lambda s: _sum(s.get("missed_water")),
                            ("EXECUTION_FAILURE", "missed_water_total"), True),
    "missed_feed_total": (lambda s: _sum(s.get("missed_feed")),
                           ("EXECUTION_FAILURE", "missed_feed_total"), True),
    "chore_completion_ratio": (lambda s: (_sum(s.get("chores_completed")) / _sum(s.get("chores_enumerated")))
                                if _sum(s.get("chores_enumerated")) else None,
                                ("EXECUTION_FAILURE", "chore_completion_ratio"), False),
    "shed_units_final": (lambda s: _final(s.get("shed_units")),
                          ("MARKET_FAILURE", "shed_units_final_high"), True),
    "animals_d15": (lambda s: _at(s.get("animals"), 15),
                     ("CAPACITY_FAILURE", "animals_d15_low"), False),
    "plants_final": (lambda s: _final(s.get("plants")),
                      ("CAPACITY_FAILURE", "plants_final_low"), False),
    "work_turns_per_day_8_15": (lambda s: _window_mean(s.get("work_turns"), 8, 15),
                                 ("LABOR_FAILURE", "work_turns_per_day_max"), False),
    "idle_turns_per_day_8_15": (lambda s: _window_mean(s.get("idle_turns"), 8, 15),
                                 ("LABOR_FAILURE", "idle_turns_per_day"), True),
}


def load_population(db, frontier=None):
    q = "SELECT c.key, c.dev_margin, c.trajectory_summary FROM candidates c"
    args = []
    where = ["c.trajectory_summary IS NOT NULL", "c.dev_margin IS NOT NULL"]
    if frontier:
        q += " JOIN runs r ON r.run_id = c.run_id"
        where.append("r.frontier=?")
        args.append(frontier)
    q += " WHERE " + " AND ".join(where)
    rows = [dict(r) for r in db.conn.execute(q, args)]
    return [(r["key"], r["dev_margin"], json.loads(r["trajectory_summary"])) for r in rows]


def analyze(pop, metric_name):
    extract, (cls, key), higher_is_worse = METRICS[metric_name]
    current = RULES[cls][key]
    pairs = [(dm, extract(s)) for _, dm, s in pop if extract(s) is not None]
    if len(pairs) < 4:
        print(f"{metric_name}: only {len(pairs)} candidates with this metric, too few to calibrate")
        return
    vals = [v for _, v in pairs]
    mean_v, sd_v = statistics.mean(vals), statistics.stdev(vals) if len(vals) > 1 else 0.0
    fire_rate = sum(1 for v in vals if (v > current if higher_is_worse else v < current)) / len(vals)
    pairs.sort(key=lambda p: p[0])
    half = len(pairs) // 2
    bottom, top = pairs[:half], pairs[-half:]
    bottom_mean = statistics.mean(v for _, v in bottom)
    top_mean = statistics.mean(v for _, v in top)
    dms = [dm for dm, _ in pairs]
    mean_dm, sd_dm = statistics.mean(dms), statistics.stdev(dms) if len(dms) > 1 else 0.0
    corr = None
    if sd_dm > 0 and sd_v > 0:
        cov = sum((dm - mean_dm) * (v - mean_v) for dm, v in pairs) / len(pairs)
        corr = cov / (sd_dm * sd_v)
    print(f"\n{metric_name}  (n={len(pairs)}, current threshold={current}, higher_is_worse={higher_is_worse})")
    print(f"  population: min={min(vals):.2f} max={max(vals):.2f} mean={mean_v:.2f} stdev={sd_v:.2f}")
    print(f"  current threshold fires on {fire_rate*100:.0f}% of candidates"
          + ("  <-- non-discriminating (fires on everyone or no one)" if fire_rate in (0.0, 1.0) else ""))
    print(f"  bottom-half dev_margin mean {metric_name}: {bottom_mean:.2f}   top-half: {top_mean:.2f}")
    if corr is not None:
        expected_sign = -1 if higher_is_worse else 1
        ok = (corr < 0) == (expected_sign < 0)
        direction = "matches assumed rule direction" if ok else "OPPOSITE of assumed rule direction -- check before trusting this rule"
        print(f"  correlation(dev_margin, {metric_name}) = {corr:+.3f}  -- {direction}")
    # a threshold near the population mean gives roughly a 50/50 split -- a starting point, not gospel
    print(f"  suggested threshold (population mean): {mean_v:.0f}   suggested scale (population stdev): {sd_v:.0f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metric", default=None, choices=list(METRICS), help="check only this metric")
    ap.add_argument("--frontier", default=None, help="restrict to one yardstick (dev_margin isn't comparable across frontiers)")
    args = ap.parse_args()
    db = db_mod.DB()
    if not args.frontier:
        frontiers = [r["frontier"] for r in db.conn.execute("SELECT DISTINCT frontier FROM runs")]
        if len(frontiers) > 1:
            print(f"WARNING: {len(frontiers)} different frontiers in the DB -- pass --frontier to avoid mixing yardsticks.\n", file=sys.stderr)
    pop = load_population(db, frontier=args.frontier)
    print(f"population: {len(pop)} candidates with a trajectory_summary + dev_margin"
          + (f" (frontier={args.frontier})" if args.frontier else ""))
    for name in ([args.metric] if args.metric else METRICS):
        analyze(pop, name)


if __name__ == "__main__":
    main()
