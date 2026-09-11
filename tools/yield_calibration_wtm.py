#!/usr/bin/env python3
"""Yield-per-planting calibration for WHEAT/TOMATO/MELON (Sep 12 discovery-phase, step 2 of Grace's
calibration sequence) -- same method O24/O26 used for STRAWBERRY/CARROT (tools/allocation_matrix.py's
per-line plantings/out_units), extended to the three crops whose CROP_SPECS "units" constant has never
been checked against realized yield: WHEAT=5.0, TOMATO=5.0, MELON=6.0 (candidates/K_SELFMODEL.py).

Reuses tools/allocation_matrix.run() as a library (same engine-driving code, no reimplementation) --
aggregates plantings and out_units per crop across seeds/opponents for OUR farm only (seat 0), reports
realized units/planting vs the assumed constant.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/yield_calibration_wtm.py CAND --seeds 11-30
"""
import sys, os, statistics, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "tools"))
import allocation_matrix as am

OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}
CROPS = ["WHEAT", "TOMATO", "MELON", "STRAWBERRY", "CARROT"]
ASSUMED = {"WHEAT": 5.0, "TOMATO": 5.0, "MELON": 6.0, "STRAWBERRY": 7.5, "CARROT": 3.0}


def _parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-"); out.extend(range(int(lo), int(hi) + 1))
        else:
            out.append(int(part))
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--seeds", default="11-30")
    ap.add_argument("--opps", default="peter,alaylm,bahaen,yangk")
    a = ap.parse_args(); os.chdir(ROOT)
    seeds = _parse_seeds(a.seeds)
    opp_names = a.opps.split(",")
    per_game = {c: [] for c in CROPS}   # list of (plantings, out_units) per game, our farm only
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for s in seeds:
            _, M, _ = am.run(a.cand, opp, s)
            for c in CROPS:
                plant = M[0][c]["plantings"]; out = M[0][c]["out_units"]
                if plant > 0:
                    per_game[c].append((plant, out))
    print(f"cand={a.cand}  opps={opp_names}  seeds={a.seeds}  n_games_with_plantings shown per crop\n")
    print(f"{'crop':10s} {'assumed u/plant':>15s} {'n_games':>8s} {'mean plant':>10s} {'mean out':>9s} {'realized u/plant':>17s} {'ratio realized/assumed':>22s}")
    for c in CROPS:
        rows = per_game[c]
        if not rows:
            print(f"{c:10s}  -- no plantings observed in this sample --")
            continue
        tot_plant = sum(r[0] for r in rows); tot_out = sum(r[1] for r in rows)
        realized = tot_out / tot_plant if tot_plant else 0.0
        ratio = realized / ASSUMED[c]
        # per-game unit/planting distribution for a spread check
        per_game_ratio = [r[1] / r[0] for r in rows if r[0] > 0]
        lo, hi = (min(per_game_ratio), max(per_game_ratio)) if per_game_ratio else (0, 0)
        print(f"{c:10s} {ASSUMED[c]:15.1f} {len(rows):8d} {tot_plant/len(rows):10.1f} {tot_out/len(rows):9.1f} {realized:17.2f} {ratio:22.2f}   (per-game range {lo:.1f}-{hi:.1f})")
