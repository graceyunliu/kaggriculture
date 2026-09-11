#!/usr/bin/env python3
"""
Step 4 (read-only counterfactual, no candidate, no gameplay change): for every near-shed crop claim
in real O36 play, trace whether preserving that exact tile would ever have actually mattered to a
LATER animal placement -- an upper-bound land-availability trace, not a panel test.

For each near-shed (shed_dist<=NEAR) crop claim event at day d0, tile T0, shed_dist s0:
  - record the nearest strictly-farther empty alternative tile available to the crop at that same
    moment (T0'), and the shed-distance cost the crop itself would have paid by using T0' instead
    (this is the crop's own displacement cost -- outcome D)
  - record whether the game's animal population is still growing after d0 (already have this)
  - find the NEXT animal-site claim anywhere later in the same real game (chronologically), and
    compare ITS shed-distance to s0:
      * if the later animal claim's shed_dist > s0: preserving T0 would (upper bound -- assumes T0
        stays free until then, i.e. no other process grabs it in between) have given that animal a
        strictly BETTER site. Record the improvement magnitude.
      * if <= s0: preserving T0 would not have helped that particular later animal (it already got
        something as good or better elsewhere).
      * if there is no later animal claim at all: preservation was moot (no animal ever needed it).

This is explicitly an upper-bound / naive trace (does not simulate a full counterfactual game), by
design -- it answers "how often would ANYTHING change" before spending panel budget on a real
reservation intervention.
"""
import sys, os, argparse, importlib.util, statistics as st
from pathlib import Path
from collections import Counter

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
    name = f"landopp_probe_{tag}_{p.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_game(agent_path, opp_path, seed, out_events):
    engmod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    mod0 = load_agent_module(agent_path, "p0")
    orig_agent = mod0.agent

    prev_empty = None
    crop_events = []     # (day, tile, s0, crop, farther_alt_tile, farther_alt_sd, displacement_cost)
    animal_events = []   # (day, tile, shed_dist)

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
                    s0 = shed_dist(tp)
                    if s0 <= NEAR:
                        farther = [q for q in prev_empty if shed_dist(q) > s0]
                        if farther:
                            alt = min(farther, key=lambda q: (shed_dist(q), q))
                            alt_sd = shed_dist(alt)
                            crop_events.append({
                                "day": day, "tile": tp, "s0": s0, "crop": t.get("crop"),
                                "alt_tile": alt, "alt_sd": alt_sd,
                                "displacement_cost": alt_sd - s0,
                            })

        claimed_before = set(mod0.S["claimed_sites"])
        result = orig_agent(obs, configuration)
        claimed_after = set(mod0.S["claimed_sites"])
        for site in claimed_after - claimed_before:
            animal_events.append({"day": day, "tile": site, "shed_dist": shed_dist(site)})

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

    # chronological lookup: for each crop event, find the next animal claim strictly after it
    animal_events.sort(key=lambda e: e["day"])
    for ce in crop_events:
        later = [ae for ae in animal_events if ae["day"] > ce["day"]]
        if not later:
            ce["outcome"] = "no_later_animal"
            ce["improvement"] = None
        else:
            nxt = later[0]  # chronologically next animal claim
            delta = nxt["shed_dist"] - ce["s0"]
            if delta > 0:
                ce["outcome"] = "would_improve"
                ce["improvement"] = delta
            else:
                ce["outcome"] = "no_help"
                ce["improvement"] = 0
        out_events.append(ce)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent", nargs="?", default="candidates/O36_MIN_HANDS2.py")
    ap.add_argument("--seeds", default="11-18")
    ap.add_argument("--opp", default="all")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opps = OPPS if args.opp == "all" else {args.opp: OPPS[args.opp]}

    events = []
    n_games = 0
    for opp_name, opp_path in opps.items():
        for seed in range(lo, hi + 1):
            run_game(args.agent, opp_path, seed, events)
            n_games += 1

    print(f"=== land-opportunity counterfactual trace, {n_games} games, {len(events)} near-shed crop events ===\n")

    outcome_ct = Counter(e["outcome"] for e in events)
    n = len(events)
    for k in ["would_improve", "no_help", "no_later_animal"]:
        c = outcome_ct.get(k, 0)
        print(f"{k:18s}: {c:5d} / {n} ({100*c/n:.1f}%)")

    improves = [e["improvement"] for e in events if e["outcome"] == "would_improve"]
    print(f"\nOf the {len(improves)} events where preservation would have helped the next animal claim:")
    if improves:
        print(f"  mean improvement    : {st.mean(improves):.2f} shed-dist tiles")
        print(f"  median improvement  : {st.median(improves):.1f}")
        dist_ct = Counter(improves)
        print(f"  improvement size distribution: {dict(sorted(dist_ct.items()))}")

    costs = [e["displacement_cost"] for e in events]
    print(f"\nCrop's own displacement cost if it had used the farther alternative instead (all {n} events):")
    print(f"  mean cost  : {st.mean(costs):.2f} shed-dist tiles")
    print(f"  median cost: {st.median(costs):.1f}")
    cost_ct = Counter(costs)
    print(f"  cost distribution: {dict(sorted(cost_ct.items()))}")

    # Cross-tab: does the crop's displacement cost tend to be smaller than the improvement it would
    # have enabled (i.e. is this a good trade even before considering animal economic value)?
    net = [e["improvement"] - e["displacement_cost"] for e in events if e["outcome"] == "would_improve"]
    if net:
        print(f"\nFor 'would_improve' events, net shed-distance tiles saved (animal improvement - crop cost):")
        print(f"  mean net: {st.mean(net):+.2f}   >0 in {sum(1 for x in net if x>0)}/{len(net)} events")


if __name__ == "__main__":
    main()
