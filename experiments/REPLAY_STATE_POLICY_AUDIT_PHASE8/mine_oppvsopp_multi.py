import json, glob, os, random
ROOT = os.path.expanduser("~/mnt/Kaggriculture")
DIRS = glob.glob(os.path.join(ROOT, "Replays/Auto/leaderboard-*"))
files = []
for d in DIRS:
    files += glob.glob(os.path.join(d, "*.json"))
random.Random(11).shuffle(files)
files = files[:200]

rows = []
for f in files:
    try:
        d = json.load(open(f))
    except Exception:
        continue
    steps = d.get("steps", [])
    if not steps:
        continue
    info = d.get("info", {})
    team_names = info.get("TeamNames") or [None, None]
    if "graceyunliu" in team_names:
        continue
    for pid in range(2):
        max_land = 1
        max_hands = 0
        first_hire_day = None
        total_hires = 0
        weed_escapes_total = 0
        final_money = None
        n_days_shed_full = 0
        for pair in steps:
            obs = pair[0]["observation"]
            day = obs.get("day")
            farm = obs["farms"][pid]
            act = pair[pid]["action"]
            market_list = act.get("market", []) if isinstance(act, dict) else []
            land = len(farm.get("unlocked_quadrants", ["NW"]))
            max_land = max(max_land, land)
            hands = len(farm.get("hands", []))
            max_hands = max(max_hands, hands)
            hires_this = sum(1 for m in (market_list or []) if m and m[0] == "HIRE")
            if hires_this and first_hire_day is None:
                first_hire_day = day
            total_hires += hires_this
            final_money = farm.get("money")
        if final_money is not None:
            rows.append({"path": os.path.relpath(f, ROOT), "team": team_names[pid],
                         "max_land": max_land, "max_hands": max_hands,
                         "first_hire_day": first_hire_day, "total_hires": total_hires,
                         "final_money": final_money})

json.dump(rows, open("/tmp/p5work/oppvsopp_multi.json", "w"))
print("n_rows", len(rows))
