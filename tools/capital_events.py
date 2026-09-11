#!/usr/bin/env python3
"""Capital-event instrument (Sep 10). For candidates built on the O-family `economy`, wrap the module's
economy() and log every turn where the mid-day capital window opened (S["capital_events"] incremented):
day, hour, cash, and the capital orders (BUY_ANIMAL / HIRE / BUY_LAND / BUY_SEED) placed that turn.
Explains why a capital-timing change (O16_CAPITAL_CHECKPOINT) does or does not stack with another change.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/capital_events.py CAND1 CAND2 ... --opp Opponents/tape_x.py --seeds 11-16
"""
import sys, os, argparse, importlib.util
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))))
import mini_engine as me
CAP = ("BUY_ANIMAL", "HIRE", "BUY_LAND", "BUY_SEED", "BUY_PRODUCT")

def load_instrumented(path, log):
    global_n = [0]
    spec = importlib.util.spec_from_file_location(f"capev_{os.path.basename(path)}_{id(log)}", path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    econ = mod.economy
    def wrapped(obs, v, pending_drop=None):
        S = mod.S; before = S.get("capital_events", 0), S.get("capital_event_day")
        out = econ(obs, v, pending_drop)
        after = S.get("capital_events", 0)
        day, hour = obs["day"], obs["hour"]
        fired = (after > before[0]) or (before[1] != day and after > 0)
        if fired:
            log.append({"day": day, "hour": hour, "cash": obs["farms"][obs["player"]]["money"],
                        "orders": [o for o in out if o and o[0] in CAP]})
        for o in out:
            if o and o[0] in CAP:
                log.append({"all": True, "day": day, "hour": hour, "orders": [o]})
        return out
    mod.economy = wrapped
    return mod.agent

def play(cand, opp, seed):
    log = []
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [load_instrumented(cand, log), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return state[0].observation.farms[0]["money"], log

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("cands", nargs="+"); ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", default="11-14"); a = ap.parse_args()
    lo, hi = map(int, a.seeds.split("-")); seeds = range(lo, hi + 1)
    for c in a.cands:
        tot_ev = 0; by_day = {}; orders = {}; allo = {}; hours = []; money = []
        for s in seeds:
            m, log = play(c, a.opp, s); money.append(m)
            for e in [e for e in log if e.get("all")]:
                for o in e["orders"]:
                    k = o[0] + ("/" + str(o[1]) if len(o) > 1 and o[0] != "HIRE" else "")
                    allo[k] = allo.get(k, 0) + (o[2] if len(o) > 2 and isinstance(o[2], (int, float)) else 1)
            log = [e for e in log if not e.get("all")]
            tot_ev += len(log)
            for e in log:
                by_day[e["day"]] = by_day.get(e["day"], 0) + 1; hours.append(e["hour"])
                for o in e["orders"]:
                    k = o[0] + ("/" + str(o[1]) if len(o) > 1 and o[0] != "HIRE" else "")
                    orders[k] = orders.get(k, 0) + (o[2] if len(o) > 2 and isinstance(o[2], (int, float)) else 1)
        n = len(list(seeds))
        print(f"\n{os.path.basename(c)}  mean money {sum(money)/n:,.0f}  events/game {tot_ev/n:.1f}  "
              f"mean event hour {sum(hours)/max(1,len(hours)):.1f}")
        print("  events by day:", " ".join(f"d{d}:{by_day[d]/n:.1f}" for d in sorted(by_day)))
        print("  ALL capital orders per game:", " ".join(f"{k}:{v/n:.1f}" for k, v in sorted(allo.items(), key=lambda kv: -kv[1])))
        print("  capital orders at event turns (per game):", " ".join(f"{k}:{v/n:.1f}" for k, v in sorted(orders.items(), key=lambda kv: -kv[1])))
