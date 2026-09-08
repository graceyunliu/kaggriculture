import json, os, random, glob, sys

ROOT = os.path.expanduser("~/mnt/Kaggriculture")
REPLAY_DIRS = [
    "Replays/Auto/mine", "Replays/Auto/leaderboard-binghua",
    "Replays/Auto/leaderboard-get_some_fries", "Replays/Auto/leaderboard-Matthew_Huang",
    "Replays/Auto/leaderboard-Andrey_Tikhomirov", "Replays/Auto/leaderboard-Mengfei_Li",
    "Replays/Auto/leaderboard-OceanMix", "Replays/Auto/leaderboard-Jesse_Bullard",
    "Replays/Auto/leaderboard-SpaTaro", "Replays/Auto/leaderboard-kwa",
    "Replays/Auto/leaderboard-3정훈", "Replays/Auto/leaderboard-ymg_aq",
    "Replays/Auto/leaderboard-MtN", "Replays/Auto/leaderboard-Otter_Vibe",
    "Replays/Leader Replays/Subin An",
]
MY_NAME_HINTS = {"graceyunliu", "grace", "Grace"}

# --- reconstructed engine rules (see vendor/kaggle_environments_engine/kaggriculture.py) ---
def _fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def hire_cost(n_already_today, mult):
    # kaggriculture.py:674-675  _hire_cost(n, mult) = mult * fib(n)
    return mult * _fib(n_already_today)

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
    cfg = d.get("configuration", {})
    hire_mult = int(cfg.get("farmHandCostMult", 1) or 1)

    my_idx = None
    for i, nm in enumerate(team_names):
        if nm in MY_NAME_HINTS:
            my_idx = i

    events = {"hire_opportunity": [], "melon_opportunity": []}
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
            sig = state_sig(day, farm)

            # --- HIRE opportunity reconstruction ---
            # Eligibility gate per kaggriculture.py:678-683 (_do_hire): only gate is
            # farm["money"] >= _hire_cost(farm["hires_today"], mult). No capacity/board gate exists.
            money = farm.get("money", 0)
            hires_today = farm.get("hires_today", 0)
            cost0 = hire_cost(hires_today, hire_mult)
            hired_this_step = len(market_events(market_list, "HIRE")) > 0
            if money >= cost0:
                tag = "OBSERVED_ACTION" if hired_this_step else "OBSERVED_ABSTENTION"
            else:
                tag = None  # no opportunity existed; not a finding row
            if tag is not None:
                events["hire_opportunity"].append({
                    "state": sig, "who": who, "team": team_names[pid],
                    "decision": tag, "cost": cost0, "money": money,
                    "seed": seed, "path": path,
                })

            # --- MELON admission opportunity reconstruction ---
            # Eligibility gate per kaggriculture.py:627-635 (_commit_unit SELL): only gate is
            # private["shed"].get(item, 0) > 0. Price is deterministic (market_price(), no RNG).
            melon_stock = shed.get("MELON", 0) if isinstance(shed, dict) else 0
            if melon_stock and melon_stock > 0:
                sold_this_step = len(market_events(market_list, "SELL")) and any(
                    m for m in market_events(market_list, "SELL") if len(m) > 1 and m[1] == "MELON")
                tag = "OBSERVED_ACTION" if sold_this_step else "OBSERVED_ABSTENTION"
                events["melon_opportunity"].append({
                    "state": sig, "who": who, "team": team_names[pid],
                    "decision": tag, "stock": melon_stock,
                    "seed": seed, "path": path,
                })
    return events

def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/phase3_output.jsonl"
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
