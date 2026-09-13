"""
experiment_ledger.py -- Adaptive Research Loop v0.1

Append-only, machine-readable record of every candidate/experiment in the
research loop. Backed by adaptive/research_loop/experiment_ledger.jsonl
(one JSON object per line, newest last). Never rewrites or deletes prior
lines -- corrections are new lines with `supersedes` set, never in-place edits.

This is provenance/bookkeeping only. It does not decide anything; see
experiment_selector.py and diagnostic_engine.py for the decision logic.
"""
from __future__ import annotations

import json
import os
from typing import Optional

LEDGER_PATH = os.path.join(os.path.dirname(__file__), "experiment_ledger.jsonl")

REQUIRED_FIELDS = [
    "candidate_id", "parent_candidate", "commit", "submission_id",
    "submission_timestamp", "hypothesis_id", "hypothesis", "rationale",
    "predicted_effect", "change_description", "changed_files",
    "controller_hash", "learner_hash", "o42_hash", "preflight_status",
    "ladder_result", "score", "wins", "losses", "draws", "games",
    "opponents", "observations", "diagnosis", "hypothesis_update", "decision",
]


def _now_placeholder_none(d: dict) -> dict:
    for k in REQUIRED_FIELDS:
        d.setdefault(k, None)
    return d


def read_all() -> list[dict]:
    if not os.path.exists(LEDGER_PATH):
        return []
    rows = []
    with open(LEDGER_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def get(candidate_id: str) -> Optional[dict]:
    for row in read_all():
        if row.get("candidate_id") == candidate_id:
            return row
    return None


def append_entry(entry: dict) -> dict:
    """Append one candidate/experiment record. Never overwrites an existing
    candidate_id -- call append_result_update() to record a later stage
    (e.g. ladder result arriving after the candidate was created
    pre-submission)."""
    entry = _now_placeholder_none(dict(entry))
    unknown = set(entry) - set(REQUIRED_FIELDS) - {"row_kind", "timestamp_written", "supersedes"}
    if unknown:
        raise ValueError(f"Unknown ledger fields (fix schema or the caller): {unknown}")
    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)
    with open(LEDGER_PATH, "a") as f:
        f.write(json.dumps(entry, sort_keys=True) + "\n")
    return entry


def append_result_update(candidate_id: str, **result_fields) -> dict:
    """Record that a ladder result arrived for an existing candidate_id.
    Writes a NEW line (row_kind='result_update') rather than mutating the
    original creation line, per the ledger's append-only / never-overwrite
    rule. effective_rows() folds these together for reading."""
    base = get(candidate_id)
    if base is None:
        raise ValueError(f"No prior ledger entry for candidate_id={candidate_id!r}; "
                          f"create it with append_entry() first.")
    row = {k: base.get(k) for k in REQUIRED_FIELDS}
    row.update(result_fields)
    row["row_kind"] = "result_update"
    return append_entry(row)


def effective_rows() -> list[dict]:
    """One row per candidate_id: the creation row merged with the latest
    result_update row (if any), most-recent field values winning field by
    field. This is a read-time fold -- the on-disk file is untouched."""
    by_id: dict = {}
    for row in read_all():
        cid = row.get("candidate_id")
        if cid is None:
            continue
        if cid not in by_id:
            by_id[cid] = dict(row)
        else:
            merged = dict(by_id[cid])
            for k, v in row.items():
                if v is not None:
                    merged[k] = v
            by_id[cid] = merged
    return list(by_id.values())


if __name__ == "__main__":
    rows = effective_rows()
    print(f"{len(rows)} candidate(s) in ledger: {[r.get('candidate_id') for r in rows]}")
