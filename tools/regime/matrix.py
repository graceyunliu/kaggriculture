#!/usr/bin/env python3
"""Regime matrix: candidates x opponent pools (R0 mirror tapes, R1 basin-B tapes, R2 own-code), held-out seeds both seats."""
import json, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
import mini_engine as me
POOLS = {
 "R0": ["Opponents/tape_strawhats_105080848.py","Opponents/tape_yuan800_104892947.py","Opponents/tape_atakan_104893687.py","Opponents/tape_iamlonely_105603965.py","Opponents/tape_yangkuang_105603038.py"],
 "R1": ["Opponents/tape_shirabe_105076319.py","Opponents/tape_kiro_105078932.py","Opponents/tape_antigone_105079803.py"],
 "R2": ["candidates/V3_12.py","candidates/E1.py","Opponents/opp_scenario_v14.py"],
}
CANDS = sys.argv[1:] or ["C1","E1","E_block","E_daba","E_e4a4","E_fert1_block","H10","H12","H30","H31","H32","P5","V3_11","V3_12","V3_29","M1_k1"]
SEEDS = list(range(11, 31))
out = ROOT / "tools/regime/matrix.json"
res = json.load(open(out)) if out.exists() else {}
for c in CANDS:
    cp = f"candidates/{c}.py"
    if not (ROOT / cp).exists(): print("missing", cp); continue
    for reg, opps in POOLS.items():
        for o in opps:
            key = f"{c}|{reg}|{Path(o).stem}"
            if key in res: continue
            t0 = time.time()
            r = me.evaluate(str(ROOT / cp), str(ROOT / o), SEEDS, both_seats=True, jobs=4)
            res[key] = {"margin": r["mean_margin_per_game"], "t": r["t"], "wins": r["wins"], "losses": r["losses"], "mean_a": r["mean_a"], "mean_b": r["mean_b"], "errors": r["agent_errors"]}
            json.dump(res, open(out, "w"), indent=1)
            print(key, res[key]["margin"], round(time.time()-t0), "s", flush=True)
