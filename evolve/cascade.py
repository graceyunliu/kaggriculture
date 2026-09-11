"""Cascaded evaluator: fingerprint -> smoke -> dev -> held-out.

Every stage is paired, both seats, on the master (ladder) engine, via mini_engine
(results cached by file sha, so re-evaluating a known file is free).

Stage 0  fingerprint : 2 games (FP_SEEDS, seat 0) vs frontier. Per-day trace hash.
                       Identical to an already-evaluated candidate => no-op, skip.
Stage 1  smoke       : SMOKE_SEEDS both seats vs frontier. Errors or margin < smoke_floor => dead.
Stage 2  dev         : three disjoint seed blocks vs frontier; block 1 also scores the ranking panel.
                       Every block must be positive and the pooled result must clear the promotion gate.
Stage 3  held-out    : HELD_SEEDS both seats vs frontier (+ clone). Only for dev winners.
                       A quarantined population panel is then required for final local promotion.
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
import classify as classify_mod  # noqa: E402
import action_table as at  # noqa: E402  # AGE-359/AGE-360: action timing table extraction

FP_SEEDS = [1, 2]
SMOKE_SEEDS = [1, 2, 3]
DEV_SEEDS = list(range(1, 11))
DEV_CONFIRM_BLOCKS = [list(range(31, 41)), list(range(41, 51))]
# Seeds 11-30, 51-70, 71-110 were inspected during the Manus bootstrap/factorial
# trials. Keep them out of future selection claims. These ranges were preregistered
# before the broad behavioral run and have not been used to steer mutations.
# Perplexity evaluated held-out candidates on 111-130 and a population survivor
# on 131-149 before its sandbox crashed. Retire both declared ranges.
HELD_SEEDS = list(range(151, 171))
POPULATION_SEEDS = list(range(171, 191))
TRAJ_SEEDS = [1, 2, 3, 4, 5]   # AGE-331: subset of DEV_SEEDS, seat 0 vs frontier only, seed 1 reuses the
                                # smoke-stage diagnosis cache so this is ~4 extra games per alive candidate.

DEFAULTS = {
    "smoke_floor": -6000.0,   # $/game paired margin below which a candidate dies at smoke
    "dev_promote": 1500.0,    # dev margin (vs frontier) needed to go to held-out
    "dev_promote_t": 2.0,
    "engine": "master",
    "pattern_death_day": 12,
    "pattern_death_weeds": 3,
    "pattern_death_cash_days": 3,
    "pattern_death_enabled": True,
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
    return fp, desc, sum(x.get("seconds", 0.0) for x in rs), errs, tr


def pattern_death_reason(tr, cfg):
    """Return a conservative early-death reason from one existing fingerprint trace."""
    last_day = min(int(cfg["pattern_death_day"]), len(tr.get("animals", [])) - 1)
    mixes = tr.get("animal_mix", [])
    sales = tr.get("sales", [])
    for day in range(1, min(last_day + 1, len(mixes))):
        sold = sales[day - 1] if day - 1 < len(sales) else {}
        for species, previous in mixes[day - 1].items():
            if previous - mixes[day].get(species, 0) >= 1 and not sold.get(species):
                return f"animal escaped by day {day}: {species}"

    weeds = tr.get("weeds", [])
    weeds_created = sum(max(0, weeds[d] - weeds[d - 1])
                        for d in range(1, min(last_day + 1, len(weeds))))
    if weeds_created >= int(cfg["pattern_death_weeds"]):
        return f"{weeds_created} weeds created by day {last_day}"

    cash_days = sum(tr["money"][d] < 50 and tr["animals"][d] >= 3
                    for d in range(1, min(9, last_day + 1, len(tr["money"]), len(tr["animals"]))))
    if cash_days >= int(cfg["pattern_death_cash_days"]):
        return f"cash trap on {cash_days} days (days 1-8)"
    return None


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


def combine_results(results):
    """Pool disjoint paired-seed evaluations and recompute uncertainty from seed-level margins."""
    merged = {}
    errors = [0, 0]
    for result in results:
        overlap = set(merged) & set(result["per_seed"])
        if overlap:
            raise ValueError(f"development blocks overlap on seeds {sorted(overlap)}")
        merged.update(result["per_seed"])
        errors[0] += result["agent_errors"][0]
        errors[1] += result["agent_errors"][1]
    margins = [row["a"] - row["b"] for row in merged.values()]
    n = len(margins)
    mean = sum(margins) / max(1, n)
    sd = (sum((m - mean) ** 2 for m in margins) / (n - 1)) ** 0.5 if n > 1 else 0.0
    t = mean / (sd / n ** 0.5) if sd > 0 else (float("inf") if mean > 0 else (float("-inf") if mean < 0 else 0.0))
    return {"mean_margin_per_game": mean / 2, "t": t,
            "wins": sum(m > 0 for m in margins), "losses": sum(m < 0 for m in margins),
            "agent_errors": errors, "per_seed": merged}


def dev_blocks_pass(results, margin_floor, t_floor):
    """Require direction replication in every preregistered block plus a pooled statistical pass."""
    pooled = combine_results(results)
    consistent = all(result["mean_margin_per_game"] > 0 for result in results)
    return consistent and pooled["mean_margin_per_game"] >= margin_floor and pooled["t"] >= t_floor, pooled


def panel_list(clone):
    """`clone` may be one path or a comma-separated / list panel of fixed opponents (Sep 9: the 4 real
    ladder tapes). Returns a list of path strings."""
    if isinstance(clone, (list, tuple)):
        return [str(c) for c in clone]
    return [c.strip() for c in str(clone).split(",") if c.strip()]


def eval_panel(cand, clone, seeds, engine, jobs):
    """Paired margin of `cand` against every opponent in the panel; mean margin is the reported number.
    Per-opponent deltas at n=10-20 swing +-$15k on this game (shop-unlock lottery), so only the panel
    mean is used for any decision."""
    per = {}
    own = {}
    dt = 0.0
    errs = [0, 0]
    for opp in panel_list(clone):
        r, d = _eval(cand, opp, seeds, engine, jobs)
        per[Path(opp).stem] = r["mean_margin_per_game"]
        # own money per game (both seats): the intrinsic-economy axis. A margin gain with falling own money is an
        # opponent exploit (e.g. input-price attacks), not a better farm -- Sep 11 capital-checkpoint lesson.
        own[Path(opp).stem] = sum(x["a"] for x in r["per_seed"].values()) / (2.0 * max(1, len(r["per_seed"])))
        dt += d
        errs[0] += r["agent_errors"][0]
    mean = sum(per.values()) / max(1, len(per))
    own_mean = sum(own.values()) / max(1, len(own))
    return {"mean_margin_per_game": mean, "own_money_per_game": own_mean, "per_opp": per, "per_opp_own": own,
            "t": 0.0, "agent_errors": errs}, dt


def classify_gain(margin_delta, own_delta, noise=250.0):
    """Two-axis taxonomy of WHY a candidate wins vs the frontier on the tape panel (Sep 11).
    architecture: margin up AND own money up (promote).  exploit: margin up, own money down (opponent-specific; never
    core).  economic: own money up, margin ~flat (investigate / widen panel).  failure: both down.  neutral: both ~flat."""
    if margin_delta is None or own_delta is None:
        return "unknown"
    m_up, m_dn = margin_delta > noise, margin_delta < -noise
    o_up, o_dn = own_delta > noise, own_delta < -noise
    if m_up and o_up: return "architecture"
    if m_up and o_dn: return "exploit"
    if o_up and not m_up: return "economic"
    if m_dn and o_dn: return "failure"
    if m_up and not o_dn: return "architecture?"   # own money flat: weak evidence, still promotable
    return "neutral"


def diagnose_candidate(db, key, cand_path, frontier, reference, engine="master", log=print):
    """Process-trace diagnosis of the candidate vs the reference agent (both seat 0 vs frontier, seed 1).
    One traced game for the candidate; the reference trace is cached. Stores text + execution summary."""
    try:
        rc = get_pool().apply(trace_mod.traced, (str(cand_path), str(frontier), 1, engine))
        rr = get_pool().apply(trace_mod.traced, (str(reference), str(frontier), 1, engine))
        d = trace_mod.diagnose(rc["trace"][0], rr["trace"][0], "cand", "C1")
        summ = trace_mod.summary_row(rc["trace"][0])
        profile = classify_mod.classify_from_exec_summary(summ, d["text"])
        db.update(key, diagnosis=d["text"], exec_summary=json.dumps(summ), failure_profile=json.dumps(profile))
        log(f"    diag: {d['text'][:220]}")
        return d, summ
    except Exception as e:  # noqa: BLE001
        log(f"    diag failed: {e!r}"[:200])
        return None, None


def collect_trajectory_summary(cand_path, frontier, seeds, engine):
    """Traced games (seat 0 vs frontier) for an alive candidate, folded to a compact per-day summary
    (AGE-331). Seed 1 is normally already cached from the smoke-stage diagnosis, so this is ~len(seeds)-1
    new traced games. Does not touch the ranking score."""
    runs = [trace_mod.traced(str(cand_path), str(frontier), s, engine) for s in seeds]
    return trace_mod.fold_trace_to_summary([r["trace"][0] for r in runs], seeds=seeds)


def run_cascade(db, key, cand_path, frontier, clone, cfg, jobs=None, log=print):
    """Push one candidate through the cascade, updating the DB as it goes. Returns final status."""
    engine = cfg.get("engine", "master")
    # ---- stage 0: fingerprint
    try:
        fp, desc, secs, errs, fingerprint_trace = fingerprint_game(cand_path, frontier, engine)
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

    # ---- stage 0.5: pattern death (no extra game; uses the first fingerprint trace)
    if cfg.get("pattern_death_enabled", True):
        reason = pattern_death_reason(fingerprint_trace, cfg)
        if reason:
            profile = classify_mod.classify_from_pattern(reason)
            db.update(key, status="dead_pattern", stage=0, note=reason, failure_profile=json.dumps(profile))
            return "dead_pattern"

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
    rc, dtc = eval_panel(cand_path, clone, DEV_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(DEV_SEEDS) * len(panel_list(clone)), dtc)
    # panel delta = candidate's mean panel margin minus the frontier's own (cfg["frontier_panel_dev"],
    # computed once per run). This is the ladder-relevant number; self-play vs the frontier is not.
    fp_dev = cfg.get("frontier_panel_dev")
    fo_dev = cfg.get("frontier_panel_own_dev")
    panel_delta_dev = rc["mean_margin_per_game"] - fp_dev if fp_dev is not None else None
    own_delta_dev = rc["own_money_per_game"] - fo_dev if fo_dev is not None else None
    kind_dev = classify_gain(panel_delta_dev, own_delta_dev)
    db.update(key, stage=2, status="alive",
              dev_margin=r["mean_margin_per_game"], dev_t=r["t"], dev_wins=r["wins"], dev_losses=r["losses"],
              clone_margin=rc["mean_margin_per_game"], clone_t=rc["t"],
              note=f"panel_dev={rc['per_opp']} panel_delta_dev={panel_delta_dev} own_delta_dev={own_delta_dev} kind_dev={kind_dev}")
    log(f"    dev {r['mean_margin_per_game']:+,.0f} (t={r['t']:.1f}, {r['wins']}-{r['losses']})  "
        f"panel {rc['mean_margin_per_game']:+,.0f}" + (f" (delta vs frontier {panel_delta_dev:+,.0f}, own {own_delta_dev:+,.0f}, {kind_dev})" if panel_delta_dev is not None and own_delta_dev is not None else ""))

    # ---- trajectory summary + failure classification (AGE-331/AGE-332): cheap, post-alive,
    # never affects ranking/status. Also extract action timing table (AGE-359/AGE-360).
    try:
        summary = collect_trajectory_summary(cand_path, frontier, TRAJ_SEEDS, engine)
        db.update(key, trajectory_summary=json.dumps(summary))
        profile = classify_mod.classify_trajectory(summary, dev_margin=r["mean_margin_per_game"])
        db.update(key, failure_profile=json.dumps(profile))
        # Extract action timing table from the same traces (AGE-359/AGE-360)
        try:
            at_result = at.action_table_from_trace(summary)
            db.update(key, action_table=json.dumps(at_result))
        except Exception as e:  # noqa: BLE001
            log(f"    action_table failed: {e!r}"[:200])
    except Exception as e:  # noqa: BLE001
        log(f"    trajectory/classify failed: {e!r}"[:200])

    # Do not make a promotion decision from this noisy ten-seed block. The Sep 11
    # Manus broad run demonstrated the failure mode directly: bf757c08b2cc had
    # +$2,011 but t=1.9 here and was never allowed to reach the two replication
    # blocks. The contract is three blocks first, then one pooled decision.
    dev_results = [r]
    for block in cfg.get("dev_confirm_blocks", DEV_CONFIRM_BLOCKS):
        rb, dtb = _eval(cand_path, frontier, block, engine, jobs)
        db.add_games(key, 2 * len(block), dtb)
        dev_results.append(rb)
    dev_ok, pooled_dev = dev_blocks_pass(dev_results, cfg["dev_promote"], cfg["dev_promote_t"])
    block_summary = [round(x["mean_margin_per_game"], 1) for x in dev_results]
    db.update(key, dev_margin=pooled_dev["mean_margin_per_game"], dev_t=pooled_dev["t"],
              dev_wins=pooled_dev["wins"], dev_losses=pooled_dev["losses"],
              dev_blocks=json.dumps(block_summary))
    log(f"    DEV REPLICATION blocks={block_summary} pooled {pooled_dev['mean_margin_per_game']:+,.0f} "
        f"(t={pooled_dev['t']:.1f}) -> {'PASS' if dev_ok else 'FAIL'}")
    if not dev_ok:
        return "alive"

    # ---- stage 3: held-out
    r, dt = _eval(cand_path, frontier, HELD_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(HELD_SEEDS), dt)
    rc, dtc = eval_panel(cand_path, clone, HELD_SEEDS, engine, jobs)
    db.add_games(key, 2 * len(HELD_SEEDS) * len(panel_list(clone)), dtc)
    fp_held = cfg.get("frontier_panel_held")
    fo_held = cfg.get("frontier_panel_own_held")
    panel_delta_held = rc["mean_margin_per_game"] - fp_held if fp_held is not None else None
    own_delta_held = rc["own_money_per_game"] - fo_held if fo_held is not None else None
    kind_held = classify_gain(panel_delta_held, own_delta_held)
    # Promotion is two-dimensional (Sep 11): (1) beats the frontier head-to-head (t>=2); (2) does not lose ground on
    # the tape panel's paired MARGIN (Sep 9: O-vs-O gains such as melon late-fert were null on the tapes); (3) does
    # not lower our OWN money on the panel (Sep 11: the capital checkpoint's +margin was an input-price attack with
    # own money -$1k -- an exploit, never core architecture). A candidate that fails only (3) is recorded as an exploit.
    passed = (not cfg.get("panel_baseline_error")
              and r["mean_margin_per_game"] > 0 and r["t"] >= 2.0
              and (panel_delta_held is None or panel_delta_held >= cfg.get("panel_floor", 0.0))
              and (own_delta_held is None or own_delta_held >= cfg.get("own_floor", 0.0)))
    population = cfg.get("population_panel")
    population_delta = population_own_delta = None
    population_per_opp = None
    if passed and population and cfg.get("population_baseline_error"):
        passed = False
        population_per_opp = {"error": cfg["population_baseline_error"]}
    elif passed and population:
        rp, dtp = eval_panel(cand_path, population, cfg.get("population_seeds", POPULATION_SEEDS), engine, jobs)
        db.add_games(key, 2 * len(cfg.get("population_seeds", POPULATION_SEEDS)) * len(panel_list(population)), dtp)
        population_delta = rp["mean_margin_per_game"] - cfg["frontier_population_margin"]
        population_own_delta = rp["own_money_per_game"] - cfg["frontier_population_own"]
        population_per_opp = rp["per_opp"]
        passed = (population_delta >= cfg.get("population_floor", 0.0)
                  and population_own_delta >= cfg.get("population_own_floor", 0.0))
    status = "held_pass" if passed else ("held_exploit" if kind_held == "exploit" and r["t"] >= 2.0 else "held_fail")
    db.update(key, stage=3, status=status,
              held_margin=r["mean_margin_per_game"], held_t=r["t"], held_wins=r["wins"], held_losses=r["losses"],
              held_clone_margin=rc["mean_margin_per_game"], population_margin=population_delta,
              population_own=population_own_delta, ladder_status="pending_external_validation" if passed else None,
              note=f"panel_held={rc['per_opp']} panel_delta_held={panel_delta_held} own_held={rc['per_opp_own']} own_delta_held={own_delta_held} kind_held={kind_held} population={population_per_opp} population_delta={population_delta} population_own_delta={population_own_delta}")
    log(f"    HELD-OUT {r['mean_margin_per_game']:+,.0f} (t={r['t']:.1f}, {r['wins']}-{r['losses']})  "
        f"panel {rc['mean_margin_per_game']:+,.0f}" + (f" (delta vs frontier {panel_delta_held:+,.0f}, own {own_delta_held:+,.0f}, {kind_held})" if panel_delta_held is not None and own_delta_held is not None else "")
        + (f" population delta {population_delta:+,.0f}, own {population_own_delta:+,.0f}" if population_delta is not None else "")
        + f"  -> {status.upper()}")
    return "held_pass" if passed else "held_fail"
