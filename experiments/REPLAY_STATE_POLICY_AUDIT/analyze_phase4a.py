import json, math, random, collections, sys

def wilson_ci(x, n, z=1.96):
    if n == 0:
        return (None, None)
    p = x / n
    denom = 1 + z*z/n
    center = (p + z*z/(2*n)) / denom
    half = (z * math.sqrt((p*(1-p) + z*z/(4*n)) / n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))

def log_choose(n, k):
    if k < 0 or k > n:
        return float("-inf")
    return math.lgamma(n+1) - math.lgamma(k+1) - math.lgamma(n-k+1)

def fisher_exact_two_sided(a, b, c, d):
    # table: [[a,b],[c,d]] ; row sums R1=a+b, R2=c+d ; col sums C1=a+c, C2=b+d ; N=a+b+c+d
    R1, R2 = a+b, c+d
    C1, N = a+c, a+b+c+d
    lo = max(0, C1 - R2)
    hi = min(R1, C1)
    log_denom = log_choose(N, C1)
    def log_p(x):
        return log_choose(R1, x) + log_choose(R2, C1-x) - log_denom
    obs_log_p = log_p(a)
    # sum probabilities <= observed (with small tolerance) over all x in [lo,hi]
    total_log_ps = [log_p(x) for x in range(lo, hi+1)]
    mx = max(total_log_ps)
    # two-sided: sum p(x) for all x with p(x) <= p(a) * (1+1e-7)
    thresh = obs_log_p + math.log(1 + 1e-7)
    # numerically stable sum via log-sum-exp restricted to qualifying terms
    qualifying = [lp for lp in total_log_ps if lp <= thresh]
    if not qualifying:
        return math.exp(obs_log_p)
    m = max(qualifying)
    s = sum(math.exp(lp - m) for lp in qualifying)
    logp = m + math.log(s)
    return min(1.0, math.exp(logp))

def rate_ratio_ci(x1, n1, x2, n2, z=1.96):
    # log rate ratio CI (x1/n1)/(x2/n2), delta method
    p1, p2 = x1/n1, x2/n2
    if x1 == 0 or x2 == 0:
        return (p1/p2 if p2 else None, None, None)
    logrr = math.log(p1/p2)
    se = math.sqrt((1-p1)/x1 + (1-p2)/x2) if p1 < 1 and p2 < 1 else math.sqrt(1/x1 + 1/x2)
    lo, hi = math.exp(logrr - z*se), math.exp(logrr + z*se)
    return (p1/p2, lo, hi)

def odds_ratio_ci(a, b, c, d, z=1.96):
    # a=mine action, b=mine abstain, c=opp action, d=opp abstain
    if 0 in (a, b, c, d):
        a2, b2, c2, d2 = a+0.5, b+0.5, c+0.5, d+0.5
    else:
        a2, b2, c2, d2 = a, b, c, d
    orr = (a2*d2) / (b2*c2)
    se = math.sqrt(1/a2 + 1/b2 + 1/c2 + 1/d2)
    logor = math.log(orr)
    return (orr, math.exp(logor - z*se), math.exp(logor + z*se))

def main():
    mine_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/phase4a_mine.jsonl"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "/tmp/phase4a_stats.json"

    per_replay = []  # (path, seed, who, n_action, n_abstain, opp_team)
    total = collections.Counter()
    opp_team_stats = collections.defaultdict(lambda: collections.Counter())

    with open(mine_path) as f:
        for line in f:
            r = json.loads(line)
            evs = r.get("events", [])
            if not evs:
                continue
            path = r["path"]; seed = r.get("seed")
            by_who = collections.defaultdict(collections.Counter)
            opp_team = None
            for e in evs:
                by_who[e["who"]][e["decision"]] += 1
                total[(e["who"], e["decision"])] += 1
                if e["who"] == "opp":
                    opp_team = e["team"]
                    opp_team_stats[e["team"]][e["decision"]] += 1
            per_replay.append({
                "path": path, "seed": seed, "opp_team": opp_team,
                "mine_action": by_who["mine"]["OBSERVED_ACTION"],
                "mine_abstain": by_who["mine"]["OBSERVED_ABSTENTION"],
                "opp_action": by_who["opp"]["OBSERVED_ACTION"],
                "opp_abstain": by_who["opp"]["OBSERVED_ABSTENTION"],
            })

    mine_action = total[("mine", "OBSERVED_ACTION")]
    mine_abstain = total[("mine", "OBSERVED_ABSTENTION")]
    opp_action = total[("opp", "OBSERVED_ACTION")]
    opp_abstain = total[("opp", "OBSERVED_ABSTENTION")]
    mine_n = mine_action + mine_abstain
    opp_n = opp_action + opp_abstain

    mine_rate = mine_action / mine_n if mine_n else None
    opp_rate = opp_action / opp_n if opp_n else None
    mine_ci = wilson_ci(mine_action, mine_n)
    opp_ci = wilson_ci(opp_action, opp_n)

    p_fisher = fisher_exact_two_sided(mine_action, mine_abstain, opp_action, opp_abstain)
    rr, rr_lo, rr_hi = rate_ratio_ci(opp_action, opp_n, mine_action, mine_n)  # opp/mine ratio
    orr, orr_lo, orr_hi = odds_ratio_ci(mine_action, mine_abstain, opp_action, opp_abstain)

    # cluster bootstrap by replay (each replay = one seed/opponent-identity cluster)
    random.seed(12345)
    B = 2000
    boot_rr = []
    replays = per_replay
    n_replays = len(replays)
    for _ in range(B):
        sample = [replays[random.randrange(n_replays)] for _ in range(n_replays)]
        ma = sum(r["mine_action"] for r in sample)
        mb = sum(r["mine_abstain"] for r in sample)
        oa = sum(r["opp_action"] for r in sample)
        ob = sum(r["opp_abstain"] for r in sample)
        mn, on = ma+mb, oa+ob
        if mn == 0 or on == 0 or ma == 0:
            continue
        boot_rr.append((oa/on) / (ma/mn))
    boot_rr.sort()
    def pct(lst, p):
        if not lst:
            return None
        idx = min(len(lst)-1, max(0, int(round(p * (len(lst)-1)))))
        return lst[idx]
    boot_ci = (pct(boot_rr, 0.025), pct(boot_rr, 0.975))

    # per-opponent-identity breakdown (opponents with enough opportunities)
    per_opp = []
    for team, c in opp_team_stats.items():
        a, ab = c["OBSERVED_ACTION"], c["OBSERVED_ABSTENTION"]
        n = a + ab
        if n >= 30:
            per_opp.append({"team": team, "action": a, "abstain": ab, "n": n, "rate": round(a/n, 4)})
    per_opp.sort(key=lambda x: -x["n"])

    result = {
        "n_replays_with_grace": n_replays,
        "distinct_opponent_identities": len(opp_team_stats),
        "mine_action": mine_action, "mine_abstain": mine_abstain, "mine_n": mine_n, "mine_rate": mine_rate,
        "mine_wilson_ci95": mine_ci,
        "opp_action": opp_action, "opp_abstain": opp_abstain, "opp_n": opp_n, "opp_rate": opp_rate,
        "opp_wilson_ci95": opp_ci,
        "fisher_exact_two_sided_p": p_fisher,
        "rate_ratio_opp_over_mine": rr, "rate_ratio_ci95": (rr_lo, rr_hi),
        "odds_ratio_mine_vs_opp": orr, "odds_ratio_ci95": (orr_lo, orr_hi),
        "cluster_bootstrap_B": B,
        "cluster_bootstrap_valid_draws": len(boot_rr),
        "cluster_bootstrap_rate_ratio_median": pct(boot_rr, 0.5),
        "cluster_bootstrap_rate_ratio_ci95": boot_ci,
        "per_opponent_identity_n_ge_30": per_opp,
    }
    json.dump(result, open(out_path, "w"), indent=2)
    print(json.dumps(result, indent=2)[:4000])

if __name__ == "__main__":
    main()
