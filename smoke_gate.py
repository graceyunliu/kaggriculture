#!/usr/bin/env python3
"""Two-stage gate: 5-seed smoke (fast) then optional 15-seed confirm, both
vs a baseline champion AND vs Opponents/opp_scenario_v14.py (paired,
both-seats each). Prints both readings."""
import subprocess
import sys

SMOKE_SEEDS = "1 7 42 99 123"
FULL_SEEDS = "1 7 42 99 123 202 303 555 2024 8080 17 2025 3001 3002 3003"
OPP = "Opponents/opp_scenario_v14.py"


def run(variant, baseline, seeds, label):
    print(f"\n=== {label}: {variant} vs {baseline} ({len(seeds.split())} seeds, both-seats) ===")
    subprocess.run(
        [sys.executable, "seeded_h2h.py", variant, baseline, "--seeds", *seeds.split(), "--both-seats"],
        check=False,
    )


if __name__ == "__main__":
    variant = sys.argv[1]
    stage = sys.argv[2] if len(sys.argv) > 2 else "smoke"
    seeds = FULL_SEEDS if stage == "full" else SMOKE_SEEDS
    run(variant, "main_v9.5_statehygiene.py", seeds, "vs v9.5")
    run(variant, OPP, seeds, "vs opp_scenario_v14")
