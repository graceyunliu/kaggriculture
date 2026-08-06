"""Measure land utilization: for each day, what fraction of a player's
UNLOCKED (owned) tiles are actually under crop/animal vs sitting empty/weed."""
import importlib.util, sys, json
from collections import defaultdict

def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent

def classify(tile):
    if tile is None:
        return "EMPTY"
    if tile == "LOCKED":
        return "LOCKED"
    if isinstance(tile, dict):
        kind = tile.get("kind")
        if kind == "PLANT":
            return "PLANT"
        if kind == "WEED":
            return "WEED"
        if kind in ("PASTURE", "COOP"):
            return "ANIMAL_STRUCT"
    return "OTHER"

def util_from_steps_iter(step_iter, tpd, player_index_fn):
    """step_iter yields step objects (list of per-player dicts w/ 'observation').
    player_index_fn(step) -> farms index to look at."""
    day_counts = {}  # day -> Counter of tile classes among UNLOCKED tiles
    for step in step_iter:
        obs0 = step[0]["observation"] if isinstance(step[0], dict) else step[0].observation
        day = obs0.get("day", 0) if isinstance(obs0, dict) else obs0["day"]
        farms = obs0.get("farms") if isinstance(obs0, dict) else obs0["farms"]
        if not farms:
            continue
        pidx = player_index_fn()
        farm = farms[pidx]
        counts = defaultdict(int)
        total_unlocked = 0
        for row in farm["tiles"]:
            for t in row:
                c = classify(t)
                if c == "LOCKED":
                    continue
                total_unlocked += 1
                counts[c] += 1
        counts["UNLOCKED_TOTAL"] = total_unlocked
        day_counts.setdefault(day, []).append(counts)
    # average per day across steps within that day
    out = {}
    for day, clist in day_counts.items():
        agg = defaultdict(float)
        for c in clist:
            for k, v in c.items():
                agg[k] += v
        n = len(clist)
        out[day] = {k: v / n for k, v in agg.items()}
    return out

def summarize(util_by_day, label, days_range=None):
    days = sorted(util_by_day.keys())
    if days_range:
        days = [d for d in days if days_range[0] <= d <= days_range[1]]
    tot_unlocked = sum(util_by_day[d]["UNLOCKED_TOTAL"] for d in days)
    tot_plant = sum(util_by_day[d].get("PLANT", 0) for d in days)
    tot_empty = sum(util_by_day[d].get("EMPTY", 0) for d in days)
    tot_weed = sum(util_by_day[d].get("WEED", 0) for d in days)
    tot_animal = sum(util_by_day[d].get("ANIMAL_STRUCT", 0) for d in days)
    print(f"=== {label} (days {days[0]}-{days[-1]}, n={len(days)}) ===")
    print(f"  avg unlocked tiles/day: {tot_unlocked/len(days):.1f}")
    print(f"  PLANT (productive):     {100*tot_plant/tot_unlocked:5.1f}%")
    print(f"  ANIMAL_STRUCT:          {100*tot_animal/tot_unlocked:5.1f}%")
    print(f"  EMPTY (idle):           {100*tot_empty/tot_unlocked:5.1f}%")
    print(f"  WEED:                   {100*tot_weed/tot_unlocked:5.1f}%")
    other = tot_unlocked - tot_plant - tot_empty - tot_weed - tot_animal
    print(f"  OTHER:                  {100*other/tot_unlocked:5.1f}%")
    return 100*tot_plant/tot_unlocked

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "sim":
        from kaggle_environments import make
        agent_path, opp_path, seed = sys.argv[2], sys.argv[3], int(sys.argv[4])
        a = load_agent(agent_path)
        b = load_agent(opp_path)
        env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=False)
        env.info = {"seed": seed}
        env.run([a, b])
        util = util_from_steps_iter(env.steps, 24, lambda: 0)
        summarize(util, f"{agent_path} (seed {seed})")
    elif mode == "replay":
        path, player_name = sys.argv[2], sys.argv[3]
        j = json.load(open(path))
        names = j.get("info", {}).get("TeamNames") or ["p0","p1"]
        pidx = names.index(player_name)
        tpd = j.get("configuration", {}).get("turnsPerDay", 24)
        util = util_from_steps_iter(j["steps"], tpd, lambda: pidx)
        summarize(util, f"{path.split('/')[-1]} :: {player_name}")
