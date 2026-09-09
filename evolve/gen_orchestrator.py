#!/usr/bin/env python3
"""Global crop orchestrator on O12 (Sep 9): each turn, build a cost matrix over (free unit x open crop task) with
cost = distance + priority weight - commitment bonus, and assign by global minimum cost (greedy matching over the
whole matrix) instead of each unit self-selecting the nearest task of its top tier. Execution at the tile is unchanged
(_crop_step's per-tile chains: harvest -> replant -> water, fert -> water). Animal routes/setup untouched."""
BASE = "candidates/O12_EVENING_DEPOSIT.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

ORCH = '''
# ===== ORCHESTRATOR (global assignment of crop tasks) =====
ORCH_PRIO = {"urgent": 0.0, "harvest": 1.0, "wwater": 1.0, "fert": 1.0, "plant": 2.0, "water": 2.0, "weeds": 3.0, "slack": 6.0}
ORCH_COMMIT = 0.75      # bonus for keeping the task a unit is already heading to (prevents swap oscillation)
ORCH_SLACK_HOUR = 14


def _orchestrate(v, pools, positions, day, hour, inv, seeds_left, busy):
    """Assign at most one crop task per free unit by global min-cost matching. Returns {unit: (tp, kind)}."""
    prev = S.get("assign", {})
    tasks = []
    for kind, lst in pools.items():
        if kind == "slack" and hour < ORCH_SLACK_HOUR:
            continue
        for tp in lst:
            tasks.append((tp, kind))
    free = [j for j in range(len(positions)) if j not in busy]
    if not free or not tasks:
        return {}
    # units already standing on a tile with an open task keep it (chain in progress)
    pairs = []
    for j in free:
        pj = positions[j]
        carry = inv[j] if j < len(inv) else {}
        for ti, (tp, kind) in enumerate(tasks):
            if kind == "fert" and carry.get("FERTILIZER", 0) <= 0:
                continue
            if kind == "plant" and not any(seeds_left.get(c, 0) > 0 for c in CROP_SPECS):
                continue
            d = _dist(pj, tp)
            if d + 1 > 24 - hour:
                continue
            cost = d + ORCH_PRIO[kind]
            if prev.get(j, (None, None))[0] == tp:
                cost -= ORCH_COMMIT
            pairs.append((cost, j, ti))
    pairs.sort()
    assigned = {}; used_t = set()
    for cost, j, ti in pairs:
        if j in assigned or ti in used_t:
            continue
        assigned[j] = tasks[ti]; used_t.add(ti)
        if len(assigned) == len(free):
            break
    return assigned

'''

def orchestrator(c):
    c = rep(c, "def _crop_step(i, pos, v, day, hour, carry, pools, seeds_left):\n", ORCH + "def _crop_step(i, pos, v, day, hour, carry, pools, seeds_left):\n")
    # run the assignment once per turn, before the ops loop; busy = units on animal routes or carrying animals
    c = rep(c, '''    positions = [tuple(me["farmer"])] + [tuple(h) for h in me["hands"]]
    v["positions"] = positions
    ops = []''', '''    positions = [tuple(me["farmer"])] + [tuple(h) for h in me["hands"]]
    v["positions"] = positions
    busy = set(S["routes"].keys())
    for j, bag in enumerate(inv):
        if any(bag.get(sp, 0) > 0 for sp in ANIMALS):
            busy.add(j)
    # rebuild the pools fresh (the sweep-based removal above is no longer the source of truth)
    pools = _crop_pools(v, seeds_left, day)
    S["assign"] = _orchestrate(v, pools, positions, day, hour, inv, seeds_left, busy)
    for j, (tp, kind) in S["assign"].items():
        sw = S["sweep"].get(j)
        if not sw or sw[0][0] != tp:
            S["sweep"][j] = [(tp, kind)]
        for pool in pools.values():
            if tp in pool: pool.remove(tp)
    ops = []''')
    return c

write("X1_ORCH", orchestrator(src))
write("X1_ORCH_COMMIT0", orchestrator(src).replace("ORCH_COMMIT = 0.75", "ORCH_COMMIT = 0.0"))
write("X1_ORCH_FLATPRIO", orchestrator(src).replace('"harvest": 1.0, "wwater": 1.0, "fert": 1.0, "plant": 2.0, "water": 2.0, "weeds": 3.0', '"harvest": 0.5, "wwater": 0.5, "fert": 0.5, "plant": 1.0, "water": 1.0, "weeds": 1.5'))
