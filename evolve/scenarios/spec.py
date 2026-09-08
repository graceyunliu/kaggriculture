"""Scenario definition vocabulary (AGE-333).

A diagnostic scenario is a *self-contained* description of a game world plus the pass/fail
rule applied to the candidate's trajectory in it. Nothing here knows how to run a game --
`runner.py` does that -- so a scenario module stays readable and editable on its own.

    Scenario(name, question, description, config, seeds, exempt_when, fail_when)

Pass/fail semantics, in order:

  1. any `exempt_when` criterion true   -> PASS  ("the candidate never took the bait")
  2. any `fail_when` criterion true     -> FAIL  (explanation names every tripped criterion)
  3. otherwise                          -> PASS

`exempt_when` exists because several of the ticket's pass conditions are disjunctive -- e.g.
"does not buy cows beyond what the market supports; OR buys but sells before they become a
liability". The first clause is an exemption (the failure mode was never entered), the second
is the absence of a fail condition.

Criteria are plain (metric, op, threshold) triples over the flat metric dict that
`metrics.scenario_metrics()` derives from a trace, so retuning a threshold is a one-line edit
and the report can always say which number triggered a verdict.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass

OPS = {
    "<": lambda a, b: a < b,
    "<=": lambda a, b: a <= b,
    ">": lambda a, b: a > b,
    ">=": lambda a, b: a >= b,
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
}


@dataclass(frozen=True)
class Criterion:
    """One threshold test over a derived metric.

    metric:    key of metrics.scenario_metrics(); `why` explains what the number means so the
               diagnostic report can print a sentence rather than a bare comparison.
    """
    metric: str
    op: str
    threshold: float
    why: str

    def __post_init__(self):
        if self.op not in OPS:
            raise ValueError(f"Criterion {self.metric!r}: unknown op {self.op!r} (have {sorted(OPS)})")

    def evaluate(self, metrics):
        """(tripped, value). A metric the trace could not produce is never tripped -- a missing
        number must not be read as evidence either way."""
        v = metrics.get(self.metric)
        if v is None:
            return False, None
        return OPS[self.op](v, self.threshold), v

    def text(self, value=None):
        shown = "n/a" if value is None else (f"{value:,.2f}".rstrip("0").rstrip(".") if isinstance(value, float) else f"{value:,}")
        return f"{self.metric} {self.op} {self.threshold} (actual {shown}) -- {self.why}"


@dataclass(frozen=True)
class Scenario:
    name: str
    question: str            # the diagnostic question, one line, from the ticket
    description: str         # what the world looks like and why it isolates that question
    config: dict             # mini_engine / kaggriculture.json configuration overrides
    seeds: tuple = (1, 2, 3)
    exempt_when: tuple = ()  # any true -> PASS regardless of fail_when
    fail_when: tuple = ()    # any true -> FAIL
    opponent: str = None     # None -> the frontier from Opponents/frontier.txt
    engine: str = "master"
    notes: str = ""          # deviations from the ticket's literal setup, recorded honestly
    report_metrics: tuple = ()  # extra metrics worth printing next to the verdict

    def config_sha(self):
        payload = json.dumps({"config": self.config, "seeds": list(self.seeds), "engine": self.engine},
                             sort_keys=True)
        return hashlib.sha256(payload.encode()).hexdigest()[:12]

    def criteria_metrics(self):
        return tuple(dict.fromkeys([c.metric for c in self.exempt_when] + [c.metric for c in self.fail_when]
                                   + list(self.report_metrics)))

    def evaluate(self, metrics):
        """Apply the criteria to one aggregated metric dict. Returns a verdict dict."""
        for c in self.exempt_when:
            tripped, value = c.evaluate(metrics)
            if tripped:
                return {"passed": True, "reason": "exempt", "trigger": c.metric,
                        "explanation": f"PASS (not exercised): {c.text(value)}",
                        "criteria": [{"kind": "exempt", "metric": c.metric, "op": c.op,
                                      "threshold": c.threshold, "value": value, "tripped": True,
                                      "why": c.why}]}
        tripped_list = []
        detail = []
        for c in self.fail_when:
            tripped, value = c.evaluate(metrics)
            detail.append({"kind": "fail", "metric": c.metric, "op": c.op, "threshold": c.threshold,
                           "value": value, "tripped": bool(tripped), "why": c.why})
            if tripped:
                tripped_list.append(c.text(value))
        if tripped_list:
            return {"passed": False, "reason": "fail_criteria",
                    "trigger": next(d["metric"] for d in detail if d["tripped"]),
                    "explanation": "FAIL: " + "; ".join(tripped_list), "criteria": detail}
        return {"passed": True, "reason": "no_fail_criteria_tripped", "trigger": None,
                "explanation": "PASS: no fail criterion tripped ("
                               + ", ".join(c.text(d["value"]) for c, d in zip(self.fail_when, detail)) + ")",
                "criteria": detail}
