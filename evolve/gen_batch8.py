#!/usr/bin/env python3
"""Batch 8 (Sep 9): herd sizing should not be capped by milk/yarn shop presence — every placed animal
yields 1 fertilizer/day unconditionally (engine) plus wool/milk floor value; the frontier runs 17 regardless."""
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

def no_shop_caps(c):
    c = rep(c, '''            if sp == "SHEEP":
                yarn = _instances(obs, "WOOL")
                if yarn == 0:
                    room = min(room, 2 - my_counts[sp])
                elif prices.get("WOOL", 0) >= 1.05 * 200 and day >= 8:
                    room = max(room, 2)
                room = min(room, MAX_SHEEP - my_counts[sp])
            else:
                if _instances(obs, "MILK") == 0 and day >= 9:
                    room = min(room, 4 - my_counts[sp])''',
    '''            if sp == "SHEEP":
                if prices.get("WOOL", 0) >= 1.05 * 200 and day >= 8:
                    room = max(room, 2)
                room = min(room, MAX_SHEEP - my_counts[sp])''')
    return c

def herd_floor(c, cap=17, start=4, per_day=1.0):
    # frontier-style schedule floor: the herd should reach `cap` by ~day 13 regardless of shop luck,
    # because fertilizer (1/animal/day, glut-resistant) plus wool/milk floor value pays for feed
    c = rep(c, '''            room = _demand_room(obs, v, sp, day, my_counts[sp], opp_count s[sp])''' if False else
               '''            room = _demand_room(obs, v, sp, day, my_counts[sp], opp_counts[sp])''',
    f'''            room = _demand_room(obs, v, sp, day, my_counts[sp], opp_counts[sp])
            sched = min({cap}, int({start} + {per_day} * day))
            room = max(room, sched - n_total)''')
    return c

c1 = no_shop_caps(src); write("B8_01_NO_SHOP_CAPS", c1)
c2 = rep(c1, "'demand_share': 0.55", "'demand_share': 1.0"); write("B8_02_NO_CAPS_SHARE1", c2)
c3 = herd_floor(c1); write("B8_03_HERD_SCHED17", c3)
c4 = rep(c3, "'wheat_per_animal': 0.0", "'wheat_per_animal': 0.5"); write("B8_04_HERD_SCHED17_WHEAT05", c4)
c5 = herd_floor(c1, cap=14); write("B8_05_HERD_SCHED14", c5)
c6 = herd_floor(src, cap=17); write("B8_06_HERD_SCHED17_KEEPCAPS", c6)
