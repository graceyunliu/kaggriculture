#!/usr/bin/env python3
"""Per-sweep move ledger (Sep 9): attribute every MOVE of every unit to a phase, for BOTH players in the same game.

A unit-day is cut into legs: a leg = a maximal run of MOVE actions ending in the first non-move action
(or the end of the day). Phase of a leg is decided by what ends it and where it started:
  spawn_walk   first leg of the unit's day (from the morning spawn tile)
  shed_trip    leg ending in DROP or PICKUP (going to the shed)
  task_walk    leg ending in a field work verb (WATER/HARVEST/PLANT/FEED/CARE/COLLECT_FERTILIZER/FERTILIZE/DIG/PLACE/BUILD_*)
  dead_walk    leg ending in PASS / end of day (moved, then did nothing)
Also counted: work actions with no preceding move (work0), PASS turns, and per-phase leg counts so we get
moves-per-leg (how far each phase walks) as well as totals.

Usage: python3 tools/move_ledger.py cand opp --seeds 1-5
"""
import sys, argparse
sys.path.insert(0, "/sessions/confident-jolly-fermat/mnt/Kaggriculture")
import mini_engine as me
MOVES = {"NORTH", "SOUTH", "EAST", "WEST"}
WORK = {"WATER", "HARVEST", "PLANT", "FEED", "CARE", "COLLECT_FERTILIZER", "FERTILIZE", "DIG", "PLACE", "BUILD_PASTURE", "BUILD_COOP"}
SHED = {"DROP", "PICKUP"}
PHASES = ["spawn_walk", "task_walk", "shed_trip", "dead_walk"]

def new_acc():
    return {p: {"moves": 0, "legs": 0, "hist": {}} for p in PHASES} | {"work0": 0, "work": 0, "pass": 0, "turns": 0,
            "task_walk_by_verb": {}, "shed_trip_load": [], "days": 0, "long_by_verb": {}, "long_by_hour": {}, "chain_hist": {}, "prev_work": {}}

def run(a, b, seed, acc):
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(a), me.load_agent(b)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    # per player: per unit index -> (current leg move count, is_first_leg_of_day)
    legs = [{}, {}]
    cur_day = -1
    HOUR = [0]
    def close_leg(i, u, phase, verb=None, load=None):
        n, _first = legs[i].get(u, (0, True))
        if n > 0:
            A = acc[i][phase]; A["moves"] += n; A["legs"] += 1; A["hist"][n] = A["hist"].get(n, 0) + 1
            if phase == "task_walk" and verb: acc[i]["task_walk_by_verb"][verb] = acc[i]["task_walk_by_verb"].get(verb, 0) + n
            if n >= 4 and verb:
                acc[i]["long_by_verb"][verb] = acc[i]["long_by_verb"].get(verb, 0) + n
                acc[i]["long_by_hour"][HOUR[0]] = acc[i]["long_by_hour"].get(HOUR[0], 0) + n
            if phase == "shed_trip" and load is not None: acc[i]["shed_trip_load"].append(load)
        legs[i][u] = (0, False)
    while True:
        obs0 = state[0].observation; day, hour = obs0.day, obs0.hour
        HOUR[0] = hour
        if day != cur_day:
            # end of previous day: any open leg is a dead walk
            for i in (0, 1):
                for u in list(legs[i]): close_leg(i, u, "dead_walk")
                legs[i] = {}
            cur_day = day
            for i in (0, 1): acc[i]["days"] += 1
        for i in (0, 1):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            units = [act.get("farmer") or []] + list(act.get("hands") or [])
            inv = obs["private"].get("inventories") or []
            for u, ua in enumerate(units):
                acc[i]["turns"] += 1
                n, first = legs[i].get(u, (0, True))
                if ua and ua[0] in MOVES:
                    legs[i][u] = (n + 1, first); continue
                verb = ua[0] if ua else "PASS"
                if verb in WORK:
                    if n == 0:
                        acc[i]["work0"] += 1
                        acc[i]["prev_work"][u] = acc[i]["prev_work"].get(u, 1) + 1
                    else:
                        ch = acc[i]["prev_work"].pop(u, None)
                        if ch: acc[i]["chain_hist"][ch] = acc[i]["chain_hist"].get(ch, 0) + 1
                        acc[i]["prev_work"][u] = 1
                    acc[i]["work"] += 1
                    close_leg(i, u, "spawn_walk" if first else "task_walk", verb)
                elif verb in SHED:
                    load = sum(v for k, v in (inv[u].items() if u < len(inv) else []) if k != "WHEAT") if verb == "DROP" else None
                    close_leg(i, u, "spawn_walk" if first else "shed_trip", load=load)
                else:
                    acc[i]["pass"] += 1
                    close_leg(i, u, "spawn_walk" if first else "dead_walk")
                    if n == 0: legs[i][u] = (0, first)  # still on first leg if never moved
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps: break
    for i in (0, 1):
        for u in list(legs[i]): close_leg(i, u, "dead_walk")
    return [state[0].observation.farms[i]["money"] for i in range(2)]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--seeds", default="1-5")
    args = ap.parse_args(); lo, hi = map(int, args.seeds.split("-")); seeds = list(range(lo, hi + 1)); n = len(seeds)
    acc = [new_acc(), new_acc()]; money = [0, 0]
    for s in seeds:
        m = run(args.a, args.b, s, acc); money[0] += m[0] / n; money[1] += m[1] / n
    print(f"n={n} seeds {args.seeds}   mean money P0 {money[0]:.0f}  P1 {money[1]:.0f}")
    print(f"{'phase':12s} {'P0 moves':>9s} {'legs':>6s} {'mv/leg':>7s} | {'P1 moves':>9s} {'legs':>6s} {'mv/leg':>7s} | {'P0-P1':>7s}")
    tot = [0, 0]
    for p in PHASES:
        r = [acc[i][p] for i in (0, 1)]
        for i in (0, 1): tot[i] += r[i]["moves"]
        print(f"{p:12s} {r[0]['moves']/n:9.0f} {r[0]['legs']/n:6.0f} {r[0]['moves']/max(1,r[0]['legs']):7.2f} | "
              f"{r[1]['moves']/n:9.0f} {r[1]['legs']/n:6.0f} {r[1]['moves']/max(1,r[1]['legs']):7.2f} | {(r[0]['moves']-r[1]['moves'])/n:+7.0f}")
    print(f"{'TOTAL moves':12s} {tot[0]/n:9.0f} {'':6s} {'':7s} | {tot[1]/n:9.0f} {'':6s} {'':7s} | {(tot[0]-tot[1])/n:+7.0f}")
    for i in (0, 1):
        A = acc[i]
        print(f"P{i}: work {A['work']/n:.0f} (of which no-move {A['work0']/n:.0f}), pass {A['pass']/n:.0f}, unit-turns {A['turns']/n:.0f}, "
              f"moves/work {tot[i]/max(1,A['work']):.2f}; shed trips {len(A['shed_trip_load'])/n:.0f} avg load {sum(A['shed_trip_load'])/max(1,len(A['shed_trip_load'])):.1f}")
        tw = A["task_walk_by_verb"]
        print(f"    task_walk moves by ending verb: " + " ".join(f"{k}:{v/n:.0f}" for k, v in sorted(tw.items(), key=lambda kv: -kv[1])))
        h = A["task_walk"]["hist"]
        print(f"    task_walk leg-length hist: " + " ".join(f"{k}:{v/n:.0f}" for k, v in sorted(h.items())[:12]))
        print(f"    LONG legs (>=4 moves) by ending verb: " + " ".join(f"{k}:{v/n:.0f}" for k, v in sorted(A["long_by_verb"].items(), key=lambda kv: -kv[1])))
        print(f"    LONG legs by hour: " + " ".join(f"h{k}:{v/n:.0f}" for k, v in sorted(A["long_by_hour"].items())))
        print(f"    same-tile work chain length hist: " + " ".join(f"{k}:{v/n:.0f}" for k, v in sorted(A["chain_hist"].items())))
