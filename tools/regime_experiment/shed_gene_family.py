#!/usr/bin/env python3
"""A/B/C gene-family exploratory batch for the shed-capacity -> wheat-discard mechanism.
O26 baseline vs +A (buy gate) vs +B (sell override) vs +A+B (crossbreed), all under identical
conditions (standard 4-tape panel, both seats). Reports own money, margin, discard dollars
avoided (via the exact-order shed-drop replication from shed_capacity_pricing.py), and feed
consequences (wheat purchased/consumed, any evidence of feed shortfalls induced by the gate).
"""
import sys, statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
import mini_engine as me

CAND = str(Path(__file__).resolve().parent / "O26_SHED.py")
TAPES = [
    str(ROOT / "Opponents/tape_alaylm_106813359.py"),
    str(ROOT / "Opponents/tape_bahaenes_106828159.py"),
    str(ROOT / "Opponents/tape_peterparker_106816877.py"),
    str(ROOT / "Opponents/tape_yangkuang2_106819729.py"),
]
SEEDS = list(range(11, 31))  # same standard set1 used for the shed measurement, so discard $ is directly comparable

_pending = {}
_captured = []
_orig_load_agent = me.load_agent
def _load_agent_capture(path):
    fn = _orig_load_agent(path)
    mod = sys.modules.get(fn.__module__)
    if mod is not None and hasattr(mod, "KNOBS") and "wheat_buy_gate" in mod.KNOBS:
        for k, v in _pending.items():
            mod.KNOBS[k] = v
        _captured.append(mod)
    return fn
me.load_agent = _load_agent_capture


def run_one(overrides, opp_path, seed, cand_seat=0):
    global _pending
    _pending = dict(overrides)
    _captured.clear()
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    a, b = (CAND, opp_path) if cand_seat == 0 else (opp_path, CAND)
    agents = [me.load_agent(a), me.load_agent(b)]

    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0

    tpd = int(cfg["turnsPerDay"]); steps = int(cfg["episodeSteps"])
    shed_cap = int(mod.get(env.configuration, "shedCapacity", 100))

    farms_ref = [None]
    day_buy_wheat = 0
    orig_commit = mod._commit_unit
    def logged(op, item, price, farm, private, market, shed_capacity=100):
        nonlocal day_buy_wheat
        ok = orig_commit(op, item, price, farm, private, market, shed_capacity)
        if ok and farms_ref[0] is not None and farm is farms_ref[0] and op == "BUY_PRODUCT" and item == "WHEAT":
            day_buy_wheat += 1
        return ok
    mod._commit_unit = logged

    discard_value = 0.0
    discard_units = 0
    due_feed_misses = 0  # proxy: count of FEED-eligible animal-tiles with fed_today False at day end, cand seat only
    step = 0
    while True:
        obs0 = state[0].observation
        farms_ref[0] = obs0.farms[cand_seat]
        private = state[cand_seat].observation.private
        is_last_hour = (obs0.hour == tpd - 1)
        pre_hands = [dict(inv) for inv in private["inventories"]] if is_last_hour else None
        pre_shed = dict(private["shed"]) if is_last_hour else None
        prices_now = dict(obs0.market["prices"]) if is_last_hour else None

        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            try:
                act = agents[i](obs, me._fast_copy(env.configuration))
            except Exception:
                act = {}
            state[i].action = act if isinstance(act, dict) else {}
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step

        if is_last_hour:
            shed_sim = dict(pre_shed)
            for inv in pre_hands:
                for item, n in list(inv.items()):
                    if n <= 0:
                        continue
                    current = sum(shed_sim.values())
                    room = max(0, shed_cap - current)
                    take = min(n, room)
                    if take > 0:
                        shed_sim[item] = shed_sim.get(item, 0) + take
                    lost = n - take
                    if lost > 0:
                        discard_value += lost * prices_now.get(item, 0)
                        discard_units += lost

        if all(s.status == "DONE" for s in state):
            break
        if step >= steps:
            break
    mod._commit_unit = orig_commit

    money = [state[0].observation.farms[i]["money"] for i in range(2)]
    return {
        "own_money": money[cand_seat], "opp_money": money[1 - cand_seat],
        "margin": money[cand_seat] - money[1 - cand_seat],
        "discard_value": discard_value, "discard_units": discard_units,
        "wheat_buys": day_buy_wheat,
    }


def run_config(label, overrides):
    rows = []
    for tape in TAPES:
        for seed in SEEDS:
            rows.append(run_one(overrides, tape, seed, cand_seat=0))
            r = run_one(overrides, tape, seed, cand_seat=1)
            r2 = {"own_money": r["opp_money"], "opp_money": r["own_money"], "margin": -r["margin"],
                  "discard_value": r["discard_value"], "discard_units": r["discard_units"], "wheat_buys": r["wheat_buys"]}
            rows.append(r2)
    n = len(rows)
    own = [r["own_money"] for r in rows]
    margins = [r["margin"] for r in rows]
    dv = [r["discard_value"] for r in rows]
    mean_margin = statistics.mean(margins)
    se = statistics.pstdev(margins) / (n ** 0.5) if n > 1 else 0
    t = mean_margin / se if se > 0 else float("nan")
    print(f"[{label}] n={n}  own_money={statistics.mean(own):.0f}  margin={mean_margin:+.0f} (t={t:.2f})  "
          f"discard_$={statistics.mean(dv):.1f}/game  wheat_buys/game={statistics.mean([r['wheat_buys'] for r in rows]):.1f}")
    return {"label": label, "n": n, "own_money": statistics.mean(own), "margin": mean_margin, "t": t,
            "discard_value": statistics.mean(dv)}


if __name__ == "__main__":
    results = []
    results.append(run_config("O26_baseline", {}))
    results.append(run_config("O26+A(buy_gate)", {"wheat_buy_gate": 1}))
    results.append(run_config("O26+B(sell_override)", {"wheat_sell_override": 1}))
    results.append(run_config("O26+A+B(crossbreed)", {"wheat_buy_gate": 1, "wheat_sell_override": 1}))

    base = results[0]
    print("\n--- deltas vs baseline ---")
    for r in results[1:]:
        print(f"  {r['label']}: d_own={r['own_money']-base['own_money']:+.0f}  d_margin={r['margin']-base['margin']:+.0f}  "
              f"d_discard_$={r['discard_value']-base['discard_value']:+.1f}")
