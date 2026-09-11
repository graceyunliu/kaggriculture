#!/usr/bin/env python3
"""Production Allocation Matrix (Sep 11): what each farm asks its crew to do, and what it earns from it -- both farms,
same games, per production line. Observational; a hypothesis generator, not a prescription.

Lines: WHEAT, CARROT, MELON, STRAWBERRY, TOMATO (crops); COW->MILK, SHEEP->WOOL, GOOSE->EGG (animals); FERTILIZER.
Per line and farm (means per game):
  assets        tile-days planted (crops) / animal-days (animals); plantings / animals placed
  oblig         obligations generated (service_ledger classes mapped to the line: water/harvest for crops; feed/care/fert/collect)
  actions       work actions the crew spent on the line's tiles (WATER/HARVEST/PLANT/FERTILIZE on crop tiles; FEED/CARE/COLLECT/HARVEST on animal tiles)
  out_units     units taken off the tile (yield drops on harvest/collect)
  sold, rev     units sold and revenue (SELL orders x quoted price at order time -- approximation, same for both farms)
  cost          direct inputs: seed buys (crop), animal purchase + wheat fed at quoted wheat price (animal), fertilizer buys (FERTILIZER line
                cost is 0; fertilizer USED is charged to the crop it was applied to at the fert price)
  net           rev - cost
  $/oblig, $/action, $/asset-day, share of actions, share of revenue
Labour (hires) is not attributed to lines; it is reported per farm as a total so 'net' is before labour.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/allocation_matrix.py CAND --opp TAPE --seeds 11-14 [--json out.json]
"""
import sys, os, argparse, json, statistics, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "tools"))
import mini_engine as me
TPD = 24

PRODUCT = {"COW": "MILK", "SHEEP": "WOOL", "GOOSE": "EGG"}
LINES = ["WHEAT", "CARROT", "MELON", "STRAWBERRY", "TOMATO", "COW", "SHEEP", "GOOSE", "FERTILIZER"]
CROP_ACTS = {"WATER", "HARVEST", "PLANT", "FERTILIZE"}
ANIM_ACTS = {"FEED", "CARE", "COLLECT_FERTILIZER", "HARVEST"}


def tile_line(t):
    if not isinstance(t, dict): return None
    if "animal" in t: return t["animal"]
    if t.get("kind") == "PLANT": return t["crop"]
    return None


def run(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    M = [{ln: collections.Counter() for ln in LINES} for _ in range(2)]
    tot = [collections.Counter() for _ in range(2)]
    prev_tiles = [None, None]
    # exact market accounting: record every committed unit (the engine's per-unit lockstep) with the farm it belongs to
    trades = []
    orig_commit = mod._commit_unit
    def rec_commit(op, item, price, farm, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok: trades.append((id(farm), op, item, price))
        return ok
    mod._commit_unit = rec_commit
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        acts = []
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act; acts.append(act)
            farm = obs0.farms[i]; prices = obs["market"]["prices"]; shed = obs["private"]["shed"]
            # market orders -> revenue / cost (quoted price at order time; capped by shed stock for sells)
            for m in (act.get("market") or []):
                if not m: continue
                if m[0] == "HIRE":
                    tot[i]["hires"] += 1
            # unit actions -> line attribution (by the tile the unit stands on)
            units = [act.get("farmer") or []] + list(act.get("hands") or [])
            positions = [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]
            for u, ua in enumerate(units):
                if not ua or u >= len(positions): continue
                x, y = positions[u]; t = farm["tiles"][y][x]; ln = tile_line(t)
                v = ua[0]
                if ln in mod.CROPS and v in CROP_ACTS:
                    M[i][ln]["actions"] += 1
                    if v == "FERTILIZE": M[i][ln]["fert_used"] += 1
                elif ln in mod.ANIMALS and v in ANIM_ACTS:
                    M[i][ln]["actions"] += 1
                    if v == "FEED": M[i][ln]["fed"] += 1
                elif v == "PLANT" and len(ua) >= 2 and ua[1] in mod.CROPS:
                    M[i][ua[1]]["actions"] += 1; M[i][ua[1]]["plantings"] += 1
                if v in ("MOVE",): tot[i]["moves"] += 1
                if v in CROP_ACTS | ANIM_ACTS | {"DIG", "DROP", "PICKUP", "PLACE_ANIMAL"}: tot[i]["work"] += 1
                tot[i]["unit_hours"] += 1
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        fid = {id(o.farms[p]): p for p in range(2)}
        for (f, op, item, price) in trades:
            i = fid.get(f)
            if i is None: continue
            if op == "SELL":
                ln = item if item in LINES else {"MILK": "COW", "WOOL": "SHEEP", "EGG": "GOOSE"}.get(item)
                if ln: M[i][ln]["sold"] += 1; M[i][ln]["rev"] += price
            elif op == "BUY_SEED": M[i][item]["cost"] += price
            elif op == "BUY_ANIMAL": M[i][item]["cost"] += price; M[i][item]["bought"] += 1
            elif op == "BUY_PRODUCT": tot[i]["buy_" + item] += price; tot[i]["buy_units_" + item] += 1
            if op == "SELL": tot[i]["revenue"] += price
            else: tot[i]["purchases"] += price
        trades.clear()
        for p in range(2):
            farm = o.farms[p]; tiles = farm["tiles"]
            # outputs: yield drops (harvest / collect), assets: tile-days at h0
            pt = prev_tiles[p]
            for y, row in enumerate(tiles):
                for x, t in enumerate(row):
                    ln = tile_line(t)
                    if pt is not None:
                        q = pt[y][x]; lq = tile_line(q)
                        if lq and (ln != lq or (isinstance(t, dict) and t.get("yield_units", 0) < q.get("yield_units", 0))):
                            drop = q.get("yield_units", 0) - (t.get("yield_units", 0) if ln == lq else 0)
                            if drop > 0: M[p][lq]["out_units"] += drop
                    if ln and o.hour == 0:
                        M[p][ln]["asset_days"] += 1
                        # obligations generated today by this tile (h0 snapshot): animal = feed + care (+ fert if available,
                        # + collect if at cap); ongoing crop = water; one-shot in its yield window = water; ready one-shot = harvest
                        if ln in mod.ANIMALS:
                            M[p][ln]["oblig"] += 2 + (1 if t.get("fertilizer_available") else 0) + (1 if t["yield_units"] >= mod.ANIMALS[ln]["max_held"] else 0)
                        else:
                            cd = mod.CROPS[ln]; age = o.day - t["planted_day"]
                            if cd["ongoing"]:
                                M[p][ln]["oblig"] += 1 + (1 if t["yield_units"] >= cd["max_yield"] else 0)
                            else:
                                ws = (cd["max_yield_day"] + 1) // 2
                                if ws <= age <= cd["max_yield_day"] and t["yield_units"] < cd["max_yield"]: M[p][ln]["oblig"] += 1
                                if t["yield_units"] >= cd["max_yield"] or age >= cd["max_yield_day"]: M[p][ln]["oblig"] += 1
            prev_tiles[p] = [[dict(t) if isinstance(t, dict) else t for t in row] for row in tiles]
        if all(s.status == "DONE" for s in state) or step >= steps: break
    mod._commit_unit = orig_commit
    return [o.farms[p]["money"] for p in range(2)], M, tot


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", default="11-14"); ap.add_argument("--json", default=None)
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    agg = [{ln: collections.Counter() for ln in LINES} for _ in range(2)]; tots = [collections.Counter(), collections.Counter()]; money = [[], []]
    for s in seeds:
        m, M, tot = run(a.cand, a.opp, s)
        for p in range(2):
            money[p].append(m[p]); tots[p].update(tot[p])
            for ln in LINES: agg[p][ln].update(M[p][ln])
    n = len(seeds)
    names = [os.path.basename(a.cand), os.path.basename(a.opp)]
    out = {}
    for p in range(2):
        wheat_p = tots[p]["buy_WHEAT"] / max(1, tots[p]["buy_units_WHEAT"]) if tots[p]["buy_units_WHEAT"] else 30.0
        fert_p = tots[p]["buy_FERTILIZER"] / max(1, tots[p]["buy_units_FERTILIZER"]) if tots[p]["buy_units_FERTILIZER"] else 100.0
        tot_rev = sum(agg[p][ln]["rev"] for ln in LINES); tot_act = sum(agg[p][ln]["actions"] for ln in LINES)
        print(f"\n{names[p]}  (farm {p}, mean money {statistics.mean(money[p]):,.0f}, {n} games; hires {tots[p]['hires']/n:.0f}/game, "
              f"unit-hours {tots[p]['unit_hours']/n:.0f}, work actions {tots[p]['work']/n:.0f}, moves {tots[p]['moves']/n:.0f}; "
              f"wheat bought {tots[p]['buy_units_WHEAT']/n:.0f}u @{wheat_p:.0f}, fert bought {tots[p]['buy_units_FERTILIZER']/n:.0f}u @{fert_p:.0f})")
        print(f"  {'line':10s} {'asset-d':>8s} {'plant/buy':>9s} {'oblig':>6s} {'actions':>8s} {'out_u':>6s} {'sold':>6s} {'rev':>8s} {'cost':>7s} {'net':>8s} {'$/obl':>6s} {'$/act':>6s} {'$/asset-d':>9s} {'act%':>5s} {'rev%':>5s}")
        rows = {}
        for ln in LINES:
            c = agg[p][ln]
            if not any(c.values()): continue
            cost = c["cost"]
            if ln in PRODUCT: cost += c["fed"] * wheat_p          # wheat fed at the quoted wheat price (bought or forgone sale)
            if ln in ("WHEAT", "CARROT", "MELON", "STRAWBERRY", "TOMATO"): cost += c["fert_used"] * fert_p
            rev = c["rev"]; net = rev - cost; act = c["actions"]
            rows[ln] = {k: v / n for k, v in dict(c).items()} | {"cost": cost / n, "net": net / n}
            ob = c["oblig"]
            print(f"  {ln:10s} {c['asset_days']/n:8.0f} {(c['plantings'] or c['bought'])/n:9.0f} {ob/n:6.0f} {act/n:8.0f} {c['out_units']/n:6.0f} {c['sold']/n:6.0f} {rev/n:8.0f} {cost/n:7.0f} {net/n:8.0f} "
                  f"{(net/ob if ob else 0):6.0f} {(net/act if act else 0):6.0f} {(net/c['asset_days'] if c['asset_days'] else 0):9.1f} {100*act/max(1,tot_act):5.1f} {100*rev/max(1,tot_rev):5.1f}")
        out[names[p]] = rows
        rev_t = tots[p]["revenue"] / n; pur = tots[p]["purchases"] / n; dm = statistics.mean(money[p]) - 3000
        print(f"  TOTAL revenue {rev_t:,.0f}  purchases (seed+animal+wheat+fert) {pur:,.0f}  => labour+land (implied) {rev_t - pur - dm:,.0f}  final money delta {dm:,.0f}")
        print(f"  fertilize actions by crop: " + " ".join(f"{ln}:{agg[p][ln]['fert_used']/n:.0f}" for ln in LINES if agg[p][ln]['fert_used']) +
              f"   units per planting: " + " ".join(f"{ln}:{agg[p][ln]['out_units']/agg[p][ln]['plantings']:.1f}" for ln in ("WHEAT","CARROT","MELON","STRAWBERRY") if agg[p][ln]['plantings']))
        print(f"  unit prices realised: " + " ".join(f"{ln}:{agg[p][ln]['rev']/agg[p][ln]['sold']:.0f}" for ln in LINES if agg[p][ln]['sold']))
    if a.json: json.dump(out, open(a.json, "w"), indent=1)
