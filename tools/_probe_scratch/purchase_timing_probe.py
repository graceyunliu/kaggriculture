#!/usr/bin/env python3
"""
Step 2 refinement: purchase/claim-timing cadence, O36 vs multiple leaderboard replays.
Observational only -- no gameplay change, no candidate built.

For each game (O36 live-play, or a leaderboard replay), builds a day-indexed timeline of every
tile that ever holds an animal, recording the day it FIRST appears with an animal and its
shed-distance at that moment. From that we derive:
  - day of first animal site claimed
  - cumulative distinct animal sites claimed by day (1,3,5,8,11,15,20,25,29)
  - shed-distance distribution of newly-claimed sites, by day-of-claim
  - near-shed-region (shed_dist <= 3) crop occupancy over the same days, as the competing signal

Usage:
  python3 purchase_timing_probe.py o36 --seeds 11-20 --opp all
  python3 purchase_timing_probe.py ladder --players 3정훈,Majkel1337,MtN,OceanMix,kanno,kwa,binghua,ymg_aq,SpaTaro --episodes 3
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

SHED = [(4, 4), (5, 4), (4, 5), (5, 5)]
DAYS_CHECKPOINTS = [1, 3, 5, 8, 11, 15, 20, 25, 29]

def dist(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
def shed_dist(p): return min(dist(p, t) for t in SHED)

OPPS = {
    "peter": "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk": "Opponents/tape_yangkuang2_106819729.py",
}


def timeline_from_daily_tiles(daily_tiles):
    """daily_tiles: list of (day, tiles-grid) in increasing day order (one snapshot per day,
    end-of-day state). Returns: first_seen = {(x,y): (day, shed_dist)} for every tile that ever
    holds an animal, plus per-day near-shed (shed_dist<=3) crop-occupied tile count."""
    first_seen = {}
    near_shed_crop_by_day = {}
    for day, tiles in daily_tiles:
        crop_near = 0
        for y, row in enumerate(tiles):
            for x, t in enumerate(row):
                if not isinstance(t, dict):
                    continue
                p = (x, y)
                if "animal" in t and p not in first_seen:
                    first_seen[p] = (day, shed_dist(p))
                if t.get("kind") == "PLANT" and shed_dist(p) <= 3:
                    crop_near += 1
        near_shed_crop_by_day[day] = crop_near
    return first_seen, near_shed_crop_by_day


def cumulative_by_checkpoint(first_seen):
    days = sorted(d for d, _ in first_seen.values())
    out = {}
    for cp in DAYS_CHECKPOINTS:
        out[cp] = sum(1 for d in days if d <= cp)
    return out


def load_agent_module(path, tag):
    p = Path(path)
    name = f"timing_probe_{tag}_{p.stem}_{os.getpid()}"
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
    daily_tiles = []
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
            daily_tiles.append((obs0.day, copy.deepcopy(obs0.farms[0]["tiles"])))
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    return daily_tiles


def cmd_o36(args):
    lo, hi = map(int, args.seeds.split("-"))
    opps = OPPS if args.opp == "all" else {args.opp: OPPS[args.opp]}
    all_cum = []
    all_first_day = []
    all_ranks_by_day = defaultdict(list)  # day -> list of shed_dist at claim
    near_shed_crop_series = defaultdict(list)  # checkpoint day -> list of crop-near-shed counts
    for opp_name, opp_path in opps.items():
        for seed in range(lo, hi + 1):
            daily_tiles = run_o36_game(args.agent, opp_path, seed)
            first_seen, near_shed = timeline_from_daily_tiles(daily_tiles)
            if not first_seen:
                continue
            all_first_day.append(min(d for d, _ in first_seen.values()))
            all_cum.append(cumulative_by_checkpoint(first_seen))
            for p, (d, sd) in first_seen.items():
                all_ranks_by_day[d].append(sd)
            for cp in DAYS_CHECKPOINTS:
                if cp in near_shed:
                    near_shed_crop_series[cp].append(near_shed[cp])

    print(f"=== O36 ({args.agent}) purchase/claim timing, {len(all_cum)} games ===")
    print(f"day of first animal site claimed: mean={st.mean(all_first_day):.2f}, median={st.median(all_first_day):.1f}, "
          f"min={min(all_first_day)}, max={max(all_first_day)}")
    print("cumulative distinct animal sites claimed by day (mean across games):")
    for cp in DAYS_CHECKPOINTS:
        vals = [c[cp] for c in all_cum]
        print(f"  day {cp:2d}: mean={st.mean(vals):5.2f}  median={st.median(vals):4.1f}")
    print("\nshed-distance of newly-claimed sites, by day claimed (pooled, mean/median/n):")
    for d in sorted(all_ranks_by_day)[:15]:
        vals = all_ranks_by_day[d]
        print(f"  day {d:2d}: mean_shed_dist={st.mean(vals):.2f} median={st.median(vals):.1f} n={len(vals)}")
    print("\nnear-shed (shed_dist<=3) crop-occupied tile count by day (mean across games):")
    for cp in DAYS_CHECKPOINTS:
        if near_shed_crop_series[cp]:
            print(f"  day {cp:2d}: mean={st.mean(near_shed_crop_series[cp]):.2f}")


def cmd_ladder(args):
    players = args.players.split(",")
    n_ep = args.episodes
    all_cum = []
    all_first_day = []
    all_ranks_by_day = defaultdict(list)
    near_shed_crop_series = defaultdict(list)
    per_player = defaultdict(list)

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
            daily = {}
            for s in steps:
                obs = s[0]["observation"] if s[0]["observation"]["day"] is not None else None
            # collect end-of-day (last hour seen) snapshot per day for this seat
            last_by_day = {}
            for s in steps:
                obs = s[0]["observation"]
                last_by_day[obs["day"]] = obs["farms"][seat]["tiles"]
            daily_tiles = sorted(last_by_day.items())
            first_seen, near_shed = timeline_from_daily_tiles(daily_tiles)
            if not first_seen:
                continue
            fd = min(dd for dd, _ in first_seen.values())
            all_first_day.append(fd)
            per_player[pname].append(fd)
            all_cum.append(cumulative_by_checkpoint(first_seen))
            for p, (dd, sd) in first_seen.items():
                all_ranks_by_day[dd].append(sd)
            for cp in DAYS_CHECKPOINTS:
                if cp in near_shed:
                    near_shed_crop_series[cp].append(near_shed[cp])

    print(f"=== LADDER purchase/claim timing, {len(all_cum)} episodes across {len(players)} players ===")
    print(f"day of first animal site claimed: mean={st.mean(all_first_day):.2f}, median={st.median(all_first_day):.1f}, "
          f"min={min(all_first_day)}, max={max(all_first_day)}")
    print("per-player mean day-of-first-claim:")
    for pname, vals in per_player.items():
        print(f"  {pname:14s}: n={len(vals)} mean={st.mean(vals):.1f} vals={vals}")
    print("\ncumulative distinct animal sites claimed by day (mean across episodes):")
    for cp in DAYS_CHECKPOINTS:
        vals = [c[cp] for c in all_cum]
        print(f"  day {cp:2d}: mean={st.mean(vals):5.2f}  median={st.median(vals):4.1f}")
    print("\nshed-distance of newly-claimed sites, by day claimed (pooled, mean/median/n):")
    for d in sorted(all_ranks_by_day)[:15]:
        vals = all_ranks_by_day[d]
        print(f"  day {d:2d}: mean_shed_dist={st.mean(vals):.2f} median={st.median(vals):.1f} n={len(vals)}")
    print("\nnear-shed (shed_dist<=3) crop-occupied tile count by day (mean across episodes):")
    for cp in DAYS_CHECKPOINTS:
        if near_shed_crop_series[cp]:
            print(f"  day {cp:2d}: mean={st.mean(near_shed_crop_series[cp]):.2f}")


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
