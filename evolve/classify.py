#!/usr/bin/env python3
"""Failure taxonomy (AGE-332): classify WHY a candidate lost, from data already computed by
AGE-331 (trajectory summaries) or by the earlier cascade stages (fingerprint / smoke diagnosis).

Three entry points, matching the three populations that reach different stages of the cascade:

    classify_trajectory(summary, dev_margin)      -- alive/held candidates, full per-day trajectory_summary
    classify_from_pattern(reason)                  -- dead_pattern candidates, one-line fingerprint reason
    classify_from_exec_summary(exec_summary, text) -- dead_smoke candidates, whole-game exec_summary only

No LLM, no new games: pure arithmetic over already-stored JSON. Thresholds live in RULES so they
can be retuned without touching the classification logic.

    python3 evolve/classify.py --key CANDIDATE_KEY [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "evolve"))

CLASSES = ("EXECUTION_FAILURE", "CAPITAL_FAILURE", "LABOR_FAILURE", "MARKET_FAILURE",
           "TIMING_FAILURE", "CAPACITY_FAILURE", "LAND_FAILURE")

RULES = {
    # Calibrated 2026-09-07 (evolve/calibrate_rules.py) against the first 23 candidates with a
    # trajectory_summary. The original missed_water_total/missed_feed_total/chore_completion_ratio
    # thresholds came from RULES.md's cross-codebase comparison (our dispatcher vs. the frontier
    # opponent tapes) and turned out to be non-discriminating *within* our own population (everyone
    # shares the same chassis): missed_water_total fired on 100% of candidates, missed_feed_total on
    # 0%. Reset to near the population mean so each rule actually separates candidates; re-run
    # calibrate_rules.py periodically as the population grows and adjust again.
    #   missed_water_total: corr(dev_margin, metric) = -0.37, direction confirmed correct.
    #   missed_feed_total:  corr = -0.77, the strongest signal available -- was completely inert before.
    #   chore_completion_ratio: corr = +0.63 (backwards from the assumed direction) but population
    #     spread was only 0.83-0.89 (n=23) -- too little variance/data to trust reversing the rule,
    #     so it's effectively disabled (threshold above the observed range) rather than flipped.
    "EXECUTION_FAILURE": {"missed_water_total": 400, "missed_feed_total": 7,
                           "chore_completion_ratio": 0.95, "escapes_any": 0},
    "CAPITAL_FAILURE": {"cash_floor": 50, "cash_floor_days": 3, "cash_floor_window": (1, 8)},
    "LABOR_FAILURE": {"hands_min": 6, "work_turns_per_day_max": 40, "window": (8, 15),
                       "idle_turns_per_day": 40},
    "MARKET_FAILURE": {"shed_units_final_high": 60},
    "TIMING_FAILURE": {"land_purchase_late_day": 17, "first_sale_late_day": 12},
    "CAPACITY_FAILURE": {"animals_d15_low": 8, "plants_final_low": 30, "dev_margin_bad": -20000},
    "LAND_FAILURE": {"land_final_min": 3, "animals_d15_low": 8, "plants_final_low": 30},
}

# Population reference stats for confidence scoring, calibrated 2026-09-07 (evolve/calibrate_rules.py
# --frontier candidates/H32.py, n=59 alive/held candidates with a trajectory_summary).
#
# WHY THIS EXISTS: before this, each rule's confidence was a fixed constant hand-picked when the rule
# was written (e.g. EXECUTION_FAILURE's missed_water/missed_feed hits capped at 0.85, CAPACITY_FAILURE
# and LABOR_FAILURE capped at 0.5). Since primary_class = whichever class has the highest confidence,
# EXECUTION_FAILURE structurally won almost every comparison it was even a candidate in, regardless of
# which class actually explained more of that specific candidate's loss -- confirmed on the live H32
# population: 100% of 130 classified candidates had EXECUTION_FAILURE as primary_class, even though
# CAPACITY_FAILURE fired as a *secondary* class on 58 of them and could plausibly have been primary for
# some. Confidence is now scored as a z-score against these population stats (how many stdevs from the
# mean, in the "worse" direction) so severity is expressed in the same units across every class.
#
# CAVEAT (report honestly, don't hide): against H32 specifically, every one of these correlations with
# dev_margin is WEAK (|r| < 0.3, several are +0.13 to +0.28 in the "wrong" direction on n=59) -- see
# evolve/calibrate_rules.py's raw output. That's because H32 beats every candidate in this population
# decisively and fairly uniformly (dev_margin -27k to -46k), so there is little true variance left to
# correlate against; none of these 8 metrics currently explains "why did THIS candidate lose more than
# THAT one" against H32. This calibration fixes the *comparability* bug (item 1); it does not manufacture
# a real per-candidate discriminating signal where the population itself is too homogeneous to have one
# yet. Re-run calibrate_rules.py once dev_margin has real spread again (e.g. against a weaker/mixed
# opponent, or once some candidates start closing the gap) and update these stats.
POPULATION_STATS = {
    # metric: (mean, stdev, higher_is_worse)
    "missed_water_total": (375.3, 27.1, True),
    "missed_feed_total": (3.9, 1.7, True),
    "animals_d15": (11.2, 1.2, False),
    "plants_final": (20.7, 4.8, False),
    "work_turns_per_day_8_15": (80.7, 3.6, False),
    "idle_turns_per_day_8_15": (12.0, 4.3, True),
    "shed_units_final": (40.7, 6.8, True),
}


def _z_confidence(value, metric, floor=0.3, ceiling=0.9, per_sigma=0.25):
    """Confidence in [floor, ceiling], scaled by how many population stdevs `value` is from the mean
    in the "worse" direction (0 stdev -> floor, 2+ stdevs -> near ceiling). Comparable across every
    rule that uses it, unlike a hand-picked constant. Falls back to `floor` if the metric has no
    calibration or zero variance."""
    stats = POPULATION_STATS.get(metric)
    if not stats or value is None:
        return floor
    mean, sd, higher_is_worse = stats
    if sd <= 0:
        return floor
    z = (value - mean) / sd if higher_is_worse else (mean - value) / sd
    return max(floor, min(ceiling, floor + max(0.0, z) * per_sigma))


def _sum(series):
    return sum(v for v in (series or []) if v is not None)


def _at(series, day, default=None):
    if not series or day is None or day >= len(series):
        return default
    v = series[day]
    return default if v is None else v


def _finite(series):
    return [v for v in (series or []) if v is not None]


# --------------------------------------------------------------------------- full trajectory rules
def _rule_execution(s, rules):
    r = rules["EXECUTION_FAILURE"]
    mw, mf = _sum(s.get("missed_water")), _sum(s.get("missed_feed"))
    enum, comp = _sum(s.get("chores_enumerated")), _sum(s.get("chores_completed"))
    ratio = comp / enum if enum else 1.0
    escapes = _sum(s.get("escapes"))
    evidence, conf = [], 0.0
    if mw > r["missed_water_total"]:
        conf = max(conf, _z_confidence(mw, "missed_water_total"))
        evidence.append({"metric": "missed_water_total", "value": mw})
    if mf > r["missed_feed_total"]:
        conf = max(conf, _z_confidence(mf, "missed_feed_total"))
        evidence.append({"metric": "missed_feed_total", "value": mf})
    if ratio < r["chore_completion_ratio"]:
        # no reliable population stats for this metric yet (near-zero observed spread) -- fixed floor
        conf = max(conf, 0.3)
        evidence.append({"metric": "chore_completion_ratio", "value": round(ratio, 3)})
    if escapes > r["escapes_any"]:
        conf = max(conf, 0.3)
        evidence.append({"metric": "escapes_total", "value": escapes})
    return ("EXECUTION_FAILURE", conf, evidence) if conf > 0 else None


def _rule_capital(s, rules):
    r = rules["CAPITAL_FAILURE"]
    lo, hi = r["cash_floor_window"]
    cash = s.get("cash") or []
    days_low = [d for d in range(lo, min(hi + 1, len(cash))) if (cash[d] or 0) < r["cash_floor"]]
    if len(days_low) >= r["cash_floor_days"]:
        return ("CAPITAL_FAILURE", 0.8,
                [{"day": d, "metric": "cash", "value": cash[d]} for d in days_low])
    return None


def _rule_labor(s, rules):
    r = rules["LABOR_FAILURE"]
    lo, hi = r["window"]
    hands, work, idle = s.get("hands") or [], s.get("work_turns") or [], s.get("idle_turns") or []
    n = min(len(hands), len(work), len(idle), hi + 1)
    window_work = [work[d] for d in range(lo, n) if work[d] is not None]
    window_idle = [idle[d] for d in range(lo, n) if idle[d] is not None]
    mean_work = sum(window_work) / len(window_work) if window_work else None
    mean_idle = sum(window_idle) / len(window_idle) if window_idle else None
    evidence, conf = [], 0.0
    for d in range(lo, n):
        if (hands[d] or 0) >= r["hands_min"] and (work[d] or 0) < r["work_turns_per_day_max"]:
            conf = max(conf, _z_confidence(mean_work, "work_turns_per_day_8_15"))
            evidence.append({"day": d, "metric": "work_turns", "value": work[d], "hands": hands[d]})
        if (idle[d] or 0) > r["idle_turns_per_day"]:
            conf = max(conf, _z_confidence(mean_idle, "idle_turns_per_day_8_15"))
            evidence.append({"day": d, "metric": "idle_turns", "value": idle[d]})
    return ("LABOR_FAILURE", conf, evidence) if conf > 0 else None


def _rule_market(s, rules):
    r = rules["MARKET_FAILURE"]
    shed = _finite(s.get("shed_units"))
    if shed and shed[-1] > r["shed_units_final_high"]:
        conf = _z_confidence(shed[-1], "shed_units_final")
        return ("MARKET_FAILURE", conf, [{"day": s.get("n_days", len(shed)) - 1,
                                           "metric": "shed_units_final", "value": shed[-1]}])
    return None


def _first_day_above(series, thresh):
    for d, v in enumerate(series or []):
        if v is not None and v > thresh:
            return d
    return None


def _first_increase_day(series):
    series = series or []
    for d in range(1, len(series)):
        if (series[d] or 0) > (series[d - 1] or 0):
            return d
    return None


def _rule_timing(s, rules):
    r = rules["TIMING_FAILURE"]
    evidence, conf = [], 0.0
    land_day = _first_increase_day(s.get("land"))
    if land_day is not None and land_day > r["land_purchase_late_day"]:
        conf = max(conf, 0.5)
        evidence.append({"day": land_day, "metric": "land_purchase_day", "value": land_day})
    sale_day = _first_day_above(s.get("sales_rev"), 0)
    if sale_day is not None and sale_day > r["first_sale_late_day"]:
        conf = max(conf, 0.5)
        evidence.append({"day": sale_day, "metric": "first_sale_day", "value": sale_day})
    return ("TIMING_FAILURE", conf, evidence) if conf > 0 else None


def _rule_capacity(s, rules, dev_margin):
    r = rules["CAPACITY_FAILURE"]
    if dev_margin is None or dev_margin >= r["dev_margin_bad"]:
        return None
    animals_d15 = _at(s.get("animals"), 15)
    plants_final = _finite(s.get("plants"))
    evidence, conf = [], 0.0
    if animals_d15 is not None and animals_d15 < r["animals_d15_low"]:
        conf = max(conf, _z_confidence(animals_d15, "animals_d15"))
        evidence.append({"day": 15, "metric": "animals", "value": animals_d15})
    if plants_final and plants_final[-1] < r["plants_final_low"]:
        conf = max(conf, _z_confidence(plants_final[-1], "plants_final"))
        evidence.append({"metric": "plants_final", "value": plants_final[-1]})
    return ("CAPACITY_FAILURE", conf, evidence) if conf > 0 else None


def _rule_land(s, rules):
    r = rules["LAND_FAILURE"]
    land_final = _finite(s.get("land"))
    animals_d15 = _at(s.get("animals"), 15)
    plants_final = _finite(s.get("plants"))
    if not land_final or land_final[-1] < r["land_final_min"]:
        return None
    if (animals_d15 is not None and animals_d15 < r["animals_d15_low"]) and \
       (plants_final and plants_final[-1] < r["plants_final_low"]):
        conf = max(_z_confidence(animals_d15, "animals_d15"), _z_confidence(plants_final[-1], "plants_final"))
        return ("LAND_FAILURE", conf, [{"metric": "land_final", "value": land_final[-1]},
                                        {"day": 15, "metric": "animals", "value": animals_d15},
                                        {"metric": "plants_final", "value": plants_final[-1]}])
    return None


def _merge_and_rank(hits):
    """Merge (class, confidence, evidence) tuples that share a class into one entry (max confidence,
    combined evidence), then sort by confidence descending. Fixes classify_from_exec_summary's
    previous behavior of emitting two separate EXECUTION_FAILURE entries when both its sub-checks fired."""
    by_class = {}
    for cls, conf, evidence in hits:
        if cls not in by_class or conf > by_class[cls][0]:
            by_class[cls] = (conf, by_class.get(cls, (0.0, []))[1] + evidence)
        else:
            by_class[cls] = (by_class[cls][0], by_class[cls][1] + evidence)
    merged = [(cls, conf, ev) for cls, (conf, ev) in by_class.items()]
    merged.sort(key=lambda h: h[1], reverse=True)
    return [{"class": c, "confidence": round(conf, 2), "evidence": ev} for c, conf, ev in merged]


_TRAJECTORY_RULES = (_rule_execution, _rule_capital, _rule_labor, _rule_market, _rule_timing)


def classify_trajectory(summary, dev_margin=None, rules=RULES):
    """Full per-day classification for a candidate with an AGE-331 trajectory_summary.
    Returns {"primary_class", "classes": [{"class","confidence","evidence"}], "notes"}."""
    hits = []
    for fn in _TRAJECTORY_RULES:
        r = fn(summary, rules)
        if r:
            hits.append(r)
    r = _rule_capacity(summary, rules, dev_margin)
    if r:
        hits.append(r)
    r = _rule_land(summary, rules)
    if r:
        hits.append(r)
    classes = _merge_and_rank(hits)
    return {
        "primary_class": classes[0]["class"] if classes else None,
        "classes": classes,
        "notes": "ranked by confidence (v1 heuristic, not a dev_margin decomposition)"
                 if classes else "no rule fired against current thresholds",
        "source": "trajectory",
    }


# --------------------------------------------------------------------------- reduced-confidence entry points
_PATTERN_TO_CLASS = (
    (re.compile(r"animal escaped"), "EXECUTION_FAILURE"),
    (re.compile(r"weeds created"), "EXECUTION_FAILURE"),
    (re.compile(r"cash trap"), "CAPITAL_FAILURE"),
)


def classify_from_pattern(reason):
    """Classification from cascade.pattern_death_reason()'s one-line string (dead_pattern candidates
    -- died before any trace.py game ran). Single-signal, so confidence is capped at 0.5."""
    if not reason:
        return {"primary_class": None, "classes": [], "notes": "no pattern-death reason given", "source": "pattern"}
    for pat, cls in _PATTERN_TO_CLASS:
        if pat.search(reason):
            return {"primary_class": cls,
                     "classes": [{"class": cls, "confidence": 0.5, "evidence": [{"metric": "pattern_death_reason", "value": reason}]}],
                     "notes": "single fingerprint-trace signal, not a full trajectory", "source": "pattern"}
    return {"primary_class": None, "classes": [], "notes": f"unrecognized pattern-death reason: {reason!r}", "source": "pattern"}


def classify_from_exec_summary(exec_summary, diagnosis_text=""):
    """Coarser classification from trace.summary_row()'s whole-game totals (dead_smoke candidates
    with cfg['reference'] set -- one seed, no per-day data). Confidence capped at 0.6."""
    if not exec_summary:
        return {"primary_class": None, "classes": [], "notes": "no exec_summary available", "source": "exec_summary"}
    s = exec_summary
    hits = []
    mw, mf = s.get("missed_water") or 0, s.get("missed_feed") or 0
    if mw > RULES["EXECUTION_FAILURE"]["missed_water_total"] or mf > RULES["EXECUTION_FAILURE"]["missed_feed_total"]:
        # same population stats as classify_trajectory (missed_water/missed_feed are whole-game sums
        # in both places, so the z-score is on the same scale) -- capped a touch lower (0.8 ceiling)
        # since this is one seed, not the 5-seed average classify_trajectory uses.
        conf = max(_z_confidence(mw, "missed_water_total", ceiling=0.8),
                   _z_confidence(mf, "missed_feed_total", ceiling=0.8))
        hits.append(("EXECUTION_FAILURE", conf, [{"metric": "missed_water", "value": s.get("missed_water")},
                                                    {"metric": "missed_feed", "value": s.get("missed_feed")}]))
    enum, comp = s.get("chores_enumerated") or 0, s.get("chores_completed") or 0
    if enum and comp / enum < RULES["EXECUTION_FAILURE"]["chore_completion_ratio"]:
        hits.append(("EXECUTION_FAILURE", 0.3, [{"metric": "chore_completion_ratio", "value": round(comp / enum, 3)}]))
    if s.get("idle_share", 0) > 0.25:
        hits.append(("LABOR_FAILURE", 0.4, [{"metric": "idle_share", "value": s.get("idle_share")}]))
    if s.get("max_animals", 99) < RULES["CAPACITY_FAILURE"]["animals_d15_low"]:
        hits.append(("CAPACITY_FAILURE", _z_confidence(s.get("max_animals"), "animals_d15", ceiling=0.8),
                     [{"metric": "max_animals", "value": s.get("max_animals")}]))
    classes = _merge_and_rank(hits)
    return {
        "primary_class": classes[0]["class"] if classes else None,
        "classes": classes,
        "notes": ("whole-game totals only, one seed" + (f"; diagnosis: {diagnosis_text[:160]}" if diagnosis_text else ""))
                 if classes else "no rule fired against whole-game totals",
        "source": "exec_summary",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    import db as db_mod
    db = db_mod.DB()
    row = db.get(args.key)
    if not row:
        raise SystemExit(f"no candidate with key {args.key!r}")
    if row.get("trajectory_summary"):
        profile = classify_trajectory(json.loads(row["trajectory_summary"]), dev_margin=row.get("dev_margin"))
    elif row.get("exec_summary"):
        profile = classify_from_exec_summary(json.loads(row["exec_summary"]), row.get("diagnosis") or "")
    elif row.get("status") == "dead_pattern":
        profile = classify_from_pattern(row.get("note"))
    else:
        profile = {"primary_class": None, "classes": [], "notes": "no trace data available for this candidate", "source": "none"}
    if args.json:
        print(json.dumps(profile, indent=2))
    else:
        print(f"{args.key}: primary_class={profile['primary_class']} ({profile['source']})")
        for c in profile["classes"]:
            print(f"  {c['class']:18s} conf={c['confidence']}  evidence={c['evidence'][:2]}")


if __name__ == "__main__":
    main()
