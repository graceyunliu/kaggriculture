#!/usr/bin/env python3
"""Stress-test main_v8.2.py's inherited HIRE-priority assumption (v7.11's
order-priority sort gives HIRE a flat High-band score of 700, which would
out-rank ordinary paced sells -- but not capacity/final/attack sells or the
ENORMOUS feed-emergency band -- in any turn where truncation actually
fires). Runs main_v82_trunc_trace.py (an instrumented copy, TRUNC lines
only, zero behavior change) across a hire-heavy/sell-heavy seed x opponent
sweep and aggregates whether truncation ever fires, and if so what gets
dropped.
"""
import importlib.util
import io
import sys
from contextlib import redirect_stdout, redirect_stderr
from collections import defaultdict

from kaggle_environments import make

AGENT_PATH = "trace_v82_truncation_agent.py"  # same directory as this script


def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent


def run_one(agent, opponent_path_or_name, seed, turns=720):
    if opponent_path_or_name in ("starter", "pass", "random"):
        opp = opponent_path_or_name
        opp_name = opponent_path_or_name
    else:
        opp = load_agent(opponent_path_or_name)
        opp_name = opponent_path_or_name.split("/")[-1]

    buf_out, buf_err = io.StringIO(), io.StringIO()
    env = make("kaggriculture", configuration={"episodeSteps": turns}, debug=True)
    env.info = {"seed": seed}
    with redirect_stdout(buf_out), redirect_stderr(buf_err):
        env.run([agent, opp])
    final = env.steps[-1]
    ra, rb = final[0].reward, final[1].reward
    sa, sb = final[0].status, final[1].status

    trunc_lines = [l for l in (buf_out.getvalue() + buf_err.getvalue()).splitlines() if l.startswith("TRUNC")]
    return opp_name, ra, rb, sa, sb, trunc_lines


def main():
    agent = load_agent(AGENT_PATH)
    seeds = [1, 7, 42, 99, 123, 202, 303]
    opponents = [
        "starter", "pass",
        "Opponents/opp_frontier_v12.py",
        "Opponents/opp_scenario_v14.py",
        "Opponents/opp_kaito_v21.py",
        "Opponents/opp_soil_v25.py",
        "Opponents/opp_replay_shield_v15.py",
        "main_v8.2.py",  # self-play mirror
    ]

    total_games = 0
    total_trunc_events = 0
    games_with_trunc = 0
    crashes = []
    hire_dropped_events = 0
    hire_kept_with_sell_dropped = 0
    all_trunc_lines = []

    for opp in opponents:
        for seed in seeds:
            total_games += 1
            opp_name, ra, rb, sa, sb, trunc_lines = run_one(agent, opp, seed)
            if sa != "DONE" or sb != "DONE":
                crashes.append((opp_name, seed, sa, sb))
            if trunc_lines:
                games_with_trunc += 1
                total_trunc_events += len(trunc_lines)
                all_trunc_lines.extend((opp_name, seed, l) for l in trunc_lines)
                import re
                for l in trunc_lines:
                    m_hd = re.search(r"hire_dropped=(\d+)", l)
                    m_hk = re.search(r"hire_kept=(\d+)", l)
                    m_dt = re.search(r"dropped_by_type=(\{[^}]*\})", l)
                    if m_hd and int(m_hd.group(1)) > 0:
                        hire_dropped_events += 1
                    if m_hk and int(m_hk.group(1)) > 0 and m_dt and "'SELL'" in m_dt.group(1):
                        hire_kept_with_sell_dropped += 1
            print(f"  [{opp_name} seed={seed}] money A={ra:.0f} B={rb:.0f} status=({sa},{sb}) trunc_events={len(trunc_lines)}")

    print(f"\n=== SUMMARY: {total_games} games across {len(opponents)} opponents x {len(seeds)} seeds ===")
    print(f"Games with >=1 truncation event: {games_with_trunc}/{total_games}")
    print(f"Total truncation events (turns where priced_orders > 10): {total_trunc_events}")
    print(f"Truncation events where a HIRE order was DROPPED (not just present): {hire_dropped_events}")
    print(f"Truncation events where HIRE was KEPT and a SELL was dropped: {hire_kept_with_sell_dropped}")
    if crashes:
        print(f"CRASHES: {crashes}")
    else:
        print("No crashes.")

    print("\n--- all TRUNC lines ---")
    for opp_name, seed, l in all_trunc_lines:
        print(f"  [{opp_name} seed={seed}] {l}")


if __name__ == "__main__":
    main()
