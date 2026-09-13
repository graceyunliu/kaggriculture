"""Unit tests for the v0.3 MIN_N_TO_TRUST_B guard.

Run with: python3 -m pytest tests/test_min_n_guard.py -q
(or plain `python3 tests/test_min_n_guard.py` -- no pytest dependency required)
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CTRL_PATH = HERE.parent / "controller" / "adaptive_slice_v0.py"
STATE_PATH = HERE.parent / "state" / "learner_frozen.json"


def load_controller():
    spec = importlib.util.spec_from_file_location("adaptive_slice_v0_3", CTRL_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def make_learner(ctrl, stats: dict):
    learner = ctrl.Learner()
    for regime, arms in stats.items():
        for arm, stat in arms.items():
            learner.stats[regime][arm]["n"] = stat["n"]
            learner.stats[regime][arm]["mean"] = stat["mean"]
    return learner


def test_thin_b_falls_back_to_a():
    ctrl = load_controller()
    learner = make_learner(ctrl, {
        "r1": {"A_FULL_O42": {"n": 5, "mean": 100.0}, "B_ONE_PER_ORDER": {"n": 3, "mean": 5000.0}},
    })
    choice, reason = learner.choose("r1", learning=False, frozen=True)
    assert choice == "A_FULL_O42", f"expected fallback to A, got {choice}"
    assert reason["algorithm"] == "frozen_greedy_min_n_guard"
    assert reason["b_n"] == 3
    assert reason["would_have_selected"] == "B_ONE_PER_ORDER"


def test_well_supported_b_is_trusted():
    ctrl = load_controller()
    learner = make_learner(ctrl, {
        "r2": {"A_FULL_O42": {"n": 5, "mean": 100.0}, "B_ONE_PER_ORDER": {"n": 45, "mean": 5000.0}},
    })
    choice, reason = learner.choose("r2", learning=False, frozen=True)
    assert choice == "B_ONE_PER_ORDER"
    assert reason["algorithm"] == "frozen_greedy"


def test_guard_only_applies_when_b_would_have_won():
    ctrl = load_controller()
    learner = make_learner(ctrl, {
        "r3": {"A_FULL_O42": {"n": 20, "mean": 900.0}, "B_ONE_PER_ORDER": {"n": 2, "mean": -100.0}},
    })
    choice, reason = learner.choose("r3", learning=False, frozen=True)
    assert choice == "A_FULL_O42"
    assert reason["algorithm"] == "frozen_greedy"  # no guard needed, A already wins


def test_guard_does_not_apply_in_training_mode():
    ctrl = load_controller()
    learner = make_learner(ctrl, {
        "r4": {"A_FULL_O42": {"n": 5, "mean": 100.0}, "B_ONE_PER_ORDER": {"n": 3, "mean": 5000.0}},
    })
    choice, reason = learner.choose("r4", learning=True, frozen=False)
    assert choice == "B_ONE_PER_ORDER", "guard must be inert outside frozen mode"
    assert reason["algorithm"] == "UCB1"


def test_choose_never_mutates_learner_state():
    ctrl = load_controller()
    learner = make_learner(ctrl, {
        "r5": {"A_FULL_O42": {"n": 5, "mean": 100.0}, "B_ONE_PER_ORDER": {"n": 3, "mean": 5000.0}},
    })
    before = json.dumps(learner.dump(), sort_keys=True)
    for _ in range(10):
        learner.choose("r5", learning=False, frozen=True)
    after = json.dumps(learner.dump(), sort_keys=True)
    assert before == after, "choose() must never call update() / mutate stats"


def test_against_certified_v0_2_frozen_state():
    """Regression pin: exact set of regimes that flip under the real v0.2 state."""
    ctrl = load_controller()
    state = json.loads(STATE_PATH.read_text())
    learner = make_learner(ctrl, state)
    flipped = []
    for regime in state:
        choice, reason = learner.choose(regime, learning=False, frozen=True)
        if reason.get("algorithm") == "frozen_greedy_min_n_guard":
            flipped.append(regime)
    assert sorted(flipped) == sorted(["late|high|roomy", "late|high|tight", "mid|low|roomy"]), flipped


def _run_all():
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run_all() else 0)
