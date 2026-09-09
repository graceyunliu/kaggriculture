"""Quantify end-of-game value leaks: goods still carried or unsold in the shed when the game ends.

Usage: python3 evolve/endgame_leak.py CAND.py OPP.py [seeds...]
Runs seat 0 only (the candidate's leak is what we care about) and prints, per seed, the market value
of (a) product carried by units at game end (lost forever), (b) product sitting in the shed unsold.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

ANIMALS = {"COW", "SHEEP", "GOOSE"}


def leak(cand, opp, seed):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    step = 0
    last_day_sells = []
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            act = agents[i](obs, me._fast_copy(env.configuration))
            state[i].action = act if isinstance(act, dict) else {}
            if i == 0 and obs["day"] == 29 and obs["hour"] >= 18:
                last_day_sells.append((obs["hour"], [o for o in act.get("market", []) if o[0] == "SELL"],
                                       [a[0] for a in [act["farmer"]] + act["hands"]]))
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
    obs0 = state[0].observation
    prices = obs0.market["prices"]
    priv = state[0].observation.private
    carried = {}
    for inv in priv["inventories"]:
        for k, n in inv.items():
            if k not in ANIMALS and n > 0:
                carried[k] = carried.get(k, 0) + n
    shed = {k: n for k, n in priv["shed"].items() if k not in ANIMALS and n > 0}
    cv = sum(n * prices.get(k, 0) for k, n in carried.items())
    sv = sum(n * prices.get(k, 0) for k, n in shed.items())
    return {"seed": seed, "money": obs0.farms[0]["money"], "carried": carried, "carried_val": cv,
            "shed": shed, "shed_val": sv, "tail": last_day_sells}


if __name__ == "__main__":
    cand, opp = sys.argv[1], sys.argv[2]
    seeds = [int(s) for s in sys.argv[3:] if s != "-v"] or [1, 2, 3, 4, 5]
    tot_c = tot_s = 0
    for s in seeds:
        r = leak(cand, opp, s)
        tot_c += r["carried_val"]; tot_s += r["shed_val"]
        print(f"seed {s}: money={r['money']:.0f} carried={r['carried']} (~${r['carried_val']:.0f}) "
              f"shed_unsold={r['shed']} (~${r['shed_val']:.0f})")
        if "-v" in sys.argv:
            for h, sells, ops in r["tail"]:
                print(f"   h{h}: sells={sells} ops={ops}")
    print(f"mean leak/game: carried ${tot_c/len(seeds):.0f}  shed ${tot_s/len(seeds):.0f}")
