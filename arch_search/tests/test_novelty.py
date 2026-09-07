import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from arch_search.trajectory import Trajectory, DayState
from arch_search.novelty import novelty_gate


def _mk(n, hands_deltas, label, buys_cost=None):
    days = []
    for i in range(n):
        days.append(DayState(day=i, cash=100, net_worth=100,
                              production_composition={"animals": 0, "plants": 5},
                              labor_allocation={"travel_share": 0.3, "idle_share": 0.3, "work_share": 0.4},
                              investment_flow={"hands_delta": hands_deltas[i], "animals_delta": 0,
                                                "plants_delta": 0,
                                                "buys_cost": (buys_cost[i] if buys_cost else 0)}))
    return Trajectory(label=label, seat=0, days=days)


def test_near_identical_trajectory_fails_gate():
    parent = _mk(12, [None] + [0] * 11, "parent")
    child = _mk(12, [None] + [0] * 11, "child")
    result = novelty_gate(child, parent, day=10)
    assert result.passed is False


def test_diverging_investment_sequence_passes_gate():
    parent = _mk(12, [None] + [0] * 11, "parent")
    deltas = [None] + [5] * 11   # much heavier hiring than parent
    buys = [0] + [500] * 11       # and much heavier spend -- both investment-sequence fields diverge
    child = _mk(12, deltas, "child", buys_cost=buys)
    result = novelty_gate(child, parent, day=10)
    assert result.passed is True
    assert result.triggered_by == "investment_sequence"
