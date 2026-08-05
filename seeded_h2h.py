#!/usr/bin/env python3
"""Seeded head-to-head: agent_a vs agent_b, N seeds, aggregate win/money.

Per project convention: configuration={"seed": N} does NOT propagate to the
engine's weed-spawn RNG. Must set env.info["seed"] = N directly after make().
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
    p.add_argument("--swap-half", action="store_true", help="alternate seat to control for first-mover effects")
    args = p.parse_args()

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


if __name__ == "__main__":
    main()
