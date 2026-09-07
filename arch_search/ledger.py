"""arch_search/ledger.py -- separate SQLite archive (arch_search/ledger.db), distinct from
evolve/evolve.db. Never delete falsified entries (spec section 10)."""
from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Any, Dict, Optional

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "arch_search" / "ledger.db"

FINDING_CLASSIFICATIONS = ("SUPPORTED", "PARTIALLY_SUPPORTED", "FALSIFIED",
                            "ARCHITECTURAL_DEAD_END", "INSUFFICIENT_EVIDENCE")

SCHEMA = """
CREATE TABLE IF NOT EXISTS candidates (
    candidate_id            TEXT PRIMARY KEY,
    family                  TEXT,
    parent                  TEXT,
    hypothesis              TEXT,   -- JSON
    mechanism_class         TEXT,
    reference_panel         TEXT,   -- JSON
    state_sequence          TEXT,   -- JSON
    first_divergence        TEXT,   -- JSON
    novelty_result          TEXT,   -- JSON
    cascade_result          TEXT,   -- JSON
    evaluation_result       TEXT,   -- JSON
    prediction_check        TEXT,   -- JSON
    finding_classification  TEXT,
    created_at               REAL,
    updated_at               REAL
);
"""


def get_conn(db_path: Optional[Path] = None) -> sqlite3.Connection:
    path = db_path or DB_PATH
    conn = sqlite3.connect(str(path))
    # the sandbox's FUSE-mounted repo filesystem doesn't support sqlite's default rollback
    # journal (raises "disk I/O error" on write) -- MEMORY journal mode works around it.
    conn.execute("PRAGMA journal_mode=MEMORY")
    conn.execute(SCHEMA)
    conn.commit()
    return conn


def _j(x):
    return json.dumps(x) if x is not None else None


def record_candidate(candidate_id: str, family: str, parent: Optional[str] = None,
                      hypothesis: Optional[Dict[str, Any]] = None, mechanism_class: Optional[str] = None,
                      reference_panel: Optional[Any] = None, state_sequence: Optional[Any] = None,
                      first_divergence: Optional[Any] = None, novelty_result: Optional[Any] = None,
                      cascade_result: Optional[Any] = None, evaluation_result: Optional[Any] = None,
                      prediction_check: Optional[Any] = None, finding_classification: Optional[str] = None,
                      db_path: Optional[Path] = None) -> None:
    """Insert or merge-update one candidate row. Never deletes -- repeated calls with the
    same candidate_id UPDATE fields (e.g. as a candidate progresses through the pipeline),
    they never remove the row, and callers must never call DELETE against this table for a
    falsified or dead-end finding (only INSUFFICIENT_EVIDENCE re-runs would normally update
    finding_classification, and even those keep the row)."""
    if finding_classification is not None and finding_classification not in FINDING_CLASSIFICATIONS:
        raise ValueError(f"finding_classification must be one of {FINDING_CLASSIFICATIONS}")
    conn = get_conn(db_path)
    now = time.time()
    existing = conn.execute("SELECT candidate_id FROM candidates WHERE candidate_id = ?",
                             (candidate_id,)).fetchone()
    fields = {
        "family": family, "parent": parent, "hypothesis": _j(hypothesis), "mechanism_class": mechanism_class,
        "reference_panel": _j(reference_panel), "state_sequence": _j(state_sequence),
        "first_divergence": _j(first_divergence), "novelty_result": _j(novelty_result),
        "cascade_result": _j(cascade_result), "evaluation_result": _j(evaluation_result),
        "prediction_check": _j(prediction_check), "finding_classification": finding_classification,
    }
    if existing:
        set_clause = ", ".join(f"{k} = COALESCE(?, {k})" for k in fields)
        conn.execute(f"UPDATE candidates SET {set_clause}, updated_at = ? WHERE candidate_id = ?",
                     (*fields.values(), now, candidate_id))
    else:
        cols = ["candidate_id"] + list(fields.keys()) + ["created_at", "updated_at"]
        vals = [candidate_id] + list(fields.values()) + [now, now]
        placeholders = ", ".join("?" for _ in cols)
        conn.execute(f"INSERT INTO candidates ({', '.join(cols)}) VALUES ({placeholders})", vals)
    conn.commit()
    conn.close()


def get_candidate(candidate_id: str, db_path: Optional[Path] = None) -> Optional[Dict[str, Any]]:
    conn = get_conn(db_path)
    row = conn.execute("SELECT * FROM candidates WHERE candidate_id = ?", (candidate_id,)).fetchone()
    if not row:
        conn.close()
        return None
    cols = [d[0] for d in conn.execute("SELECT * FROM candidates LIMIT 0").description]
    conn.close()
    out = dict(zip(cols, row))
    for k in ("hypothesis", "reference_panel", "state_sequence", "first_divergence", "novelty_result",
              "cascade_result", "evaluation_result", "prediction_check"):
        if out.get(k):
            out[k] = json.loads(out[k])
    return out


def list_candidates(family: Optional[str] = None, db_path: Optional[Path] = None) -> list:
    conn = get_conn(db_path)
    if family:
        rows = conn.execute("SELECT candidate_id FROM candidates WHERE family = ?", (family,)).fetchall()
    else:
        rows = conn.execute("SELECT candidate_id FROM candidates").fetchall()
    conn.close()
    return [r[0] for r in rows]
