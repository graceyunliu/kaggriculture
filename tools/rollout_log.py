#!/usr/bin/env python3
"""Record paired per-day net-worth rollouts."""
from __future__ import annotations
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.networth import networth_game
from tools.plot_rollout import plot_rollout

def parse_seeds(value):
    if isinstance(value, str) and "-" in value:
        start, end = (int(part) for part in value.split("-", 1))
        if end < start:
            raise ValueError("seed range end must be >= start")
        return list(range(start, end + 1))
    if isinstance(value, str):
        return [int(value)]
    return list(value)

def agent_stem(path):
    return Path(path).stem.replace(" ", "_")

def rollout(agent_a_path, agent_b_path, seeds, engine="master"):
    """Play each seed with A/B in both seat assignments and write flat records."""
    records = []
    for seed in parse_seeds(seeds):
        for seat in (0, 1):
            if seat == 0:
                first, second = agent_a_path, agent_b_path
            else:
                first, second = agent_b_path, agent_a_path
            first_traj, second_traj = networth_game(first, second, seed, engine)
            for day in range(30):
                if seat == 0:
                    net_a, net_b = first_traj[day], second_traj[day]
                else:
                    net_a, net_b = second_traj[day], first_traj[day]
                records.append({"seed": seed, "seat": seat, "day": day,
                                "networth_a": net_a, "networth_b": net_b})
    out_dir = ROOT / "tools" / "rollouts"
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    json_path = out_dir / f"{agent_stem(agent_a_path)}_vs_{agent_stem(agent_b_path)}_{timestamp}.json"
    json_path.write_text(json.dumps(records, indent=2) + "\n")
    png_path = plot_rollout(json_path)
    return json_path, png_path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("agent_a")
    parser.add_argument("agent_b")
    parser.add_argument("--seeds", required=True, help="seed or inclusive range such as 1-20")
    parser.add_argument("--engine", default="master")
    args = parser.parse_args()
    json_path, png_path = rollout(args.agent_a, args.agent_b, args.seeds, args.engine)
    print(json_path)
    print(png_path)

if __name__ == "__main__":
    main()
