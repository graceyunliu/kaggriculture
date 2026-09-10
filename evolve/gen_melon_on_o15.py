#!/usr/bin/env python3
"""O17_MELON_ON_O15 (Sep 10): the B4_01 melon late-fert patch (MELON one-shot fertilize at age 7-8 + harvest-before-first-yield
gate) ported onto O15_SALE_PRIORITY, for the fixed-shops panel read that gates a `melon` island."""
import re
src = open("candidates/O15_SALE_PRIORITY.py").read()
def rep(c, old, new):
    assert c.count(old) == 1, f"NOT UNIQUE/FOUND:\n{old}"
    return c.replace(old, new)
# harvest gate: find the _harvestable-style function that computes age then checks c["first"] -- copy O14's hunk context
m = re.search(r"\n(    age = day - t\.get\(\"planted_day\", day\)\n)(    if age < c\[\"first\"\]:\n)", src)
c = src
if "engine: HARVEST before first_yield_day is a silent no-op" not in c:
    # locate exactly as in O12->O14 diff: the line after which the gate was inserted (line 185 in O12)
    o12 = open("candidates/O12_EVENING_DEPOSIT.py").read().splitlines()
    anchor = o12[184]  # 0-based line 185 of O12
    assert c.count(anchor + "\n") >= 1
    # use the first occurrence inside the same function as O12 (verify by neighbourhood)
    i = c.index(anchor + "\n")
    gate = '    if age < c["first"]:\n        return False  # engine: HARVEST before first_yield_day is a silent no-op\n'
    # O15 defines yu/age after the `if not c` check; insert the gate after `age = ...` inside _harvest_ready
    j = c.index("def _harvest_ready("); k = c.index('    age = day - t.get("planted_day", day)\n', j)
    k += len('    age = day - t.get("planted_day", day)\n'); c = c[:k] + gate + c[k:]
c = rep(c, '    if not c or not c["ongoing"] or day > 26:\n', '    if not c or day > 26:\n')
# insert melon rule right after the two lines that followed in O12 (lines 196-197 -> 199-201 in O14)
o14 = open("candidates/O14_EVENING_MELON.py").read()
blk = '''    if not c["ongoing"]:
        if t.get("crop") != "MELON":
            return False
        # B4_01: fertilize melons late in the yield window (age 7-8) -> 6 units by age 9
        return (7 <= age <= 8 and t.get("yield_units", 0) < c["max_yield"]
                and t.get("fertilized_until_day", -1) < day)
'''
pre = o14.split(blk)[0].splitlines()[-2:]   # the two lines preceding the block in O14
key = "\n".join(pre) + "\n"
assert c.count(key) == 1, key
c = c.replace(key, key + blk)
hdr = "# O17_MELON_ON_O15: O15_SALE_PRIORITY + B4_01/O14 melon late-fert patch (MELON fertilize age 7-8, harvest age gate). Panel-read candidate, not promoted.\n"
open("candidates/O17_MELON_ON_O15.py", "w").write(hdr + c); compile(hdr + c, "x", "exec"); print("wrote")
