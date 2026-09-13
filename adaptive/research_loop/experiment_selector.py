"""
experiment_selector.py -- Adaptive Research Loop v0.1

Simple, explainable next-experiment heuristic (spec requirement 6: "simple
decision procedure", not an elaborate Bayesian optimizer). Scores each
candidate next-experiment on five factors, each 0-2, and returns the ranked
list plus the reasoning -- so the choice is auditable, not a black box.

Factors (each scored 0/1/2, higher = more attractive to test next):
  information_value    -- how much would resolving this teach us
  low_cost             -- 2 = no code change / reuses existing artifact,
                           1 = single small, isolable change, 0 = broad/costly
  isolable             -- 2 = change affects exactly one mechanism, cleanly
                           separable from other hypotheses' effects
  not_already_tested   -- 2 = NEW/no evidence yet, 1 = tested once (WEAK),
                           0 = already MODERATE/STRONG evidence either way
  avoids_local_optimum -- 2 = this hypothesis has NOT been the basis of the
                           last accepted change (guards against spec req 13)

total = sum of the five factors (max 10). Ties broken by next_test_priority
already recorded on the hypothesis.
"""
from __future__ import annotations

from typing import Optional

import hypothesis_store as hs
import experiment_ledger as el


def _last_change_hypothesis():
    rows = el.effective_rows()
    if not rows:
        return None
    rows_with_ts = [r for r in rows if r.get("submission_timestamp")]
    rows_sorted = sorted(rows_with_ts or rows,
                          key=lambda r: r.get("submission_timestamp") or "")
    return rows_sorted[-1].get("hypothesis_id") if rows_sorted else None


def score_hypothesis(h: dict, *, last_change_hypothesis, candidate_exists: bool) -> dict:
    status = h["status"]
    confidence = h["confidence"]

    if status == "REJECTED":
        information_value = 0
    elif confidence == "STRONG":
        information_value = 0
    elif status in ("NEW", "ACTIVE"):
        information_value = 2
    else:
        information_value = 1

    if candidate_exists:
        low_cost = 2
    elif h["hypothesis_id"] == "H_RATING":
        low_cost = 2
    elif h["hypothesis_id"] in ("H1",):
        low_cost = 2
    elif h["hypothesis_id"] in ("H3",):
        low_cost = 0
    else:
        low_cost = 1

    isolable = 2 if h["hypothesis_id"] in ("H_RATING", "H1", "H5") else 1

    if confidence == "NO_EVIDENCE":
        not_already_tested = 2
    elif confidence == "WEAK":
        not_already_tested = 1
    else:
        not_already_tested = 0

    avoids_local_optimum = 0 if h["hypothesis_id"] == last_change_hypothesis else 2

    total = (information_value + low_cost + isolable + not_already_tested
             + avoids_local_optimum)
    return {
        "hypothesis_id": h["hypothesis_id"],
        "total": total,
        "factors": {
            "information_value": information_value,
            "low_cost": low_cost,
            "isolable": isolable,
            "not_already_tested": not_already_tested,
            "avoids_local_optimum": avoids_local_optimum,
        },
        "next_test_priority_tiebreak": h.get("next_test_priority", "low"),
    }


def rank_next_experiments(*, existing_candidates=None) -> list:
    existing_candidates = existing_candidates or set()
    last_change = _last_change_hypothesis()
    tiebreak_order = {"high": 2, "medium": 1, "low": 0}
    scored = []
    for h in hs.all_hypotheses():
        if h["status"] == "REJECTED":
            continue
        candidate_exists = any(h["hypothesis_id"] in (e or "") for e in existing_candidates)
        s = score_hypothesis(h, last_change_hypothesis=last_change,
                              candidate_exists=candidate_exists)
        scored.append(s)
    scored.sort(key=lambda s: (s["total"], tiebreak_order.get(s["next_test_priority_tiebreak"], 0)),
                reverse=True)
    return scored


def select_next_experiment() -> dict:
    existing = {"adaptive-v0.3-ladder-candidate: H1"}
    ranking = rank_next_experiments(existing_candidates=existing)
    if not ranking:
        return {"selected": None, "reason": "no active hypotheses"}
    top = ranking[0]
    hyp = hs.get(top["hypothesis_id"])
    return {
        "selected": top["hypothesis_id"],
        "score": top,
        "hypothesis": hyp,
        "full_ranking": ranking,
        "reasoning": "{} ranks highest (score {}/10): {}...".format(
            top['hypothesis_id'], top['total'], hyp['statement'][:160]),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(select_next_experiment(), indent=2, default=str))
