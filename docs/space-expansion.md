# Search-space expansion (Sep 4)

Adds new mutation surface to `candidates/K.py` and wires it into `evolve/space.py`'s
`KNOB_SPACE`. All new knobs default to a value that reproduces current (V3.12) behaviour
exactly — verified by a 3-seed both-seats run vs `candidates/V3_12.py` showing margin
$+0 and 0 agent errors on both sides (see Verification below).

## New knobs (candidates/K.py)

Per-crop overrides — read at runtime via a new `_spec(c, field)` helper
(`CROP_SPECS[c][field]` unless a `spec_<field>_<crop>` knob overrides it; `None` = use
the `CROP_SPECS` default). Wired into every allocator site that previously read
`CROP_SPECS[c][...]` / `sp_["..."]` directly (the seed-value scorer, the room-units
calc, the per-crop seed-count cap, and the WHEAT tile-floor accounting).

| knob | default | range in KNOB_SPACE | meaning |
|---|---|---|---|
| `spec_units_<crop>` | `None` | cat, `[None, ±40% of base]` | units/tile override |
| `spec_cycle_<crop>` | `None` | cat, `[None, ±40% of base]` | sell-cycle-length override |
| `spec_cutoff_<crop>` | `None` | cat, `[None, base±4 days]` | last planting day override |
| `spec_minval_<crop>` | `None` | cat, `[None, 6, 12, 18, 24, 30]` | min $/cycle-day to plant override |

(for STRAWBERRY, MELON, WHEAT, CARROT, TOMATO — 20 knobs total)

| knob | default | range | meaning |
|---|---|---|---|
| `seed_orders_cap` | `4` | int, 2–6 | replaces the hard-coded `n_seed_orders < 4` cap in the seed allocator loop |
| `land_deadline_shift` | `0` | int, −4..+4 | added to every `LAND_DEADLINE[quads+1]` lookup |
| `sell_order` | `"default"` | cat, `["default","perishables_first","fert_first"]` | selects a fixed sell-ordering tuple from a new `SELL_ORDERS` dict |
| `herd_species_bias` | `0.0` | float, −2.0..2.0 step 0.5 | added to SHEEP room / subtracted from COW room in the herd-sizing loop (clamped ≥ 0); `0.0` is a no-op (branch is skipped entirely) |

All 24 new knobs are additive lines — no existing logic was rewritten, only
`CROP_SPECS[c][field]` reads replaced with `_spec(c, field)`, the `4` in the seed loop
replaced with `KNOBS["seed_orders_cap"]`, `LAND_DEADLINE[...]` given a `+ KNOBS["land_deadline_shift"]`
term, the fixed sell tuple replaced with `SELL_ORDERS.get(KNOBS["sell_order"], ...)`, and
one small `if KNOBS["herd_species_bias"]:` block inserted before the existing SHEEP/COW room
calc.

## Tolerance for an un-rebuilt chassis (evolve/space.py)

`evolve/space.py` renders candidates from `evolve/chassis.py`, a frozen file the owner
rebuilds from `candidates/K.py` with `python3 evolve/blocks.py build` — NOT automatically
kept in sync. Until that rebuild happens, the new knobs above don't exist in the frozen
chassis's `KNOBS` dict yet.

- `_read_base()` no longer asserts every `CONST_SPACE` name exists — a missing constant
  triggers one `_warn_once()` message to stderr and is skipped.
- A new `_live_knob_space()` returns only the `KNOB_SPACE` keys present in the current
  chassis's `KNOBS` dict, warning once (via the same `_warn_once`) for each one that's
  missing.
- `base_params()` uses `_live_knob_space()`, so its dict only contains keys the live
  chassis actually understands — it grows automatically the next time the owner rebuilds
  the chassis, no code change needed here.
- `mutate()`, `crossover()`, `params_key()`, `diff()` all now operate over
  `SPACE ∩ params.keys()` instead of the full `SPACE`, so old candidate dicts (missing
  the new keys) still mutate/hash/diff correctly, and `params_key()` for an *old*
  candidate (built before this change) is unaffected — only params dicts that already
  carry the new keys get them folded into the hash.
- `render()` now guards both the per-knob substitution loop and the per-constant regex
  substitution with `if k in knobs`/`if name not in params: continue`, so rendering
  against an old chassis silently drops knobs it doesn't have instead of raising.
- Fixed a latent bug surfaced by adding `None`-valued knobs: `render()` was serializing
  the `KNOBS` dict with `json.dumps()` but the dict is read back with Python's `eval()`
  — `json.dumps(None)` produces `null`, which is not valid Python and crashed the
  chassis at import time. Switched to `repr(knobs)`, which round-trips through `eval()`
  correctly for `None`/`True`/`False`/dicts alike. (This bug existed before this change
  too, for any candidate that happened to render a `None` knob value — it just hadn't
  been hit yet.)

## Verification (run from `Kaggriculture/` project root)

```
$ python3 -c "import ast;ast.parse(open('candidates/K.py').read())"
(no output — parses clean)

$ python3 mini_engine.py candidates/K.py candidates/V3_12.py --seeds 1 2 3 --both-seats --no-cache
K.py vs V3_12.py  engine=master config={}
seeds=3 both_seats=True
mean A $88,126  mean B $88,126  margin/game $+0  t=inf
seed-wins 0-0   seat0 wins 0  seat1 wins 3   agent errors [0, 0]
  seed     1: margin +0   seat0:-3,617  seat1:+3,617
  seed     2: margin +0   seat0:-1,813  seat1:+1,813
  seed     3: margin +0   seat0:-67  seat1:+67
```
Confirms K.py with all-default knobs is byte-for-byte behaviourally identical to V3.12
(margin $+0 every seed, 0 agent errors on both sides).

```
$ python3 -c "import sys;sys.path.insert(0,'evolve');sys.path.insert(0,'.');import space;p=space.c1_params();print(len(p));print(space.render(p))"
36
evolve/gen/cand_913fb0b0694b.py
```
`render()` against the *current* (not-yet-rebuilt) `evolve/chassis.py` still works —
`base_params()`/`c1_params()` silently drop the 24 new knobs (one warning per name to
stderr) and render the remaining 36 keys as before, so nothing already using
`evolve/space.py` breaks.

Fresh chassis built to a temp path (`evolve/chassis.py` was NOT touched):
```
$ python3 -c "import sys;sys.path.insert(0,'evolve');import blocks;blocks.build('candidates/K.py','/tmp/chassis_new.py')"
built
```
Pointed `space.K_LIVE` at `/tmp/chassis_new.py` and re-froze; `c1_params()` then returns
**60** params (36 old + 24 new) with no warnings. Rendered one candidate with a
non-default value in every new knob group (`spec_units_STRAWBERRY=6.3`,
`spec_cycle_MELON=9`, `spec_cutoff_WHEAT=22`, `spec_minval_CARROT=24`,
`spec_units_TOMATO=7.0`, `seed_orders_cap=6`, `land_deadline_shift=2`,
`sell_order="perishables_first"`, `herd_species_bias=1.5`) and ran it 2 seeds vs V3.12:

```
$ python3 mini_engine.py <rendered candidate> candidates/V3_12.py --seeds 1 2 --both-seats --no-cache
cand_976b621d09cb.py vs V3_12.py  engine=master config={}
seeds=2 both_seats=True
mean A $84,151  mean B $86,112  margin/game $-1,962  t=-0.45
seed-wins 1-1   seat0 wins 1  seat1 wins 1   agent errors [0, 0]
  seed     1: margin +4,703   seat0:+301  seat1:+4,402
  seed     2: margin -12,549   seat0:-4,873  seat1:-7,676
```
Zero agent errors on both sides with every new knob active and non-default — the new
mutation surface runs clean end to end (not evaluated for quality here, just wired
correctly; that non-default combination happens to be a slight loser at n=2, unsurprising
since it wasn't tuned).

## To activate the new knobs in the live search

The owner must rebuild the frozen chassis from `candidates/K.py`:

```
python3 evolve/blocks.py build
```

This overwrites `evolve/chassis.py` in place. **All existing candidate `params_key`
values will change** the next time a run touches a params dict that includes the new
knobs (any dict produced by a fresh `base_params()`/`mutate()`/`crossover()` call after
the rebuild will carry the new keys, so its hash differs from a pre-rebuild dict with the
same values on the shared keys) — old archived candidates and their cached scores remain
valid and readable (their stored params dicts simply lack the new keys, and
`params_key()`/`diff()`/`mutate()` all tolerate that), but any *new* dict generated after
the rebuild will not collide with an old one even if all shared knobs match. This is the
same "chassis snapshot is part of identity" behaviour `evolve/space.py` already documents
via `BASE_SHA`.
