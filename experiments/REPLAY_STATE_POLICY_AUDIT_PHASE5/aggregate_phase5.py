import json, sys, math
from collections import defaultdict

def wilson(k, n, z=1.96):
    if n == 0:
        return (None, None, None)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (round(p, 4), round(center - half, 4), round(center + half, 4))

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/phase5c_mined.jsonl"
    lines = [json.loads(l) for l in open(path)]

    mine_reach2 = 0
    opp_reach2 = 0
    n_games = 0
    tier1_mine_flat = []
    tier1_opp_flat = []

    for rec in lines:
        rows = rec["events"]["expansion_day_events"]
        by = defaultdict(list)
        for r in rows:
            by[r["who"]].append(r)
        m = by.get("mine", [])
        o = by.get("opp", [])
        if not m and not o:
            continue
        n_games += 1
        m_max_tier = max([r["land_pre"] for r in m], default=1)
        o_max_tier = max([r["land_pre"] for r in o], default=1)
        if m_max_tier >= 2:
            mine_reach2 += 1
        if o_max_tier >= 2:
            opp_reach2 += 1
        for r in m:
            if r["land_pre"] == 1:
                tier1_mine_flat.append(1 if r["decision"] == "OBSERVED_ACTION" else 0)
        for r in o:
            if r["land_pre"] == 1:
                tier1_opp_flat.append(1 if r["decision"] == "OBSERVED_ACTION" else 0)

    p1, lo1, hi1 = wilson(mine_reach2, n_games)
    p2, lo2, hi2 = wilson(opp_reach2, n_games)
    p_pool = (mine_reach2 + opp_reach2) / (2 * n_games)
    se = math.sqrt(p_pool * (1 - p_pool) * (2 / n_games))
    z = (p2 - p1) / se if se > 0 else None

    out = {
        "n_games": n_games,
        "mine_reach_land2plus": {"k": mine_reach2, "n": n_games, "p": p1, "wilson95": [lo1, hi1]},
        "opp_reach_land2plus": {"k": opp_reach2, "n": n_games, "p": p2, "wilson95": [lo2, hi2]},
        "two_proportion_z": round(z, 3) if z is not None else None,
        "tier1_opportunity_conditioned_action_rate": {
            "mine": {"k": sum(tier1_mine_flat), "n": len(tier1_mine_flat)},
            "opp": {"k": sum(tier1_opp_flat), "n": len(tier1_opp_flat)},
        },
    }
    print(json.dumps(out, indent=2))
    json.dump(out, open("/tmp/phase5_summary.json", "w"), indent=2)

if __name__ == "__main__":
    main()
