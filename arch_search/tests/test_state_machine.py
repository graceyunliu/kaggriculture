import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from arch_search.trajectory import Trajectory, DayState
from arch_search.state_machine import extract_state_sequence, THRESHOLDS, STATES


def _mk_traj(n, prod_units, hands_delta=None, sales=None, cash=None, label="synthetic"):
    days = []
    for i in range(n):
        days.append(DayState(
            day=i,
            cash=cash[i] if cash else 100 * (i + 1),
            net_worth=cash[i] if cash else 100 * (i + 1),
            production_composition={"animals": 0, "plants": prod_units[i]},
            labor_allocation={"idle_share": 0.1},
            investment_flow={
                "hands_delta": (hands_delta[i] if hands_delta else None),
                "sales_rev": (sales[i] if sales else 0),
            },
        ))
    return Trajectory(label=label, seat=0, days=days)


def test_condition_triggered_not_fixed_day():
    """Two trajectories that reach the same production level on DIFFERENT calendar days
    must be assigned PRODUCTION_ACTIVATION on those different days -- i.e. the state is a
    function of the condition, not of the day index."""
    fast = _mk_traj(10, [0, 20, 20, 20, 20, 20, 20, 20, 20, 20])
    slow = _mk_traj(10, [0, 0, 0, 20, 20, 20, 20, 20, 20, 20])
    seq_fast = extract_state_sequence(fast)
    seq_slow = extract_state_sequence(slow)
    fast_entry = min(t.entry_day for t in seq_fast if t.state == "PRODUCTION_ACTIVATION")
    slow_entry = min(t.entry_day for t in seq_slow if t.state == "PRODUCTION_ACTIVATION")
    assert fast_entry == 1
    assert slow_entry == 3
    assert fast_entry != slow_entry


def test_thresholds_are_inspectable_and_overridable():
    """THRESHOLDS is a plain dict, and extract_state_sequence accepts an override without
    editing state_machine.py -- required for testing a revised taxonomy."""
    assert isinstance(THRESHOLDS, dict)
    assert "labor_scale_min_hands_burst" in THRESHOLDS
    traj = _mk_traj(5, [0, 20, 20, 20, 20], hands_delta=[None, 2, 0, 0, 0])
    seq_default = extract_state_sequence(traj)
    assert not any(t.state == "LABOR_SCALE" for t in seq_default)   # burst of 2 < default floor of 3
    seq_override = extract_state_sequence(traj, thresholds={"labor_scale_min_hands_burst": 2})
    assert any(t.state == "LABOR_SCALE" for t in seq_override)      # now crosses the lowered floor


def test_overlap_supported_when_data_shows_it():
    """A day where both DENSIFICATION (plateaued production) and LABOR_SCALE (a hiring
    burst) conditions hold simultaneously must appear in BOTH states' intervals when
    allow_overlap=True (the default) -- concurrent membership is not suppressed."""
    prod = [0, 20, 20, 20, 20, 20, 20]
    hands_delta = [None, 0, 0, 0, 3, 0, 0]
    traj = _mk_traj(7, prod, hands_delta=hands_delta)
    seq = extract_state_sequence(traj, allow_overlap=True)
    on_day4 = {t.state for t in seq if t.entry_day <= 4 <= (t.exit_day if t.exit_day is not None else 4)}
    assert "LABOR_SCALE" in on_day4
    assert "DENSIFICATION" in on_day4   # both true on day 4 -- overlap preserved


def test_allow_overlap_false_keeps_one_state_per_day():
    prod = [0, 20, 20, 20, 20, 20, 20]
    hands_delta = [None, 0, 0, 0, 3, 0, 0]
    traj = _mk_traj(7, prod, hands_delta=hands_delta)
    seq = extract_state_sequence(traj, allow_overlap=False)
    for day in range(7):
        active = [t.state for t in seq if t.entry_day <= day <= (t.exit_day if t.exit_day is not None else day)]
        assert len(active) <= 1
