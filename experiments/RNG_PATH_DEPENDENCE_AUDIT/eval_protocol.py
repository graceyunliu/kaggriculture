#!/usr/bin/env python3
"""
eval_protocol.py — RNG-controlled evaluation protocol for Kaggriculture policy comparisons.

WHY THIS EXISTS
----------------
artifacts/rng_path_dependence_audit/REPORT.md found that the production engine
(vendor/kaggle_environments_engine_master/kaggriculture.py::_end_of_day()) shares
ONE random.Random object, within a day, between:
  1. weed-spawning (one rng.random() draw per empty board tile, per player), and
  2. the periodic town-shop-unlock draw (rng.choice(sorted(SHOPS))), drawn from
     the SAME rng object immediately after the weed loop.
Weed-spawn draw COUNT depends on how many tiles are empty at end-of-day, which is
policy-dependent (a policy that plants/builds more leaves fewer empty tiles). So
two policies given the identical seed can still receive a DIFFERENT shop-unlock
outcome, purely because they occupied a different number of board tiles that day
-- not because of any real skill difference. Because `town["unlocked_shops"]` is
permanent state, one diverged draw can alter the game's shop economy for every
remaining day.

This module turns the report's Phase 4 "minimal protocol" recommendation into
actual, runnable tooling:
  - paired/common-seed comparison (same seed used for both arms of a comparison)
  - per-day RNG draw-count instrumentation (weed draws per farm, shop-unlock
    picks) logged directly off the REAL engine via a read-only monkeypatch,
    not a synthetic analogue
  - a report structure that separates ACTION DIFFERENCE / TRAJECTORY DIFFERENCE
    / OUTCOME DIFFERENCE (report's Phase 4 vocabulary), so a $ delta can be
    checked for RNG-path confounding before being treated as a real effect
  - paired-seed distribution reporting (mean, sample stdev, t-stat, win/loss/tie)
    instead of a single trajectory

WHAT IS REAL VS. SIMPLIFIED
----------------------------
REAL: this module runs the actual production engine
(vendor/kaggle_environments_engine_master/kaggriculture.py, or the "1.32" vendor
copy) via mini_engine.py's existing shim (no kaggle_environments pip install
needed, no synthetic reimplementation of game rules). The RNG instrumentation
patches module-level function references (`_end_of_day`, `_spawn_weeds`) using
the exact same monkeypatch pattern mini_engine.py already uses for
`_commit_unit` -- i.e. this is not a new/riskier technique, it's the same one
already in use elsewhere in this repo, applied read-only (nothing is written
back to the engine file or any champion/candidate policy file).

SIMPLIFICATION: draw counts are recovered by counting empty tiles immediately
before `_spawn_weeds` runs (which is exactly the draw count `_spawn_weeds` will
consume, since the short-circuit is `if tile is None: draw = rng.random()`) --
this avoids subclassing/wrapping the actual `random.Random` instance (which
would require patching the global `random.Random` class for the duration of
the game, a larger blast radius). The two approaches are mathematically
equivalent for draw COUNTING (not for the drawn values themselves, which are
not needed here) -- documented so the choice is visible, not hidden.

READ-ONLY GUARANTEE
--------------------
This module does not modify, import-and-mutate, or write to any file under
submissions/, evolve/, or any champion strategy file. It only *reads* whatever
candidate/opponent .py files are passed to it on the command line (or as
paths to the compare_paired() function), exactly the way mini_engine.py's
own `--engine` CLI already does. Engine monkeypatches are installed on the
in-memory module object returned by mini_engine.load_engine() and are restored
before the function returns.

CLI
---
    python3 eval_protocol.py CANDIDATE_A.py CANDIDATE_B.py OPPONENT.py \
        --seeds 1 2 3 4 5 --engine master --both-seats --out results.json

Programmatic:
    from eval_protocol import compare_paired
    report = compare_paired("A.py", "B.py", "OPPONENT.py", seeds=range(1, 11))
    report["mean_delta"], report["t"], report["seeds_trajectory_diverged"]

See README.md in this directory for how to interpret output.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import mini_engine as me  # noqa: E402  (read-only import of existing repo-root harness)


# --------------------------------------------------------------------------- instrumentation
def run_game_instrumented(agent_a, agent_b, seed, engine="master", config=None, turns=None):
    """Same as mini_engine.run_game(), but additionally returns 'rng_log': a
    per-day record of (a) how many weed-spawn draws each farm consumed before
    that day's shop-unlock check, and (b) whether/what shop unlocked that day.

    Implementation: monkeypatches the loaded engine module's `_end_of_day` and
    `_spawn_weeds` names (module-global function lookup, same pattern
    mini_engine.py already uses for `_commit_unit`), restores them before
    returning. Does not touch any file on disk.
    """
    mod, defaults = me.load_engine(engine)
    orig_end_of_day = mod._end_of_day
    orig_spawn_weeds = mod._spawn_weeds

    rng_log = []
    _day_draws = []  # reset each day, appended to by wrapped _spawn_weeds, in farm-enumeration order

    def wrapped_spawn_weeds(farm, board_size, weed_chance, rng):
        empty = sum(1 for row in farm["tiles"] for t in row if t is None)
        _day_draws.append(empty)
        return orig_spawn_weeds(farm, board_size, weed_chance, rng)

    def wrapped_end_of_day(state, env, day):
        _day_draws.clear()
        obs0 = state[0].observation
        town = obs0.town
        before = list(town.get("unlocked_shops", []))
        orig_end_of_day(state, env, day)
        after = list(town.get("unlocked_shops", []))
        newly_unlocked = after[len(before):] or None
        rng_log.append({
            "day": day,
            "weed_draws_per_farm": list(_day_draws),  # index i == farm i's draw count that day
            "shop_unlocked_this_day": (newly_unlocked[0] if newly_unlocked else None),
            "unlocked_shops_after": after,
        })

    mod._spawn_weeds = wrapped_spawn_weeds
    mod._end_of_day = wrapped_end_of_day
    try:
        result = me.run_game(agent_a, agent_b, seed, engine, config, trace=True, turns=turns)
    finally:
        mod._spawn_weeds = orig_spawn_weeds
        mod._end_of_day = orig_end_of_day

    result["rng_log"] = rng_log
    return result


# --------------------------------------------------------------------------- divergence check
def _first_shop_divergence_day(rng_log_a, rng_log_b):
    """Return the first day index where the two runs' `unlocked_shops_after`
    sequences differ (i.e. the trajectory-divergence checkpoint), or None if
    they never differ across the whole game. Compares the two runs' *own*
    town state (each run has its own independent town / farms), so this
    answers: 'did these two arms' town-shop trajectories diverge from each
    other', not 'did each diverge from some third baseline'."""
    for da, db in zip(rng_log_a, rng_log_b):
        if da["unlocked_shops_after"] != db["unlocked_shops_after"]:
            return da["day"]
    if len(rng_log_a) != len(rng_log_b):
        return min(len(rng_log_a), len(rng_log_b))
    return None


def _draw_count_divergence_days(rng_log_a, rng_log_b):
    """Days where farm-0's weed-draw count differed between the two runs --
    i.e. the candidate under test (assumed seat 0) actually occupied a
    different number of tiles that day. This is the ACTION DIFFERENCE
    evidence (Phase 4 vocabulary): confirms the intervention changed
    behavior, before asking whether that behavior change touched the
    RNG-coupled mechanic."""
    days = []
    for da, db in zip(rng_log_a, rng_log_b):
        wa = da["weed_draws_per_farm"]
        wb = db["weed_draws_per_farm"]
        if wa and wb and wa[0] != wb[0]:
            days.append(da["day"])
    return days


# --------------------------------------------------------------------------- paired comparison
def compare_paired(candidate_a, candidate_b, opponent, seeds, engine="master", config=None,
                    both_seats=True, turns=None):
    """Paired/common-random-numbers comparison of two CANDIDATE policies,
    each played against the SAME fixed opponent, on the SAME seed, so any
    seed-driven variance is controlled for (common random numbers design).

    For each seed s (and, if both_seats, again with candidate/opponent seats
    swapped):
        game_a = run_game_instrumented(candidate_a, opponent, seed=s, ...)
        game_b = run_game_instrumented(candidate_b, opponent, seed=s, ...)
    Both games share (seed, opponent, engine, config) -- the ONLY thing that
    differs is which candidate is in the candidate seat. Because
    `_end_of_day`'s rng object is freshly constructed from (seed, day) at the
    start of each day in EACH game independently, and because the opponent's
    actions are the same function run against materially the same game state
    up to first divergence, any difference in that day's weed-draw count (and
    therefore shop-unlock outcome) traces back to the candidate's own board
    occupancy -- exactly the mechanism the audit report identified.

    Returns a report dict with:
      - per_seed: list of per-seed records (money delta, first divergence day,
        action-divergence days, whether shop-unlock outcome ever differed)
      - mean_delta, stdev, t (paired t-statistic vs. 0), wins/losses/ties
      - seeds_trajectory_diverged: seeds where the two arms' town-shop state
        ever differed -- a $ delta on one of these seeds is NOT yet a "robust
        causal mechanism" per the report's Phase 4 bar; it needs the larger
        fresh-seed check in that same section before being trusted.
    """
    per_seed = []
    seat_variants = [False] + ([True] if both_seats else [])
    for seed in seeds:
        for swapped in seat_variants:
            if not swapped:
                ga = run_game_instrumented(candidate_a, opponent, seed, engine, config, turns)
                gb = run_game_instrumented(candidate_b, opponent, seed, engine, config, turns)
                money_a, money_b = ga["money"][0], gb["money"][0]
            else:
                ga = run_game_instrumented(opponent, candidate_a, seed, engine, config, turns)
                gb = run_game_instrumented(opponent, candidate_b, seed, engine, config, turns)
                money_a, money_b = ga["money"][1], gb["money"][1]

            div_day = _first_shop_divergence_day(ga["rng_log"], gb["rng_log"])
            action_div_days = _draw_count_divergence_days(ga["rng_log"], gb["rng_log"])
            per_seed.append({
                "seed": seed,
                "seat_swapped": swapped,
                "money_a": money_a,
                "money_b": money_b,
                "delta": money_a - money_b,
                "action_diverged": bool(action_div_days),
                "action_divergence_first_day": (action_div_days[0] if action_div_days else None),
                "action_divergence_days": action_div_days,
                "trajectory_diverged": div_day is not None,
                "trajectory_divergence_first_day": div_day,
                "errors_a": ga["errors"][0] if not swapped else ga["errors"][1],
                "errors_b": gb["errors"][0] if not swapped else gb["errors"][1],
            })

    deltas = [r["delta"] for r in per_seed]
    n = len(deltas)
    mean = sum(deltas) / n if n else 0.0
    sd = (sum((d - mean) ** 2 for d in deltas) / (n - 1)) ** 0.5 if n > 1 else 0.0
    t = (mean / (sd / n ** 0.5)) if sd > 0 else (float("inf") if mean != 0 else 0.0)

    return {
        "candidate_a": str(candidate_a),
        "candidate_b": str(candidate_b),
        "opponent": str(opponent),
        "engine": engine,
        "config": config or {},
        "n_games_per_arm": n,
        "mean_delta": mean,
        "stdev_delta": sd,
        "t": t,
        "wins": sum(d > 0 for d in deltas),
        "losses": sum(d < 0 for d in deltas),
        "ties": sum(d == 0 for d in deltas),
        "n_action_diverged": sum(r["action_diverged"] for r in per_seed),
        "n_trajectory_diverged": sum(r["trajectory_diverged"] for r in per_seed),
        "seeds_trajectory_diverged": [r["seed"] for r in per_seed if r["trajectory_diverged"]],
        "per_seed": per_seed,
    }


def print_report(report):
    print(f"{Path(report['candidate_a']).name} vs {Path(report['candidate_b']).name}  "
          f"(common opponent: {Path(report['opponent']).name}, engine={report['engine']})")
    print(f"n={report['n_games_per_arm']} paired games   "
          f"mean delta ${report['mean_delta']:+,.0f}   stdev ${report['stdev_delta']:,.0f}   t={report['t']:.2f}")
    print(f"wins {report['wins']}  losses {report['losses']}  ties {report['ties']}")
    print(f"action-diverged (candidate's own board occupancy differed that day): "
          f"{report['n_action_diverged']}/{report['n_games_per_arm']} games")
    print(f"trajectory-diverged (shop-unlock state ever differed between arms): "
          f"{report['n_trajectory_diverged']}/{report['n_games_per_arm']} games"
          f"  seeds: {report['seeds_trajectory_diverged']}")
    print()
    for r in report["per_seed"]:
        flag = ""
        if r["trajectory_diverged"]:
            flag = f"  ** TRAJECTORY DIVERGED at day {r['trajectory_divergence_first_day']} -- $ delta may be RNG-path-confounded, not a policy effect **"
        print(f"  seed {r['seed']:>5} seat_swapped={r['seat_swapped']!s:5}  "
              f"delta=${r['delta']:+,.0f}  action_diverged={r['action_diverged']}{flag}")


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("candidate_a")
    p.add_argument("candidate_b")
    p.add_argument("opponent")
    p.add_argument("--seeds", type=int, nargs="+", default=list(range(1, 11)))
    p.add_argument("--engine", default="master", choices=list(me.ENGINES))
    p.add_argument("--config", default=None, help='JSON overrides, e.g. \'{"townShopUnlockInterval": 3}\'')
    p.add_argument("--both-seats", action="store_true")
    p.add_argument("--turns", type=int, default=None)
    p.add_argument("--out", default=None, help="write full JSON report here")
    args = p.parse_args()
    config = json.loads(args.config) if args.config else None

    t0 = time.time()
    report = compare_paired(args.candidate_a, args.candidate_b, args.opponent, args.seeds,
                             engine=args.engine, config=config, both_seats=args.both_seats,
                             turns=args.turns)
    print_report(report)
    print(f"\n({time.time() - t0:.1f}s)")
    if args.out:
        json.dump(report, open(args.out, "w"), indent=2, default=str)
        print(f"full report written to {args.out}")


if __name__ == "__main__":
    main()
