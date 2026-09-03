"""SQLite population database for the evolution loop."""
from __future__ import annotations

import json
import os
import sqlite3
import time
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "evolve.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS candidates (
    key TEXT PRIMARY KEY,
    run_id TEXT,
    gen INTEGER,
    parents TEXT,
    origin TEXT,               -- seed | mutate | crossover
    params TEXT NOT NULL,
    path TEXT,
    created REAL,
    stage INTEGER DEFAULT 0,   -- highest stage completed
    status TEXT DEFAULT 'new', -- new | noop | dead_smoke | dead_dev | alive | held_fail | held_pass | error
    fingerprint TEXT,
    smoke_margin REAL,
    dev_margin REAL, dev_t REAL, dev_wins INTEGER, dev_losses INTEGER,
    clone_margin REAL, clone_t REAL,
    held_margin REAL, held_t REAL, held_wins INTEGER, held_losses INTEGER,
    held_clone_margin REAL,
    descriptor TEXT,
    island TEXT DEFAULT 'c1',
    blocks TEXT,
    ablation TEXT,
    diagnosis TEXT,
    exec_summary TEXT,
    games INTEGER DEFAULT 0,
    seconds REAL DEFAULT 0,
    note TEXT
);
CREATE TABLE IF NOT EXISTS runs (
    run_id TEXT PRIMARY KEY,
    started REAL, finished REAL,
    engine_sha TEXT, k_sha TEXT, frontier TEXT, clone TEXT,
    config TEXT, summary TEXT
);
CREATE INDEX IF NOT EXISTS idx_status ON candidates(status);
CREATE INDEX IF NOT EXISTS idx_dev ON candidates(dev_margin);
"""


def _journal_ok(directory):
    """Can SQLite use its normal rollback journal in this directory?"""
    probe = Path(directory) / f".probe-{os.getpid()}.db"
    try:
        c = sqlite3.connect(str(probe))
        c.execute("CREATE TABLE t(x)")
        c.execute("INSERT INTO t VALUES(1)")
        c.commit()
        c.close()
        return True
    except sqlite3.OperationalError:
        return False
    finally:
        for p in (probe, Path(str(probe) + "-journal")):
            try:
                p.unlink()
            except OSError:
                pass


class DB:
    def __init__(self, path=DB_PATH):
        self.path = Path(path)
        self.conn = sqlite3.connect(str(self.path), timeout=60)
        self.conn.row_factory = sqlite3.Row
        if not _journal_ok(self.path.parent):
            # FUSE/network mounts (e.g. the Cowork sandbox) refuse the rollback-journal file.
            # An in-memory journal works there; on a real disk (the Air) the default is kept.
            self.conn.execute("PRAGMA journal_mode=MEMORY")
        self.conn.executescript(SCHEMA)
        cols = {r["name"] for r in self.conn.execute("PRAGMA table_info(candidates)")}
        for col, decl in (("island", "TEXT DEFAULT 'c1'"), ("blocks", "TEXT"), ("ablation", "TEXT"), ("diagnosis", "TEXT"), ("exec_summary", "TEXT")):
            if col not in cols:
                self.conn.execute(f"ALTER TABLE candidates ADD COLUMN {col} {decl}")
        self.conn.commit()

    # -- candidates
    def get(self, key):
        r = self.conn.execute("SELECT * FROM candidates WHERE key=?", (key,)).fetchone()
        return dict(r) if r else None

    def insert(self, key, params, run_id, gen, parents, origin, path, island="c1", blocks=None):
        self.conn.execute(
            "INSERT OR IGNORE INTO candidates(key, run_id, gen, parents, origin, params, path, created, island, blocks) "
            "VALUES(?,?,?,?,?,?,?,?,?,?)",
            (key, run_id, gen, json.dumps(parents), origin, json.dumps(params), str(path), time.time(), island,
             json.dumps(blocks) if blocks else None))
        self.conn.commit()

    def update(self, key, **fields):
        cols = ", ".join(f"{k}=?" for k in fields)
        self.conn.execute(f"UPDATE candidates SET {cols} WHERE key=?", (*fields.values(), key))
        self.conn.commit()

    def add_games(self, key, n, seconds):
        self.conn.execute("UPDATE candidates SET games=games+?, seconds=seconds+? WHERE key=?", (n, seconds, key))
        self.conn.commit()

    def alive(self, limit=None, island=None, k_sha=None):
        q = ("SELECT c.* FROM candidates c JOIN runs r ON r.run_id=c.run_id "
             "WHERE c.status IN ('alive','held_pass','held_fail') AND c.dev_margin IS NOT NULL")
        args = []
        if island:
            q += " AND c.island=?"
            args.append(island)
        if k_sha:
            q += " AND r.k_sha=?"
            args.append(k_sha)
        q += " ORDER BY c.dev_margin DESC"
        if limit:
            q += f" LIMIT {int(limit)}"
        return [dict(r) for r in self.conn.execute(q, args)]

    def by_fingerprint(self, fp):
        r = self.conn.execute("SELECT key FROM candidates WHERE fingerprint=? AND status<>'noop' LIMIT 1", (fp,)).fetchone()
        return r["key"] if r else None

    def counts(self, run_id=None):
        q = "SELECT status, COUNT(*) n, SUM(games) g FROM candidates"
        args = ()
        if run_id:
            q += " WHERE run_id=?"
            args = (run_id,)
        q += " GROUP BY status"
        return {r["status"]: (r["n"], r["g"] or 0) for r in self.conn.execute(q, args)}

    def all(self, run_id=None):
        if run_id:
            return [dict(r) for r in self.conn.execute("SELECT * FROM candidates WHERE run_id=?", (run_id,))]
        return [dict(r) for r in self.conn.execute("SELECT * FROM candidates")]

    # -- runs
    def start_run(self, run_id, engine_sha, k_sha, frontier, clone, config):
        self.conn.execute("INSERT OR REPLACE INTO runs(run_id, started, engine_sha, k_sha, frontier, clone, config) "
                          "VALUES(?,?,?,?,?,?,?)",
                          (run_id, time.time(), engine_sha, k_sha, frontier, clone, json.dumps(config)))
        self.conn.commit()

    def finish_run(self, run_id, summary):
        self.conn.execute("UPDATE runs SET finished=?, summary=? WHERE run_id=?", (time.time(), json.dumps(summary), run_id))
        self.conn.commit()

    def run(self, run_id):
        r = self.conn.execute("SELECT * FROM runs WHERE run_id=?", (run_id,)).fetchone()
        return dict(r) if r else None
