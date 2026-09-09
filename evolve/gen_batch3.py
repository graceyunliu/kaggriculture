#!/usr/bin/env python3
"""Batch 3 (Sep 9): day-10 melon first-mover WITHOUT extra early labor."""
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()
exec(open("evolve/gen_batch2.py").read().split("# B2_01")[0].replace('BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"\nsrc = open(BASE).read()', ""))

def melon_early_harvest(c, min_units=4):
    # harvest melons on the first legal day at >= min_units instead of waiting for 6 (day 11)
    c = rep(c, '''    if KNOBS["melon_rush"] and t.get("crop") == "MELON" and age >= c["first"] and yu >= 5:
        return True
    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''',
    f'''    if t.get("crop") == "MELON" and age >= c["first"] and yu >= {min_units}:
        return True
    if age < c["first"]:
        return False
    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''')
    return c

def melon_return(c, thresh=6, last_day=11):
    # a hand carrying a full tile of melons on the first melon days heads to the shed so the
    # sale lands before the frontier's day-10 dump (no fertilizer, no early-game labor)
    c = rep(c, '''    # 2a. melon rush: carried melons go straight to the shed to sell into the day-10 price
    if KNOBS["melon_rush"] and 10 <= day <= 14 and carry.get("MELON", 0) >= 4 and carry.get("WHEAT", 0) == 0 and i not in S["routes"]:''',
    f'''    # 2a. melon return: a full tile of melons on the first melon days goes straight to the shed
    if 10 <= day <= {last_day} and carry.get("MELON", 0) >= {thresh} and carry.get("WHEAT", 0) == 0 and i not in S["routes"]:''')
    return c

c1 = melon_priority(melon_early_harvest(src, 4)); write("B3_01_MELON_H4_PRIO", c1)
c2 = melon_return(c1, 6, 11); write("B3_02_MELON_H4_PRIO_RETURN", c2)
c3 = melon_priority(melon_early_harvest(src, 5)); write("B3_03_MELON_H5_PRIO", c3)
c4 = melon_return(c3, 5, 11); write("B3_04_MELON_H5_PRIO_RETURN5", c4)
c5 = melon_return(src, 4, 14); c5 = rep(c5, "'melon_rush': 0", "'melon_rush': 1"); write("B3_05_MELON_RUSH_REF", c5)
# B3_06: early-harvest only, no priority tier, no return (pure "harvest instead of water on day 10")
c6 = melon_early_harvest(src, 4); write("B3_06_MELON_H4_ONLY", c6)
