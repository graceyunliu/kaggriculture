#!/usr/bin/env python3
"""Stratified weed-recovery panel + causal-chain ledger (Sep 11).

Extends weed_recovery_cf.py: buckets overnight-carry weed events by created_day (early <19, mid 19-23,
late >=24), and for each sampled event traces the SAME tile's subsequent history (kind/crop/yield_units,
from the forced-clear step to game end) in both the base and counterfactual runs, so we can tell whether a
delta actually ran through the intended causal chain (earlier clear -> earlier replant -> extra completed
cycle -> extra units) or is incidental downstream replanning noise.

Usage: KAGG_FIXED_SHOPS=1 python3 tools/weed_recovery_panel.py CAND OPP --seeds 21-40 --max-per-seed 8 --per-stratum 40
"""
import sys, os, argparse, statistics, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me
TPD = 24


def play(cand, opp, seed, force_clear=None, record=None, trace_pos=None, trace_from=0):
    """force_clear = (step, pos). record: weed create/clear transitions (farm 0).
    trace_pos/trace_from: if set, also record (step, kind, crop_or_animal, yield_units) for that one
    position at every step from trace_from onward."""
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev_kind = {}
    trace = []
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try: act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception: act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        o = state[0].observation
        day = o.day
        farm = o.farms[0]
        if force_clear is not None and force_clear[0] == step:
            x, y = force_clear[1]
            farm["tiles"][y][x] = None
        if record is not None:
            for y, row in enumerate(farm["tiles"]):
                for x, t in enumerate(row):
                    pos = (x, y)
                    kind = t.get("kind") if isinstance(t, dict) else None
                    pk = prev_kind.get(pos)
                    if kind == "WEED" and pk != "WEED":
                        record.append((step, day, pos, "create"))
                    elif pk == "WEED" and kind != "WEED":
                        record.append((step, day, pos, "clear"))
                    prev_kind[pos] = kind
        if trace_pos is not None and step >= trace_from:
            x, y = trace_pos
            t = farm["tiles"][y][x]
            if isinstance(t, dict):
                kind = t.get("kind")
                what = t.get("crop") or t.get("animal")
                yu = t.get("yield_units", 0)
            else:
                kind, what, yu = None, None, 0
            trace.append((step, kind, what, yu))
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return state[0].observation.farms[0]["money"], trace


def bucket(day):
    if day < 19: return "early(<19)"
    if day <= 23: return "mid(19-23)"
    return "late(>=24)"


def chain_summary(trace):
    """From a per-step tile trace, derive: first_replant_step, crop, n_completed_cycles (yield resets
    to 0 from >0 while staying PLANT, i.e. a harvest, not a weed death), ended_as."""
    replant_step, crop = None, None
    cycles = 0
    prev_kind, prev_yu = None, 0
    for step, kind, what, yu in trace:
        if kind == "PLANT" and prev_kind != "PLANT" and replant_step is None:
            replant_step, crop = step, what
        if prev_kind == "PLANT" and kind == "PLANT" and prev_yu > 0 and yu == 0:
            cycles += 1
        prev_kind, prev_yu = kind, yu
    ended_as = trace[-1][1] if trace else None
    return {"replant_step": replant_step, "crop": crop, "completed_cycles": cycles, "ended_as": ended_as}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("opp")
    ap.add_argument("--seeds", default="21-40"); ap.add_argument("--max-per-seed", type=int, default=8)
    ap.add_argument("--per-stratum", type=int, default=40)
    ap.add_argument("--json", default=None)
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    by_bucket = {"early(<19)": [], "mid(19-23)": [], "late(>=24)": []}
    for seed in seeds:
        if all(len(v) >= a.per_stratum for v in by_bucket.values()):
            break
        rec = []
        base_money, _ = play(a.cand, a.opp, seed, record=rec)
        opens = {}
        events = []
        for step, day, pos, ev in rec:
            if ev == "create":
                opens.setdefault(pos, []).append((step, day))
            elif ev == "clear":
                st = opens.get(pos)
                if st:
                    cstep, cday = st.pop(0)
                    events.append((cstep, cday, step, pos))
        overnight = [e for e in events if (e[2] - 1) // TPD > e[1]]
        overnight.sort(key=lambda e: e[2] - e[0], reverse=True)
        take = 0
        for cstep, cday, clear_step, pos in overnight:
            b = bucket(cday)
            if len(by_bucket[b]) >= a.per_stratum or take >= a.max_per_seed:
                continue
            target = max(cstep + 1, clear_step - TPD)
            cf_money, cf_trace = play(a.cand, a.opp, seed, force_clear=(target, pos), trace_pos=pos, trace_from=target)
            _, base_trace = play(a.cand, a.opp, seed, trace_pos=pos, trace_from=target)
            delta = cf_money - base_money
            base_chain = chain_summary(base_trace)
            cf_chain = chain_summary(cf_trace)
            row = {"seed": seed, "pos": pos, "created_day": cday, "bucket": b, "created_step": cstep,
                   "actual_clear_step": clear_step, "forced_clear_step": target,
                   "carry_hours": clear_step - cstep, "delta": delta,
                   "base_replant_step": base_chain["replant_step"], "base_crop": base_chain["crop"],
                   "base_cycles": base_chain["completed_cycles"],
                   "cf_replant_step": cf_chain["replant_step"], "cf_crop": cf_chain["crop"],
                   "cf_cycles": cf_chain["completed_cycles"],
                   "extra_cycle": cf_chain["completed_cycles"] - base_chain["completed_cycles"],
                   "earlier_replant": (cf_chain["replant_step"] is not None and base_chain["replant_step"] is not None
                                        and cf_chain["replant_step"] < base_chain["replant_step"]),
                   "same_crop": cf_chain["crop"] == base_chain["crop"]}
            by_bucket[b].append(row)
            take += 1
            print(f"seed{seed} {b} pos{pos} d{cday} carried{clear_step-cstep}h delta{delta:+.0f} "
                  f"replant base@{base_chain['replant_step']}({base_chain['crop']}) cf@{cf_chain['replant_step']}({cf_chain['crop']}) "
                  f"cycles base={base_chain['completed_cycles']} cf={cf_chain['completed_cycles']}", flush=True)
            if a.json:
                open(a.json, "a").write(json.dumps(row) + "\n")
    print("\n=== stratified summary ===")
    for b, rows in by_bucket.items():
        if not rows: print(f"{b}: n=0"); continue
        ds = [r["delta"] for r in rows]
        pos_f = sum(1 for d in ds if d > 0) / len(ds)
        zero_f = sum(1 for d in ds if d == 0) / len(ds)
        neg_f = sum(1 for d in ds if d < 0) / len(ds)
        extra_cycle_f = sum(1 for r in rows if r["extra_cycle"] > 0) / len(rows)
        earlier_replant_f = sum(1 for r in rows if r["earlier_replant"]) / len(rows)
        print(f"{b}: n={len(rows)} mean={statistics.mean(ds):+.1f} median={statistics.median(ds):+.1f} "
              f"pos={pos_f:.2f} zero={zero_f:.2f} neg={neg_f:.2f} earlier_replant={earlier_replant_f:.2f} extra_cycle={extra_cycle_f:.2f}")


if __name__ == "__main__":
    main()
