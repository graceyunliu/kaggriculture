#!/usr/bin/env python3
"""Marginal consequence of a one-hour delay, measured by counterfactual (Sep 10).

Against a deterministic tape the whole game is deterministic, so: run the base game and record every work action
(step, unit, verb, tile, state features). Sample events; for each, replay the game identically up to that step,
force THAT unit to PASS on that step (a one-hour delay of that exact action), let the unchanged policy play on,
and record final money. delta = cf_money - base_money is the exact consequence of delaying that action one hour.
Aggregated by (verb, state bucket) this is the empirical "value at risk per hour" the orchestrator should use.

Usage: python3 tools/delay_counterfactual.py CAND OPP --seed 1 --sample 80 [--verbs WATER,HARVEST,FEED,...]
"""
import sys, argparse, random
sys.path.insert(0, "/sessions/confident-jolly-fermat/mnt/Kaggriculture")
import mini_engine as me
WORK = {"WATER", "HARVEST", "PLANT", "FEED", "CARE", "COLLECT_FERTILIZER", "FERTILIZE", "DIG", "DROP"}

def bucket(verb, t, day, hour, carry):
    """State bucket for an action on tile t (dict or None)."""
    if verb == "WATER" and isinstance(t, dict):
        c = t.get("crop"); cu = t.get("consecutive_unwatered", 0)
        age = day - t.get("planted_day", day)
        ongoing = c in ("STRAWBERRY", "TOMATO")
        return f"WATER/{'ongoing' if ongoing else 'oneshot'}/cu{min(cu,1)}"
    if verb == "HARVEST" and isinstance(t, dict):
        if "animal" in t:
            return "HARVEST/animal"
        c = t.get("crop"); age = day - t.get("planted_day", day)
        md = {"WHEAT": 4, "CARROT": 3, "MELON": 12}.get(c)
        if md is None:
            return f"HARVEST/{c}"
        return f"HARVEST/{c}/{'at_maxday' if age >= md else 'early'}"
    if verb == "FEED" and isinstance(t, dict):
        return f"FEED/cu{min(t.get('consecutive_unfed',0),1)}"
    if verb == "CARE":
        return "CARE"
    if verb == "COLLECT_FERTILIZER":
        return "COLLECT"
    if verb == "PLANT":
        return f"PLANT/{'early' if day < 12 else 'mid' if day < 22 else 'late'}"
    if verb == "DROP":
        return f"DROP/{'eve' if hour >= 18 else 'day'}"
    return verb

PRICE_FALLBACK = {"MILK": 160, "WOOL": 200, "STRAWBERRY": 120, "MELON": 250, "TOMATO": 60, "CARROT": 35, "WHEAT": 25, "EGG": 50, "FERTILIZER": 100}
ANIMAL_VALUE = {"COW": 400, "SHEEP": 500, "GOOSE": 300}

def networth(obs0, priv):
    """Short-horizon consequence proxy: cash + shed & carried goods at current price + standing yield at price + live animals."""
    farm = obs0.farms[0]; prices = dict(obs0.market["prices"])
    val = farm["money"]
    for k, n in dict(priv["shed"]).items():
        if k in ANIMAL_VALUE: val += ANIMAL_VALUE[k] * n
        elif n > 0: val += prices.get(k, PRICE_FALLBACK.get(k, 0)) * n
    for bag in (priv.get("inventories") or []):
        for k, n in bag.items():
            if k in ANIMAL_VALUE: val += ANIMAL_VALUE[k] * n
            elif n > 0: val += prices.get(k, PRICE_FALLBACK.get(k, 0)) * n
    for row in farm["tiles"]:
        for t in row:
            if not isinstance(t, dict): continue
            if "animal" in t:
                val += ANIMAL_VALUE.get(t["animal"], 300) + t.get("yield_units", 0) * prices.get({"COW": "MILK", "SHEEP": "WOOL", "GOOSE": "EGG"}.get(t["animal"], ""), 100)
            elif t.get("kind") == "PLANT":
                val += t.get("yield_units", 0) * prices.get(t.get("crop"), PRICE_FALLBACK.get(t.get("crop"), 0))
    return val

def play(cand, opp, seed, force=None, record=None, stop_at=None):
    """force=(step, unit) -> that unit PASSes on that step. record: list to append (step, unit, verb, bucket)."""
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            if i == 0:
                units = [act.get("farmer") or []] + list(act.get("hands") or [])
                if record is not None:
                    farm = obs0.farms[0]
                    positions = [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]
                    inv = obs["private"].get("inventories") or []
                    for u, ua in enumerate(units):
                        if ua and ua[0] in WORK and u < len(positions):
                            x, y = positions[u]; t = farm["tiles"][y][x]
                            record.append((step, u, ua[0], bucket(ua[0], t, day, hour, inv[u] if u < len(inv) else {}), day, hour))
                if force is not None and force[0] == step:
                    u = force[1]
                    if u == 0: act["farmer"] = ["PASS"]
                    elif u - 1 < len(act.get("hands") or []): act["hands"][u - 1] = ["PASS"]
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if stop_at is not None and step >= stop_at:
            return networth(state[0].observation, state[0].observation.private)
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return state[0].observation.farms[0]["money"]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("opp")
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--sample", type=int, default=60)
    ap.add_argument("--verbs", default="WATER,HARVEST,FEED,CARE,COLLECT_FERTILIZER,PLANT,DROP")
    ap.add_argument("--maxday", type=int, default=27)
    ap.add_argument("--buckets", default=None, help="comma list of bucket prefixes to test")
    ap.add_argument("--json", default=None, help="append per-event results to this jsonl")
    ap.add_argument("--horizon", type=int, default=48, help="steps after the delayed action at which net worth is compared (0 = final money)")
    a = ap.parse_args()
    rec = []
    base = play(a.cand, a.opp, a.seed, record=rec)
    verbs = set(a.verbs.split(","))
    pool = [r for r in rec if r[2] in verbs and r[4] <= a.maxday and r[4] >= 2]
    if a.buckets:
        pre = a.buckets.split(",")
        pool = [r for r in pool if any(r[3].startswith(px) for px in pre)]
    random.seed(a.seed)
    # stratified: equal share per bucket where possible
    by_b = {}
    for r in pool: by_b.setdefault(r[3], []).append(r)
    per = max(1, a.sample // max(1, len(by_b)))
    sample = []
    for b, lst in by_b.items():
        random.shuffle(lst); sample += lst[:per]
    print(f"base money {base:.0f}; {len(rec)} work events, {len(by_b)} buckets, testing {len(sample)} delays", flush=True)
    out = {}
    import json
    for (step, u, verb, b, day, hour) in sample:
        if a.horizon > 0:
            base_h = play(a.cand, a.opp, a.seed, stop_at=step + a.horizon)
            cf = play(a.cand, a.opp, a.seed, force=(step, u), stop_at=step + a.horizon)
            d = cf - base_h
        else:
            cf = play(a.cand, a.opp, a.seed, force=(step, u)); d = cf - base
        out.setdefault(b, []).append(d)
        if a.json:
            open(a.json, "a").write(json.dumps({"seed": a.seed, "step": step, "unit": u, "verb": verb, "bucket": b, "day": day, "hour": hour, "delta": d, "horizon": a.horizon}) + "\n")
    print(f"{'bucket':30s} {'n':>3s} {'mean':>8s} {'median':>8s} {'min':>8s} {'max':>8s}  frac<-50")
    for b, ds in sorted(out.items(), key=lambda kv: sum(kv[1]) / len(kv[1])):
        ds_s = sorted(ds); n = len(ds)
        print(f"{b:30s} {n:3d} {sum(ds)/n:8.0f} {ds_s[n//2]:8.0f} {ds_s[0]:8.0f} {ds_s[-1]:8.0f}  {sum(1 for d in ds if d < -50)/n:.2f}")
