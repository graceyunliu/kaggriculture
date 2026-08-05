#!/usr/bin/env python3
"""Quick mechanism-trace diagnostic: run one seeded game for a given agent
vs v7.9, and report per-day weed count, watering coverage, harvest tile
count, and action-type tallies for player 0 (the candidate). Not a
decision tool by itself -- just instrumentation to see WHERE money is
being lost/gained relative to v7.9's known-good baseline behavior.
"""
import argparse
import importlib.util
import sys
from collections import Counter

from kaggle_environments import make


def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    p = argparse.ArgumentParser()
    p.add_argument("agent_a")
    p.add_argument("agent_b")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--turns", type=int, default=720)
    args = p.parse_args()

    mod_a = load_agent(args.agent_a)
    mod_b = load_agent(args.agent_b)
    agent_a = mod_a.agent
    agent_b = mod_b.agent

    action_counts = Counter()
    fertilize_applied = 0
    fertilizer_picked = 0
    fertilizer_sold_units = 0

    orig_agent_func = mod_a.agent

    def wrapped_a(obs, configuration=None):
        result = orig_agent_func(obs, configuration)
        farmer_op = result.get("farmer")
        hand_ops = result.get("hands", [])
        for op in [farmer_op] + hand_ops:
            if not op:
                continue
            key = op[0]
            action_counts[key] += 1
            if key == "FERTILIZE":
                nonlocal_fert = True
        market = result.get("market", [])
        for order in market:
            if order and order[0] == "SELL" and len(order) > 1 and order[1] == "FERTILIZER":
                pass
        return result

    env = make("kaggriculture", configuration={"episodeSteps": args.turns}, debug=False)
    env.info = {"seed": args.seed}
    env.run([wrapped_a, agent_b])

    final = env.steps[-1]
    ra, rb = final[0].reward, final[1].reward
    sa, sb = final[0].status, final[1].status
    print(f"Final: A({args.agent_a})={ra}  B({args.agent_b})={rb}  status=({sa},{sb})")
    print("Action counts (player A / candidate):")
    for k, v in action_counts.most_common(30):
        print(f"  {k:20s} {v}")

    # Per-day weed/water/harvest trace for player A (candidate), sampled at hour 0 each day
    print("\nDay-by-day (player A) at hour 0: weeds / empty / hands / money / shed_load / FERTILIZER-in-shed")
    days_seen = set()
    for step in env.steps:
        obs0 = step[0].observation
        day = obs0.get("day")
        hour = obs0.get("hour")
        if hour != 0 or day in days_seen:
            continue
        days_seen.add(day)
        farms = obs0.get("farms")
        if not farms:
            continue
        player_idx = obs0.get("player", 0)
        me = farms[player_idx]
        tiles = me.get("tiles", [])
        weeds = sum(1 for row in tiles for t in row if isinstance(t, dict) and t.get("kind") == "WEED")
        empty = sum(1 for row in tiles for t in row if t is None)
        n_hands = len(me.get("hands", []))
        money = me.get("money")
        shed = obs0.get("private", {}).get("shed", {})
        shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)
        fert_shed = shed.get("FERTILIZER", 0)
        print(f"  day {day:>2}: weeds={weeds:>3} empty={empty:>3} hands={n_hands:>2} money={money:>8.0f} shed_load={shed_load:>3} fert_in_shed={fert_shed:>3}")


if __name__ == "__main__":
    main()
