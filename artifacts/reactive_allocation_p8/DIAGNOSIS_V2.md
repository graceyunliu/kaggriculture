# P8v2 → P8v3 — Land/Herd Retune Diagnosis

Status label convention (same as DIAGNOSIS.md / REPORT.md / RNG_PATH_DEPENDENCE_AUDIT):
**DIRECTLY_OBSERVED** = read straight off code or an engine run with no inference.
**SUPPORTED** = inferred from multiple directly-observed data points.
**PLAUSIBLE** = a reasonable read that wasn't independently confirmed.
**UNRESOLVED** = open question, flagged rather than guessed at.

## 0. Scope and method — DIRECTLY_OBSERVED

Task brief: close the remaining `P8v2_reactive_allocation.py` vs `P6_baseline.py`/`C1.py`
gap (-$12,634/-$16,365 per game, DIAGNOSIS.md §4) by retuning ONLY land-expansion and
herd-purchase logic. `LOAD_PER_HAND` (already fixed 5→20) was not touched.

`experiments/P8_DIAGNOSIS/instrument_v2.py` (new file, adapted from
`instrument_allocation.py` — reuses its `summarize_policy_seed`/event-extraction
helpers verbatim via `import instrument_allocation as ia`, only the policy set and
opponent-relative logging changed) ran P8v2, P6, C1 vs `Opponents/opp_scenario_v14.py`,
seeds 1-10, both seats (n=20 games/policy). Raw traces:
`experiments/P8_DIAGNOSIS/raw_v2/*.json`. Aggregate: `experiments/P8_DIAGNOSIS/summary_v2.json`.
0 agent errors across all 60 games. All retune candidates were then validated with
`eval_protocol.py compare_paired()` (seeds 1-10, both seats, n=20 paired games), the same
harness/seed range DIAGNOSIS.md's §4 retune used.

## 1. Headline finding — DIRECTLY_OBSERVED: the land/herd hypothesis is NOT supported

The task brief hypothesized land-expansion and herd-purchase-ratio thresholds as the
residual leak. Instrumentation contradicts this for land, and herd retuning in
**both directions was tested and made results worse**, not better.

**Land — P8v2 already outpaces P6/C1, not the other way around** (`summary_v2.json`,
n=20 games/policy):

| metric | P8v2 | P6 | C1 |
|---|---|---|---|
| day reach 2 land quads (mean, n reached) | **day 6.6** (20/20) | day 8.0 (20/20) | day 8.0 (20/20) |
| day reach 3 land quads | day 12.25 (20/20) | day 12.0 (19/20) | day 11.4 (18/20) |
| day reach 4 land quads | day 15.68 (**19/20**) | day 14.0 (3/20) | day 14.5 (4/20) |
| mean final land quads | **3.95** | 3.1 | 3.1 |

P8v2 reaches 2 quads *faster* than P6/C1 and reaches 4 quads in 19/20 seeds where P6/C1
reach it in only 3-4/20. Land-expansion pace/threshold (`OCC_HIGH=0.65` vs P6/C1's
`LAND_DEADLINE` day-table) is not under-investing — it is, if anything, ahead.

**Herd — the one real gap found, but it doesn't fix the $ delta when retuned**
(`summary_v2.json`):

| metric | P8v2 | P6 | C1 |
|---|---|---|---|
| day reach 15 animals (n reached/20) | **never (0/20)** | day 12.29 (7/20) | day 13.43 (7/20) |
| mean final animals | 13.45 | 12.3 | 12.7 |

Reading P8v2's code (`HERD_RATIO_CAP = 1.1`, animals-per-hand cap, `MAX_HANDS=13` →
ceiling ≈14.3) against P6/C1's (`KNOBS["max_animals"]=20` in P6, uncapped in C1, gated
only by a load-model check vs `MAX_HANDS` that rarely binds given `LOAD_ANIMAL=6` and
`LOAD_PER_HAND=20`, i.e. an effective ceiling around 20 animals / 13 hands ≈ 1.54
animals/hand) is a real, concrete numeric gap: **P8v2's herd cap (1.1) is ~40% tighter
than P6/C1's effective cap (~1.54), and P8v2 never reaches 15 animals in 20 seeds where
P6/C1 do in 7/20.**

## 2. Retunes tried — TESTED, all four made the paired $ delta worse

Four candidate retunes were built and validated via `compare_paired()` (seeds 1-10,
both seats, n=20). Baseline to beat: P8v2 vs P6 = **-$12,634/game** (t=-1.80), P8v2 vs
C1 = **-$16,365/game** (t=-2.25) (DIAGNOSIS.md §4).

| attempt | change | vs P8v2 (direct) | vs P6 | vs C1 |
|---|---|---|---|---|
| 1 | `HERD_RATIO_CAP` 1.1→1.6 (match P6/C1's effective ~1.54) | -$11,373/game, t=-2.18, 7W/13L | -$24,006/game, t=-3.29 | (not run; already worse) |
| 2 | `OCC_HIGH` 0.65→0.80 (delay land, save cash for crops/herd) | -$9,322/game, t=-2.54, 6W/14L | -$21,956/game, t=-2.81 | -$25,687/game, t=-3.69 |
| 3 | `HERD_RATIO_CAP` 1.1→1.25 (smaller step toward attempt 1) | -$8,968/game, t=-2.58, 6W/14L | (not separately run; strictly between 1 and 4) | (not separately run) |
| 4 | `HERD_RATIO_CAP` 1.1→0.85 (opposite direction: lower, not raise) | -$6,367/game, t=-1.81, 9W/11L (least-bad) | **-$19,000/game, t=-3.07**, 6W/14L | **-$22,732/game, t=-3.70**, 4W/16L |

Every attempt is a net loss relative to P8v2's own baseline against both P6 and C1 —
attempt 4 (lowering, not raising, `HERD_RATIO_CAP`) is the least-bad of the four
against P8v2 directly (t=-1.81, not quite decisive at n=20) but it is still decisively
**worse** than P8v2 when compared to the actual targets, P6 (-$19,000 vs P8v2's
-$12,634) and C1 (-$22,732 vs P8v2's -$16,365).

**Mechanism, SUPPORTED**: reading `economy()`'s order of operations in
`P8v2_reactive_allocation.py`, R3 (herd) runs and spends from the shared `free` cash
pool *before* R4 (crop mix) gets a turn at it. Raising `HERD_RATIO_CAP` lets herd
purchases claim more of that pool earlier in the day, which reduces the cash left for
crop seeds — and per DIAGNOSIS.md's own §2 mechanism (over-investing in one allocation
category starves a more productive one), crops appear to be the more cash-efficient
spend here: seed 1's raw trace (`raw_v2/P8v2_seed1_swap0.json`) shows P8v2 already
reaches a 79-plant peak (day 20) vs P6's 67-plant peak, so the crop side is not
starved in the current (1.1) configuration — pushing more cash toward herd, in either
direction tested, only moves cash away from a channel that was already working.

## 3. Verdict — gap NOT closed, hypothesis largely disconfirmed

**Land**: hypothesis disconfirmed. P8v2 already expands land faster/further than
P6/C1 (§1) — this was never the leak.

**Herd**: a real, concrete threshold gap exists (`HERD_RATIO_CAP=1.1` vs P6/C1's
effective ~1.54, §1) and P8v2 does undershoot P6/C1's peak animal count. But **closing
that specific gap by retuning the constant, in either direction, makes the overall $
outcome worse, not better** (§2) — the animal-count metric and the $-outcome metric
point in different directions here, so "P8v2 has fewer animals than P6/C1" is real but
is not, on this evidence, the thing actually costing P8v2 the game.

**P8v3, as shipped** (`candidates/P8v3_reactive_allocation.py`): ships attempt 4
(`HERD_RATIO_CAP` 1.1→0.85, the least-bad of four tested variants) rather than a
fabricated win, per the task's honesty instruction — this is a **regression relative
to P8v2**, not an improvement: -$19,000/game vs P6 (P8v2: -$12,634) and -$22,732/game
vs C1 (P8v2: -$16,365), both decisive (t=-3.07, t=-3.70, n=20). **The gap is NOT
closed and NOT partially closed by any land/herd retune tested in this session — it
is unchanged at best, worse if this specific file is used.**

**Recommendation**: do not promote P8v3 over P8v2. The residual -$12.6k/-$16.4k gap
between P8v2 and P6/C1 does not appear to live in land-expansion or herd-purchase-
ratio thresholds (both were tested directly and independently); per §2's mechanism
read, the more promising next lever is **R5 sell timing** (P8v2's reactive
`MELON_FLOOR_FRAC`/`SHED_OVERFLOW` vs P6/C1's fixed `melon_floor`/`wheat_sell_price`
dollar floors) or **wage/cash-buffer sizing** (`CASH_BUFFER=120`, untouched this
session) — both outside this task's land/herd-only scope and flagged here as
**UNRESOLVED**, not tested.

## Files

- `candidates/P8v3_reactive_allocation.py` — P8v2 + `HERD_RATIO_CAP: 1.1 → 0.85`
  (least-bad of 4 tested land/herd retunes; ships as a documented regression, not a
  win — see §3).
- `experiments/P8_DIAGNOSIS/instrument_v2.py` — instrumentation harness (P8v2/P6/C1),
  reuses `instrument_allocation.py`'s helpers.
- `experiments/P8_DIAGNOSIS/raw_v2/*.json`, `experiments/P8_DIAGNOSIS/summary_v2.json`
  — the 60-game land/herd trace data behind §1.
- `experiments/P8_DIAGNOSIS/p8v3*_vs_*.json` — full `compare_paired()` reports for
  each of the 4 retune attempts vs P8v2/P6/C1.
- This report: `artifacts/reactive_allocation_p8/DIAGNOSIS_V2.md`.
- Prior reports: `artifacts/reactive_allocation_p8/DIAGNOSIS.md`, `REPORT.md`.
