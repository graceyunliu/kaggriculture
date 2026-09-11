# Discovery phase (Sep 11): candidate drought, self-model audit, worst/best decomposition

Per governance decision: **no new ladder candidate (O34+) until a measurement first identifies a mechanism with
demonstrated behavioral engagement and a plausible economic causal chain.** This replaces ad hoc knob search. Every
discovery cycle below must resolve to one of: (1) new measurable mechanism → isolate it, (2) known mechanism →
sharpen/close it, (3) environmental variation → no policy lever. Only (1) earns a new candidate number.

## 1. Self-model assumption audit (`candidates/K_SELFMODEL.py::economy()`)

Every high-economic-weight decision point in `economy()`, what state it reads, what it assumes, and whether that
assumption has an instrument behind it (see `docs/economic-self-model.md` Tier 1/2 for what's already been measured).

| Decision | State variable used | Assumption | Ever measured? |
|---|---|---|---|
| Feed buy (`feed_need`) | `due_feed`, shed WHEAT, `spare`/`feed_spare_poor` knob | Tomorrow's animal feed obligation ≈ today's `due_feed` + fixed 3-unit buffer | Partial — buffer is a bare constant, never swept against actual shortfall/overbuy rate |
| Hire sizing (`_hire_plan` / `_load_model`) | `n_total`, `seeds_on_hand`, `shed_animals+carried_animals`, `day` | `_load_model` produces the "right" hand count; `HIRE_MAX_MARGINAL=144` is the true marginal-hire ceiling | Yes for the price ceiling (H_GATE144, own +1.3–1.6k). `_load_model`'s target formula itself — no |
| `BUY_ANIMAL` (herd) | `_demand_room`, `opp_counts`, `MAX_SHEEP`, `cash_after ≥ need_tomorrow` liquidity check | Demand room is the binding constraint once reachability knobs are fixed (per doc: "market is the real wall") | Yes, closed Sep 11 (sheep herd-gate probe, 360-game panel) — but the **liquidity check's next-day cost/income estimate** (`labor_tomorrow`, `income_tomorrow`) that can still block a `k>0` buy is unaudited |
| `BUY_LAND` | `land_wanted` (driven only by STRAWBERRY overflow), `empty_count - pending_place < 8`, `LAND_DEADLINE` | The only reason to want land is strawberry-tile overflow; land price/deadline tradeoff for quad 3 (`day<=14 and land_wanted>=12`) is a bare threshold | Partially — quad-1/2 gate untested since O16; the `land_wanted>=12` cutoff for quad 3 has no cited panel |
| `BUY_SEED` (crop mix) | `_daily_demand`, `inv_c` (market inventory), `DEMAND_SHARE=0.5`, per-crop `min_val` cutoff | A single global `DEMAND_SHARE=0.5` correctly splits daily demand between us and the opponent for every crop, every day | No — `DEMAND_SHARE` is a flat constant; never measured against actual realized fill rate vs opponent by crop |
| `STRAW_UNITS=7.5`, `CARROT_UNITS=3.0` | seed allocator's committed-units accounting | Fixed yield-per-planting constants generalize across opponents/seeds | Yes (O24, O26 panels) — but **only for these two crops**; WHEAT/TOMATO/MELON in `CROP_SPECS["units"]` are still stale bare guesses (5.0/5.0/6.0), never audited the way straw/carrot were |
| Fertilizer buy (`fert_buy` knob, `fp <= 0.6*STRAWBERRY price`) | `len(v["fert"])` eligible ongoing-crop count, `FERT_PHASE_RULE`, `FERT_IS_INPUT` | Fertilizer pays for itself below a strawberry-price-relative ceiling | Doc says "more fertilizer raises output but not profit" (Tier 2 point 1) — the 0.6× price ceiling itself is untested against realized ROI |
| Melon sell timing (`MELON_MORNING`, `melon_floor` knob) | `prices["MELON"]`, `shed_load`, hour cutoff 8 | The day-10 morning window is the profitable one; profitable "to h8, negative after" | Yes (`tools/sale_timeline.py`, O20/O22) |
| Wheat sell/hold (`wheat_sell_price`, `wheat_stock`, `wheat_hold_days`) | `reserve_feed`, `shed_load>80` override | Holding wheat past the feed reserve for a later sell price beats selling now | Closed negative — "speculative inventory holding" is in `db.REJECTED_MECHANISMS` |
| Capital-event override (`event`, `capital_hour2`) | `cash >= previous+100`, `hour` window 2–12, capped 3/day | A cash jump mid-day is worth an out-of-cycle capital decision | Never audited on its own — folded in since early V3.x, no isolated panel found in `docs/` |

**Highest-value gaps** (economic weight × never-measured): the flat `DEMAND_SHARE=0.5` used for every crop's seed
sizing, and the un-audited `CROP_SPECS["units"]` guesses for WHEAT/TOMATO/MELON (only STRAWBERRY/CARROT got the
yield-correction treatment that drove O24/O26). Both are structurally the same shape of fact as `STRAW_UNITS`
before O24 — a stale constant feeding the seed allocator's sizing math. Next instrument to build: extend
`tools/allocation_matrix.py` (which already measured STRAW_UNITS) to WHEAT/TOMATO/MELON and to per-crop realized
demand share vs `DEMAND_SHARE=0.5`.

## 2. Worst/best decomposition (K_SELFMODEL vs `Opponents/tape_alaylm_106813359.py`, fixed shops)

8-seed scout (101–108) to find a worst/best pair for the same opponent:

| seed | cand money | opp money |
|---|---|---|
| 101 | 68,789 | 95,763 |
| 102 | 92,080 | 117,038 |
| 103 | 80,084 | 107,815 |
| **104** | 78,948 | 103,801 |
| **105 (best)** | **123,603** | 138,783 |
| 106 | 77,961 | 105,881 |
| **107 (worst)** | **49,751** | 71,229 |
| 108 | 76,891 | 90,604 |

Full per-day gap profile (`tools/gap_profile.py`) pulled for both seed 105 and seed 107 — same opponent, same code,
day-by-day money/animals/plants/hands/quads plus final sales-by-item.

**Earliest persistent divergence:** hand count. In the worst game (107), hired hands stall at 4 through days 8–9
while the opponent runs 7–8; in the best game (105) hands hit 10 by day 9. That early labor gap is followed by an
**animal-count divergence that never recovers**: in the worst game our herd sticks at 13 (opponent 17) for the rest
of the game (days 17–29); in the best game our herd reaches 17 — full parity — by day 16. Nothing else in the trace
diverges as early or as persistently: money, plant count and quad count all track close to the best-game shape until
day ~17, when the animal-count shortfall in the worst game starts compounding into the money gap (day 16: money gap
-5.9k; day 22: -12.3k; day 29 final: -21.5k below the best game's gap to the same opponent).

Sales breakdown confirms where the money actually leaks in the worst game relative to opponent: WOOL -$5,838,
WHEAT -$5,660, FERTILIZER -$4,800 — all three scale with animal/hand count (wool needs sheep, fertilizer eligibility
needs ongoing crops that need hands to tend, wheat needs hands to plant/harvest). MELON (+12,930) and CARROT
(+5,511) stay strongly positive in both games — those aren't the story.

**Classification:** this is not a new mechanism finding yet — it's an environmental-variation vs a real policy-lever
question, open. The candidate herd-buy liquidity check (`cash_after >= need_tomorrow`, per audit row above) is the
plausible causal link: a slower early hire ramp lowers `income_tomorrow` and raises the effective cost of the next
animal purchase, which can hold `k` at 0 for an extra day or two under the `while k>0: ... k -= 1` loop in the herd
block. This also overlaps the already-open `min_hands_knob_interactions` DELAY thread (project memory) — the
mechanism (`hands_early` replacing `min_hands`) is the same lever this trace points at. **Not resolved here** — the
next step is a targeted probe: hold the opponent and seed set fixed, force `hands_early` / lower `min_hands` only in
the seed-107-shaped low-early-hire regime, and check whether herd count recovers to opponent parity. That's a
measurement, not a candidate, until it clears a real panel.

## Open items for next cycle
1. Extend `tools/allocation_matrix.py` to WHEAT/TOMATO/MELON units-per-planting and to realized `DEMAND_SHARE` by
   crop — the two largest never-audited assumptions in the table above.
2. Run the `hands_early`/`min_hands` low-early-hire-regime probe against the animal-parity gap found here (ties to
   the existing min_hands_knob_interactions DELAY thread — read that before starting so this isn't a duplicate).
3. Do not open a new O-number from either of the above until a panel (multi-seed, both seats) shows a real own+margin
   gain, per the candidate-drought rule at the top of this file.

## Correction / cross-reference (found after the trace above)

Project memory already contains a more rigorous version of this exact decomposition, one step ahead of this
session: `kaggriculture-worst-loss-best-win-decomposition-sep12.md` (worst-10 vs best-10 seeds vs
`tape_bahaenes_106828159`, 30-seed slice) found the same SHEEP/animal-herd-size divergence (10 vs 16 animals,
splitting day 9-13, well before money) — and its follow-up, `kaggriculture-sheep-gate-causal-probe-outcome3-sep12.md`,
pre-registered a structural ablation of the SHEEP readiness override (`O37_SHEEP_GATE_OFF`) and found it made
**margin worse**, not better (-34,758 → -39,471): forcing more sheep purchases pushed wool supply into a market
that can't absorb it (price fell, feed cost rose). Conclusion there: the herd-size gap is substantially the policy
correctly reading real seed-level demand conditions, not a suppressible internal miscalibration — do not build a
sheep-count-relaxation candidate off this shape of finding again.

**So the hands_early/min_hands lever proposed above is NOT a fresh, unclosed thread — it's the same "buy the herd
sooner" family already shown to run into demand saturation once tested causally.** Before spending a cycle on it,
the open, not-yet-asked question is narrower than either prior write: is the early hand-count shortfall itself
binding the PURCHASE, or does `_demand_room()` already cap sheep purchases at that point regardless of hand count
(in which case relaxing labor changes nothing, consistent with Outcome 3)? That's a one-shot check — read `_demand_room()`'s
return value at day 9-11 in a worst-seed run alongside the `k` computed in the herd loop — before any panel, and
likely resolves to "no lever" rather than a new candidate.

## 3. Dormant-knob engagement audit (Sep 12, per Grace's 5-step protocol)

Scope: knobs in `O36_MIN_HANDS2.py`'s `KNOBS` dict sitting at an off/no-op default, NOT already covered by the
Sep-11 20-knob dev-h2h sweep (`kaggriculture-knob-sweep-min-hands-do-sep11.md` already tested and closed
open_melons/open_wheat/open_cows/open_sheep/min_hands/load_per_hand/early_hire_days/melon_floor/harvest_min/
demand_share/max_animals/hands_early/drop_min/feed_spare_poor, and flagged `labor_reserve_buffer` and
`setup_capital_share` as orphaned-never-referenced). Remaining dormant set: `wheat_tiles`, `wheat_per_animal`,
`wheat_stock`, `wheat_hold_days`, `wheat_water_tier`, `wheat_cap`, `drop_radius`, `capital_hour2`, `melon_rush`,
`straw_delay`, `sell_hourly`, `fert_carry`, `geese` (geese already closed ABANDON, not re-audited here).

**Method** (`tools/dormant_knob_probe.py`): for each knob, one nudged-value variant of O36 vs O36 baseline, same
seed/opponent (`tape_alaylm_106813359`)/seat, 3 seeds (21-23), counting turns where the produced action list
differs from baseline (engagement) and the resulting money delta (direction only — 3 seeds is not a panel).

| knob | branch condition (code) | reached at current default? | engaged when nudged? | classification |
|---|---|---|---|---|
| `sell_hourly` | **none — never referenced anywhere in the file outside the KNOBS dict** | n/a | 0/719 turns, $0 every seed | **unreached/dead — orphaned, not even wired.** Do not panel-test without first writing the intended behavior. |
| `drop_radius` | nested inside `if KNOBS["drop_min"]>0 and ...:` (line ~1167) — `drop_min` is 0 by default | no (gated by a sibling knob that's also off) | 0/719 turns, $0 every seed, confirms the gating | **reached but behaviorally redundant while `drop_min=0`** — not a candidate on its own; would need `drop_min` raised too (already closed flat in the Sep-11 sweep at drop_min_10: -316 h2h) |
| `wheat_cap` | `wheat_target = min(wheat_target, KNOBS["wheat_cap"])`, downstream of `wheat_tiles`/`wheat_per_animal` (both 0) | no — it's a ceiling on a floor that's already 0 | 0/719 turns, $0 every seed | **reached but behaviorally redundant** unless `wheat_tiles`/`wheat_per_animal` are raised first — same family as those two, not separate |
| `wheat_tiles` / `wheat_per_animal` | `wheat_target = max(KNOBS["wheat_tiles"], round(wheat_per_animal*n_total))`; `if wheat_target>0 and day<=24: ...` | no (both 0 → target 0) | yes — 142-168/719 turns differ, money swings both directions and are large on individual seeds (-4,394 to +5,750) | **engaged, behavior-changing → eligible for economic testing** (test as one lever — they feed the same `wheat_target`, don't treat as two independent knobs) |
| `wheat_stock` | `hold = KNOBS["wheat_stock"] if day<27 else 0` inside the WHEAT sell-surplus calc | yes, reached every day the WHEAT-sell branch runs, but `hold=0` contributes nothing | yes — 133-148/719 turns differ, **consistently positive across all 3 seeds** (+431/+726/+1,726) | **engaged, behavior-changing, consistent sign → eligible for economic testing** (best signal of this batch — same shape as `wheat_hold_days`, don't test both without checking overlap) |
| `wheat_hold_days` | `reserve_feed = (n_total+3) + (n_total*wheat_hold_days if day<27 else 0)` | yes, same branch as `wheat_stock` | yes — 129-132/719 turns differ, mixed sign (-411/-1,642/+3,443) | **engaged but noisier/mixed sign** — check against `wheat_stock` for redundancy before spending a panel on both |
| `wheat_water_tier` | `if KNOBS["wheat_water_tier"]: v["wwater"] = ...` (splits WHEAT out of the general water queue) | no (0 → split never happens) | yes — 65-114/719 turns differ, mixed sign | **engaged, mixed → eligible for economic testing**, lower priority (smallest engagement count of the "eligible" group) |
| `capital_hour2` | `KNOBS["capital_hour2"]>=0 and hour==...` in the capital-event gate | no (-1 → condition always false) | yes — strongly, 184-192/719 turns differ, large swings | **ALREADY CLOSED**: this is exactly `capital_timing_input_price_attack` in `evolve/directions.yaml`, state=ABANDON — "margin +0.7-1.6k, own -1.0..-2.6k, the tape pays the wheat/fert prices we push up (exploit class)." Do not re-test; the engagement probe just reconfirms the mechanism fires, which was never in question. |
| `melon_rush` | two sites: `_harvest_ready` early-harvest allowance + a dispatch-side melon-carry check | no (0 → both off) | yes — 116-131/719 turns differ, mixed sign | **eligible for economic testing, BUT** historical candidate files `O6_MELON_RUSH.py` / `B3_05_MELON_RUSH_REF.py` exist in `candidates/` predating the current `directions.yaml` ledger — check those files/any surviving notes before re-running, may already be a closed lead under an informal name |
| `straw_delay` | `if c=="STRAWBERRY" and day < KNOBS["straw_delay"]: continue` (skip planting) | no (0 → day<0 never true) | yes — 142-161/719 turns differ, net negative-leaning on 2/3 seeds | **engaged → eligible for economic testing**, but weakest prior (net negative lean in this quick probe) |
| `fert_carry` | feeds fertilizer-carry accounting alongside `fert_buy`/`fert_keep` | yes (used every day `fert_buy>0`) | yes — 175-203/719 turns differ, largest single-seed swing (-6,327) | **engaged, behavior-changing but noisy/mixed → eligible for economic testing**, treat as a `fert_buy`/`fert_keep`/`fert_carry` group, not standalone |

**Net of the audit:** 3 of 12 dormant knobs are dead under the current regime for structural reasons (one orphaned
— `sell_hourly` — and two gated by an already-off sibling knob — `drop_radius`, `wheat_cap`); 1 (`capital_hour2`)
is already closed in the ledger and the probe just reconfirms the known mechanism; the remaining 7
(`wheat_tiles`/`wheat_per_animal` as one lever, `wheat_stock`, `wheat_hold_days`, `wheat_water_tier`,
`melon_rush`, `straw_delay`, `fert_carry`) are genuinely engaged and eligible for economic testing, with
`wheat_stock` the cleanest signal (consistent sign across seeds) and `melon_rush` needing a check against
historical candidate files first. None of these 7 has been panel-tested — this audit only establishes
engagement (Grace's steps 3-4), not economic value (step 5 onward is the next cycle, and per the agreed
sequencing, DEMAND_SHARE/yield-calibration work comes before spending a panel on any of them).

## 4. Calibration instrumentation (Sep 12, per Grace's calibration-first sequence)

Built two new instruments, both reusing the existing engine-driving code (`allocation_matrix.py` / the same
`_commit_unit` trade-recording pattern) rather than reimplementing the game loop.

### 4a. Crop-yield calibration (`tools/yield_calibration_wtm.py`) — WHEAT/TOMATO/MELON vs realized

O36_MIN_HANDS2, 4-tape panel, seeds 11-30 (80 games with plantings for WHEAT/MELON, fewer for CARROT/TOMATO):

| crop | assumed units/planting | realized units/planting | ratio | per-game range | read |
|---|---|---|---|---|---|
| **WHEAT** | 5.0 | **3.80** | **0.76** | 3.4-4.0 (tight) | **Real, consistent 24% overstatement — same shape as the pre-O24 STRAW_UNITS bug.** |
| TOMATO | 5.0 | 6.20 | 1.24 | n=1 game only | Not a yield-calibration finding — TOMATO is barely ever planted at all under current sizing (engagement problem, not a units problem; see 4c). |
| MELON | 6.0 | 5.96 | 0.99 | 5.8-6.0 | Already accurate — no correction needed (sanity check: matches the "melon window" work being closed already). |
| STRAWBERRY | 7.5 | 6.03 | 0.80 | 5.0-7.2 | Reproduces the already-known strawberry coverage gap (`kaggriculture-strawberry-coverage-gap-o28-sep11`, realized 5.6-6.0 vs 7.5) — confirms the tool is measuring correctly, not a new finding. |
| CARROT | 3.0 | 2.94 | 0.98 | 2.5-3.0 | Already accurate. |

**WHEAT is the one live finding here.** Direction of the error matters: because the seed-sizing formula divides
the available demand-pool room by the assumed units/planting to decide how many plantings to buy
(`k = room_units // CROP_SPECS[c]["units"]`), an OVERSTATED units constant makes the allocator plant FEWER
wheat tiles than the pool would actually support — this is the opposite direction from the original
STRAW_UNITS bug (which understated yield and caused over-planting). Correcting WHEAT's constant toward ~3.8
would let the allocator plant MORE wheat where the pool has room — whether that is profitable depends on
whether the wheat market has room for more supply (see 4b below), which is the same "produce more ≠ earn
more" caution the self-model doc already raises. Not yet a candidate — needs the panel, and needs 4b read
alongside it before deciding a direction.

### 4b. DEMAND_SHARE calibration (`tools/demand_share_trace.py`) — realized market split vs assumed 0.5

`candidates/K_SELFMODEL.py` has TWO separate "demand share" concepts — do not conflate them:
- `KNOBS["demand_share"]=0.55`, used only in `_demand_room()` for ANIMAL sizing — already knob-swept
  (`demand_share_up`, tested at 0.65, ABANDON: won h2h +1,350 but reversed on panel -503/-1,663).
- The global constant `DEMAND_SHARE = 0.5` (line ~91), used only in the CROP seed-sizing `pool` formula
  (line ~589) — **never tested, this is the one flagged in the original audit.**

Method: realized share = my units sold of a crop / (my + opponent units sold), same games, split into
day-phase (early/mid/late). One opponent (`tape_alaylm_106813359`), 15 seeds (11-25) — an exploratory pass,
not yet contract depth:

| crop | early | mid | late | ALL |
|---|---|---|---|---|
| **WHEAT** | 0.33 | 0.40 | 0.34 | **0.36** |
| MELON | n/a | 0.45 | 1.00 (small n) | 0.53 |
| STRAWBERRY | n/a | 0.40 | 0.47 | 0.45 |
| CARROT | n/a | 1.00 (small n) | 0.42 | 0.43 |
| TOMATO | n/a | n/a | 1.00 (n=31 units, one-sided) | 1.00 |

**WHEAT again stands out**, and in the same direction as 4a: realized market share (0.36) is well below the
assumed 0.5, consistently across all three day-phases (not just an endgame artifact). This tape is a
significantly stronger wheat seller than we are. MELON/STRAWBERRY/CARROT sit closer to 0.5 (0.42-0.53) —
roughly consistent with the assumption, though not a precise match; TOMATO's "1.00" is a single-sided small
sample (we sold the only 31 units recorded), not evidence of anything.

**Two independent signals now point the same way on WHEAT**: the seed allocator both overstates how much a
wheat planting yields (4a) AND overstates how big a share of the wheat market we capture (4b). Both errors
push in the SAME direction — toward under-committing to wheat relative to what the pool math would otherwise
support, on a crop where this one tape in particular dominates. This is the strongest, cleanest lead the
audit has produced: a real, consistent, two-instrument-confirmed miscalibration on a single crop, not a
diffuse effect across all five.

### 4c. Housekeeping finding: TOMATO is barely planted at all

Across every panel run in 4a/4b, TOMATO plantings are near-zero (1 game with any planting out of 100+ sampled).
This is a separate, prior question to yield calibration — something in the seed-sizing loop's per-crop `val`
scoring, `min_val=12` cutoff, or `cutoff=20` day limit is effectively excluding TOMATO before yield ever
matters. Worth a quick trace of why TOMATO never clears the `best` selection in the seed loop, but that is a
different instrument than either calibration trace above — noting it here rather than chasing it now.

### Step 4 (melon_rush lineage check, done before any ranking)

`melon_rush` was already informally tested pre-ledger: `docs/schedule-block-findings-sep04.md` records
"C1 + sell_hourly / drop_min / capital_hour2 / melon_rush: -14k to -27k, no-op or worse" (Sep 4, on the old C1
chassis), and `docs/block-library.md` records a related harvest-first-melon block as "+$98/game, t=1.16 ...
NO-OP / marginal" against E1. Both are negative-to-flat priors, on an older chassis lineage, not the current
O26/O36 one. Net: `melon_rush` carries a real negative/no-op history and should sit at the BOTTOM of any
engaged-knob priority list, not be treated as fresh, per Grace's step 4.

### Next: revised priority if/when engaged knobs are revisited

Per Grace's step 5, only after WHEAT's calibration is resolved (a real panel deciding whether to correct
`CROP_SPECS["WHEAT"]["units"]` toward ~3.8, and whether the wheat-market-share finding changes that
direction or magnitude) should the engaged-knob list be revisited. `wheat_tiles`/`wheat_per_animal` and
`wheat_stock`/`wheat_hold_days` are now suspect for a different reason than originally audited: their
apparent engagement in the Sep-12 probe may be partly compensating for (or fighting against) this same
WHEAT sizing miscalibration rather than being independent mechanisms — resolve the calibration first, per
the stated research principle, before spending a panel on any of them.

## 5. Wheat headroom / marginal-demand probe (Sep 12, before any corrected-constant candidate)

Per Grace's caution -- calibration error ≠ profitable correction, and the two WHEAT corrections are not
necessarily additive -- built `tools/wheat_headroom_trace.py` as a measurement-only counterfactual: it reuses
K_SELFMODEL's own `perceive()` and `_daily_demand()` functions (not reimplemented) to recompute the seed-sizing
`room_units` formula for WHEAT under BOTH corrected constants together (units 5.0->3.8, DEMAND_SHARE 0.5->0.36)
using the exact same observation the real policy sees each turn, without changing its actual behavior.
Also tracks realized price vs same-day sold volume, and mine-vs-opponent sold totals, as a price-impact /
market-share cross-check. Small exploratory sample (O36 vs tape_peterparker, seeds 11-13, 3 games) --
directional only, not a panel.

**1-4 (market condition read):** mine/opp WHEAT units sold ratio = 451/772 = 0.58, i.e. realized share
≈0.37 -- matches the earlier demand_share_trace.py reading (0.36) almost exactly, a good cross-check.
Realized price does NOT fall as our same-day sold volume rises -- it's mildly HIGHER on our high-volume
days ($37.1 at 0 units sold that day, $42.2 at 26+ units sold that day). This is consistent with reverse
causality, not headroom: the sell logic only sells WHEAT "if price >= wheat_sell_price(30)", so high-volume
days are high-volume BECAUSE the price happened to be favorable that day, not the other way around. In the
observed range of our current (modest) supply, there is no visible sign we are already depressing our own
price -- but this says nothing about what happens if supply increased substantially, which this small sample
can't observe (we never actually supplied more).

**5 (the net counterfactual, both corrections combined -- the key number Grace asked for):** summed across
all day-0/1 seed-sizing decision points in the 3 games, the room-implied plantings under the REAL constants
totalled 2,272/game vs 2,115/game under the CORRECTED constants (both, together) -- a NET DELTA of **-158
implied plantings/game, i.e. slightly FEWER, not more.** The two corrections partially cancel: the lower
units constant (3.8 vs 5.0) mechanically INCREASES implied room (dividing the same pool by a smaller number),
but the lower DEMAND_SHARE (0.36 vs 0.5) SHRINKS the pool itself, and the share effect wins narrowly. This
directly confirms Grace's caution -- correcting either constant alone would have looked like "plant a lot
more wheat"; correcting both together, properly, shows a much smaller and even slightly negative combined
effect.

**Caveat on this instrument:** the raw room-units number (thousands/game) is not capped by the real
formula's other constraints (tile space, `free` cash, the day's 20-unit BUY_SEED cap, or competition against
STRAWBERRY/MELON/CARROT for the same day's "best" pick) -- so the absolute magnitude is not a real planting
count, only a directional comparison between the two constant sets under identical caps (since both share
the same uncapped formula). The comparison is meaningful; the raw numbers are not.

**Read: this does NOT clear the bar for building an isolated corrected-WHEAT_UNITS/DEMAND_SHARE candidate
yet.** The standalone signals (4a/4b above) were each individually suggestive of under-investment; the
combined, causally-honest counterfactual is a wash-to-slightly-negative, and there is no price-collapse
evidence pointing the other way either. Per the discovery-phase decision rule (docs/discovery-phase-sep11.md
top), this resolves to **Outcome 3: environmental variation / no clear policy lever** on the combined
question, though the standalone yield miscalibration (4a, tight range, 80 real games) and market-share
miscalibration (4b) remain real, documented facts about the self-model worth having corrected the internal
model of even if the net planting-quantity effect is small. Recommendation: do not build a
corrected-WHEAT_UNITS candidate off this probe alone. If this is worth pursuing further, the next real step
would be a capped, realistic version of this same counterfactual (respecting the 20-unit/day cap and
competition against other crops) rather than a bigger sample of the current uncapped one -- the uncapped
number is not going to converge to something more decision-relevant with more seeds.

## 6. Capped headroom probe — CLOSES the combined WHEAT lead (Sep 12)

Per Grace's direction, built the capped follow-up cheaply by reusing the existing trace's structure
(`tools/wheat_headroom_trace_capped.py`): replicates K_SELFMODEL.py's ACTUAL seed-selection while-loop
(the value-density competition across all 5 crops, capped by tile space, the daily 20-unit BUY_SEED cap, and
at most 4 crop picks/day) twice per decision day — once with real WHEAT constants, once with both corrected
(units 3.8, WHEAT's own pool at share 0.36) — and compares the WHEAT `k` the competition actually selects.
Approximations kept simple by design (free budget ≈ observed cash, pending_place ≈ 0, no `_load_model`/
MAX_HANDS labor check) bias both passes equally, so they don't distort the real-vs-corrected comparison that
matters even though absolute k values run a bit high.

**Result, 16 games (2 tapes x 8 seeds):**

| | mean WHEAT plantings/game | days WHEAT wins a slot (of ~15) |
|---|---|---|
| REAL constants (5.0u, share 0.5) | 82.6 (range 42-120) | 12.2 |
| CORRECTED constants (3.8u, share 0.36) | 52.3 (range 5-103) | 7.2 |
| **net delta** | **-30.3/game** | **-5.0 days** |

Same sign as the uncapped probe (section 5, -158/game uncapped vs -30.3/game capped) — the capped version, if
anything, sharpens the conclusion: correcting WHEAT's yield and market-share assumptions TOGETHER would make
the seed-selection competition choose wheat LESS often and in smaller quantity, not more, because the pool
that WHEAT competes for shrinks (lower share) faster than the lower unit-cost inflates its per-planting
value density against the other four crops.

**Formal disposition: ABANDON the combined WHEAT calibration lead.** Two independent measurement passes
(uncapped and capped, the capped one respecting real tile/cash/daily-cap/cross-crop-competition constraints)
agree in sign and are not close to zero. The individual miscalibrations remain true and documented (WHEAT
realized yield 3.8 vs assumed 5.0, tight; realized market share 0.36 vs assumed 0.5, consistent across
day-phases) — but jointly correcting them does not expose an economically actionable under-investment. This
is a genuine negative result: **the WHEAT yield and DEMAND_SHARE constants are individually miscalibrated,
but correcting them jointly does not expose economically actionable under-investment** — recorded so the
project does not rediscover and re-test these same two constants later.

## Section 7: TOMATO near-zero-planting exclusion-gate trace (Sep 13)

Question (Grace): why does TOMATO almost never become plantable under the actual O36 policy? Trace every
exclusion gate -- demand room, seed availability, cash, tile competition, labor, day cutoff,
profitability/ranking -- and quantify which one is actually responsible.

Method: `tools/tomato_gate_trace.py` replays the real seed-selection competition loop
(`candidates/K_SELFMODEL.py` lines ~576-609) for TOMATO specifically on every day>=1 decision point,
classifying each day into exactly one of: day_window, sell_window, demand_room, min_val, loses_ranking,
k_zero, planted. Static gates (day_window/sell_window/demand_room/min_val) are TOMATO-only and don't
depend on iteration order; loses_ranking/k_zero/planted require replaying the full competition against
MELON/WHEAT/STRAWBERRY/CARROT.

Panel: 80 games (seeds 11-30 x 4 tapes: peterparker, alaylm, bahaenes, yangkuang2), KAGG_FIXED_SHOPS=1,
2320 TOMATO decision-day observations.

Result -- fully deterministic across all 80 games, zero variance:
| reason | count | % |
|---|---|---|
| loses_ranking | 1600 | 69.0% |
| day_window (day>20 cutoff) | 720 | 31.0% |
| sell_window | 0 | 0% |
| demand_room | 0 | 0% |
| min_val | 0 | 0% |
| k_zero | 0 | 0% |
| planted | 0 | 0% |

TOMATO is **never** individually gated -- it never fails demand-room, never fails the min-value floor,
never fails on cash/space (k_zero), and its sell window never closes before its plant window does. Every
single eligible day (day 1-20), TOMATO passes all four static gates and then loses the value-density "best"
comparison, 100% of the time. Beaten by: MELON (515/1600, 32%), WHEAT (462/1600, 29%), STRAWBERRY
(133/1600, 8%), CARROT (55/1600, 3%) -- these sum to less than 1600 because a day can have TOMATO beaten by
different crops across loop iterations; MELON/WHEAT dominate.

Mechanism (from CROP_SPECS, val = min(units,room)*price/cycle, price capped at 2x base):
- TOMATO: units=5.0, base=60, cycle=12 -> val ceiling 25 (50 at 2x-price cap)
- WHEAT: units=5.0, base=25, cycle=5 -> val ceiling 25 (50 at cap) -- tied with TOMATO
- CARROT: units=3.0, base=35, cycle=4 -> val ceiling 26.25 (52.5 at cap) -- tied with TOMATO
- STRAWBERRY: units=7.5, base=120, cycle=18 -> val ceiling 50 (100 at cap) -- 2x TOMATO
- MELON: units=6.0, base=250, cycle=12 -> val ceiling 125 (250 at cap) -- 5x TOMATO

TOMATO's long cycle (12 days, same as MELON but at 1/4 the base price) puts its value-density at the very
bottom of the crop set, tied with WHEAT and CARROT and dominated by MELON and STRAWBERRY. WHEAT usually
gets pre-reserved via the separate wheat-tile-floor logic before the competitive loop even runs, so in
practice TOMATO is squeezed out mainly by MELON (whenever melon room is open) and secondarily by
STRAWBERRY, with WHEAT filling remaining slots when its floor isn't already met.

**Disposition: Outcome 2 (known/explained mechanism, not a bug) with a possible Tier-2 candidate premise.**
This is not a hidden gate, cash constraint, or labor constraint -- it is the seed-allocator's own
value-density ranking correctly deprioritizing TOMATO given its current CROP_SPECS constants. Two distinct
follow-up questions this opens (not yet investigated, not authorized to act on without further direction):
1. Is TOMATO's cycle=12/base=60 assumption itself accurate (an O24/O26-style calibration check), or is the
   allocator using a wrong cycle/price and TOMATO would rank competitively if corrected? -- this is a
   calibration question, same class as the closed WHEAT lead.
2. Even if TOMATO's constants are accurate, is there a real-world edge case (e.g. late-game when
   MELON/STRAWBERRY windows have closed but TOMATO's hasn't) where TOMATO's exclusion is NOT structurally
   guaranteed and a genuine missed opportunity exists? The trace above shows 0/1600 planted, suggesting no,
   but this hasn't been separately checked late-game (day 17-20, after STRAWBERRY cutoff=17 and
   MELON cutoff=16) where TOMATO's competition should be thinner.

Late-game check (day 17-20 only, after MELON cutoff=16 and STRAWBERRY cutoff=17, same 80-game panel, 320
observations): still 100% loses_ranking, 0 planted. Beaten by WHEAT (222/320, 69%), CARROT (49/320, 15%),
STRAWBERRY (4/320, residual day-17 overlap). Confirms question 2 above: TOMATO's exclusion is structurally
guaranteed across the entire eligible window, including late game -- there is no thin-competition pocket
where it currently slips through. Any future action on TOMATO would have to go through question 1
(a calibration check on its cycle/base-price assumptions), not a "missed window" fix.
