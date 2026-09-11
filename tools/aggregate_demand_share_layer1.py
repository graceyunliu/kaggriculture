#!/usr/bin/env python3
import json, glob, collections, os

ROOT = os.path.expanduser("~/mnt/Kaggriculture/experiments/demand_share_layer1_sep11")
PHASES = ["early", "mid", "late"]
CROPS = ["WHEAT", "CARROT", "MELON", "STRAWBERRY", "TOMATO"]

gate_elig = collections.Counter()
gate_exc = collections.Counter()
gate_flip = collections.Counter()
siz_elig = collections.Counter()
siz_bound = collections.Counter()
siz_diff = collections.defaultdict(list)
n_games = 0
opps = []

for path in sorted(glob.glob(os.path.join(ROOT, "*.json"))):
    if "11-30" in path or "aggregate" in path:
        continue
    with open(path) as f:
        d = json.load(f)
    opps.append((d["opp"], d["n_games"]))
    n_games += d["n_games"]
    for k, v in d["gate_eligible"].items():
        c, p = k.split("|"); gate_elig[(c, p)] += v
    for k, v in d["gate_excluded_baseline"].items():
        c, p = k.split("|"); gate_exc[(c, p)] += v
    for k, v in d["gate_flips_under_alt"].items():
        c, p = k.split("|"); gate_flip[(c, p)] += v
    for k, v in d["sizing_eligible"].items():
        c, p = k.split("|"); siz_elig[(c, p)] += v
    for k, v in d["sizing_bound_by_demand"].items():
        c, p = k.split("|"); siz_bound[(c, p)] += v
    for k, v in d["sizing_material_diff"].items():
        c, p = k.split("|"); siz_diff[(c, p)].extend(v)

print(f"FULL LAYER-1 POPULATION -- opponents={opps} total_games={n_games} alt_share=0.35 (frozen from pilot, not re-tuned)")
print("cand=O26_CARROT_SIZING, KAGG_FIXED_SHOPS=1, seeds=11-30,71-90 (2x20-seed sets), both seats, full horizon\n")

print("== LAYER 1a: GATE (crop excluded from consideration this iteration by demand-room shortfall) ==")
print(f"{'crop':10s} {'phase':6s} {'eligible':>9s} {'excluded':>9s} {'excl_rate':>10s} {'flips_under_alt':>16s} {'flip_rate':>10s}")
for c in CROPS:
    for ph in PHASES:
        elig = gate_elig[(c, ph)]
        if not elig:
            continue
        exc = gate_exc[(c, ph)]
        flips = gate_flip[(c, ph)]
        print(f"{c:10s} {ph:6s} {elig:9d} {exc:9d} {exc/elig:10.2%} {flips:16d} {flips/elig:10.2%}")

print("\n== LAYER 1b: SIZING (was demand-room the strictest of the four caps on k?) ==")
print(f"{'crop':10s} {'phase':6s} {'eligible':>9s} {'demand_bound':>13s} {'bound_rate':>11s}")
for c in CROPS:
    for ph in PHASES:
        elig = siz_elig[(c, ph)]
        if not elig:
            continue
        bound = siz_bound[(c, ph)]
        print(f"{c:10s} {ph:6s} {elig:9d} {bound:13d} {bound/elig:11.2%}")

print("\n== LOCAL LAYER 2 (single-decision, same-trajectory): counterfactual k delta under alt_share=0.35 ==")
print(f"{'crop':10s} {'phase':6s} {'n_diffs':>8s} {'mean_delta_k':>13s} {'max_abs_delta':>14s} {'pct_of_sizing_elig':>19s}")
for c in CROPS:
    for ph in PHASES:
        diffs = siz_diff[(c, ph)]
        elig = siz_elig[(c, ph)]
        if not diffs:
            continue
        mean_d = sum(diffs) / len(diffs)
        max_abs = max(abs(x) for x in diffs)
        pct = len(diffs) / elig if elig else float("nan")
        print(f"{c:10s} {ph:6s} {len(diffs):8d} {mean_d:13.2f} {max_abs:14d} {pct:19.2%}")

with open(os.path.join(ROOT, "aggregate_full_population.json"), "w") as f:
    json.dump({
        "n_games": n_games, "opps": opps, "alt_share": 0.35,
        "gate_eligible": {f"{c}|{p}": v for (c, p), v in gate_elig.items()},
        "gate_excluded_baseline": {f"{c}|{p}": v for (c, p), v in gate_exc.items()},
        "gate_flips_under_alt": {f"{c}|{p}": v for (c, p), v in gate_flip.items()},
        "sizing_eligible": {f"{c}|{p}": v for (c, p), v in siz_elig.items()},
        "sizing_bound_by_demand": {f"{c}|{p}": v for (c, p), v in siz_bound.items()},
        "sizing_material_diff": {f"{c}|{p}": v for (c, p), v in siz_diff.items()},
    }, f, indent=2)
