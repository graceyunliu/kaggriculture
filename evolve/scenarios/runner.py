#!/usr/bin/env python3
"""Diagnostic scenario runner (AGE-333).

Separate from evolve/cascade.py by construction: it imports nothing from it, writes to its own
table, and no value it produces is read by ranking, promotion or parent selection. Running it on
a candidate is a read-only act as far as the evolution loop is concerned.

For each scenario it plays `seeds` traced games (candidate in seat 0 against the frontier tape,
under the scenario's engine config), derives whole-game metrics with metrics.scenario_metrics(),
averages them across seeds, and applies the scenario's criteria to get pass/fail plus the sentence
naming the number that decided it.

    python3 evolve/run_scenarios.py --agent candidates/C1.py
    python3 evolve/run_scenarios.py --agent candidates/C1.py --only idle_labor land_pressure
    python3 evolve/run_scenarios.py --from-db --frontier candidates/H32.py --md out.md

Caching: traced games are cached under evolve/scenarios/cache/ keyed by (agent sha, opponent sha,
engine, config, seed). trace.traced()'s own cache is NOT reusable here -- its key omits the engine
config, so a scenario run would collide with a default-config trace of the same pair.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
for _p in (str(ROOT), str(ROOT / "evolve"), str(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import trace as trace_mod            # noqa: E402
import metrics as metrics_mod        # noqa: E402
from registry import SUITE_VERSION, select  # noqa: E402

CACHE_DIR = HERE / "cache"
DEFAULT_FRONTIER = ROOT / "Opponents" / "frontier.txt"


def resolve_frontier(frontier=None):
    """Opponent for every scenario game. Defaults to the frontier tape named in
    Opponents/frontier.txt, which is what the cascade scores against."""
    if frontier:
        return str(Path(frontier))
    return str(ROOT / DEFAULT_FRONTIER.read_text().strip())


def _sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def _cache_key(agent, opponent, seed, engine, config, suite_version):
    cfg = hashlib.md5(json.dumps(config or {}, sort_keys=True).encode()).hexdigest()[:10]
    return f"{suite_version}_{_sha(agent)}_{_sha(opponent)}_{engine}_{cfg}_{seed}"


def _game_job(args):
    """One traced scenario game -> (seed, metrics, money, errors, seconds). Module-level and
    picklable so a spawn pool can run these in parallel."""
    agent, opponent, seed, engine, config, suite_version, use_cache = args
    key = _cache_key(agent, opponent, seed, engine, config, suite_version)
    f = CACHE_DIR / f"{key}.json"
    if use_cache and f.exists():
        try:
            with open(f) as fh:
                return json.load(fh)
        except Exception:  # noqa: BLE001 - a corrupt cache entry is just a cache miss
            pass
    t0 = time.time()
    r = trace_mod.run_traced(str(agent), str(opponent), seed, engine=engine, config=config or None)
    out = {"seed": seed, "money": r["money"][0], "opponent_money": r["money"][1],
           "errors": r["errors"][0], "seconds": round(time.time() - t0, 2),
           "metrics": metrics_mod.scenario_metrics(r["trace"][0])}
    if use_cache:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        with open(f, "w") as fh:
            json.dump(out, fh)
    return out


def run_scenario(scenario, agent, frontier=None, seeds=None, use_cache=True, pool=None):
    """Play one scenario on one agent. Returns a result dict with the verdict, the aggregated
    metrics and the per-seed rows behind them."""
    opponent = resolve_frontier(frontier)
    seeds = tuple(seeds or scenario.seeds)
    jobs = [(str(agent), opponent, s, scenario.engine, scenario.config, SUITE_VERSION, use_cache)
            for s in seeds]
    rows = pool.map(_game_job, jobs) if pool is not None else [_game_job(j) for j in jobs]
    agg = metrics_mod.aggregate([r["metrics"] for r in rows])
    errors = sum(r["errors"] for r in rows)
    if errors:
        # The candidate crashed inside this world. Its metrics describe a PASSing agent only because
        # it stopped acting, so the verdict is withheld rather than guessed.
        return {"scenario": scenario.name, "agent": str(agent), "opponent": opponent,
                "seeds": list(seeds), "passed": None, "trigger": "agent_errors",
                "explanation": f"INCONCLUSIVE: agent raised on {errors} turn(s) in this world; "
                               f"metrics are not a verdict on behaviour",
                "metrics": agg, "criteria": [], "per_seed": rows, "errors": errors,
                "seconds": round(sum(r["seconds"] for r in rows), 2)}
    verdict = scenario.evaluate(agg)
    return {"scenario": scenario.name, "agent": str(agent), "opponent": opponent,
            "seeds": list(seeds), "passed": verdict["passed"], "trigger": verdict["trigger"],
            "explanation": verdict["explanation"], "metrics": agg, "criteria": verdict["criteria"],
            "per_seed": rows, "errors": 0,
            "seconds": round(sum(r["seconds"] for r in rows), 2)}


def run_suite(agent, only=None, frontier=None, seeds=None, use_cache=True, jobs=None, key=None,
              log=None):
    """Run the selected scenarios on one agent. Returns a scenario_report dict."""
    scenarios = select(only)
    pool = _make_pool(jobs) if jobs and jobs > 1 else None
    try:
        results = []
        for sc in scenarios:
            r = run_scenario(sc, agent, frontier=frontier, seeds=seeds, use_cache=use_cache, pool=pool)
            results.append(r)
            if log:
                mark = {True: "PASS", False: "FAIL", None: "????"}[r["passed"]]
                log(f"  {sc.name:24s} {mark}  {r['explanation'][:150]}")
    finally:
        if pool is not None:
            pool.terminate()
    passed = [r for r in results if r["passed"] is True]
    failed = [r for r in results if r["passed"] is False]
    return {"key": key, "agent": str(agent), "suite_version": SUITE_VERSION,
            "opponent": resolve_frontier(frontier),
            "n_pass": len(passed), "n_fail": len(failed),
            "n_inconclusive": len(results) - len(passed) - len(failed),
            "failed": [r["scenario"] for r in failed], "results": results,
            "seconds": round(sum(r["seconds"] for r in results), 2)}


def _make_pool(jobs):
    import multiprocessing as mp
    return mp.get_context("spawn").Pool(jobs)


# ------------------------------------------------------------------ candidate selection (dev+)
def dev_candidates(db, frontier=None, island=None, limit=None):
    """Candidates that have reached the dev stage, best dev_margin first. Scenarios are a
    post-dev diagnostic: anything that died at fingerprint or smoke never played enough games for
    a trajectory to mean anything.

    `frontier` filters to one yardstick for the same reason db.alive() does -- candidates scored
    against different frontiers are not one population."""
    q = ("SELECT c.key, c.path, c.dev_margin, c.status, c.island FROM candidates c "
         "JOIN runs r ON r.run_id = c.run_id "
         "WHERE c.stage >= 2 AND c.status IN ('alive','held_pass','held_fail') AND c.path IS NOT NULL")
    args = []
    if frontier:
        q += " AND r.frontier=?"
        args.append(frontier)
    if island:
        q += " AND c.island=?"
        args.append(island)
    q += " ORDER BY c.dev_margin DESC"
    if limit:
        q += f" LIMIT {int(limit)}"
    return [dict(r) for r in db.conn.execute(q, args)]


def main(argv=None):
    ap = argparse.ArgumentParser(description="AGE-333 adversarial diagnostic scenarios "
                                             "(diagnostic only -- never feeds cascade ranking)")
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--agent", nargs="+", help="agent file(s) to diagnose")
    src.add_argument("--from-db", action="store_true", help="every candidate that reached dev")
    ap.add_argument("--only", nargs="+", default=None, help="subset of scenario names")
    ap.add_argument("--frontier", default=None, help="opponent tape (default: Opponents/frontier.txt)")
    ap.add_argument("--seeds", type=int, nargs="+", default=None, help="override the per-scenario seeds")
    ap.add_argument("--island", default=None)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--jobs", type=int, default=None, help="parallel games per scenario")
    ap.add_argument("--db", default=None, help="population DB (default evolve/evolve.db)")
    ap.add_argument("--no-store", action="store_true", help="do not write scenario_results")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--md", default=None, help="write the markdown diagnostic report here")
    ap.add_argument("--json", action="store_true", help="dump the raw reports as JSON")
    ap.add_argument("--list", action="store_true", help="print the scenario definitions and exit")
    args = ap.parse_args(argv)

    import store as store_mod
    import report as report_mod
    from registry import names as scenario_names

    if args.only:
        unknown = [n for n in args.only if n not in scenario_names()]
        if unknown:
            ap.error(f"unknown scenario(s) {unknown}; have {scenario_names()}")

    if args.list:
        for sc in select(args.only):
            print(f"{sc.name}\n  Q: {sc.question}\n  {sc.description}\n  config: {json.dumps(sc.config)[:200]}")
            for c in sc.exempt_when:
                print(f"  PASS if {c.metric} {c.op} {c.threshold}  -- {c.why}")
            for c in sc.fail_when:
                print(f"  FAIL if {c.metric} {c.op} {c.threshold}  -- {c.why}")
            if sc.notes:
                print(f"  note: {sc.notes}")
            print()
        return 0

    if not (args.agent or args.from_db):
        ap.error("one of --agent, --from-db or --list is required")

    targets = []
    db = None
    if args.from_db:
        import db as db_mod
        db = db_mod.DB(args.db) if args.db else db_mod.DB()
        rows = dev_candidates(db, frontier=args.frontier, island=args.island, limit=args.limit)
        targets = [(r["key"], r["path"]) for r in rows]
        if not targets:
            print("no candidate has reached dev for this frontier/island", file=sys.stderr)
            return 1
    else:
        targets = [(None, a) for a in args.agent]

    reports = []
    for key, path in targets:
        print(f"{Path(path).name}  ({key or 'ad-hoc'})")
        rep = run_suite(path, only=args.only, frontier=args.frontier, seeds=args.seeds,
                        use_cache=not args.no_cache, jobs=args.jobs, key=key, log=print)
        print(f"  -> {rep['n_pass']} pass / {rep['n_fail']} fail"
              + (f" / {rep['n_inconclusive']} inconclusive" if rep["n_inconclusive"] else "")
              + f"   {rep['seconds']}s")
        reports.append(rep)
        if not args.no_store:
            if db is None:
                import db as db_mod
                db = db_mod.DB(args.db) if args.db else db_mod.DB()
            store_mod.save_report(db.conn, rep)

    if args.json:
        print(json.dumps(reports, indent=1, default=str))
    if args.md:
        Path(args.md).write_text(report_mod.render(reports))
        print(f"wrote {args.md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
