import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import marginal_sweep as ms

SEEDS = list(range(301, 311))  # 10 fresh seeds, both-seats -> 20 games per config

print("=" * 30, "COW SWEEP (sheep/geese at O26 defaults)", "=" * 30)
cow_rows = ms.sweep(
    [
        ("cow_base(=defaults)", {}),
        ("cow_maxcow20_land2", {"max_cow": 20, "land_reserve": 2, "max_animals": 40}),
        ("cow_maxcow26_land0", {"max_cow": 26, "land_reserve": 0, "max_animals": 40}),
        ("cow_maxcow32_land0", {"max_cow": 32, "land_reserve": 0, "max_animals": 40}),
    ],
    seeds=SEEDS,
)

print()
print("=" * 30, "SHEEP SWEEP (cows/geese at O26 defaults)", "=" * 30)
sheep_rows = ms.sweep(
    [
        ("sheep_base(=defaults)", {}),
        ("sheep_max20_land2", {"max_sheep": 20, "land_reserve": 2, "max_animals": 40}),
        ("sheep_max26_land0", {"max_sheep": 26, "land_reserve": 0, "max_animals": 40}),
        ("sheep_max32_land0", {"max_sheep": 32, "land_reserve": 0, "max_animals": 40}),
    ],
    seeds=SEEDS,
)

print()
print("=" * 30, "GEESE SWEEP (cows/sheep at O26 defaults)", "=" * 30)
geese_rows = ms.sweep(
    [
        ("geese_0(=defaults)", {}),
        ("geese_2", {"geese": 2, "geese_day_limit": 20, "max_animals": 40}),
        ("geese_4", {"geese": 4, "geese_day_limit": 20, "max_animals": 40}),
        ("geese_8", {"geese": 8, "geese_day_limit": 20, "max_animals": 40}),
    ],
    seeds=SEEDS,
)

print("\nDONE")
