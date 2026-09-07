import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from arch_search.state_machine import StateTransition, find_convergent_transitions


def test_stable_ordering_detected():
    """Three references that all reach A before B before C, at different calendar days,
    should mark A/B/C as convergent with high order agreement."""
    def seq(a_day, b_day, c_day):
        return [
            StateTransition("BOOTSTRAP", 0, 0),
            StateTransition("PRODUCTION_ACTIVATION", a_day, a_day),
            StateTransition("LABOR_SCALE", b_day, b_day),
            StateTransition("EXPANSION", c_day, c_day),
        ]
    seqs = {"r1": seq(1, 5, 12), "r2": seq(2, 6, 14), "r3": seq(1, 7, 13)}
    result = find_convergent_transitions(seqs)
    for s in ("PRODUCTION_ACTIVATION", "LABOR_SCALE", "EXPANSION"):
        assert s in result["convergent_transitions"], result
        assert result["convergent_transitions"][s]["confidence"] == "3/3"


def test_adversarial_mismatched_panel_does_not_falsely_produce_invariants():
    """A panel where each reference has a DIFFERENT relative order of the same 3 states
    must NOT be reported as a convergent, order-stable invariant."""
    seqs = {
        "r1": [StateTransition("PRODUCTION_ACTIVATION", 1, 1), StateTransition("LABOR_SCALE", 5, 5),
               StateTransition("EXPANSION", 10, 10)],
        "r2": [StateTransition("LABOR_SCALE", 1, 1), StateTransition("EXPANSION", 5, 5),
               StateTransition("PRODUCTION_ACTIVATION", 10, 10)],
        "r3": [StateTransition("EXPANSION", 1, 1), StateTransition("PRODUCTION_ACTIVATION", 5, 5),
               StateTransition("LABOR_SCALE", 10, 10)],
    }
    result = find_convergent_transitions(seqs, min_fraction=0.6)
    # all three states are PRESENT in all references (fraction 1.0) but their relative
    # order disagrees completely across the panel -- order_agreement must be low, so none
    # should be treated as an order-stable invariant.
    for s in ("PRODUCTION_ACTIVATION", "LABOR_SCALE", "EXPANSION"):
        info = result["convergent_transitions"].get(s) or result["implementation_detail"].get(s)
        assert info["relative_order_agreement"] <= 0.4, info
        assert s not in result["convergent_transitions"], \
            f"{s} was falsely marked convergent despite disagreeing order across the panel"


def test_minority_state_not_falsely_convergent():
    """A state present in only 1/5 references must not be reported as convergent."""
    base = [StateTransition("BOOTSTRAP", 0, 0), StateTransition("PRODUCTION_ACTIVATION", 1, 1)]
    seqs = {f"r{i}": list(base) for i in range(4)}
    seqs["r5"] = base + [StateTransition("EXPANSION_READY", 3, 3)]
    result = find_convergent_transitions(seqs, min_fraction=0.6)
    assert "EXPANSION_READY" in result["implementation_detail"]
    assert "EXPANSION_READY" not in result["convergent_transitions"]
