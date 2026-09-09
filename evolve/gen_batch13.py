#!/usr/bin/env python3
"""Batch 13 (Sep 9): proximity ownership for dispatch, designed against the move ledger.
 D3 sweep ownership: when a hand starts a new sweep, it only takes a task if no other free hand is closer to it
    (falls back to the old nearest-of-top-tier rule if it owns nothing).
 D4 route ownership: a hand only takes an animal route if no other free hand is >=2 closer to the nearest pending animal.
"""
BASE = "candidates/O9_MELON_LATEFERT.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

HELPER = '''
def _free_competitors(i):
    """Other units that could take a task this turn: no animal route, and (no sweep or not yet dispatched)."""
    out = []
    for j, pj in enumerate(S.get("positions", [])):
        if j == i or j in S["routes"]:
            continue
        if j < i and S["sweep"].get(j):
            continue
        out.append(pj)
    return out


def _owned(i, pos, tp, comps, slack=0):
    d = _dist(pos, tp)
    return all(_dist(pj, tp) + slack > d for pj in comps)

'''

def sweep_ownership(c, slack=0):
    c = rep(c, "def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):\n", HELPER + "def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):\n    comps = _free_competitors(i)\n")
    c = rep(c, '''    first = None
    for kind in tiers:
        if pools[kind]:
            tp = _nearest(pos, pools[kind])
            first = (tp, kind)
            for pool in pools.values():
                if tp in pool:pool.remove(tp)
            break
    if first is None:
        return None''', f'''    first = None
    for kind in tiers:
        mine = [tp for tp in pools[kind] if _owned(i, pos, tp, comps, {slack})]
        if mine:
            tp = _nearest(pos, mine)
            first = (tp, kind)
            for pool in pools.values():
                if tp in pool:pool.remove(tp)
            break
    if first is None:
        for kind in tiers:
            if pools[kind]:
                tp = _nearest(pos, pools[kind])
                first = (tp, kind)
                for pool in pools.values():
                    if tp in pool:pool.remove(tp)
                break
    if first is None:
        return None''')
    c = rep(c, '''    v["positions"] = positions''', '''    v["positions"] = positions
    S["positions"] = positions''')
    return c

def route_ownership(c, margin=2):
    if "_free_competitors" not in c:
        c = rep(c, "def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):\n", HELPER + "def _build_sweep(i, pos, v, day, hour, carry, pools, seeds_left):\n")
        c = rep(c, '''    v["positions"] = positions''', '''    v["positions"] = positions
    S["positions"] = positions''')
    c = rep(c, '''    if not cands:
        return None
    stops = []
    cur = pos
    pool = dict(cands)''', f'''    if not cands:
        return None
    # route ownership: leave the animals to a clearly closer free hand
    near = _nearest(pos, [p2 for p2, _t in cands])
    dme = _dist(pos, near)
    for pj in _free_competitors(i):
        if _dist(pj, near) + {margin} <= dme:
            return None
    stops = []
    cur = pos
    pool = dict(cands)''')
    return c

write("B13_01_SWEEP_OWN", sweep_ownership(src))
write("B13_02_ROUTE_OWN", route_ownership(src))
write("B13_03_BOTH_OWN", route_ownership(sweep_ownership(src)))
write("B13_04_SWEEP_OWN_SLACK1", sweep_ownership(src, slack=1))
write("B13_05_ROUTE_OWN_M1", route_ownership(src, margin=1))
