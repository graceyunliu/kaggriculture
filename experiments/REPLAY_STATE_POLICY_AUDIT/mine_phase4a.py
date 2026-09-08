import json, os, random, glob, sys

ROOT = os.path.expanduser("~/mnt/Kaggriculture")
OPP_DIRS = [
    "Replays/Auto/leaderboard-binghua", "Replays/Auto/leaderboard-get_some_fries",
    "Replays/Auto/leaderboard-Matthew_Huang", "Replays/Auto/leaderboard-Andrey_Tikhomirov",
    "Replays/Auto/leaderboard-Mengfei_Li", "Replays/Auto/leaderboard-OceanMix",
    "Replays/Auto/leaderboard-Jesse_Bullard", "Replays/Auto/leaderboard-SpaTaro",
    "Replays/Auto/leaderboard-kwa", "Replays/Auto/leaderboard-3정훈",
    "Replays/Auto/leaderboard-ymg_aq", "Replays/Auto/leaderboard-MtN",
    "Replays/Auto/leaderboard-Otter_Vibe", "Replays/Leader Replays/Subin An",
]
MINE_DIR = "Replays/Auto/mine"
MY_NAME_HINTS = {"graceyunliu", "grace", "Grace"}

def cash_bucket(m):
    if m < 500: return "C0_<500"
    if m < 2000: return "C1_500-2k"
    if m < 5000: return "C2_2k-5k"
    if m < 15000: return "C3_5k-15k"
    if m < 40000: return "C4_15k-40k"
    return "C5_40k+"

def land_tier(farm):
    return len(farm.get("unlocked_quadrants", ["NW"]))

def labor_bucket(n):
    if n <= 4: return "L0_<=4"
    if n <= 8: return "L1_5-8"
    if n <= 14: return "L2_9-14"
    return "L3_15+"

def state_sig(day, farm):
    return [day, cash_bucket(farm.get("money", 0)), land_tier(farm), labor_bucket(len(farm.get("hands", [])))]

def market_events(market_list, kind):
    return [m for m in (market_list or []) if m and m[0] == kind]

def process_file(path):
    try:
        d = json.load(open(path))
    except Exception:
        return None
    info = d.get("info", {})
    team_names = info.get("TeamNames") or [None, None]
    seed = info.get("seed")
    steps = d.get("steps", [])
    if not steps:
        return None
    my_idx = None
    for i, nm in enumerate(team_names):
        if nm in MY_NAME_HINTS:
            my_idx = i

    evs = []
    for pair in steps:
        obs = pair[0]["observation"]
        day = obs.get("day")
        farms = obs.get("farms", [])
        for pid in range(len(farms)):
            farm = farms[pid]
            act = pair[pid]["action"]
            private = pair[pid]["observation"].get("private", {})
            shed = private.get("shed", {}) if isinstance(private, dict) else {}
            market_list = act.get("market", []) or []
            who = "mine" if (my_idx is not None and pid == my_idx) else ("opp" if my_idx is not None else "unk")
            if who == "unk":
                continue
            melon_stock = shed.get("MELON", 0) if isinstance(shed, dict) else 0
            if melon_stock and melon_stock > 0:
                sold = any(m for m in market_events(market_list, "SELL") if len(m) > 1 and m[1] == "MELON")
                evs.append({
                    "state": state_sig(day, farm), "who": who, "team": team_names[pid],
                    "decision": "OBSERVED_ACTION" if sold else "OBSERVED_ABSTENTION",
                    "stock": melon_stock, "seed": seed,
                })
    if not evs:
        return {"path": os.path.relpath(path, ROOT), "seed": seed, "teams": team_names, "n_events": 0}
    return {"path": os.path.relpath(path, ROOT), "seed": seed, "teams": team_names, "events": evs}

def main():
    out_path = sys.argv[1]
    pool = sys.argv[2]  # "opp" or "mine"
    limit = int(sys.argv[3])
    start = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    mode = sys.argv[5] if len(sys.argv) > 5 else "a"
    files = []
    if pool == "opp":
        for d in OPP_DIRS:
            full = os.path.join(ROOT, d)
            if os.path.isdir(full):
                files.extend(sorted(glob.glob(os.path.join(full, "*.json"))))
        files = [f for f in files if not f.endswith(".DS_Store")]
    else:
        full = os.path.join(ROOT, MINE_DIR)
        files = sorted(glob.glob(os.path.join(full, "*.json")))
        files = [f for f in files if not f.endswith(".DS_Store")]
        random.Random(42).shuffle(files)
    chunk = files[start:start+limit]
    n = 0
    with open(out_path, mode) as out:
        for f in chunk:
            res = process_file(f)
            n += 1
            if res is None:
                continue
            out.write(json.dumps(res) + "\n")
    print(f"pool={pool} processed={n} of total_available={len(files)} range=[{start}:{start+limit}]")

if __name__ == "__main__":
    main()
