"""arch_search/hypothesis.py -- causal hypothesis schema (data structures only, no LLM
automation in this phase -- see spec section 7 / STOP CONDITIONS)."""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any


@dataclass
class Hypothesis:
    hypothesis_id: str
    structural_divergence: Dict[str, Any]     # a Divergence.as_dict() this hypothesis is about
    causal_claim: str                          # one sentence, mechanism not metric
    prediction_steps: List[str] = field(default_factory=list)   # ordered, falsifiable, multi-step
    falsification_conditions: List[str] = field(default_factory=list)
    mechanism_class: str = "structural"        # "structural" | "consequential" (see classify note below)

    def as_dict(self):
        return asdict(self)


MECHANISM_TAXONOMY = {
    "structural": (
        "A different state-transition graph: different entry conditions, different "
        "transition order, or a panel-convergent state the candidate skips or reaches via "
        "a different trigger. Only these become hypothesis seeds (spec 2.6)."
    ),
    "consequential": (
        "A downstream effect of an upstream divergence already found earlier in the state "
        "sequence -- correlated, not causal on its own. Never a hypothesis seed by itself."
    ),
}
