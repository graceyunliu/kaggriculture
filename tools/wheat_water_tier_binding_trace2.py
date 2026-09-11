#!/usr/bin/env python3
"""wheat_water_tier binding/error trace, paired per-game version (Sep 13) -- adds paired deltas + t-stats
on top of wheat_water_tier_binding_trace.py's pooled counts, so the wheat-urgent reduction / other-urgent
cost can be judged for consistency (sign agreement across games), not just pooled magnitude.
"""
import sys, os, argparse, statistics, importlib.util
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mini_engine as me

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = os.path.join(ROOT, "candidates/O36_MIN_HANDS2.py")
TREAT = os.path.join(ROOT, "candidates/_probe_wheat_water_tier_1.py")
OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}


def play_one(cand, opp, seed):
    spec = importlib.util.spec_from_file_location("kcand" + str(id(cand)), cand)
    kc = importlib.util.module_from_spec(spec); spec.loader.exec_module(kc)
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    last_day = -1
    wheat_urgent = 0; other_urgent = 0
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            if i == 0 and day != last_day and hour == 0:
                v = kc.perceive(obs)
                for pos, t in v["crops"]:
                    need = kc._water_needed(t, day)
                    if need == "urgent":
                        if t.get("crop") == "WHEAT": wheat_urgent += 1
                        else: other_urgent += 1
                last_day = day
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return wheat_urgent, other_urgent


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

    wheat_deltas = []; other_deltas = []
    for opp_name in opp_names:
        opp = OPPS[opp_name]
        for sd in seeds:
            bw, bo = play_one(BASE, opp, sd)
            tw, to = play_one(TREAT, opp, sd)
            wheat_deltas.append(tw - bw)
            other_deltas.append(to - bo)

    n = len(wheat_deltas)
    def summarize(name, deltas):
        mean = statistics.mean(deltas)
        sd = statistics.stdev(deltas) if n > 1 else 0.0
        t = mean / (sd / (n ** 0.5)) if sd > 0 else float("nan")
        pos = sum(1 for d in deltas if d > 0); neg = sum(1 for d in deltas if d < 0); zero = sum(1 for d in deltas if d == 0)
        print(f"{name}: n={n} mean_delta(treat-base)={mean:+.2f} sd={sd:.2f} t={t:.2f}  pos={pos} neg={neg} zero={zero}")

    summarize("wheat_urgent (treat-base, negative=fewer wheat misses under tier)", wheat_deltas)
    summarize("other_urgent (treat-base, positive=more other-crop misses under tier)", other_deltas)
