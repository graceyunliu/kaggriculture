#!/usr/bin/env python3
"""Deeper diagnostic runner for v8 fertilize candidates: FERTTRACE stderr
capture (see fert_trace.py's docstring for why env.logs is needed instead
of live stdout) PLUS final weed count and peak/final animal-fleet size,
read directly off env.steps (available regardless of debug=False -- only
per-agent stdout/stderr is captured/hidden, not the state itself)."""
import argparse
import importlib.util

from kaggle_environments import make


def load_agent(path):
    spec = importlib.util.spec_from_file_location(path, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.agent


def count_weeds(tiles):
    return sum(1 for row in tiles for t in row if isinstance(t, dict) and t.get("kind") == "WEED")


def count_animals(tiles):
    return sum(1 for row in tiles for t in row if isinstance(t, dict) and t.get("kind") == "PASTURE" and t.get("animal"))


def run(agent_a_path, agent_b_path, seed, turns=720, swap=False):
    a = load_agent(agent_a_path)
    b = load_agent(agent_b_path)
    env = make("kaggriculture", configuration={"episodeSteps": turns}, debug=False)
    env.info = {"seed": seed}
    players = [b, a] if swap else [a, b]
    env.run(players)

    names = (agent_b_path, agent_a_path) if swap else (agent_a_path, agent_b_path)
    idx_a = 1 if swap else 0  # index of agent_a's seat in the final farms list

    peak_animals = [0, 0]
    for step in env.steps:
        obs = step[0].observation
        if not hasattr(obs, "farms") or not obs.farms:
            continue
        for i in range(2):
            peak_animals[i] = max(peak_animals[i], count_animals(obs.farms[i].tiles))

    final_obs = env.steps[-1][0].observation
    final_weeds = [count_weeds(final_obs.farms[i].tiles) for i in range(2)]
    final_animals = [count_animals(final_obs.farms[i].tiles) for i in range(2)]
    final_money = [env.steps[-1][0].reward, env.steps[-1][1].reward]

    fert_lines = {0: [], 1: []}
    for step_logs in env.logs:
        for i, log in enumerate(step_logs):
            if not isinstance(log, dict):
                continue
            for stream in ("stdout", "stderr"):
                text = log.get(stream, "") or ""
                if "FERTTRACE" in text:
                    for line in text.splitlines():
                        if "FERTTRACE" in line:
                            fert_lines[i].append(line)

    print(f"--- seed={seed} swap={swap}  seat0={names[0]}  seat1={names[1]} ---")
    for i in range(2):
        label = names[i]
        last_fert = fert_lines[i][-1] if fert_lines[i] else "(no FERTTRACE captured)"
        print(f"  seat{i} [{label}]: final_money={final_money[i]:.0f} "
              f"final_weeds={final_weeds[i]} peak_animals={peak_animals[i]} "
              f"final_animals={final_animals[i]}")
        print(f"           {last_fert}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("agent_a")
    p.add_argument("agent_b")
    p.add_argument("--seeds", type=int, nargs="+", default=[1])
    p.add_argument("--turns", type=int, default=720)
    p.add_argument("--both-seats", action="store_true")
    args = p.parse_args()
    for seed in args.seeds:
        run(args.agent_a, args.agent_b, seed, args.turns, swap=False)
        if args.both_seats:
            run(args.agent_a, args.agent_b, seed, args.turns, swap=True)


if __name__ == "__main__":
    main()
