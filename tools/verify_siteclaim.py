#!/usr/bin/env python3
"""Behavioral verification (Sep 9) for the O2 site-claim coordination ablation.
Loads the candidate module directly (not just its agent() function) and monkey-patches
_pick_site to record every (day, hour, site) it returns, so we can count how often two
calls within the SAME turn return the SAME site -- a direct measurement of "two of our
own units targeting the same empty tile", not just an indirect money-margin inference.
"""
import sys, importlib.util, os
sys.path.insert(0, "/sessions/upbeat-eager-fermi/mnt/Kaggriculture")
import mini_engine as me

def load_module(path):
    path = me.Path(path)
    name = f"verifymod_{path.stem}_{os.getpid()}"
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def verify(agent_path, opp="candidates/C1.py", seed=1):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)

    cand_mod = load_module(agent_path)
    opp_agent = me.load_agent(opp)

    calls = []  # (day, hour, site)
    orig_pick_site = cand_mod._pick_site
    current_turn = {}
    def wrapped(v, species=None):
        site = orig_pick_site(v, species)
        if site is not None:
            calls.append((current_turn.get("day"), current_turn.get("hour"), site))
        return site
    cand_mod._pick_site = wrapped

    agents = [cand_mod.agent, opp_agent]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])

    step = 0
    while True:
        obs0 = state[0].observation
        current_turn["day"], current_turn["hour"] = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
        if step >= steps:
            break

    # Count same-turn duplicate sites (two _pick_site calls in the same (day,hour) returning the same tile).
    from collections import Counter
    turn_sites = {}
    for day, hour, site in calls:
        turn_sites.setdefault((day, hour), []).append(site)
    dup_turns = 0
    for k, sites in turn_sites.items():
        c = Counter(sites)
        if any(v > 1 for v in c.values()):
            dup_turns += 1
    return {"pick_site_calls": len(calls), "turns_with_duplicate_target": dup_turns,
            "final_money_p0": state[0].observation.farms[0]["money"]}

if __name__ == "__main__":
    for cand in sys.argv[1:]:
        r = verify(cand)
        print(f"{cand}: {r}", flush=True)
