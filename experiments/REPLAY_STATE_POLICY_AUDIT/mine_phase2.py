import json, os, random, glob, sys

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

def flat_tokens(lst):
    # farmer action arrays and per-hand action arrays are lists possibly mixing
    # move tokens, verb tokens, and arg tokens; scan sequentially for pairs.
    out = []
    i = 0
    while i < len(lst):
        out.append(lst[i])
        i += 1
    return out

def scan_plant_events(tok_list):
    crops = []
    i = 0
    while i < len(tok_list) - 1:
        if tok_list[i] == "PLANT":
            crops.append(tok_list[i+1])
            i += 2
        else:
            i += 1
    return crops

def has_verb(tok_list, verb):
    return verb in tok_list

def market_events(market_list, kind):
    out = []
    for m in market_list or []:
        if m and m[0] == kind:
            out.append(m)
    return out

def state_sig(day, farm):
    money = farm.get("money", 0)
    return [day, cash_bucket(money), land_tier(farm), labor_bucket(len(farm.get("hands", [])))]

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

    events = {"hire": [], "plant": [], "fertilize": [], "melon": [], "chore": []}
    for step_idx, pair in enumerate(steps):
        obs = pair[0]["observation"]
        day = obs.get("day")
        farms = obs.get("farms", [])
        for pid in range(len(farms)):
            farm = farms[pid]
            act = pair[pid]["action"]
            private = pair[pid]["observation"].get("private", {})
            shed = private.get("shed", {}) if isinstance(private, dict) else {}
            farmer_toks = act.get("farmer", []) or []
            market_list = act.get("market", []) or []
            hand_lists = act.get("hands", []) or []
            who = "mine" if (my_idx is not None and pid == my_idx) else ("opp" if my_idx is not None else "unk")
            if who == "unk":
                continue
            sig = state_sig(day, farm)

            hires = market_events(market_list, "HIRE")
            if hires:
                events["hire"].append({"state": sig, "who": who, "team": team_names[pid],
                                         "decision": "HIRE", "n": len(hires), "seed": seed, "path": path})

            plant_crops = scan_plant_events(farmer_toks)
            for hl in hand_lists:
                if hl:
                    plant_crops.extend(scan_plant_events(hl))
            for crop in plant_crops:
                events["plant"].append({"state": sig, "who": who, "team": team_names[pid],
                                          "decision": crop, "seed": seed, "path": path})

            fert_farmer = has_verb(farmer_toks, "FERTILIZE")
            fert_hands = any(hl and has_verb(hl, "FERTILIZE") for hl in hand_lists)
            fert_applied = fert_farmer or fert_hands
            fert_stock = shed.get("FERTILIZER", 0) if isinstance(shed, dict) else 0
            if fert_stock and fert_stock > 0:
                events["fertilize"].append({"state": sig, "who": who, "team": team_names[pid],
                                              "decision": "APPLY" if fert_applied else "HOLD",
                                              "stock": fert_stock, "seed": seed, "path": path})

            melon_sells = [m for m in market_events(market_list, "SELL") if len(m) > 1 and m[1] == "MELON"]
            melon_stock = shed.get("MELON", 0) if isinstance(shed, dict) else 0
            if melon_stock and melon_stock > 0:
                events["melon"].append({"state": sig, "who": who, "team": team_names[pid],
                                          "decision": "SELL" if melon_sells else "HOLD",
                                          "stock": melon_stock, "seed": seed, "path": path})

            n_hands = len(farm.get("hands", []))
            if n_hands > 0:
                idle = sum(1 for hl in hand_lists if not hl)
                assigned = n_hands - idle if n_hands >= len(hand_lists) else max(0, len(hand_lists) - idle)
                events["chore"].append({"state": sig, "who": who, "team": team_names[pid],
                                          "decision": "IDLE_MAJORITY" if idle >= max(1, n_hands // 2) else "ASSIGNED_MAJORITY",
                                          "n_hands": n_hands, "idle": idle, "seed": seed, "path": path})
    return events

def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/phase2_output.jsonl"
    limit_per_dir = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    start_dir_idx = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    end_dir_idx = int(sys.argv[4]) if len(sys.argv) > 4 else len(REPLAY_DIRS)
    mode = sys.argv[5] if len(sys.argv) > 5 else "w"
    n_files = 0
    with open(out_path, mode) as out:
        for d in REPLAY_DIRS[start_dir_idx:end_dir_idx]:
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
                out.write(json.dumps({"path": os.path.relpath(f, ROOT), "events": res}) + "\n")
    print("files_processed", n_files, "dirs", REPLAY_DIRS[start_dir_idx:end_dir_idx])

if __name__ == "__main__":
    main()
