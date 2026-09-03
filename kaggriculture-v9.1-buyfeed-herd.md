# v9.1 Buy-Feed Herd → v9.2 Parallel Assembly — 2026-08-06

> **SUPERSEDED AS CHAMPION by `main_v9.2_parallel_build.py` (commit ea2b405), same session — see the v9.2 section at the end of this doc.** v9.2 vs v9.1: 20/28 seeds, +$2,816/game, t=+3.64. v9.2 vs v8.3 direct: 21/28, +$2,962/game, t=+4.49.

## Result

`main_v9.1_buyfeed_herd.py` (committed 3dc4a8b) beats main_v8.3.py **21/28 unique seeds, +$2,495/game, t=+2.73, 95% CI [+$706, +$4,285]/game — entirely positive.** Both-seats protocol, seed sets {1–15} ∪ {4,11,19,33,50,77,88,101,150,250,404,606,707,909,1234}. No crashes in ~90 games. Clears the promotion bar that rejected v8.8–v8.13 (v8.3 itself was promoted on +$1,894/game).

Not yet submitted to the ladder.

## The design change

One assumption removed: **feed is bought from the market, not grown.** The Aug 6 ledger instrumentation showed the top-tier herd script funds 14–15 animals by buying ~1,100–1,300 wheat units (accepting a -$10k wheat book as a feed bill), keeping all land and labor on premium crops. Every prior sheep experiment (v8.9/8.10/8.11/8.12) kept grow-feed wheat floors and died of strawberry cannibalization — the sheep were never the problem, the feed logistics funding them were.

Base: main_v8.11.py (its 10-animal support system — service hands, loosened crop gate, sheep composition floor — is the validated chassis). Changes, all tagged `v9.1` inline:

- Wheat planting removed entirely (`want["WHEAT"]` deleted, wheat-floor constants zeroed); feed bought continuously (per-turn cap 10→24, `EXPANSION_WHEAT_BUDGET_FRAC` 0.15→0.50).
- Fleet: cap 10 (iter C), sheep floor {4:1, 6:2, 8:3, ...} → lands ~5 cow + 5 sheep. Purchase windows pruned to payback runway (iter B): COW last_day 22→12, SHEEP 22→15 — a cow placed day 14 grosses ~$1.5k against ~$1.5k feed + $400 capital.
- Wool-glut stop: sheep buys halt while WOOL inventory ≥ I0+30 (herd-vs-herd protection; never fires vs the mass field).
- `want["STRAWBERRY"]` ph1 14→20, `MELON` 10→12 (labor freed from ~20–40 wheat tiles).

## What each iteration taught

- **v1 (fleet 15, 5 service hands):** mechanism worked (8 cow + 6 sheep, wool +$22.6k) but lost the mirror -$4.9k — service hands starved crop planting during the ramp; strawberry standing tiles halved.
- **iter A (service hands→3, bigger seed targets):** flipped seed 1 positive. Gate: 11/15, +$1,795/game, t=1.33 — blowout losses on seeds 3/15 (-$21k/-$27k).
- **iter B (prune late animal buys):** +$1,795→ same wins, tails softened.
- **iter C (fleet 15→10):** the blowout mechanism was labor saturation — at 12 animals, weeds hit 22 (vs v8.3's 2) and unwatered strawberry tiles died late-game exactly when prices peak. 10 is the service capacity v8.11 validated. Gate: t=+2.73, promoted.

## Economy (seed 1 mirror ledger, v9.1 vs v8.3)

STRAWBERRY $36.2k vs $36.7k, MILK $29.7k vs $29.9k, MELON $18.7k vs $21.1k, FERT $9.5k vs $8.7k — crop economy preserved within noise. WOOL **+$19.9k vs +$2.2k**; WHEAT book -$10.0k vs -$1.9k (the feed bill). Net: wool is a pure addition, funded by bought feed, cannibalizing nothing.

## Caveats

- **Does not close the top-tier gap:** vs `opp_scenario_v14` (herd clone) the paired diff is +$1,806/game, t=0.88 (n.s.) — still ~-$60k/game. In herd-vs-herd the wool pool saturates (sq glut curve) and the edge vanishes. v9.1's payoff is against the ~93% mass field, whose wool pool is empty.
- 7/28 seeds still lose (worst -$12.7k) — v8.3's own fleet occasionally reaches 8 animals with a 55-tile strawberry board and out-earns us late. Variance, not a bug.
- Our feed buying (~600–900 units/game) raises the shared wheat price, handing a v8.3-style opponent roughly +$3–5k on its wheat sells; already priced into the measured margins.

## Next levers (in expected-value order)

1. Submit v9.1 to the ladder; judge vs the clone-fingerprint field from the daily replay sync, not the public score alone.
2. The remaining ~$60k top-tier gap: their herd is in place by ~day 10 (ours finishes ~day 15 through the serial farmer build pipeline) and they still out-earn us on strawberry units per tile. Parallelizing/earlier fleet assembly and strawberry replant cadence are the measured deficits.
3. MELON dipped -$2.4k (76 vs 91 units) — planting-cadence residue; a small want/cutoff tune may recover it.

---

# v9.2 Parallel Herd Assembly — NEW CHAMPION (commit ea2b405)

## Result

`main_v9.2_parallel_build.py` beats v9.1 **20/28 seeds, +$2,816/game, t=+3.64**, and beats v8.3 directly **21/28, +$2,962/game, t=+4.49, 95% CI [+$1,670, +$4,255]/game** — the strongest gate result in the project. Vs the herd clone (opp_scenario_v14, paired): **+$5,139/game vs v8.3's baseline, t=+1.86** — borderline, but the first measurable compression of the ~$62k top-tier gap. Not yet ladder-submitted.

## Design

Two changes on v9.1, both aimed at herd completion day (~15 → ~13, with denser mid-game placement):

1. **Parallel build pipeline.** v9.1 serialized animal setup through the farmer (one buy→build→carry→place cycle at a time). v9.2 runs up to `MAX_CONCURRENT_BUILDS = 3` cycles at once: each in-flight plan is pinned to a worker slot at purchase (0 = farmer, k ≥ 1 = hands[k-1]); the pinned worker runs the existing `animal_setup_action` state machine (it already took generic pos/carry). Site selection excludes other plans' claimed sites; same-species buys are allowed while shed stock is fully claimed by existing BOUGHT plans. Overnight hand resets are safe by construction: carried animals auto-drop to the shed, reconcile falls the plan back to BOUGHT, the slot resumes next day.
2. **Herd capital ahead of seed budget (iter D).** The animal-purchase block now runs before the seed pipeline in economy(), so early-game cash reaches the $550/$650 animal gates before seeds consume it (purchase windows close by day 12/15, so late-game order is unchanged). min_money trimmed 700/800 → 550/650.

## Negative result worth keeping (iter E)

Bypassing the crop-space and feed-budget-fraction gates for the first 6 animals through day 8 completed the fleet by day 11 but **collapsed money -$11.7k on seed 1** — early pastures and capital cannibalize early crop establishment. Those gates encode a real constraint; the win comes from *ordering* (capital priority + parallel labor), not from *loosening* safety gates. This mirrors the iter-C lesson (fleet 12+ saturates labor): every profitable change so far removed a false coupling; every rejected one bypassed a true constraint.

## Remaining known deficits vs top tier (~-$57k after v9.2)

Fleet still stalls at 2–3 animals until ~day 8 — the binding constraint there is genuinely cash flow plus early crop-space scarcity at 1–2 quadrants, per iter E's failure. The other measured deficit is strawberry units per tile (replant cadence / fertilizer cycle-compression) — untouched by v9.2, next lever.

---

# v9.3 Fertilize Cycle-Compression — NEW CHAMPION (commit 7c7b62f)

## Result

`main_v9.3_fertilize.py` beats v8.3 **28/28 seeds, +$10,454/game, t=+18.42, 95% CI [+$9,342, +$11,566]/game — a clean sweep, zero losses**, the largest champion margin in project history by roughly 4x. Vs v9.2: 22/28, +$6,438/game, t=+5.26. Vs the herd clone (opp_scenario_v14, paired vs v8.3 baseline): **+$10,435/game gap compression, t=+5.08** (from ~-$62k toward ~-$52k). Not yet ladder-submitted. Cumulative v9 line over v8.3: buy-feed herd → parallel assembly → fertilize ≈ +$10.5k/game.

## The mechanism — and a graveyard verdict overturned

Action census vs opp_scenario_v14 (seed 1): **they run 82 FERTILIZE actions/game; we ran 0.** They extract ~6 strawberry units per planted lifecycle from 35 plantings; we extracted ~3.2 from 50. The engine truth (re-verified in `_daily_refresh_plants`): a watered+fertilized production event yields **2 units instead of 1**, and `max_yield=4` caps *unharvested accumulation*, not lifetime output — with prompt harvest (which our task system already does), a covered strawberry lifecycle produces up to 8 units. **The v8.11_berry conclusion "fertilizer can't raise ongoing crops' lifetime yield" was an implementation artifact, not an engine rule.** The economics per FERTILIZE action: ~1–2 covered events = +1–2 strawberries (~$220–450) against one forgone fertilizer sale (~$66–100) and a few worker-steps.

## Implementation (minimal labor by design)

- `perceive()` builds `fert_targets`: ongoing-crop tiles (STRAWBERRY/TOMATO) with production events remaining, no active fertilizer, age inside the event window.
- Dispatch pass in `_agent`: workers who *already carry* fertilizer (from routine `COLLECT_FERTILIZER` at our own pastures, ~150/game, free) and have fallen through to ordinary crop duty divert to the nearest eligible tile. No preemption of urgent water/feed/harvest/animal work.
- Iter F (the step that made it work — first attempt managed only 19 fertilizes/game because economy() sold every collected unit the moment it hit the shed): keep a 6-unit shed reserve until day 26, and let crop-duty workers already standing at the shed (deposit trips end there) restock 2 units when targets are pending. Fertilize rate: 62–88/game.

## Scoreboard, end of Aug 6 session

| agent | vs v8.3 (28 seeds, both-seats) | vs herd clone (paired diff over v8.3) |
|---|---|---|
| v9.1 buy-feed herd | +$2,495/game, t=+2.73 | +$1,806, n.s. |
| v9.2 parallel assembly | +$2,962/game, t=+4.49 | +$5,139, t=+1.86 |
| **v9.3 fertilize** | **+$10,454/game, t=+18.42, 28/28** | **+$10,435, t=+5.08** |

Remaining vs top tier (~-$52k): early-fleet cash flow (true constraint per iter E), their remaining strawberry/melon coverage (they also fertilize melon in its watering window), and wool/milk scale. Melon fertilize-in-window is the obvious next small lever; the day-8 cash-flow stall is the structural one.
