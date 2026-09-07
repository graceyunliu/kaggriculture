"""arch_search/trajectory.py -- thin adapter: existing tracer output -> Trajectory/DayState.

Reuses evolve/trace.py's traced()/run_traced() (itself built on mini_engine.py) for ALL
instrumentation. This module adds no new engine hooks and computes nothing the engine
did not already expose through evolve/trace.py's per-day METRICS. Where a DayState field
has no source in the available trace format, it is left None/empty -- never fabricated.

evolve/trace.py's METRICS (per player, per day 0..29):
  cash, networth, sales_rev, buys_cost, hands, animals, plants, weeds_new, escapes,
  missed_feed, missed_water, feed_hour, water_hour, unit_turns, move_turns, idle_turns,
  reversals, work_turns, travel_per_task, shed_units, carried_units,
  chores_enumerated, chores_completed, skipped_feed_not_due.

Notably absent from this substrate (documented, not invented): land-parcel counts,
per-crop/animal-species composition, explicit (x,y) spatial layout. Phase 0's report
records this as a real limitation of the current tracer, not a gap in this adapter.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional, List, Dict, Any

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "evolve") not in sys.path:
    sys.path.insert(0, str(ROOT / "evolve"))
import trace as _trace_mod  # evolve/trace.py -- imported, never modified  # noqa: E402


@dataclass
class DayState:
    """One day's economic snapshot. Every field traces back to evolve/trace.py's output;
    a field is None/empty rather than guessed when the underlying trace doesn't carry it."""
    day: int
    cash: Optional[float] = None
    net_worth: Optional[float] = None
    # aggregate counts only -- evolve/trace.py does not break composition down by species
    production_composition: Dict[str, Any] = field(default_factory=dict)     # {"animals": n, "plants": n}
    labor_allocation: Dict[str, Any] = field(default_factory=dict)           # travel/idle/work/chore turn shares
    investment_flow: Dict[str, Any] = field(default_factory=dict)           # deltas vs previous day
    spatial_layout: Optional[Dict[str, Any]] = None    # not available from this trace source -> always None here
    declared_phase: Optional[str] = None               # only populated if the agent module exposes PHASE state

    def as_dict(self):
        return asdict(self)


@dataclass
class Trajectory:
    label: str                 # e.g. "V3_12__vs__opp_scenario_v14__seed1"
    seat: int
    days: List[DayState] = field(default_factory=list)

    def __len__(self):
        return len(self.days)

    def __getitem__(self, i):
        return self.days[i]

    def field_series(self, path: str) -> List[Optional[float]]:
        """Dotted-path accessor, e.g. 'labor_allocation.idle_share' or 'cash'."""
        parts = path.split(".")
        out = []
        for d in self.days:
            v: Any = d.as_dict()
            for p in parts:
                if v is None:
                    break
                v = v.get(p) if isinstance(v, dict) else getattr(v, p, None)
            out.append(v)
        return out


def _safe_div(a, b):
    return (a / b) if b else None


def _delta(series, i):
    if i == 0 or series[i] is None or series[i - 1] is None:
        return None
    return series[i] - series[i - 1]


def extract_trajectory(agent_a: str, agent_b: str, seed: int, seat: int = 0,
                        engine: str = "master", label: Optional[str] = None) -> Trajectory:
    """Build a Trajectory for `seat` (0 = agent_a, 1 = agent_b) from evolve.trace.traced().

    No new simulation is run beyond what evolve/trace.py already does (results are cached
    by evolve/trace.py's own content-hash cache, reused as-is).
    """
    r = _trace_mod.traced(str(agent_a), str(agent_b), seed, engine=engine)
    t = r["trace"][seat]
    n = len(t["cash"])
    days: List[DayState] = []
    for d in range(n):
        unit_turns = t["unit_turns"][d] or 0
        move_turns = t["move_turns"][d] or 0
        idle_turns = t["idle_turns"][d] or 0
        work_turns = t["work_turns"][d] or 0
        labor_allocation = {
            "unit_turns": unit_turns,
            "move_turns": move_turns,
            "idle_turns": idle_turns,
            "work_turns": work_turns,
            "travel_share": _safe_div(move_turns, unit_turns),
            "idle_share": _safe_div(idle_turns, unit_turns),
            "work_share": _safe_div(work_turns, unit_turns),
            "travel_per_task": t["travel_per_task"][d],
            "chores_enumerated": t["chores_enumerated"][d],
            "chores_completed": t["chores_completed"][d],
        }
        production_composition = {
            "animals": t["animals"][d],
            "plants": t["plants"][d],
        }
        investment_flow = {
            "hands_delta": _delta(t["hands"], d),
            "animals_delta": _delta(t["animals"], d),
            "plants_delta": _delta(t["plants"], d),
            "buys_cost": t["buys_cost"][d],
            "sales_rev": t["sales_rev"][d],
            # land deltas are NOT available from evolve/trace.py's METRICS -- omitted, not guessed
        }
        days.append(DayState(
            day=d,
            cash=t["cash"][d],
            net_worth=t["networth"][d],
            production_composition=production_composition,
            labor_allocation=labor_allocation,
            investment_flow=investment_flow,
            spatial_layout=None,
            declared_phase=None,
        ))
    lbl = label or f"{Path(agent_a).stem}__vs__{Path(agent_b).stem}__seed{seed}__seat{seat}"
    return Trajectory(label=lbl, seat=seat, days=days)


def extract_trajectory_from_raw(raw_trace: dict, seat: int = 0, label: str = "raw") -> Trajectory:
    """Same conversion as extract_trajectory() but from an already-produced evolve/trace.py
    run_traced()/traced() result dict -- for callers (e.g. tests) that already have one,
    so we never re-run the engine twice for the same data."""
    t = raw_trace["trace"][seat]
    n = len(t["cash"])
    days: List[DayState] = []
    for d in range(n):
        unit_turns = t["unit_turns"][d] or 0
        move_turns = t["move_turns"][d] or 0
        idle_turns = t["idle_turns"][d] or 0
        work_turns = t["work_turns"][d] or 0
        days.append(DayState(
            day=d,
            cash=t["cash"][d],
            net_worth=t["networth"][d],
            production_composition={"animals": t["animals"][d], "plants": t["plants"][d]},
            labor_allocation={
                "unit_turns": unit_turns, "move_turns": move_turns, "idle_turns": idle_turns,
                "work_turns": work_turns,
                "travel_share": _safe_div(move_turns, unit_turns),
                "idle_share": _safe_div(idle_turns, unit_turns),
                "work_share": _safe_div(work_turns, unit_turns),
                "travel_per_task": t["travel_per_task"][d],
                "chores_enumerated": t["chores_enumerated"][d],
                "chores_completed": t["chores_completed"][d],
            },
            investment_flow={
                "hands_delta": _delta(t["hands"], d),
                "animals_delta": _delta(t["animals"], d),
                "plants_delta": _delta(t["plants"], d),
                "buys_cost": t["buys_cost"][d],
                "sales_rev": t["sales_rev"][d],
            },
            spatial_layout=None,
            declared_phase=None,
        ))
    return Trajectory(label=label, seat=seat, days=days)
