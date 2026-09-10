#!/usr/bin/env python3
"""Behavioural identity check for the knobbed chassis source (Sep 10):
   O16K with ORCH_ON=0  vs O15_SALE_PRIORITY  -> paired margin must be exactly 0 on every seed
   O16K with ORCH_ON=1  vs O16_ORCH_ON_O15    -> exactly 0
Run: KAGG_FIXED_SHOPS=1 python3 evolve/orch_knobbed_check.py"""
import os, sys, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "evolve"))
import cascade

def variant(on):
    src = open("candidates/O16K_ORCH_KNOBBED.py").read()
    src = re.sub(r"^ORCH_ON = \d", f"ORCH_ON = {on}", src, count=1, flags=re.M)
    p = f"evolve/gen/_o16k_on{on}.py"; os.makedirs("evolve/gen", exist_ok=True)
    open(p, "w").write(src); return p

if __name__ == "__main__":
    os.chdir(ROOT)
    seeds = list(range(1, 7))
    for on, ref in ((0, "candidates/O15_SALE_PRIORITY.py"), (1, "candidates/O16_ORCH_ON_O15.py")):
        r, _ = cascade._eval(variant(on), ref, seeds, "master", jobs=5)
        per = [round(r["per_seed"][s]["a"] - r["per_seed"][s]["b"]) for s in seeds]
        print(f"ORCH_ON={on} vs {os.path.basename(ref)}: per-seed margins {per}  -> {'IDENTICAL' if all(x == 0 for x in per) else 'DIFFERS'}", flush=True)
