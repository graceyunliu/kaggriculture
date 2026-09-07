#!/usr/bin/env python3
"""
repro_rng_path_dependence.py

MINIMAL ANALOGUE of the production RNG mechanism found in
vendor/kaggle_environments_engine_master/kaggriculture.py::_end_of_day()
(lines ~869-891).

This is NOT the production engine. It is a faithful, deliberately shrunk
model of the exact code shape that matters:

    rng = random.Random((seed * 1_000_003) ^ day)      # fresh RNG each day
    for tile in board:
        if tile is None and rng.random() < weed_chance: # <-- SHORT-CIRCUITED:
            tile = WEED                                #     draw only fires
                                                          #     on empty tiles
    if day_boundary_for_shop_unlock:
        town.append(rng.choice(SHOPS))                  # <-- same rng object,
                                                          #     drawn AFTER
                                                          #     the weed loop

The number of rng.random() calls consumed by the weed loop on a given day
depends on how many board tiles are None (empty) at that point -- which is
policy-dependent (a policy that plants more tiles leaves fewer empty tiles).
Because the shop-unlock draw reuses the SAME rng object immediately after,
its outcome can differ between two policies even though both start from the
identical per-day seed `(seed * 1_000_003) ^ day`.

This script demonstrates that mechanism directly and measures its effect.
"""

import random
import copy
import json

SEED = 12345
BOARD_SIZE = 10
WEED_CHANCE = 0.005
SHOPS = ["FARM_SUPPLY", "PIZZA_SHOP", "BAKERY", "ICE_CREAM_SHOP",
         "BUTCHER", "SMOOTHIE_SHOP", "DAIRY", "GENERAL_STORE"]
MAX_SHOP_INSTANCES = 8
SHOP_UNLOCK_INTERVAL = 3


def make_board(board_size, occupied_fraction, occupied_rng):
    """Build a board where `occupied_fraction` of tiles are pre-occupied
    (simulating a policy that plants more tiles). Occupancy pattern itself
    uses a SEPARATE rng so this is purely about draw *count*, not which
    tiles specifically are empty."""
    board = [[None for _ in range(board_size)] for _ in range(board_size)]
    for y in range(board_size):
        for x in range(board_size):
            if occupied_rng.random() < occupied_fraction:
                board[y][x] = "CROP"
    return board


def spawn_weeds(board, board_size, weed_chance, rng):
    """Exact structural copy of production _spawn_weeds()."""
    draws = 0
    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] is None:
                draws += 1
                if rng.random() < weed_chance:
                    board[y][x] = "WEED"
    return draws


def run_day(seed, day, occupied_fraction, occupied_rng_seed):
    """Faithful analogue of _end_of_day(): fresh per-day rng, weeds first,
    then (on unlock-interval days) a shop draw from the SAME rng object."""
    rng = random.Random((seed * 1_000_003) ^ day)

    occ_rng = random.Random(occupied_rng_seed)
    board = make_board(BOARD_SIZE, occupied_fraction, occ_rng)

    draws_before_shop = spawn_weeds(board, BOARD_SIZE, WEED_CHANCE, rng)

    shop_pick = None
    next_day = day + 1
    if next_day > 0 and next_day % SHOP_UNLOCK_INTERVAL == 0:
        shop_pick = rng.choice(sorted(SHOPS))

    weed_count = sum(1 for row in board for cell in row if cell == "WEED")
    return {
        "day": day,
        "occupied_fraction": occupied_fraction,
        "weed_draws_consumed": draws_before_shop,
        "weeds_spawned": weed_count,
        "shop_pick": shop_pick,
    }


def main():
    print("=" * 78)
    print("RNG PATH-DEPENDENCE MINIMAL ANALOGUE")
    print(f"seed={SEED}  board={BOARD_SIZE}x{BOARD_SIZE}  weed_chance={WEED_CHANCE}")
    print("=" * 78)

    # Two "policies": POLICY_SPARSE plants little (many empty tiles ->
    # many weed rng.random() draws consumed before the shop draw).
    # POLICY_DENSE plants heavily (few empty tiles -> few draws consumed).
    # Both use an IDENTICAL occupied_rng_seed per day so tile-occupancy
    # patterns for a given fraction are comparable across the run; only
    # the *fraction* (a stand-in for "policy plants more/fewer tiles")
    # differs, exactly mirroring how two real policies leave different
    # numbers of None tiles on the same day.
    policies = {
        "POLICY_SPARSE (10% occupied -> ~90 empty tiles/day)": 0.10,
        "POLICY_DENSE  (90% occupied -> ~10 empty tiles/day)": 0.90,
    }

    checkpoints = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]  # day-boundaries checked
    results = {}

    for label, frac in policies.items():
        print(f"\n--- {label} ---")
        rows = []
        for day in range(0, 30):
            occ_seed = (SEED * 7919) ^ day  # deterministic, same across policies for a fixed day
            r = run_day(SEED, day, frac, occ_seed)
            rows.append(r)
            if (day + 1) in checkpoints:
                print(f"  day={day:2d}  weed_draws_consumed={r['weed_draws_consumed']:3d}  "
                      f"weeds_spawned={r['weeds_spawned']:2d}  shop_unlock_pick={r['shop_pick']}")
        results[label] = rows

    # Compare shop picks across the two policies on unlock-interval days.
    print("\n" + "=" * 78)
    print("DIVERGENCE CHECK: same seed, same day, different policy occupancy")
    print("=" * 78)
    labels = list(policies.keys())
    rows_a = results[labels[0]]
    rows_b = results[labels[1]]
    divergences = []
    for ra, rb in zip(rows_a, rows_b):
        if ra["shop_pick"] is not None:
            same = ra["shop_pick"] == rb["shop_pick"]
            divergences.append({
                "day": ra["day"],
                "draws_A": ra["weed_draws_consumed"],
                "draws_B": rb["weed_draws_consumed"],
                "shop_A": ra["shop_pick"],
                "shop_B": rb["shop_pick"],
                "same_pick": same,
            })
            marker = "SAME" if same else "DIVERGED"
            print(f"  day={ra['day']:2d}  draws A={ra['weed_draws_consumed']:3d} vs "
                  f"B={rb['weed_draws_consumed']:3d}  shop_pick A={ra['shop_pick']!r:16s} "
                  f"B={rb['shop_pick']!r:16s}  -> {marker}")

    n_diverged = sum(1 for d in divergences if not d["same_pick"])
    print(f"\nTotal shop-unlock checkpoints: {len(divergences)}")
    print(f"Diverged (different shop unlocked despite identical seed): {n_diverged}")
    print(f"Same pick despite different draw counts: {len(divergences) - n_diverged}")

    out = {
        "seed": SEED,
        "policies": {k: v for k, v in policies.items()},
        "per_day_results": results,
        "divergence_summary": divergences,
        "n_diverged": n_diverged,
        "n_checkpoints": len(divergences),
    }
    with open("rng_path_dependence_results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)
    print("\nFull results written to rng_path_dependence_results.json")


if __name__ == "__main__":
    main()
