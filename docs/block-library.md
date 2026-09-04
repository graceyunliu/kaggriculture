# Block library (Sep 4) — lib_A..lib_E

Five execution-layer block replacements evaluated on the chassis, rendered on E1's params
(`melon_floor 200, load_per_hand 16, open_melons 10, open_wheat 8, wheat_water_tier 1,
wheat_sell_price 29, CROP_SWEEP_LEN 5, MELON_MAX_TILES 50, HERD_LAST_DAY 22, NEAR_RADIUS 2,
OPP_GROWTH 1.1`) with the banded crop_admission block underneath (unless the block replaces
crop_admission itself). Baseline render (`candidates/gen_lib/base_e1.py`) verified to reproduce
`candidates/E1.py` exactly: margin $+0 on seeds 1-2 both-seats.

All margins below are seeds 1-6, both-seats, mini_engine master, "A" = candidate, "B" = opponent
(E1 unless noted). No agent errors were observed for any of the five blocks.

| block | file | mechanism | vs E1 (dev, n=6) | vs tape_yuan800 | vs tape_shirabe | verdict |
|---|---|---|---|---|---|---|
| A | `evolve/blocks/lib_a_full_sweep.py` | sweep: once the urgent tier is drained, chain all remaining pending tasks by nearest-neighbour with no `CROP_SWEEP_LEN` cap | **-$19,099/game, t=-10.78** | not run (killed at dev) | not run | **REJECTED — decisive loss.** Uncapped chaining drags hands into long low-value tours instead of returning to the highest-value tier promptly; this looks like the same failure mode RULES already documents for NEAR_RADIUS growth — bigger sweeps ≠ better throughput here. |
| B | `evolve/blocks/lib_b_harvest_first_melon.py` | sweep: days 10-12, harvest tier precedes water tier for MELON tiles with `yield_units >= 5` (the carry-and-DROP half of the idea is already covered by the existing `KNOBS["melon_rush"]` dispatch logic, unchanged) | +$98/game, t=1.16 | -$34,213 (E1 baseline: -$33,772) | -$27,513 (E1 baseline: -$27,084) | **NO-OP / marginal.** Slightly positive vs E1, essentially flat-to-slightly-worse vs both tapes (within noise of E1's own gap). Not decisive either way — safe to queue as a sweep option. |
| C | `evolve/blocks/lib_c_herd_scaled_route.py` | animal_routing: `route_len = min(5, max(2, herd // 3))` instead of the fixed `ROUTE_LEN`; unfed animals ordered before fed ones in the stop chain. Feed/care pairing and on-tile-only fertilizer collection were verified already true in the chassis (no change needed). | -$3,398/game, t=-0.95 | not run (non-positive) | not run | **REJECTED (soft).** Not decisive but consistently negative (2 of 6 seeds down >$14k/$38k); herd-scaled route length does not pay for the reordering overhead. Excluded from the queue. |
| D | `evolve/blocks/lib_d_opportunistic_deposit.py` | dispatch: a hand off-route, not carrying feed wheat or an animal, carrying 1-3 units of product, one Manhattan step from a shed tile, steps on and DROPs immediately rather than waiting for `drop_min`/`drop_radius` | +$449/game, t=0.50 | -$29,976 (E1 baseline: -$33,772) | -$26,958 (E1 baseline: -$27,084) | **NO-OP / mildly positive.** Flat vs E1, and closes ~$3.8k of the gap to tape_yuan800 (still a large decisive loss overall, not remotely competitive). Cheap and harmless — queued as a dispatch option. |
| E | `evolve/blocks/lib_e_wheat_trade_large_herd.py` | crop_admission: extends the banded block — once herd size >= 12, `_plant_choice` prefers WHEAT over MELON for the far band, and `_crop_pools` reserves the 4 nearest far tiles for WHEAT | -$8/game, t=-0.05 | not run (non-positive, though effectively zero) | not run | **EXACT NO-OP.** Herd rarely if ever reaches 12 by the time far-tile planting still has open seed slots under E1's params, so the reservation logic almost never fires. Queued anyway (as an alternative crop_admission option) since it costs nothing and might matter at other points in the parameter space (bigger herd knobs) that the factorial will explore. |
| B+D combo | `candidates/gen_lib/lib_BD.py` | both B and D together | +$484/game, t=0.54 | -$31,184 (E1: -$33,772) | -$26,471 (E1: -$27,084) | Small positive on dev, not significant; combination doesn't compound meaningfully (each block barely moves the needle alone) but doesn't conflict either. |

## Honest summary

None of the five mechanisms found a decisive win. Two (A, C) are net negative and excluded from
the queue; A is a decisive rejection consistent with RULES's "bigger sweep radius/coverage loses"
pattern. Three (B, D, E) are statistically indistinguishable from no-ops vs E1 and don't close
the frontier-tape gap in any single-seed way that stands out — they were queued as low-risk,
non-harmful options for the evolutionary search to combine with parameter mutations, per the
observation in RULES.md that execution-only changes without a paired allocation change tend to be
flat (routing-oracle finding, Sep 3).

## Queued

- `evolve/queue/lib_blocks.json` — factorial: `crop_admission` in {banded, lib_E}, `sweep` in
  {null, lib_B}, `dispatch` in {null, lib_D}. `animal_routing` (lib_C) and the uncapped-sweep
  variant (lib_A) are excluded (rejected above).
- `evolve/queue/lib_A.json`, `lib_B.json`, `lib_C.json`, `lib_D.json`, `lib_E.json` — one
  single-block "candidate" queue entry per block (E1 params + that block only) so each can be
  scored alone in the loop's own cascade for confirmation.
