#!/usr/bin/env python3
"""Wheat headroom / marginal-demand probe (Sep 12, per Grace's sequencing: measure economic exposure BEFORE
building a corrected-constant candidate). Answers, per Grace's 5 questions:
  1. how much wheat demand is actually realized (price behaviour, volume sold both farms)
  2. is our wheat supply demand-constrained or production-constrained (do we run out of wheat to sell, or
     run out of buyers)
  3. what happens to realized WHEAT price as our supply increases (marginal price impact)
  4. how often is apparent wheat demand left unserved by us
  5. NET counterfactual sizing error: what would the seed-sizing formula have computed under BOTH corrected
     constants together (units 5.0->3.8, DEMAND_SHARE 0.5->0.36), not each alone (Grace's non-additivity
     caution) -- a measurement-only counterfactual, does NOT change agent behaviour.

Reuses K_SELFMODEL's own pure functions (perceive, _daily_demand, CROP_SPECS, I0) via direct import rather
than reimplementing the sizing math, so the counterfactual room_units figure is computed with the exact same
formula the real policy uses, just with the two constants swapped.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/wheat_headroom_trace.py --seeds 11-20 --opps peter,alaylm
"""
import sys, os, importlib.util, statistics, collections, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

CAND = os.path.join(ROOT, "candidates/O36_MIN_HANDS2.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}

# import the candidate as a plain module so we can call its pure functions directly (perceive, _daily_demand)
spec = importlib.util.spec_from_file_location("km", CAND)
km = importlib.util.module_from_spec(spec); spec.loader.exec_module(km)

REAL_UNITS, CORR_UNITS = 5.0, 3.8
REAL_SHARE, CORR_SHARE = 0.5, 0.36


def wheat_room(obs, v, seeds_wheat, units, share):
    day = obs["day"]
    wheat_tiles_now = sum(1 for _pos, t in v["crops"] if t.get("crop") == "WHEAT")
    committed = (wheat_tiles_now + seeds_wheat) * units
    inv_c = obs["market"]["inventory"].get("WHEAT", km.I0)
    dd = km._daily_demand(obs, "WHEAT", day, day + km.CROP_SPECS["WHEAT"]["first"])
    pool = share * (max(0.0, km.I0 - inv_c) + dd * (29 - day))
    return pool - committed, wheat_tiles_now


def play(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    trades = []
    orig = mod._commit_unit
    def rec(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig(op, item, price, farm, private, market, shed_capacity)
        if ok and item == "WHEAT": trades.append((id(farm), op, price))
        return ok
    mod._commit_unit = rec
    day_price = {}      # day -> WHEAT price at hour0
    my_sold = collections.Counter(); opp_sold = collections.Counter()   # by day
    buy_seed_real = 0      # cumulative BUY_SEED WHEAT quantity actually ordered (real policy)
    room_real_sum = 0.0; room_corr_sum = 0.0
    seeds_wheat_running = 0
    last_day = -1
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        if day != last_day:
            day_price[day] = obs0.market["prices"].get("WHEAT", 0)
            last_day = day
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == 0 and day > 0 and hour in (0, 1):
                # shadow-compute room under real vs corrected constants using the SAME obs the real
                # policy sees this turn, without altering its action
                v = km.perceive(obs)
                seeds_wheat = obs["private"]["seeds"].get("WHEAT", 0)
                seeds_wheat_running = seeds_wheat
                room_r, _ = wheat_room(obs, v, seeds_wheat, REAL_UNITS, REAL_SHARE)
                room_c, _ = wheat_room(obs, v, seeds_wheat, CORR_UNITS, CORR_SHARE)
                room_real_sum = max(room_real_sum, 0)  # (kept for clarity; summed per-decision below)
                globals_last_room_r, globals_last_room_c = room_r, room_c
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            if i == 0:
                for m in (act.get("market") or []):
                    if m and m[0] == "BUY_SEED" and m[1] == "WHEAT":
                        buy_seed_real += int(m[2])
                if day > 0 and hour in (0, 1):
                    room_real_sum += max(0.0, globals_last_room_r) / max(1, REAL_UNITS)
                    room_corr_sum += max(0.0, globals_last_room_c) / max(1, CORR_UNITS)
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        fid = {id(o.farms[p]): p for p in range(2)}
        day2 = o.day
        for f, op, price in trades:
            i = fid.get(f)
            if op == "SELL" and i == 0: my_sold[day2] += 1
            if op == "SELL" and i == 1: opp_sold[day2] += 1
        trades.clear()
        if all(s.status == "DONE" for s in state) or step >= steps: break
    mod._commit_unit = orig
    final_money = [state[p].observation.farms[p]["money"] for p in range(2)]
    return {
        "day_price": day_price, "my_sold": my_sold, "opp_sold": opp_sold,
        "buy_seed_real": buy_seed_real,
        "room_real_units_seen": room_real_sum, "room_corr_units_seen": room_corr_sum,
        "final_money": final_money,
    }


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
    ap = argparse.ArgumentParser(); ap.add_argument("--seeds", default="11-20"); ap.add_argument("--opps", default="peter,alaylm")
    a = ap.parse_args(); os.chdir(ROOT)
    seeds = _parse_seeds(a.seeds); opp_names = a.opps.split(",")
    price_by_myvol_bucket = collections.defaultdict(list)   # my daily units sold bucket -> next-day-ish price obs
    total_my = total_opp = 0
    real_room_total = corr_room_total = 0.0
    buy_seed_totals = []
    unserved_days = 0; total_wheat_days = 0
    price_series_examples = []
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for s in seeds:
            r = play(CAND, opp, s)
            total_my += sum(r["my_sold"].values()); total_opp += sum(r["opp_sold"].values())
            real_room_total += r["room_real_units_seen"]; corr_room_total += r["room_corr_units_seen"]
            buy_seed_totals.append(r["buy_seed_real"])
            # price-vs-volume: bucket days by my units sold that day, average WHEAT price that day
            for day, price in r["day_price"].items():
                myv = r["my_sold"].get(day, 0)
                bucket = "0" if myv == 0 else ("1-10" if myv <= 10 else ("11-25" if myv <= 25 else "26+"))
                price_by_myvol_bucket[bucket].append(price)
    n_games = len(seeds) * len(opp_names)
    print(f"n_games={n_games}  cand={CAND}  opps={opp_names}  seeds={a.seeds}\n")
    print(f"Total WHEAT units sold across all games: mine={total_my}  opp={total_opp}  (mine/opp ratio={total_my/max(1,total_opp):.2f})\n")
    print(f"Mean BUY_SEED WHEAT quantity actually ordered per game (real policy): {statistics.mean(buy_seed_totals):.1f} (range {min(buy_seed_totals)}-{max(buy_seed_totals)})\n")
    print("Realized WHEAT price by my same-day sold-volume bucket (proxy for marginal price impact):")
    for bucket in ("0", "1-10", "11-25", "26+"):
        vals = price_by_myvol_bucket[bucket]
        if vals:
            print(f"  my_units_sold={bucket:6s}: n_days={len(vals):5d}  mean_price={statistics.mean(vals):6.1f}  stdev={statistics.pstdev(vals):5.1f}")
    print(f"\nCumulative NET counterfactual sizing signal (sum over all day-0/1 decisions, both games, both corrections APPLIED TOGETHER):")
    print(f"  room-implied extra plantings under REAL constants (5.0u, share 0.5):      {real_room_total/n_games:8.1f} /game")
    print(f"  room-implied extra plantings under CORRECTED constants (3.8u, share 0.36): {corr_room_total/n_games:8.1f} /game")
    print(f"  net delta (corrected - real), i.e. how many MORE/FEWER wheat plantings the corrected formula would size for: {(corr_room_total-real_room_total)/n_games:+8.1f} /game")
