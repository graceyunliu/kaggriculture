#!/usr/bin/env python3
"""melon_rush binding trace (Sep 12), pre-registered per Grace's spec.

Primary question: does melon_rush capture a genuinely scarce economic opportunity, or merely rearrange
tile turnover? Measured separately, all from real O26_CARROT_SIZING games (only melon_rush toggled) vs
real opponent tapes, seat 0, KAGG_FIXED_SHOPS=1:

1. Price-window capture: for every MELON harvest, record the MELON market price at the turn the tile
   clears (obs.market.prices -- the same dict economy() reads, no reimplementation). Compare mean captured
   price, rush vs baseline, restricted to harvests in the melon_rush-eligible window (age>=10).
2. Avoided yield loss: per-planting realized yield_units at harvest (out of max_yield=6). rush's own
   trigger (yu>=5, age>=10) intentionally forfeits unit 6 whenever it fires before age 12/yu=6 would have --
   measure how often and how much yield is actually given up, not just "harvested earlier."
3. Tile-turnover displacement: for each cleared MELON tile, find the next planting there within
   DISPLACE_WINDOW days (crop type + day offset), and whether the tile stayed idle instead.
4. Net exposed population: the "decisive" subset -- harvests that fire under rush's yu>=5&age>=10 rule
   strictly before baseline's yu>=6-or-age>=12 rule would have -- then sum units*captured_price over just
   that subset in the rush run, and the same population's outcome in the baseline run's harvest that would
   otherwise have happened at that tile, to size the actually-exposed dollar population.

Historical-prior guardrail: melon_rush has an older negative/no-op result on the C1 chassis (Sep 4,
schedule-block batch, kaggriculture-schedule-block-sep04.md). This trace's job is to say whether the
mechanism differs enough on current O36/O26 lineage for that prior to still apply, not to assume either way.

Usage: KAGG_FIXED_SHOPS=1 python3 melon_rush_binding_trace.py --opp bahaen --seeds 71-90 --json out.json
Runs BOTH configs (baseline, rush) per seed/opp in one process so aggregation is a single artifact.
"""
import sys, os, argparse, json, collections, importlib.util
ROOT = "/root/mnt/Kaggriculture" if os.path.isdir("/root/mnt/Kaggriculture") else os.path.expanduser("~/mnt/Kaggriculture")
sys.path.insert(0, ROOT)
import mini_engine as me

CAND = os.path.join(ROOT, "candidates/O26_CARROT_SIZING.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}
MAX_YIELD, FIRST, MAX_DAY = 6, 10, 12
DISPLACE_WINDOW = 3


def load_cand(melon_rush):
    spec = importlib.util.spec_from_file_location(f"cand_{melon_rush}_{id(object())}", CAND)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.KNOBS["melon_rush"] = 1 if melon_rush else 0
    return mod


def run(mod, opp_path, seed):
    engine_mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    opp_agent = me.load_agent(opp_path)

    def cand_agent(obs, configuration):
        try:
            return mod.agent(obs, configuration)
        except Exception:
            return {}

    agents = [cand_agent, opp_agent]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                            "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = engine_mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev_tiles = None
    lives = {}      # pos -> life dict, while a MELON is standing there
    done = []
    plant_events = []   # (day, pos, crop) for every planting event (any crop), for displacement lookup

    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = engine_mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        day = o.day
        tiles = o.farms[0]["tiles"]
        melon_price = o.market["prices"].get("MELON", 0)
        for y, row in enumerate(tiles):
            for x, t in enumerate(row):
                pos = (x, y)
                is_melon = isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("crop") == "MELON"
                pt = prev_tiles[y][x] if prev_tiles is not None else None
                was_melon = isinstance(pt, dict) and pt.get("kind") == "PLANT" and pt.get("crop") == "MELON"
                if is_melon:
                    L = lives.get(pos)
                    if L is None or L["planted_day"] != t["planted_day"]:
                        if L is not None:
                            L["cleared_day"] = day
                            L["capture_price"] = melon_price
                            L["realized_units"] = L["yield_units"]
                            done.append(L)
                        L = {"pos": pos, "planted_day": t["planted_day"], "yield_units": 0, "last_age": 0}
                        lives[pos] = L
                    L["yield_units"] = t.get("yield_units", 0)
                    L["last_age"] = day - t["planted_day"]
                elif was_melon and pos in lives:
                    L = lives.pop(pos)
                    L["cleared_day"] = day
                    L["capture_price"] = melon_price
                    L["realized_units"] = pt.get("yield_units", L["yield_units"])
                    done.append(L)
                if isinstance(t, dict) and t.get("kind") == "PLANT" and t.get("planted_day") == day and not (is_melon and pt is t):
                    plant_events.append((day, pos, t.get("crop")))
        prev_tiles = [[dict(tt) if isinstance(tt, dict) else tt for tt in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    for L in list(lives.values()):
        L.setdefault("cleared_day", None)
        L.setdefault("capture_price", None)
        L.setdefault("realized_units", L["yield_units"])
        done.append(L)

    by_pos = collections.defaultdict(list)
    for d, pos, crop in plant_events:
        by_pos[pos].append((d, crop))
    for L in done:
        L["displaced_by"] = None
        L["displace_lag"] = None
        if L.get("cleared_day") is None:
            continue
        cd = L["cleared_day"]
        cands = sorted((d, crop) for d, crop in by_pos.get(L["pos"], []) if d >= cd and d - cd <= DISPLACE_WINDOW and d != L["planted_day"])
        if cands:
            d0, crop0 = cands[0]
            L["displaced_by"] = crop0
            L["displace_lag"] = d0 - cd
    return done


def is_decisive_rush(L):
    """This planting harvested under rush's condition (yu>=5, age>=FIRST) strictly earlier than baseline's
    (yu>=6 or age>=MAX_DAY) would have fired."""
    if L["cleared_day"] is None:
        return False
    return L["realized_units"] < MAX_YIELD and L["last_age"] < MAX_DAY and L["last_age"] >= FIRST


def summarize(lives, label):
    n = len(lives)
    if n == 0:
        return {"n": 0}
    window = [L for L in lives if L["last_age"] >= FIRST and L["cleared_day"] is not None]
    decisive = [L for L in lives if is_decisive_rush(L)]
    disp = collections.Counter(L["displaced_by"] for L in lives if L["cleared_day"] is not None)
    n_cleared = sum(1 for L in lives if L["cleared_day"] is not None)
    return {
        "n": n,
        "n_cleared": n_cleared,
        "avg_realized_units": sum(L["realized_units"] for L in lives) / n,
        "avg_harvest_age": sum(L["last_age"] for L in lives if L["cleared_day"] is not None) / max(1, n_cleared),
        "avg_capture_price_window": (sum(L["capture_price"] for L in window if L["capture_price"] is not None) /
                                      max(1, sum(1 for L in window if L["capture_price"] is not None))),
        "n_decisive_early": len(decisive),
        "decisive_avg_units": sum(L["realized_units"] for L in decisive) / max(1, len(decisive)),
        "decisive_avg_price": sum(L["capture_price"] for L in decisive if L["capture_price"] is not None) / max(1, len(decisive)),
        "decisive_dollars": sum((L["realized_units"] or 0) * (L["capture_price"] or 0) for L in decisive),
        "displacement": dict(disp),
        "idle_ge1_rate": disp.get(None, 0) / max(1, n_cleared),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--opp", required=True, choices=list(OPPS) + ["all"])
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()
    lo, hi = map(int, args.seeds.split("-"))
    opp_list = list(OPPS) if args.opp == "all" else [args.opp]

    baseline_all, rush_all = [], []
    per_opp = {}
    for opp_key in opp_list:
        opp_path = OPPS[opp_key]
        b_lives, r_lives = [], []
        for seed in range(lo, hi + 1):
            mod_b = load_cand(False)
            b_lives.extend(run(mod_b, opp_path, seed))
            mod_r = load_cand(True)
            r_lives.extend(run(mod_r, opp_path, seed))
        baseline_all.extend(b_lives)
        rush_all.extend(r_lives)
        per_opp[opp_key] = {"baseline": summarize(b_lives, "baseline"), "rush": summarize(r_lives, "rush")}

    result = {
        "opp": args.opp, "seeds": args.seeds,
        "combined_baseline": summarize(baseline_all, "baseline"),
        "combined_rush": summarize(rush_all, "rush"),
        "per_opp": per_opp,
    }
    print(json.dumps(result, indent=2))
    if args.json:
        with open(args.json, "w") as f:
            json.dump(result, f, indent=2)


if __name__ == "__main__":
    main()
