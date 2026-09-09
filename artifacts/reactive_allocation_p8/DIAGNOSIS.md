# P8 Reactive Allocation — Day-by-Day Diagnosis

Status label convention (same as REPORT.md / RNG_PATH_DEPENDENCE_AUDIT):
**DIRECTLY_OBSERVED** = read straight off code or an engine run with no inference.
**SUPPORTED** = inferred from multiple directly-observed data points.
**PLAUSIBLE** = a reasonable read that wasn't independently confirmed.
**UNRESOLVED** = open question, flagged rather than guessed at.

## 0. Method — DIRECTLY_OBSERVED

`experiments/P8_DIAGNOSIS/instrument_allocation.py` runs P8, P6, and C1 each vs
the same fixed opponent (`Opponents/opp_scenario_v14.py`) on the same 10 seeds
(1-10), both seats (20 paired games per policy), through the real engine via
`mini_engine.run_game()` (the exact same call `eval_protocol.py` uses — no new
engine-calling code). `mini_engine.py` already snapshots, per game day: money,
end-of-day hand count (`hands_eod`, captured at hour `turnsPerDay-1` — the
useful signal, see §1 caveat), land quadrants owned, herd size/mix, and
planted-tile count. Raw per-game traces: `experiments/P8_DIAGNOSIS/raw/*.json`.
Cross-seed aggregate: `experiments/P8_DIAGNOSIS/summary.json`. 0 agent errors
across all 60 games (20 P8 + 20 P6 + 20 C1).

**One methodology correction made mid-run, DIRECTLY_OBSERVED**: mini_engine's
`trace["hands"]` field (hour-0 snapshot) reads 0 for nearly the entire game for
all three policies, because the engine re-hires the whole crew from scratch
every day and the hour-0 snapshot is taken *before* that day's HIRE orders
land (confirmed: `trace["hands"]` for every policy/seed is `[0]*29 + [final]`).
`trace["hands_eod"]` (end-of-day count, after hiring) is the field that
actually carries the day-by-day hiring signal and is what all "N hands by day
D" figures below use.

## 1. Headline finding — DIRECTLY_OBSERVED, decisive (10/10 seeds)

**P8's labor-target formula is ~4x more hand-hungry than P6/C1's, and this
single gap cascades into every other allocation failure the prior REPORT.md
observed.**

- P8 (`candidates/P8_reactive_allocation.py`, `_hands_target`):
  `target = ceil(pending_load / LOAD_PER_HAND)`, `LOAD_PER_HAND = 5.0`.
- P6/C1 (`candidates/P6_baseline.py` / `C1.py`, `_load_model`):
  `tgt = ceil(load / KNOBS["load_per_hand"])`, `KNOBS["load_per_hand"] = 20`.

Both compute `load` the same way (same `LOAD_ANIMAL`/`LOAD_CROP_TASK` unit
weights — P8 copies P6's formula verbatim in `_pending_load`, see
P8_reactive_allocation.py:121-127). The only difference is the per-hand
capacity divisor: **5 vs 20, a 4x gap**, and P8's clamp ceiling (`MAX_HANDS`,
13) is the same ceiling P6/C1 use — so P8's target saturates at the hard cap
almost immediately instead of leveling off at a load-appropriate value below it.

Directly observed in all 10 traced seeds (`P8_seed{1..10}_swap0.json`):

| seed | day P8 hits 13 hands (=MAX_HANDS) | day P8's planted-tile count collapses to 0 | final land quads | final animals |
|---|---|---|---|---|
| 1 | 7 | 14 | 2 | 14 |
| 2 | 7 | 30 (never fully collapses) | 3 | 14 |
| 3 | 7 | 27 | 2 | 14 |
| 4 | 6 | 11 | 2 | 14 |
| 5 | 7 | 12 | 2 | 14 |
| 6 | 7 | 16 | 2 | 14 |
| 7 | 7 | 24 | 2 | 14 |
| 8 | 7 | 30 (never fully collapses) | 3 | 14 |
| 9 | 7 | 27 | 2 | 14 |
| 10 | 7 | 24 | 2 | 14 |

P8 reaches `MAX_HANDS=13` by **day 6-7 in all 10 seeds**, and **final herd
size is exactly 14 in all 10 seeds** — not a coincidence: P8's herd cap is
`HERD_RATIO_CAP (1.1) x n_hands`, and once hands pin at 13,
`1.1 x 13 = 14.3 -> 14` is the hard ceiling every single game converges to.
Land stays at 2 quadrants in 8/10 seeds, 3 in 2/10, never reaching 4.

Cross-seed aggregate (`summary.json`, n=20 paired games per policy,
both seats, seeds 1-10):

| metric | P8 | P6 | C1 |
|---|---|---|---|
| mean final $ delta vs opp_scenario_v14 | **-$55,641** | +$17,668 | +$11,447 |
| day reach 8 hands | **day 2** (20/20) | day 9.95 (20/20) | day 8.3 (20/20) |
| day reach 10 hands | **day 4** (20/20) | day 12.2 (20/20) | day 10.45 (20/20) |
| day reach 3 land quads | day 12 (**4/20 seeds**) | day 12 (19/20) | day 11.4 (18/20) |
| day reach 4 land quads | never (**0/20**) | day 14 (3/20) | day 14.5 (4/20) |
| day reach 15 animals | never (**0/20**) | day 12.3 (7/20) | day 13.4 (7/20) |

So the original hypothesis in the task brief ("P8's reactive thresholds
under-invest in land/labor balance") is **half right and points the wrong
direction on labor**: P8 does not under-hire — it **massively over-hires**,
years ahead of P6/C1's schedule (10 hands by day 4 vs day ~10-12), and that
over-hiring is exactly what causes the land/herd under-investment the report
observed, via a specific mechanical chain (§2).

## 2. The mechanism — SUPPORTED (traced directly, one seed shown, pattern
confirmed across all 10)

Seed 1, P8, `hands_eod` / `plants` / `land` / `animals` / `money` by day
(`experiments/P8_DIAGNOSIS/raw/P8_seed1_swap0.json`):

```
day:     0    1    2    3    4     5    6     7     8     9    10    11    12     13     14     ...  29
hands:   7    5    9    8    11    9    12    13    13    13   13    13    13     13     13     ...  13
plants:  0    7    9    10   12    13   11    10    14    16   17    10    4      1      0      ...  0
land:    1    1    1    1    1     1    1     1     1     2    2     2     2      2      2      ...  2
animals: 0    2    4    4    4     4    5     5     7     10   11    12    14     14     14     ...  14
money:   3000 1306 93   70   259   273  31    30    52    40   66    250   10276  10935  12481  ...  37767
```

The chain, read directly off P8_reactive_allocation.py's own gating logic:

1. **Day 0-7**: `LOAD_PER_HAND=5.0` makes `_hands_target` climb to 13
   (`MAX_HANDS`) by day 6-7 — far earlier than the actual chore load justifies
   (chore count/plant count at day 6-7 is only 10-14 tiles, well within what
   4-5 hands at P6's `load_per_hand=20` would clear).
2. **`_hire_orders` spends cash on this every day** via `_fib(hires_today+n)`
   — hiring cost is Fibonacci-scaled per hire *that day*, so hiring toward 13
   repeatedly (the crew resets to 0 and must be re-hired every single day per
   engine rule) burns a large, escalating daily wage bill P6/C1 do not pay
   at the same pace. Money sits at $30-300 for days 2-11 (row above) — P8 is
   cash-starved for the entire early game, confirmed directly in the trace.
3. **Once `target_hands >= MAX_HANDS` (`labor_saturated = True`,
   P8_reactive_allocation.py:253), R4's crop-mix throttle
   (`if space > 0 and not labor_saturated and day >= 1`) permanently blocks
   all further `BUY_SEED` orders** — this gate is a one-way trip: nothing in
   the file ever re-enables planting once `target_hands` has hit the cap even
   once, because the reactive target only ever ratchets up with load, and
   with the labor pool now oversized relative to the (smaller, correctly-
   sized) real chore load, `target_hands` never drops back below `MAX_HANDS`.
   The `plants` column shows exactly this: peaks at 17 (day 10), then
   monotonically collapses to 0 by day 14 as existing crops are harvested and
   never replaced.
4. **With crop planting dead, tile occupancy stalls out**, so R2's land
   trigger (`occupancy >= OCC_HIGH=0.65`) stops advancing — `land` freezes at
   2 quadrants from day 9 onward in 8/10 seeds. (P6/C1 use a day-deadline
   table instead, so they are not exposed to this feedback loop at all.)
5. **Herd is separately capped at `HERD_RATIO_CAP x n_hands = 1.1 x 13 = 14.3`**
   — with hands pinned at the max, herd purchases stop cold at 14 in
   literally every one of the 10 traced seeds, regardless of market room or
   cash.
6. Net effect: P8 spends the whole game with 13x the wage bill of a
   4-5-hand crew, working an economy that is capped at 2 land quads / 14
   animals / (eventually) 0 active crop tiles — while P6/C1 keep expanding
   land to 3-4 quads and herd past 15 through day 20+. P8's late-game money
   growth is roughly linear (~$1.5k/day from day 12-30 in seed 1) where
   P6/C1's is steeper because they keep adding productive capacity instead of
   just harvesting a frozen 14-animal/2-quad base.

## 3. Concrete, retunable gap

**`LOAD_PER_HAND = 5.0` in `candidates/P8_reactive_allocation.py` line 110 is
the single load-bearing number.** P6/C1's equivalent knob
(`KNOBS["load_per_hand"]`) is 20 — a 4x difference — and P8's target hits
`MAX_HANDS` by day 6-7 in 10/10 seeds where P6/C1 don't reach even 10 hands
until day ~10-12. Retuning `LOAD_PER_HAND` toward P6/C1's 20 (or something in
that neighborhood) should, by the mechanism traced in §2, delay
`labor_saturated` from ever triggering in the early game, which should in turn
un-block R4's crop-mix throttle and R2's occupancy-driven land trigger and
R3's herd-ratio cap (since `n_hands` in the denominator would stay smaller and
the labor-saturation gate would stop firing at day 6).

A secondary, smaller finding: P8's R4 throttle (`labor_saturated =
target_hands >= MAX_HANDS`) is a **one-way gate with no un-stick condition** —
even if `LOAD_PER_HAND` is retuned so this triggers less *often*, any future
policy that reuses this pattern should consider re-checking `labor_saturated`
against the day's *actual* pending load rather than a target that, once
pinned at the ceiling, has no mechanism to fall back below it (P8's own
report, REPORT.md §3, already flags a version of this "never grows" /
"runaway hiring" tension as something tuned around once — this diagnosis
shows the tuning went too far in the runaway direction, not the "never
grows" direction the report worried about).

## 4. Retune — TESTED (paired eval run this session)

Retuned `LOAD_PER_HAND` from 5.0 to 20.0 (matching P6/C1's `load_per_hand`
knob exactly) in a new file, `candidates/P8v2_reactive_allocation.py`
(single-line diff, nothing else changed — `P8_reactive_allocation.py` itself
was not modified). Sanity check on seed 1 confirms the mechanism in §2
reverses: `hands_eod` no longer saturates at `MAX_HANDS=13` until day 17
(vs day 6-7 for P8), `land` reaches 4 quadrants by day 15 (P8: capped at 2),
`animals` reaches 14 by day 19 (P8: same ceiling but 7 days later, with the
extra days spent on land/crops instead of idle hands) — full trace:
`experiments/P8_DIAGNOSIS/raw/` doesn't include P8v2 (kept out of the sanctioned
harness's fixed POLICIES dict for time reasons); the seed-1 numbers above were
pulled with a one-off `mini_engine.run_game()` call, not saved as a file.

**TESTED paired-eval results** (`experiments/RNG_PATH_DEPENDENCE_AUDIT/
eval_protocol.py compare_paired()`, seeds 1-10, both seats, n=20 games/pair,
common opponent `opp_scenario_v14.py` except the first row which compares the
two P8 variants directly):

| comparison | mean delta | stdev | t | wins/losses |
|---|---|---|---|---|
| P8v2 vs P8 (direct) | **+$42,263/game** | $30,620 | 6.17 | 17W/3L |
| P8v2 vs P6_baseline | -$12,634/game | $31,317 | -1.80 | 8W/12L |
| P8v2 vs C1 | -$16,365/game | $32,569 | -2.25 | 8W/12L |

So the single-line `LOAD_PER_HAND: 5.0 -> 20.0` retune **recovers roughly
75-80% of the original gap** (P8's -$48-50k/game vs P6/C1 in REPORT.md shrinks
to -$13-16k/game) with a decisive, large-sample win over the untuned P8
(t=6.17, 17/20 seed-pairs). It does not fully close the gap to P6/C1 — the
remaining -$13-16k is smaller than P8's original deficit but still a real,
directionally consistent loss (t=-1.8 and -2.25, borderline-to-decisive at
n=20), meaning `LOAD_PER_HAND=20` was the dominant lever but not the only one;
some residual gap (plausibly R2's land-occupancy trigger threshold, R3's
`HERD_RATIO_CAP`, or R5's sell floors — none of which were touched by this
retune) likely still needs its own pass. All trajectories flagged
`trajectory_diverged=True` (the known RNG-path-dependence confound from
`experiments/RNG_PATH_DEPENDENCE_AUDIT/`, expected any time board occupancy
differs between arms) — noted per that report's convention, not treated as
invalidating a t=6.17/n=20 result.

## Files

- `experiments/P8_DIAGNOSIS/instrument_allocation.py` — the instrumentation
  harness (reuses `mini_engine.run_game()`, no new engine-calling code).
- `experiments/P8_DIAGNOSIS/raw/*.json` — 60 full per-game traces (P8/P6/C1 x
  seeds 1-10 x both seats).
- `experiments/P8_DIAGNOSIS/summary.json` — cross-seed aggregate used for the
  tables above.
- This report: `artifacts/reactive_allocation_p8/DIAGNOSIS.md`.
- Prior report (final-$ only, no day-by-day trace):
  `artifacts/reactive_allocation_p8/REPORT.md`.
