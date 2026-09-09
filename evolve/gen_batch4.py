#!/usr/bin/env python3
"""Batch 4 (Sep 9): late-window melon fertilization (age 7-8) -> 6 units by day 9 -> sell day 10 early."""
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()
exec(open("evolve/gen_batch2.py").read().split("# B2_01")[0].replace('BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"\nsrc = open(BASE).read()', ""))
exec(open("evolve/gen_batch3.py").read().split("c1 = ")[0].split('exec(open("evolve/gen_batch2.py")')[0].replace('BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"\nsrc = open(BASE).read()', ""))
# re-define helpers from batch3 (they were after the exec line)
def melon_return(c, thresh=6, last_day=11):
    c = rep(c, '''    # 2a. melon rush: carried melons go straight to the shed to sell into the day-10 price
    if KNOBS["melon_rush"] and 10 <= day <= 14 and carry.get("MELON", 0) >= 4 and carry.get("WHEAT", 0) == 0 and i not in S["routes"]:''',
    f'''    # 2a. melon return: a full tile of melons on the first melon days goes straight to the shed
    if 10 <= day <= {last_day} and carry.get("MELON", 0) >= {thresh} and carry.get("WHEAT", 0) == 0 and i not in S["routes"]:''')
    return c

def melon_late_fert(c, lo=7, hi=8):
    c = rep(c, '''def _fert_eligible(t, day):
    c = CROPS.get(t.get("crop"))
    if not c or not c["ongoing"] or day > 26:
        return False
    age = day - t.get("planted_day", day)''',
    f'''def _fert_eligible(t, day):
    c = CROPS.get(t.get("crop"))
    if not c or day > 26:
        return False
    age = day - t.get("planted_day", day)
    if not c["ongoing"]:
        if t.get("crop") != "MELON":
            return False
        # melon: fertilize late in the yield window (age {lo}-{hi}) so the remaining waterings
        # count double -> 6 units by age 9 -> harvest+sell day 10 ahead of the day-10 dump,
        # and the labor lands on days 7-8 (more hands) instead of days 5-6
        return ({lo} <= age <= {hi} and t.get("yield_units", 0) < c["max_yield"]
                and t.get("fertilized_until_day", -1) < day)''')
    c = rep(c, '''    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''',
               '''    if age < c["first"]:
        return False  # engine: HARVEST before first_yield_day is a silent no-op
    return yu >= c["max_yield"] or age >= c["max_day"] or day >= 29''')
    return c

c1 = melon_late_fert(src); write("B4_01_MELON_LATEFERT", c1)
c2 = melon_priority(c1); write("B4_02_MELON_LATEFERT_PRIO", c2)
c3 = melon_return(c2, 6, 11); write("B4_03_MELON_LATEFERT_PRIO_RET", c3)
c4 = rep(c3, "'fert_keep': 0", "'fert_keep': 6"); write("B4_04_MELON_LATEFERT_PRIO_RET_KEEP", c4)
