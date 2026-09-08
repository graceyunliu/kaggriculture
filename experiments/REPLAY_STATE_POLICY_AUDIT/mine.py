import json, os, random, collections, glob, sys

ROOT = os.path.expanduser("~/mnt/Kaggriculture")
REPLAY_DIRS = [
    "Replays/Auto/mine",
    "Replays/Auto/leaderboard-binghua",
    "Replays/Auto/leaderboard-get_some_fries",
    "Replays/Auto/leaderboard-Matthew_Huang",
    "Replays/Auto/leaderboard-Andrey_Tikhomirov",
    "Replays/Auto/leaderboard-Mengfei_Li",
    "Replays/Auto/leaderboard-OceanMix",
    "Replays/Auto/leaderboard-Jesse_Bullard",
    "Replays/Auto/leaderboard-SpaTaro",
    "Replays/Auto/leaderboard-kwa",
    "Replays/Auto/leaderboard-3정훈",
    "Replays/Auto/leaderboard-ymg_aq",
    "Replays/Auto/leaderboard-MtN",
    "Replays/Auto/leaderboard-Otter_Vibe",
    "Replays/Leader Replays/Subin An",
]

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

def day_bucket(day):
    return day // 3

def crop_counts(farm):
    counts = collections.Counter()
    for row in farm.get("tiles", []):
        for t in row:
            if isinstance(t, dict) and t.get("kind") == "PLANT":
                counts[t.get("crop")] += 1
    return counts

def dominant_crop(counts):
    if not counts:
        return "NONE"
    return counts.most_common(1)[0][0]

def process_file(path, sample_every_hours=24):
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

    records = []
    for step_idx in range(0, len(steps), sample_every_hours):
        pair = steps[step_idx]
        obs = pair[0]["observation"]
        day = obs.get("day")
        farms = obs.get("farms", [])
        for pid in range(len(farms)):
            farm = farms[pid]
            money = farm.get("money", 0)
            hands = farm.get("hands", [])
            hires_today = farm.get("hires_today", 0)
            counts = crop_counts(farm)
            dom = dominant_crop(counts)
            total_plants = sum(counts.values())
            wheat_frac = (counts.get("WHEAT", 0) / total_plants) if total_plants else 0.0
            state_sig = [day_bucket(day) if isinstance(day, int) else -1,
                         cash_bucket(money), land_tier(farm), labor_bucket(len(hands))]
            who = "mine" if (my_idx is not None and pid == my_idx) else ("opp" if my_idx is not None else "unk")
            rec = {"state": state_sig, "who": who, "team": team_names[pid], "dom_crop": dom,
                   "wheat_frac": round(wheat_frac, 3), "hires_today": hires_today, "money": money,
                   "day": day, "seed": seed, "path": os.path.relpath(path, ROOT)}
            records.append(rec)
    return {"seed": seed, "teams": team_names, "records": records}

def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/mining_output.jsonl"
    limit_per_dir = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    n_files = 0
    n_games_with_me = 0
    with open(out_path, "w") as out:
        for d in REPLAY_DIRS:
            full = os.path.join(ROOT, d)
            if not os.path.isdir(full):
                continue
            files = sorted(glob.glob(os.path.join(full, "*.json")))
            files = [f for f in files if not f.endswith(".DS_Store")]
            random.Random(42).shuffle(files)
            files = files[:limit_per_dir]
            for f in files:
                res = process_file(f)
                n_files += 1
                if res is None:
                    continue
                if any(t in MY_NAME_HINTS for t in res["teams"]):
                    n_games_with_me += 1
                out.write(json.dumps(res) + "\n")
    print("files_processed", n_files, "games_with_me", n_games_with_me, "out", out_path)

if __name__ == "__main__":
    main()
