#!/usr/bin/env python3
"""
Step 1 (observational only, O36 unmodified): measure shared-pool land-use collision pressure
between animal siting (_pick_site) and crop admission (_crop_pools), both of which draw from
S["claimed_sites"]/v["empty"]. Does NOT modify O36 or test any zoning/reservation scheme --
purely instruments the real, live decision process every hour.

For each hour of real play (both O36 and the opponent run unmodified):
  - recomputes (read-only, side-effect-free) the animal candidate set _pick_site would have seen
    this hour, and the crop "plant" candidate set _crop_pools would have seen this hour
  - records CONTENTION: hours where those two sets overlap at all, and the sharper case where
    the single top-ranked animal pick this hour is *also* in the crop's plant pool this hour
  - after the real agent call, detects newly-claimed animal sites (added to S["claimed_sites"])
    and checks whether that exact tile was in this hour's crop "plant" pool -> ANIMAL DISPLACES CROP
  - across hours, detects tiles that flip from empty to a PLANT tile and checks whether that tile
    was in this hour's (pre-flip) animal candidate set -> CROP DISPLACES ANIMAL
  - tracks every built PASTURE/COOP tile with no animal on it, hour by hour, for STRANDED
    INFRASTRUCTURE count + duration (not just final-board snapshot)
  - accumulates a per-tile heatmap of contention-set membership for SPATIAL PERSISTENCE

Usage: python3 collision_pressure_probe.py [--seeds 11-20] [--opp all|peter|alaylm|bahaen|yangk]
"""
import sys, os, argparse, importlib.util, statistics as stats
from pathlib import Path
from collections import Counter, defaultdict

def find_repo_root():
    for p in [Path.home() / "mnt" / "Kaggriculture"]:
        if (p / "mini_engine.py").exists():
            return p
    return None

REPO = find_repo_root()
sys.path.insert(0, str(REPO))
os.chdir(REPO)
import mini_engine as me  # noqa: E402

OPPS = {
    "peter": "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk": "Opponents/tape_yangkuang2_106819729.py",
}


def load_agent_module(path, tag):
    p = Path(path)
    name = f"collision_probe_{tag}_{p.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def phase(day):
    if day <= 10:
        return "early(1-10)"
    if day <= 20:
        return "mid(11-20)"
    return "late(21-29)"


def animal_candidates(mod, v):
    claimed = mod.S["claimed_sites"]
    if v["empty_pastures"]:
        c = [s_ for s_ in v["empty_pastures"] if s_ not in claimed]
        if c:
            return set(c), "empty_pastures"
    c = [s_ for s_ in v["empty"] if s_ not in claimed and s_ not in mod.SHED_TILES]
    return set(c), "empty"


def stranded_tiles(v):
    out = set()
    for y, row in enumerate(v["tiles"]):
        for x, t in enumerate(row):
            if isinstance(t, dict) and t.get("kind") in ("PASTURE", "COOP") and "animal" not in t:
                out.add((x, y))
    return out


def run_game(agent_path, opp_path, seed, metrics):
    engmod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)

    mod0 = load_agent_module(agent_path, "p0")
    orig_agent = mod0.agent

    prev_empty = None          # v["empty"] set from the previous hour (for crop-claim detection)
    prev_anim_cand = None      # animal candidate set from the previous hour
    stranded_since = {}        # tile -> day first seen stranded (for duration)

    def agent_patched(obs, configuration=None):
        nonlocal prev_empty, prev_anim_cand
        day, hour = obs["day"], obs["hour"]
        ph = phase(day)
        v = mod0.perceive(obs)
        seeds_left = dict(obs["private"]["seeds"])
        pools = mod0._crop_pools(v, seeds_left, day)
        plant_cand = set(pools["plant"])
        anim_cand, _branch = animal_candidates(mod0, v)

        # 4. actual contention: overlap this hour
        overlap = plant_cand & anim_cand
        metrics["hours_total"] += 1
        if overlap:
            metrics["hours_with_overlap"] += 1
            metrics["overlap_cells_sum"] += len(overlap)
            for s_ in overlap:
                metrics["heatmap"][s_] += 1
        # sharper: this hour's #1 animal pick is also in the crop pool
        if anim_cand:
            top_pick = min(anim_cand, key=mod0._site_key) if hasattr(mod0, "_site_key") else min(anim_cand, key=mod0._shed_dist)
            if top_pick in plant_cand:
                metrics["hours_top_pick_collision"] += 1

        # 2. crop -> animal displacement: did a tile flip from empty to PLANT since last hour,
        #    and was that tile in the animal candidate set as of the previous hour?
        if prev_empty is not None and prev_anim_cand is not None:
            now_empty = v["empty"]
            newly_not_empty = prev_empty - set(now_empty)
            for tp in newly_not_empty:
                t = v["tiles"][tp[1]][tp[0]]
                if isinstance(t, dict) and t.get("kind") == "PLANT":
                    metrics["crop_claims_total"] += 1
                    if tp in prev_anim_cand:
                        metrics["crop_displaces_animal"] += 1
                        metrics["crop_displaces_animal_by_phase"][ph] += 1
                        # STRONG-displacement refinement: rank tp among the animal candidate
                        # set as _pick_site would have ranked it (shed-distance order), and
                        # measure whether removing tp actually degrades the best available site.
                        ranked = sorted(prev_anim_cand, key=lambda s_: (mod0._shed_dist(s_), s_))
                        rank = ranked.index(tp) + 1  # 1-indexed
                        metrics["crop_displaces_animal_ranks"].append(rank)
                        if rank <= 1:
                            metrics["crop_displaces_animal_top1"] += 1
                        if rank <= 3:
                            metrics["crop_displaces_animal_top3"] += 1
                        if rank <= 5:
                            metrics["crop_displaces_animal_top5"] += 1
                        if rank <= 10:
                            metrics["crop_displaces_animal_top10"] += 1
                        best_before = mod0._shed_dist(ranked[0])
                        remaining = [s_ for s_ in ranked if s_ != tp]
                        best_after = mod0._shed_dist(min(remaining, key=mod0._shed_dist)) if remaining else None
                        if best_after is not None and best_after > best_before:
                            metrics["crop_displaces_animal_degrades_best"] += 1
                            metrics["crop_displaces_animal_degrade_amount"].append(best_after - best_before)

        claimed_before = set(mod0.S["claimed_sites"])
        stranded_before = stranded_tiles(v)

        result = orig_agent(obs, configuration)

        # 1. animal -> crop displacement: newly-claimed animal sites this hour that were in the
        #    crop's plant pool this same hour
        claimed_after = set(mod0.S["claimed_sites"])
        newly_claimed = claimed_after - claimed_before
        for site in newly_claimed:
            if site in plant_cand:
                crop = mod0._plant_choice(site, seeds_left)
                metrics["animal_displaces_crop"] += 1
                metrics["animal_displaces_crop_by_phase"][ph] += 1
                metrics["animal_displaces_crop_by_crop"][crop or "none_wanted"] += 1

        # 3. stranded infrastructure: tick every stranded tile's duration
        for tp in stranded_before:
            if tp not in stranded_since:
                stranded_since[tp] = day
            metrics["stranded_tile_hours"] += 1
        for tp in list(stranded_since.keys()):
            if tp not in stranded_before:
                dur = day - stranded_since[tp]
                metrics["stranded_durations_days"].append(dur)
                del stranded_since[tp]

        prev_empty = set(v["empty"])
        prev_anim_cand = anim_cand
        return result

    mod0.agent = agent_patched
    agent0 = agent_patched
    mod1 = load_agent_module(opp_path, "p1")
    agent1 = mod1.agent

    agents = [agent0, agent1]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                            "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = engmod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0
    while True:
        for i in (0, 1):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = engmod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break

    # any still-stranded tiles at game end: count their duration through day 29
    for tp, since in stranded_since.items():
        metrics["stranded_durations_days"].append(29 - since)

    metrics["games"] += 1
    metrics["final_money"].append(state[0].observation.farms[0]["money"])
    metrics["final_stranded_count"].append(len(stranded_tiles(mod0.perceive(state[0].observation))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--seeds", default="11-20")
    ap.add_argument("--opp", default="all")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opps = OPPS if args.opp == "all" else {args.opp: OPPS[args.opp]}

    metrics = {
        "games": 0, "hours_total": 0, "hours_with_overlap": 0, "overlap_cells_sum": 0,
        "hours_top_pick_collision": 0,
        "crop_claims_total": 0, "crop_displaces_animal": 0,
        "crop_displaces_animal_by_phase": Counter(),
        "crop_displaces_animal_ranks": [], "crop_displaces_animal_top1": 0,
        "crop_displaces_animal_top3": 0, "crop_displaces_animal_top5": 0,
        "crop_displaces_animal_top10": 0, "crop_displaces_animal_degrades_best": 0,
        "crop_displaces_animal_degrade_amount": [],
        "animal_displaces_crop": 0,
        "animal_displaces_crop_by_phase": Counter(),
        "animal_displaces_crop_by_crop": Counter(),
        "stranded_tile_hours": 0, "stranded_durations_days": [],
        "final_money": [], "final_stranded_count": [],
        "heatmap": Counter(),
    }

    for opp_name, opp_path in opps.items():
        for seed in range(lo, hi + 1):
            run_game(args.agent, opp_path, seed, metrics)

    g = metrics["games"]
    print(f"=== collision-pressure probe: {g} games, seeds {args.seeds}, opp={args.opp} ===\n")
    print(f"hours observed                         : {metrics['hours_total']}")
    print(f"hours with animal/crop candidate overlap: {metrics['hours_with_overlap']} "
          f"({100*metrics['hours_with_overlap']/metrics['hours_total']:.1f}%)")
    print(f"  mean overlap set size when nonzero    : {metrics['overlap_cells_sum']/max(1,metrics['hours_with_overlap']):.2f} tiles")
    print(f"hours where #1 animal pick sits in crop's plant pool: {metrics['hours_top_pick_collision']} "
          f"({100*metrics['hours_top_pick_collision']/metrics['hours_total']:.1f}%)\n")

    print(f"ANIMAL -> CROP displacement events      : {metrics['animal_displaces_crop']}  "
          f"({metrics['animal_displaces_crop']/g:.2f}/game)")
    print(f"  by phase: {dict(metrics['animal_displaces_crop_by_phase'])}")
    print(f"  by crop that wanted the tile: {dict(metrics['animal_displaces_crop_by_crop'])}\n")

    print(f"CROP -> ANIMAL displacement events      : {metrics['crop_displaces_animal']} / "
          f"{metrics['crop_claims_total']} crop claims  ({metrics['crop_displaces_animal']/g:.2f}/game)")
    print(f"  by phase: {dict(metrics['crop_displaces_animal_by_phase'])}")
    n = metrics['crop_displaces_animal']
    if n:
        print(f"  STRONG displacement (rank among live animal candidates at time of claim):")
        print(f"    top1 : {metrics['crop_displaces_animal_top1']}/{n} ({100*metrics['crop_displaces_animal_top1']/n:.1f}%)")
        print(f"    top3 : {metrics['crop_displaces_animal_top3']}/{n} ({100*metrics['crop_displaces_animal_top3']/n:.1f}%)")
        print(f"    top5 : {metrics['crop_displaces_animal_top5']}/{n} ({100*metrics['crop_displaces_animal_top5']/n:.1f}%)")
        print(f"    top10: {metrics['crop_displaces_animal_top10']}/{n} ({100*metrics['crop_displaces_animal_top10']/n:.1f}%)")
        print(f"    median rank: {stats.median(metrics['crop_displaces_animal_ranks']):.0f}, "
              f"mean rank: {stats.mean(metrics['crop_displaces_animal_ranks']):.1f}")
        deg = metrics['crop_displaces_animal_degrades_best']
        print(f"    degraded the single best available animal-site score: {deg}/{n} ({100*deg/n:.1f}%)")
        if metrics['crop_displaces_animal_degrade_amount']:
            print(f"      mean degradation when it happened: {stats.mean(metrics['crop_displaces_animal_degrade_amount']):.2f} shed-dist tiles")
    print()

    durs = metrics["stranded_durations_days"]
    print(f"STRANDED PASTURE/COOP episodes           : {len(durs)}  ({len(durs)/g:.2f}/game)")
    if durs:
        print(f"  mean duration (days stranded)          : {stats.mean(durs):.1f}, median {stats.median(durs):.1f}, max {max(durs)}")
    print(f"  mean final-board stranded count/game   : {stats.mean(metrics['final_stranded_count']):.2f}")
    print(f"  mean stranded-tile-hours/game          : {metrics['stranded_tile_hours']/g:.1f}\n")

    print(f"mean final money                         : {stats.mean(metrics['final_money']):.0f}\n")

    top_heat = metrics["heatmap"].most_common(15)
    print("SPATIAL PERSISTENCE -- top 15 contention-set tiles (tile: hours appeared in overlap set):")
    for tile, cnt in top_heat:
        print(f"  {tile}: {cnt}")


if __name__ == "__main__":
    main()
