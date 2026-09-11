#!/usr/bin/env python3
"""Paired knob-panel test: TREATMENT vs COMPARATOR (not vs O26), per EVIDENCE_CONTRACT['knob']
(seeds_per_set=20, sets=2, metrics=own+margin, t_min=2.0). Sep 12.

For each seed/opponent/seat, plays TREATMENT vs opp and COMPARATOR vs opp separately (each candidate
occupies the SAME seat against the SAME opponent on the SAME seed), then takes the paired delta
(treatment - comparator) on own money and on margin (own - opp, single seat, matching the paired-seed
methodology already used to promote min_hands_lower to DO). Reports mean delta, t-stat, and per-tape
breakdown for both metrics, across the 4-tape standard panel.

Usage:
  KAGG_FIXED_SHOPS=1 python3 tools/knob_panel.py candidates/O38_MIN_HANDS2_FSP3.py candidates/O36_MIN_HANDS2.py \
      --seeds 11-30 --json experiments/O38_vs_O36_s11-30.json
"""
from __future__ import annotations
import argparse, json, math, os, statistics, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
import mini_engine as me

OPPS = {
    "peter": os.path.join(ROOT, "Opponents/tape_peterparker_106816877.py"),
    "alaylm": os.path.join(ROOT, "Opponents/tape_alaylm_106813359.py"),
    "bahaen": os.path.join(ROOT, "Opponents/tape_bahaenes_106828159.py"),
    "yangk": os.path.join(ROOT, "Opponents/tape_yangkuang2_106819729.py"),
}


def parse_seeds(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def run_game(cand_path, opp_path, seed, cand_seat):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agent_paths = [None, None]
    agent_paths[cand_seat] = cand_path
    agent_paths[1 - cand_seat] = opp_path
    agents = [me.load_agent(p) for p in agent_paths]
    state = me.structify(
        [
            {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
             "reward": 0.0, "status": "ACTIVE", "info": {}}
            for i in range(2)
        ]
    )
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    step = 0
    while True:
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
        if state[0].status != "ACTIVE" or step >= steps:
            break
    cand_money = state[cand_seat].observation.farms[cand_seat]["money"]
    opp_money = state[1 - cand_seat].observation.farms[1 - cand_seat]["money"]
    return cand_money, opp_money


def t_stat(deltas):
    n = len(deltas)
    if n < 2:
        return float("nan")
    mean = statistics.mean(deltas)
    sd = statistics.stdev(deltas)
    if sd == 0:
        return float("inf") if mean != 0 else 0.0
    return mean / (sd / math.sqrt(n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("treatment")
    ap.add_argument("comparator")
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--json")
    args = ap.parse_args()

    seeds = parse_seeds(args.seeds)
    rows = []
    for opp_name, opp_path in OPPS.items():
        for seed in seeds:
            for cand_seat in (0, 1):
                t_own, t_oppmoney = run_game(args.treatment, opp_path, seed, cand_seat)
                c_own, c_oppmoney = run_game(args.comparator, opp_path, seed, cand_seat)
                t_margin = t_own - t_oppmoney
                c_margin = c_own - c_oppmoney
                rows.append({
                    "opp": opp_name, "seed": seed, "cand_seat": cand_seat,
                    "treatment_own": t_own, "treatment_margin": t_margin,
                    "comparator_own": c_own, "comparator_margin": c_margin,
                    "delta_own": t_own - c_own, "delta_margin": t_margin - c_margin,
                })

    all_delta_own = [r["delta_own"] for r in rows]
    all_delta_margin = [r["delta_margin"] for r in rows]

    print("=== OVERALL (all tapes, both seats) ===")
    print(f"n={len(rows)} mean delta_own={statistics.mean(all_delta_own):+.1f} t={t_stat(all_delta_own):+.2f}")
    print(f"n={len(rows)} mean delta_margin={statistics.mean(all_delta_margin):+.1f} t={t_stat(all_delta_margin):+.2f}")

    print("\n=== PER TAPE ===")
    for opp_name in OPPS:
        sub = [r for r in rows if r["opp"] == opp_name]
        d_own = [r["delta_own"] for r in sub]
        d_margin = [r["delta_margin"] for r in sub]
        print(f"{opp_name}: n={len(sub)} delta_own={statistics.mean(d_own):+.1f} delta_margin={statistics.mean(d_margin):+.1f}")

    out = {
        "treatment": args.treatment, "comparator": args.comparator, "seeds": args.seeds,
        "summary": {
            "n": len(rows),
            "mean_delta_own": statistics.mean(all_delta_own),
            "t_delta_own": t_stat(all_delta_own),
            "mean_delta_margin": statistics.mean(all_delta_margin),
            "t_delta_margin": t_stat(all_delta_margin),
        },
        "rows": rows,
    }
    if args.json:
        with open(args.json, "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
