#!/usr/bin/env python3
"""tape_days.py -- turn an expert trajectory (a tape agent, or any agent module) into a
per-day chore ledger, per docs/SPEC-planner-from-tape.md section 2.

Usage:
  python3 tools/tape_days.py candidates/H32.py --seed 1 --out evolve/expert/H32_s1/

Writes day_00.json .. day_29.json (one per day) plus summary.json into --out.
Seat 0 = the agent under test, seat 1 = --opponent (default candidates/V3_12.py).

Implementation note: we drive the real engine (mini_engine.load_engine("master")) exactly
like mini_engine.run_game does, but monkeypatch kaggriculture._apply_unit_action and
_end_of_day (the sentinel-path trick from tools/sell_shift.py, applied to engine internals
instead of load_agent) so we can diff each unit's tile/inventory before vs after its own
action -- that's what lets us tell a *completed* WATER from an attempted one.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402

MOVES = {"NORTH", "SOUTH", "EAST", "WEST", "PASS"}
LOGISTICS = {"PICKUP", "DROP", "PLACE", "BUILD_COOP", "BUILD_PASTURE"}
SIMPLE_CHORE = {"WATER": "water", "FEED": "feed", "CARE": "care",
                 "COLLECT_FERTILIZER": "collect", "DIG": "dig", "FERTILIZE": "fertilize"}


def to_plain(o):
    if isinstance(o, dict):
        return {k: to_plain(v) for k, v in o.items()}
    if isinstance(o, list):
        return [to_plain(v) for v in o]
    return o


# --------------------------------------------------------------------------- chore id / done
def classify(action, tile_before):
    """Return (kind, chore_id_prefix) for an action; kind is None for moves/logistics."""
    if not isinstance(action, list) or not action:
        return None
    op = action[0]
    if op in MOVES or op in LOGISTICS:
        return None
    if op == "PLANT":
        return "plant"
    if op == "HARVEST":
        if isinstance(tile_before, dict) and tile_before.get("kind") == "PLANT":
            return "harvest"
        if isinstance(tile_before, dict) and "animal" in tile_before:
            return "harvest_animal"
        return "harvest"  # attempted on a tile with no yield -> still classify, will fail "done" check
    if op in SIMPLE_CHORE:
        return SIMPLE_CHORE[op]
    return None


def action_done(mod, op, tile_before, tile_after, inv_before, inv_after):
    if op == "WATER":
        return (isinstance(tile_before, dict) and not tile_before.get("watered_today")
                and isinstance(tile_after, dict) and tile_after.get("watered_today"))
    if op == "FEED":
        return (isinstance(tile_before, dict) and not tile_before.get("fed_today")
                and isinstance(tile_after, dict) and tile_after.get("fed_today"))
    if op == "CARE":
        return (isinstance(tile_before, dict) and not tile_before.get("cared_today")
                and isinstance(tile_after, dict) and tile_after.get("cared_today"))
    if op == "COLLECT_FERTILIZER":
        return inv_after.get("FERTILIZER", 0) > inv_before.get("FERTILIZER", 0)
    if op == "FERTILIZE":
        return (isinstance(tile_before, dict) and isinstance(tile_after, dict)
                and tile_after.get("fertilized_until_day", -1) > tile_before.get("fertilized_until_day", -1))
    if op == "DIG":
        return tile_before is not None and tile_after is None
    if op == "PLANT":
        return tile_before is None and isinstance(tile_after, dict) and tile_after.get("kind") == "PLANT"
    if op == "HARVEST":
        if isinstance(tile_before, dict) and tile_before.get("kind") == "PLANT":
            crop = tile_before.get("crop")
            return inv_after.get(crop, 0) > inv_before.get(crop, 0)
        if isinstance(tile_before, dict) and "animal" in tile_before:
            product = mod.ANIMALS[tile_before["animal"]]["product"]
            return inv_after.get(product, 0) > inv_before.get(product, 0)
    return False


def failure_reason(op, tile_before, inv_before):
    if op == "WATER":
        if not isinstance(tile_before, dict) or tile_before.get("kind") != "PLANT":
            return "no plant here"
        if tile_before.get("watered_today"):
            return "already watered"
        return "unknown"
    if op == "FEED":
        if not isinstance(tile_before, dict) or "animal" not in tile_before:
            return "no animal here"
        if tile_before.get("fed_today"):
            return "already fed"
        if inv_before.get("WHEAT", 0) <= 0:
            return "no wheat carried"
        return "unknown"
    if op == "CARE":
        if not isinstance(tile_before, dict) or "animal" not in tile_before:
            return "no animal here"
        return "already cared"
    if op == "COLLECT_FERTILIZER":
        if not isinstance(tile_before, dict) or "animal" not in tile_before:
            return "no animal here"
        return "no fertilizer available"
    if op == "FERTILIZE":
        if inv_before.get("FERTILIZER", 0) <= 0:
            return "no fertilizer carried"
        if not isinstance(tile_before, dict) or tile_before.get("kind") != "PLANT":
            return "no plant here"
        return "unknown"
    if op == "DIG":
        return "nothing to dig"
    if op == "PLANT":
        if tile_before is not None:
            return "tile occupied"
        return "no seed"
    if op == "HARVEST":
        if not isinstance(tile_before, dict):
            return "nothing here"
        return "no yield ready"
    return "unknown"


# --------------------------------------------------------------------------- chore enumeration
def enumerate_chores_from_state(state_h0, day):
    """Per SPEC-day-planner-executor.md sec 4. Returns (all_ids, hard_ids)."""
    farm = state_h0["farm"]
    private = state_h0["private"]
    tiles = farm["tiles"]
    seeds = private.get("seeds", {}) or {}
    fert_avail = (private.get("shed", {}) or {}).get("FERTILIZER", 0) > 0
    all_ids, hard_ids = [], []

    def add(cid, hard):
        all_ids.append(cid)
        if hard:
            hard_ids.append(cid)

    CROPS = {
        "WHEAT": (4, 2), "CARROT": (3, 2), "MELON": (12, 10), "TOMATO": (8, None), "STRAWBERRY": (10, None),
    }
    ONE_TIME = {"WHEAT": 6, "CARROT": 4, "MELON": 6}

    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if not isinstance(tile, dict):
                continue
            kind = tile.get("kind")
            if kind == "WEED":
                add(f"dig:{x},{y}", False)
                continue
            if kind == "PLANT":
                crop = tile["crop"]
                cu = tile.get("consecutive_unwatered", 0)
                if cu >= 1:
                    add(f"water:{x},{y}", True)
                elif crop in ONE_TIME:
                    max_yield_day = CROPS[crop][0]
                    window_start = (max_yield_day + 1) // 2
                    age = day - tile["planted_day"]
                    if window_start <= age <= max_yield_day and tile.get("yield_units", 0) < ONE_TIME[crop]:
                        hard = (crop == "MELON" and 6 <= day <= 10)
                        add(f"water:{x},{y}", hard)
                elif tile.get("fertilized_until_day", -1) >= day:
                    add(f"water:{x},{y}", False)
                # harvest
                age = day - tile["planted_day"]
                first_yield = 2 if crop in ("WHEAT", "CARROT") else (10 if crop == "MELON" else (8 if crop == "TOMATO" else 10))
                if tile.get("yield_units", 0) > 0 and age >= first_yield:
                    add(f"harvest:{x},{y}", False)
                if fert_avail and tile.get("fertilized_until_day", -1) < day:
                    add(f"fertilize:{x},{y}", False)
                continue
            if "animal" in tile:
                if not tile.get("fed_today"):
                    add(f"feed:{x},{y}", True)
                if not tile.get("cared_today") and day < 28:
                    add(f"care:{x},{y}", False)
                if tile.get("fertilizer_available"):
                    add(f"collect:{x},{y}", False)
                if tile.get("yield_units", 0) > 0:
                    add(f"harvest_animal:{x},{y}", False)
                continue
            if kind in ("COOP", "PASTURE"):
                continue
            if tile is None:
                pass
    # empty tiles -> plant chore, one per empty owned tile if seeds available
    if any(n > 0 for n in seeds.values()):
        for y, row in enumerate(tiles):
            for x, tile in enumerate(row):
                if tile is None:
                    add(f"plant:{x},{y}", False)
    return all_ids, hard_ids


# --------------------------------------------------------------------------- main driver
def run_tape(agent_path, opponent_path, seed, days=30):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults)
    cfg["seed"] = None
    env = me._Env(cfg, seed)
    agent_a = me.load_agent(agent_path)
    agent_b = me.load_agent(opponent_path)

    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0

    farm0 = [state[0].observation.farms[0]]
    hour_log = []
    orig_apply = mod._apply_unit_action
    orig_eod = mod._end_of_day
    eod_snapshot = {}

    def patched_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity=100):
        if farm is not farm0[0]:
            return orig_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)
        pos = None
        if idx == 0:
            pos = tuple(farm["farmer"])
        elif idx - 1 < len(farm["hands"]):
            pos = tuple(farm["hands"][idx - 1])
        tile_before = copy.deepcopy(farm["tiles"][pos[1]][pos[0]]) if pos else None
        inv_before = dict(private["inventories"][idx]) if idx < len(private["inventories"]) else {}
        orig_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)
        tile_after = farm["tiles"][pos[1]][pos[0]] if pos else None
        inv_after = private["inventories"][idx] if idx < len(private["inventories"]) else {}
        hour_log.append((idx, pos, list(action) if isinstance(action, list) else action,
                          tile_before, copy.deepcopy(tile_after), inv_before, dict(inv_after)))

    def patched_eod(state, env, day):
        farm = farm0[0]
        unfed = sum(1 for row in farm["tiles"] for t in row
                    if isinstance(t, dict) and "animal" in t and not t.get("fed_today"))
        unwatered = sum(1 for row in farm["tiles"] for t in row
                         if isinstance(t, dict) and t.get("kind") == "PLANT" and not t.get("watered_today"))
        eod_snapshot[day] = {"unfed": unfed, "unwatered_plants": unwatered}
        return orig_eod(state, env, day)

    mod._apply_unit_action = patched_apply
    mod._end_of_day = patched_eod

    tpd = int(cfg["turnsPerDay"])
    steps = int(cfg["episodeSteps"])
    n_days = min(days, steps // tpd)

    days_out = []
    day_data = None
    prev_h0_snapshot = None

    def new_day_bucket(d, state_h0_plain, seed):
        return {
            "day": d, "seed": seed, "state_h0": state_h0_plain, "hands_hired": [],
            "actions": {}, "chores_done": {}, "chores_available_h0": [], "chores_hard_h0": [],
            "market": [], "money": [], "shed": [], "eod": {}, "failed": [],
        }

    try:
        step = 0
        while step < steps:
            obs0 = state[0].observation
            hour = obs0.hour
            day = obs0.day
            farm = obs0.farms[0]
            priv0 = state[0].observation.private

            if hour == 0:
                if day_data is not None:
                    days_out.append(day_data)
                state_h0_plain = {
                    "day": day, "farm": to_plain(farm), "private": to_plain(priv0),
                    "market": to_plain(obs0.market), "town": to_plain(obs0.town),
                }
                day_data = new_day_bucket(day, state_h0_plain, seed)
                all_ids, hard_ids = enumerate_chores_from_state(state_h0_plain, day)
                day_data["chores_available_h0"] = all_ids
                day_data["chores_hard_h0"] = hard_ids
                if prev_h0_snapshot is not None:
                    prev_animals = sum(1 for row in prev_h0_snapshot["farm"]["tiles"] for t in row
                                        if isinstance(t, dict) and "animal" in t)
                    cur_animals = sum(1 for row in farm["tiles"] for t in row
                                       if isinstance(t, dict) and "animal" in t)
                    prev_weeds = sum(1 for row in prev_h0_snapshot["farm"]["tiles"] for t in row
                                      if isinstance(t, dict) and t.get("kind") == "WEED")
                    cur_weeds = sum(1 for row in farm["tiles"] for t in row
                                     if isinstance(t, dict) and t.get("kind") == "WEED")
                    prev_day = prev_h0_snapshot["day"]
                    eod = dict(eod_snapshot.get(prev_day, {"unfed": 0, "unwatered_plants": 0}))
                    eod["escaped"] = max(0, prev_animals - cur_animals)
                    eod["new_weeds"] = max(0, cur_weeds - prev_weeds)
                    days_out[-1]["eod"] = eod
                prev_h0_snapshot = state_h0_plain

            hands_before = len(farm["hands"])
            money_before = farm["money"]
            shed_before = dict(priv0["shed"])
            day_data["money"].append(money_before)
            day_data["shed"].append(shed_before)

            hour_log.clear()
            for i in range(2):
                obs = me._fast_copy(state[i].observation)
                obs["step"] = step
                try:
                    act = (agent_a if i == 0 else agent_b)(obs, me._fast_copy(env.configuration))
                except Exception:
                    act = {}
                state[i].action = act if isinstance(act, dict) else {}

            mkt_orders = (state[0].action or {}).get("market", []) if isinstance(state[0].action, dict) else []
            for o in mkt_orders or []:
                day_data["market"].append([hour, o])

            state = mod.interpreter(state, env)
            step += 1
            for s in state:
                s.observation.step = step

            hands_after = len(state[0].observation.farms[0]["hands"])
            if hands_after > hands_before:
                day_data["hands_hired"].append([hour, hands_after - hands_before])

            for idx, pos, action, tile_before, tile_after, inv_before, inv_after in hour_log:
                op = action[0] if isinstance(action, list) and action else None
                kind = classify(action, tile_before)
                cid = None
                if kind is not None and pos is not None:
                    cid = f"{kind}:{pos[0]},{pos[1]}"
                day_data["actions"].setdefault(idx, []).append([hour, list(pos) if pos else None, action, cid])
                if kind is not None:
                    done = action_done(mod, op, tile_before, tile_after, inv_before, inv_after)
                    if done:
                        day_data["chores_done"].setdefault(cid, [hour, idx])
                    else:
                        reason = failure_reason(op, tile_before, inv_before)
                        day_data["failed"].append([hour, idx, action, reason])

            if all(s.status == "DONE" for s in state):
                break
    finally:
        mod._apply_unit_action = orig_apply
        mod._end_of_day = orig_eod

    if day_data is not None:
        days_out.append(day_data)
        # final day has no "next day h0" to diff eod against; leave eod from patched_eod hook if present
        last_day = days_out[-1]["day"]
        if not days_out[-1]["eod"]:
            days_out[-1]["eod"] = dict(eod_snapshot.get(last_day, {"unfed": 0, "unwatered_plants": 0}),
                                        escaped=0, new_weeds=0)

    return days_out[:n_days]


def summarize(days_out):
    summary = []
    for d in days_out:
        kinds = {}
        for cid in d["chores_done"]:
            k = cid.split(":", 1)[0]
            kinds[k] = kinds.get(k, 0) + 1
        moves = 0
        work = 0
        idle = 0
        turns = 0
        for idx, acts in d["actions"].items():
            for hour, pos, action, cid in acts:
                turns += 1
                op = action[0] if isinstance(action, list) and action else None
                if op in MOVES:
                    if op == "PASS":
                        idle += 1
                    else:
                        moves += 1
                elif op in LOGISTICS:
                    pass
                else:
                    work += 1
        hires = d["hands_hired"]
        hire_cost = None  # fib cost not tracked here; see money deltas instead
        summary.append({
            "day": d["day"],
            "hands_h0": len(d["state_h0"]["farm"]["hands"]) + 1,
            "chores_done_by_kind": kinds,
            "chores_done_total": len(d["chores_done"]),
            "chores_available_h0": len(d["chores_available_h0"]),
            "chores_hard_h0": len(d["chores_hard_h0"]),
            "moves": moves, "work_actions": work, "idle_turns": idle,
            "travel_per_work": round(moves / work, 3) if work else None,
            "failed": len(d["failed"]),
            "hires": hires,
            "money_h0": d["money"][0] if d["money"] else None,
            "money_h23": d["money"][-1] if d["money"] else None,
            "eod": d["eod"],
        })
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent")
    ap.add_argument("--opponent", default=str(ROOT / "candidates" / "V3_12.py"))
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    out_dir = Path(a.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    days_out = run_tape(a.agent, a.opponent, a.seed, a.days)
    for d in days_out:
        with open(out_dir / f"day_{d['day']:02d}.json", "w") as f:
            json.dump(d, f, separators=(",", ":"))
    summary = summarize(days_out)
    with open(out_dir / "summary.json", "w") as f:
        json.dump(summary, f, indent=1)
    print(f"{a.agent}: wrote {len(days_out)} days to {out_dir}")
    for row in summary[:5]:
        print(f"  day {row['day']:>2}: hands={row['hands_h0']} chores_done={row['chores_done_total']}"
              f"/{row['chores_available_h0']} (hard={row['chores_hard_h0']}) travel/work={row['travel_per_work']}"
              f" failed={row['failed']} eod={row['eod']}")


if __name__ == "__main__":
    main()
