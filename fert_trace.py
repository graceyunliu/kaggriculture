#!/usr/bin/env python3
"""Instrumentation-only runner for the v8 fertilize candidates (D/E).

kaggle_environments' Agent.act() redirects each agent's stdout/stderr into
a per-step StringIO buffer instead of the real console (see agent.py:
`with StringIO() as out_buffer, ... redirect_stdout(out_buffer)`), even
with debug=False. seeded_h2h.py never reads those buffers back, so any
print() inside an agent (e.g. main_v8_candidateD.py's end-of-match
"FERTTRACE ..." line) is captured but silently discarded there.

This script re-runs the same match and reads the captured logs back from
env.logs (a list of per-step [log_agent0, log_agent1] dicts with 'stdout'/
'stderr' keys) to surface those FERTTRACE lines. It does not change
scoring/margin behavior at all -- same make()/run() calls as seeded_h2h.py,
just with the logs read back afterward. seeded_h2h.py itself is untouched.
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


def run_one(agent_a_path, agent_b_path, seed, turns=720, swap=False, tag=""):
    a = load_agent(agent_a_path)
    b = load_agent(agent_b_path)
    env = make("kaggriculture", configuration={"episodeSteps": turns}, debug=False)
    env.info = {"seed": seed}
    players = [b, a] if swap else [a, b]
    env.run(players)
    final = env.steps[-1]
    if swap:
        rb, ra = final[0].reward, final[1].reward
    else:
        ra, rb = final[0].reward, final[1].reward

    names = (agent_b_path, agent_a_path) if swap else (agent_a_path, agent_b_path)
    for step_logs in env.logs:
        for i, log in enumerate(step_logs):
            if not isinstance(log, dict):
                continue
            for stream in ("stdout", "stderr"):
                text = log.get(stream, "") or ""
                if "FERTTRACE" in text:
                    for line in text.splitlines():
                        if "FERTTRACE" in line:
                            print(f"[{tag} seed={seed} swap={swap} agent={names[i]}] {line}")
    return ra, rb


def main():
    p = argparse.ArgumentParser()
    p.add_argument("agent_a")
    p.add_argument("agent_b")
    p.add_argument("--seeds", type=int, nargs="+", default=[1])
    p.add_argument("--turns", type=int, default=720)
    p.add_argument("--both-seats", action="store_true")
    args = p.parse_args()

    for seed in args.seeds:
        ra, rb = run_one(args.agent_a, args.agent_b, seed, args.turns, swap=False, tag="norm")
        print(f"seed={seed} swap=False  A={ra:.0f}  B={rb:.0f}")
        if args.both_seats:
            ra2, rb2 = run_one(args.agent_a, args.agent_b, seed, args.turns, swap=True, tag="swap")
            print(f"seed={seed} swap=True   A={ra2:.0f}  B={rb2:.0f}")


if __name__ == "__main__":
    main()
