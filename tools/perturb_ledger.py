#!/usr/bin/env python3
"""perturb_ledger.py -- §4.3 overfit-guard perturbation, per docs/SPEC-planner-from-tape.md.

Copies a ledger directory to a new directory. For every day_XX.json, with a deterministic
seed-0 RNG:
  - deletes up to 3 random PLANT tiles (sets them to an empty/GRASS tile)
  - adds up to 2 random WEED tiles (on previously empty/GRASS tiles)
  - removes one hand from farm.hands in state_h0, if any hands are present

`chores_available_h0` / `chores_hard_h0` are NOT recomputed (the bench only uses them to
score against the *tape's* original chores_done, which is unperturbed -- the point of this
tool is to test whether the candidate's plan degrades sensibly, e.g. digs the added weeds
and does not "escape" onto animal chores, when its own state_h0 differs slightly from what
it was tuned against). Does not modify the source ledger.

Usage:
  python3 tools/perturb_ledger.py evolve/expert/H32_s1/ evolve/expert/H32_s1_perturbed/
"""
from __future__ import annotations

import argparse
import copy
import json
import random
import shutil
from pathlib import Path

SEED = 0


def perturb_day(ledger_day, rng):
    h0 = ledger_day["state_h0"]
    tiles = h0["farm"]["tiles"]
    h = len(tiles)
    w = len(tiles[0]) if h else 0

    plant_positions = [
        (x, y) for y in range(h) for x in range(w)
        if isinstance(tiles[y][x], dict) and tiles[y][x].get("kind") == "PLANT"
    ]
    rng.shuffle(plant_positions)
    for (x, y) in plant_positions[:3]:
        tiles[y][x] = {"kind": "GRASS"}

    empty_positions = [
        (x, y) for y in range(h) for x in range(w)
        if not (isinstance(tiles[y][x], dict) and tiles[y][x].get("kind") not in (None, "GRASS"))
    ]
    rng.shuffle(empty_positions)
    for (x, y) in empty_positions[:2]:
        tiles[y][x] = {"kind": "WEED"}

    hands = h0["farm"].get("hands", [])
    if hands:
        idx = rng.randrange(len(hands))
        hands.pop(idx)

    return ledger_day


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="source ledger directory (e.g. evolve/expert/H32_s1/)")
    ap.add_argument("dst", help="destination directory for the perturbed ledger")
    a = ap.parse_args()

    src, dst = Path(a.src), Path(a.dst)
    dst.mkdir(parents=True, exist_ok=True)

    for f in sorted(src.glob("day_*.json")):
        ledger_day = json.load(open(f))
        rng = random.Random((SEED, ledger_day["day"]))
        perturbed = perturb_day(copy.deepcopy(ledger_day), rng)
        json.dump(perturbed, open(dst / f.name, "w"))

    summary_src = src / "summary.json"
    if summary_src.exists():
        shutil.copy(summary_src, dst / "summary.json")

    print(f"wrote perturbed ledger to {dst}")


if __name__ == "__main__":
    main()
