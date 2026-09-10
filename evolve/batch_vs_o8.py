#!/usr/bin/env python3
"""Batch candidate harness (Sep 9). For each candidate file:
  (a) paired same-seed margin vs the frontier O8 (self-play), DEV seeds;
  (b) own-money delta vs O8 across a panel of real opponents (4 ladder tapes + clone),
      paired by seed (cand's money vs opp minus O8's money vs same opp, same seed).
(b) matters for opponent-interaction mechanisms (e.g. melon first-mover) that are invisible
in self-play vs O8. O8's panel numbers are cached in evolve/_o8_panel_cache.json.
Usage: python3 evolve/batch_vs_o8.py cand1.py cand2.py ... [--held] [--seeds 1-10]
"""
import sys, os, json, math, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "evolve"))
import cascade

O8 = os.environ.get("BASE", "candidates/O8_PURE_ANIMAL_THROTTLE.py")
PANEL = {
    "peter":  "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk":  "Opponents/tape_yangkuang2_106819729.py",
    "clone":  "Opponents/opp_scenario_v14.py",
}
CACHE = os.path.join(ROOT, "evolve", "_panel_cache_" + os.path.basename(O8).replace(".py","") + ("_margin" if os.environ.get("PANEL_METRIC", "margin") == "margin" else "") + ".json")

def tstat(vals):
    n = len(vals); m = sum(vals)/n
    var = sum((v-m)**2 for v in vals)/(n-1) if n > 1 else 0.0
    se = math.sqrt(var/n) if var > 0 else 0.0
    return m, (m/se if se > 0 else 0.0)

MARGIN = os.environ.get("PANEL_METRIC", "margin") == "margin"
def own_money(cand, opp, seeds):
    """Per-seed panel metric: paired margin (cand - opp) by default (the ladder scores margins and both players share
    the game's shop draw), or own money if PANEL_METRIC=own."""
    r, _ = cascade._eval(cand, opp, seeds, "master", jobs=5)
    if MARGIN:
        return {str(s): (r["per_seed"][s]["a"] - r["per_seed"][s]["b"])/2.0 for s in seeds}, r["agent_errors"]
    return {str(s): r["per_seed"][s]["a"]/2.0 for s in seeds}, r["agent_errors"]

def o8_panel(seeds):
    key = ",".join(map(str, seeds))
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    if key not in cache:
        cache[key] = {}
        for name, opp in PANEL.items():
            cache[key][name], _ = own_money(O8, opp, seeds)
        json.dump(cache, open(CACHE, "w"))
    return cache[key]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cands", nargs="+")
    ap.add_argument("--held", action="store_true")
    ap.add_argument("--nopanel", action="store_true")
    ap.add_argument("--seeds", default=None, help="e.g. 31-50")
    a = ap.parse_args()
    seeds = list(range(11, 31)) if a.held else list(range(1, 11))
    if a.seeds:
        lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    base = None if a.nopanel else o8_panel(seeds)
    print(f"{'candidate':34s} {'vsO8 margin':>12s} {'t':>6s} {'w-l':>6s} | {'panel delta':>12s} {'t':>6s}  per-opp deltas")
    for c in a.cands:
        r, _ = cascade._eval(c, O8, seeds, "master", jobs=5)
        errs = r["agent_errors"]
        line = f"{os.path.basename(c)[:34]:34s} {r['mean_margin_per_game']:12.0f} {r['t']:6.2f} {r['wins']:>2d}-{r['losses']:<3d}"
        if base is not None:
            deltas_all = []; per = []
            for name, opp in PANEL.items():
                mine, e2 = own_money(c, opp, seeds)
                errs = [errs[0] + e2[0], errs[1] + e2[1]]
                d = [mine[str(s)] - base[name][str(s)] for s in seeds]
                deltas_all += d
                m, t = tstat(d)
                per.append(f"{name}:{m:+.0f}(t{t:.1f})")
            m, t = tstat(deltas_all)
            line += f" | {m:12.0f} {t:6.2f}  " + " ".join(per)
        if errs[0]:
            line += f"  !!AGENT_ERRORS={errs[0]}"
        print(line, flush=True)

if __name__ == "__main__":
    main()
