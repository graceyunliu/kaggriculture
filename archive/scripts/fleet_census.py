#!/usr/bin/env python3
"""One-off: run agent_a vs agent_b on a single seed, print per-day animal
counts + money + hand counts for both farms, to check the opening-sequence
tempo hypothesis (opponent's fleet completes ~day10 vs ours ~day12)."""
import importlib.util
import sys
from kaggle_environments import make


def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def animal_count(farm):
    n = 0
    for row in farm.get("tiles", []) or []:
        for t in row:
            if isinstance(t, dict) and "animal" in t:
                n += 1
    return n


def main():
    agent_a_path, agent_b_path = sys.argv[1], sys.argv[2]
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    a = load_agent(agent_a_path)
    b = load_agent(agent_b_path)
    env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=False)
    env.info = {"seed": seed}
    env.run([a, b])

    seen_days = set()
    print(f"{'day':>4} {'A_animals':>10} {'A_hands':>8} {'A_money':>10} "
          f"{'B_animals':>10} {'B_hands':>8} {'B_money':>10}")
    for step in env.steps:
        obs0 = step[0].observation
        day = obs0.get("day")
        hour = obs0.get("hour")
        if hour != 0 or day in seen_days:
            continue
        seen_days.add(day)
        farms = obs0.get("farms", [])
        fa, fb = farms[0], farms[1]
        print(f"{day:>4} {animal_count(fa):>10} {len(fa.get('hands', [])):>8} "
              f"{fa.get('money', 0):>10.0f} {animal_count(fb):>10} "
              f"{len(fb.get('hands', [])):>8} {fb.get('money', 0):>10.0f}")

    final = env.steps[-1]
    print(f"\nFinal: A reward {final[0].reward:.0f} ({final[0].status}), "
          f"B reward {final[1].reward:.0f} ({final[1].status})")


if __name__ == "__main__":
    main()
