import sys, statistics
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import marginal_sweep as ms

ROOT = Path(__file__).resolve().parents[2]
ms.OPPONENTS.update({
    "opp_soil_v25": str(ROOT / "Opponents/opp_soil_v25.py"),
    "opp_kaito_v21": str(ROOT / "Opponents/opp_kaito_v21.py"),
})

SEEDS = list(range(401, 431))  # 30 fresh seeds, disjoint from exploratory (301-310) and smoke (101-105/201-202)

CONFIGS = [("O26_baseline", {}), ("sheep_max32_land0", {"max_sheep": 32, "land_reserve": 0, "max_animals": 40})]

overall = {}
for opp_key in ("tape_feeltheagi", "opp_soil_v25", "opp_kaito_v21"):
    print("\n" + "#" * 20, opp_key, "#" * 20)
    rows = ms.sweep(CONFIGS, seeds=SEEDS, opp_key=opp_key)
    overall[opp_key] = rows

print("\n" + "=" * 20, "SUMMARY ACROSS OPPONENTS", "=" * 20)
for opp_key, rows in overall.items():
    base, var = rows
    d_margin = var["mean_margin"] - base["mean_margin"]
    d_money = var["mean_own_money"] - base["mean_own_money"]
    print(f"{opp_key}: base_margin={base['mean_margin']:+.0f}(t={base['t']:.2f}) var_margin={var['mean_margin']:+.0f}(t={var['t']:.2f}) "
          f"d_margin={d_margin:+.0f}  base_money={base['mean_own_money']:.0f} var_money={var['mean_own_money']:.0f} d_money={d_money:+.0f}")
