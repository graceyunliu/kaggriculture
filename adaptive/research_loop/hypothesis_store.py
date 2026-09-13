"""
hypothesis_store.py -- Adaptive Research Loop v0.1

Persistent hypothesis registry at adaptive/research_loop/hypotheses.json.
This is the "research learner" layer: it tracks which explanations for
ladder behavior are plausible, what evidence bears on them, and how
confident we are -- kept deliberately separate from the gameplay learner
(adaptive/*.py, the frozen A/B controller) and from candidate lineage
(experiment_ledger.py). See ADAPTIVE_RESEARCH_LOOP_V0_1_REPORT.md section
"Three layers of learning" for why these are not merged.

Confidence is QUALITATIVE by design (spec requirement: no fake numerical
confidence without a defined statistical basis): one of
NO_EVIDENCE, WEAK, MODERATE, STRONG, and each level's meaning is fixed
here rather than left to the caller's judgment call each time.
"""
from __future__ import annotations

import json
import os
from typing import Optional

STORE_PATH = os.path.join(os.path.dirname(__file__), "hypotheses.json")

STATUSES = ("NEW", "ACTIVE", "SUPPORTED", "WEAKENED", "REJECTED", "INCONCLUSIVE")

CONFIDENCE_LEVELS = {
    "NO_EVIDENCE": "No experiment has tested this hypothesis yet.",
    "WEAK": "Tested by <=1 ladder submission, or evidence is confounded "
            "(no matched pairing / small n / plausible alternative explanation).",
    "MODERATE": "Tested by >=2 independent ladder submissions or by both an "
                "offline study and >=1 ladder submission, pointing the same "
                "direction, but still short of a controlled matched comparison.",
    "STRONG": "Tested by a matched/controlled comparison (shared opponents or "
              "seeds, or a designed ablation) with a consistent direction "
              "across repeats.",
}

REQUIRED_FIELDS = [
    "hypothesis_id", "statement", "supporting_evidence", "contradicting_evidence",
    "experiments", "status", "confidence", "last_tested", "next_test_priority",
    "source",
]


def _load() -> dict:
    if not os.path.exists(STORE_PATH):
        return {"hypotheses": []}
    with open(STORE_PATH) as f:
        return json.load(f)


def _save(data: dict) -> None:
    os.makedirs(os.path.dirname(STORE_PATH), exist_ok=True)
    tmp = STORE_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, STORE_PATH)


def all_hypotheses() -> list[dict]:
    return _load()["hypotheses"]


def get(hypothesis_id: str) -> Optional[dict]:
    for h in all_hypotheses():
        if h["hypothesis_id"] == hypothesis_id:
            return h
    return None


def upsert(hyp: dict) -> dict:
    missing = [f for f in REQUIRED_FIELDS if f not in hyp]
    if missing:
        raise ValueError(f"hypothesis missing required fields: {missing}")
    if hyp["status"] not in STATUSES:
        raise ValueError(f"bad status {hyp['status']!r}, must be one of {STATUSES}")
    if hyp["confidence"] not in CONFIDENCE_LEVELS:
        raise ValueError(f"bad confidence {hyp['confidence']!r}, must be one of "
                          f"{list(CONFIDENCE_LEVELS)}")
    data = _load()
    hyps = data["hypotheses"]
    for i, h in enumerate(hyps):
        if h["hypothesis_id"] == hyp["hypothesis_id"]:
            hyps[i] = hyp
            _save(data)
            return hyp
    hyps.append(hyp)
    _save(data)
    return hyp


def record_evidence(hypothesis_id: str, *, experiment_candidate_id: str,
                     direction: str, note: str) -> dict:
    """direction: 'supports' | 'contradicts'. Appends to the hypothesis's
    evidence lists; does not itself change status/confidence (that is a
    deliberate call made by diagnostic_engine.py, which justifies the
    change and writes the new status/confidence via upsert())."""
    h = get(hypothesis_id)
    if h is None:
        raise ValueError(f"unknown hypothesis_id {hypothesis_id!r}")
    entry = {"experiment": experiment_candidate_id, "note": note}
    if direction == "supports":
        h["supporting_evidence"].append(entry)
    elif direction == "contradicts":
        h["contradicting_evidence"].append(entry)
    else:
        raise ValueError("direction must be 'supports' or 'contradicts'")
    if experiment_candidate_id not in h["experiments"]:
        h["experiments"].append(experiment_candidate_id)
    return upsert(h)


if __name__ == "__main__":
    for h in all_hypotheses():
        print(f"{h['hypothesis_id']:6s} [{h['status']:11s} conf={h['confidence']:8s}] "
              f"{h['statement'][:80]}")
