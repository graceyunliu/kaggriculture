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
    status TEXT DEFAULT 'new', -- new | noop | dead_pattern | dead_smoke | dead_dev | alive | held_fail | held_exploit | held_pass | error
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
    trajectory_summary TEXT,
    failure_profile TEXT,
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
CREATE TABLE IF NOT EXISTS rejected_mechanisms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mechanism_tag TEXT NOT NULL UNIQUE,
    verdict TEXT NOT NULL CHECK (verdict IN ('rejected','exhausted','no_general_fix')),
    one_line_cause TEXT NOT NULL,
    doc_ref TEXT NOT NULL,
    date TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_status ON candidates(status);
CREATE INDEX IF NOT EXISTS idx_dev ON candidates(dev_margin);
"""

REJECTED_MECHANISMS = (
    ("opponent_fingerprint_sizing", "rejected",
     "M2's opponent-purchase fingerprint and sell table are a fitted exploit, not a general sizing rule.",
     "docs/M3-general-sizing-results.md", "2026-09-05"),
    ("shared_market_inventory_threshold_fix", "no_general_fix",
     "The M3/V3_12 gap is shared-market chaos; an inventory-threshold branch would be opponent-specific overfitting.",
     "docs/M3-v3_12-regression-diagnosis.md", "2026-09-05"),
    ("blended_capital_labor_constraint", "rejected",
     "One constraint conflates lumpy setup capital with recurring labor capacity on different cash horizons.",
     "docs/planner-allocation-hiring-results.md", "2026-09-05"),
    # Sep 10-11 (O16..O26 programme; docs/economic-self-model.md, evolve/RULES.md)
    ("worker_matching_within_priorities", "exhausted",
     "Changing which free unit takes which current task saves ~26 tiles/game (<1% of travel); the orchestrator already captures it.",
     "evolve/RULES.md#Sep 10", "2026-09-10"),
    ("per_task_delay_value_at_risk", "rejected",
     "3,060 counterfactuals: delaying any single action 1-4 h has no consequence distinguishable from zero (all CIs through 0). Do not weight dispatch by per-task urgency.",
     "evolve/delay_panel_O16_summary.txt", "2026-09-10"),
    ("chronic_service_debt", "exhausted",
     "Service ledger: no obligation class is chronically late or under-served vs the tapes' own service on the same games; execution is not the gap.",
     "tools/service_ledger.py", "2026-09-11"),
    ("fertilizer_output_maximisation", "rejected",
     "More fertilized strawberry nights raise units but not own money (+0): strawberry demand is fixed, extra units only shift price share. Same-output-fewer-inputs pays; more-output does not.",
     "evolve/RULES.md#O23", "2026-09-11"),
    ("tape_wheat_portfolio_via_knobs", "exhausted",
     "wheat_per_animal / wheat_tiles / wheat_stock / wheat_hold_days / wheat_sell_price all fail a gate (three rounds). Holding wheat: own +1.4k but margin -0.6k because the tapes are net wheat sellers.",
     "evolve/RULES.md#wheat", "2026-09-11"),
    ("speculative_inventory_holding", "rejected",
     "Holding or metering MILK/WOOL/STRAWBERRY for a better price loses -1.8..-4.7k (O13); forecast-driven sale timing -0.6k. Sell immediately; the only timing gain is arrival-vs-pool-decay (melon morning).",
     "docs/hold-meter (Sep 9)", "2026-09-11"),
    ("input_price_attack_capital_timing", "rejected",
     "EXPLOIT class: extra mid-day wheat/fertilizer buying (capital checkpoint, capital_hour2) raises margin by lowering the opponent's money while lowering ours (-1.0..-2.6k own). Never core.",
     "tools/capital_events.py", "2026-09-10"),
    ("melon_convoy_interior_interruption", "rejected",
     "Any urgency-shaped hole in the h<=8 melon convoy (O30/O31/O32/O32B: any-urgent, catastrophic-only, orchestrator-assigned) loses on all four tapes at 1,440 games; edge trimming (h7) is a +$250 lead. Protected blocks tolerate edge trimming, not interior interruption.",
     "evolve/directions.yaml#strawberry_urgent_slack", "2026-09-11"),
    ("adaptive_melon_cutoff_on_entry_state", "rejected",
     "2,240-game h6-h10 sweep: the optimal cutoff does not move with day-9 farm state; segment argmax does not replicate.",
     "evolve/directions.yaml#adaptive_melon_timing", "2026-09-11"),
    ("deferred_melon_pickup_lost_sale", "rejected",
     "tools/melon_trace.py: every 6-unit melon is harvested and sold in both O26 and O32; the 8-11 unit delta is a d10-11 replant-count side-effect and money does not track melon units.",
     "evolve/directions.yaml#melon_commitment_recoverability", "2026-09-11"),
    ("melon_convoy_beyond_slack", "rejected",
     "BOUNDARY: melon morning pays only for units the animal routes do not need (h<=8, 6-unit tiles); to h12 or harvesting 5-unit tiles displaces feeding and goes negative.",
     "evolve/RULES.md#O22", "2026-09-11"),
    ("hire_gate_output_loss", "rejected",
     "Weed-recovery counterfactual at N=165 (every overnight-carry event, unbiased) is worth ~$0 (mean -28, median 0, d19-23 negative); with the fertilizer piece at 15-18% the accounting bridge covers <20% of the $504 residual, no concentrated class. Keep HIRE_MAX_MARGINAL=144 as is.",
     "evolve/directions.yaml#hire_gate_output_loss", "2026-09-11"),
    ("investment_readiness_buy_animal_marginal_sign", "exhausted",
     "32-cell x 2 independent seed-set marginal counterfactual: BUY_ANIMAL's sign flips between sets at every day 4-12. Not measurable at this panel size; leave the hand threshold.",
     "evolve/directions.yaml#investment_readiness_threshold", "2026-09-11"),
    ("land_deadline_tightening_to_marginal_decay", "rejected",
     "O33_LAND_DEADLINE_TIGHT (LAND_DEADLINE pulled in ~3-4 days/tier to match the marginal-value decay to 0 by day 12) loses on both own and margin, all four tapes on the stronger seed set. The single-unit marginal counterfactual doesn't see the option value of completing a quad early enough to use the extra tile-days; tightening the deadline throws that value away too.",
     "evolve/directions.yaml#land_deadline_horizon", "2026-09-11"),
    ("goose_animal_class", "rejected",
     "O34_GOOSE_TEST (chassis's disabled geese knob turned on, 4 GOOSE, affordability window widened from a dead day<=3 to day<=10): margin -7,058/-7,301 on two 20-seed sets, negative on all four tapes both sets, own money not even sign-consistent. A cheaper/faster-cycling animal class is not automatically profitable at this scale.",
     "evolve/directions.yaml#goose_animal_class", "2026-09-11"),
)


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
        self.conn.executemany(
            "INSERT OR IGNORE INTO rejected_mechanisms(mechanism_tag, verdict, one_line_cause, doc_ref, date) "
            "VALUES(?,?,?,?,?)", REJECTED_MECHANISMS)
        # Sep 11: INSERT OR IGNORE silently dropped 5 of 14 closed mechanisms whose verdict did not satisfy the table's
        # CHECK constraint, so the proposer was seeded with an incomplete closed set for a day. A partial seed is now a
        # hard failure: every tag in REJECTED_MECHANISMS must be present after seeding.
        seeded = {r[0] for r in self.conn.execute("SELECT mechanism_tag FROM rejected_mechanisms")}
        missing = [t[0] for t in REJECTED_MECHANISMS if t[0] not in seeded]
        if missing:
            raise RuntimeError(f"rejected_mechanisms seed incomplete -- {missing} were not inserted "
                               f"(verdict must be one of rejected/exhausted/no_general_fix; check the CHECK constraint)")
        cols = {r["name"] for r in self.conn.execute("PRAGMA table_info(candidates)")}
        for col, decl in (("island", "TEXT DEFAULT 'c1'"), ("blocks", "TEXT"), ("ablation", "TEXT"), ("diagnosis", "TEXT"), ("exec_summary", "TEXT"), ("trajectory_summary", "TEXT"), ("failure_profile", "TEXT"), ("action_table", "TEXT")):
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

    def alive(self, limit=None, island=None, k_sha=None, frontier=None):
        q = ("SELECT c.* FROM candidates c JOIN runs r ON r.run_id=c.run_id "
             "WHERE c.status IN ('alive','held_pass','held_fail','held_exploit') AND c.dev_margin IS NOT NULL")
        args = []
        if island:
            q += " AND c.island=?"
            args.append(island)
        if k_sha:
            q += " AND r.k_sha=?"
            args.append(k_sha)
        if frontier:
            # dev/held margins are only comparable within one yardstick; never mix candidates scored
            # against different frontiers into the same pool or leaderboard.
            q += " AND r.frontier=?"
            args.append(frontier)
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

    def rejected_mechanisms(self):
        return [dict(r) for r in self.conn.execute(
            "SELECT id, mechanism_tag, verdict, one_line_cause, doc_ref, date "
            "FROM rejected_mechanisms ORDER BY date, id")]

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
