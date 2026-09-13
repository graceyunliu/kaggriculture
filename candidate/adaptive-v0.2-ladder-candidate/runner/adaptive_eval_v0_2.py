#!/usr/bin/env python3
"""Adaptive Eval v0.2: preregistered train/held-out matched evaluation."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import math
import platform
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


CERTIFIED_O42 = "154d1ff480e9aa05084e323604a1a09ce73b68adbff95dd4f410e6acf4f52813"
CERTIFIED_CONTROLLER = "9ff99b50656c1ed19b4410d773a83946082bb6f88d605020615dcb3c8e735687"
TRAIN_SEEDS = (1001, 1002, 1003, 1004)
EVAL_SEEDS = (1101, 1102, 1103, 1104)
CONDITIONS = ("baseline_a", "baseline_b", "adaptive_frozen")


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader: raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def sha(path: Path):
    h = hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()


def learned_values_unchanged(before, after):
    for regime, arms in before.items():
        if after.get(regime) != arms: return False
    return all(v["n"] == 0 and v["mean"] == 0.0 for r, arms in after.items() if r not in before for v in arms.values())


def learner_from(v0, state):
    x = v0.Learner()
    for r, arms in state.items():
        for a, values in arms.items(): x.stats[r][a] = copy.deepcopy(values)
    return x


def mean_ci(values):
    if len(values) < 2: return {"n": len(values), "mean": values[0] if values else None, "sd": None, "ci95": None}
    m, sd = statistics.mean(values), statistics.stdev(values)
    half = 1.96 * sd / math.sqrt(len(values))
    return {"n": len(values), "mean": m, "sd": sd, "ci95": [m-half, m+half], "method": "normal-approx descriptive interval"}


def write(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--controller", type=Path, required=True)
    ap.add_argument("--o42", type=Path, required=True)
    ap.add_argument("--scenario", type=Path, required=True)
    ap.add_argument("--frontier", type=Path, required=True)
    ap.add_argument("--soil", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args(); out = args.out.resolve(); out.mkdir(parents=True, exist_ok=True)
    if sha(args.o42) != CERTIFIED_O42: raise SystemExit("STOP: O42 hash mismatch")
    if sha(args.controller) != CERTIFIED_CONTROLLER: raise SystemExit("STOP: controller hash mismatch")
    v0 = load_module(args.controller, "certified_adaptive_slice_v0")
    opponents = {"scenario_v14": args.scenario, "o42_selfplay": args.o42,
                 "frontier_v12": args.frontier, "soil_v25": args.soil}
    opp_hashes = {k: sha(v) for k,v in opponents.items()}
    config = {"design_frozen_before_execution": True, "primary_outcome": "paired adaptive_frozen minus baseline_a final money",
              "secondary_outcome": "paired adaptive_frozen minus baseline_b final money",
              "unit_of_analysis": "held-out (opponent, seed, seat) episode",
              "training_opponents": ["scenario_v14", "o42_selfplay"], "evaluation_opponents": list(opponents),
              "unseen_evaluation_opponents": ["frontier_v12", "soil_v25"],
              "training_seeds": list(TRAIN_SEEDS), "evaluation_seeds": list(EVAL_SEEDS),
              "seats": [0,1], "conditions": list(CONDITIONS), "reward_turns": v0.REWARD_TURNS,
              "multiplicity": "one primary contrast; secondary contrasts and strata descriptive; no p-value tests"}
    write(out/"experiment_manifest.json", config | {"controller_sha256": sha(args.controller), "o42_sha256": sha(args.o42), "opponent_sha256": opp_hashes})

    learner, train_events, training_games, game_no = v0.Learner(), [], [], 0
    for opponent_name in config["training_opponents"]:
        for seed in TRAIN_SEEDS:
            for seat in (0,1):
                start = len(train_events)
                g = v0.run_game(args.o42, opponents[opponent_name], seed, seat, "adaptive_train", learner, train_events, game_no); game_no += 1
                gid = f"train-{opponent_name}-{seed}-s{seat}"; g.update(game_id=gid, opponent=opponent_name, phase="training")
                for e in train_events[start:]: e.update(game_id=gid, opponent=opponent_name, phase="training")
                training_games.append(g)
    frozen = learner.dump(); write(out/"learner_frozen.json", frozen)
    updates = sum(e["update_applied"] for e in train_events)
    if updates == 0: raise SystemExit("STOP: learner did not update in training")

    eval_events, eval_games = [], []
    for condition in CONDITIONS:
        for opponent_name, opponent_path in opponents.items():
            for seed in EVAL_SEEDS:
                for seat in (0,1):
                    local = learner_from(v0, frozen); start = len(eval_events)
                    g = v0.run_game(args.o42, opponent_path, seed, seat, condition, local, eval_events, game_no); game_no += 1
                    gid = f"eval-{condition}-{opponent_name}-{seed}-s{seat}"
                    g.update(game_id=gid, opponent=opponent_name, phase="evaluation", condition=condition, final_money=g["terminal_reward"])
                    for e in eval_events[start:]: e.update(game_id=gid, opponent=opponent_name, phase="evaluation")
                    if not learned_values_unchanged(frozen, local.dump()): raise SystemExit("STOP: evaluation updated learner")
                    eval_games.append(g)

    # Shadow validation for every opponent, both seats, one preregistered eval seed.
    parity = []
    for opponent_name, opponent_path in opponents.items():
        for seat in (0,1):
            ref = next(g for g in eval_games if g["condition"]=="baseline_a" and g["opponent"]==opponent_name and g["seed"]==EVAL_SEEDS[0] and g["seat"]==seat)
            sh = v0.run_game(args.o42, opponent_path, EVAL_SEEDS[0], seat, "shadow", learner_from(v0,frozen), [], game_no); game_no += 1
            row={"opponent":opponent_name,"seed":EVAL_SEEDS[0],"seat":seat,
                 "action_stream_equal":ref["action_stream_hash"]==sh["action_stream_hash"],
                 "terminal_state_equal":ref["terminal_state_hash"]==sh["terminal_state_hash"],
                 "final_money_equal":ref["final_money"]==sh["terminal_reward"],"episode_length_equal":ref["steps"]==sh["steps"]}
            parity.append(row)
    if not all(all(v for k,v in r.items() if k.endswith("equal")) for r in parity): raise SystemExit("STOP: parity failure")

    events=train_events+eval_events
    with (out/"decisions.jsonl").open("w") as f:
        for e in events:f.write(json.dumps(e,sort_keys=True)+"\n")
    write(out/"games.json", {"training":training_games,"evaluation":eval_games})
    write(out/"parity_manifest.json", parity)
    # Matched episode contrasts.
    keyed={(g["condition"],g["opponent"],g["seed"],g["seat"]):g for g in eval_games}
    matched=[]
    for opp in opponents:
        for seed in EVAL_SEEDS:
            for seat in (0,1):
                a=keyed[("baseline_a",opp,seed,seat)]["final_money"]; b=keyed[("baseline_b",opp,seed,seat)]["final_money"]
                ad=keyed[("adaptive_frozen",opp,seed,seat)]["final_money"]
                matched.append({"opponent":opp,"seed":seed,"seat":seat,"fixed_a":a,"fixed_b":b,"adaptive":ad,
                                "adaptive_minus_a":ad-a,"adaptive_minus_b":ad-b})
    adaptive_events=[e for e in eval_events if e["execution_mode"]=="adaptive_frozen"]
    by_regime=defaultdict(Counter); by_opponent=defaultdict(Counter)
    for e in adaptive_events: by_regime[e["regime"]][e["selected_variant"]]+=1;by_opponent[e["opponent"]][e["selected_variant"]]+=1
    quartiles=[]
    n=len(train_events)
    for q in range(4):
        xs=train_events[q*n//4:(q+1)*n//4];quartiles.append({"quartile":q+1,"n":len(xs),"selection":dict(Counter(e["selected_variant"] for e in xs))})
    analysis={"primary":mean_ci([x["adaptive_minus_a"] for x in matched]),
              "secondary_adaptive_minus_b":mean_ci([x["adaptive_minus_b"] for x in matched]),
              "matched_results":matched,"training_games":len(training_games),"evaluation_games":len(eval_games),
              "training_decisions":len(train_events),"training_updates":updates,"training_selection":dict(Counter(e["selected_variant"] for e in train_events)),
              "training_chronology":quartiles,"heldout_adaptive_decisions":len(adaptive_events),
              "heldout_selection":dict(Counter(e["selected_variant"] for e in adaptive_events)),
              "heldout_selection_by_regime":{k:dict(v) for k,v in sorted(by_regime.items())},
              "heldout_selection_by_opponent":{k:dict(v) for k,v in sorted(by_opponent.items())},
              "unseen_opponent_selection":dict(Counter(e["selected_variant"] for e in adaptive_events if e["opponent"] in config["unseen_evaluation_opponents"])),
              "evaluation_updates":sum(e["update_applied"] for e in eval_events),"parity_all_pass":True,
              "counterfactuals":"no same-state outcome counterfactuals; only matched executed episode contrasts"}
    write(out/"analysis.json",analysis)
    write(out/"environment.json",{"python":sys.version,"platform":platform.platform(),"kaggle_environments":__import__("kaggle_environments").__version__})
    if sha(args.o42)!=CERTIFIED_O42 or sha(args.controller)!=CERTIFIED_CONTROLLER:raise SystemExit("STOP: source drift")
    print(out)


if __name__=="__main__":main()
