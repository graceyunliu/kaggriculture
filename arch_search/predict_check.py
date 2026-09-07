"""arch_search/predict_check.py -- test_causal_prediction(): re-extracts the state sequence
of an evaluated candidate's actual trajectory and checks each of a Hypothesis's predicted
steps, classifying the outcome. This is what stops a correlated metric being mistaken for
a cause (spec section 2.6 / the CRITICAL CONCEPTUAL RULE)."""
from __future__ import annotations

from typing import Callable, Dict, List, Any

from arch_search.hypothesis import Hypothesis

CLASSIFICATIONS = ("CONFIRMED", "PARTIALLY_CONFIRMED", "PREDICTION_CHAIN_FAILED",
                    "FALSIFIED", "INSUFFICIENT_EVIDENCE")


def test_causal_prediction(hypothesis: Hypothesis, step_checkers: List[Callable[[], bool]],
                            parent_trajectory=None, candidate_trajectory=None) -> Dict[str, Any]:
    """`step_checkers` is a list of zero-arg callables, one per hypothesis.prediction_steps
    entry, each returning True/False/None (None = INSUFFICIENT_EVIDENCE for that step -- e.g.
    a field the current tracer doesn't expose). Order matters: this is a step-by-step check
    of the SAME multi-step causal chain the hypothesis declared, not a single endpoint metric.

    Classification rule:
      - all steps True                                  -> CONFIRMED
      - step 1 True, later step(s) False (not None)      -> FALSIFIED (spec: this is the case
        that stops the search generating endless plausible stories that only ever show
        "the score went up" -- step 1 without steps 2-N falsifies the specific mechanism)
      - step 1 False                                     -> PREDICTION_CHAIN_FAILED (the very
        first predicted mechanical step didn't even occur -- the candidate never actually
        instantiated the hypothesis, distinct from "instantiated it and it didn't work")
      - some steps True, rest None (no False)            -> PARTIALLY_CONFIRMED
      - any None present alongside a False, or all None   -> INSUFFICIENT_EVIDENCE
    """
    if len(step_checkers) != len(hypothesis.prediction_steps):
        raise ValueError("one step_checker required per hypothesis.prediction_steps entry")

    results = []
    for check in step_checkers:
        try:
            results.append(check())
        except Exception as e:  # noqa: BLE001
            results.append(None)

    detail = {"steps": hypothesis.prediction_steps, "results": results}

    if not results:
        return {"classification": "INSUFFICIENT_EVIDENCE", "detail": detail}

    if results[0] is False:
        return {"classification": "PREDICTION_CHAIN_FAILED", "detail": detail}

    if all(r is True for r in results):
        return {"classification": "CONFIRMED", "detail": detail}

    if any(r is False for r in results[1:]):
        if any(r is None for r in results):
            return {"classification": "INSUFFICIENT_EVIDENCE", "detail": detail}
        return {"classification": "FALSIFIED", "detail": detail}

    if any(r is True for r in results) and all(r is not False for r in results):
        return {"classification": "PARTIALLY_CONFIRMED", "detail": detail}

    return {"classification": "INSUFFICIENT_EVIDENCE", "detail": detail}
