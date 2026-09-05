#!/usr/bin/env python3
"""One-off: measure a few reference candidates' margins against the new frontier (H32),
so evolve/yardstick.conf's SMOKE_FLOOR/DEV_PROMOTE can be recalibrated the same way the
H10-era comment describes ("C1 scores about -14k... floor shifted accordingly").

    python3 tools/calibrate_yardstick.py

Prints margin/t/W-L for each reference candidate vs the new frontier, seeds 1-10 both seats,
plus a suggested SMOKE_FLOOR/DEV_PROMOTE (mean - 1 stdev of the reference margins, rounded to
the nearest 1000, so a genuinely-competitive-but-not-winning candidate still clears smoke).
"""
from __future__ import annotations
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "evolve"))

import mini_engine  # noqa: E402

FRONTIER = "candidates/H32.py"
SEEDS = list(range(1, 11))

# Reference candidates: known-weaker (C1, a control that should clearly fail smoke),
# known-competitive (P6, this project's best own-code planner), and the frontier itself
# (should be ~0 margin, a sanity check the harness is wired right).
REFERENCES = [
    ("C1", "candidates/C1.py"),
    ("P6", "candidates/P6_baseline.py"),   # frozen baseline, not candidates/P.py (may be mid-edit)
    ("H32_self", FRONTIER),
]

def main():
    print(f"Frontier: {FRONTIER}, seeds {SEEDS[0]}-{SEEDS[-1]}, both seats\n")
    margins = []
    for name, path in REFERENCES:
        p = ROOT / path
        if not p.exists():
            print(f"{name}: SKIP ({path} not found)")
            continue
        result = mini_engine.evaluate(str(p), FRONTIER, SEEDS, engine="master", both_seats=True)
        margin = result["mean_margin_per_game"]
        t = result.get("t")
        wins = result.get("wins")
        losses = result.get("losses")
        print(f"{name:10s} margin={margin:>10.0f}  t={t:>6.2f}  W-L={wins}-{losses}")
        if name != "H32_self":
            margins.append(margin)

    if margins:
        mean = statistics.mean(margins)
        stdev = statistics.pstdev(margins) if len(margins) > 1 else 0
        suggested_floor = round((mean - stdev) / 1000) * 1000
        suggested_promote = round((mean) / 1000) * 1000
        print(f"\nReference margins: mean={mean:.0f} stdev={stdev:.0f}")
        print(f"Suggested SMOKE_FLOOR  ≈ {suggested_floor}   (mean - 1 stdev, loose enough to pass a competitive-but-losing candidate)")
        print(f"Suggested DEV_PROMOTE  ≈ {suggested_promote}   (near the reference mean; tighten once more data comes in)")
        print("\nSanity-check these against the actual reference results above before writing them into yardstick.conf —")
        print("this is a starting point from ~10 seeds, not a final calibration.")

if __name__ == "__main__":
    main()
