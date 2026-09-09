#!/usr/bin/env python3
"""
instrument_v4_cropmix.py — crop-selection (R4) diagnosis for
candidates/P8v2_reactive_allocation.py vs candidates/P6_baseline.py.

WHY: DIAGNOSIS_V3.md found P8v2 sells 5-7x more WHEAT and ~1/4-2/5 the
STRAWBERRY/MILK volume of P6/C1, at REALIZED PRICES that are equal-to-better
than P6/C1's -- i.e. R5 sell-timing was ruled out; the volume gap is
upstream, in R4's greedy crop-selection/planting choice. This script traces
R4's own decision inputs (per-crop `room_units`/`val`/`price` the greedy loop
computes) day by day, for both P8v2's formula and P6's formula, against the
SAME real obs (same seeds, same opponent), to determine whether P8v2 is
ACTIVELY CHOOSING WHEAT over STRAWBERRY (a ranking-logic difference) or
STRUCTURALLY UNABLE to plant STRAWBERRY (space/labor/siting gate closes
before STRAWBERRY's turn) so it defaults to WHEAT.

METHOD: reuses mini_engine.py's own game loop (load_engine/load_agent
pattern, `mod._commit_unit` sales logging) -- no new engine-calling code --
but replaces mini_engine.load_agent with a local variant that, after loading
each candidate module, wraps its top-level `economy(obs, v)` function with a
logging shim. The shim calls the REAL, unmodified economy() to get the real
orders (nothing about policy behavior is changed), and ADDITIONALLY
recomputes -- purely for logging, using each policy's own imported
CROP_SPECS/I0/DEMAND_SHARE constants and (for P6) its own `_daily_demand`
helper -- the `room_units`/`val`/`eligible` score the real greedy loop would
have assigned to WHEAT/STRAWBERRY/MELON that call, reproducing each policy's
own formula (P8v2's simpler `pool = DEMAND_SHARE * max(0, I0-inv)` vs P6's
`pool = DEMAND_SHARE * (max(0, I0-inv) + cushion_left + daily_demand*(29-day))`)
verbatim from the source read in this session. This is read-only
introspection: candidates/P8v2_reactive_allocation.py and
candidates/P6_baseline.py are loaded and run completely unmodified on disk;
only the freshly-imported IN-MEMORY module object's `economy` attribute is
reassigned to a wrapper, exactly the same monkeypatch pattern
eval_protocol.py already uses on `mod._commit_unit`.

OUTPUT: experiments/P8_DIAGNOSIS/raw_v4/*.json (per policy/seed/seat full
day-by-day crop-score + BUY_SEED order log) and
experiments/P8_DIAGNOSIS/summary_v4.json (cross-seed aggregate: how often
each policy's own room_units/eligible gate blocks STRAWBERRY vs WHEAT, and
how often each crop wins the greedy pick).
"""
from __future__ import annotations

import importlib.util
import json
import statistics
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "experiments" / "RNG_PATH_DEPENDENCE_AUDIT"))

import mini_engine as me  # noqa: E402

CANDS = ROOT / "candidates"
OPP = ROOT / "Opponents" / "opp_scenario_v14.py"
OUT_DIR = Path(__file__).resolve().parent
RAW_DIR = OUT_DIR / "raw_v4"
RAW_DIR.mkdir(exist_ok=True)

POLICIES = {
    "P8v2": CANDS / "P8v2_reactive_allocation.py",
    "P6": CANDS / "P6_baseline.py",
}

WATCH_CROPS = ("WHEAT", "STRAWBERRY", "MELON")

_AGENT_N = 0


def _score_p8v2_style(mod, obs, v, seeds):
    """Reproduce P8v2 economy()'s R4 pool/val formula verbatim (read-only,
    for logging only -- does not affect the real orders)."""
    CROP_SPECS, I0, DEMAND_SHARE = mod.CROP_SPECS, mod.I0, mod.DEMAND_SHARE
    prices = obs["market"]["prices"]
    inventory = obs["market"]["inventory"]
    committed = {c: 0.0 for c in CROP_SPECS}
    for _pos, t in v["crops"]:
        c = t.get("crop")
        if c in committed:
            committed[c] += CROP_SPECS[c]["units"]
    for c in committed:
        committed[c] += seeds.get(c, 0) * CROP_SPECS[c]["units"]
    out = {}
    for c in WATCH_CROPS:
        sp = CROP_SPECS[c]
        inv_c = inventory.get(c, I0)
        pool = DEMAND_SHARE * max(0.0, I0 - inv_c)
        room_units = pool - committed[c]
        price = min(prices.get(c, sp["base"]), sp["base"] * 2.0)
        val = min(sp["units"], room_units) * price / sp["cycle"] if room_units > 0 else 0.0
        out[c] = {
            "room_units": round(room_units, 1), "val": round(val, 2), "price": round(price, 2),
            "committed": round(committed[c], 1),
            "eligible": bool(room_units >= sp["units"] * 0.5 and val >= sp["min_val"]),
        }
    return out


def _score_p6_style(mod, obs, v, seeds):
    """Reproduce P6_baseline.py economy()'s R4 pool/val formula verbatim
    (read-only, for logging only)."""
    CROP_SPECS, I0, DEMAND_SHARE = mod.CROP_SPECS, mod.I0, mod.DEMAND_SHARE
    prices = obs["market"]["prices"]
    inventory = obs["market"]["inventory"]
    day = obs["day"]
    committed = {c: 0.0 for c in CROP_SPECS}
    for _pos, t in v["crops"]:
        c = t.get("crop")
        if c in committed:
            committed[c] += CROP_SPECS[c]["units"]
    for c in committed:
        committed[c] += seeds.get(c, 0) * CROP_SPECS[c]["units"]
    out = {}
    for c in WATCH_CROPS:
        sp = CROP_SPECS[c]
        inv_c = inventory.get(c, I0)
        cushion_left = max(0.0, sp.get("cushion", 0) - max(0.0, inv_c - I0))
        dd = mod._daily_demand(obs, c, day, day + sp["first"])
        pool = DEMAND_SHARE * (max(0.0, I0 - inv_c) + cushion_left + dd * (29 - day))
        room_units = pool - committed[c]
        price = min(prices.get(c, sp["base"]), sp["base"] * 2.0)
        val = min(sp["units"], room_units) * price / sp["cycle"] if room_units > 0 else 0.0
        out[c] = {
            "room_units": round(room_units, 1), "val": round(val, 2), "price": round(price, 2),
            "committed": round(committed[c], 1),
            "eligible": bool(room_units >= sp["units"] * 0.5 and val >= sp["min_val"]),
        }
    return out


SCORERS = {"P8v2": _score_p8v2_style, "P6": _score_p6_style}


def load_agent_traced(path, policy_name, log):
    """Same as mini_engine.load_agent, but wraps the module's top-level
    economy(obs, v) with a read-only logging shim. Real orders returned by
    the real, unmodified economy() are passed through untouched."""
    global _AGENT_N
    _AGENT_N += 1
    path = Path(path)
    name = f"agent_{path.stem}_{_AGENT_N}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)

    if hasattr(mod, "economy"):
        orig_economy = mod.economy
        scorer = SCORERS[policy_name]

        def traced_economy(obs, v):
            orders = orig_economy(obs, v)  # REAL, unmodified decision -- shim does not alter it
            day, hour = obs["day"], obs["hour"]
            buys = [(o[1], int(o[2])) for o in orders if o[0] == "BUY_SEED"]
            # R4 (both policies) has no hour==0 gate -- economy() can plant on any hour
            # of the day, so log EVERY call that actually places a BUY_SEED order, plus
            # one hour==0 call per day for the score-eligibility snapshot (informational).
            if (hour == 0 and day >= 1) or buys:
                seeds = obs["private"]["seeds"]
                try:
                    scores = scorer(mod, obs, v, seeds)
                except Exception as exc:  # diagnostic path only; never let this break the real game
                    scores = {"error": repr(exc)}
                empty_count = len(v["empty"]) + len(v["empty_pastures"])
                tile_counts = {}
                for _pos, t in v["crops"]:
                    c = t.get("crop")
                    tile_counts[c] = tile_counts.get(c, 0) + 1
                log.append({
                    "day": day, "hour": hour, "scores": scores, "buy_seed_orders": buys,
                    "space_proxy_empty_tiles": empty_count, "tile_counts": tile_counts,
                })
            return orders

        mod.economy = traced_economy
    return mod.agent


def run_one(policy_name, path, opp_path, seed, seat_swapped):
    log = []
    orig_load_agent = me.load_agent

    def patched(p):
        p = Path(p)
        if p == path:
            return load_agent_traced(p, policy_name, log)
        return orig_load_agent(p)

    me.load_agent = patched
    try:
        if not seat_swapped:
            r = me.run_game(str(path), str(opp_path), seed, engine="master", trace=True)
            own_idx = 0
        else:
            r = me.run_game(str(opp_path), str(path), seed, engine="master", trace=True)
            own_idx = 1
    finally:
        me.load_agent = orig_load_agent
    opp_idx = 1 - own_idx
    money_delta = r["money"][own_idx] - r["money"][opp_idx]
    return log, money_delta, r["errors"][own_idx]


def main(seeds):
    all_records = {name: [] for name in POLICIES}
    for seed in seeds:
        for swapped in (False, True):
            for name, path in POLICIES.items():
                log, delta, errors = run_one(name, path, OPP, seed, swapped)
                rec = {"policy": name, "seed": seed, "seat_swapped": swapped, "errors": errors,
                       "final_money_delta": delta, "day_log": log}
                all_records[name].append(rec)
                json.dump(rec, open(RAW_DIR / f"{name}_seed{seed}_swap{int(swapped)}.json", "w"),
                          indent=2, default=str)
                wheat_buys = sum(q for d in log for it, q in d["buy_seed_orders"] if it == "WHEAT")
                straw_buys = sum(q for d in log for it, q in d["buy_seed_orders"] if it == "STRAWBERRY")
                print(f"{name} seed={seed} swap={swapped}: errors={errors} delta=${delta:+,.0f} "
                      f"wheat_seed_bought={wheat_buys} straw_seed_bought={straw_buys}")

    summary = {}
    for name, recs in all_records.items():
        n_days_wheat_wins = 0
        n_days_straw_wins = 0
        n_days_straw_ineligible = 0
        n_days_wheat_eligible = 0
        n_days_straw_eligible = 0
        wheat_val_when_straw_eligible = []
        straw_val_when_eligible = []
        total_wheat_seed = 0
        total_straw_seed = 0
        for r in recs:
            for d in r["day_log"]:
                s = d["scores"]
                if "error" in s:
                    continue
                buys = {it: q for it, q in d["buy_seed_orders"]}
                if buys.get("WHEAT", 0) > 0:
                    n_days_wheat_wins += 1
                if buys.get("STRAWBERRY", 0) > 0:
                    n_days_straw_wins += 1
                if not s["STRAWBERRY"]["eligible"]:
                    n_days_straw_ineligible += 1
                else:
                    n_days_straw_eligible += 1
                    straw_val_when_eligible.append(s["STRAWBERRY"]["val"])
                    if s["WHEAT"]["eligible"]:
                        wheat_val_when_straw_eligible.append(s["WHEAT"]["val"])
                if s["WHEAT"]["eligible"]:
                    n_days_wheat_eligible += 1
                total_wheat_seed += buys.get("WHEAT", 0)
                total_straw_seed += buys.get("STRAWBERRY", 0)
        n_days = sum(len(r["day_log"]) for r in recs)
        # mean live tile count by crop, sampled at each hour==0 snapshot (not rebuy-frequency-biased)
        wheat_tiles_samples, straw_tiles_samples = [], []
        for r in recs:
            for d in r["day_log"]:
                if d["hour"] == 0:
                    wheat_tiles_samples.append(d["tile_counts"].get("WHEAT", 0))
                    straw_tiles_samples.append(d["tile_counts"].get("STRAWBERRY", 0))
        summary[name] = {
            "n_games": len(recs), "n_days_logged": n_days,
            "n_days_wheat_bought": n_days_wheat_wins,
            "n_days_straw_bought": n_days_straw_wins,
            "n_days_wheat_eligible": n_days_wheat_eligible,
            "n_days_straw_eligible": n_days_straw_eligible,
            "n_days_straw_ineligible": n_days_straw_ineligible,
            "pct_days_straw_ineligible": round(100 * n_days_straw_ineligible / max(1, n_days), 1),
            "mean_wheat_val_when_straw_also_eligible": round(statistics.mean(wheat_val_when_straw_eligible), 2) if wheat_val_when_straw_eligible else None,
            "mean_straw_val_when_eligible": round(statistics.mean(straw_val_when_eligible), 2) if straw_val_when_eligible else None,
            "total_wheat_seed_bought": total_wheat_seed,
            "total_straw_seed_bought": total_straw_seed,
            "mean_live_wheat_tiles": round(statistics.mean(wheat_tiles_samples), 2) if wheat_tiles_samples else None,
            "mean_live_straw_tiles": round(statistics.mean(straw_tiles_samples), 2) if straw_tiles_samples else None,
            "max_live_wheat_tiles": max(wheat_tiles_samples) if wheat_tiles_samples else None,
            "max_live_straw_tiles": max(straw_tiles_samples) if straw_tiles_samples else None,
            "mean_final_delta": round(statistics.mean(r["final_money_delta"] for r in recs), 1),
        }
    json.dump(summary, open(OUT_DIR / "summary_v4.json", "w"), indent=2, default=str)
    print("\n=== SUMMARY ===")
    print(json.dumps(summary, indent=2, default=str))
    return summary


if __name__ == "__main__":
    seeds = list(range(1, 11))
    if len(sys.argv) > 1:
        seeds = [int(x) for x in sys.argv[1:]]
    main(seeds)
