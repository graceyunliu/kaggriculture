import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from arch_search.hypothesis import Hypothesis
from arch_search.predict_check import test_causal_prediction as causal_check


def _h(n):
    return Hypothesis(hypothesis_id="H_test", structural_divergence={}, causal_claim="test claim",
                       prediction_steps=[f"step{i}" for i in range(n)])


def test_full_confirmation():
    h = _h(3)
    result = causal_check(h, [lambda: True, lambda: True, lambda: True])
    assert result["classification"] == "CONFIRMED"


def test_partial_confirmation():
    h = _h(3)
    result = causal_check(h, [lambda: True, lambda: None, lambda: True])
    assert result["classification"] == "PARTIALLY_CONFIRMED"


def test_chain_failure_first_step_false():
    h = _h(3)
    result = causal_check(h, [lambda: False, lambda: True, lambda: True])
    assert result["classification"] == "PREDICTION_CHAIN_FAILED"


def test_falsified_step1_true_later_false():
    h = _h(4)
    result = causal_check(h, [lambda: True, lambda: True, lambda: False, lambda: True])
    assert result["classification"] == "FALSIFIED"


def test_insufficient_evidence_all_none():
    h = _h(2)
    result = causal_check(h, [lambda: None, lambda: None])
    assert result["classification"] == "INSUFFICIENT_EVIDENCE"


def test_insufficient_evidence_false_mixed_with_none():
    h = _h(3)
    result = causal_check(h, [lambda: True, lambda: None, lambda: False])
    assert result["classification"] == "INSUFFICIENT_EVIDENCE"
