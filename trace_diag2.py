#!/usr/bin/env python3
"""Mechanism trace: day-by-day weeds/empty/hands/money/pasture-count for
player A (candidate), one seed, vs player B (opponent). Adds pasture
(animal) count on top of trace_diag.py's fields, needed to diagnose fleet
size / weed count for the F/G gate-fix candidates.
"""
import argparse
import importlib.util

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

    env = make("kaggriculture", configuration={"episodeSteps": args.turns}, debug=False)
    env.info = {"seed": args.seed}
    env.run([agent_a, agent_b])

    final = env.steps[-1]
    ra, rb = final[0].reward, final[1].reward
    print(f"Final: A({args.agent_a})={ra}  B({args.agent_b})={rb}")

    print("\nDay-by-day (player A) at hour 0: weeds/empty/hands/money/pastures/shed_load")
    days_seen = set()
    peak_pastures = 0
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
        pastures = sum(1 for row in tiles for t in row
                        if isinstance(t, dict) and t.get("kind") == "PASTURE" and t.get("animal"))
        peak_pastures = max(peak_pastures, pastures)
        n_hands = len(me.get("hands", []))
        money = me.get("money")
        shed = obs0.get("private", {}).get("shed", {})
        shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)
        print(f"  day {day:>2}: weeds={weeds:>3} empty={empty:>3} hands={n_hands:>2} "
              f"money={money:>8.0f} pastures={pastures:>2} shed_load={shed_load:>3}")
    print(f"\nPEAK pastures (player A): {peak_pastures}")


if __name__ == "__main__":
    main()
