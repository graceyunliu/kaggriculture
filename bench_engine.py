#!/usr/bin/env python3
"""Benchmark mini_engine with representative agent pairs."""
from __future__ import annotations

import argparse
import cProfile
import io
import pstats
import time
from pathlib import Path

import mini_engine as me

ROOT = Path(__file__).resolve().parent
PAIRS = [
    (ROOT / "candidates/E1.py", ROOT / "candidates/V3_12.py"),
    (ROOT / "candidates/C1.py", ROOT / "Opponents/tape_yuan800_104892947.py"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, nargs="+", default=[1, 2, 4])
    ap.add_argument("--profile-games", type=int, default=2)
    args = ap.parse_args()

    profiler = cProfile.Profile()
    profiler.enable()
    for a, b in PAIRS:
        for seed in range(1, args.profile_games + 1):
            me.run_game(a, b, seed, trace=True)
    profiler.disable()
    stream = io.StringIO()
    pstats.Stats(profiler, stream=stream).sort_stats("cumulative").print_stats(25)
    print(stream.getvalue())

    for trace in (True, False):
        t0 = time.perf_counter()
        games = 0
        for a, b in PAIRS:
            for seed in range(1, 5):
                me.run_game(a, b, seed, trace=trace)
                games += 1
        elapsed = time.perf_counter() - t0
        print(f"trace={trace}: {elapsed / games:.4f}s/game ({games / elapsed:.2f} games/s)")

    for workers in args.workers:
        t0 = time.perf_counter()
        games = 0
        with __import__("multiprocessing").get_context("spawn").Pool(workers) as pool:
            for a, b in PAIRS:
                jobs = [(str(a), str(b), seed, "master", None, False, False) for seed in range(1, 5)]
                pool.map(me._job, jobs)
                games += len(jobs)
        elapsed = time.perf_counter() - t0
        print(f"workers={workers}: {elapsed:.3f}s, {games / elapsed:.2f} games/s")


if __name__ == "__main__":
    main()
