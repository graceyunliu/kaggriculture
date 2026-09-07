import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from arch_search.trajectory import Trajectory, DayState
from arch_search.state_machine import StateTransition, find_convergent_transitions
from arch_search.divergence import find_first_divergence, raw_field_divergence


def _panel_seqs():
    def seq(labor_day):
        return [
            StateTransition("BOOTSTRAP", 0, 0),
            StateTransition("PRODUCTION_ACTIVATION", 1, 1),
            StateTransition("LABOR_SCALE", labor_day, labor_day),
            StateTransition("EXPANSION", labor_day + 5, labor_day + 5),
        ]
    return {"r1": seq(5), "r2": seq(6), "r3": seq(5)}


def _convergent(panel):
    return find_convergent_transitions(panel)["convergent_transitions"]


def test_skipped_state_detected():
    panel = _panel_seqs()
    conv = _convergent(panel)
    cand = [StateTransition("BOOTSTRAP", 0, 0), StateTransition("PRODUCTION_ACTIVATION", 1, 1),
            StateTransition("EXPANSION", 10, 10)]  # never reaches LABOR_SCALE
    div = find_first_divergence(cand, panel, conv)
    assert div is not None
    assert div.kind == "state_skip"
    assert div.detail["state"] == "LABOR_SCALE"


def test_changed_trigger_detected():
    panel = _panel_seqs()
    conv = _convergent(panel)
    cand = [StateTransition("BOOTSTRAP", 0, 0), StateTransition("PRODUCTION_ACTIVATION", 1, 1),
            StateTransition("LABOR_SCALE", 20, 20), StateTransition("EXPANSION", 25, 25)]  # way late
    div = find_first_divergence(cand, panel, conv)
    assert div is not None
    assert div.kind == "state_trigger_change"
    assert div.detail["state"] == "LABOR_SCALE"


def test_changed_order_detected():
    panel = _panel_seqs()
    conv = _convergent(panel)
    # candidate reaches EXPANSION before LABOR_SCALE -- reversed relative order vs every panel member
    cand = [StateTransition("BOOTSTRAP", 0, 0), StateTransition("PRODUCTION_ACTIVATION", 1, 1),
            StateTransition("EXPANSION", 3, 3), StateTransition("LABOR_SCALE", 6, 6)]
    div = find_first_divergence(cand, panel, conv)
    assert div is not None
    assert div.kind in ("state_order_change", "state_trigger_change")


def test_matching_sequence_returns_none_state_level():
    panel = _panel_seqs()
    conv = _convergent(panel)
    cand = _panel_seqs()["r1"]  # identical to a panel member
    div = find_first_divergence(cand, panel, conv)
    assert div is None


def _mk_traj_field(values, label):
    days = [DayState(day=i, cash=v, net_worth=v, production_composition={}, labor_allocation={},
                      investment_flow={}) for i, v in enumerate(values)]
    return Trajectory(label=label, seat=0, days=days)


def test_raw_field_noisy_one_day_blip_ignored():
    """A single-day spike outside the reference's MAD band must NOT count as a divergence --
    persistence across >=2 consecutive days is required."""
    ref = _mk_traj_field([100] * 20, "ref")
    cand_vals = [100] * 20
    cand_vals[10] = 100000  # one-day blip
    cand = _mk_traj_field(cand_vals, "cand")
    div = raw_field_divergence(cand, ref, fields=["cash"])
    assert div is None


def test_raw_field_persistent_divergence_detected():
    ref = _mk_traj_field([100] * 20, "ref")
    cand_vals = [100] * 20
    for i in (10, 11, 12):
        cand_vals[i] = 100000
    cand = _mk_traj_field(cand_vals, "cand")
    div = raw_field_divergence(cand, ref, fields=["cash"])
    assert div is not None
    assert div.kind == "raw_field"
    assert div.day == 10
