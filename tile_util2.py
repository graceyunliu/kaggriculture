"""Extended: hand count, crop mix, animal fleet size/type over the game."""
import importlib.util, sys, json
from collections import defaultdict, Counter

def load_agent(path):
    spec = importlib.util.spec_from_file_location(path.replace("/", "_").replace(".", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.agent

def analyze(step_iter, pidx_fn, tpd, label):
    hand_counts = []
    crop_counter = Counter()
    animal_counter = Counter()
    plant_tile_days = 0.0
    last_day = -1
    days_seen = set()
    end_hands = 0
    end_animals = Counter()
    for step in step_iter:
        obs0 = step[0]["observation"] if isinstance(step[0], dict) else step[0].observation
        day = obs0.get("day", 0) if isinstance(obs0, dict) else obs0["day"]
        farms = obs0.get("farms") if isinstance(obs0, dict) else obs0["farms"]
        if not farms:
            continue
        farm = farms[pidx_fn()]
        days_seen.add(day)
        hand_counts.append(len(farm.get("hands", [])))
        end_hands = len(farm.get("hands", []))
        end_animals = Counter()
        for row in farm["tiles"]:
            for t in row:
                if isinstance(t, dict):
                    if t.get("kind") == "PLANT":
                        crop_counter[t.get("crop")] += 1
                        plant_tile_days += 1.0 / tpd
                    elif t.get("kind") == "PASTURE" and t.get("animal"):
                        animal_counter[t["animal"]] += 1
                        end_animals[t["animal"]] += 1
                    elif t.get("kind") == "COOP" and t.get("animal"):
                        animal_counter[t["animal"]] += 1
                        end_animals[t["animal"]] += 1
    n_snap = len(hand_counts)
    print(f"=== {label} ===")
    print(f"  avg hands (across all snapshots): {sum(hand_counts)/n_snap:.2f}, final hands: {end_hands}")
    print(f"  final animal fleet: {dict(end_animals)}")
    total_crop_tiledays = sum(crop_counter.values()) / n_snap * len(days_seen)  # rough
    print(f"  crop-tile snapshot mix (share of PLANT snapshots): {[(k, f'{100*v/sum(crop_counter.values()):.1f}%') for k,v in crop_counter.most_common()]}")

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "sim":
        from kaggle_environments import make
        agent_path, opp_path, seed = sys.argv[2], sys.argv[3], int(sys.argv[4])
        a = load_agent(agent_path); b = load_agent(opp_path)
        env = make("kaggriculture", configuration={"episodeSteps": 720}, debug=False)
        env.info = {"seed": seed}
        env.run([a, b])
        analyze(env.steps, lambda: 0, 24, f"{agent_path} (seed {seed})")
    elif mode == "replay":
        path, player_name = sys.argv[2], sys.argv[3]
        j = json.load(open(path))
        names = j.get("info", {}).get("TeamNames") or ["p0","p1"]
        pidx = names.index(player_name)
        tpd = j.get("configuration", {}).get("turnsPerDay", 24)
        analyze(j["steps"], lambda: pidx, tpd, f"{path.split('/')[-1]} :: {player_name}")
