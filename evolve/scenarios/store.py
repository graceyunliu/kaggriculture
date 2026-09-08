"""Persistence for scenario verdicts (AGE-333).

Owns its own table rather than adding columns to `candidates`, for the same reason the runner does
not live in cascade.py: a diagnostic must not be reachable from the ranking path by accident. It
shares evolve/evolve.db so results are queryable next to the candidate that produced them, but
db.py's schema is untouched and dropping `scenario_results` loses nothing the loop depends on.

    SELECT key, scenario, passed, trigger FROM scenario_results WHERE suite_version='v1';
    SELECT scenario, SUM(passed), COUNT(*) FROM scenario_results GROUP BY scenario;
"""
from __future__ import annotations

import json
import time

SCHEMA = """
CREATE TABLE IF NOT EXISTS scenario_results (
    key TEXT,                  -- candidate key, or NULL for an ad-hoc agent path
    agent TEXT NOT NULL,       -- agent file the verdict is about
    scenario TEXT NOT NULL,
    suite_version TEXT NOT NULL,
    opponent TEXT,
    seeds TEXT,
    passed INTEGER,            -- 1 pass, 0 fail, NULL inconclusive (agent errored in this world)
    trigger TEXT,              -- metric that decided the verdict
    explanation TEXT,          -- one sentence naming the number that decided it
    metrics TEXT,              -- JSON: seed-averaged metrics
    criteria TEXT,             -- JSON: every criterion with its value and whether it tripped
    per_seed TEXT,             -- JSON: per-seed money/errors/metrics
    seconds REAL,
    created REAL,
    PRIMARY KEY (agent, scenario, suite_version)
);
CREATE INDEX IF NOT EXISTS idx_scenario_key ON scenario_results(key);
CREATE INDEX IF NOT EXISTS idx_scenario_name ON scenario_results(scenario);
"""


def ensure_schema(conn):
    conn.executescript(SCHEMA)
    conn.commit()


def save_report(conn, report):
    """Upsert every scenario verdict in one run_suite() report."""
    ensure_schema(conn)
    now = time.time()
    rows = []
    for r in report["results"]:
        rows.append((report.get("key"), report["agent"], r["scenario"], report["suite_version"],
                     r.get("opponent"), json.dumps(r.get("seeds")),
                     None if r["passed"] is None else int(r["passed"]),
                     r.get("trigger"), r.get("explanation"),
                     json.dumps(r.get("metrics"), default=str), json.dumps(r.get("criteria"), default=str),
                     json.dumps(r.get("per_seed"), default=str), r.get("seconds"), now))
    conn.executemany(
        "INSERT OR REPLACE INTO scenario_results"
        "(key, agent, scenario, suite_version, opponent, seeds, passed, trigger, explanation,"
        " metrics, criteria, per_seed, seconds, created) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    conn.commit()
    return len(rows)


def _rows(conn, where="", args=()):
    ensure_schema(conn)
    q = "SELECT * FROM scenario_results"
    if where:
        q += " WHERE " + where
    q += " ORDER BY agent, scenario"
    return [dict(r) for r in conn.execute(q, args)]


def results_for(conn, agent=None, key=None, suite_version=None):
    """Stored verdicts for one agent path or candidate key."""
    where, args = [], []
    if agent:
        where.append("agent=?")
        args.append(str(agent))
    if key:
        where.append("key=?")
        args.append(key)
    if suite_version:
        where.append("suite_version=?")
        args.append(suite_version)
    return _rows(conn, " AND ".join(where), tuple(args))


def population(conn, suite_version=None):
    """Every stored verdict, for the population view of the report."""
    return _rows(conn, "suite_version=?" if suite_version else "",
                 (suite_version,) if suite_version else ())


def pass_rates(conn, suite_version=None):
    """scenario -> {pass, fail, inconclusive} counts across every agent diagnosed."""
    out = {}
    for r in population(conn, suite_version):
        d = out.setdefault(r["scenario"], {"pass": 0, "fail": 0, "inconclusive": 0})
        d["pass" if r["passed"] == 1 else ("fail" if r["passed"] == 0 else "inconclusive")] += 1
    return out


def reports_from_rows(rows):
    """Regroup stored rows back into per-agent report dicts (for rendering a report from the DB)."""
    by_agent = {}
    for r in rows:
        rep = by_agent.setdefault(r["agent"], {"key": r["key"], "agent": r["agent"],
                                               "suite_version": r["suite_version"],
                                               "opponent": r["opponent"], "results": [],
                                               "seconds": 0.0})
        rep["results"].append({
            "scenario": r["scenario"], "passed": None if r["passed"] is None else bool(r["passed"]),
            "trigger": r["trigger"], "explanation": r["explanation"],
            "metrics": json.loads(r["metrics"] or "{}"), "criteria": json.loads(r["criteria"] or "[]"),
            "per_seed": json.loads(r["per_seed"] or "[]"), "seeds": json.loads(r["seeds"] or "[]"),
            "seconds": r["seconds"] or 0.0, "errors": 0,
        })
        rep["seconds"] += r["seconds"] or 0.0
    for rep in by_agent.values():
        rep["n_pass"] = sum(x["passed"] is True for x in rep["results"])
        rep["n_fail"] = sum(x["passed"] is False for x in rep["results"])
        rep["n_inconclusive"] = sum(x["passed"] is None for x in rep["results"])
        rep["failed"] = [x["scenario"] for x in rep["results"] if x["passed"] is False]
    return list(by_agent.values())
