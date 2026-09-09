"""Action-effect audit: which of a candidate's unit actions actually change engine state?

Wraps the engine's _apply_unit_action and compares a cheap fingerprint of (farm tiles/positions/money,
private shed/inventories/seeds) before and after every unit action. An action that leaves state unchanged
is a no-op (illegal, redundant, or raced). Also logs end-of-day shed overflow (goods discarded) and how
many unit-turns are spent walking to a shed tile for a DROP after hour H (when the day's capital events
are over and the free end-of-day auto-drop would have deposited the goods anyway).

Usage: python3 evolve/action_audit.py CAND.py OPP.py [seeds...]
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import mini_engine as me  # noqa: E402


def fp(farm, private):
    return json.dumps([farm["tiles"], farm["farmer"], farm["hands"], farm["money"], private["shed"],
                       private["inventories"], private["seeds"]], sort_keys=True)


def audit(cand, opp, seed, late_hour=13):
    mod, defaults = me.load_engine("master")
    cfg = dict(defaults); cfg["seed"] = None
    env = me._Env(cfg, seed)
    agents = [me.load_agent(cand), me.load_agent(opp)]
    state = me.structify([
        {"observation": {"player": i, "remainingOverageTime": 60, "step": 0}, "action": {},
         "reward": 0.0, "status": "ACTIVE", "info": {}} for i in range(2)
    ])
    state = mod.interpreter(state, env)
    for s in state:
        s.observation.step = 0

    stats = {"total": Counter(), "noop": Counter(), "noop_by_day": defaultdict(Counter),
             "idle_pass": 0, "units_turns": 0, "overflow_discard": Counter(), "late_drop_walk": 0,
             "late_drops": 0, "drop_hours": Counter(), "drop_units": Counter()}
    cur = {"day": 0, "hour": 0}
    farm0 = state[0].observation.farms[0]
    priv0 = state[0].observation.private
    orig_apply = mod._apply_unit_action

    def wrapped(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity=100):
        mine = farm is farm0
        if mine and isinstance(action, list) and action:
            before = fp(farm, private)
        orig_apply(farm, private, idx, action, board_size, day, turns_per_day, shed_capacity)
        if mine and isinstance(action, list) and action:
            op = action[0]
            stats["total"][op] += 1
            if op == "PASS":
                stats["idle_pass"] += 1
            elif fp(farm, private) == before:
                stats["noop"][op] += 1
                stats["noop_by_day"][day][op] += 1
            if op == "DROP":
                stats["drop_hours"][cur["hour"]] += 1
                stats["drop_units"][cur["hour"]] += 0

    mod._apply_unit_action = wrapped
    orig_eod = mod._drop_inventories_to_shed

    def wrapped_eod(private, capacity):
        if private is priv0:
            carried = sum(n for inv in private["inventories"] for n in inv.values() if n > 0)
            room = max(0, capacity - sum(private["shed"].values()))
            lost = max(0, carried - room)
            if lost:
                stats["overflow_discard"][cur["day"]] += lost
        orig_eod(private, capacity)

    mod._drop_inventories_to_shed = wrapped_eod
    step = 0
    while True:
        obs0 = state[0].observation
        cur["day"], cur["hour"] = obs0["day"], obs0["hour"]
        for i in range(2):
            obs = me._fast_copy(state[i].observation)
            obs["step"] = step
            act = agents[i](obs, me._fast_copy(env.configuration))
            state[i].action = act if isinstance(act, dict) else {}
        # late-day walk-to-shed detection for seat 0: a move whose unit is carrying product and heading to a shed tile
        a0 = state[0].action
        if isinstance(a0, dict) and cur["hour"] >= late_hour and cur["day"] < 29:
            inv = state[0].observation.private["inventories"]
            pos = [tuple(obs0.farms[0]["farmer"])] + [tuple(h) for h in obs0.farms[0]["hands"]]
            for u, op in enumerate([a0.get("farmer")] + list(a0.get("hands", []))):
                if u < len(inv) and op and op[0] in ("NORTH", "SOUTH", "EAST", "WEST", "DROP"):
                    prod = sum(n for k, n in inv[u].items() if k not in ("COW", "SHEEP", "GOOSE") and n > 0)
                    if prod and op[0] == "DROP":
                        stats["late_drops"] += 1
        stats["units_turns"] += 1 + len(obs0.farms[0]["hands"])
        state = mod.interpreter(state, env)
        step += 1
        for s in state:
            s.observation.step = step
        if all(s.status == "DONE" for s in state):
            break
    mod._apply_unit_action = orig_apply
    mod._drop_inventories_to_shed = orig_eod
    stats["money"] = state[0].observation.farms[0]["money"]
    return stats


if __name__ == "__main__":
    cand, opp = sys.argv[1], sys.argv[2]
    seeds = [int(s) for s in sys.argv[3:]] or [1, 2, 3]
    for s in seeds:
        r = audit(cand, opp, s)
        tot = sum(r["total"].values())
        print(f"\nseed {s}: money={r['money']:.0f} unit-turns={r['units_turns']} actions={tot} idle PASS={r['idle_pass']} "
              f"({100*r['idle_pass']/max(1,r['units_turns']):.1f}%)")
        print("  no-op actions (state unchanged):", dict(r["noop"].most_common()))
        print("  by op total:", dict(r["total"].most_common()))
        print("  eod overflow discarded units by day:", dict(r["overflow_discard"]))
        print("  DROPs by hour:", dict(sorted(r["drop_hours"].items())), " late (>=13, day<29) drops:", r["late_drops"])
        worst = sorted(r["noop_by_day"].items(), key=lambda kv: -sum(kv[1].values()))[:5]
        print("  worst no-op days:", [(d, dict(c)) for d, c in worst])
