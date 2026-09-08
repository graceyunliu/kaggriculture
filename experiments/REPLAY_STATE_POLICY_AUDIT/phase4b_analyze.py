import sys, json, math
sys.path.insert(0, ".")
from mini_engine import run_game

BASE = "experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_variants/variant0_baseline.py"
V1 = "experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_variants/variant1_melon_floor0.py"
V2 = "experiments/REPLAY_STATE_POLICY_AUDIT/phase4b_variants/variant2_melon_floor50.py"

def per_player_stats(trace_p):
    opp_days = 0
    sold_days = 0
    units = 0
    revenue = 0.0
    weeds_seq = trace_p.get("weeds", [])
    for day_idx, shed in enumerate(trace_p["shed"]):
        melon = shed.get("MELON", 0)
        if melon > 0:
            opp_days += 1
    for day_idx, sales in enumerate(trace_p["sales"]):
        m = sales.get("MELON")
        if m:
            sold_days += 1
            units += m[0]
            revenue += m[1]
    return {"opportunity_days": opp_days, "sold_days": sold_days,
            "melon_units_sold": units, "melon_revenue": revenue,
            "weeds_seq": weeds_seq}

def run_pair(variant_path, seeds, engine="master", jobs=6):
    rows = []
    for seed in seeds:
        for swap in (False, True):
            a, b = (variant_path, BASE) if not swap else (BASE, variant_path)
            r = run_game(a, b, seed=seed, engine=engine, trace=True)
            ta, tb = r["trace"][0], r["trace"][1]
            sa, sb = per_player_stats(ta), per_player_stats(tb)
            # figure out which slot is "variant" and which is "baseline"
            variant_slot, base_slot = (sa, sb) if not swap else (sb, sa)
            variant_money, base_money = (r["money"][0], r["money"][1]) if not swap else (r["money"][1], r["money"][0])
            variant_weeds = (ta if not swap else tb)["weeds"]
            base_weeds = (tb if not swap else ta)["weeds"]
            rows.append({
                "seed": seed, "swap": swap,
                "variant_money": variant_money, "base_money": base_money,
                "variant_stats": variant_slot, "base_stats": base_slot,
                "variant_weeds": variant_weeds, "base_weeds": base_weeds,
            })
    return rows

def summarize(rows, label):
    def agg(key_stats, field):
        return sum(r[key_stats][field] for r in rows)
    v_opp = agg("variant_stats", "opportunity_days")
    v_sold = agg("variant_stats", "sold_days")
    v_rev = agg("variant_stats", "melon_revenue")
    v_units = agg("variant_stats", "melon_units_sold")
    b_opp = agg("base_stats", "opportunity_days")
    b_sold = agg("base_stats", "sold_days")
    b_rev = agg("base_stats", "melon_revenue")
    b_units = agg("base_stats", "melon_units_sold")
    margins = [r["variant_money"] - r["base_money"] for r in rows]
    # pair up swap=False/True per seed for seat-controlled margin
    seed_margins = {}
    for r in rows:
        seed_margins.setdefault(r["seed"], []).append(r["variant_money"] - r["base_money"])
    paired_margins = [sum(v) for v in seed_margins.values()]  # sums both seats -> seat-controlled
    mean_pm = sum(paired_margins)/len(paired_margins)
    if len(paired_margins) > 1:
        var = sum((m-mean_pm)**2 for m in paired_margins)/(len(paired_margins)-1)
        se = (var/len(paired_margins))**0.5
        t = mean_pm/se if se else float('inf')
    else:
        se, t = None, None
    # RNG side-effect check: does weed sequence diverge between variant-game and base-game
    # for the SAME seed (comparing the variant's own farm-weed sequence across the two
    # opponent conditions it's not directly comparable seat-to-seat; instead compare
    # variant's weed sequence when variant plays vs baseline, seed-matched, across swap
    # to detect any within-seed divergence caused by the intervention's board effects).
    weed_divergences = 0
    for r in rows:
        # compare variant's weed seq length/content sanity; true test: same seed, does
        # variant's own board-occupancy-driven weed draw differ from baseline's in the
        # mirrored (swap) condition where both should reflect the SAME seed's RNG stream
        pass
    return {
        "label": label, "n_games": len(rows), "n_seed_pairs": len(seed_margins),
        "variant_opportunity_days": v_opp, "variant_sold_days": v_sold,
        "variant_sell_rate": (v_sold/v_opp if v_opp else None),
        "variant_melon_units_sold": v_units, "variant_melon_revenue": v_rev,
        "base_opportunity_days": b_opp, "base_sold_days": b_sold,
        "base_sell_rate": (b_sold/b_opp if b_opp else None),
        "base_melon_units_sold": b_units, "base_melon_revenue": b_rev,
        "mean_seat_controlled_margin_variant_minus_base": mean_pm,
        "stderr": se, "t_stat": t,
        "paired_margins": paired_margins,
    }

def weed_rng_audit(rows):
    # For each seed, compare the weed sequence the SAME farm-seat experiences across
    # swap=False vs swap=True is not meaningful (different seats). Instead: compare,
    # for a fixed seed, the variant-farm's weed sequence to the baseline-farm's weed
    # sequence WITHIN the same game (they share the same per-day rng object, drawn in
    # player order -- see kaggriculture.py _end_of_day). If the intervention changes
    # board occupancy (empty tile count), the OTHER player's weed draw count that day
    # can change too, which is the actual RNG-coupling channel to check: does the
    # opponent's weed count in variant-games differ from a reference?
    # Practical proxy: total weeds absorbed by the non-intervened (baseline) seat,
    # summed per seed, compared across the two swap assignments (which put baseline
    # in each seat once) -- if intervention has no downstream RNG effect on the
    # opponent's board, this should be internally consistent seed-by-seed.
    out = []
    for r in rows:
        vw = sum(r["variant_weeds"]) if r["variant_weeds"] else 0
        bw = sum(r["base_weeds"]) if r["base_weeds"] else 0
        out.append({"seed": r["seed"], "swap": r["swap"], "variant_total_weeds": vw, "base_total_weeds": bw})
    return out

def main():
    out_path = sys.argv[1]
    variant = sys.argv[2]  # "v1" or "v2"
    seeds = [int(x) for x in sys.argv[3].split(",")]
    label = sys.argv[4] if len(sys.argv) > 4 else "matched"
    vpath = V1 if variant == "v1" else V2
    rows = run_pair(vpath, seeds)
    summary = summarize(rows, f"{variant}_{label}")
    weed_audit = weed_rng_audit(rows)
    result = {"summary": summary, "weed_audit": weed_audit}
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
