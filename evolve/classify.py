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
    "EXECUTION_FAILURE": {"missed_water_total": 300, "missed_feed_total": 100,
                           "chore_completion_ratio": 0.7, "escapes_any": 0},
    "CAPITAL_FAILURE": {"cash_floor": 50, "cash_floor_days": 3, "cash_floor_window": (1, 8)},
    "LABOR_FAILURE": {"hands_min": 6, "work_turns_per_day_max": 40, "window": (8, 15),
                       "idle_turns_per_day": 40},
    "MARKET_FAILURE": {"shed_units_final_high": 60},
    "TIMING_FAILURE": {"land_purchase_late_day": 17, "first_sale_late_day": 12},
    "CAPACITY_FAILURE": {"animals_d15_low": 8, "plants_final_low": 30, "dev_margin_bad": -20000},
    "LAND_FAILURE": {"land_final_min": 3, "animals_d15_low": 8, "plants_final_low": 30},
}


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
        conf = max(conf, 0.85)
        evidence.append({"metric": "missed_water_total", "value": mw})
    if mf > r["missed_feed_total"]:
        conf = max(conf, 0.85)
        evidence.append({"metric": "missed_feed_total", "value": mf})
    if ratio < r["chore_completion_ratio"]:
        conf = max(conf, 0.6)
        evidence.append({"metric": "chore_completion_ratio", "value": round(ratio, 3)})
    if escapes > r["escapes_any"]:
        conf = max(conf, 0.4)
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
    evidence, conf = [], 0.0
    for d in range(lo, n):
        if (hands[d] or 0) >= r["hands_min"] and (work[d] or 0) < r["work_turns_per_day_max"]:
            conf = max(conf, 0.75)
            evidence.append({"day": d, "metric": "work_turns", "value": work[d], "hands": hands[d]})
        if (idle[d] or 0) > r["idle_turns_per_day"]:
            conf = max(conf, 0.5)
            evidence.append({"day": d, "metric": "idle_turns", "value": idle[d]})
    return ("LABOR_FAILURE", conf, evidence) if conf > 0 else None


def _rule_market(s, rules):
    r = rules["MARKET_FAILURE"]
    shed = _finite(s.get("shed_units"))
    if shed and shed[-1] > r["shed_units_final_high"]:
        return ("MARKET_FAILURE", 0.6, [{"day": s.get("n_days", len(shed)) - 1,
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
        conf = max(conf, 0.5)
        evidence.append({"day": 15, "metric": "animals", "value": animals_d15})
    if plants_final and plants_final[-1] < r["plants_final_low"]:
        conf = max(conf, 0.5)
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
        return ("LAND_FAILURE", 0.5, [{"metric": "land_final", "value": land_final[-1]},
                                       {"day": 15, "metric": "animals", "value": animals_d15},
                                       {"metric": "plants_final", "value": plants_final[-1]}])
    return None


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
    hits.sort(key=lambda h: h[1], reverse=True)
    classes = [{"class": c, "confidence": round(conf, 2), "evidence": ev} for c, conf, ev in hits]
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
    if (s.get("missed_water") or 0) > RULES["EXECUTION_FAILURE"]["missed_water_total"] or \
       (s.get("missed_feed") or 0) > RULES["EXECUTION_FAILURE"]["missed_feed_total"]:
        hits.append(("EXECUTION_FAILURE", 0.6, [{"metric": "missed_water", "value": s.get("missed_water")},
                                                  {"metric": "missed_feed", "value": s.get("missed_feed")}]))
    enum, comp = s.get("chores_enumerated") or 0, s.get("chores_completed") or 0
    if enum and comp / enum < RULES["EXECUTION_FAILURE"]["chore_completion_ratio"]:
        hits.append(("EXECUTION_FAILURE", 0.5, [{"metric": "chore_completion_ratio", "value": round(comp / enum, 3)}]))
    if s.get("idle_share", 0) > 0.25:
        hits.append(("LABOR_FAILURE", 0.4, [{"metric": "idle_share", "value": s.get("idle_share")}]))
    if s.get("max_animals", 99) < RULES["CAPACITY_FAILURE"]["animals_d15_low"]:
        hits.append(("CAPACITY_FAILURE", 0.35, [{"metric": "max_animals", "value": s.get("max_animals")}]))
    hits.sort(key=lambda h: h[1], reverse=True)
    classes = [{"class": c, "confidence": round(conf, 2), "evidence": ev} for c, conf, ev in hits]
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
