"""arch_search/divergence.py -- find_first_divergence(): state-transition-level FIRST,
raw per-day-field statistics SECOND (only if the state sequence matches the panel).

See docs/SPEC-trajectory-directed-architecture-search.md section 2.5.
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

from arch_search.state_machine import STATES, StateTransition, state_order_signature

# Raw-field fallback tolerance: 1.5 MAD (median absolute deviation) band, requiring the
# candidate's value to fall outside the band on >= 2 consecutive days before counting as
# a divergence (filters single-day noise/seed variance). This is a STARTING GUESS per the
# spec's open questions, not validated against per-field seed-to-seed spread -- documented
# as a limitation in PHASE_0_STATE_MACHINE_AUDIT.md / this module's docstring.
DEFAULT_MAD_TOLERANCE = 1.5
DEFAULT_MIN_CONSECUTIVE_DAYS = 2

FIELD_PATHS = ["cash", "net_worth", "labor_allocation.idle_share", "labor_allocation.travel_per_task",
               "investment_flow.sales_rev", "investment_flow.hands_delta"]


@dataclass
class Divergence:
    kind: str                    # "state_skip" | "state_trigger_change" | "state_order_change" | "raw_field"
    day: int
    detail: Dict[str, Any] = field(default_factory=dict)

    def as_dict(self):
        return {"kind": self.kind, "day": self.day, "detail": self.detail}


def _panel_expected_order(convergent: Dict[str, Any]) -> List[str]:
    """Order states by their median first-entry day across the panel (from find_convergent_transitions output)."""
    order = []
    for s, info in convergent.items():
        order.append((s, info.get("entry_day_spread", 0)))
    # convergent dict doesn't carry median day directly; caller should pass per_reference_order
    return [s for s, _ in order]


def _first_entry_days(sequences: Dict[str, List[StateTransition]], state: str) -> List[int]:
    out = []
    for seq in sequences.values():
        days = [t.entry_day for t in seq if t.state == state]
        if days:
            out.append(min(days))
    return out


def find_first_divergence(candidate_seq: List[StateTransition],
                           panel_sequences: Dict[str, List[StateTransition]],
                           convergent_states: Dict[str, Any],
                           candidate_traj=None, panel_trajs: Optional[Dict[str, Any]] = None,
                           mad_tolerance: float = DEFAULT_MAD_TOLERANCE,
                           min_consecutive_days: int = DEFAULT_MIN_CONSECUTIVE_DAYS) -> Optional[Divergence]:
    """Find the earliest point (in trajectory order) where `candidate_seq` diverges from the
    panel's convergent-transition set. Ranks by trajectory order (earlier = more likely
    upstream) but this is a prioritization heuristic, NOT proof of causality (see spec 2.5) --
    callers must still run test_causal_prediction() before believing any causal story built
    on this divergence.

    Step 1 (state level): for each convergent state (in panel median-entry-day order), check:
      (a) SKIP    -- candidate's sequence never reaches this state at all.
      (b) TRIGGER -- candidate reaches the state, but via conditions/day far outside the
                     panel's own spread (> 2x the panel's max entry_day_spread, or the min
                     across the panel if spread is 0).
      (c) ORDER   -- candidate reaches states in a different relative order than every
                     panel member's order signature.
    Returns the FIRST such divergence in candidate trajectory order, or None if the
    candidate's state sequence matches the panel on every convergent state (Step 2 below
    should then be tried by the caller using raw_field_divergence()).
    """
    cand_states_reached: Dict[str, int] = {}
    for t in candidate_seq:
        if t.state not in cand_states_reached or t.entry_day < cand_states_reached[t.state]:
            cand_states_reached[t.state] = t.entry_day
    cand_order = state_order_signature(candidate_seq)

    # order states to check by the panel's own median first-entry day (earliest divergence
    # possible = earliest state in the panel's own trajectory order)
    median_day = {}
    for s, info in convergent_states.items():
        days = _first_entry_days(panel_sequences, s)
        median_day[s] = statistics.median(days) if days else 9999
    ordered_states = sorted(convergent_states.keys(), key=lambda s: median_day[s])

    panel_orders = [state_order_signature(seq) for seq in panel_sequences.values()]

    for s in ordered_states:
        info = convergent_states[s]
        if s not in cand_states_reached:
            return Divergence(kind="state_skip", day=int(median_day[s]),
                               detail={"state": s, "panel_confidence": info["confidence"],
                                       "panel_median_entry_day": median_day[s]})

        entry_days = _first_entry_days(panel_sequences, s)
        lo, hi = (min(entry_days), max(entry_days)) if entry_days else (0, 0)
        spread = max(1, hi - lo)
        cand_day = cand_states_reached[s]
        # trigger-changed: candidate enters this state clearly outside the panel's own spread
        if cand_day < lo - spread or cand_day > hi + spread:
            return Divergence(kind="state_trigger_change", day=cand_day,
                               detail={"state": s, "candidate_entry_day": cand_day,
                                       "panel_entry_day_range": [lo, hi]})

    # order check: does the candidate's overall order match ANY panel member's order on the
    # convergent-state subsequence?
    conv_set = set(convergent_states.keys())
    cand_conv_order = [s for s in cand_order if s in conv_set]
    matched_any = False
    for po in panel_orders:
        panel_conv_order = [s for s in po if s in conv_set]
        if panel_conv_order == cand_conv_order:
            matched_any = True
            break
    if not matched_any and cand_conv_order:
        # find first position where candidate's order departs from every panel order
        first_bad_idx = 0
        for i in range(len(cand_conv_order)):
            prefix = cand_conv_order[:i + 1]
            if not any(prefix == po[:i + 1] for po in [[s for s in po if s in conv_set] for po in panel_orders]):
                first_bad_idx = i
                break
        bad_state = cand_conv_order[first_bad_idx]
        return Divergence(kind="state_order_change", day=cand_states_reached.get(bad_state, 0),
                           detail={"state": bad_state, "candidate_order": cand_conv_order,
                                   "panel_orders_sample": [ [s for s in po if s in conv_set] for po in panel_orders]})

    return None  # state-level sequence matches the panel; fall back to raw-field divergence


def _get(traj, path, i):
    parts = path.split(".")
    v = traj.days[i].as_dict()
    for p in parts:
        if v is None:
            return None
        v = v.get(p) if isinstance(v, dict) else None
    return v


def raw_field_divergence(candidate_traj, reference_traj, fields: Optional[List[str]] = None,
                          mad_tolerance: float = DEFAULT_MAD_TOLERANCE,
                          min_consecutive_days: int = DEFAULT_MIN_CONSECUTIVE_DAYS) -> Optional[Divergence]:
    """Secondary, finer-grained fallback (spec 2.5 step 2): only meaningful once the state
    sequence already matches. Uses a robust statistic (median + 1.5*MAD band from the
    reference's OWN distribution) and requires persistence across >= min_consecutive_days
    to filter noise, per spec's stated tolerance-band method."""
    fields = fields or FIELD_PATHS
    n = min(len(candidate_traj.days), len(reference_traj.days))
    for f in fields:
        ref_vals = [v for v in (_get(reference_traj, f, i) for i in range(n)) if v is not None]
        if len(ref_vals) < 5:
            continue
        med = statistics.median(ref_vals)
        mad = statistics.median([abs(v - med) for v in ref_vals]) or 1e-6
        band = mad_tolerance * mad
        run = 0
        for i in range(n):
            cv = _get(candidate_traj, f, i)
            if cv is None:
                run = 0
                continue
            if abs(cv - med) > band:
                run += 1
                if run >= min_consecutive_days:
                    return Divergence(kind="raw_field", day=i - min_consecutive_days + 1,
                                       detail={"field": f, "candidate_value": cv, "reference_median": med,
                                               "band": band})
            else:
                run = 0
    return None
