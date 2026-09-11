#!/usr/bin/env python3
"""
leader_strategy_earliest_divergence: day-by-day strategy decomposition, O36 vs ladder replays.
Observational only. Purpose: find the EARLIEST persistent divergence in economic/policy behavior,
rather than starting from final-board geometry and working backward.

Metrics captured per end-of-day snapshot, for both O36 (live self-play/vs-opponent-tape) and real
ladder replay episodes (same observation shape: obs["private"], obs["farms"][seat]):
  - cash (money)
  - workers (1 + len(hands))
  - animals_placed (cumulative distinct animal-holding tiles)
  - animals_pending (currently unplaced animals sitting in shed + hands, i.e. bought but not sited)
  - animal_structures (PASTURE/COOP tile count, placed or not)
  - crop_tiles (PLANT kind tile count)
  - empty_tiles (None tiles)
  - seeds_held (sum of obs["private"]["seeds"])

Feed spending and revenue-by-product are NOT captured here (would need action/transaction logs, not
just state snapshots) -- flagged as a known gap, not silently omitted.

Usage:
  python3 strategy_divergence_probe.py o36 --seeds 11-18 --opp all
  python3 strategy_divergence_probe.py ladder --players 3정훈,Majkel1337,MtN,OceanMix,kanno,kwa,binghua,ymg_aq,SpaTaro --episodes 3
"""
import sys, os, argparse, importlib.util, json, glob, copy, statistics as st
from pathlib import Path
from collections import defaultdict

def find_repo_root():
    for p in [Path.home() / "mnt" / "Kaggriculture"]:
        if (p / "mini_engine.py").exists():
            return p
    return None

REPO = find_repo_root()
sys.path.insert(0, str(REPO))
os.chdir(REPO)
import mini_engine as me  # noqa: E402

CHECKPOINTS = [1, 3, 5, 8, 11, 15, 20, 25, 29]
ANIMALS = ["COW", "SHEEP", "GOOSE"]

OPPS = {
    "peter": "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk": "Opponents/tape_yangkuang2_106819729.py",
}


def metrics_from_obs(obs, seat_public):
    """obs: the full observation dict for the seat we care about (has its own 'private').
    seat_public: which index in farms/tiles is this seat's public farm (usually == player)."""
    farm = obs["farms"][seat_public]
    tiles = farm["tiles"]
    n_animal_tiles = 0
    n_structures = 0
    n_crop = 0
    n_empty = 0
    for row in tiles:
        for t in row:
            if t is None:
                n_empty += 1
            elif isinstance(t, dict):
                if "animal" in t:
                    n_animal_tiles += 1
                    n_structures += 1
                elif t.get("kind") in ("PASTURE", "COOP"):
                    n_structures += 1
                elif t.get("kind") == "PLANT":
                    n_crop += 1
    priv = obs.get("private", {})
    shed = priv.get("shed", {})
    invs = priv.get("inventories", [])
    pending = sum(shed.get(a, 0) for a in ANIMALS) + sum(sum(inv.get(a, 0) for a in ANIMALS) for inv in invs)
    seeds_held = sum(priv.get("seeds", {}).values())
    return {
        "cash": farm["money"],
        "workers": 1 + len(farm.get("hands", [])),
        "animals_placed": n_animal_tiles,
        "animals_pending": pending,
        "animal_structures": n_structures,
        "crop_tiles": n_crop,
        "empty_tiles": n_empty,
        "seeds_held": seeds_held,
    }


def load_agent_module(path, tag):
    p = Path(path)
    name = f"strat_probe_{tag}_{p.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_o36_game(agent_path, opp_path, seed):
    engmod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    a0 = load_agent_module(agent_path, "p0").agent
    a1 = load_agent_module(opp_path, "p1").agent
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                            "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = engmod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    per_day = {}
    seen_days = set()
    while True:
        for i in (0, 1):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = (a0 if i == 0 else a1)(obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = engmod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        obs0 = state[0].observation
        if obs0.hour == 23 and obs0.day not in seen_days:
            seen_days.add(obs0.day)
            snap = copy.deepcopy(me._fast_copy(obs0))
            per_day[obs0.day] = metrics_from_obs(snap, 0)
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    return per_day


def cmd_o36(args):
    lo, hi = map(int, args.seeds.split("-"))
    opps = OPPS if args.opp == "all" else {args.opp: OPPS[args.opp]}
    series = defaultdict(lambda: defaultdict(list))  # metric -> day -> [values]
    for opp_name, opp_path in opps.items():
        for seed in range(lo, hi + 1):
            per_day = run_o36_game(args.agent, opp_path, seed)
            for day, m in per_day.items():
                for k, v in m.items():
                    series[k][day].append(v)
    print_table("O36", series)
    return series


def cmd_ladder(args):
    players = args.players.split(",")
    n_ep = args.episodes
    series = defaultdict(lambda: defaultdict(list))
    for pname in players:
        folder = f"Replays/Auto/leaderboard-{pname}"
        files = sorted(glob.glob(folder + "/*.json"))[:n_ep]
        for f in files:
            try:
                d = json.load(open(f))
            except Exception:
                continue
            names = [a.get("Name") for a in d.get("info", {}).get("Agents", [])]
            if pname not in names:
                continue
            seat = names.index(pname)
            steps = d["steps"]
            last_by_day = {}
            for s in steps:
                obs = s[seat]["observation"]
                last_by_day[obs["day"]] = obs
            for day, obs in last_by_day.items():
                m = metrics_from_obs(obs, seat)
                for k, v in m.items():
                    series[k][day].append(v)
    print_table("LADDER", series)
    return series


def print_table(label, series):
    print(f"\n=== {label}: day-by-day means ===")
    metrics = ["cash", "workers", "animals_placed", "animals_pending", "animal_structures",
               "crop_tiles", "empty_tiles", "seeds_held"]
    header = "day   " + "  ".join(f"{m:>16s}" for m in metrics)
    print(header)
    for day in CHECKPOINTS:
        row = [f"{day:3d}  "]
        for m in metrics:
            vals = series[m].get(day, [])
            row.append(f"{st.mean(vals):16.1f}" if vals else f"{'--':>16s}")
        print("  ".join(row))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("o36")
    p1.add_argument("agent", nargs="?", default="candidates/O36_MIN_HANDS2.py")
    p1.add_argument("--seeds", default="11-18")
    p1.add_argument("--opp", default="all")
    p2 = sub.add_parser("ladder")
    p2.add_argument("--players", required=True)
    p2.add_argument("--episodes", type=int, default=3)
    args = ap.parse_args()
    if args.cmd == "o36":
        cmd_o36(args)
    else:
        cmd_ladder(args)


if __name__ == "__main__":
    main()
