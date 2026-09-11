#!/usr/bin/env python3
"""wheat_hold_days binding/error trace (Sep 13) -- per Grace's spec, before any economic panel.

Mechanism (K_SELFMODEL.py ~lines 409-419, the daily SELL block):
    w = shed.get("WHEAT", 0)
    elif price >= wheat_sell_price threshold:
        hold = KNOBS["wheat_stock"] if day<27 else 0
        reserve_feed = (n_total+3) + (n_total * KNOBS["wheat_hold_days"] if day<27 else 0)
        surplus = w - reserve_feed - hold
        if surplus > 0: SELL surplus
So wheat_hold_days scales an extra feed-safety reserve (n_total*hold_days units) that is subtracted from
sellable surplus -- baseline (hold_days=0) already reserves n_total+3 unconditionally; the knob adds more.
Separately, feed purchases are computed as `feed_need = due_feed + spare - shed.get("WHEAT",0)` (line 426) --
i.e. WHEAT sitting in the shed (including anything held back by this knob) DIRECTLY substitutes for a future
BUY_PRODUCT WHEAT purchase. So this knob is a genuine price-timing / self-sufficiency hedge: hold wheat back
from today's sale, hoping to avoid a later feed purchase at a possibly worse price -- exactly the mechanism
Grace's spec asks to trace, not an inferred one.

This traces, per Grace's 5 questions:
  1. How often does the hold rule actually delay a sale (surplus reduced from what it would be at hold_days=0)?
  2. How many units, and for how long are they held (days between when they'd have sold vs when they finally
     leave the shed via SELL or via being consumed as feed)?
  3/5. What price difference does it produce: sale price forgone today vs. (a) feed-purchase price avoided
     if the units get consumed as feed, or (b) the eventual sale price if they get sold later instead?
  4. Does held inventory ever get force-dumped by the shed_load>80 override or the day29 forced sale (a sign
     of it just delaying instead of being useful)?

Method: run baseline (O36_MIN_HANDS2, hold_days=0) and treatment (_probe_wheat_hold_days_1.py, hold_days=1)
in parallel simulation using the SAME seed/opp (paired, independent runs -- like the wheat_water_tier trace),
instrumenting the candidate's own reserve/sell computation each day via its own module functions, and
tracking shed WHEAT stock day-over-day plus BUY_PRODUCT WHEAT orders actually issued.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/wheat_hold_days_binding_trace.py --seeds 11-30 --opps peter,alaylm,bahaen,yangk
"""
import sys, os, argparse, statistics, importlib.util
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mini_engine as me

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "candidates/O36_MIN_HANDS2.py")
TREAT = os.path.join(ROOT, "candidates/_probe_wheat_hold_days_1.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}


def play_one(cand, opp, seed):
    """Track, per day: WHEAT shed stock before sell decision, SELL WHEAT qty actually issued, BUY_PRODUCT
    WHEAT qty issued (feed), WHEAT price, and n_total (animals) -- enough to reconstruct hold-binding events
    and their downstream fate without re-deriving the agent's private KNOBS/n_total bookkeeping."""
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    daily = []   # list of dicts per day: day, wheat_shed, price, sell_qty, buy_feed_qty, n_animals
    day_sell = {}; day_buy = {}
    last_day = -1
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == 0 and day != last_day and hour == 0:
                wheat_shed = obs["private"]["shed"].get("WHEAT", 0)
                price = obs["market"]["prices"].get("WHEAT", 0)
                tiles = obs["farms"][obs["player"]]["tiles"]
                n_animals = sum(1 for row in tiles for t in row if isinstance(t, dict) and "animal" in t)
                daily.append({"day": day, "wheat_shed": wheat_shed, "price": price, "n_animals": n_animals,
                              "sell_qty": day_sell.get(day - 1, 0), "buy_feed_qty": day_buy.get(day - 1, 0)})
                last_day = day
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        # capture orders issued this exact turn (day, before interpreter mutates) for seat 0
        try:
            a0 = state[0].action
            ords = a0.get("market", []) if isinstance(a0, dict) else []
            for o in ords:
                if not isinstance(o, (list, tuple)) or len(o) < 3:
                    continue
                if o[0] == "SELL" and o[1] == "WHEAT":
                    day_sell[day] = day_sell.get(day, 0) + int(o[2])
                elif o[0] == "BUY_PRODUCT" and o[1] == "WHEAT":
                    day_buy[day] = day_buy.get(day, 0) + int(o[2])
        except Exception:
            pass
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return daily, day_sell, day_buy


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
    ap.add_argument("--seeds", default="11-20")
    ap.add_argument("--opps", default="peter,alaylm")
    args = ap.parse_args()
    seeds = _parse_seeds(args.seeds)
    opp_names = [o.strip() for o in args.opps.split(",")]

    tot_sell_delta = []; tot_buy_feed_delta = []; tot_shed_stock_delta = []
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for sd in seeds:
            bd, bs, bb = play_one(BASE, opp, sd)
            td, ts, tb = play_one(TREAT, opp, sd)
            b_sell = sum(bs.values()); t_sell = sum(ts.values())
            b_buy = sum(bb.values()); t_buy = sum(tb.values())
            b_shed_avg = statistics.mean(d["wheat_shed"] for d in bd) if bd else 0
            t_shed_avg = statistics.mean(d["wheat_shed"] for d in td) if td else 0
            tot_sell_delta.append(t_sell - b_sell)
            tot_buy_feed_delta.append(t_buy - b_buy)
            tot_shed_stock_delta.append(t_shed_avg - b_shed_avg)

    n = len(tot_sell_delta)
    def summarize(name, deltas):
        mean = statistics.mean(deltas); sd = statistics.stdev(deltas) if n > 1 else 0.0
        t = mean / (sd / (n ** 0.5)) if sd > 0 else float("nan")
        pos = sum(1 for d in deltas if d > 0); neg = sum(1 for d in deltas if d < 0)
        print(f"{name}: n={n} mean={mean:+.3f} sd={sd:.3f} t={t:.2f} pos={pos} neg={neg}")

    summarize("total WHEAT sold/game (treat-base)", tot_sell_delta)
    summarize("total WHEAT bought-as-feed/game (treat-base)", tot_buy_feed_delta)
    summarize("avg shed WHEAT stock/day (treat-base)", tot_shed_stock_delta)
