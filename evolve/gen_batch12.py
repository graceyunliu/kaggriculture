#!/usr/bin/env python3
"""Batch 12 (Sep 9): siting from the move ledger — reserve the inner ring (shed dist <= R) for pastures while the
herd is still growing, so animals (visited daily for ~25 days) sit at dist ~1.5 like the tape's, not 2.4."""
BASE = "candidates/O9_MELON_LATEFERT.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

def ring_reserve(c, R=2, until_day=17, min_keep=0):
    # plant pool and plant validity skip ring tiles while animals may still arrive
    c = rep(c, '''    plant = [q for q in sorted(v["empty"], key=lambda q: (_shed_dist(q), q)) if q not in S["claimed_sites"] and q not in S.get("pending_sites",set())][:n_seeds]''',
    f'''    ring = (day <= {until_day} and S.get("herd_room", 0) > {min_keep})
    plant = [q for q in sorted(v["empty"], key=lambda q: (_shed_dist(q), q)) if q not in S["claimed_sites"] and q not in S.get("pending_sites",set())
             and not (ring and _shed_dist(q) <= {R})][:n_seeds]''')
    c = rep(c, '''    if kind == "plant":
        return tp not in S["claimed_sites"] and tp not in S.get("pending_sites",set()) and t is None and _plant_choice(tp, seeds_left) is not None and hour < 22''',
    f'''    if kind == "plant":
        if day <= {until_day} and S.get("herd_room", 0) > {min_keep} and _shed_dist(tp) <= {R}:
            return False
        return tp not in S["claimed_sites"] and tp not in S.get("pending_sites",set()) and t is None and _plant_choice(tp, seeds_left) is not None and hour < 22''')
    # herd_room = animals still to come (cap - current total), computed in economy()
    c = rep(c, '''    # ---- herd
    pending_place = shed_animals + carried_animals''', '''    # ---- herd
    pending_place = shed_animals + carried_animals
    S["herd_room"] = max(0, KNOBS["max_animals"] - n_total)''')
    return c

write("B12_01_RING2", ring_reserve(src, R=2, until_day=17))
write("B12_02_RING1", ring_reserve(src, R=1, until_day=17))
write("B12_03_RING2_D12", ring_reserve(src, R=2, until_day=12))
# ring2 but only reserve as many ring tiles as animals still to come (keep >=4 unreserved for crops): approximated by min_keep
write("B12_04_RING2_ROOM4", ring_reserve(src, R=2, until_day=17, min_keep=4))
