import json, collections, sys

path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/phase2_output.jsonl"
MIN_SUPPORT = 8

def rng_class(decision_type, day):
    if decision_type in ("hire", "melon"):
        return "RNG_INDEPENDENT"
    if decision_type == "chore":
        return "UNKNOWN"
    if decision_type in ("plant", "fertilize"):
        if isinstance(day, int) and day % 3 == 2:
            return "RNG_COUPLED"
        return "RNG_EXPOSED"
    return "UNKNOWN"

by_type = collections.defaultdict(list)
n_files = 0
with open(path) as f:
    for line in f:
        rec = json.loads(line)
        n_files += 1
        for dtype, evs in rec["events"].items():
            by_type[dtype].extend(evs)

print(f"files: {n_files}", file=sys.stderr)
for dtype, evs in by_type.items():
    print(f"{dtype}: {len(evs)} events (mine={sum(1 for e in evs if e['who']=='mine')}, opp={sum(1 for e in evs if e['who']=='opp')})", file=sys.stderr)

findings = []
for dtype, evs in by_type.items():
    buckets = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    seeds = collections.defaultdict(lambda: collections.defaultdict(set))
    games = collections.defaultdict(lambda: collections.defaultdict(set))
    teams = collections.defaultdict(lambda: collections.defaultdict(set))
    for e in evs:
        st = tuple(e["state"])
        who = e["who"]
        buckets[st][who][e["decision"]] += 1
        seeds[st][who].add(e["seed"])
        games[st][who].add(e["path"])
        teams[st][who].add(e["team"])
    for st, d in buckets.items():
        if "mine" not in d or "opp" not in d:
            continue
        mc, oc = d["mine"], d["opp"]
        nm, no = sum(mc.values()), sum(oc.values())
        if nm < MIN_SUPPORT or no < MIN_SUPPORT:
            continue
        mtop, mtopn = mc.most_common(1)[0]
        otop, otopn = oc.most_common(1)[0]
        mfrac, ofrac = mtopn/nm, otopn/no
        if mtop != otop and mfrac >= 0.4 and ofrac >= 0.4:
            day = st[0]
            findings.append({
                "decision_type": dtype, "state": list(st),
                "mine_action": mtop, "mine_frac": round(mfrac,2), "mine_n": nm,
                "opp_action": otop, "opp_frac": round(ofrac,2), "opp_n": no,
                "mine_seeds": len(seeds[st]["mine"]), "opp_seeds": len(seeds[st]["opp"]),
                "mine_games": len(games[st]["mine"]), "opp_games": len(games[st]["opp"]),
                "opp_teams": sorted(t for t in teams[st]["opp"] if t),
                "rng_classification": rng_class(dtype, day),
            })

findings.sort(key=lambda x: -(x["mine_n"] + x["opp_n"]))
print(json.dumps(findings, indent=2, ensure_ascii=False))
print(f"\n# total findings: {len(findings)}", file=sys.stderr)
from collections import Counter
print("# by rng class:", Counter(f["rng_classification"] for f in findings), file=sys.stderr)
print("# by decision type:", Counter(f["decision_type"] for f in findings), file=sys.stderr)
