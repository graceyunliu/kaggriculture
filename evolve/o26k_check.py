#!/usr/bin/env python3
"""Identity checks for the K_SELFMODEL chassis source (Sep 11). Run: KAGG_FIXED_SHOPS=1 python3 evolve/o26k_check.py
  all switches off (+ STRAW_UNITS 4.5, HIRE_MAX_MARGINAL 10**9)  vs O15_SALE_PRIORITY  -> paired margin 0 on every seed
  facts off (FERT_PHASE_RULE=0, FERT_IS_INPUT=0)                  vs O25_STRAW_HIREGATE -> 0 on every seed
"""
import os, sys, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "evolve"))
import cascade

def variant(name, **consts):
    src = open("candidates/K_SELFMODEL.py").read()
    for k, v in consts.items():
        src, n = re.subn(rf"^{k} = [^#\n]+", f"{k} = {v!r}", src, count=1, flags=re.M)
        assert n == 1, k
    os.makedirs("evolve/gen", exist_ok=True)
    p = f"evolve/gen/_ksm_{name}.py"; open(p, "w").write(src); return p

if __name__ == "__main__":
    os.chdir(ROOT)
    seeds = list(range(1, 7))
    o15 = variant("o15", ORCH_ON=0, MELON_LATE_FERT=0, MELON_MORNING=0, STRAW_UNITS=4.5, CARROT_UNITS=4.0, HIRE_MAX_MARGINAL=10**9, FERT_PHASE_RULE=0, FERT_IS_INPUT=0)
    o26 = variant("o26", FERT_PHASE_RULE=0, FERT_IS_INPUT=0)
    for f, ref in ((o15, "candidates/O15_SALE_PRIORITY.py"), (o26, "candidates/O26_CARROT_SIZING.py")):
        r, _ = cascade._eval(f, ref, seeds, "master", jobs=5)
        per = [round(r["per_seed"][s]["a"] - r["per_seed"][s]["b"]) for s in seeds]
        print(f"{os.path.basename(f)} vs {os.path.basename(ref)}: {per} -> {'IDENTICAL' if all(x == 0 for x in per) else 'DIFFERS'}", flush=True)
