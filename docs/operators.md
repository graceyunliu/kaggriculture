# Paired search operators (Sep 4)

## Why

`evolve/RULES.md`'s routing-oracle finding: making the router free is ~0 on average vs C1
because the economy doesn't generate enough obligations to use freed labor, and porting the
opponent's allocation onto our dispatcher loses -$68k. Allocation-only and execution-only
mutations have both been measured to fail; the frontier's edge is *paired* — more obligations
(herd/crop/seed sizing) generated **and** an execution change that services them (sweep/
dispatch/animal_routing/crop_admission). Plain `space.mutate()` picks a random subset of knobs
with no regard for this split, so most of its children are allocation-only or execution-only
by chance. `evolve/operators.py` forces the pairing.

## What it does

- **`ECON_KEYS` / `EXEC_KEYS`** (`evolve/operators.py`): every key of `space.SPACE` classified
  into allocation/economy vs execution/labor (see table below). One key, `OPP_GROWTH`, scales
  the *opponent's* tape rather than our own allocation or execution, so it lands in a third,
  unused bucket — logged at import time, excluded from the paired operators. All keys are
  covered by an assertion; run `python3 -c "import sys;sys.path.insert(0,'evolve');sys.path.insert(0,'.');import operators as o;print(len(o.ECON_KEYS), len(o.EXEC_KEYS), o.UNKNOWN_KEYS)"` to see the split for the live chassis.

- **`paired_mutate(params, rng, sigma_frac)`**: mutates exactly one `ECON_KEYS` entry and
  exactly one `EXEC_KEYS` entry (same Gaussian/flip clamp semantics as `space.mutate`, applied
  per-key so the "exactly one from each bucket" guarantee is deterministic given `rng`),
  leaves every other key untouched.

- **`block_pair_mutate(params, blocks, rng, library)`**: mutates one `ECON_KEYS` entry **and**
  swaps one execution block (`sweep`, `animal_routing`, `dispatch`, or `crop_admission`) for a
  random alternative source pulled from `evolve/blocks/*.py` (grouped by which block's required
  functions a file defines, via `evolve/blocks.py`'s `BLOCKS`). `None` in the library (chassis
  default) is always included and drawn first-in-list.

- **`coupled_grid(base_params, econ_axes, exec_axes, block_options)`**: full factorial
  generator over econ knobs × exec knobs × block choices, yielding `(params, blocks, tag)`.

- **CLI**: `python3 evolve/operators.py grid --out evolve/queue/coupled_grid_sep04.json`
  writes a `{"kind":"factorial", ...}` queue item that `loop.py`'s `consume_queue()` already
  knows how to expand (`base`, `axes`, `block_options`, `origin`, `note`). Caps at 64
  candidates; a larger grid prints the count and refuses unless `--allow-large` is passed.

## ECON / EXEC classification

| Bucket | Keys |
|---|---|
| EXEC (9) | `min_hands`, `load_per_hand`, `early_hire_days`, `harvest_min`, `MAX_HANDS`, `ROUTE_LEN`, `CROP_SWEEP_LEN`, `CROP_SWEEP_RADIUS`, `NEAR_RADIUS` |
| UNKNOWN (1, excluded) | `OPP_GROWTH` (scales the opponent tape, not our own allocation/execution) |
| ECON (everything else in `space.SPACE`) | `opening`, `demand_share`, `max_animals`, herd/species sizing (`open_cows`, `open_sheep`, `geese`, `herd_species_bias`, `HERD_LAST_DAY`, `MAX_SHEEP`), wheat knobs (`wheat_tiles`, `wheat_stock`, `wheat_per_animal`, `wheat_cap`, `wheat_water_tier`, `wheat_sell_price`, `wheat_hold_days`), melon knobs (`open_melons`, `melon_floor`, `MELON_MAX_TILES`, `MELON_PRICE_CUSHION`, `OPENING_MELONS`), fertilizer (`fert_keep`, `fert_buy`, `fert_carry`), all 20 `spec_units/cycle/cutoff/minval_{STRAWBERRY,MELON,WHEAT,CARROT,TOMATO}`, `STRAW_CUTOFF`, `seed_orders_cap`, `land_deadline_shift`, `sell_order`, `feed_spare_poor` |

Counts are computed dynamically from the live chassis (some `SPACE` keys are skipped with a
warning if the chassis hasn't been rebuilt to carry them yet — see `space.py`'s
`_warn_once`), so the exact numbers can shift; run the one-liner above for the current split.

## Enabling in the loop

`evolve/loop.py` gained one `generate_one` branch and one flag:

```bash
python3 evolve/loop.py --hours 2 --paired-rate 0.3
```

`--paired-rate F` sets `ISLANDS["c1"]["paired"] = ISLANDS["wide"]["paired"] = F` (default 0.0,
i.e. no behaviour change unless passed). When a non-crossover child is generated on the `c1`
or `wide` island, with probability `cfg.get("paired", 0.0)` it comes from `paired_mutate`
(origin `"paired"`) instead of `space.mutate`; within that branch, with probability
`cfg.get("block_pair", 0.0)` (0 unless set some other way — no CLI flag added for it yet, wire
it the same way as `--paired-rate` if wanted) it uses `block_pair_mutate` instead (origin
`"block_pair"`). Everything else in `loop.py` — pools, ablation, queue consumption, reporting —
is unchanged.

## The grid file

`evolve/queue/coupled_grid_sep04.json`: a single `factorial` queue item.

- **base**: `"c1"` (i.e. `space.c1_params()`) with fixed overrides matching the E1-style
  banded-siting candidate: `melon_floor=200, load_per_hand=16, open_melons=10, open_wheat=8,
  wheat_water_tier=1, wheat_sell_price=29, CROP_SWEEP_LEN=5, MELON_MAX_TILES=50,
  HERD_LAST_DAY=22, NEAR_RADIUS=2, OPP_GROWTH=1.1`.
- **econ axes**: `demand_share ∈ {0.5, 0.6}`, `open_melons ∈ {10, 12}`,
  `wheat_per_animal ∈ {0.0, 0.3}`.
- **exec axes**: `load_per_hand ∈ {16, 12}`, `MAX_HANDS ∈ {13, 15}`.
- **block_options**: `sweep` (chassis default + `lib_a_full_sweep.py` +
  `lib_b_harvest_first_melon.py`), `dispatch` (chassis default + `lib_d_opportunistic_deposit.py`
  + `dispatch_idledrop.py`) — both drawn from files under `evolve/blocks/` whose names start
  with `lib_`, `dispatch_`, or `animal_routing_`, filtered to files that actually define that
  block's required functions; `crop_admission` fixed to the banded block
  (`evolve/blocks_banded_crop_admission.py`) via a single-option axis so every cell in the grid
  gets it without adding a combinatorial dimension.
- **size**: 2×2×2 (econ) × 2×2 (exec) × 3 (sweep) × 3 (dispatch) × 1 (crop_admission) = **288
  candidates** — over the 64-candidate default cap, so `operators.py grid` refused to write it
  without `--allow-large` (printed `grid: 288 candidates` and exited 1) and was then written
  with `--allow-large`.

## Test output (Sep 4)

```
$ python3 -c "...;import operators as o; print(len(o.ECON_KEYS), len(o.EXEC_KEYS))"
50 9

$ paired_mutate on c1_params(), 20 seeded trials:
all pass   # every trial: exactly 2 keys differ, one ECON one EXEC

$ mini_engine.py <3 paired children + 2 block-pair children> candidates/V3_12.py --seeds 1
agent errors [0, 0]   # for all 5 (margins ranged -$8,488 to +$7,974 vs V3_12, seed 1 only —
                       # not a selection result, just an error/crash smoke check)

$ python3 evolve/operators.py grid --out evolve/queue/coupled_grid_sep04.json
grid: 288 candidates
refusing to write: 288 > 64 candidates; pass --allow-large to override   # exit 1

$ python3 evolve/operators.py grid --out evolve/queue/coupled_grid_sep04.json --allow-large
grid: 288 candidates
wrote evolve/queue/coupled_grid_sep04.json (288 candidates)

$ python3 -c "import json;json.load(open('evolve/queue/coupled_grid_sep04.json'))"
# parses clean; kind=factorial, keys = kind/base/axes/block_options/origin/note

$ python3 evolve/loop.py --help
# shows --paired-rate PAIRED_RATE
```

## Files

- `evolve/operators.py` — the operators + grid CLI (new).
- `evolve/loop.py` — `generate_one` gained the paired/block_pair branch;
  `main()` gained `--paired-rate`. Nothing else in the file changed.
- `evolve/queue/coupled_grid_sep04.json` — the generated factorial (queued for the next run;
  `loop.py` moves it to `evolve/queue/done/` once consumed).
- `docs/operators.md` — this file.
