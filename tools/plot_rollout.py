#!/usr/bin/env python3
"""Plot mean paired-seat net-worth trajectories with one-standard-error bands."""
from __future__ import annotations
import argparse
import json
import math
import statistics
from pathlib import Path

def plot_rollout(json_path, png_path=None):
    import matplotlib.pyplot as plt
    path = Path(json_path)
    records = json.loads(path.read_text())
    seeds = sorted({r["seed"] for r in records})
    days = sorted({r["day"] for r in records})
    grouped = {}
    for record in records:
        grouped.setdefault((record["seed"], record["day"]), []).append(record)
    means = {"a": [], "b": []}
    bands = {"a": [], "b": []}
    for day in days:
        for key, field in (("a", "networth_a"), ("b", "networth_b")):
            values = [statistics.mean(r[field] for r in grouped[(seed, day)])
                      for seed in seeds if (seed, day) in grouped]
            means[key].append(statistics.mean(values))
            bands[key].append(statistics.stdev(values) / math.sqrt(len(values)) if len(values) > 1 else 0.0)
    output = Path(png_path) if png_path else path.with_suffix(".png")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    for key, label, color in (("a", "Agent A", "#2563eb"), ("b", "Agent B", "#dc2626")):
        center, stderr = means[key], bands[key]
        ax.plot(days, center, label=label, color=color, linewidth=2)
        ax.fill_between(days, [m - e for m, e in zip(center, stderr)],
                        [m + e for m, e in zip(center, stderr)], color=color, alpha=0.18)
    ax.set_title(f"Mean net worth by day ({len(seeds)} seeds, paired seats)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Net worth")
    ax.set_xlim(min(days), max(days))
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output)
    plt.close(fig)
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path")
    parser.add_argument("--output", default=None)
    args = parser.parse_args()
    print(plot_rollout(args.json_path, args.output))

if __name__ == "__main__":
    main()
