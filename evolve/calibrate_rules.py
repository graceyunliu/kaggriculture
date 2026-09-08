#!/usr/bin/env python3
"""Calibration check for evolve/classify.py's RULES thresholds (AGE-332 follow-up).

The thresholds in RULES were picked from RULES.md's cross-codebase comparisons (our dispatcher
vs. the frontier opponent tapes -- a different codebase entirely). Applied *within* our own
candidate population, where every candidate shares the same chassis/dispatcher, an absolute
threshold borrowed from that comparison can end up true for 100% (or 0%) of candidates -- directionally
right but useless as a discriminator. This script checks, for each metric a RULES threshold reads,
whether it actually separates high-dev_margin candidates from low ones in the *current* DB population,
and reports the current threshold's fire rate + suggests a data-derived alternative.

    python3 evolve/calibrate_rules.py [--metric missed_water_total]

Read-only: does not modify RULES. Recalibration is a judgment call (see the printed correlation and
sample size before trusting a suggested threshold) -- apply changes to classify.py by hand.
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


# metric name -> (extractor(summary) -> float|None, current threshold path in RULES)
METRICS = {
    "missed_water_total": (lambda s: _sum(s.get("missed_water")),
                            ("EXECUTION_FAILURE", "missed_water_total")),
    "missed_feed_total": (lambda s: _sum(s.get("missed_feed")),
                           ("EXECUTION_FAILURE", "missed_feed_total")),
    "chore_completion_ratio": (lambda s: (_sum(s.get("chores_completed")) / _sum(s.get("chores_enumerated")))
                                if _sum(s.get("chores_enumerated")) else None,
                                ("EXECUTION_FAILURE", "chore_completion_ratio")),
    "shed_units_final": (lambda s: _final(s.get("shed_units")),
                          ("MARKET_FAILURE", "shed_units_final_high")),
}


def load_population(db):
    rows = [dict(r) for r in db.conn.execute(
        "SELECT key, dev_margin, trajectory_summary FROM candidates "
        "WHERE trajectory_summary IS NOT NULL AND dev_margin IS NOT NULL")]
    return [(r["key"], r["dev_margin"], json.loads(r["trajectory_summary"])) for r in rows]


def analyze(pop, metric_name):
    extract, (cls, key) = METRICS[metric_name]
    current = RULES[cls][key]
    pairs = [(dm, extract(s)) for _, dm, s in pop if extract(s) is not None]
    if len(pairs) < 4:
        print(f"{metric_name}: only {len(pairs)} candidates with this metric, too few to calibrate")
        return
    vals = [v for _, v in pairs]
    mean_v, sd_v = statistics.mean(vals), statistics.stdev(vals) if len(vals) > 1 else 0.0
    fire_rate = sum(1 for v in vals if v > current) / len(vals)
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
    print(f"\n{metric_name}  (n={len(pairs)}, current threshold={current})")
    print(f"  population: min={min(vals):.2f} max={max(vals):.2f} mean={mean_v:.2f} stdev={sd_v:.2f}")
    print(f"  current threshold fires on {fire_rate*100:.0f}% of candidates"
          + ("  <-- non-discriminating (fires on everyone or no one)" if fire_rate in (0.0, 1.0) else ""))
    print(f"  bottom-half dev_margin mean {metric_name}: {bottom_mean:.2f}   top-half: {top_mean:.2f}")
    if corr is not None:
        direction = "higher values correlate with worse dev_margin (rule direction OK)" if corr < 0 \
            else "higher values correlate with BETTER dev_margin (rule direction may be backwards for this population)"
        print(f"  correlation(dev_margin, {metric_name}) = {corr:+.3f}  -- {direction}")
    # a threshold near the population mean gives roughly a 50/50 split -- a starting point, not gospel
    print(f"  suggested threshold (population mean): {mean_v:.0f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metric", default=None, choices=list(METRICS), help="check only this metric")
    args = ap.parse_args()
    db = db_mod.DB()
    pop = load_population(db)
    print(f"population: {len(pop)} candidates with a trajectory_summary + dev_margin")
    for name in ([args.metric] if args.metric else METRICS):
        analyze(pop, name)


if __name__ == "__main__":
    main()
