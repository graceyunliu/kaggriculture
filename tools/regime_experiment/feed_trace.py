import sys, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT); os.chdir(ROOT)
import mini_engine as me

def run(cand, opp, seed, player=0):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {}, "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0

    # hook FEED action attempts (including failed ones) via wrapping _apply_action if present,
    # else just observe fed_today/consecutive_unfed/escape via tile diffing each end-of-day.
    log = []
    prev_animal_tiles = {}
    prev_hands = None
    prev_shed_wheat = None
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        d, h = state[0].observation.day, state[0].observation.hour
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        farm = o.farms[player]
        priv = state[player].observation.private
        shed_wheat = priv["shed"].get("WHEAT", 0)
        if h == 0:  # end-of-day snapshot (day just rolled)
            board = farm["tiles"]
            n_animals = 0
            n_unfed_ge1 = 0
            escapes = []
            for y, row in enumerate(board):
                for x, t in enumerate(row):
                    key = (x,y)
                    if isinstance(t, dict) and "animal" in t:
                        n_animals += 1
                        cu = t.get("consecutive_unfed", 0)
                        if cu >= 1: n_unfed_ge1 += 1
                        prev_animal_tiles[key] = t.get("animal")
                    else:
                        if key in prev_animal_tiles:
                            escapes.append((key, prev_animal_tiles.pop(key)))
            log.append({
                "day": d, "animals": n_animals, "unfed>=1": n_unfed_ge1,
                "shed_wheat": shed_wheat, "hands_prev_day": prev_hands,
                "escapes": escapes,
            })
        prev_hands = len(farm.get("hands", []))
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return log

if __name__ == "__main__":
    cand = "tools/regime_experiment/sweep/O26_A28.py"
    opp = "candidates/O26_CARROT_SIZING.py"
    seed = 1
    log = run(cand, opp, seed, player=0)
    print(f"{'day':>4} {'animals':>7} {'unfed>=1':>8} {'shed_wheat':>10} {'hands(prevday)':>14}   escapes")
    for r in log:
        esc = r["escapes"]
        print(f"{r['day']:>4} {r['animals']:>7} {r['unfed>=1']:>8} {r['shed_wheat']:>10} {str(r['hands_prev_day']):>14}   {esc if esc else ''}")
