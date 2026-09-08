import json, collections, sys

path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/mining_output.jsonl"

state_crop = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
state_seeds = collections.defaultdict(lambda: collections.defaultdict(set))
state_teams = collections.defaultdict(lambda: collections.defaultdict(set))
state_games = collections.defaultdict(lambda: collections.defaultdict(set))
state_hires = collections.defaultdict(lambda: collections.defaultdict(list))
state_wheatfrac = collections.defaultdict(lambda: collections.defaultdict(list))

n_games = 0
with open(path) as f:
    for line in f:
        g = json.loads(line)
        n_games += 1
        seed = g.get("seed")
        for r in g["records"]:
            if r["who"] not in ("mine", "opp"):
                continue
            st = tuple(r["state"])
            who = r["who"]
            state_crop[st][who][r["dom_crop"]] += 1
            state_seeds[st][who].add(seed)
            state_teams[st][who].add(r["team"])
            state_games[st][who].add(r["path"])
            state_hires[st][who].append(r["hires_today"])
            state_wheatfrac[st][who].append(r["wheat_frac"])

print(f"total games processed: {n_games}", file=sys.stderr)

MIN_SUPPORT = 8
findings = []
for st in state_crop:
    if "mine" not in state_crop[st] or "opp" not in state_crop[st]:
        continue
    mine_c = state_crop[st]["mine"]
    opp_c = state_crop[st]["opp"]
    n_mine = sum(mine_c.values())
    n_opp = sum(opp_c.values())
    if n_mine < MIN_SUPPORT or n_opp < MIN_SUPPORT:
        continue
    mine_top, mine_top_n = mine_c.most_common(1)[0]
    opp_top, opp_top_n = opp_c.most_common(1)[0]
    mine_frac = mine_top_n / n_mine
    opp_frac = opp_top_n / n_opp
    if mine_top != opp_top and mine_frac >= 0.4 and opp_frac >= 0.4:
        day_bucket = st[0]
        days_in_bucket = [day_bucket * 3 + k for k in range(3)]
        exposed = any((d % 3 == 2) or (d % 3 == 0) for d in days_in_bucket)
        findings.append({
            "state": list(st),
            "mine_action": mine_top, "mine_frac": round(mine_frac, 2), "mine_n": n_mine,
            "opp_action": opp_top, "opp_frac": round(opp_frac, 2), "opp_n": n_opp,
            "mine_seeds": len(state_seeds[st]["mine"]), "opp_seeds": len(state_seeds[st]["opp"]),
            "mine_games": len(state_games[st]["mine"]), "opp_games": len(state_games[st]["opp"]),
            "opp_teams": sorted(state_teams[st]["opp"]),
            "rng_exposed_daybucket": exposed,
        })

findings.sort(key=lambda x: -(x["mine_n"] + x["opp_n"]))
print(json.dumps(findings, indent=2, ensure_ascii=False))
print(f"\n# total candidate divergences: {len(findings)}", file=sys.stderr)

all_mine_wf = [v for st in state_wheatfrac for v in state_wheatfrac[st].get("mine", [])]
all_opp_wf = [v for st in state_wheatfrac for v in state_wheatfrac[st].get("opp", [])]
all_mine_hr = [v for st in state_hires for v in state_hires[st].get("mine", [])]
all_opp_hr = [v for st in state_hires for v in state_hires[st].get("opp", [])]
def avg(l): return sum(l)/len(l) if l else None
print(f"# GLOBAL wheat_frac mine={avg(all_mine_wf):.3f} n={len(all_mine_wf)} opp={avg(all_opp_wf):.3f} n={len(all_opp_wf)}", file=sys.stderr)
print(f"# GLOBAL hires_today mine={avg(all_mine_hr):.3f} n={len(all_mine_hr)} opp={avg(all_opp_hr):.3f} n={len(all_opp_hr)}", file=sys.stderr)
