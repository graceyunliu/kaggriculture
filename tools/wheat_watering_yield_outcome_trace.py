#!/usr/bin/env python3
"""wheat_water_tier -- direct yield/death outcome trace (Sep 13), extending the binding-trace conflict.

Engine facts (vendor/kaggle_environments_engine_master/kaggriculture.py):
  - WHEAT is non-ongoing, max_yield_day=4, window_start=(4+1)//2=2 -> productive water window is age 2-4
    (exactly 3 days), max_yield=6 (2/day if fertilized every day -- the window's full 3 days are needed to
    reach max_yield). A single missed watering DURING the window permanently forfeits that day's yield
    increment -- there is no catch-up mechanic (only one WATER-scored bonus per day, ever).
  - Independently of the window, ANY tile (regardless of crop or age) that goes 2 CONSECUTIVE days unwatered
    is converted to WEED -- a full loss of all accumulated yield_units and the sunk seed cost.
This means "urgent" events (the wheat_water_tier_binding_trace.py signal) plausibly translate into two
different real economic costs the prior harvest-timing trace never tested: (a) permanently reduced final
yield_units on tiles that survive, (b) tile death on tiles that don't. This script measures both directly,
per WHEAT tile, paired treatment (candidates/_probe_wheat_water_tier_1.py) vs baseline (O36_MIN_HANDS2.py).

Method: poll the real farm-tile board every hour (not just decision hours), track every WHEAT PLANT tile by
board position from first sighting to disappearance, record final yield_units and cause (harvested = tile
became None with yield_units drained i.e. was >0 the hour before; died_unwatered = tile became WEED;
other/still-alive-at-game-end = uncounted).

Usage: KAGG_FIXED_SHOPS=1 python3 tools/wheat_watering_yield_outcome_trace.py --seeds 11-30 --opps peter,alaylm,bahaen,yangk
"""
import sys, os, argparse, statistics, importlib.util
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mini_engine as me

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "candidates/O36_MIN_HANDS2.py")
TREAT = os.path.join(ROOT, "candidates/_probe_wheat_water_tier_1.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}


def play_one(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    tracked = {}   # pos -> last-seen yield_units (int)
    harvested_yields = []   # final yield_units at the moment of harvest, per completed wheat planting
    n_died = 0
    n_planted = 0
    while True:
        obs0 = state[0].observation
        tiles = obs0.private_view_placeholder if False else None
        farm = obs0.farms[0] if hasattr(obs0, "farms") else obs0["farms"][0]
        tb = farm["tiles"] if isinstance(farm, dict) else farm.tiles
        board_size = len(tb)
        seen_now = set()
        for y in range(board_size):
            for x in range(board_size):
                t = tb[y][x]
                is_dict = isinstance(t, dict)
                if is_dict and t.get("kind") == "PLANT" and t.get("crop") == "WHEAT":
                    seen_now.add((x, y))
                    if (x, y) not in tracked:
                        n_planted += 1
                    tracked[(x, y)] = t.get("yield_units", 0)
        # anything previously tracked but not seen now has resolved (harvested, died, or decayed away)
        for pos in list(tracked.keys()):
            if pos not in seen_now:
                last_yield = tracked.pop(pos)
                t_now = tb[pos[1]][pos[0]]
                if isinstance(t_now, dict) and t_now.get("kind") == "WEED":
                    n_died += 1
                elif t_now is None:
                    if last_yield > 0:
                        harvested_yields.append(last_yield)
                    # else: last_yield==0 would mean it was harvested with 0 units, shouldn't happen for PLANT
                # else: became something else unexpected (e.g. re-tiled) -- ignore, rare edge case
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    # anything still tracked at game end: still alive, uncounted (neither harvested nor died) -- log separately
    n_alive_at_end = len(tracked)
    return n_planted, n_died, harvested_yields, n_alive_at_end


def _parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-"); out.extend(range(int(lo), int(hi) + 1))
        else:
            out.append(int(part))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", default="11-30")
    ap.add_argument("--opps", default="peter,alaylm,bahaen,yangk")
    args = ap.parse_args()
    seeds = _parse_seeds(args.seeds)
    opp_names = [o.strip() for o in args.opps.split(",")]

    rows = {"baseline": [], "treatment": []}
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for sd in seeds:
            for label, cand in [("baseline", BASE), ("treatment", TREAT)]:
                n_planted, n_died, hy, n_alive = play_one(cand, opp, sd)
                rows[label].append((n_planted, n_died, hy, n_alive))

    for label in ("baseline", "treatment"):
        data = rows[label]
        tot_planted = sum(r[0] for r in data)
        tot_died = sum(r[1] for r in data)
        all_hy = [y for r in data for y in r[2]]
        tot_alive_end = sum(r[3] for r in data)
        n_games = len(data)
        print(f"\n=== {label} -- {n_games} games ===")
        print(f"  total WHEAT plantings: {tot_planted} ({tot_planted/n_games:.2f}/game)")
        print(f"  died (unwatered->WEED): {tot_died} ({100*tot_died/tot_planted:.1f}% of plantings, {tot_died/n_games:.2f}/game)")
        print(f"  harvested: {len(all_hy)} ({100*len(all_hy)/tot_planted:.1f}% of plantings)")
        print(f"  mean yield_units per HARVESTED planting: {statistics.mean(all_hy):.3f}" if all_hy else "  mean yield per harvested: n/a")
        print(f"  mean yield_units per ALL plantings (deaths=0): {sum(all_hy)/tot_planted:.3f}")
        print(f"  still alive at game end (uncounted): {tot_alive_end} ({tot_alive_end/n_games:.2f}/game)")

    # paired per-game deltas on the two headline metrics
    print("\n=== paired deltas (treatment - baseline), per game ===")
    death_rate_deltas = []
    mean_yield_deltas = []
    for (bp, bd, bhy, ba), (tp, td, thy, ta) in zip(rows["baseline"], rows["treatment"]):
        b_rate = bd / bp if bp else 0.0
        t_rate = td / tp if tp else 0.0
        death_rate_deltas.append(t_rate - b_rate)
        b_mean = (sum(bhy) / bp) if bp else 0.0
        t_mean = (sum(thy) / tp) if tp else 0.0
        mean_yield_deltas.append(t_mean - b_mean)
    n = len(death_rate_deltas)
    for name, deltas in [("death_rate (treat-base)", death_rate_deltas), ("mean_yield_per_planting (treat-base)", mean_yield_deltas)]:
        mean = statistics.mean(deltas); sd = statistics.stdev(deltas) if n > 1 else 0.0
        t = mean / (sd / (n ** 0.5)) if sd > 0 else float("nan")
        pos = sum(1 for d in deltas if d > 0); neg = sum(1 for d in deltas if d < 0)
        print(f"  {name}: n={n} mean={mean:+.4f} sd={sd:.4f} t={t:.2f} pos={pos} neg={neg}")
