#!/usr/bin/env python3
"""Routing oracle bound: how much is there to gain from better hand routing, if decisions stay the same?

STATUS (Sep 3): built and run. Result on C1 vs the Yuan800 tape, seeds 1-8: free travel changes own money by
-63k..+25k per seed, mean ~0; halved travel ~0. Idle unit-turns explode. Interpretation: C1 is work-generation
limited, not routing limited -- its economy does not scale production when labor is freed. See RULES.md.
Caveat: --fix-decisions (step-by-step replay of the base game's buy/hire orders) is fragile because cash timing
shifts under the oracle and replayed orders fail; a robust version needs day-level targets. Results vs an
adaptive opponent (V3.12) are confounded because V3.12 reacts to our visible herd. Use tape opponents.

Two counterfactual executors, applied to an unmodified agent by the driver loop (the agent's code and all of
its decisions -- what to buy, plant, sell, which tasks exist -- are untouched; only travel gets cheaper):

  speed2   every MOVE covers 2 tiles instead of 1 (travel halved)        ~ what a good router could plausibly reach
  teleport every relocation costs exactly 1 turn regardless of distance  = upper bound: travel ~free

Mechanism: the agent file is rendered with a patched `_step()` that records the target tile of every move
(keyed by the unit's current position). After the agent acts, the driver reads those targets from the loaded
module and either moves the unit an extra tile toward its target (speed2) or sets its position to the target
and replaces the op with PASS (teleport). The opponent is unaffected. Same seeds, both seats, so the result is
a paired margin exactly like the cascade's.

    python3 evolve/oracle.py candidates/C1.py --opp candidates/V3_12.py --seeds 1-10
    python3 evolve/oracle.py candidates/C1.py --opp Opponents/tape_yuan800_104892947.py --seeds 11-30 --mode teleport
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
import time
from multiprocessing import get_context
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

GEN = ROOT / "evolve" / "gen"
PATCH = '''
ORACLE_TARGETS = {}
ORACLE_UNIT = [None]


def _step(pos, tgt):
    x, y = pos
    tx, ty = tgt
    if (x, y) != (tx, ty) and ORACLE_UNIT[0] is not None:
        ORACLE_TARGETS[ORACLE_UNIT[0]] = (int(tx), int(ty))
    if x < tx: return "EAST"
    if x > tx: return "WEST"
    if y < ty: return "SOUTH"
    if y > ty: return "NORTH"
    return None
'''
MOVES = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}


def render_oracle_agent(agent_path):
    """Copy of the agent with `_step` replaced by the recording version. Returns the new path."""
    src = Path(agent_path).read_text()
    start = src.index("\ndef _step(pos, tgt):")
    end = src.index("\ndef ", start + 1)
    out = src[:start] + "\n" + PATCH + src[end:]
    # tag the unit index before each unit's dispatch so _step can attribute targets per unit
    import re
    out, n = re.subn(r"(\ndef _unit_action\(i, pos, [^\n]*\):\n)", r"\1    ORACLE_UNIT[0] = i\n", out, count=1)
    if n != 1:
        raise SystemExit("could not find _unit_action(i, pos, ...) to patch")
    GEN.mkdir(parents=True, exist_ok=True)
    p = GEN / f"oracle_{hashlib.sha256(out.encode()).hexdigest()[:12]}.py"
    if not p.exists():
        p.write_text(out)
    return p


def _unit_positions(farm):
    return [tuple(farm["farmer"])] + [tuple(h) for h in farm["hands"]]


def _set_pos(farm, idx, pos):
    if idx == 0:
        farm["farmer"] = list(pos)
    else:
        farm["hands"][idx - 1] = list(pos)


BUY_OPS = ("BUY_ANIMAL", "BUY_SEED", "BUY_PRODUCT", "HIRE", "BUY_LAND")


def record_market(agent_path, opp_path, seed, seat=0, engine="master"):
    """Per-step market orders the unmodified agent issues in a normal game (to hold decisions fixed)."""
    mod, defaults = me.load_engine(engine)
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    paths = [str(agent_path), str(opp_path)] if seat == 0 else [str(opp_path), str(agent_path)]
    agents = [me.load_agent(p) for p in paths]
    state = me.structify([{"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
                           "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s_ in state:
        s_.observation.step = 0
    steps = int(cfg["episodeSteps"])
    out = []
    step = 0
    while True:
        for i in range(2):
            obs = copy.deepcopy(state[i].observation); obs["step"] = step
            try:
                act = agents[i](obs, copy.deepcopy(env.configuration))
            except Exception:  # noqa: BLE001
                act = {}
            state[i].action = act if isinstance(act, dict) else {}
        out.append([o for o in (state[seat].action.get("market") or []) if isinstance(o, (list, tuple)) and o and o[0] in BUY_OPS])
        state = mod.interpreter(state, env)
        step += 1
        for s_ in state:
            s_.observation.step = step
        if all(s_.status == "DONE" for s_ in state) or step >= steps:
            break
    return out


def run_oracle(agent_path, opp_path, seed, mode="teleport", seat=0, engine="master", fix_decisions=False, debug=None):
    """One game with the oracle executor applied to `agent_path` in `seat`. Returns (money_agent, money_opp).
    fix_decisions: replay the unmodified agent's BUY/HIRE/LAND orders step by step (its SELL orders stay live),
    so the counterfactual changes execution only, not capital allocation."""
    fixed = record_market(agent_path, opp_path, seed, seat, engine) if fix_decisions else None
    oracle_agent = render_oracle_agent(agent_path)
    mod, defaults = me.load_engine(engine)
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    paths = [str(oracle_agent), str(opp_path)] if seat == 0 else [str(opp_path), str(oracle_agent)]
    agents = [me.load_agent(p) for p in paths]
    # the module object of the oracle agent, to read ORACLE_TARGETS
    amod = sys.modules[agents[seat].__module__]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0
    steps = int(cfg["episodeSteps"])
    board = int(cfg.get("boardSize", 10))
    step = 0
    stats = {"moves_saved": 0, "teleports": 0}
    daily = {"money": [], "hands": [], "sales": [], "buys": [], "idle": []}
    day_sales = [0.0]; day_buys = [0.0]; day_idle = [0]; hands_max = [0]
    orig_commit = mod._commit_unit
    def logged_commit(op, item, price, farm_, private, market, shed_capacity=100):
        ok = orig_commit(op, item, price, farm_, private, market, shed_capacity)
        if ok and farm_ is state[0].observation.farms[seat]:
            if op == "SELL": day_sales[0] += price
            elif op in ("BUY_PRODUCT", "BUY_SEED", "BUY_ANIMAL"): day_buys[0] += price
        return ok
    mod._commit_unit = logged_commit
    cur_day = -1
    while True:
        obs0 = state[0].observation
        if obs0.day != cur_day:
            if cur_day >= 0:
                daily["sales"].append(round(day_sales[0])); daily["buys"].append(round(day_buys[0]))
                daily["hands"].append(hands_max[0]); daily["idle"].append(day_idle[0])
                day_sales[0] = 0.0; day_buys[0] = 0.0; day_idle[0] = 0; hands_max[0] = 0
            cur_day = obs0.day
            daily["money"].append(obs0.farms[seat]["money"])
            daily.setdefault("opp_money", []).append(obs0.farms[1 - seat]["money"])
            daily.setdefault("animals", []).append(sum(1 for row in obs0.farms[seat]["tiles"] for t_ in row if isinstance(t_, dict) and "animal" in t_))
            daily.setdefault("plants", []).append(sum(1 for row in obs0.farms[seat]["tiles"] for t_ in row if isinstance(t_, dict) and t_.get("kind") == "PLANT"))
            daily.setdefault("prices", []).append({k: round(v) for k, v in dict(state[0].observation.get("market", {}).get("prices", {})).items()} if hasattr(state[0].observation, "get") else {})
        for i in range(2):
            obs = copy.deepcopy(state[i].observation)
            obs["step"] = step
            if i == seat:
                amod.ORACLE_TARGETS.clear()
            try:
                act = agents[i](obs, copy.deepcopy(env.configuration))
            except Exception:  # noqa: BLE001
                act = {}
            state[i].action = act if isinstance(act, dict) else {}
        # apply the oracle to our seat's units
        farm = obs0.farms[seat]
        act = state[seat].action
        if fixed is not None and step < len(fixed):
            sells = [o for o in (act.get("market") or []) if isinstance(o, (list, tuple)) and o and o[0] not in BUY_OPS]
            act["market"] = (list(fixed[step]) + sells)[:10]
        ops = [act.get("farmer") or ["PASS"]] + list(act.get("hands") or [])
        positions = _unit_positions(farm)
        hands_max[0] = max(hands_max[0], len(positions) - 1)
        day_idle[0] += sum(1 for o in ops if (o[0] if isinstance(o, (list, tuple)) and o else "PASS") == "PASS")
        targets = dict(amod.ORACLE_TARGETS)
        new_hands = list(act.get("hands") or [])
        for u, pos in enumerate(positions):
            op = ops[u] if u < len(ops) else ["PASS"]
            verb = op[0] if isinstance(op, (list, tuple)) and op else None
            if debug is not None and u == debug[0] and step < debug[1]:
                print(f"    step {step:3d} day {obs0.day} h {obs0.hour:2d} unit {u} at {pos} op {op} target {targets.get(u)}")
            if mode == "none" or verb not in MOVES:
                continue
            tgt = targets.get(u)
            if tgt is None:
                continue
            dist = abs(tgt[0] - pos[0]) + abs(tgt[1] - pos[1])
            if mode == "teleport":
                _set_pos(farm, u, tgt)
                stats["teleports"] += 1
                stats["moves_saved"] += dist - 1
                if u == 0:
                    act["farmer"] = ["PASS"]
                else:
                    new_hands[u - 1] = ["PASS"]
            elif mode == "speed2" and dist >= 2:
                dx, dy = MOVES[verb]
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < board and 0 <= ny < board:
                    _set_pos(farm, u, (nx, ny))   # first tile now; the engine applies the second step below
                    stats["moves_saved"] += 1
                    # second step must follow the path from the NEW position (x first, then y -- same rule as _step)
                    if nx != tgt[0]:
                        nxt = "EAST" if nx < tgt[0] else "WEST"
                    else:
                        nxt = "SOUTH" if ny < tgt[1] else "NORTH"
                    if u == 0:
                        act["farmer"] = [nxt]
                    else:
                        new_hands[u - 1] = [nxt]
        if new_hands:
            act["hands"] = new_hands
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state) or step >= steps:
            break
    mod._commit_unit = orig_commit
    daily["sales"].append(round(day_sales[0])); daily["buys"].append(round(day_buys[0])); daily["hands"].append(hands_max[0]); daily["idle"].append(day_idle[0])
    money = [state[0].observation.farms[i]["money"] for i in range(2)]
    return {"seed": seed, "seat": seat, "mode": mode, "money_agent": money[seat], "money_opp": money[1 - seat], "daily": daily, **stats}


def _job(args):
    return run_oracle(*args[:6], fix_decisions=args[6] if len(args) > 6 else False)


def parse_seeds(s):
    out = []
    for part in s.split(","):
        if "-" in part:
            a, b = part.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--opp", default=str(ROOT / "candidates" / "V3_12.py"))
    ap.add_argument("--seeds", default="1-10")
    ap.add_argument("--mode", default="both", choices=["teleport", "speed2", "both"])
    ap.add_argument("--jobs", type=int, default=None)
    ap.add_argument("--fix-decisions", action="store_true", help="replay the base game's buy/hire/land orders; only execution changes")
    ap.add_argument("--per-seed", action="store_true")
    args = ap.parse_args()
    seeds = parse_seeds(args.seeds)
    modes = ["speed2", "teleport"] if args.mode == "both" else [args.mode]
    t0 = time.time()
    # baseline: unmodified agent vs opp, both seats (cached via mini_engine)
    base = me.evaluate(args.agent, args.opp, seeds, engine="master", both_seats=True, jobs=args.jobs, use_cache=True)
    print(f"baseline {Path(args.agent).name} vs {Path(args.opp).name}: margin {base['mean_margin_per_game']:+,.0f}/game "
          f"(t={base['t']:.1f}, {base['wins']}-{base['losses']}), own mean ${base['mean_a']:,.0f}")
    jobs = []
    for mode in modes:
        for s in seeds:
            for seat in (0, 1):
                jobs.append((args.agent, args.opp, s, mode, seat, "master", args.fix_decisions))
    with get_context("spawn").Pool(args.jobs or 4) as pool:
        res = pool.map(_job, jobs)
    if args.per_seed:
        for r in sorted(res, key=lambda r: (r["seed"], r["seat"], r["mode"])):
            d = base["per_seed"][r["seed"]]
            bown = d["a"] / 2
            print(f"  seed {r['seed']} seat {r['seat']} {r['mode']:8s}: own {r['money_agent']:>9,.0f} (base avg {bown:>9,.0f}, {r['money_agent']-bown:+,.0f}) opp {r['money_opp']:>9,.0f} saved {r['moves_saved']}")
    for mode in modes:
        rows = [r for r in res if r["mode"] == mode]
        per_seed = {}
        for r in rows:
            d = per_seed.setdefault(r["seed"], {"a": 0.0, "b": 0.0})
            d["a"] += r["money_agent"]
            d["b"] += r["money_opp"]
        margins = [d["a"] - d["b"] for d in per_seed.values()]
        n = len(margins)
        mean = sum(margins) / n
        sd = (sum((m - mean) ** 2 for m in margins) / (n - 1)) ** 0.5 if n > 1 else 0
        own = sum(d["a"] for d in per_seed.values()) / n / 2
        saved = sum(r["moves_saved"] for r in rows) / len(rows)
        print(f"{mode:9s}: margin {mean/2:+,.0f}/game vs opp (t={mean/(sd/n**0.5) if sd else 0:.1f}), own mean ${own:,.0f} "
              f"-> ORACLE GAIN {own - base['mean_a']:+,.0f}/game over baseline; moves saved/game {saved:,.0f}")
    print(f"{time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
