import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from arch_search.trajectory import extract_trajectory, extract_trajectory_from_raw, DayState


def test_extract_trajectory_real_cached():
    """Real engine run (cached by evolve/trace.py's own sha-keyed cache) -- 30 days,
    every DayState has cash/net_worth, and no field is fabricated when the source lacks it."""
    traj = extract_trajectory(str(ROOT / "candidates/V3_12.py"), str(ROOT / "Opponents/opp_scenario_v14.py"),
                               1, seat=0)
    assert len(traj) == 30
    for d in traj.days:
        assert isinstance(d, DayState)
        assert d.cash is not None
        assert d.net_worth is not None
        # spatial layout is NOT available from evolve/trace.py's substrate -- must stay None,
        # never fabricated
        assert d.spatial_layout is None
    assert traj.days[0].investment_flow["hands_delta"] is None  # no "previous day" on day 0


def test_missing_fields_handled_safely():
    """A trace dict missing optional keys must not crash extraction and must yield None,
    not a fabricated value, for the missing metric."""
    n = 3
    raw = {
        "trace": [
            {
                "cash": [100, 150, 200], "networth": [100, 160, 210],
                "animals": [0, 1, 1], "plants": [0, 2, 2],
                "unit_turns": [5, 5, 5], "move_turns": [1, 1, 1], "idle_turns": [1, 1, 1],
                "work_turns": [3, 3, 3], "travel_per_task": [0.3, 0.3, 0.3],
                "chores_enumerated": [0, 1, 1], "chores_completed": [0, 1, 1],
                "hands": [1, 1, 1], "buys_cost": [0, 50, 0], "sales_rev": [0, 0, 10],
            },
            {},
        ]
    }
    traj = extract_trajectory_from_raw(raw, seat=0, label="synthetic")
    assert len(traj) == n
    assert traj.days[1].investment_flow["animals_delta"] == 1
    assert traj.days[0].investment_flow["hands_delta"] is None


def test_multiple_trace_formats_do_not_crash():
    """A minimal trace with only some METRICS present (simulating a different trace format /
    an older cache) should not raise -- missing keys must be handled, not assumed present."""
    raw = {"trace": [{
        "cash": [1, 2], "networth": [1, 2], "animals": [0, 0], "plants": [0, 0],
        "unit_turns": [0, 0], "move_turns": [0, 0], "idle_turns": [0, 0], "work_turns": [0, 0],
        "travel_per_task": [None, None], "chores_enumerated": [0, 0], "chores_completed": [0, 0],
        "hands": [0, 0], "buys_cost": [0, 0], "sales_rev": [0, 0],
    }, {"cash": [1, 2], "networth": [1, 2], "animals": [0, 0], "plants": [0, 0],
        "unit_turns": [0, 0], "move_turns": [0, 0], "idle_turns": [0, 0], "work_turns": [0, 0],
        "travel_per_task": [None, None], "chores_enumerated": [0, 0], "chores_completed": [0, 0],
        "hands": [0, 0], "buys_cost": [0, 0], "sales_rev": [0, 0]}]}
    traj = extract_trajectory_from_raw(raw, seat=1, label="minimal")
    assert len(traj) == 2
