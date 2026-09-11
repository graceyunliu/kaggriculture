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
    ("knob_space_local_optimum_sweep", "no_general_fix",
     "20-knob one-at-a-time dev h2h sweep of the chassis's live KNOBS defaults: 18 of 20 nudges flat-to-negative (a 3rd starting COW/SHEEP is -31k/-35k; load_per_hand and open_wheat are interior optima in either direction). The current default knob values already sit at or near a local optimum in this space.",
     "evolve/directions.yaml#knob_space_local_optimum_sweep", "2026-09-11"),
    ("demand_share_up", "rejected",
     "demand_share 0.55 -> 0.65 won the dev h2h screen (+1,350) but reversed on the real 4-tape panel (margin -503, own -1,663) -- h2h vs the O26 clone alone is a weak signal for this class of knob.",
     "evolve/directions.yaml#demand_share_up", "2026-09-11"),
    ("animal_scale_expansion_reachability_fix", "rejected",
     "Fixed the real reachability confound first (land_reserve/max_sheep/geese_day_limit exposed as knobs, verified causal via smoke test, byte-identical at defaults) then re-tested herd scale -- so this supersedes the earlier goose_animal_class result by ruling in the underlying species/land economics, not just geese. Cows: expansion reaches a real demand_room (milk-market) plateau; max_cow 26 == 32 byte-identical outcome, no validated economic gain. Sheep: full validation, 360 games / 3 opponents (tape_feeltheagi + 2 synthetic), sheep_max32_land0 vs O26 baseline -- own money negative in every single panel (-7.9k..-11.3k); margin sign flips by opponent (-332 vs the live tape, +447/+710 vs synthetic ones), all |t|<0.35. Geese: reachable after fixing the day<=3 timing gate, but directionally negative in the exploratory sweep, consistent with the prior goose_animal_class finding -- cash competition with early hires/feed is the real cost, not unreachability. Net: extra sheep can improve relative margin against some opponents by depressing the shared wool market, but the agent's own economy deteriorates every time, so it is not promotable. The apparent hidden-animal-cap opportunity was falsified: the real ceiling is market saturation (demand_room), not an inaccessible chassis parameter -- MAX_SHEEP=14 and the geese day<=3 gate were red herrings, not the actual constraint.",
     "tools/regime_experiment/O26_REACH.py, tools/regime_experiment/marginal_sweep.py, tools/regime_experiment/validate_sheep.py", "2026-09-11"),
    ("shed_overflow_wheat_only_gate_sell_genes", "rejected",
     "CORRECTED Sep 11 (same session): the A/B/C null is real (all four configs identical to the decimal, own money +552/margin/discard-dollars/wheat-buys unchanged across baseline/A/B/A+B, 160 games/config) but the premise underneath it was a measurement artifact, not a real mechanism. My own shed-discard pricing pass ($18,965/80 games, 46% of games affected) used a shed-drop simulation that snapshotted carried inventory at the START of the day's last hour, before that hour's own DROP actions run -- one hour too early. Cross-checked against tools/shed_overflow.py (hooks the engine's real _drop_inventories_to_shed directly, no reimplementation) on the identical seeds/opponent (11-30, tape_alaylm): 0 discard events, 0 units, every game -- reproduced independently in this session, matching a separate/concurrent pass already in evolve/directions.yaml's shed_capacity_margin_calibration resolution. So: occupancy genuinely reaches 100 regularly (confirmed both ways), but the shed_load>75/80 triggers already prevent every real discard; there was never a real discard-dollar opportunity for the wheat_buy_gate/wheat_sell_override genes to fail to capture. Do not re-attempt shed-overflow interventions on this chassis without a NEW instrument showing real (engine-function-hooked, not reimplemented) discard events -- the mechanism itself is closed, not just these two genes.",
     "tools/shed_overflow.py, tools/regime_experiment/O26_SHED.py, tools/regime_experiment/shed_gene_family.py", "2026-09-11"),
    ("o26_open_wheat9_fert_carry1", "rejected",
     "Manus factorial: +$1,942 on development reversed to -$817 (t=-1.35) on fresh seeds 71-90; fitted seed-set interaction, not an O26 improvement.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
    ("o26_melon_max_tiles_knob", "exhausted",
     "MELON_MAX_TILES produced zero factorial effect and is not consumed by the exact-O26 decision path; removed from active search.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
    ("single_dev_block_promotion", "rejected",
     "A ten-seed t/margin pre-screen can reject candidates before the required three-block pooled decision; all three dev blocks must run before promotion is decided.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
    ("bf757c08b2cc_behavioral_bundle", "rejected",
     "Corrected three-block evaluation: +2010.6/+43.6/+1233.4 by block, pooled +1095.9 with t=1.85. Failed both pooled gates; fresh seeds 111-150 were not touched.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
    ("cloud_7a735e93b1b9_panel_failure", "rejected",
     "Pooled dev +1989 and held-out +2576 did not generalize to the historical panel: margin delta -2748 and own-money delta -2016.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
    ("cloud_26bb1ab37c2d_population_failure", "rejected",
     "Pooled dev +3380 and held-out +2703 passed the historical panel, then failed population validation: margin delta -3344 and own-money delta -4775.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
    ("f01cec5376e1_rapid_parameter_bundle", "rejected",
     "Three-block dev +5934 (t=6.29) shrank to +2677 with t=1.67 and 10-10 on confirmation seeds 111-130; failed confirmation and never reached population.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
    ("global_hard_veto_capital_lookahead", "rejected",
     "All eight 2/4-day reserve-gate cells lost every dev block; best was -125913/game (t=-28.25). Reserving future inputs before every purchase starves the farm of investments needed to generate future cash.",
     "docs/cloud-evolution-results-sep11.md", "2026-09-11"),
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
        for col, decl in (("island", "TEXT DEFAULT 'c1'"), ("blocks", "TEXT"), ("ablation", "TEXT"), ("diagnosis", "TEXT"), ("exec_summary", "TEXT"), ("trajectory_summary", "TEXT"), ("failure_profile", "TEXT"), ("action_table", "TEXT"), ("dev_blocks", "TEXT"), ("population_margin", "REAL"), ("population_own", "REAL"), ("ladder_status", "TEXT")):
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
