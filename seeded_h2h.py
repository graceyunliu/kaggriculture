#!/usr/bin/env python3
"""Seeded head-to-head: agent_a vs agent_b, N seeds, aggregate win/money.

Per project convention: configuration={"seed": N} does NOT propagate to the
engine's weed-spawn RNG. Must set env.info["seed"] = N directly after make().

=== READ THIS BEFORE TRUSTING A RESULT: --swap-half IS NOT A CONTROL ===

Running an agent against ITSELF under `--swap-half` over the standard
11-seed set does not come out even. It comes out 2/11, mean -$2,772,
min -$6,544, max +$5,407 -- a large, reproducible bias against seat A,
produced entirely by the engine, not by either agent.

Cause: `_end_of_day` builds one RNG per day and calls `_spawn_weeds` for
each player sequentially from the same stream, so seat 0 and seat 1 get
different weed layouts even under identical code. `--swap-half`
alternates which seed lands in which seat, but each seed is still played
in only ONE seat, so the seat effect is not cancelled -- it is merely
shuffled, and it does not average out at n=11.

Consequence: any margin measured with `--swap-half` carries roughly a
-$2,772 offset against agent A on this seed set, and per-seed margins are
dominated by a seat x seed interaction rather than by agent skill. A
challenger that appears to lose by a few thousand dollars may in fact be
behaviorally identical to the champion. This is not hypothetical: it is
exactly what happened to v7.7, which was rejected on numbers that turned
out to be this mirror-match table to the dollar.

Use `--both-seats` instead. It plays every seed in BOTH seats and
compares summed money, which cancels the seat effect exactly (an agent
against itself scores a clean 0.0 margin). It costs 2x the games. Use it
for any result you intend to act on; `--swap-half` is retained only for
reproducing historical numbers.
"""
import argparse
import importlib.util
import sys

from kaggle_environments import make


def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def run_one(agent_a_path, agent_b_path, seed, turns=720, swap=False):
    a = load_agent(agent_a_path)
    b = load_agent(agent_b_path)
    env = make("kaggriculture", configuration={"episodeSteps": turns}, debug=False)
    env.info = {"seed": seed}
    players = [b, a] if swap else [a, b]
    env.run(players)
    final = env.steps[-1]
    if swap:
        rb, ra = final[0].reward, final[1].reward
        sb, sa = final[0].status, final[1].status
    else:
        ra, rb = final[0].reward, final[1].reward
        sa, sb = final[0].status, final[1].status
    return ra, sa, rb, sb


def main():
    p = argparse.ArgumentParser()
    p.add_argument("agent_a")
    p.add_argument("agent_b")
    p.add_argument("--seeds", type=int, nargs="+", default=list(range(1, 11)))
    p.add_argument("--turns", type=int, default=720)
    p.add_argument("--swap-half", action="store_true",
                   help="alternate seat per seed. NOT a control -- see module docstring. "
                        "Retained only to reproduce historical numbers.")
    p.add_argument("--both-seats", action="store_true",
                   help="play every seed in BOTH seats and compare summed money. "
                        "Cancels the engine's seat bias exactly. 2x games. Use this.")
    args = p.parse_args()

    if args.both_seats:
        return run_both_seats(args)

    wins_a = wins_b = ties = 0
    margins = []
    print(f"{'seed':>6} {'seat':>6} {args.agent_a:>20} {args.agent_b:>20} {'winner':>8}")
    for i, seed in enumerate(args.seeds):
        swap = args.swap_half and (i % 2 == 1)
        ra, sa, rb, sb = run_one(args.agent_a, args.agent_b, seed, args.turns, swap=swap)
        if sa != "DONE" or sb != "DONE":
            winner = f"CRASH(a={sa},b={sb})"
        elif ra > rb:
            wins_a += 1
            winner = "A"
        elif rb > ra:
            wins_b += 1
            winner = "B"
        else:
            ties += 1
            winner = "TIE"
        margins.append(ra - rb)
        seat = "swap" if swap else "norm"
        print(f"{seed:>6} {seat:>6} {ra:>20.0f} {rb:>20.0f} {winner:>8}")

    n = len(args.seeds)
    print(f"\n{args.agent_a} wins: {wins_a}/{n}   {args.agent_b} wins: {wins_b}/{n}   ties: {ties}")
    print(f"mean margin (A-B): {sum(margins)/len(margins):+.0f}   min: {min(margins):+.0f}   max: {max(margins):+.0f}")
    print("\nWARNING: --swap-half does not cancel the engine's seat bias. An agent "
          "against itself scores -$2,772 mean on the standard 11-seed set. "
          "Re-run with --both-seats before acting on this result.")


def run_both_seats(args):
    """Every seed played in both seat assignments; margin is the sum.

    This is the seat-effect control. Because the same seed is played with
    the agents in both orders, the engine's per-seat weed-RNG advantage
    appears once on each side and cancels in the sum. An agent compared
    against itself under this scheme scores exactly 0.0, which is what
    makes a nonzero margin here attributable to the agents.
    """
    wins_a = wins_b = ties = 0
    margins = []
    crashes = []
    print(f"{'seed':>6} {'A_norm':>12} {'B_norm':>12} {'A_swap':>12} {'B_swap':>12} "
          f"{'A_total':>12} {'B_total':>12} {'margin':>11} {'win':>5}")
    for seed in args.seeds:
        ra1, sa1, rb1, sb1 = run_one(args.agent_a, args.agent_b, seed, args.turns, swap=False)
        ra2, sa2, rb2, sb2 = run_one(args.agent_a, args.agent_b, seed, args.turns, swap=True)
        if "DONE" != sa1 or "DONE" != sb1 or "DONE" != sa2 or "DONE" != sb2:
            crashes.append((seed, sa1, sb1, sa2, sb2))
        ta, tb = ra1 + ra2, rb1 + rb2
        margin = ta - tb
        if ta > tb:
            wins_a += 1; win = "A"
        elif tb > ta:
            wins_b += 1; win = "B"
        else:
            ties += 1; win = "TIE"
        margins.append(margin)
        print(f"{seed:>6} {ra1:>12.0f} {rb1:>12.0f} {ra2:>12.0f} {rb2:>12.0f} "
              f"{ta:>12.0f} {tb:>12.0f} {margin:>+11.0f} {win:>5}")

    n = len(args.seeds)
    mean = sum(margins) / len(margins)
    print(f"\n{args.agent_a} wins: {wins_a}/{n}   {args.agent_b} wins: {wins_b}/{n}   ties: {ties}")
    print(f"paired margin (A-B, seat-controlled): mean {mean:+.0f}   "
          f"min {min(margins):+.0f}   max {max(margins):+.0f}")
    if len(margins) > 1:
        var = sum((m - mean) ** 2 for m in margins) / (len(margins) - 1)
        sd = var ** 0.5
        se = sd / (len(margins) ** 0.5)
        print(f"stdev {sd:,.0f}   stderr {se:,.0f}   t {(mean / se) if se else 0:+.2f}")
        print(f"rough 95% CI: [{mean - 1.96 * se:+,.0f}, {mean + 1.96 * se:+,.0f}]")
    if crashes:
        print(f"\nCRASHES on seeds: {crashes}")
    if all(m == 0 for m in margins):
        print("\nAll margins exactly zero -- the two agents are behaviorally identical.")


if __name__ == "__main__":
    main()
