#!/usr/bin/env python3
"""DEMAND_SHARE calibration trace (Sep 12 discovery-phase, step 1 of Grace's calibration sequence).

candidates/K_SELFMODEL.py line ~91 hard-codes DEMAND_SHARE=0.5 as "my share of daily town demand (two
sellers)" and uses it to size the crop-seed pool at BUY_SEED time (line ~589: pool = DEMAND_SHARE * (...)).
This is a DIFFERENT constant from KNOBS["demand_share"]=0.55 (used only for animal _demand_room sizing,
already knob-swept and closed ABANDON at 0.65 -- see kaggriculture-knob-sweep-min-hands-do-sep11). The crop
constant has never been checked.

Method: realized share = my units SOLD of a crop / (my units sold + opponent units sold) of that same crop,
over the same games -- the most direct empirical read of "what fraction of the two-seller market did each
side actually capture", split into three day-phases (early 0-9, mid 10-19, late 20-29) since the assumed
0.5 is a single flat number applied at every planting decision regardless of phase. Reuses the SAME trade
recording as allocation_matrix.py (same engine driving code) but buckets by day at time of trade.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/demand_share_trace.py CAND --opp TAPE --seeds 11-30
"""
import sys, os, statistics, collections, argparse
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me

CROPS = ["WHEAT", "CARROT", "MELON", "STRAWBERRY", "TOMATO"]
PHASES = [("early", 0, 9), ("mid", 10, 19), ("late", 20, 29)]


def phase_of(day):
    for name, lo, hi in PHASES:
        if lo <= day <= hi: return name
    return "late"


def run(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    sold = collections.Counter()  # (farm_idx, crop, phase) -> units sold
    trades = []
    orig_commit = mod._commit_unit
    def rec(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok and op == "SELL" and item in CROPS: trades.append((id(farm), item, 1))
        return ok
    mod._commit_unit = rec
    while True:
        obs0 = state[0].observation; day = obs0.day
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        fid = {id(o.farms[p]): p for p in range(2)}
        ph = phase_of(day)
        for f, item, n in trades:
            i = fid.get(f)
            if i is not None: sold[(i, item, ph)] += n
        trades.clear()
        if all(s.status == "DONE" for s in state) or step >= steps: break
    mod._commit_unit = orig_commit
    return sold


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
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", default="11-30")
    a = ap.parse_args(); os.chdir(ROOT)
    seeds = _parse_seeds(a.seeds)
    agg = collections.Counter()
    for s in seeds:
        sold = run(a.cand, a.opp, s)
        agg.update(sold)
    print(f"cand={a.cand} opp={a.opp} seeds={a.seeds} (assumed DEMAND_SHARE=0.5)\n")
    print(f"{'crop':10s} {'phase':6s} {'my_units':>9s} {'opp_units':>10s} {'realized_share':>15s}")
    for c in CROPS:
        for ph, _, _ in PHASES:
            mine = agg[(0, c, ph)]; opp = agg[(1, c, ph)]
            tot = mine + opp
            share = mine / tot if tot else float("nan")
            print(f"{c:10s} {ph:6s} {mine:9d} {opp:10d} {share:15.2f}" if tot else f"{c:10s} {ph:6s} {mine:9d} {opp:10d} {'n/a (no sales)':>15s}")
        mine_all = sum(agg[(0, c, ph)] for ph, _, _ in PHASES); opp_all = sum(agg[(1, c, ph)] for ph, _, _ in PHASES)
        tot_all = mine_all + opp_all
        share_all = mine_all / tot_all if tot_all else float("nan")
        print(f"{c:10s} {'ALL':6s} {mine_all:9d} {opp_all:10d} {share_all:15.2f}\n")
