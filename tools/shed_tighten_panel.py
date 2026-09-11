#!/usr/bin/env python3
"""Stage-1 isolation panel for shed_capacity_margin_calibration (AGE-363 candidate family).

Compares a tightened sell-trigger variant (O34_SHED_TIGHT: shed_load>75/80 -> >65/70) against the
O26_CARROT_SIZING baseline on the same standard tape panel, own money + margin, plus the shed_overflow.py
style occupancy stats so a first isolation pass sees both "does it cost money" and "does it actually reduce
ceiling contact" in one run.

Usage:
  KAGG_FIXED_SHOPS=1 python3 tools/shed_tighten_panel.py \
      candidates/O34_SHED_TIGHT.py candidates/O26_CARROT_SIZING.py \
      --opp Opponents/tape_bahaenes_106828159.py --seeds 71-75
"""
import sys, os, argparse, statistics, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me


def run_game(a_path, b_path, seed, a_seat):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agent_paths = [None, None]
    agent_paths[a_seat] = a_path
    agent_paths[1 - a_seat] = b_path
    agents = [me.load_agent(p) for p in agent_paths]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state: s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    max_load = [0, 0]; ge95 = [0, 0]; ge100 = [0, 0]
    discard_units = [0, 0]

    orig_drop = mod._drop_inventories_to_shed
    farm_idx_of = {}

    def counting_drop(private, capacity):
        shed = private["shed"]
        lost_total = 0
        for inv in private["inventories"]:
            for item, n in list(inv.items()):
                if n <= 0: continue
                current = sum(v for k, v in shed.items())
                room = max(0, capacity - current)
                lost = max(0, n - room)
                if lost > 0:
                    lost_total += lost
        fi = private.get("_farm_idx")
        if lost_total > 0 and fi is not None:
            discard_units[fi] += lost_total
        return orig_drop(private, capacity)

    mod._drop_inventories_to_shed = counting_drop
    for i in range(2):
        state[i].observation.private["_farm_idx"] = i

    step = 0
    while True:
        for i in range(2):
            obs = me._fast_copy(state[i].observation); obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act
        state = mod.interpreter(state, env); step += 1
        for s in state: s.observation.step = step
        for i in range(2):
            load = sum(state[i].observation.private["shed"].values())
            if load > max_load[i]: max_load[i] = load
            if load >= 95: ge95[i] += 1
            if load >= 100: ge100[i] += 1
        if state[0].status != "ACTIVE" or step >= steps:
            break

    mod._drop_inventories_to_shed = orig_drop
    o = state[0].observation
    money = [o.farms[p]["money"] for p in range(2)]
    return {
        "a_money": money[a_seat], "b_money": money[1 - a_seat],
        "a_max_load": max_load[a_seat], "a_ge95": ge95[a_seat], "a_ge100": ge100[a_seat],
        "a_discard": discard_units[a_seat],
        "b_max_load": max_load[1 - a_seat], "b_ge95": ge95[1 - a_seat], "b_ge100": ge100[1 - a_seat],
        "b_discard": discard_units[1 - a_seat],
    }


def parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part: continue
        if "-" in part:
            a, b = part.split("-"); out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cand_a")
    ap.add_argument("cand_b")
    ap.add_argument("--opp", required=True)
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()
    seeds = parse_seeds(args.seeds)

    # A vs B directly (own-money / margin between the two variants), both seats.
    ab_rows = []
    for seed in seeds:
        for a_seat in (0, 1):
            r = run_game(args.cand_a, args.cand_b, seed, a_seat)
            r["seed"] = seed; r["a_seat"] = a_seat
            ab_rows.append(r)

    a_money = [r["a_money"] for r in ab_rows]
    b_money = [r["b_money"] for r in ab_rows]
    margin = [r["a_money"] - r["b_money"] for r in ab_rows]

    def stats(vals):
        m = statistics.mean(vals)
        sd = statistics.pstdev(vals) if len(vals) > 1 else 0.0
        se = sd / (len(vals) ** 0.5) if len(vals) > 1 else 0.0
        t = m / se if se > 0 else float("nan")
        return {"mean": round(m, 1), "n": len(vals), "t": round(t, 2)}

    summary = {
        "cand_a": args.cand_a, "cand_b": args.cand_b, "opp_for_occupancy_context": args.opp,
        "n_games_a_vs_b": len(ab_rows),
        "a_money_direct": stats(a_money),
        "b_money_direct": stats(b_money),
        "margin_a_minus_b": stats(margin),
        "a_max_load_mean": round(statistics.mean(r["a_max_load"] for r in ab_rows), 1),
        "a_turns_ge95_mean": round(statistics.mean(r["a_ge95"] for r in ab_rows), 2),
        "a_turns_ge100_mean": round(statistics.mean(r["a_ge100"] for r in ab_rows), 2),
        "a_discard_total": sum(r["a_discard"] for r in ab_rows),
        "b_max_load_mean": round(statistics.mean(r["b_max_load"] for r in ab_rows), 1),
        "b_turns_ge95_mean": round(statistics.mean(r["b_ge95"] for r in ab_rows), 2),
        "b_turns_ge100_mean": round(statistics.mean(r["b_ge100"] for r in ab_rows), 2),
        "b_discard_total": sum(r["b_discard"] for r in ab_rows),
    }
    print(json.dumps(summary, indent=2))
    if args.json:
        with open(args.json, "w") as f:
            json.dump({"summary": summary, "rows": ab_rows}, f, indent=2)


if __name__ == "__main__":
    main()
