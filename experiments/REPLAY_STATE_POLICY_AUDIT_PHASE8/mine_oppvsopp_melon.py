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
        continue  # exclude any accidental mine-games
    for pid in range(2):
        melon_opp = 0
        melon_act = 0
        final_money = None
        for pair in steps:
            obs = pair[0]["observation"]
            farm = obs["farms"][pid]
            private = pair[pid]["observation"].get("private", {})
            shed = private.get("shed", {}) if isinstance(private, dict) else {}
            act = pair[pid]["action"]
            market_list = act.get("market", []) if isinstance(act, dict) else []
            melon_stock = shed.get("MELON", 0) if isinstance(shed, dict) else 0
            if melon_stock > 0:
                melon_opp += 1
                sold = any(m for m in (market_list or []) if m and m[0] == "SELL" and len(m) > 1 and m[1] == "MELON")
                if sold:
                    melon_act += 1
            final_money = farm.get("money")
        if melon_opp >= 3:
            rows.append({"path": os.path.relpath(f, ROOT), "team": team_names[pid],
                         "melon_opp": melon_opp, "melon_act": melon_act,
                         "melon_rate": melon_act / melon_opp, "final_money": final_money})

json.dump(rows, open("/tmp/p5work/oppvsopp_melon.json", "w"))
print("n_rows", len(rows), "n_files", len(files))
