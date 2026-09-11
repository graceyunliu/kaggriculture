import sys, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT); os.chdir(ROOT)
import mini_engine as me

def run(cand, opp, seed):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    trades = []; orig = mod._commit_unit
    def rec(op, it, price, farm, private, market, shed_capacity=100):
        ok = orig(op, it, price, farm, private, market, shed_capacity)
        if ok: trades.append((op, it, price, id(farm)))
        return ok
    mod._commit_unit = rec
    # per-player: item -> [units, revenue] for SELL, [units, cost] for BUY
    sell = [collections.defaultdict(lambda: [0,0.0]), collections.defaultdict(lambda: [0,0.0])]
    buy  = [collections.defaultdict(lambda: [0,0.0]), collections.defaultdict(lambda: [0,0.0])]
    sell_days = [collections.defaultdict(list), collections.defaultdict(list)]
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        d = state[0].observation.day
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation; fid = {id(o.farms[p]): p for p in range(2)}
        for op, it, price, f in trades:
            p = fid.get(f)
            if p is None: continue
            tbl = sell[p] if op == "SELL" else buy[p]
            tbl[it][0] += 1; tbl[it][1] += price
            if op == "SELL": sell_days[p][it].append(d)
        trades.clear()
        if all(s.status == "DONE" for s in state) or step >= steps: break
    mod._commit_unit = orig
    money = [o.farms[p]["money"] for p in range(2)]
    return money, sell, buy, sell_days

if __name__ == "__main__":
    import sys
    cand = "candidates/O26_CARROT_SIZING.py"
    opp = "Opponents/tape_feeltheagi_107564195.py"
    seeds = list(range(1,11))
    agg_sell = [collections.defaultdict(lambda: [0,0.0]), collections.defaultdict(lambda: [0,0.0])]
    agg_buy  = [collections.defaultdict(lambda: [0,0.0]), collections.defaultdict(lambda: [0,0.0])]
    agg_days = [collections.defaultdict(list), collections.defaultdict(list)]
    moneys = [[],[]]
    for s in seeds:
        money, sell, buy, sd = run(cand, opp, s)
        for p in range(2):
            moneys[p].append(money[p])
            for it,(u,r) in sell[p].items(): agg_sell[p][it][0]+=u; agg_sell[p][it][1]+=r
            for it,(u,r) in buy[p].items(): agg_buy[p][it][0]+=u; agg_buy[p][it][1]+=r
            for it, ds in sd[p].items(): agg_days[p][it].extend(ds)
        print(f"seed {s}: O26 ${money[0]:,.0f}  feeltheagi ${money[1]:,.0f}", file=sys.stderr)

    print(f"\nmean money: O26 ${sum(moneys[0])/len(seeds):,.0f}  feeltheagi ${sum(moneys[1])/len(seeds):,.0f}  margin ${sum(moneys[0])/len(seeds)-sum(moneys[1])/len(seeds):+,.0f}")
    items = sorted(set(list(agg_sell[0])+list(agg_sell[1])))
    print(f"\n{'item':<12} {'O26 units':>9} {'O26 rev':>10} {'O26 avgP':>8} {'O26 day':>7}   {'opp units':>9} {'opp rev':>10} {'opp avgP':>8} {'opp day':>7}   {'rev gap':>9}")
    total_gap = 0
    for it in items:
        u0,r0 = agg_sell[0][it]; u1,r1 = agg_sell[1][it]
        p0 = r0/u0 if u0 else 0; p1 = r1/u1 if u1 else 0
        d0 = sum(agg_days[0][it])/len(agg_days[0][it]) if agg_days[0][it] else 0
        d1 = sum(agg_days[1][it])/len(agg_days[1][it]) if agg_days[1][it] else 0
        gap = (r0-r1)/len(seeds)
        total_gap += gap
        print(f"{it:<12} {u0:>9} {r0/len(seeds):>10,.0f} {p0:>8.1f} {d0:>7.1f}   {u1:>9} {r1/len(seeds):>10,.0f} {p1:>8.1f} {d1:>7.1f}   {gap:>9,.0f}")
    print(f"\nsale revenue gap total (O26 - opp, per game): {total_gap:+,.0f}")

    print(f"\n{'buy item':<12} {'O26 units':>9} {'O26 cost':>10}   {'opp units':>9} {'opp cost':>10}   {'cost gap':>9}")
    buy_gap = 0
    bitems = sorted(set(list(agg_buy[0])+list(agg_buy[1])))
    for it in bitems:
        u0,c0 = agg_buy[0][it]; u1,c1 = agg_buy[1][it]
        gap = (c0-c1)/len(seeds)
        buy_gap += gap
        print(f"{it:<12} {u0:>9} {c0/len(seeds):>10,.0f}   {u1:>9} {c1/len(seeds):>10,.0f}   {gap:>9,.0f}")
    print(f"\nbuy cost gap total (O26 - opp, per game): {buy_gap:+,.0f}  (positive = O26 spends more)")
