#!/usr/bin/env python3
"""One-off: what fraction of our own unit-turns are movement vs real work,
under the current v9.3 architecture (GLOBAL_TASK_ASSIGNMENT / assign_tasks
joint nearest-pair matching). Answers whether movement overhead (flagged
Aug 5 at 66% for the pre-assign_tasks v7.9) is still the dominant cost."""
import importlib.util
import sys
from collections import Counter
from kaggle_environments import make

def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent

MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}

def census(agent_path, seed):
    agent = load_agent(agent_path)
    env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=False)
    env.info = {"seed": seed}
    counts = Counter()
    def wrapped(obs):
        act = agent(obs)
        ops = [act.get("farmer")] + list(act.get("hands") or [])
        for op in ops:
            if not op:
                counts["none"] += 1
                continue
            verb = op[0]
            if verb in MOVES:
                counts["move"] += 1
            elif verb == "PASS":
                counts["pass"] += 1
            else:
                counts["work"] += 1
        return act
    env.run([wrapped, "pass"])
    total = sum(counts.values())
    print(f"seed {seed}: total unit-turns={total}  move={counts['move']} ({counts['move']/total:.1%})  "
          f"work={counts['work']} ({counts['work']/total:.1%})  pass={counts['pass']} ({counts['pass']/total:.1%})")
    final_money = env.steps[-1][0]["reward"]
    print(f"  final money: {final_money:,.0f}")

if __name__ == "__main__":
    agent_path = sys.argv[1] if len(sys.argv) > 1 else "main_v9.3_fertilize.py"
    seeds = [int(s) for s in sys.argv[2:]] or [1, 7, 42]
    for s in seeds:
        census(agent_path, s)
