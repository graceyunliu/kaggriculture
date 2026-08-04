#!/usr/bin/env python3
"""Quick local regression check for a Kaggriculture agent.

Usage:
    python3 smoke_test.py main_v5.py
    python3 smoke_test.py main_v5.py --opponent starter --turns 720
    python3 smoke_test.py main_v5.py --vs main_v4.py   # compare two of your own versions

Run this before every submission. It will:
  1. Load the agent's `agent(obs, configuration=None)` function from the given file.
  2. Play a full (or --turns) game against a built-in opponent ("random",
     "starter", or "pass") or another local agent file.
  3. Print final money and status for both players, and flag crashes/timeouts
     (status != DONE) which are auto-losses per the design doc's Layer 5
     robustness guards.
"""
import argparse
import importlib.util
import sys
import time


def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "agent"):
        raise AttributeError(f"{path} has no top-level `agent(obs, configuration=None)` function")
    return module.agent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("agent_file", help="Path to your agent .py file (must define agent())")
    parser.add_argument("--opponent", default="random", help="'random', 'starter', 'pass', or a path to another agent .py file")
    parser.add_argument("--turns", type=int, default=720, help="episodeSteps (default: full 30-day season)")
    args = parser.parse_args()

    from kaggle_environments import make

    p0 = load_agent(args.agent_file)
    p1 = args.opponent if args.opponent in ("random", "starter", "pass") else load_agent(args.opponent)

    env = make("kaggriculture", configuration={"episodeSteps": args.turns}, debug=True)
    t0 = time.time()
    try:
        env.run([p0, p1])
    except Exception as e:
        print(f"CRASH during env.run(): {e!r}")
        sys.exit(1)
    elapsed = time.time() - t0

    final = env.steps[-1]
    names = [args.agent_file, args.opponent if isinstance(p1, str) else args.opponent]
    ok = True
    print(f"\n{args.turns} turns in {elapsed:.1f}s")
    for i, s in enumerate(final):
        flag = "" if s.status == "DONE" else "  <-- NOT DONE (crash/timeout = auto-loss)"
        print(f"  Player {i} ({names[i]}): reward={s.reward}, status={s.status}{flag}")
        if s.status != "DONE":
            ok = False

    if not ok:
        print("\nFAIL: a player did not finish cleanly.")
        sys.exit(1)
    print("\nOK: both players finished cleanly.")


if __name__ == "__main__":
    main()
