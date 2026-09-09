# P8v2 → P8v4 — Sell-Timing / Cash-Buffer Diagnosis

Status label convention (same as DIAGNOSIS.md / DIAGNOSIS_V2.md / REPORT.md /
RNG_PATH_DEPENDENCE_AUDIT):
**DIRECTLY_OBSERVED** = read straight off code or an engine run with no inference.
**SUPPORTED** = inferred from multiple directly-observed data points.
**PLAUSIBLE** = a reasonable read that wasn't independently confirmed.
**UNRESOLVED** = open question, flagged rather than guessed at.

## 0. Scope and method — DIRECTLY_OBSERVED

Task brief: close the remaining `P8v2_reactive_allocation.py` vs `P6_baseline.py`/`C1.py`
gap (-$12,634/-$16,365 per game, DIAGNOSIS.md §4) by retuning ONLY sell-timing (R5) and
cash-buffer sizing (`CASH_BUFFER`). Land/herd thresholds were not touched (already ruled
out by DIAGNOSIS_V2.md).

`experiments/P8_DIAGNOSIS/instrument_v3_selltiming.py` (new file, reuses
`instrument_allocation.py`'s policy-loading pattern; imports it directly for its module
namespace) ran P8v2, P6, C1 vs `Opponents/opp_scenario_v14.py`, seeds 1-10, both seats
(n=20 games/policy), through `mini_engine.run_game(trace=True)`. `mini_engine.py`
already logs, per day: `trace["money"]` (cash, hour-0 snapshot), `trace["shed"]`
(inventory held, hour-0 snapshot — i.e. BEFORE that day's SELL orders execute), and
`trace["sales"]` (per-day `item -> (qty_sold, revenue)`, logged directly off the real
engine's own `_commit_unit` calls — exact realized sale price, not an estimate). Raw
traces: `experiments/P8_DIAGNOSIS/raw_v3/*.json`. Aggregate:
`experiments/P8_DIAGNOSIS/summary_v3.json`. 0 agent errors across all 60 games.

## 1. Headline finding — DIRECTLY_OBSERVED: both hypotheses are NOT supported

**Cash-buffer: P8v2 is not cash-constrained — it holds MORE idle cash than P6/C1, not
less.** From `summary_v3.json` (n=20 games/policy, mean cash on hand):

| metric | P8v2 | P6 | C1 |
|---|---|---|---|
| mean cash, days 1-10 | **$1,288** | $503 | $456 |
| mean cash, days 11-20 | $13,689 | $15,984 | $15,874 |
| mean days with cash < $100 | **0.6/game** | 2.1/game | 2.25/game |

P8v2 carries ~2.5x P6/C1's early-game cash and is cash-starved (< $100 on hand) in only
0.6 days/game on average, vs 2.1-2.25 for P6/C1 — the opposite of what a binding
`CASH_BUFFER` would produce. Seed 1's raw money trace
(`experiments/P8_DIAGNOSIS/raw_v3/P8v2_seed1_swap0.json`) confirms directly: cash never
dips near the `CASH_BUFFER=120` floor after day 1 (`[3000, 1327, 683, 765, 959, 1140,
1293, ...]`, climbing steadily). `CASH_BUFFER` is not the leak.

**Sell-timing: R5's price floors and reserve logic are working exactly as coded, and the
realized per-unit sale prices P8v2 achieves are as good as or BETTER than P6/C1's — the
problem is volume, which is upstream of R5.** From `summary_v3.json`:

| item | metric | P8v2 | P6 | C1 |
|---|---|---|---|---|
| WHEAT | mean total qty sold/game | **399.3** | 78.0 | 54.6 |
| WHEAT | mean $/unit realized | $45.36 | $40.46 | $40.00 |
| WHEAT | mean shed level (held) | 22.76 | 6.88 | 6.49 |
| MELON | mean total qty sold/game | 42.0 | 72.1 | 63.5 |
| MELON | mean $/unit realized | **$216.03** | $177.85 | $190.50 |
| STRAWBERRY | mean total qty sold/game | **62.3** | 232.0 | 228.2 |
| STRAWBERRY | mean $/unit realized | **$196.14** | $132.49 | $176.12 |
| MILK | mean total qty sold/game | **77.1** | 192.5 | 191.6 |
| MILK | mean $/unit realized | **$172.39** | $114.34 | $129.53 |

Tracing seed 1's WHEAT sell mechanics directly (`raw_v3/P8v2_seed1_swap0.json`,
`per_item.WHEAT.shed.by_day` and `sell_events`): on day 22, pre-sell shed WHEAT = 53,
`reserve_feed = n_total(14) + FEED_SPARE(3) = 17`, and the logged sell that day is
exactly `qty=36` (`53 - 17 = 36`, matching to the unit) — **the surplus-sell formula
sells everything above the feed reserve, every single day, exactly as designed.** The
huge WHEAT shed buildup (mean 22.76, vs P6/C1's ~6.5-6.9) and huge sell volume (399 vs
55-78/game) are not a sell-timing failure at all — they are P8v2 *producing* roughly
5-7x more WHEAT than P6/C1 (a crop-mix/R4 planting-volume fact, out of this task's R5/
cash-buffer scope) which R5 then correctly, promptly liquidates at a price (`$45.36/
unit`) that is *higher* than what P6 ($40.46) or C1 ($40.00) realize.

The same pattern holds for MELON and MILK/STRAWBERRY, but in the other direction: P8v2
realizes a *better* price per unit on MELON ($216 vs $178-191) and dramatically better
prices on STRAWBERRY ($196 vs $132-176) and MILK ($172 vs $114-130) — its price floors
are, if anything, holding out for *more* money per sale than P6/C1's fixed dollar floors
achieve. What it lacks is volume: 62 STRAWBERRY units/game vs 228-232, 77 MILK units/game
vs 192, 42 MELON units/game vs 63-72. Volume is set by how much is grown/raised (crop-mix
and herd size, both DIAGNOSIS_V2.md-scoped or land/herd-scoped, not R5), not by when it
is sold.

## 2. Retunes tried — TESTED, both roughly a no-op / marginal regression

Two candidate retunes were built into `candidates/P8v4_reactive_allocation.py` (branched
from P8v2, not P8v3) and validated via `eval_protocol.py compare_paired()` (seeds 1-20,
both seats, n=40 paired games — the full range the task asked for, runtime ~150s total
for all three comparisons, well inside budget):

1. **`CASH_BUFFER` 120.0 → 40.0** — motivated by §1's idle-cash finding, on the chance
   the buffer was still shaving a purchase at the margin even though it wasn't the
   dominant constraint.
2. **`MELON_FLOOR_FRAC` 0.72 → 0.55** — motivated by §1's MELON volume shortfall, on the
   chance the floor (even though realized price was already good) was still delaying
   enough sells to cost volume.

Baseline to beat: P8v2 vs P6 = **-$12,634/game** (t=-1.80, n=20, DIAGNOSIS.md §4), P8v2
vs C1 = **-$16,365/game** (t=-2.25, n=20).

**Results, n=40 (seeds 1-20, both seats):**

| comparison | mean delta | stdev | t | wins/losses/ties |
|---|---|---|---|---|
| P8v4 vs P8v2 (direct) | **-$1,007/game** | $8,301 | -0.77 | 9W/13L/18T |
| P8v4 vs P6 | **-$15,340/game** | $27,188 | -3.57 | 12W/28L/0T |
| P8v4 vs C1 | **-$17,386/game** | $30,795 | -3.57 | 15W/25L/0T |

P8v4 vs P8v2 direct is **not decisive** (t=-0.77, n=40, 18/40 ties — most seeds saw zero
change at all, consistent with §1's finding that neither knob was actually binding on
most games) but leans slightly negative rather than positive. Against the real targets,
P8v4 is **decisively worse than P8v2's own baseline**: -$15,340 vs P6 (P8v2: -$12,634)
and -$17,386 vs C1 (P8v2: -$16,365), both now comfortably past t=-3.5 where P8v2's own
numbers were only t≈-2. All comparisons flag `trajectory_diverged=True` on effectively
every game (the known RNG-path-dependence confound, per convention noted and not treated
as invalidating a t=-3.57/n=40 result).

**Why the retune doesn't help, SUPPORTED**: §1 already shows neither `CASH_BUFFER` nor
`MELON_FLOOR_FRAC` was the actual constraint in the games instrumented — cash was
already abundant and MELON's realized price was already good. Loosening a knob that
isn't binding cannot improve the outcome; the small negative drift (-$1,007/game, not
individually significant but consistently negative-leaning) is most plausibly explained
by `CASH_BUFFER=40` occasionally letting a herd/land/hire purchase fire on a turn where
the $80 of freed-up margin would otherwise have been better spent the following turn
with slightly more information (a minor second-order effect, not the intended fix) —
flagged **PLAUSIBLE**, not independently traced turn-by-turn.

## 3. Verdict — gap NOT closed, both hypotheses disconfirmed

**Sell-timing (R5)**: hypothesis disconfirmed. R5's surplus-sell arithmetic matches its
own formula exactly (§1's day-22 WHEAT trace), and realized per-unit prices on every
item checked are equal to or better than P6/C1's. This was never the leak.

**Cash-buffer (`CASH_BUFFER`)**: hypothesis disconfirmed. P8v2 holds 2.5x P6/C1's
early-game cash and is starved (<$100) 3-4x less often than P6/C1. The buffer is not
binding.

**P8v4, as shipped** (`candidates/P8v4_reactive_allocation.py`): ships both tested
retunes rather than a fabricated win, per the task's honesty instruction — this is a
**regression relative to P8v2**, not an improvement: -$15,340/game vs P6 (P8v2:
-$12,634) and -$17,386/game vs C1 (P8v2: -$16,365), both decisive at n=40 (t=-3.57 for
both). **The gap is NOT closed and NOT partially closed by any sell-timing/cash-buffer
retune tested in this session — it is unchanged at best (the direct P8v4-vs-P8v2
comparison is not itself decisive, t=-0.77), worse if this specific file is used against
the real targets.**

**What the data actually points to instead, SUPPORTED**: the residual -$12.6k/-$16.4k
gap is a **crop-mix / production-volume gap**, not an allocation-threshold gap in any of
the three places tested across DIAGNOSIS.md, DIAGNOSIS_V2.md, and this report (labor
target, land timing, herd ratio, sell floors, cash buffer). P8v2 grows and sells 5-7x
more WHEAT (a low-value, 5-day-cycle crop, `base=$25`) than P6/C1, while growing/selling
roughly a quarter of P6/C1's STRAWBERRY volume (a high-value, 18-day-cycle crop,
`base=$120`) and about 40% of their MILK volume — despite total plant *count* already
being competitive (DIAGNOSIS_V2.md §2: P8v2 peaks at 79 plants vs P6's 67). This is R4
(crop-mix selection) and/or the herd-size gap DIAGNOSIS_V2.md already found and
explicitly could not fix by retuning `HERD_RATIO_CAP` alone — i.e., the next honest
candidate lever is **why R4's greedy value/cycle ranking (kept identical to P6's,
per P8/P8v2's own design note) selects WHEAT so much more often for P8v2 than for P6/C1
given the same ranking formula** — plausibly an interaction with R1's `labor_saturated`
gate or the day-by-day `space`/`free`-cash sequencing that differs from P6's, not a
constant that can be hand-tuned in isolation the way `LOAD_PER_HAND` was. This is
**UNRESOLVED** and flagged, per the task's honesty instruction, as a genuine open
question rather than a fourth retune-and-hope attempt — R4/crop-mix interaction analysis
is explicitly out of this task's stated scope (sell-timing/cash-buffer only) and was not
tested here.

**Recommendation**: do not promote P8v4 over P8v2; keep `candidates/P8v2_reactive_
allocation.py` as the live baseline. If this line of work continues, the next
diagnostic pass should trace R4's per-day crop-selection choices (which candidate crop
wins the greedy ranking, and why WHEAT wins so much more often for P8v2 than the
identical ranking formula produces for P6/C1) rather than retuning any more R5/cash
constants — three independent passes (land/herd in DIAGNOSIS_V2.md, sell-timing/cash-
buffer here) have now ruled out every allocation *threshold* in the file; what remains
is the crop-mix *selection logic itself* and its interaction with R1's labor gate.

## Files

- `candidates/P8v4_reactive_allocation.py` — P8v2 + `CASH_BUFFER: 120 -> 40` +
  `MELON_FLOOR_FRAC: 0.72 -> 0.55` (both tested, both a no-op-to-marginal-regression —
  see §2-3; ships as a documented non-improvement, not a win).
- `experiments/P8_DIAGNOSIS/instrument_v3_selltiming.py` — instrumentation harness
  (P8v2/P6/C1), reuses `instrument_allocation.py`'s policy-loading pattern.
- `experiments/P8_DIAGNOSIS/raw_v3/*.json`, `experiments/P8_DIAGNOSIS/summary_v3.json`
  — the 60-game sell-timing/cash-trace data behind §1.
- `experiments/P8_DIAGNOSIS/p8v4_vs_P8v2.json`, `p8v4_vs_P6.json`, `p8v4_vs_C1.json`,
  `p8v4_paired_summary.json` — full `compare_paired()` reports (n=40, seeds 1-20, both
  seats) behind §2.
- This report: `artifacts/reactive_allocation_p8/DIAGNOSIS_V3.md`.
- Prior reports: `artifacts/reactive_allocation_p8/DIAGNOSIS_V2.md`,
  `artifacts/reactive_allocation_p8/DIAGNOSIS.md`,
  `artifacts/reactive_allocation_p8/REPORT.md`.
