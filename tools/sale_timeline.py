#!/usr/bin/env python3
"""Sale timeline for one item, both farms (Sep 11): every committed SELL unit (day, hour, price) via the engine's
per-unit lockstep, plus harvest (yield-drop) events for the item's crop, so 'who sells first at what price' is visible.
Usage: KAGG_FIXED_SHOPS=1 python3 tools/sale_timeline.py CAND --opp TAPE --seed 11 --item MELON"""
import sys, os, argparse, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me
CROP_OF = {"MILK": "COW", "WOOL": "SHEEP", "EGG": "GOOSE"}

def run(cand, opp, seed, item):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    trades = []; orig = mod._commit_unit
    def rec(op, it, price, farm, private, market, shed_capacity=100):
        ok = orig(op, it, price, farm, private, market, shed_capacity)
        if ok and op == "SELL" and it == item: trades.append((id(farm), price))
        return ok
    mod._commit_unit = rec
    sells = [collections.defaultdict(list), collections.defaultdict(list)]   # (day,hour) -> prices
    harv = [collections.Counter(), collections.Counter()]                     # day -> units harvested
    shed_item = [collections.Counter(), collections.Counter()]                # day -> shed stock at h0
    prev = [None, None]; crop = CROP_OF.get(item, item)
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if obs["hour"] == 0: shed_item[i][obs["day"]] = obs["private"]["shed"].get(item, 0)
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        d, h = state[0].observation.day, state[0].observation.hour
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation; fid = {id(o.farms[p]): p for p in range(2)}
        for f, price in trades:
            p = fid.get(f)
            if p is not None: sells[p][(d, h)].append(price)
        trades.clear()
        for p in range(2):
            tiles = o.farms[p]["tiles"]
            if prev[p] is not None:
                for y, row in enumerate(tiles):
                    for x, t in enumerate(row):
                        q = prev[p][y][x]
                        ql = (q.get("animal") or q.get("crop")) if isinstance(q, dict) else None
                        if ql == crop:
                            tl = (t.get("animal") or t.get("crop")) if isinstance(t, dict) else None
                            drop = q.get("yield_units", 0) - (t.get("yield_units", 0) if tl == crop else 0)
                            if drop > 0: harv[p][(d, h)] += drop
            prev[p] = [[dict(t) if isinstance(t, dict) else t for t in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    mod._commit_unit = orig
    return [o.farms[p]["money"] for p in range(2)], sells, harv, shed_item

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True); ap.add_argument("--seed", type=int, default=11); ap.add_argument("--item", default="MELON")
    a = ap.parse_args(); os.chdir(ROOT)
    money, sells, harv, shed = run(a.cand, a.opp, a.seed, a.item)
    names = [os.path.basename(a.cand), os.path.basename(a.opp)]
    for p in range(2):
        print(f"\n{names[p]} money {money[p]:,.0f}  {a.item}: harvested by day/hour " + " ".join(f"d{d}h{h}:{n}" for (d, h), n in sorted(harv[p].items())))
        tot_u = sum(len(v) for v in sells[p].values()); tot_r = sum(sum(v) for v in sells[p].values())
        print(f"  sells ({tot_u}u, ${tot_r:,.0f}, avg {tot_r/max(1,tot_u):.0f}): " + " ".join(f"d{d}h{h}:{len(v)}u@{sum(v)/len(v):.0f}" for (d, h), v in sorted(sells[p].items())))
        print(f"  shed {a.item} at h0: " + " ".join(f"d{d}:{n}" for d, n in sorted(shed[p].items()) if n))
