#!/usr/bin/env python3
"""wheat_hold_days -- dollar-level consequence trace (Sep 13), extending wheat_hold_days_binding_trace.py's
quantity finding (treatment sells ~51 fewer WHEAT units/game, buys ~32 fewer as feed/game, both t>7, highly
consistent) into an actual price comparison, per Grace's question "what price difference does the delay
actually produce."

Uses the same sell/buy multipliers the candidate's own revenue_est/wheat_cost math uses (sell*0.9, buy*1.15
-- K_SELFMODEL.py lines ~408-419/427) so the dollar figures are on the same basis the policy itself reasons
about, not an invented external price.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/wheat_hold_days_dollar_trace.py --seeds 11-30 --opps peter,alaylm,bahaen,yangk
"""
import sys, os, argparse, statistics
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
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    sell_revenue = 0.0; feed_cost = 0.0
    last_price = {"WHEAT": 25}
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == 0:
                last_price["WHEAT"] = obs["market"]["prices"].get("WHEAT", last_price["WHEAT"])
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        try:
            a0 = state[0].action
            ords = a0.get("market", []) if isinstance(a0, dict) else []
            for o in ords:
                if not isinstance(o, (list, tuple)) or len(o) < 3:
                    continue
                if o[0] == "SELL" and o[1] == "WHEAT":
                    sell_revenue += int(o[2]) * last_price["WHEAT"] * 0.9
                elif o[0] == "BUY_PRODUCT" and o[1] == "WHEAT":
                    feed_cost += int(o[2]) * last_price["WHEAT"] * 1.15
        except Exception:
            pass
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return sell_revenue, feed_cost


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

    net_deltas = []; sell_rev_deltas = []; feed_cost_deltas = []
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for sd in seeds:
            b_sell, b_feed = play_one(BASE, opp, sd)
            t_sell, t_feed = play_one(TREAT, opp, sd)
            b_net = b_sell - b_feed; t_net = t_sell - t_feed
            net_deltas.append(t_net - b_net)
            sell_rev_deltas.append(t_sell - b_sell)
            feed_cost_deltas.append(t_feed - b_feed)

    n = len(net_deltas)
    def summarize(name, deltas):
        mean = statistics.mean(deltas); sd = statistics.stdev(deltas) if n > 1 else 0.0
        t = mean / (sd / (n ** 0.5)) if sd > 0 else float("nan")
        pos = sum(1 for d in deltas if d > 0); neg = sum(1 for d in deltas if d < 0)
        print(f"{name}: n={n} mean=${mean:+.2f} sd={sd:.2f} t={t:.2f} pos={pos} neg={neg}")

    summarize("sell revenue (treat-base)", sell_rev_deltas)
    summarize("feed cost (treat-base)", feed_cost_deltas)
    summarize("NET (sell_revenue - feed_cost), treat-base", net_deltas)
