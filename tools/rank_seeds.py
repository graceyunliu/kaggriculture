#!/usr/bin/env python3
"""Rank seeds by candidate margin vs one opponent, both seats combined (Sep 12).

Companion to tools/gap_profile.py / allocation_matrix.py / spend_diff.py: this just finds WHICH seeds to
feed them. Per seed, plays both seat assignments and sums: own = cand money (both seats), opp = opponent
money (both seats), margin = own - opp. Both-seats-summed cancels the engine's per-seat weed-RNG bias
(mini_engine equivalent of seeded_h2h.py --both-seats).

Usage:
  KAGG_FIXED_SHOPS=1 python3 tools/rank_seeds.py candidates/O26_CARROT_SIZING.py \
      --opp Opponents/opp_frontier_v12.py --seeds 201-260 --json ranked.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me  # noqa: E402


def parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def run_game(cand_path, opp_path, seed, cand_seat):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agent_paths = [None, None]
    agent_paths[cand_seat] = cand_path
    agent_paths[1 - cand_seat] = opp_path
    agents = [me.load_agent(p) for p in agent_paths]
    state = me.structify(
        [
            {
                "observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                "action": {},
                "reward": 0.0,
                "status": "ACTIVE",
                "info": {},
            }
            for i in range(2)
        ]
    )
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if state[0].status != "ACTIVE" or step >= steps:
            break
    cand_money = state[cand_seat].observation.farms[cand_seat]["money"]
    opp_money = state[1 - cand_seat].observation.farms[1 - cand_seat]["money"]
    return cand_money, opp_money


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cand")
    ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    ap.add_argument("--top", type=int, default=10, help="how many worst/best seeds to report")
    args = ap.parse_args()

    seeds = parse_seeds(args.seeds)
    rows = []
    for seed in seeds:
        own_total = opp_total = 0.0
        for cand_seat in (0, 1):
            cm, om = run_game(args.cand, args.opp, seed, cand_seat)
            own_total += cm
            opp_total += om
        margin = own_total - opp_total
        rows.append({"seed": seed, "own": round(own_total, 1), "opp": round(opp_total, 1), "margin": round(margin, 1)})

    rows.sort(key=lambda r: r["margin"])
    worst = rows[: args.top]
    best = rows[-args.top :][::-1]

    print(f"{'seed':>6} {'own':>12} {'opp':>12} {'margin':>12}")
    for r in rows:
        print(f"{r['seed']:>6} {r['own']:>12.0f} {r['opp']:>12.0f} {r['margin']:>12.0f}")

    print(f"\nWorst {args.top} (biggest losses, ranked): {[r['seed'] for r in worst]}")
    print(f"Best {args.top} (biggest wins, ranked):   {[r['seed'] for r in best]}")

    margins = [r["margin"] for r in rows]
    print(f"\nn={len(rows)}  mean margin={sum(margins)/len(margins):+.0f}  min={min(margins):+.0f}  max={max(margins):+.0f}")

    out = {"cand": args.cand, "opp": args.opp, "rows": rows, "worst": worst, "best": best}
    if args.json:
        with open(args.json, "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
