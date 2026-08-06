#!/usr/bin/env python3
import importlib.util, sys
from kaggle_environments import make

def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent

SEEDS = [1,7,42,99,123,202,303,555,2024,8080,17,2025,3001,3002,3003]
TURNS_PER_DAY = 24
STARTING_MONEY = 3000

def run_one(agent_path, seed, opponent_path):
    a = load_agent(agent_path)
    b = load_agent(opponent_path)
    env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=False)
    env.info = {"seed": seed}
    env.run([a, b])
    steps = env.steps
    tile_days = 0.0
    prev_day = -1
    prev_tiles = 25
    for s in steps:
        obs0 = s[0].observation
        day = obs0.get("day", 0)
        farms = obs0.get("farms")
        if not farms:
            continue
        farm = farms[0]
        n_quads = len(farm["unlocked_quadrants"])
        tiles = 25 * n_quads
        if day != prev_day:
            # credit the day that just ended (or starting) with tiles owned during it
            prev_day = day
        prev_tiles = tiles
    # Instead of per-step tracking above (imprecise), redo with per-step day-weighted sum
    tile_days = 0.0
    last_day_seen = -1
    for s in steps:
        obs0 = s[0].observation
        day = obs0.get("day", 0)
        farms = obs0.get("farms")
        if not farms:
            continue
        tiles = 25 * len(farms[0]["unlocked_quadrants"])
        tile_days += tiles / TURNS_PER_DAY  # each step is 1/24th of a day
    final_money = steps[-1][0].reward
    net = final_money - STARTING_MONEY
    return final_money, net, tile_days

def main():
    agent_path = sys.argv[1]
    opponent_path = sys.argv[2] if len(sys.argv) > 2 else "main_v8.3.py"
    results = []
    for seed in SEEDS:
        final_money, net, tile_days = run_one(agent_path, seed, opponent_path)
        rate = net / tile_days if tile_days else 0
        results.append((seed, final_money, net, tile_days, rate))
        print(f"seed={seed:5d} final=${final_money:8.0f} net=${net:8.0f} tile_days={tile_days:7.1f} $/tile/day={rate:6.3f}")
    avg_net = sum(r[2] for r in results) / len(results)
    avg_td = sum(r[3] for r in results) / len(results)
    avg_rate = sum(r[4] for r in results) / len(results)
    pooled_rate = sum(r[2] for r in results) / sum(r[3] for r in results)
    print(f"\nAVG net=${avg_net:.0f}  avg tile_days={avg_td:.1f}  avg of per-seed rates=${avg_rate:.3f}/tile/day  pooled rate=${pooled_rate:.3f}/tile/day")

if __name__ == "__main__":
    main()
