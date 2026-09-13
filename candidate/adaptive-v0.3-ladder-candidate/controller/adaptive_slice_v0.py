#!/usr/bin/env python3
"""Adaptive Slice v0: auditable online selection at O42's animal boundary.

The O42 module is loaded read-only.  A decision exists only when O42 emits at
least one BUY_ANIMAL order.  Variant A returns the O42 action unchanged;
variant B limits each emitted animal order to one animal.  Shadow mode records
the selection but always returns O42's original action.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import math
import os
import platform
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

VARIANTS = ("A_FULL_O42", "B_ONE_PER_ORDER")
REWARD_TURNS = 24

# --- v0.3 change (this file only; learner state and reward/regime logic are
# byte-identical to certified v0.2) ---
# The certified v0.2 frozen learner state has several regimes where the
# chosen arm's empirical mean is estimated from a small handful of games
# (some cells n=1..4), yet frozen-eval selection is plain greedy over those
# noisy means (UCB's explore bonus is negligible once totals are fixed at
# eval time, since it does not grow with more real play). MIN_N_TO_TRUST_B
# requires variant B ("B_ONE_PER_ORDER", the deviation from O42) to have at
# least this many training observations in a regime before frozen selection
# is allowed to pick it over A ("A_FULL_O42" == O42's own behavior, the safe
# baseline this candidate is built on). Regimes where B has fewer than this
# many observations fall back to A regardless of the raw mean comparison.
# This does not change training-time UCB1 behavior and does not retrain or
# alter learner_frozen.json in any way -- it only changes which arm frozen
# (evaluation/ladder) mode is willing to act on.
MIN_N_TO_TRUST_B = 10


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def stable_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def load_agent(path: Path, tag: str):
    spec = importlib.util.spec_from_file_location(tag, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.agent


def animal_orders(action: dict) -> list[list]:
    return [o for o in action.get("market", []) if o and o[0] == "BUY_ANIMAL"]


def apply_variant(action: dict, variant: str) -> dict:
    if variant == "A_FULL_O42":
        return action
    out = copy.deepcopy(action)
    for order in out.get("market", []):
        if order and order[0] == "BUY_ANIMAL":
            order[2] = min(1, int(order[2]))
    return out


def state_vector(obs: dict) -> dict:
    p = obs["player"]
    me = obs["farms"][p]
    private = obs["private"]
    inv = private.get("inventories") or []
    animals = ("COW", "SHEEP", "GOOSE")
    owned = 0
    empty = 0
    for row in me["tiles"]:
        for tile in row:
            if isinstance(tile, dict):
                owned += int(tile.get("animal") in animals)
                empty += int(not tile.get("animal") and not tile.get("crop") and tile.get("type") != "SHED")
    unplaced = sum(private.get("shed", {}).get(a, 0) for a in animals)
    unplaced += sum(bag.get(a, 0) for bag in inv for a in animals)
    prices = obs["market"]["prices"]
    return {
        "day": int(obs["day"]), "hour": int(obs["hour"]), "cash": float(me["money"]),
        "empty_land": empty, "owned_animals": owned, "unplaced_animals": unplaced,
        "feed_inventory": int(private.get("shed", {}).get("WHEAT", 0)),
        "cow_price": float(prices.get("COW", 0)), "sheep_price": float(prices.get("SHEEP", 0)),
        "remaining_days": 29 - int(obs["day"]), "hands": len(me.get("hands", [])),
    }


def regime(s: dict) -> str:
    # Fixed coarse representation, not a policy: actions are learned per cell.
    phase = "early" if s["day"] <= 7 else "mid" if s["day"] <= 17 else "late"
    liquidity = "low" if s["cash"] < 1500 else "high"
    pressure = "tight" if s["hands"] < max(5, s["owned_animals"] // 2) else "roomy"
    return f"{phase}|{liquidity}|{pressure}"


class Learner:
    """Deterministic UCB1 with per-regime empirical means."""
    def __init__(self):
        self.stats = defaultdict(lambda: {v: {"n": 0, "mean": 0.0} for v in VARIANTS})

    def snapshot(self, r: str) -> dict:
        return copy.deepcopy(self.stats[r])

    def choose(self, r: str, learning: bool, frozen: bool = False) -> tuple[str, dict]:
        st = self.stats[r]
        if not learning and not frozen:
            return VARIANTS[0], {"algorithm": "learning_off", "scores": {VARIANTS[0]: 0.0}}
        unseen = [v for v in VARIANTS if st[v]["n"] == 0]
        if unseen and not frozen:
            v = unseen[0]
            return v, {"algorithm": "UCB1", "reason": "deterministic_unseen_arm", "scores": {x: None for x in VARIANTS}}
        total = max(1, sum(st[v]["n"] for v in VARIANTS))
        scores = {v: st[v]["mean"] + math.sqrt(2 * math.log(total) / max(1, st[v]["n"])) for v in VARIANTS}
        v = max(VARIANTS, key=lambda x: (scores[x], -VARIANTS.index(x)))
        if frozen and v == "B_ONE_PER_ORDER" and st["B_ONE_PER_ORDER"]["n"] < MIN_N_TO_TRUST_B:
            return VARIANTS[0], {"algorithm": "frozen_greedy_min_n_guard", "scores": scores,
                                  "reason": "insufficient_B_support", "b_n": st["B_ONE_PER_ORDER"]["n"],
                                  "min_n_to_trust_b": MIN_N_TO_TRUST_B, "would_have_selected": v}
        return v, {"algorithm": "frozen_greedy" if frozen else "UCB1", "scores": scores}

    def update(self, r: str, v: str, reward: float) -> None:
        x = self.stats[r][v]
        x["n"] += 1
        x["mean"] += (reward - x["mean"]) / x["n"]

    def dump(self) -> dict:
        return {r: copy.deepcopy(v) for r, v in sorted(self.stats.items())}


class WrappedAgent:
    def __init__(self, base, learner: Learner, mode: str, meta: dict, events: list):
        self.base, self.learner, self.mode, self.meta, self.events = base, learner, mode, meta, events
        self.pending, self.index, self.turn = [], 0, 0

    def __call__(self, obs, cfg):
        cash = float(obs["farms"][obs["player"]]["money"])
        for pending in list(self.pending):
            if self.turn >= pending["due_turn"]:
                reward = cash - pending["cash_before"]
                before = self.learner.snapshot(pending["regime"])
                if self.mode == "adaptive_train":
                    self.learner.update(pending["regime"], pending["variant"], reward)
                event = self.events[pending["event_index"]]
                event["reward"] = reward
                event["learning_state_after"] = self.learner.snapshot(pending["regime"])
                event["update_applied"] = self.mode == "adaptive_train"
                event["learning_state_at_update_before"] = before
                self.pending.remove(pending)
        original = self.base(obs, cfg)
        emitted = animal_orders(original)
        if not emitted:
            self.turn += 1
            return original
        s, r = state_vector(obs), None
        r = regime(s)
        fixed = {"baseline_a": VARIANTS[0], "baseline_b": VARIANTS[1]}.get(self.mode)
        if fixed:
            selected, reason = fixed, {"algorithm": "fixed_baseline", "variant": fixed}
        else:
            selected, reason = self.learner.choose(r, learning=self.mode == "adaptive_train", frozen=self.mode == "adaptive_frozen")
        event = {**self.meta, "decision_index": self.index, "turn": self.turn, "day": int(obs["day"]),
                 "hour": int(obs["hour"]), "state": s, "regime": r,
                 "available_policy_variants": list(VARIANTS), "selected_variant": selected,
                 "learning_state_before": self.learner.snapshot(r), "selection_reason": reason,
                 "o42_animal_orders": emitted, "action_original_hash": stable_hash(original),
                 "execution_mode": self.mode, "executed_variant": VARIANTS[0] if self.mode == "shadow" else selected,
                 "reward_window": {"start_turn": self.turn + 1, "end_turn": self.turn + REWARD_TURNS},
                 "reward": None, "learning_state_after": None}
        self.events.append(event)
        self.pending.append({"due_turn": self.turn + REWARD_TURNS, "cash_before": cash, "regime": r,
                             "variant": selected, "event_index": len(self.events) - 1})
        self.index += 1
        result = original if self.mode == "shadow" else apply_variant(original, selected)
        event["same_state_policy_actions"] = {v: copy.deepcopy(apply_variant(original, v)) for v in VARIANTS}
        event["same_state_counterfactual_rewards"] = None
        event["actual_action"] = copy.deepcopy(result)
        event["action_executed_hash"] = stable_hash(result)
        self.turn += 1
        return result


def run_game(o42: Path, opponent: Path | None, seed: int, seat: int, mode: str,
             learner: Learner, events: list, game_no: int) -> dict:
    from kaggle_environments import make
    base = load_agent(o42, f"o42_{game_no}_{mode}_{seed}_{seat}")
    opp = (load_agent(opponent, f"opp_{game_no}_{seed}_{seat}") if opponent else (lambda obs, cfg: []))
    opponent_name = opponent.name if opponent else "noop"
    meta = {"game_id": f"{mode}-{opponent_name}-{seed}-s{seat}", "seed": seed,
            "opponent": opponent_name, "seat": seat}
    wrapped = WrappedAgent(base, learner, mode, meta, events)
    agents = [wrapped, opp] if seat == 0 else [opp, wrapped]
    env = make("kaggriculture", configuration={"seed": seed}, debug=False)
    env.run(agents)
    terminal = env.steps[-1]
    actions = [step[seat].get("action") for step in env.steps]
    state_hash = stable_hash(terminal)
    return {**meta, "terminal_reward": terminal[seat].get("reward"), "action_stream_hash": stable_hash(actions),
            "terminal_state_hash": state_hash, "steps": len(env.steps)}


def write_json(path: Path, value: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def summarize(events: list, games: list, learner: Learner) -> dict:
    picks = Counter(e["selected_variant"] for e in events)
    by_regime = defaultdict(Counter)
    for e in events: by_regime[e["regime"]][e["selected_variant"]] += 1
    rewards = defaultdict(list)
    for g in games: rewards[g["execution_mode"] if "execution_mode" in g else g["game_id"].split("-",1)[0]].append(g["terminal_reward"])
    return {"decisions": len(events), "selection_counts": dict(picks),
            "selection_by_regime": {k: dict(v) for k, v in sorted(by_regime.items())},
            "learner_final": learner.dump(), "games": len(games)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--o42", type=Path, required=True)
    ap.add_argument("--opponent", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--train-seeds", default="920,921,922,923")
    ap.add_argument("--test-seeds", default="924,925")
    args = ap.parse_args()
    out = args.out.resolve(); out.mkdir(parents=True, exist_ok=True)
    train = [int(x) for x in args.train_seeds.split(",") if x]
    test = [int(x) for x in args.test_seeds.split(",") if x]
    learner, events, games = Learner(), [], []
    n = 0
    # Training is sequential and update-enabled.
    for seed in train:
        for seat in (0, 1):
            games.append(run_game(args.o42, args.opponent, seed, seat, "adaptive_train", learner, events, n)); n += 1
    frozen_state = learner.dump()
    # Held-out games never update. Evaluate the real opponent and a structurally
    # different no-op control under identical seeds/seats for generalization.
    for eval_opponent in (args.opponent, None):
        for mode in ("baseline_a", "baseline_b", "adaptive_frozen"):
            for seed in test:
                for seat in (0, 1):
                    g = run_game(args.o42, eval_opponent, seed, seat, mode, learner, events, n)
                    g["execution_mode"] = mode
                    games.append(g); n += 1
    # Shadow parity: fresh O42-vs-opponent reference then shadow, identical seed/seat.
    parity = []
    for seed, seat in [(test[0], 0), (test[0], 1)]:
        ref = run_game(args.o42, args.opponent, seed, seat, "baseline_a", Learner(), [], n); n += 1
        sh = run_game(args.o42, args.opponent, seed, seat, "shadow", learner, events, n); n += 1
        parity.append({"seed": seed, "seat": seat, "action_stream_equal": ref["action_stream_hash"] == sh["action_stream_hash"],
                       "terminal_state_equal": ref["terminal_state_hash"] == sh["terminal_state_hash"], "reference": ref, "shadow": sh})
    # Deterministic reproducibility (fresh state, fixed arm).
    r1 = run_game(args.o42, args.opponent, test[0], 0, "baseline_a", Learner(), [], n); n += 1
    r2 = run_game(args.o42, args.opponent, test[0], 0, "baseline_a", Learner(), [], n)
    reproducibility = {"action_stream_equal": r1["action_stream_hash"] == r2["action_stream_hash"],
                       "terminal_state_equal": r1["terminal_state_hash"] == r2["terminal_state_hash"], "run_1": r1, "run_2": r2}
    with (out / "adaptation.jsonl").open("w") as f:
        for e in events: f.write(json.dumps(e, sort_keys=True) + "\n")
    write_json(out / "games.json", games)
    write_json(out / "learner_frozen.json", frozen_state)
    write_json(out / "parity.json", parity)
    write_json(out / "reproducibility.json", reproducibility)
    write_json(out / "summary.json", summarize(events, games, learner))
    write_json(out / "environment.json", {"python": sys.version, "platform": platform.platform(),
               "kaggle_environments": __import__("kaggle_environments").__version__, "o42_path": str(args.o42.resolve()),
               "o42_sha256": sha256(args.o42), "opponent_path": str(args.opponent.resolve()) if args.opponent else None,
               "opponent_sha256": sha256(args.opponent) if args.opponent else None,
               "train_seeds": train, "test_seeds": test, "reward_turns": REWARD_TURNS})
    print(out)


if __name__ == "__main__": main()
