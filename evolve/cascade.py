"""Cascaded evaluator: fingerprint -> smoke -> dev -> held-out.

Every stage is paired, both seats, on the master (ladder) engine, via mini_engine
(results cached by file sha, so re-evaluating a known file is free).

Stage 0  fingerprint : 2 games (FP_SEEDS, seat 0) vs frontier. Per-day trace hash.
                       Identical to an already-evaluated candidate => no-op, skip.
Stage 1  smoke       : SMOKE_SEEDS both seats vs frontier. Errors or margin < smoke_floor => dead.
Stage 2  dev         : DEV_SEEDS both seats vs frontier, and vs clone. This is the ranking score.
Stage 3  held-out    : HELD_SEEDS both seats vs frontier (+ clone). Only for dev winners.
                       Never used for selection of parents -- reporting only.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402
sys.path.insert(0, str(ROOT / "evolve"))
import trace as trace_mod  # noqa: E402

FP_SEEDS = [1, 2]
SMOKE_SEEDS = [1, 2, 3]
DEV_SEEDS = list(range(1, 11))
HELD_SEEDS = list(range(11, 31))

DEFAULTS = {
    "smoke_floor": -6000.0,   # $/game paired margin below which a candidate dies at smoke
    "dev_promote": 1500.0,    # dev margin (vs frontier) needed to go to held-out
    "dev_promote_t": 2.0,
    "engine": "master",
}


def fingerprint_game(cand, frontier, engine="master"):
    """Two cached games (seeds FP_SEEDS, seat 0); returns (fingerprint, descriptor, seconds, errors).
    Two seeds so a change that happens not to fire on one seed is not misread as a no-op."""
    rs = get_pool().map(me._job, [(str(cand), str(frontier), s, engine, None, True, False) for s in FP_SEEDS])
    fp_src = json.dumps([{k: r["trace"][0][k] for k in ("money", "hands", "animals", "land")} for r in rs])
    fp = hashlib.sha256(fp_src.encode()).hexdigest()[:16]
    r = rs[0]
    tr = r["trace"][0]
    animals15 = tr["animals"][15] if len(tr["animals"]) > 15 else tr["animals"][-1]
    desc = {
        "animals_d15": int(animals15),
        "land_final": int(tr["land"][-1]),
        "hands_max": int(max(tr["hands"])) if tr["hands"] else 0,
        "money_d10": int(tr["money"][10]) if len(tr["money"]) > 10 else None,
    }
    errs = [sum(x["errors"][0] for x in rs), sum(x["errors"][1] for x in rs)]
    return fp, desc, sum(x.get("seconds", 0.0) for x in rs), errs


_POOL = None


def get_pool(jobs=None):
    """One persistent worker pool for the whole run (spawn context: identical behaviour on macOS and Linux,
    and no fork-after-sqlite/threads hazards)."""
    global _POOL
    if _POOL is None:
        import multiprocessing as mp
        n = jobs or max(1, (mp.cpu_count() or 2) - 1)
        _POOL = mp.get_context("spawn").Pool(n)
    return _POOL


def close_pool():
    global _POOL
    if _POOL is not None:
        _POOL.terminate()
        _POOL = None


def evaluate(a, b, seeds, engine="master", jobs=None):
    """Paired both-seats evaluation using the persistent pool. Same summary shape as mini_engine.evaluate."""
    jobs_list = []
    for s in seeds:
        jobs_list.append((str(a), str(b), s, engine, None, True, False))
        jobs_list.append((str(b), str(a), s, engine, None, True, True))
    results = get_pool(jobs).map(me._job, jobs_list)
    per_seed = {}
    for r in results:
        s = r["seed"]
        if not r["swapped"]:
            a_money, b_money, seat = r["money"][0], r["money"][1], 0
        else:
            a_money, b_money, seat = r["money"][1], r["money"][0], 1
        d = per_seed.setdefault(s, {"a": 0.0, "b": 0.0, "seat_margin": {}, "errors": [0, 0]})
        d["a"] += a_money
        d["b"] += b_money
        d["seat_margin"][seat] = a_money - b_money
        d["errors"][0] += r["errors"][0 if seat == 0 else 1]
        d["errors"][1] += r["errors"][1 if seat == 0 else 0]
    margins = [d["a"] - d["b"] for d in per_seed.values()]
    n = len(margins)
    mean = sum(margins) / n
    sd = (sum((m - mean) ** 2 for m in margins) / (n - 1)) ** 0.5 if n > 1 else 0.0
    t = mean / (sd / n ** 0.5) if sd > 0 else (float("inf") if mean > 0 else (float("-inf") if mean < 0 else 0.0))
    return {
        "mean_margin_per_game": mean / 2, "t": t,
        "wins": sum(m > 0 for m in margins), "losses": sum(m < 0 for m in margins),
        "agent_errors": [sum(d["errors"][0] for d in per_seed.values()), sum(d["errors"][1] for d in per_seed.values())],
        "per_seed": per_seed,
    }


def _eval(cand, opp, seeds, engine, jobs):
    t0 = time.time()
    r = evaluate(cand, opp, seeds, engine=engine, jobs=jobs)
    return r, time.time() - t0


def diagnose_candidate(db, key, cand_path, frontier, reference, engine="master", log=print):
    """Process-trace diagnosis of the candidate vs the reference agent (both seat 0 vs frontier, seed 1).
    One traced game for the candidate; the reference trace is cached. Stores text + execution summary."""
    try:
        rc = get_pool().apply(trace_mod.traced, (str(cand_path), str(frontier), 1, engine))
        rr = get_pool().apply(trace_mod.traced, (str(reference), str(frontier), 1, engine))
        d = trace_mod.diagnose(rc["trace"][0], rr["trace"][0], "cand", "C1")
        summ = trace_mod.summary_row(rc["trace"][0])
        db.update(key, diagnosis=d["text"], exec_summary=json.dumps(summ))
        log(f"    diag: {d['text'][:220]}")
        return d, summ
    except Exception as e:  # noqa: BLE001
        log(f"    diag failed: {e!r}"[:200])
        return None, None


def run_cascade(db, key, cand_path, frontier, clone, cfg, jobs=None, log=print):
    """Push one candidate through the cascade, updating the DB as it goes. Returns final status."""
    engine = cfg.get("engine", "master")
    # ---- stage 0: fingerprint
    try:
        fp, desc, secs, errs = fingerprint_game(cand_path, frontier, engine)
    except Exception as e:  # noqa: BLE001
        db.update(key, status="error", note=f"fingerprint: {e!r}")
        return "error"
    db.add_games(key, len(FP_SEEDS), secs)
    dup = db.by_fingerprint(fp)
    if dup and dup != key:
        db.update(key, status="noop", stage=0, fingerprint=fp, descriptor=json.dumps(desc), note=f"same trace as {dup}")
        return "noop"
    db.update(key, fingerprint=fp, descriptor=json.dumps(desc), stage=0)
    if sum(errs) > 0:
        db.update(key, status="dead_smoke", note=f"agent errors in fingerprint game: {errs}")
        return "dead_smoke"

    # ---- stage 1: smoke
    r, dt = _eval(cand_path, frontier, SMOKE_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(SMOKE_SEEDS), dt)
    db.update(key, smoke_margin=r["mean_margin_per_game"], stage=1)
    if cfg.get("reference"):
        diagnose_candidate(db, key, cand_path, frontier, cfg["reference"], engine, log)
    if r["agent_errors"][0] > 0:
        db.update(key, status="dead_smoke", note=f"agent errors: {r['agent_errors']}")
        return "dead_smoke"
    if r["mean_margin_per_game"] < cfg["smoke_floor"]:
        db.update(key, status="dead_smoke")
        return "dead_smoke"

    # ---- stage 2: dev (ranking score)
    r, dt = _eval(cand_path, frontier, DEV_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(DEV_SEEDS), dt)
    rc, dtc = _eval(cand_path, clone, DEV_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(DEV_SEEDS), dtc)
    db.update(key, stage=2, status="alive",
              dev_margin=r["mean_margin_per_game"], dev_t=r["t"], dev_wins=r["wins"], dev_losses=r["losses"],
              clone_margin=rc["mean_margin_per_game"], clone_t=rc["t"])
    log(f"    dev {r['mean_margin_per_game']:+,.0f} (t={r['t']:.1f}, {r['wins']}-{r['losses']})  "
        f"clone {rc['mean_margin_per_game']:+,.0f}")
    if not (r["mean_margin_per_game"] >= cfg["dev_promote"] and r["t"] >= cfg["dev_promote_t"]):
        return "alive"

    # ---- stage 3: held-out
    r, dt = _eval(cand_path, frontier, HELD_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(HELD_SEEDS), dt)
    rc, dtc = _eval(cand_path, clone, HELD_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(HELD_SEEDS), dtc)
    passed = r["mean_margin_per_game"] > 0 and r["t"] >= 2.0
    db.update(key, stage=3, status="held_pass" if passed else "held_fail",
              held_margin=r["mean_margin_per_game"], held_t=r["t"], held_wins=r["wins"], held_losses=r["losses"],
              held_clone_margin=rc["mean_margin_per_game"])
    log(f"    HELD-OUT {r['mean_margin_per_game']:+,.0f} (t={r['t']:.1f}, {r['wins']}-{r['losses']})  "
        f"clone {rc['mean_margin_per_game']:+,.0f}  -> {'PASS' if passed else 'fail'}")
    return "held_pass" if passed else "held_fail"
