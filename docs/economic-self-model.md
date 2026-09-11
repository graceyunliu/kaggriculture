# The economic self-model (Sep 11, from the O15 → O26 programme)

What is fed back into the engine, what is fed back into the evaluation loop, and what is deliberately **not**
hard-coded. Read this before proposing a new candidate.

## The organising idea

Every real win from O16 to O26 was the policy being told a true fact about its own farm or the market it already acts
in — not a new heuristic. The engine now carries a small explicit self-model, and a proposed change should say which
of these five questions it corrects:

> **What will this unit produce? What will it cost? When will it arrive? What will it displace? What happens to the
> market if we add it?**

## Tier 1 — factual corrections, in the chassis (`candidates/K_SELFMODEL.py`, `evolve/chassis.py`)

Each is a top-level constant/switch so the loop can tune it and so the chassis with everything off is exactly O15
(verified byte-behaviour, `evolve/o26k_check.py`).

| fact | constant | evidence |
|---|---|---|
| A strawberry planting yields ~7.5 sellable units, not 4.5; sizing plantings from a stale constant over-plants by 40% and depresses our own price. | `STRAW_UNITS = 7.5` | O24: own +5.5k, margin +5.8k vs O22; optimum is the true yield (6.0 +3.5k, 9.0 +3.3k, 20 −0.9k) |
| A carrot planting yields 3.0, not 4.0. | `CARROT_UNITS = 3.0` | O26: own +1.4–1.6k (other session) |
| Labour is re-bought every night on a convex (fibonacci) curve; the n-th hire of a day costs `_fib(n)`. Buy the next hand on its marginal price, not because a target says you are short. | `HIRE_MAX_MARGINAL = 144` in `_hire_plan` | O25 / H_GATE144: own +1.3–1.6k |
| Our melon crop arrives over 14 hours while the melon price pool drains in 6; the tapes harvest 60 units by h9 and sell at $217–260, we dumped 30 at the d11 h0 price. | `MELON_LATE_FERT`, `MELON_MORNING`, `MELON_MORNING_LAST_HOUR = 8`, `MELON_MORNING_MIN_YIELD = 6` | O22: own +0.4–1.8k, margin +0.9–2.5k on three seed sets |
| Fertilizer lasts 3 days and an ongoing crop produces every `interval` nights: applied on a production day it covers two nights, on an off day one. | `FERT_PHASE_RULE = 1` | O23 (engine read) |
| `PRODUCTS` contains FERTILIZER, so carried fertilizer was treated as cargo to deposit and walked back to the shed. | `FERT_IS_INPUT = 1` | O23: coverage 1.9 → 2.7 nights/planting (own +0 alone — see Tier 2) |
| Other workers' positions matter: one global cost matrix over free units × open crop tasks beats per-unit nearest-task sweeps. | `ORCH_ON = 1`, `ORCH_P_*`, `ORCH_COMMIT` | O16: own +1.7k, margin +3.1k vs O15 |

**Principle:** `expected production ≠ planting count × stale constant`. The allocator sizes commitments from expected
output; it does not plant because capacity exists.

## Tier 2 — economic concepts (how to reason about the next change)

1. **Marginal-unit profitability.** For any unit (tile, hire, fertilizer, animal, land):
   `marginal_value = incremental own revenue − incremental cost − displaced-work cost − price-impact cost`.
   This is compiled offline into the constants above; the runtime does not search. Calibrated facts so far: the
   marginal strawberry unit is demand-limited (price impact eats it); the 13th daily hire costs 233 against 34 for the
   9th; more fertilizer raises output but not profit; the melon window is profitable to h8 and negative after.
2. **Demand-aware portfolio sizing.** In this market *same output from fewer inputs* pays; *more output* mostly does
   not (three independent results: fert phase, fert_buy 8, fert courier — all +margin, own ≈ 0). Ask "is the next unit
   economically useful?", not "can I produce more?".
3. **Cycle-level commitments, not per-action urgency.** A 1–4 h delay of one action has no measurable consequence
   (3,060 counterfactuals); consequence lives at the block level — the melon morning, the animal-service block, a
   planting commitment. Reason about blocks and what they displace.
4. **Displaced work is a first-class cost.** The value of prioritising work is compared with the value of the work it
   displaces. The melon convoy is the worked example: profitable on the crew's slack, negative when it eats feeding.
5. **Herd scale is capped by market saturation, not chassis reachability.** Cows and sheep both plateau at a real
   `demand_room` (milk/wool market) ceiling once the land/knob-level reachability limits are relaxed (Sep 11
   `land_reserve`/`max_sheep`/`geese_day_limit` fix + validation, 360 games/3 opponents) -- own money fell in every
   panel when sheep scale was pushed past the default. Treat any apparent hard cap (`MAX_SHEEP=14`, a dead purchase
   gate) as a reachability question first, but once reachability is fixed, expect the market to be the real wall.

## Tier 3 — evaluation infrastructure (`evolve/cascade.py`, `evolve/db.py`)

* Every candidate is scored on **own money, opponent money and margin** on the fixed-shops tape panel
  (`KAGG_FIXED_SHOPS=1`), and classified: `architecture` (own ↑, margin ↑ → promotable), `exploit` (margin ↑, own ↓ —
  input-price attack, never core), `economic` (own ↑, margin ~flat — shared-market spillover, e.g. holding wheat:
  the tapes are net wheat sellers), `failure`, `neutral`. Promotion requires margin ≥ floor **and** own ≥ floor.
* Closed hypotheses are seeded into `db.REJECTED_MECHANISMS` and shown to the proposer as "do not re-propose":
  worker matching, per-task delay VaR, chronic service debt, fertilizer output maximisation, tape wheat portfolio via
  knobs, speculative inventory holding, input-price-attack capital timing, melon convoy beyond the crew's slack.
* Islands: `o15` (the yardstick, control), `best` (chassis defaults), `wide`, `queue`.

## Deliberately not hard-coded

* A universal hire cap. The mechanism (marginal price) is validated; 144 is environment-sensitive and is a knob.
* A universal melon schedule. The window depends on herd size on day 10 (we run 12–16 animals, the tapes 10–11).
* "Produce fewer strawberries." That is the current consequence of the corrected yield, not a rule.
* Tape-derived portfolio proportions. The wheat line (31% of the tapes' labour, net sellers) does not transplant onto
  a 12-sheep farm; every knob-level attempt failed a gate.

## Method rules that came out of this

* Do not promote an observational ranking (action table, one-seed counterfactual) into a decision weight without a
  multi-seed, multi-opponent intervention panel.
* Judge every candidate on both metrics over ≥2 fresh seed sets; head-to-head vs the frontier is a weak ranking
  signal for timing and market mechanisms.
* Measure first (allocation matrix, sale timeline, service ledger), then intervene once, narrowly.
