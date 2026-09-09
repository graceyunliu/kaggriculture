import json, os, random, glob, sys
from collections import defaultdict

ROOT = os.path.expanduser("~/mnt/Kaggriculture")
REPLAY_DIRS = ["Replays/Auto/mine"]
MY_NAME_HINTS = {"graceyunliu", "grace", "Grace"}
LAND_PRICES = [1000, 2000, 4000]

def process_file(path):
    try:
        d = json.load(open(path))
    except Exception:
        return None
    info = d.get("info", {})
    team_names = info.get("TeamNames") or [None, None]
    seed = info.get("seed")
    steps = d.get("steps", [])
    if not steps or len(steps) < 2:
        return None
    my_idx = None
    for i, nm in enumerate(team_names):
        if nm in MY_NAME_HINTS:
            my_idx = i
    if my_idx is None:
        return None

    by_day = defaultdict(list)
    for idx, pair in enumerate(steps):
        day = pair[0]["observation"].get("day")
        by_day[day].append(idx)
    days_sorted = sorted(by_day.keys())

    out = {"expansion_day_events": []}
    for pid in range(2):
        who = "mine" if pid == my_idx else "opp"
        for di, day in enumerate(days_sorted):
            first_idx = by_day[day][0]
            if first_idx == 0:
                pre_money = steps[0][pid]["observation"]["farms"][pid].get("money", 0)
                pre_land = len(steps[0][pid]["observation"]["farms"][pid].get("unlocked_quadrants", ["NW"]))
            else:
                pre_obs = steps[first_idx - 1][pid]["observation"]["farms"][pid]
                pre_money = pre_obs.get("money", 0)
                pre_land = len(pre_obs.get("unlocked_quadrants", ["NW"]))
            n_extra = pre_land - 1
            if n_extra >= len(LAND_PRICES):
                continue
            cost = LAND_PRICES[n_extra]
            # end of day D: state at end of last step of day D (post-state of that step)
            last_idx = by_day[day][-1]
            land_end = len(steps[last_idx][pid]["observation"]["farms"][pid].get("unlocked_quadrants", ["NW"]))
            acted = land_end > pre_land
            if pre_money >= cost:
                tag = "OBSERVED_ACTION" if acted else "OBSERVED_ABSTENTION"
            else:
                tag = None
            if tag is not None:
                out["expansion_day_events"].append({
                    "day": day, "who": who, "team": team_names[pid], "decision": tag,
                    "cost": cost, "money_pre": pre_money, "land_pre": pre_land, "seed": seed,
                })
    return out

def main():
    out_path = sys.argv[1]
    limit = int(sys.argv[2])
    n_files = 0
    with open(out_path, "w") as out:
        full = os.path.join(ROOT, REPLAY_DIRS[0])
        files = sorted(glob.glob(os.path.join(full, "*.json")))
        files = [f for f in files if not f.endswith(".DS_Store")]
        random.Random(42).shuffle(files)
        files = files[:limit]
        for f in files:
            res = process_file(f)
            n_files += 1
            if res is None:
                continue
            out.write(json.dumps({"path": os.path.relpath(f, ROOT), "events": res}) + "\n")
    print("files_processed", n_files)

if __name__ == "__main__":
    main()
