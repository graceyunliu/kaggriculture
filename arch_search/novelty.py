"""arch_search/novelty.py -- trajectory-based novelty gate, candidate vs its OWN PARENT
(never vs other families, never on source-code similarity). See spec section 2.7."""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional

from arch_search.trajectory import Trajectory
from arch_search.state_machine import extract_state_sequence, state_order_signature

DEFAULT_NOVELTY_DAY = 10

# Distance thresholds by dimension, by day 10. Investment/production/labor are fractional
# distances (0..1-ish, can exceed 1); state_sequence is a discrete "did the order differ"
# flag. These are starting defaults (spec explicitly leaves exact numbers unresolved,
# section 3) -- documented here rather than silently assumed, and overridable per call.
DEFAULT_THRESHOLDS = {
    "investment_seq_min_dist": 0.35,
    "production_composition_min_dist": 0.25,
    "labor_allocation_min_dist": 0.25,
}


@dataclass
class NoveltyResult:
    passed: bool
    day: int
    distances: Dict[str, float]
    triggered_by: Optional[str]
    state_sequence_diverged: bool

    def as_dict(self):
        return asdict(self)


def _series_upto(traj: Trajectory, path: str, day: int):
    parts = path.split(".")
    out = []
    for d in traj.days[: day + 1]:
        v = d.as_dict()
        for p in parts:
            if v is None:
                break
            v = v.get(p) if isinstance(v, dict) else None
        out.append(v)
    return out


def _l1_dist(a, b):
    n = min(len(a), len(b))
    num, den = 0.0, 0.0
    for i in range(n):
        av, bv = a[i], b[i]
        if av is None or bv is None:
            continue
        num += abs(av - bv)
        den += max(abs(av), abs(bv), 1.0)
    return (num / den) if den else 0.0


def novelty_gate(candidate: Trajectory, parent: Trajectory, day: int = DEFAULT_NOVELTY_DAY,
                  thresholds: Optional[Dict[str, float]] = None) -> NoveltyResult:
    """Require distance to exceed threshold on AT LEAST ONE of: investment sequence,
    production composition, or labor allocation, by `day` (default 10). Also reports (but
    does not require) a state-transition-sequence divergence as an extra signal.
    Source-code similarity is explicitly NOT checked here -- only realized trajectories."""
    th = dict(DEFAULT_THRESHOLDS)
    if thresholds:
        th.update(thresholds)

    inv_cand = [_series_upto(candidate, "investment_flow.hands_delta", day),
                _series_upto(candidate, "investment_flow.animals_delta", day),
                _series_upto(candidate, "investment_flow.plants_delta", day),
                _series_upto(candidate, "investment_flow.buys_cost", day)]
    inv_par = [_series_upto(parent, "investment_flow.hands_delta", day),
               _series_upto(parent, "investment_flow.animals_delta", day),
               _series_upto(parent, "investment_flow.plants_delta", day),
               _series_upto(parent, "investment_flow.buys_cost", day)]
    inv_dist = sum(_l1_dist(a, b) for a, b in zip(inv_cand, inv_par)) / 4

    prod_cand = [_series_upto(candidate, "production_composition.animals", day),
                 _series_upto(candidate, "production_composition.plants", day)]
    prod_par = [_series_upto(parent, "production_composition.animals", day),
                _series_upto(parent, "production_composition.plants", day)]
    prod_dist = sum(_l1_dist(a, b) for a, b in zip(prod_cand, prod_par)) / 2

    lab_cand = [_series_upto(candidate, "labor_allocation.travel_share", day),
                _series_upto(candidate, "labor_allocation.idle_share", day),
                _series_upto(candidate, "labor_allocation.work_share", day)]
    lab_par = [_series_upto(parent, "labor_allocation.travel_share", day),
               _series_upto(parent, "labor_allocation.idle_share", day),
               _series_upto(parent, "labor_allocation.work_share", day)]
    lab_dist = sum(_l1_dist(a, b) for a, b in zip(lab_cand, lab_par)) / 3

    distances = {"investment_sequence": round(inv_dist, 4), "production_composition": round(prod_dist, 4),
                 "labor_allocation": round(lab_dist, 4)}

    triggered = None
    if inv_dist >= th["investment_seq_min_dist"]:
        triggered = "investment_sequence"
    elif prod_dist >= th["production_composition_min_dist"]:
        triggered = "production_composition"
    elif lab_dist >= th["labor_allocation_min_dist"]:
        triggered = "labor_allocation"

    cand_seq = extract_state_sequence(Trajectory(candidate.label, candidate.seat, candidate.days[: day + 1]))
    par_seq = extract_state_sequence(Trajectory(parent.label, parent.seat, parent.days[: day + 1]))
    state_diverged = state_order_signature(cand_seq) != state_order_signature(par_seq)

    return NoveltyResult(passed=triggered is not None, day=day, distances=distances,
                          triggered_by=triggered, state_sequence_diverged=state_diverged)
