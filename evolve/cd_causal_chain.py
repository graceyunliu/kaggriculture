#!/usr/bin/env python3
"""Experiment 2 (Sep 9): trace the proposed C x D causal chain --
D -> inventory sellable earlier -> C sells it earlier -> cash arrives earlier ->
reinvestment happens earlier -> productive capacity increases.

Runs one instrumented game per candidate (O2, D-alone, C-alone, CD) vs C1, and logs,
per day: hour of first DROP (release) event, hour of first SELL after that DROP,
hour cash crosses each day's opening balance + $500 (proxy for "cash arrives"),
hour of next BUY_ANIMAL/BUY_SEED/HIRE after that cash bump (proxy for "reinvestment"),
and cumulative product deposited vs shed inventory sold same-day.
"""
import sys
sys.path.insert(0, "/sessions/vigilant-great-cori/mnt/Kaggriculture")
import mini_engine as me

def trace(agent_path, opp="candidates/C1.py", seed=1, days_to_show=range(1, 21)):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(agent_path), me.load_agent(opp)]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])

    day_events = {}  # day -> dict of first-occurrence hours
    day_open_cash = {}
    step = 0
    while True:
        obs0 = state[0].observation
        day, hour = obs0.day, obs0.hour
        cash = obs0.farms[0]["money"]
        if day not in day_open_cash:
            day_open_cash[day] = cash
            day_events[day] = {"drop_hour": None, "sell_after_drop_hour": None,
                                "cash_bump_hour": None, "reinvest_hour": None}
        ev = day_events[day]
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            if i == 0:
                farmer_act = act.get("farmer") or []
                hand_acts = act.get("hands") or []
                market_act = act.get("market") or []
                all_unit = [farmer_act] + list(hand_acts)
                if ev["drop_hour"] is None:
                    for a in all_unit:
                        if a and a[0] == "DROP":
                            ev["drop_hour"] = hour
                            break
                if ev["drop_hour"] is not None and ev["sell_after_drop_hour"] is None and hour >= ev["drop_hour"]:
                    for m in market_act:
                        if m and m[0] == "SELL":
                            ev["sell_after_drop_hour"] = hour
                            break
                if ev["cash_bump_hour"] is None and cash >= day_open_cash[day] + 500:
                    ev["cash_bump_hour"] = hour
                if ev["cash_bump_hour"] is not None and ev["reinvest_hour"] is None and hour >= ev["cash_bump_hour"]:
                    for m in market_act:
                        if m and m[0] in ("BUY_ANIMAL", "BUY_SEED"):
                            ev["reinvest_hour"] = hour
                            break
                    for a in all_unit:
                        if a and a[0] == "HIRE":
                            ev["reinvest_hour"] = hour
                            break
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
        if step >= steps:
            break

    print(f"\n=== {agent_path} (seed {seed}) ===")
    for d in days_to_show:
        if d in day_events:
            e = day_events[d]
            print(f"  day {d:2d}: drop={e['drop_hour']}  sell_after_drop={e['sell_after_drop_hour']}  "
                  f"cash_bump(+500)={e['cash_bump_hour']}  reinvest_after_bump={e['reinvest_hour']}")

if __name__ == "__main__":
    for cand in sys.argv[1:]:
        trace(cand)
