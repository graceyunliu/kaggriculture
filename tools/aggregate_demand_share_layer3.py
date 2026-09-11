#!/usr/bin/env python3
import json, glob, collections, os

ROOT = os.path.expanduser("~/mnt/Kaggriculture/experiments/demand_share_layer3_sep11")
TARGETS = [("MELON", "early"), ("MELON", "mid"), ("STRAWBERRY", "mid"), ("CARROT", "late")]

exposures = []
planted_all = []
sold_all = collections.defaultdict(list)  # crop -> list of prices (per game dedup by opp handled naturally since we just concat)
n_games = 0
opps = []

for path in sorted(glob.glob(os.path.join(ROOT, "*.json"))):
    with open(path) as f:
        d = json.load(f)
    opps.append((d["opp"], d["n_games"]))
    n_games += d["n_games"]
    exposures.extend(d["exposures"])
    planted_all.extend(d["planted_census"])
    for item, fid, price in d["sold_census"]:
        sold_all[item].append(price)

print(f"FULL LAYER-3 EXPOSURE -- opponents={opps} total_games={n_games} alt_share=0.35\n")

by_cell = collections.defaultdict(list)
for e in exposures:
    by_cell[(e["crop"], e["phase"])].append(e)

for c, ph in TARGETS:
    recs = by_cell.get((c, ph), [])
    planted = [1 for cc, p, d in planted_all if cc == c and p == ph]
    print(f"== {c} {ph} ==  (n_games={n_games})")
    print(f"  exposed decisions: {len(recs)}")
    if recs:
        cash_deltas = [r["cash_delta"] for r in recs]
        qty_deltas = [r["delta_qty"] for r in recs]
        occurs = sum(1 for r in recs if r["purchase_occurs"])
        print(f"  purchase occurs at baseline: {occurs}/{len(recs)} ({occurs/len(recs):.1%})")
        print(f"  total cash_delta across population (alt vs baseline): {sum(cash_deltas):.0f}  (mean per exposed decision: {sum(cash_deltas)/len(cash_deltas):.1f})")
        print(f"  mean qty_delta: {sum(qty_deltas)/len(qty_deltas):.2f}")
        other_excl = collections.Counter()
        for r in recs:
            other_excl.update(r["other_crops_excluded_this_turn"])
        print(f"  other crops excluded same-turn (opportunity-cost proxy, count of co-occurrences): {dict(other_excl)}")
        free_after = [r["free_cash_remaining_after"] for r in recs]
        space_after = [r["space_remaining_after"] for r in recs]
        print(f"  mean free cash remaining after this buy: {sum(free_after)/len(free_after):.1f}")
        print(f"  mean tile space remaining after this buy: {sum(space_after)/len(space_after):.2f}")
    print(f"  planted (this crop/phase, census across population): {len(planted)}")
    sold = sold_all.get(c, [])
    print(f"  sold (this crop, ALL games in population, all phases -- game-level context, not phase- or decision-isolated): {len(sold)}", end="")
    if sold:
        print(f", mean realized price: {sum(sold)/len(sold):.2f}, per-game avg units sold: {len(sold)/n_games:.1f}")
    else:
        print()
    if len(planted):
        print(f"  rough realization signal: total sold (whole game, all phases) / total planted (this phase only) = {len(sold)/len(planted):.2f} -- NOT a per-decision lineage ratio, see script docstring for scope limits")
    print()

with open(os.path.join(ROOT, "aggregate_full_population.json"), "w") as f:
    json.dump({"n_games": n_games, "opps": opps, "n_exposures": len(exposures)}, f, indent=2)
