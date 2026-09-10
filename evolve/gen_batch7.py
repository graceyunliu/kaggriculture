#!/usr/bin/env python3
"""Batch 7 (Sep 9): late-game wheat filler (tapes keep ~58 plants to day 27, sell ~255 wheat at $50)."""
BASE = "candidates/O8_PURE_ANIMAL_THROTTLE.py"
src = open(BASE).read()
def rep(c, old, new, count=1):
    assert old in c, f"NOT FOUND:\n{old}"
    return c.replace(old, new, count)
def write(name, c):
    open(f"candidates/{name}.py", "w").write(c); compile(c, name, "exec"); print("wrote", name)

def late_cutoff(c, wheat=26, carrot=26):
    c = rep(c, '''"WHEAT":      {"seed": 10,  "units": 5.0, "first": 2,  "cycle": 5,  "cutoff": 24,''',
               f'''"WHEAT":      {{"seed": 10,  "units": 5.0, "first": 2,  "cycle": 5,  "cutoff": {wheat},''')
    c = rep(c, '''"CARROT":     {"seed": 20,  "units": 4.0, "first": 2,  "cycle": 4,  "cutoff": 25,''',
               f'''"CARROT":     {{"seed": 20,  "units": 4.0, "first": 2,  "cycle": 4,  "cutoff": {carrot},''')
    return c

def day29_hands(c, n=12):
    return rep(c, '''    if day >= 29:
        tgt = min(tgt, 6)''', f'''    if day >= 29:
        tgt = min(tgt, {n})''')

c1 = late_cutoff(src); write("B7_01_LATE_WHEAT26", c1)
c2 = day29_hands(c1); write("B7_02_LATE_WHEAT26_H12", c2)
c3 = day29_hands(late_cutoff(src, 27, 27)); write("B7_03_LATE_WHEAT27_H12", c3)
# sell-window: late one-shot crops harvested only when full or day>=29; allow harvest at age>=max_day-? no change.
# B7_04: also let the seed loop place more than 4 orders/day late and allow wheat to bypass the value filter after day 20
c4 = rep(c2, '''                if val < sp_["min_val"]:
                    continue''', '''                if val < sp_["min_val"] and not (c == "WHEAT" and day >= 20):
                    continue''')
write("B7_04_LATE_WHEAT26_H12_NOMINVAL", c4)
# B7_05: c4 + wheat_cap raised so the late wheat isn't capped by the 22-tile cap
c5 = rep(c4, "'wheat_cap': 22", "'wheat_cap': 60"); write("B7_05_LATE_WHEAT_CAP60", c5)
