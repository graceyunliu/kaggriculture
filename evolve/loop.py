#!/usr/bin/env python3
"""Autonomous evolution loop over the K.py parameter space.

    python3 evolve/loop.py --hours 8 --jobs 7
    python3 evolve/loop.py --minutes 15            # quick check

Population = every candidate that reached the dev stage (status alive/held_*), ranked by
paired dev margin vs the FIXED frontier opponent for this run. Parents are drawn by
tournament from the top of that ranking, plus MAP-Elites-style draws from behavioural
cells so distinct economies survive as parents. Children come from Gaussian mutation
(70%) or uniform crossover (30%). Held-out results are reported, never used for selection.

The yardstick (frontier + clone opponents) is fixed for the whole run so every score in a
run is comparable. Promote a held-out winner to the next run's --frontier by hand.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import signal
import sys
import time
from collections import defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT))

import space  # noqa: E402
from cascade import DEFAULTS, close_pool, get_pool, run_cascade  # noqa: E402
from db import DB  # noqa: E402
import report as report_mod  # noqa: E402

LOG_DIR = HERE / "logs"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]


def cell_of(desc):
    if not desc:
        return None
    d = json.loads(desc) if isinstance(desc, str) else desc
    return (d.get("animals_d15", 0) // 3, d.get("land_final", 0), d.get("hands_max", 0) // 3)


def pick_parent(alive, rng):
    """alive: list of dicts sorted by dev_margin desc."""
    if not alive:
        return None
    u = rng.random()
    if u < 0.25:  # MAP-Elites draw: best candidate of a random behavioural cell
        cells = {}
        for c in alive:
            k = cell_of(c.get("descriptor"))
            if k is not None and k not in cells:
                cells[k] = c
        if cells:
            return rng.choice(list(cells.values()))
    if u < 0.35:  # pure exploration
        return rng.choice(alive)
    top = alive[:30]
    return max(rng.sample(top, min(3, len(top))), key=lambda c: c["dev_margin"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=0.0)
    ap.add_argument("--minutes", type=float, default=0.0)
    ap.add_argument("--max-candidates", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=None)
    ap.add_argument("--frontier", default=str(ROOT / "candidates" / "V3_12.py"))
    ap.add_argument("--clone", default=str(ROOT / "Opponents" / "opp_scenario_v14.py"))
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--smoke-floor", type=float, default=DEFAULTS["smoke_floor"])
    ap.add_argument("--dev-promote", type=float, default=DEFAULTS["dev_promote"])
    ap.add_argument("--mutation-rate", type=float, default=0.2)
    ap.add_argument("--sigma", type=float, default=0.2)
    ap.add_argument("--db", default=None)
    ap.add_argument("--base", default=None,
                    help="chassis file to snapshot (default candidates/K.py); pass a previous evolve/base/K_<sha>.py "
                         "to continue a population on the same code")
    args = ap.parse_args()

    budget = args.hours * 3600 + args.minutes * 60
    run_id = args.run_id or datetime.now().strftime("%Y%m%d-%H%M")
    rng = random.Random(args.seed if args.seed is not None else int(time.time()))
    LOG_DIR.mkdir(exist_ok=True)
    logf = open(LOG_DIR / f"{run_id}.log", "a")

    def log(msg):
        line = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"
        print(line, flush=True)
        logf.write(line + "\n")
        logf.flush()

    get_pool(args.jobs)   # start workers before anything else is open
    db = DB(args.db) if args.db else DB()
    cfg = {"smoke_floor": args.smoke_floor, "dev_promote": args.dev_promote,
           "dev_promote_t": DEFAULTS["dev_promote_t"], "engine": "master",
           "mutation_rate": args.mutation_rate, "sigma": args.sigma, "jobs": args.jobs}
    engine_sha = sha(ROOT / "vendor" / "kaggle_environments_engine_master" / "kaggriculture.py")
    snap, k_sha = space.freeze_base(args.base) if args.base else space.freeze_base()
    cfg["base"] = str(snap)
    db.start_run(run_id, engine_sha, k_sha, args.frontier, args.clone, cfg)
    log(f"run {run_id}: engine={engine_sha} chassis={snap.name} frontier={Path(args.frontier).name} "
        f"clone={Path(args.clone).name} budget={budget/3600:.2f}h jobs={args.jobs}")

    stop = {"flag": False}
    main_pid = os.getpid()

    def _stop(signum, _frame):
        if os.getpid() != main_pid:      # pool workers inherit the handler; only the driver should react
            return
        stop["flag"] = True
        log(f"signal {signum}: stop requested; finishing current candidate")

    signal.signal(signal.SIGTERM, _stop)
    signal.signal(signal.SIGINT, _stop)

    t_start = time.time()
    stats = defaultdict(int)
    gen = 0

    def evaluate(params, parents, origin):
        key = space.params_key(params)
        if db.get(key):
            stats["dup"] += 1
            return None
        path = space.render(params)
        db.insert(key, params, run_id, gen, parents, origin, path)
        ref = parents[0] if parents else None
        pdesc = ""
        if ref:
            pp = json.loads(db.get(ref)["params"])
            pdesc = " ".join(f"{k}:{a}->{b}" for k, (a, b) in space.diff(params, pp).items())
        log(f"#{stats['evaluated']+1} {origin} {key} {pdesc}")
        status = run_cascade(db, key, path, args.frontier, args.clone, cfg, jobs=args.jobs, log=log)
        stats["evaluated"] += 1
        stats[status] += 1
        return status

    # ---- seed population
    for name, p in (("V3_12", space.base_params()), ("C1", space.c1_params())):
        key = space.params_key(p)
        if not db.get(key):
            log(f"seeding {name}")
            evaluate(p, [], f"seed:{name}")
        else:
            log(f"seed {name} already in DB ({key})")

    # ---- main loop
    try:
        while not stop["flag"]:
            if budget and time.time() - t_start > budget:
                log("time budget reached")
                break
            if args.max_candidates and stats["evaluated"] >= args.max_candidates:
                log("candidate budget reached")
                break
            alive = db.alive()
            gen += 1
            if len(alive) >= 2 and rng.random() < 0.3:
                a, b = rng.sample(alive[:40], 2) if len(alive) >= 2 else (alive[0], alive[0])
                child = space.crossover(json.loads(a["params"]), json.loads(b["params"]), rng)
                evaluate(child, [a["key"], b["key"]], "crossover")
            else:
                parent = pick_parent(alive, rng)
                if parent is None:
                    log("no alive candidates to mutate; stopping")
                    break
                child = space.mutate(json.loads(parent["params"]), rate=cfg["mutation_rate"],
                                     sigma_frac=cfg["sigma"], rng=rng)
                evaluate(child, [parent["key"]], "mutate")
    finally:
        close_pool()
        elapsed = time.time() - t_start
        counts = db.counts(run_id)
        games = sum(g for _, g in counts.values())
        summary = {"elapsed_s": round(elapsed), "evaluated": stats["evaluated"], "counts": {k: v[0] for k, v in counts.items()},
                   "games": games, "games_per_hour": round(games / max(elapsed, 1) * 3600)}
        db.finish_run(run_id, summary)
        log(f"done: {json.dumps(summary)}")
        out = report_mod.write_report(db, run_id)
        log(f"report: {out}")
        logf.close()


if __name__ == "__main__":
    main()
