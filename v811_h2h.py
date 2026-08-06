#!/usr/bin/env python3
"""Both-seats seeded h2h for a v8.11 variant vs main_v8.3.py, PLUS FERTTRACE
mechanism capture (fertilizer_applied/sold, target_harvest_units,
target_tile_days, fert_worker_actions) pulled from env.logs for the
variant's seat in each orientation. Combines seeded_h2h.py's --both-seats
protocol (the project's required seat-bias control) with fert_diag.py's
log-reading technique.
"""
import argparse
import importlib.util
import re
import sys

from kaggle_environments import make

STANDARD_SEEDS = [1, 7, 42, 99, 123, 202, 303, 555, 2024, 8080, 17, 2025, 3001, 3002, 3003]

FERT_RE = re.compile(
    r"FERTTRACE fertilizer_applied=(\d+) fertilizer_sold=(\d+) "
    r"fert_worker_actions=(\d+) target_harvest_units=(\d+) target_tile_days=(\d+)"
)


def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def _last_ferttrace(env, seat_idx):
    """Last FERTTRACE line (fully-accumulated counters) for seat_idx, or None."""
    last = None
    for step_logs in env.logs:
        if seat_idx >= len(step_logs):
            continue
        log = step_logs[seat_idx]
        if not isinstance(log, dict):
            continue
        for stream in ("stdout", "stderr"):
            text = log.get(stream, "") or ""
            if "FERTTRACE" in text:
                for line in text.splitlines():
                    m = FERT_RE.search(line)
                    if m:
                        last = m
    return last


def run_one(variant_path, base_path, seed, turns, swap):
    """swap=False: variant in seat0(A), base in seat1(B).
    swap=True: base in seat0, variant in seat1.
    Returns (r_variant, r_base, s_variant, s_base, fert_match_or_None)."""
    v = load_agent(variant_path)
    b = load_agent(base_path)
    env = make("kaggriculture", configuration={"episodeSteps": turns}, debug=False)
    env.info = {"seed": seed}
    players = [b, v] if swap else [v, b]
    env.run(players)
    final = env.steps[-1]
    variant_seat = 1 if swap else 0
    base_seat = 0 if swap else 1
    r_variant, s_variant = final[variant_seat].reward, final[variant_seat].status
    r_base, s_base = final[base_seat].reward, final[base_seat].status
    fert = _last_ferttrace(env, variant_seat)
    return r_variant, r_base, s_variant, s_base, fert


def main():
    p = argparse.ArgumentParser()
    p.add_argument("variant")
    p.add_argument("--base", default="main_v8.3.py")
    p.add_argument("--seeds", type=int, nargs="+", default=STANDARD_SEEDS)
    p.add_argument("--turns", type=int, default=720)
    args = p.parse_args()

    wins_v = wins_b = ties = 0
    margins = []
    crashes = []
    agg = {"fertilizer_applied": 0, "fertilizer_sold": 0, "fert_worker_actions": 0,
           "target_harvest_units": 0, "target_tile_days": 0}
    n_fert_matches = 0

    print(f"{'seed':>6} {'V_norm':>10} {'B_norm':>10} {'V_swap':>10} {'B_swap':>10} "
          f"{'V_total':>10} {'B_total':>10} {'margin':>10} {'win':>4}")
    for seed in args.seeds:
        rv1, rb1, sv1, sb1, f1 = run_one(args.variant, args.base, seed, args.turns, swap=False)
        rv2, rb2, sv2, sb2, f2 = run_one(args.variant, args.base, seed, args.turns, swap=True)
        if "DONE" not in (sv1,) or sv1 != "DONE" or sb1 != "DONE" or sv2 != "DONE" or sb2 != "DONE":
            crashes.append((seed, sv1, sb1, sv2, sb2))
        tv, tb = rv1 + rv2, rb1 + rb2
        margin = tv - tb
        if tv > tb:
            wins_v += 1; win = "V"
        elif tb > tv:
            wins_b += 1; win = "B"
        else:
            ties += 1; win = "TIE"
        margins.append(margin)
        for f in (f1, f2):
            if f:
                n_fert_matches += 1
                agg["fertilizer_applied"] += int(f.group(1))
                agg["fertilizer_sold"] += int(f.group(2))
                agg["fert_worker_actions"] += int(f.group(3))
                agg["target_harvest_units"] += int(f.group(4))
                agg["target_tile_days"] += int(f.group(5))
        print(f"{seed:>6} {rv1:>10.0f} {rb1:>10.0f} {rv2:>10.0f} {rb2:>10.0f} "
              f"{tv:>10.0f} {tb:>10.0f} {margin:>+10.0f} {win:>4}")

    n = len(args.seeds)
    mean = sum(margins) / len(margins)
    print(f"\n{args.variant} wins: {wins_v}/{n}   {args.base} wins: {wins_b}/{n}   ties: {ties}")
    print(f"paired margin (V-B, seat-controlled): mean {mean:+.0f}   "
          f"min {min(margins):+.0f}   max {max(margins):+.0f}")
    if len(margins) > 1:
        var = sum((m - mean) ** 2 for m in margins) / (len(margins) - 1)
        sd = var ** 0.5
        se = sd / (len(margins) ** 0.5)
        print(f"stdev {sd:,.0f}   stderr {se:,.0f}   t {(mean / se) if se else 0:+.2f}")
    if crashes:
        print(f"\nCRASHES on seeds: {crashes}")

    print(f"\n--- fertilize mechanism (summed over {n_fert_matches}/{2*n} variant-seat games; "
          f"per-game average in parens) ---")
    for k, v in agg.items():
        avg = v / n_fert_matches if n_fert_matches else 0.0
        print(f"  {k}: {v}  (avg/game {avg:.1f})")


if __name__ == "__main__":
    main()
