#!/usr/bin/env python3
"""Held-out-tape check: paired margin AND own-money delta of CAND vs BASE across tapes NOT in the 4-tape panel.
Usage: KAGG_FIXED_SHOPS=1 python3 evolve/wide_tapes.py BASE CAND --seeds 11-20 [--tapes N]"""
import sys, os, argparse, glob, math
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "evolve"))
import cascade
PANEL = {"tape_peterparker_106816877.py", "tape_alaylm_106813359.py", "tape_bahaenes_106828159.py", "tape_yangkuang2_106819729.py"}
def t(xs):
    n = len(xs); m = sum(xs) / n; v = sum((x - m) ** 2 for x in xs) / (n - 1) if n > 1 else 0
    return m, (m / math.sqrt(v / n) if v > 0 else 0)
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("base"); ap.add_argument("cand"); ap.add_argument("--seeds", default="11-20"); ap.add_argument("--tapes", type=int, default=10); ap.add_argument("--skip", type=int, default=0)
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    tapes = sorted(p for p in glob.glob("Opponents/tape_*.py") if os.path.basename(p) not in PANEL)[a.skip:a.skip + a.tapes]
    allm, allo = [], []
    for tp in tapes:
        rb, _ = cascade._eval(a.base, tp, seeds, "master", jobs=5); rc, _ = cascade._eval(a.cand, tp, seeds, "master", jobs=5)
        dm = [((rc["per_seed"][s]["a"] - rc["per_seed"][s]["b"]) - (rb["per_seed"][s]["a"] - rb["per_seed"][s]["b"])) / 2 for s in seeds]
        do = [(rc["per_seed"][s]["a"] - rb["per_seed"][s]["a"]) / 2 for s in seeds]
        allm += dm; allo += do
        print(f"{os.path.basename(tp)[:32]:32s} margin {t(dm)[0]:+7.0f} (t{t(dm)[1]:4.1f})  own {t(do)[0]:+7.0f} (t{t(do)[1]:4.1f})   base margin vs tape {rb['mean_margin_per_game']:+8.0f}", flush=True)
    print(f"{'ALL':32s} margin {t(allm)[0]:+7.0f} (t{t(allm)[1]:4.1f})  own {t(allo)[0]:+7.0f} (t{t(allo)[1]:4.1f})  n={len(allm)}")
