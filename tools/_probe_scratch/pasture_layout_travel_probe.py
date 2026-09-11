#!/usr/bin/env python3
"""
Measurement-only probe (no gameplay change) for the pasture-siting geometry question:

    Does the current _pick_site rule (min shed-distance, tie-break by raw (x,y))
    create economically meaningful extra travel vs a counterfactual rule that
    additionally prefers adjacency to already-claimed pasture/coop sites?

For each real game (agent's actual decisions untouched):
  - hooks _pick_site to record, at each real siting decision, the exact candidate
    set the agent saw and the site it actually chose, and ALSO computes (offline,
    not fed back into the game) what a compact-preferring tie-break would have
    chosen from that same candidate set.
  - hooks _route_step to classify every animal-route action as TRAVEL (a _step
    direction) or WORK (PICKUP/FEED/CARE/COLLECT_FERTILIZER/HARVEST/PASS), which
    is the direct "turns spent traveling vs productive" instrumentation.

After the game: computes a greedy nearest-neighbor tour distance from the shed
over (a) the actual chosen site sequence and (b) the counterfactual site
sequence, as a cheap route-length proxy, and reports the travel/work action
split actually observed in the real game.

Usage: python3 pasture_layout_travel_probe.py AGENT_PATH --seeds 1-10
"""
import sys, os, argparse, importlib.util, statistics as stats
from pathlib import Path

def find_repo_root():
    for p in [Path.home() / "mnt" / "Kaggriculture"]:
        if (p / "mini_engine.py").exists():
            return p
    return None

REPO = find_repo_root()
if REPO is None:
    print("Could not locate Kaggriculture repo root (expected mini_engine.py).", file=sys.stderr)
    sys.exit(1)
sys.path.insert(0, str(REPO))
os.chdir(REPO)

import mini_engine as me  # noqa: E402

SHED = [(4, 4), (5, 4), (4, 5), (5, 5)]
DIRS = {"EAST", "WEST", "SOUTH", "NORTH"}


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def shed_dist(pos):
    return min(dist(pos, t) for t in SHED)


def nn_tour_length(sites, start=None):
    if not sites:
        return 0.0
    remaining = list(sites)
    cur = start if start is not None else min(SHED, key=lambda t: dist(t, remaining[0]))
    total = 0.0
    while remaining:
        nxt = min(remaining, key=lambda s: dist(cur, s))
        total += dist(cur, nxt)
        cur = nxt
        remaining.remove(nxt)
    return total


def bbox_area(sites):
    if len(sites) < 2:
        return 0.0
    xs = [s[0] for s in sites]; ys = [s[1] for s in sites]
    return (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)


def mean_pairwise_dist(sites):
    if len(sites) < 2:
        return 0.0
    n = len(sites)
    tot = 0.0; cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            tot += dist(sites[i], sites[j]); cnt += 1
    return tot / cnt if cnt else 0.0


def connected_components(sites, radius=1):
    """Count clusters under Chebyshev-adjacency (radius=1 => 8-connected)."""
    pts = set(sites)
    seen = set()
    comps = 0
    for p in pts:
        if p in seen:
            continue
        comps += 1
        stack = [p]
        seen.add(p)
        while stack:
            cx, cy = stack.pop()
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if dx == 0 and dy == 0:
                        continue
                    q = (cx + dx, cy + dy)
                    if q in pts and q not in seen:
                        seen.add(q)
                        stack.append(q)
    return comps


def load_agent_module(path, tag):
    path = Path(path)
    name = f"probe_agent_{tag}_{path.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def instrument(mod, log):
    orig_pick_site = mod._pick_site
    orig_route_step = mod._route_step
    placed_actual = []
    placed_counterfactual = []

    def compact_key_factory(claimed_so_far):
        def key(s):
            adj = 0 if not claimed_so_far else min(dist(s, c) for c in claimed_so_far)
            return (shed_dist(s), adj, s)
        return key

    def pick_site_patched(v, species=None):
        claimed = mod.S["claimed_sites"]
        cand = None
        if v["empty_pastures"]:
            c = [s_ for s_ in v["empty_pastures"] if s_ not in claimed]
            if c:
                cand = c
        if cand is None:
            c = [s_ for s_ in v["empty"] if s_ not in claimed and s_ not in mod.SHED_TILES]
            cand = c if c else None

        result = orig_pick_site(v, species)

        if cand:
            actual_choice = result
            compact_choice = min(cand, key=compact_key_factory(placed_counterfactual))
            log["pick_site_calls"].append({
                "n_candidates": len(cand),
                "actual": actual_choice,
                "compact": compact_choice,
                "agree": actual_choice == compact_choice,
            })
            if actual_choice is not None:
                placed_actual.append(actual_choice)
            placed_counterfactual.append(compact_choice)
        return result

    def route_step_patched(*args, **kwargs):
        result = orig_route_step(*args, **kwargs)
        if isinstance(result, list) and len(result) >= 1:
            if result[0] in DIRS:
                log["travel_actions"] += 1
            elif result[0] is not None:
                log["work_actions"] += 1
        return result

    mod._pick_site = pick_site_patched
    mod._route_step = route_step_patched
    return placed_actual, placed_counterfactual


def run_game(agent_path, opponent_path, seed, engine="master"):
    engmod, defaults = me.load_engine(engine)
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)

    mod0 = load_agent_module(agent_path, "p0")
    log0 = {"pick_site_calls": [], "travel_actions": 0, "work_actions": 0}
    placed0_actual, placed0_cf = instrument(mod0, log0)
    agent0 = mod0.agent

    opp_path = opponent_path if opponent_path else agent_path
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

    tour_actual = nn_tour_length(placed0_actual)
    tour_cf = nn_tour_length(placed0_cf)
    n_calls = len(log0["pick_site_calls"])
    n_agree = sum(1 for c in log0["pick_site_calls"] if c["agree"])
    travel = log0["travel_actions"]
    work = log0["work_actions"]
    frac_travel = travel / (travel + work) if (travel + work) else float("nan")
    return {
        "seed": seed,
        "n_sitings": n_calls,
        "n_agree_with_compact": n_agree,
        "tour_actual": tour_actual,
        "tour_compact_cf": tour_cf,
        "tour_delta": tour_actual - tour_cf,
        "mean_pairwise_actual": mean_pairwise_dist(placed0_actual),
        "mean_pairwise_cf": mean_pairwise_dist(placed0_cf),
        "bbox_actual": bbox_area(placed0_actual),
        "bbox_cf": bbox_area(placed0_cf),
        "comps_actual": connected_components(placed0_actual),
        "comps_cf": connected_components(placed0_cf),
        "travel_actions": travel,
        "work_actions": work,
        "frac_travel": frac_travel,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--opponent", default=None)
    ap.add_argument("--seeds", default="1-10")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))

    rows = []
    for seed in range(lo, hi + 1):
        r = run_game(args.agent, args.opponent, seed)
        rows.append(r)
        print(f"seed={r['seed']:3d} sitings={r['n_sitings']:3d} agree={r['n_agree_with_compact']:3d}/{r['n_sitings']:<3d} "
              f"tour_act={r['tour_actual']:6.1f} tour_cf={r['tour_compact_cf']:6.1f} d={r['tour_delta']:+6.1f} "
              f"mpd_act={r['mean_pairwise_actual']:5.1f} mpd_cf={r['mean_pairwise_cf']:5.1f} "
              f"bbox_act={r['bbox_actual']:5.1f} bbox_cf={r['bbox_cf']:5.1f} "
              f"comps_act={r['comps_actual']:2d} comps_cf={r['comps_cf']:2d} "
              f"travel={r['travel_actions']:4d} work={r['work_actions']:4d} frac_travel={r['frac_travel']:.3f}")

    def mean(key):
        vals = [r[key] for r in rows]
        return stats.mean(vals) if vals else float("nan")

    print("\n--- summary across seeds ---")
    for k in ["n_sitings", "n_agree_with_compact", "tour_actual", "tour_compact_cf", "tour_delta",
              "mean_pairwise_actual", "mean_pairwise_cf", "bbox_actual", "bbox_cf",
              "comps_actual", "comps_cf", "travel_actions", "work_actions", "frac_travel"]:
        print(f"mean {k:24s} = {mean(k):.3f}")
    ta = mean("tour_actual"); td = mean("tour_delta")
    if ta:
        print(f"tour_delta as % of actual tour = {td/ta*100:+.1f}%")


if __name__ == "__main__":
    main()
