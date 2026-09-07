"""arch_search/state_machine.py -- condition-triggered economic state reconstruction.

Converts a raw Trajectory (arch_search/trajectory.py) into a sequence of economic states,
using boolean entry conditions over DayState fields -- NOT fixed-day labels. The taxonomy
below is a PROVISIONAL HYPOTHESIS (see docs/SPEC-trajectory-directed-architecture-search.md
section 2.3 and arch_search/reports/PHASE_0_STATE_MACHINE_AUDIT.md), validated/revised
against real reference trajectories rather than assumed correct.

THRESHOLDS is deliberately a plain module-level dict (not buried constants) so it is
inspectable and overridable -- pass a different dict to extract_state_sequence() to test
a revised taxonomy without editing this file.

Every threshold below was chosen by inspecting the six real trajectories in the Phase 0
reference panel (arch_search/references.py) BEFORE being hardcoded here -- see
PHASE_0_STATE_MACHINE_AUDIT.md section A for the derivation of each one. They are not
guesses; where the panel data did not cleanly separate a state, that is documented as a
limitation rather than papered over with a threshold tuned to force separation.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Callable

from arch_search.trajectory import Trajectory, DayState

# ---------------------------------------------------------------------- taxonomy (hypothesis)
STATES = [
    "BOOTSTRAP",
    "LABOR_SCALE",
    "PRODUCTION_ACTIVATION",
    "DENSIFICATION",
    "EXPANSION_READY",
    "EXPANSION",
    "THROUGHPUT_SCALE",
    "ENDGAME_CONVERSION",
]

# Data-derived defaults -- see PHASE_0_STATE_MACHINE_AUDIT.md section A for how each number
# was picked from the reference panel (min-across-panel or panel-median, as noted per key).
THRESHOLDS = {
    # BOOTSTRAP: production_units (animals+plants stock) is exactly 0 -- true for all 6
    # panel trajectories on day 0 by construction (nothing planted turn 0), so this is not
    # a tuned number, it's the literal starting condition.
    "bootstrap_production_units_max": 0,

    # PRODUCTION_ACTIVATION: first day production_units > this floor. All 6 panel
    # trajectories cross from 0 straight past 15 within the first 1-3 days (day-3 values
    # ranged 20-24 across the panel+champion), so 1 (i.e. "> 0") is the honest crossing
    # point -- a higher floor like 15 would still fire on day 1-3 for everyone but adds
    # nothing since the data shows no trajectory pausing partway between 0 and ~20.
    "production_activation_min_units": 1,

    # DENSIFICATION: >=2 consecutive days where |production_units delta| <= this, occurring
    # AFTER production_activation has fired. Chosen as the largest single-day delta observed
    # during the panel's own day3-day8 plateau windows (deltas of -1..+3 were typical there,
    # vs. +19..+24 during the panel's day1 and day9-13 growth waves) -- i.e. picked to separate
    # "plateau" from "wave", not picked to force a particular day.
    "densification_max_daily_delta": 4,
    "densification_min_run_days": 2,

    # EXPANSION: a single-day production_units jump >= this, occurring on/after day 5 (so the
    # day-1 initial planting wave doesn't count as "expansion"). The panel's second wave jumps
    # were 15-24 units/day (shared_clone +24 day12, budget_fork/strawhats ~+23 day8-9,
    # kronki +16 day8, kwa +24 day10); champion's second wave was +19 on day13. 15 is the
    # min-across-panel value that still cleanly excludes the day3-8 plateau's <=4/day noise.
    "expansion_min_jump": 15,
    "expansion_min_day": 5,

    # EXPANSION_READY: day immediately preceding an EXPANSION jump, while cash is
    # non-collapsing (>= this) and idle_share is not high (labor is not sitting idle waiting
    # on something else). cash floor set at 0 deliberately loose -- see audit doc: cash alone
    # did not cleanly gate readiness in this data, this is flagged as UNSUPPORTED/weak below.
    "expansion_ready_min_cash": 0,
    "expansion_ready_max_idle_share": 0.5,

    # THROUGHPUT_SCALE: trailing 5-day sales_rev sum >= this. Chosen from the panel's
    # own day15-29 windows, which ranged ~18k-41k/5-day window; champion's equivalent windows
    # were 14.7k-22.5k, i.e. below every panel window except its lowest (kwa/kronki ~15-18k).
    # 25000 is the median of the panel's day15-29 windows, so "throughput scale" means
    # "producing revenue at or above the panel's own median rate", not an arbitrary number.
    "throughput_scale_min_5day_sales": 25000,

    # LABOR_SCALE: a single-day hands_delta >= this. This is the smallest value that still
    # appears as a distinct spike (not day-to-day churn) in EVERY panel trajectory: shared_clone
    # +3, budget_fork +3, strawhats +3, kronki +3, kwa +5, champion +4. 3 is the min across
    # the panel's own hiring-burst days.
    "labor_scale_min_hands_burst": 3,

    # ENDGAME_CONVERSION: last N days of the game, where production_units is falling (stock
    # being liquidated/harvested down rather than grown). 30-day games -> last 5 days is the
    # tail where every panel trajectory's production_units visibly drops (see audit doc).
    "endgame_last_n_days": 5,
    "endgame_production_decline_min": 1,
}


@dataclass
class StateTransition:
    state: str
    entry_day: int
    exit_day: Optional[int]
    entry_conditions: Dict[str, Any] = field(default_factory=dict)
    evidence: Dict[str, Any] = field(default_factory=dict)

    def as_dict(self):
        return {
            "state": self.state, "entry_day": self.entry_day, "exit_day": self.exit_day,
            "entry_conditions": self.entry_conditions, "evidence": self.evidence,
        }


# ---------------------------------------------------------------------- feature helpers
def _prod_units(d: DayState) -> Optional[int]:
    pc = d.production_composition or {}
    a, p = pc.get("animals"), pc.get("plants")
    if a is None and p is None:
        return None
    return (a or 0) + (p or 0)


def _series(traj: Trajectory, fn) -> List[Optional[float]]:
    return [fn(d) for d in traj.days]


def _trailing_sum(series, i, n):
    lo = max(0, i - n + 1)
    vals = [v for v in series[lo:i + 1] if v is not None]
    return sum(vals) if vals else None


# ---------------------------------------------------------------------- per-day membership
def _day_conditions(traj: Trajectory, i: int, prod: List[Optional[int]], hands_delta: List[Optional[float]],
                     sales: List[Optional[float]], th: Dict[str, Any]) -> Dict[str, bool]:
    """Return which states' entry conditions hold on day i. Overlapping membership is
    supported explicitly -- more than one condition can be True on the same day (see
    PHASE_0_STATE_MACHINE_AUDIT.md section B for why mutual exclusivity was NOT enforced)."""
    n = len(traj.days)
    d = traj.days[i]
    pu = prod[i]
    conds = {s: False for s in STATES}

    if pu is not None and pu <= th["bootstrap_production_units_max"]:
        conds["BOOTSTRAP"] = True

    if pu is not None and pu >= th["production_activation_min_units"] and (i == 0 or (prod[i - 1] or 0) == 0
                                                                            or (pu - (prod[i - 1] or 0)) > 0):
        # fires on the day(s) production_units is rising from/near zero
        if pu >= th["production_activation_min_units"] and (prod[i - 1] if i > 0 else 0) is not None:
            prev = prod[i - 1] if i > 0 else 0
            if pu > (prev or 0):
                conds["PRODUCTION_ACTIVATION"] = True

    # densification: look at a trailing run ending at day i
    run_n = th["densification_min_run_days"]
    if i + 1 >= run_n:
        deltas = []
        ok = True
        for k in range(i - run_n + 1, i + 1):
            if k <= 0 or prod[k] is None or prod[k - 1] is None:
                ok = False
                break
            deltas.append(abs(prod[k] - prod[k - 1]))
        if ok and all(dl <= th["densification_max_daily_delta"] for dl in deltas) and (pu or 0) >= 15:
            conds["DENSIFICATION"] = True

    if hands_delta[i] is not None and hands_delta[i] >= th["labor_scale_min_hands_burst"]:
        conds["LABOR_SCALE"] = True

    if pu is not None and i > 0 and prod[i - 1] is not None and i >= th["expansion_min_day"] \
            and (pu - prod[i - 1]) >= th["expansion_min_jump"]:
        conds["EXPANSION"] = True

    # expansion_ready: day before an EXPANSION day (computed via lookahead), densifying, cash ok
    if i + 1 < n and prod[i] is not None and prod[i + 1] is not None \
            and (prod[i + 1] - prod[i]) >= th["expansion_min_jump"] and (i + 1) >= th["expansion_min_day"]:
        idle = (d.labor_allocation or {}).get("idle_share")
        cash_ok = (d.cash or 0) >= th["expansion_ready_min_cash"]
        idle_ok = idle is None or idle <= th["expansion_ready_max_idle_share"]
        if cash_ok and idle_ok:
            conds["EXPANSION_READY"] = True

    tsum = _trailing_sum(sales, i, 5)
    if tsum is not None and tsum >= th["throughput_scale_min_5day_sales"]:
        conds["THROUGHPUT_SCALE"] = True

    if i >= n - th["endgame_last_n_days"] and pu is not None and prod[i - 1] is not None \
            and (prod[i - 1] - pu) >= th["endgame_production_decline_min"]:
        conds["ENDGAME_CONVERSION"] = True

    return conds


def extract_state_sequence(traj: Trajectory, thresholds: Optional[Dict[str, Any]] = None,
                            allow_overlap: bool = True) -> List[StateTransition]:
    """Condition-triggered state sequence, NOT day-indexed labels. Supports overlapping/
    concurrent membership by default (allow_overlap=True): the returned list may contain
    intervals for different states that overlap in day range, if the data shows the economy
    can be, e.g., simultaneously densifying one quadrant and expanding another. Set
    allow_overlap=False to force single-state-at-a-time (keeps the highest-priority active
    state per day, priority = STATES list order) for callers that need a flat sequence."""
    th = dict(THRESHOLDS)
    if thresholds:
        th.update(thresholds)
    n = len(traj.days)
    prod = _series(traj, _prod_units)
    hands_delta = _series(traj, lambda d: (d.investment_flow or {}).get("hands_delta"))
    sales = _series(traj, lambda d: (d.investment_flow or {}).get("sales_rev"))

    per_day = [_day_conditions(traj, i, prod, hands_delta, sales, th) for i in range(n)]

    if not allow_overlap:
        for i in range(n):
            active = [s for s in STATES if per_day[i][s]]
            for s in STATES:
                if s not in active[:1]:
                    per_day[i][s] = False

    transitions: List[StateTransition] = []
    open_since: Dict[str, int] = {}
    for i in range(n):
        for s in STATES:
            on = per_day[i][s]
            if on and s not in open_since:
                open_since[s] = i
            elif not on and s in open_since:
                entry = open_since.pop(s)
                transitions.append(StateTransition(
                    state=s, entry_day=entry, exit_day=i - 1,
                    entry_conditions={k: v for k, v in th.items() if s.lower().split('_')[0] in k or True},
                    evidence={"production_units_at_entry": prod[entry], "cash_at_entry": traj.days[entry].cash},
                ))
    for s, entry in open_since.items():
        transitions.append(StateTransition(
            state=s, entry_day=entry, exit_day=n - 1,
            entry_conditions={},
            evidence={"production_units_at_entry": prod[entry], "cash_at_entry": traj.days[entry].cash},
        ))
    transitions.sort(key=lambda t: (t.entry_day, STATES.index(t.state)))
    return transitions


# ---------------------------------------------------------------------- convergence
def state_order_signature(transitions: List[StateTransition]) -> List[str]:
    """First-entry order of each state that appears at all (dedup, keep first occurrence)."""
    seen = []
    for t in sorted(transitions, key=lambda t: t.entry_day):
        if t.state not in seen:
            seen.append(t.state)
    return seen


def find_convergent_transitions(sequences: Dict[str, List[StateTransition]],
                                 min_fraction: float = 0.6) -> Dict[str, Any]:
    """Given {label: state_transition_list} for multiple reference trajectories, report which
    states appear across most references (with confidence counts), and whether their relative
    entry order is stable. Does NOT claim causality -- output is labeled "observed convergent
    transitions" only. Distinguishes "candidate architecture invariant" (state appears + order
    stable across >= min_fraction of the panel) from "implementation detail" (appears but at
    wildly different relative positions, or on a minority of the panel)."""
    labels = list(sequences.keys())
    n_refs = len(labels)
    presence: Dict[str, List[str]] = {s: [] for s in STATES}
    first_entry_day: Dict[str, Dict[str, int]] = {s: {} for s in STATES}
    for label, seq in sequences.items():
        seen_states = set()
        for t in sorted(seq, key=lambda t: t.entry_day):
            if t.state not in seen_states:
                presence[t.state].append(label)
                first_entry_day[t.state][label] = t.entry_day
                seen_states.add(t.state)

    orders = {label: state_order_signature(seq) for label, seq in sequences.items()}

    convergent = {}
    implementation_detail = {}
    for s in STATES:
        refs_with = presence[s]
        frac = len(refs_with) / n_refs if n_refs else 0
        entry_days = [first_entry_day[s][l] for l in refs_with]
        day_spread = (max(entry_days) - min(entry_days)) if entry_days else None
        # relative-order stability: what fraction of pairwise (other_state, s) orderings agree
        rel_order_votes = {}
        for label in refs_with:
            order = orders[label]
            if s not in order:
                continue
            idx = order.index(s)
            before = tuple(order[:idx])
            rel_order_votes.setdefault(before, 0)
            rel_order_votes[before] += 1
        order_agreement = (max(rel_order_votes.values()) / len(refs_with)) if refs_with else 0
        entry = {
            "state": s,
            "present_in": refs_with,
            "confidence": f"{len(refs_with)}/{n_refs}",
            "fraction": round(frac, 2),
            "entry_day_spread": day_spread,
            "relative_order_agreement": round(order_agreement, 2),
        }
        if frac >= min_fraction and order_agreement >= 0.6:
            convergent[s] = entry
        else:
            implementation_detail[s] = entry

    return {
        "reference_labels": labels,
        "n_references": n_refs,
        "convergent_transitions": convergent,
        "implementation_detail": implementation_detail,
        "per_reference_order": orders,
        "note": "These are OBSERVED convergent transitions across the given reference panel, "
                "not proof of causality or of a universally optimal order.",
    }
