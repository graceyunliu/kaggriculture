#!/usr/bin/env python3
"""
Step 3: explain O36's near-shed crop admission -- observational only, O36 unmodified.

Code fact established by reading candidates/O36_MIN_HANDS2.py before running anything (not an aggregate
occupancy comparison): `_crop_pools`'s "plant" candidate list is
    sorted(v["empty"], key=lambda q: (_shed_dist(q), q))[:n_seeds]
i.e. it is ALWAYS exactly the n_seeds nearest-to-shed empty tiles, full stop -- not scan-order incidental,
not crop-type-aware. The crop TYPE for a tile (`_plant_choice`) is decided only AFTER the tile is already
admitted, and depends only on whether the tile happens to be within NEAR_RADIUS, not on whether that
specific tile needed to be near the shed. So by construction, crop admission cannot choose a farther tile
while a nearer one sits empty and available, unless there are literally more near-shed empty cells than
seeds in hand -- there's no opportunity-cost check against future animal demand anywhere in this path.

This probe measures, for every ACTUAL crop claim in the real game:
  1. shed_dist of the claimed tile, and the crop type chosen there
  2. how many strictly-farther empty tiles existed simultaneously (the tile was never a forced choice
     among only near-shed candidates -- there was land order structurally exhausted first)
  3. whether more distinct animal sites get claimed LATER in the same game (i.e. this crop claim happened
     while future animal demand still existed, not after the animal population was already finished growing)
  4. crop-type breakdown specifically within the near-shed band (shed_dist<=3)
"""
import sys, os, argparse, importlib.util, copy, statistics as st
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

SHED = [(4, 4), (5, 4), (4, 5), (5, 5)]
NEAR = 3

def dist(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
def shed_dist(p): return min(dist(p, t) for t in SHED)

OPPS = {
    "peter": "Opponents/tape_peterparker_106816877.py",
    "alaylm": "Opponents/tape_alaylm_106813359.py",
    "bahaen": "Opponents/tape_bahaenes_106828159.py",
    "yangk": "Opponents/tape_yangkuang2_106819729.py",
}


def load_agent_module(path, tag):
    p = Path(path)
    name = f"reasons_probe_{tag}_{p.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_game(agent_path, opp_path, seed, out):
    engmod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    mod0 = load_agent_module(agent_path, "p0")
    orig_agent = mod0.agent

    prev_empty = None
    crop_claims = []   # list of dict: day, shed_dist, crop, n_farther_available
    animal_claim_days = []
    claimed_before_state = set()

    def agent_patched(obs, configuration=None):
        nonlocal prev_empty
        day = obs["day"]
        v = mod0.perceive(obs)
        now_empty = set(v["empty"])

        if prev_empty is not None:
            newly_not_empty = prev_empty - now_empty
            for tp in newly_not_empty:
                t = v["tiles"][tp[1]][tp[0]]
                if isinstance(t, dict) and t.get("kind") == "PLANT":
                    sd = shed_dist(tp)
                    n_farther = sum(1 for q in prev_empty if shed_dist(q) > sd)
                    crop_claims.append({"day": day, "shed_dist": sd, "crop": t.get("crop"),
                                         "n_farther_available": n_farther})

        claimed_before = set(mod0.S["claimed_sites"])
        result = orig_agent(obs, configuration)
        claimed_after = set(mod0.S["claimed_sites"])
        for site in claimed_after - claimed_before:
            animal_claim_days.append(day)

        prev_empty = now_empty
        return result

    mod0.agent = agent_patched
    a0 = agent_patched
    a1 = load_agent_module(opp_path, "p1").agent
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0},
                            "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = engmod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while True:
        for i in (0, 1):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = (a0 if i == 0 else a1)(obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = engmod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break

    last_animal_claim_day = max(animal_claim_days) if animal_claim_days else -1
    for c in crop_claims:
        c["claimed_before_animal_population_finished"] = c["day"] < last_animal_claim_day
        out.append(c)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent", nargs="?", default="candidates/O36_MIN_HANDS2.py")
    ap.add_argument("--seeds", default="11-18")
    ap.add_argument("--opp", default="all")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opps = OPPS if args.opp == "all" else {args.opp: OPPS[args.opp]}

    claims = []
    n_games = 0
    for opp_name, opp_path in opps.items():
        for seed in range(lo, hi + 1):
            run_game(args.agent, opp_path, seed, claims)
            n_games += 1

    near = [c for c in claims if c["shed_dist"] <= NEAR]
    far = [c for c in claims if c["shed_dist"] > NEAR]

    print(f"=== near-shed crop admission reasons, {n_games} games ({args.agent}) ===\n")
    print(f"total crop claims: {len(claims)}  |  near-shed (<=  {NEAR}): {len(near)} ({100*len(near)/len(claims):.1f}%)  |  far: {len(far)}\n")

    print("1/2. Mechanical-preference check: for every crop claim, how many strictly-farther empty tiles")
    print("     existed simultaneously and were passed over (never a forced 'only option' situation)?")
    n_far_avail = [c["n_farther_available"] for c in claims]
    n_had_farther = sum(1 for x in n_far_avail if x > 0)
    print(f"     claims where >=1 farther empty tile existed at the same time: {n_had_farther}/{len(claims)} "
          f"({100*n_had_farther/len(claims):.1f}%)")
    print(f"     mean farther-tiles-available when a claim happened: {st.mean(n_far_avail):.1f} (median {st.median(n_far_avail):.0f})\n")

    print("4. Fraction of near-shed crop claims made BEFORE the game's animal population finished growing")
    print("   (i.e. planted while future animal demand still existed):")
    n_premature = sum(1 for c in near if c["claimed_before_animal_population_finished"])
    print(f"   {n_premature}/{len(near)} ({100*n_premature/len(near):.1f}%) of near-shed crop claims happened")
    print(f"   on a day strictly before this game's LAST animal-site claim.\n")

    print("5. Crop-type breakdown, near-shed vs far:")
    near_ct = Counter(c["crop"] for c in near)
    far_ct = Counter(c["crop"] for c in far)
    all_crops = sorted(set(near_ct) | set(far_ct))
    for crop in all_crops:
        n_n, n_f = near_ct.get(crop, 0), far_ct.get(crop, 0)
        tot = n_n + n_f
        print(f"   {crop:12s}: near={n_n:4d} far={n_f:4d}  ({100*n_n/tot:.0f}% of this crop planted near-shed)" if tot else "")

    print(f"\nby-day distribution of near-shed claims (day: count):")
    by_day = Counter(c["day"] for c in near)
    for d in sorted(by_day)[:20]:
        print(f"   day {d:2d}: {by_day[d]}")


if __name__ == "__main__":
    main()
