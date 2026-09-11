#!/usr/bin/env python3
"""Melon commitment recoverability trace (Sep 11, ledger DELAY `melon_commitment_recoverability`).

Two candidates on the SAME seed/tape (e.g. O26 vs O32): for every melon tile, record its life -- planted day, yield
by day, claim state inside the melon window (S["melon_claim"]), the hour it was harvested (yield drop) and how many
units, when those units reached the shed and were sold, and its terminal state (harvested / rotted to WEED / still
standing at game end). Then diff the two runs tile by tile: the 8-11 "lost" units per game must be one of
  harvest_lost   -- tile rotted (engine: yield decays from (planted+max_day+1)*24, then WEED) or never harvested
  units_lost     -- harvested but with fewer units (harvested past max, or before 6)
  sale_lost      -- harvested but units never reached the shed / never sold (auto-drop at night, deadline)
  none           -- same units, different hour (a timing shift, not a loss)
Usage: KAGG_FIXED_SHOPS=1 python3 tools/melon_trace.py candidates/O26_CARROT_SIZING.py candidates/O32_MELON_URGENT_EXEMPT.py --opp Opponents/tape_bahaenes_106828159.py --seed 151
"""
import sys, os, argparse, importlib.util, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import mini_engine as me


def load_mod(path):
    spec = importlib.util.spec_from_file_location("mt_" + os.path.basename(path).replace(".", "_"), path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def run(cand, opp, seed):
    eng, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); cmod = load_mod(cand); agents = [cmod.agent, me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = eng.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    tiles = {}          # (pos, planted_day) -> record
    sells = []          # (day, hour, price) melon sells by us
    orig = eng._commit_unit
    def rec(op, it, price, farm, private, market, shed_capacity=100):
        ok = orig(op, it, price, farm, private, market, shed_capacity)
        if ok and op == "SELL" and it == "MELON": sells.append((id(farm), price))
        return ok
    eng._commit_unit = rec
    prev = None; shed_hist = []; carry_hist = []
    while True:
        o0 = state[0].observation; d, h = o0.day, o0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        # claim state after our agent ran this turn
        mc = dict(cmod.S.get("melon_claim", {})); claims = {v: k for k, v in mc.items() if k != "day"}
        obsn = state[0].observation
        farm = obsn.farms[0]
        shed_hist.append((d, h, obsn.private["shed"].get("MELON", 0)))
        carry_hist.append((d, h, sum(b.get("MELON", 0) for b in (obsn.private.get("inventories") or []))))
        for y, row in enumerate(farm["tiles"]):
            for x, t in enumerate(row):
                if isinstance(t, dict) and t.get("crop") == "MELON":
                    k = ((x, y), t["planted_day"])
                    r = tiles.setdefault(k, {"pos": (x, y), "planted": t["planted_day"], "yield_by_day": {}, "claims": [], "harvest": None, "units": 0, "end": None})
                    r["yield_by_day"][d] = t["yield_units"]
                    if (x, y) in claims and 9 <= d <= 14 and h <= 12:
                        r["claims"].append((d, h, claims[(x, y)]))
        state = eng.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation; fid = {id(o.farms[p]): p for p in range(2)}
        for f, price in sells:
            if fid.get(f) == 0: pass
        sells_ours = [(d, h, p) for f, p in sells if fid.get(f) == 0]; sells.clear()
        for e in sells_ours: pass
        run.sold = getattr(run, "sold", []) ; run.sold += sells_ours
        farm = o.farms[0]
        if prev is not None:
            for y, row in enumerate(farm["tiles"]):
                for x, t in enumerate(row):
                    q = prev[y][x]
                    if isinstance(q, dict) and q.get("crop") == "MELON":
                        k = ((x, y), q["planted_day"]); r = tiles.get(k)
                        if r is None: continue
                        same = isinstance(t, dict) and t.get("crop") == "MELON" and t.get("planted_day") == q["planted_day"]
                        if same and t["yield_units"] < q["yield_units"] and r["harvest"] is None:
                            r["harvest"] = (d, h); r["units"] += q["yield_units"] - t["yield_units"]
                        elif not same:
                            if isinstance(t, dict) and t.get("kind") == "WEED":
                                r["end"] = ("weed", d, h, q["yield_units"])
                            elif r["harvest"] is None:
                                r["harvest"] = (d, h); r["units"] += q["yield_units"]; r["end"] = ("harvested", d, h)
                            else:
                                r["end"] = r["end"] or ("harvested", d, h)
        prev = [[dict(t) if isinstance(t, dict) else t for t in row] for row in farm["tiles"]]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    eng._commit_unit = orig
    for r in tiles.values():
        if r["end"] is None: r["end"] = ("standing_at_end",) if r["harvest"] is None else ("harvested",) + r["harvest"]
    sold = getattr(run, "sold", []); run.sold = []
    return o.farms[0]["money"], tiles, sold, shed_hist, carry_hist


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--opp", required=True); ap.add_argument("--seed", type=int, default=151)
    a = ap.parse_args(); os.chdir(ROOT)
    res = {}
    for c in (a.a, a.b):
        money, tiles, sold, shed, carry = run(c, a.opp, a.seed)
        res[c] = (money, tiles, sold, shed, carry)
        n_sold = len(sold); rev = sum(p for _, _, p in sold)
        print(f"\n{os.path.basename(c)}  money {money:,.0f}  melon tiles {len(tiles)}  harvested units {sum(r['units'] for r in tiles.values())}  sold {n_sold}u ${rev:,.0f}")
        by_end = collections.Counter(r["end"][0] for r in tiles.values()); print("  terminal:", dict(by_end))
        print("  sells:", " ".join(f"d{d}h{h}:${p:.0f}" for d, h, p in sold[:40]))
    A, B = res[a.a][1], res[a.b][1]
    print(f"\n== tile diff ({os.path.basename(a.a)} -> {os.path.basename(a.b)}) ==")
    for k in sorted(set(A) | set(B)):
        ra, rb = A.get(k), B.get(k)
        if ra is None or rb is None:
            print(f"  {k}: only in {'A' if ra else 'B'}"); continue
        if ra["units"] != rb["units"] or ra["end"][0] != rb["end"][0] or ra["harvest"] != rb["harvest"]:
            print(f"  tile {k[0]} planted d{k[1]}: A harvest {ra['harvest']} {ra['units']}u end {ra['end']} | B harvest {rb['harvest']} {rb['units']}u end {rb['end']}")
            ya = ra["yield_by_day"]; yb = rb["yield_by_day"]
            print(f"      yield A d8-13: {[ya.get(d) for d in range(8, 14)]}  B: {[yb.get(d) for d in range(8, 14)]}")
            print(f"      claims A: {ra['claims'][:8]}  B: {rb['claims'][:8]}")
