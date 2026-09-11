#!/usr/bin/env python3
"""Weed-recovery counterfactual (Sep 11): what is one day of earlier weed clearance actually worth?

Design (per Grace's Sep 11 spec): identify tiles that die into WEED under H_GATE144 and carry overnight
uncleared; replay the SAME deterministic game but force that one tile to clear (WEED -> empty) one day
earlier than it actually did; let the UNCHANGED policy continue; measure final-money delta. This isolates
the value of earlier tile availability, separate from the labour cost of the dig itself (which is a sunk
one-hour action either way).

Usage: KAGG_FIXED_SHOPS=1 python3 tools/weed_recovery_cf.py CAND OPP --seeds 21-25 --max-per-seed 6
"""
import sys, os, argparse, statistics, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me
TPD = 24


def play(cand, opp, seed, force_clear=None, record=None):
    """force_clear = (step, pos) -> at that step, after interpreter runs, set that tile to empty (None).
    record: list to append (step, day, pos, event) weed create/clear transitions for farm 0."""
    mod, defaults = me.load_engine("master"); cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed); agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"]); step = 0
    prev_kind = {}
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
        if all(s.status == "DONE" for s in state) or step >= steps: break
    return state[0].observation.farms[0]["money"]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cand"); ap.add_argument("opp")
    ap.add_argument("--seeds", default="21-25"); ap.add_argument("--max-per-seed", type=int, default=6)
    ap.add_argument("--json", default=None)
    a = ap.parse_args(); os.chdir(ROOT)
    lo, hi = map(int, a.seeds.split("-")); seeds = list(range(lo, hi + 1))
    all_deltas = []
    done_seeds = set()
    if a.json and os.path.exists(a.json):
        done_seeds = {json.loads(l)["seed"] for l in open(a.json) if l.strip()}
        print(f"resume: {len(done_seeds)} seeds already in {a.json}", flush=True)
    for seed in seeds:
        if seed in done_seeds:
            continue
        rec = []
        base_money = play(a.cand, a.opp, seed, record=rec)
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
        sample = overnight if a.max_per_seed <= 0 else overnight[: a.max_per_seed]   # <=0: every overnight event (unbiased)
        print(f"seed {seed}: base {base_money:.0f}, {len(events)} weed events, {len(overnight)} overnight-carry, testing {len(sample)}", flush=True)
        for cstep, cday, clear_step, pos in sample:
            target = max(cstep + 1, clear_step - TPD)
            cf_money = play(a.cand, a.opp, seed, force_clear=(target, pos))
            delta = cf_money - base_money
            all_deltas.append(delta)
            row = {"seed": seed, "pos": pos, "created_step": cstep, "created_day": cday,
                   "actual_clear_step": clear_step, "forced_clear_step": target,
                   "carry_hours": clear_step - cstep, "delta": delta}
            print(f"  pos {pos} created d{cday} (step {cstep}), actually cleared step {clear_step} "
                  f"(carried {clear_step-cstep}h), forced clear at {target} -> delta {delta:+.0f}", flush=True)
            if a.json:
                open(a.json, "a").write(json.dumps(row) + "\n")
    if all_deltas:
        print(f"\nN={len(all_deltas)}  mean {statistics.mean(all_deltas):+.1f}  median {statistics.median(all_deltas):+.1f}  "
              f"min {min(all_deltas):+.0f}  max {max(all_deltas):+.0f}")


if __name__ == "__main__":
    main()
