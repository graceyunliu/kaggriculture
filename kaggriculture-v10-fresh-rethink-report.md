# Kaggriculture v10: a from-scratch rethink

## Approach

Treated this as a first build: read the engine source and README rules
directly (not replay-mined guesses), derived the economics from the price
tables, then formed and tested hypotheses across every lever in the game —
labor, crops, animals, land, shops, market timing — against three
opponents: our own **v9.3** baseline, and the two fixed-strength ladder
opponents **opp_scenario_v14** and **opp_frontier_v12**.

One important fact about those two opponents, confirmed in earlier project
work and re-verified here: they are **fixed replay-tape clones** of the
current real-ladder leaders (Savko / Subin An), not reasoning policies —
their play is identical regardless of what we do, and they bank roughly
**$130k–$141k/game** doing it (aggressive day-0 spend, land by day 7/10,
8 cow + 6 sheep by day 10, hand cap ~12, wheat/strawberry/melon only).
"Beating" them means matching their money, not out-maneuvering a reactive
opponent.

All tests below used `seeded_h2h.py --both-seats` (plays every seed in both
seat assignments and sums — this engine has a real, reproducible ~$2.7k/seed
scoring bias that a naive swap-half comparison does not cancel).

## Hypotheses tested

| # | Version | Hypothesis | Result vs control | Verdict |
|---|---------|------------|--------------------|---------|
| 1 | v10 (ramp) | Two-phase economy: suppress ALL crop seed spend days 0–9, put every dollar into land+animals to match the clone's flat/negative day-10 money curve, then flip to full crop production | **−$96k to −$116k/game** vs v9.3 (3/3 seeds) | **Rejected, decisively.** Diagnosed, not just observed: STRAWBERRY/MELON have a fixed lifetime yield window tied to planting day. Delaying the first STRAWBERRY buy from day 0 to day 10 roughly halves its productive season (9 days left vs 19); MELON's 16-day buy window shrinks to 6. Land/animal purchases already run ahead of the seed pipeline in priority order, so they weren't cash-starved to begin with — suppressing crops just forfeited growing season for no offsetting gain. |
| 2 | v10.1 | CARROT is the most under-exploited demand pool on record (431 units, Pet Cafe shop doubles the draw) yet every version since v7 caps it at a flat, untuned 4 — scale it like the other crops | Looked neutral at 3–6 seeds; **−$8,505/game at 10 seeds (t=−2.53, real)** vs v9.3 | **Rejected.** A smaller sample masked a genuine, if modest, regression — more seed orders per turn compete for the 5-slot seed budget and the 10-slot market-order cap, crowding out higher-value orders. |
| 3 | v10.2 | Town shops are a permanent extra buyer once unlocked but no version in this lineage reads `obs["town"]["unlocked_shops"]` anywhere (confirmed by grep) — relax the sell-price floor per currently-unlocked shop backing an item, to capture more of a real, active demand pool | −$2,289/game vs v10.1, not significant (t=−1.03); several seeds came back **exactly tied**, meaning the mechanism rarely even engaged | **Rejected / inert.** Not harmful, but no measurable benefit at the price-floor relief tested. |
| 4 | v10.3 | Re-test the fleet-size ceiling (`EXPERIMENT_MAX_FLEET` 10→12) now that later versions (v9.21/v9.22) fixed the build-slot throughput that originally caused 12+ animals to saturate the hand pool | −$639/game vs v10.1, not significant (t=−1.00); **5/6 seeds exactly tied** | **Rejected / inert.** Confirms the fleet essentially never reaches 10 in the first place under the current gates — this ceiling isn't the binding constraint, so raising it does nothing.|

For a reference point, unmodified **v9.22** (the codebase's own most-evolved
prior version) was also run against v9.3 head-to-head: −$5,935/game,
not statistically significant (t=−1.77). The whole v9.x lineage clusters
within noise of itself in this matchup — consistent with the project's own
prior conclusion that this architecture sits at a real local optimum.

## Does it clear $80k/game?

Yes, comfortably, in every version tested here, when measured the way the
task specifies (average money at game end). Across the 10-seed both-seats
v9.22-vs-v9.3 run, both sides averaged **$85k–$92k/game**. Against the two
fixed-tape ladder clones specifically, our own score ranges roughly
**$58k–$92k/game** depending on seed — usually, not always, above $80k;
the clones themselves score $130k–$141k regardless of our play.

## Round 2: found a real winner — v10.5 (movement-aware crop siting)

Grace pushed back on "none beat v9.3" and asked to keep testing. Rather
than re-try variations of the same four exhausted categories, I first
re-measured whether movement overhead (flagged in project history at 66%
of unit-turns, but measured under an older, pre-`assign_tasks()` version)
was still the real bottleneck under the *current* architecture. Wrote a
one-off census (`census_movement.py`) and ran it on v9.3: **movement is
still 57–60% of every unit-turn**, barely improved from the old figure.
That's the strongest evidence in the whole project that the binding
constraint is genuinely a movement/labor-efficiency problem, not a
crop-mix or capital-timing one — consistent with three independent,
decisive failures of "add more crop coverage" (v7.9-era STRAWBERRY/MELON
bump, v9.13, and this session's own v10.4 TOMATO test, −$26k/game, t=−11.32,
10/10 losses — TOMATO's flat, never-scaled seed target turned out to be
the exact same bug shape as the old pre-fix STRAWBERRY bug, but scaling it
up made things *worse*, not better, closing off "more of any crop" as a
lever entirely).

**v10.5 hypothesis:** every worker respawns at the shed each morning (an
engine mechanic, not something we control), so a tile's real season-long
labor cost is *distance from shed × number of times it must be revisited*.
Ongoing crops (STRAWBERRY/TOMATO) need watering every single day for
their whole ~12–17 day life; one-time crops (WHEAT/CARROT/MELON) are
watered only during a short bonus window and harvested once. No version in
this project's history has ever sited crops by distance — `plantable_crops()`
returns one global priority order applied identically to every tile,
regardless of where that tile is. v10.5 makes it siting-aware: on tiles
within `NEAR_SHED_RADIUS=4` of a shed tile, ongoing crops are preferred;
on farther tiles, one-time crops are preferred. Nothing else changed — same
crop-mix *targets*, same hire/land/animal logic, same everything else.

**Result — real, and it replicates:**

| Test | Seeds | Mean margin | t | 95% CI |
|---|---|---|---|---|
| v10.5 vs v9.3 (seed set 1) | 1,7,42,99,123,202,303,555,2024,8080 | **+$11,510/game** | +3.77 | [+5,528, +17,491] |
| v10.5 vs v9.3 (independent seed set 2) | 3,11,17,33,64,77,128,256,512,777 | **+$9,424/game** | +2.48 | [+1,982, +16,867] |

Both intervals are entirely positive — this is not noise. It also
generalizes past self-play, in absolute terms (own average $/game, same 5
seeds each): **vs opp_scenario_v14, $86,971 (v10.5) vs $81,565 (v9.3),
+$5,406/game; vs opp_frontier_v12, $84,812 vs $77,427, +$7,385/game.**
Neither version comes close to beating those two fixed-tape opponents'
own $130k–141k, but v10.5 closes a real slice of that gap while beating
v9.3 head-to-head too.

**Mechanism note:** the movement-time-share itself barely moved (still
~58–60%) — the win isn't from walking less overall, it's from what happens
*during* each of those unavoidable daily walks: the same footsteps now
produce a better-matched crop-to-location assignment (short-hop ongoing
crops near the shed workers already revisit constantly; long-hop one-time
crops on land that's visited rarely regardless), so the same labor budget
converts to more harvested value without hiring anyone or changing the
crop mix.

## Round 3: extending v10.5 — one more real win (v10.6), six rejections

Grace asked for 3 more hypotheses with even higher win margins, built on
top of v10.5. Also independently confirmed v10.5 beats **v9.10**
(currently a stronger real-ladder baseline than v9.3 per Grace) by a
similar margin: +$13,096/game (seed set 1, t=+2.91) and +$12,793/game
(independent seed set 2, t=+3.34), both CIs entirely positive.

Seven follow-on hypotheses were tested, each vs the best version so far,
10 seeds both-seats:

| # | Change | Result | Verdict |
|---|--------|--------|---------|
| v10.6 | Sweep `NEAR_SHED_RADIUS` (was 4): tested 1, 2, 3, 6 | **3 beats 4: +$7,310/game, t=+2.96, 95% CI [+2,470,+12,151], 9/10.** 6 is a decisive loss vs 4 (−$12,693, t=−7.94, 10/10). 1 and 2 are statistically tied with 3. | **Adopted — new champion.** |
| v10.7 | Generalize binary near/far into 3 tiers (MELON as a "mid" tier, second radius=6) | −$8,380/game vs v10.6, t=−3.81, 9/10 losses | Rejected. |
| v10.8 | Scale the radius with unlocked-quadrant count (3/4/5/6) instead of holding it flat | −$17,578/game vs v10.6, t=−10.28, 10/10 losses | Rejected, decisively — re-confirms smaller/flat radius is better, growing it as land unlocks reintroduces the same problem that made radius=6 bad. |
| v10.9 | Weight the hire-target formula by tile distance from shed (far tasks count as "more work") | −$6,983/game vs v10.6, t=−1.99, 95% CI [−13,844,−121] | Rejected — likely pushes hiring higher, and this project's history shows more hands is almost always a net loss (exponential fibonacci cost). |
| v10.10 | Modest TOMATO/CARROT coverage bump (3→5, 4→6) now that siting makes labor more efficient | −$10,547/game vs v10.6, t=−4.76, 10/10 losses | Rejected — v10.6 improved output *per unit* of existing labor, it didn't create spare labor capacity; more plants still competes for the same saturated movement budget. |
| v10.11 | Add MELON to the near-shed-preferred crop set | **−$30,716/game vs v10.6, t=−8.78, 10/10 losses** | Rejected, the worst result of the round — melon is a slow one-time crop that occupies a tile for ~13 days; putting it in the scarce near zone locks out the genuinely-recurring STRAWBERRY/TOMATO it was competing with. |
| v10.12 | Reallocate (not add) STRAWBERRY→TOMATO mix, same total ongoing-crop count | −$2,208/game vs v10.6, t=−0.84, 95% CI crosses zero | Statistical wash — the STRAWBERRY:TOMATO ratio doesn't matter much either way; total planted-tile count is what's tuned correctly, not the split. |
| v10.13 | Double `FERT_SHED_RESERVE` (6→12), reasoning fertilizer has zero town demand so holding more back to fertilize crops should be free upside | −$17,588/game vs v10.6, t=−4.90, 9/10 losses | Rejected — the existing reserve was already well-tuned; a bigger reserve just ties up shed capacity/cash without a proportional increase in actual fertilize-dispatch rate. |

**Pattern worth recording:** the one hypothesis that worked (v10.6) was a
pure parameter sweep on the exact mechanism v10.5 had already validated.
Every hypothesis that *expanded scope* — a new tier system, a second
radius, a different formula, more planted tiles, a different crop-mix
ratio, a bigger reserve — lost, several decisively. This is a genuine
signal, not bad luck: v10.6 (radius=3) sits at a real local optimum for
this whole family of "use the shed-distance insight somewhere else"
ideas. Further movement-efficiency gains, if they exist, likely require a
different kind of lever than "adjust a constant near this mechanism."

## Round 4: skipping the 4th quadrant (v10.14) — rejected

Grace observed that real ladder players scoring in the 800s never expand
to a 4th (SE) quadrant by game end, and asked to test that directly on
top of v10.6. An older version of this exact idea exists in the
project's history (`main_v7.10c_no_se.py`, v7-era) and came back neutral
(−$234/game, t=−0.11) — but that predates v8's dispatch rewrite, v9's
animal/hire rebuild, and v10.5/v10.6's siting logic entirely, so it
deserved an independent re-test rather than trusting a 20-versions-old
result on a very different codebase.

**v10.14 (never buy SE): rejected, and this time not neutral.**
−$6,922/game vs v10.6, t=−3.33, 95% CI [−10,999,−2,845], 9/10 losses (10
seeds, both-seats).

**Why the ladder pattern doesn't transfer:** those 800-score players are
almost certainly running a structurally different economy — a smaller
number of high-throughput animals/crops serviced tightly by a compact
farm, where the freed-up $4,000 and labor fund something else entirely.
Our agent's whole economy is built around using land broadly (crops
spread across all unlocked quadrants, plus siting them by distance since
v10.5/v10.6) — removing SE just removes productive capacity without any
compensating shift in strategy elsewhere. This is the same meta-lesson
this project has hit before (see the Aug 6/7 "opening-sequence-tempo"
investigation above): copying one surface trait from a different
strategy, without the rest of that strategy's logic supporting it,
doesn't transfer.

## Round 5: hypothesizing the "compact economy" behind the ladder pattern

Grace asked to keep going: since real 800-score players never buy the 4th
quadrant, what ELSE might they be doing, and is it worth a large rewrite
to find out? Seven more hypotheses were tested, escalating in scope from
parameter tweaks to a full architectural rewrite.

**v10.15 (skip SE + raise the animal fleet ceiling 10→14):** rejected,
decisively. −$31,112/game vs v10.14 (skip-SE alone), t=−7.08, 10/10
losses. A **3rd independent confirmation** (after the original v9.1 iter
C finding and this project's earlier gate-instrumentation work) that our
architecture's animal-service capacity genuinely caps out around 10,
regardless of land footprint — not a symptom of land competing with
animals for hands, a hard ceiling in its own right.

**v10.16 (skip SE + drop CARROT/TOMATO, concentrating the crop mix into
what's left):** a real, very clean win over v10.14 — +$5,796/game,
t=+6.21, 95% CI [+3,968,+7,625], **10/10 wins**. This matches the actual
clone opponents' own crop mix (WHEAT/STRAWBERRY/MELON only, confirmed in
project memory from real replay analysis) more closely. But combined
with the SE loss, it landed at −$4,211/game vs v10.6 overall (t=−1.80,
CI barely crosses zero) — recovered most, not all, of the gap.

**v10.17 (the same crop-mix concentration, but on the full 4-quadrant
board, keeping SE):** a wash, −$4,678/game, t=−1.02, not significant.
So crop-mix concentration only pays off when land is genuinely scarce —
it isn't independently valuable in general.

**v10.18 (v10.16 + modestly more aggressive hiring, divisor 5→4):** a
wash vs v10.16, −$1,793/game, t=−0.81. More hands still doesn't help,
even on the smaller, more efficiently-sited farm.

**v10.19 (drop only CARROT, the weaker of the two, on the full board):**
looked promising on one seed set (+$3,394, not significant) but flipped
to −$452 on an independent set — a true wash once both are combined, not
a real effect.

**v10.20 — the big one: decouple animal purchase from worker-slot
pinning.** Grace explicitly authorized a full rewrite if needed, so this
attempted the mechanism the real clone opponents actually use (diagnosed
extensively in this project's history): buy animals in bulk, let them
sit as plain shed stock, and let ANY free worker claim and place one that
turn — instead of pre-pinning each purchase to one specific worker slot
for its whole multi-turn walk/pickup/place journey. Rewrote the purchase
loop (removed the `MAX_CONCURRENT_BUILDS` slot cap, added burst-buying)
and the placement dispatch (`_animal_acquire_action`, ~50 new lines,
replacing the old per-plan state machine with live-state reads: shed
stock, per-unit carry, and placed pastures ARE the fleet state, nothing
to reconcile). Verified it loads and runs crash-free first.

**Result: a clear regression, at both the old fleet ceiling and a raised
one.** At the unchanged ceiling of 10 (isolating the mechanism itself):
−$16,782/game vs v10.6, t=−2.48. With the ceiling also raised to 14 (the
clone's own fleet size): −$27,833/game, t=−5.99 — worse, not better.
**Rejected.** The pinned-slot architecture, despite being theoretically
inferior on paper (that's the whole reason this project's history kept
flagging it as the likely root cause), has accumulated many small
correctness and timing refinements across 20+ prior versions that a
from-scratch replacement doesn't automatically inherit. This wasn't a
half-hearted attempt — it's a real, working, crash-free rewrite that
simply performs worse in practice than the thing it replaced.

**What this round establishes, taken together:** the ladder players'
"never buy SE" pattern is real, but it's a SYMPTOM of a fundamentally
different, animal-centric economy (large decoupled-purchase fleet, thin
crop footprint) — not a standalone lever. Copying pieces of it (skip
land, concentrate crops, bigger fleet, more hands, a genuine rewrite of
the mechanism believed to enable it) each got tested in isolation and in
combination. Crop-mix concentration is real but conditional; everything
else — bigger fleet, more hands, decoupled placement — lost, several
decisively, confirming across three independent architectural angles
that our current chassis has a real, load-bearing ~10-animal service
ceiling that isn't a tuning artifact.

## Honest bottom line

None of the four fresh hypotheses beat v9.3 in a statistically meaningful
way — three were flat/inert, one (the boldest, a genuine architecture
rethink) was a clear, informative failure. That's a real result, not a
non-result: it independently re-confirms, via new tests rather than by
trusting prior notes, that this agent's land/animal/hire/crop-mix gates are
already close to the ceiling reachable without adopting the clone's entire
playbook wholesale (not just loosening a few gates, but actually
target-sizing the fleet/land purchases to match its day-0–10 spend curve
and accepting the execution risk that comes with it — a bigger rebuild than
this session validated).

**Recommendation stands: ship `main_v10.6_radius3.py`.** Twelve more
hypotheses across rounds 4 and 5 (skip-SE, bigger fleet, crop-mix
concentration in three variants, more aggressive hiring, and a full
animal-acquisition architecture rewrite) — one real win (crop-mix
concentration, but only conditional on also losing SE, netting to a
wash-or-slight-loss overall) and eleven rejections, several decisive.
v10.6 remains undefeated by anything built in this session after the
original v10.5→v10.6 chain. Chain of
genuine, independently-replicated improvements: v9.3/v9.10 → v10.5
(+$9.4k–$13.1k/game, siting mechanism) → v10.6 (+$7,310/game on top of
v10.5, radius tuned from 4 to 3). Combined, v10.6 beats v9.3 by
something like +$17k–19k/game (not separately re-measured as one
head-to-head — the two gains were validated in separate paired
comparisons — but both legs are individually significant with
non-overlapping-zero CIs, so the composition is trustworthy directionally
even without a single combined-effect run). All of it from ~30 lines: one
function made siting-aware, one constant swept.

Six further hypotheses built on v10.6 (see table above) — all rejected,
one wash. That's a real, informative result, not a failure to find
enough ideas: it shows v10.6 sits at a genuine local optimum for the
whole "use the shed-distance insight elsewhere" family, the same way
v9.3's land/animal/hire gates turned out to sit at a local optimum for
the "capital timing" family back in the v9.6–v9.22 round. Confirmed by
convergent evidence rather than a single result: *every* attempt to
expand scope on top of the validated mechanism lost, several decisively.

The next-highest-credibility lever, still not attempted, is still
**GOOSE/EGG** as a third animal species (341-unit demand pool, real ladder
opponents barely touch it, ≈77 EGG sold across 5 replays) — bigger scope
(6–8 functions), deserves its own dedicated build/test cycle. A genuine
*reduction* in the movement-time-share itself (still ~58–60% even under
v10.6) remains open and unclaimed — everything tested this round used
that movement more effectively without actually reducing it.

## Round 6: GOOSE/EGG (Aug 7) — REJECTED, v10.6 still champion

Built the GOOSE/EGG pipeline the report above flagged as the standing
next step. Engine-verified specs (kaggriculture.py `ANIMALS` dict):
GOOSE cost=$300 (cheapest of the three), structure=COOP (not PASTURE —
genuinely separate buildable), first_yield_day=4/interval=1 (much
faster nominal payback than COW's 8/2 or SHEEP's 6/3), max_held=4,
product=EGG (MARKET_PARAMS base=$50, T=332). FEED/CARE/HARVEST/
COLLECT_FERTILIZER/2-day-unfed-escape rules are byte-identical between
COOP and PASTURE animals in the engine — only the structure tile kind
and BUILD_* op differ.

Implementation, on top of v10.6 (no rewrite — the v10.20 decoupled-
architecture rewrite already lost decisively, see round 5): generalized
`perceive()` to also scan COOP tiles (`my_coops`/`empty_coops`, plus a
combined `my_animals` used everywhere maintenance/feed-target/service-
target/survival-check code was already species-agnostic), added an
`ANIMAL_STRUCTURE` species→structure map, made `animal_setup_action`
structure-aware (BUILD_COOP vs BUILD_PASTURE), and added GOOSE to
`ANIMAL_SPECS` (cost 300, min_money 400, start_day 0, last_day 20) with
its own feasibility gate (`_goose_expansion_feasible`, mirroring
SHEEP's, with an EGG-glut stop instead of WOOL's).

**v10.21 (`main_v10.21_goose.py`) — try GOOSE only as a last resort**,
after COW's and SHEEP's gates (both unchanged) already declined this
turn, sharing the same already-validated `EXPERIMENT_MAX_FLEET=10`
ceiling as cow/sheep (not a new/higher cap). Result: **exactly identical
to v10.6 on all 10 seeds, to the dollar** (mean margin +0, t=+0.00).
GOOSE never fired a single purchase in any of the 10 games. Mechanism:
COW+SHEEP reliably fill all 10 fleet slots well before either species'
own day-window closes (day 12/15), so by the time either gate would
ever decline, it's almost always because `n_animals >= 10` — the exact
same shared-ceiling check that then blocks GOOSE's gate too. A clean,
confirmed no-op, not a wash.

**v10.22 (`main_v10.22_goose_floor.py`) — genuine composition floor**,
added `GOOSE_FLOOR_BY_FLEET_SIZE = {3: 1, 6: 2, 9: 3}` (same pattern as
the existing SHEEP floor) so GOOSE actually displaces some COW/SHEEP
slots within the same 10-slot ceiling, tried before the SHEEP
composition check. Result: **decisive loss**, -$9,444/game (t=-2.32,
95% CI [-17,436, -1,452], 8/10 losses, 10 seeds both-seats). Smoke-test
confirmed geese were actually being purchased this time (reward
differed from v10.21's run, unlike v10.21 which matched v10.6 exactly).

Likely mechanism (not separately re-verified, but consistent with the
market constants): revenue-per-service-day, not sticker cost, is what
matters once an animal is already inside the fleet's shared feed/labor
loop. EGG's low base price ($50) more than cancels out its faster
interval — back-of-envelope pre-decay revenue rate is roughly
$50/day for GOOSE (interval 1 × base 50) vs ~$80/day for COW (base 160
÷ interval 2) and ~$67/day for SHEEP (base 200 ÷ interval 3) — so a
GOOSE occupying a fleet slot earns meaningfully less per day than the
COW or SHEEP it displaced, while still costing the same daily feed
labor (FEED consumes 1 WHEAT/animal/day regardless of species, verified
in the engine — GOOSE's faster interval doesn't reduce that). This also
explains why v10.21's true no-op didn't get a chance to reveal this:
GOOSE never actually got tested against a live cow/sheep slot until
v10.22 forced the substitution.

Given the already-3x-confirmed finding that raising the fleet ceiling
itself fails (labor/movement saturation) and this round's new finding
that EGG's revenue-per-day is lower than MILK's or WOOL's, a purely
*additive* GOOSE fleet beyond the 10-slot ceiling was not separately
tested — the same movement/labor mechanism that killed three prior
ceiling-raise attempts would apply here too, now compounded by a lower-
value animal, making a positive result very unlikely for the compute
cost. **v10.6 remains champion; GOOSE/EGG is now a closed line of
inquiry**, same status as the fleet-ceiling and land/hand-tuning
families before it.

## Round 7 (Aug 7): 21 structural-economy hypotheses — ALL REJECTED, v10.6 still champion

Grace asked for a step change: stop tuning parameters on the validated siting
mechanism and instead test genuinely different economy STRUCTURES, informed
by two new data points — (1) today's aggregate replay tally, 129W/100L/4T,
shows the dominant loss cause is `SHED_AT_CAP` (31/100 losses, the shed's
100-unit capacity blocking further storage/selling), never specifically
targeted before; (2) a screenshot of a real opponent's board showing
pastures sited near each quadrant's own center (not the shared shed),
apparent one-quadrant-at-a-time development discipline, and strawberry
concentrated into one or two diagonal quadrants. Authorized "shots in the
dark," minimum 20 hypotheses. Delegated to 5 parallel subagents by theme,
each building isolated `main_v11.N_*.py` variants on top of v10.6 and
running the full `--both-seats` 10-seed protocol. **21 hypotheses tested,
21 rejections (12 decisive losses, 9 washes), zero wins.** v10.6 is now
undefeated across 41 hypotheses total since it became champion.

**Shed-capacity theme (v11.1–v11.5)** — direct attempts to fix the
data-confirmed SHED_AT_CAP bottleneck via selling/production rhythm rather
than siting:
- v11.1 (earlier/wider force-dump trigger, CAP-35 @ hour≥10 vs CAP-15 @
  hour≥18): **exact no-op**, t=0.00 — shed_load never actually crosses even
  the widened threshold before hour 18 against this particular champion
  opponent.
- v11.2 (remove premium-crop holding-phase gate, always sell on normal
  logic): **decisive loss**, -$653/game, t=-5.97, 10/10 losses — giving up
  peak-price timing costs more than the shed relief is worth.
- v11.3 (continuous 15%-of-holdings proportional dump above 50% shed
  occupancy, price-blind): **wash**, -$4,721/game, t=-1.18, CI crosses zero
  (9/10 losses but one large outlier win drives the CI width) — price-blind
  forced selling gives away value most seeds.
- v11.4 (seed-buy targets throttled down as shed occupancy rises): **wash /
  near no-op**, -$336/game, t=-0.92 — shed occupancy rarely reaches even the
  50% throttle tier against this opponent.
- v11.5 (lower normal paced-sell price floors 0.85/0.70→0.65/0.45): **wash**,
  +$34/game, t=+0.53 — statistically indistinguishable from zero.
- **Takeaway: SHED_AT_CAP is real in the aggregate 100-game tally but didn't
  reproduce as an exploitable lever against the specific v10.6 champion
  opponent used for these paired tests — none of the 5 direct fixes moved
  the needle, and the one that touched price-timing (v11.2) actively hurt.**

**Geometric siting theme (v11.6–v11.9)** — the screenshot-inspired
hypotheses, all decisive losses, the most one-sided theme of the round:
- v11.6 (pasture at quadrant-own-center instead of near shared shed):
  **-$76,132/game**, t=-12.85, 10/10 losses — directly fights the validated
  near-shed movement mechanism (v10.5/v10.6); a quadrant's own center is
  much farther from the shed every worker respawns at each morning.
- v11.7 (gate next-quadrant purchase on current quadrant ≥70% built +≥2
  animals): **-$26,867/game**, t=-17.33, 10/10 losses — delays land
  expansion enough to lose real land-days over the 30-day season.
- v11.8 (strawberry confined to one quadrant only): **-$44,610/game**,
  t=-16.36, 10/10 losses — the highest-value crop can't fully use its own
  seed-buy target from one quadrant's tile count alone.
- v11.9 (full per-quadrant crop lock, diagonal strawberry pattern):
  **-$84,060/game**, t=-32.37, 10/10 losses, the single worst result of the
  whole round — compounded by NW being assigned WHEAT, which this codebase
  hasn't planted since v9.1 (feed is market-bought), so NW goes essentially
  unplanted under a strict lock.
- **Takeaway: the screenshot pattern doesn't transfer into this codebase's
  engine mechanics as tested — every version directly fights the already-
  validated near-shed movement-cost insight or starves land/seed
  throughput. Real opponents running this visual pattern are very likely a
  structurally different, non-transferable economy (see the v10.14/SE-skip
  finding's identical conclusion from Aug 7 round 4).**

**Capital-allocation theme (v11.10–v11.13)** — different land/animal
spend orderings, all decisive losses, 40/40 games lost in aggregate:
- v11.10 (animal-fleet-first, no land until fleet complete or windows
  closed): **-$64,543/game**, t=-14.75, 10/10 losses.
- v11.11 (land-first-maximal, animals deprioritized until quads==4 or
  day≥8): **-$55,828/game**, t=-9.15, 10/10 losses.
- v11.12 (no animals at all, budget redirected to land/seeds): **-$84,817/
  game**, t=-12.96, 10/10 losses — worst of the four, confirms the animal
  fleet is genuinely load-bearing revenue, not just competing overhead.
- v11.13 (hard 2-quadrant cap, NW+NE only, denser packing): **-$37,325/
  game**, t=-8.50, 10/10 losses — smallest loss of the four, suggesting the
  3rd/4th quadrant's marginal value is real but modest (consistent with
  the v10.14/skip-SE finding being a real-but-moderate loss rather than a
  blowout either direction).
- **Takeaway: v10.6's existing interleaved/balanced land+animal+seed
  ordering, tuned incrementally across 20+ prior hypotheses, is a fairly
  tight local optimum — no coarser restructuring found slack it was
  leaving on the table.**

**Selling-rhythm theme (v11.14–v11.17)** — two washes, two decisive losses:
- v11.14 (big-batch selling, hold to 20+ units or 5-day cadence):
  **-$19,620/game**, t=-6.08, 9/10 losses — holding stock longer just feeds
  more force-dump firesales instead of avoiding them.
- v11.15 (stagger ongoing-crop planting start by quadrant, offset harvest
  peaks): **wash**, -$246/game, t=-0.10 — no measurable effect at the scale
  tested.
- v11.16 (sort sell order by quantity held instead of price): **wash**,
  +$334/game, t=+0.33, directionally positive but not significant.
- v11.17 (prioritize selling into active town-shop demand ahead of price):
  **-$5,999/game**, t=-4.09, 10/10 losses — undercuts the existing price/
  attack-timing logic rather than complementing it.

**Shot-in-the-dark theme (v11.18–v11.21)** — two decisive losses, two
washes, plus one notable side-finding:
- v11.18 (permanently pinned per-quadrant worker crews, no cross-quadrant
  dispatch): **-$13,960/game**, t=-3.81, 9/10 losses — confirms v8's global
  joint-nearest-pair `assign_tasks()` is itself load-bearing; losing that
  global visibility costs more than any locality benefit.
- v11.19 (inverted-siting sanity check, flip v10.5/v10.6's rule): **wash**,
  -$1,310/game, t=-0.55, 5/10 — directionally still negative (consistent
  with the original finding) but no longer statistically significant.
  **Flagged as worth a closer look outside this round's scope**: the
  original v10.5 siting effect was a clean, large, decisive win when first
  found — this round's re-check suggests the signal may have weakened
  under current codebase/opponent conditions, not that it reversed.
- v11.20 (lower EXPERIMENT_MAX_FLEET 10→6 for shed relief, not labor
  relief): **wash, leaning negative**, -$3,467/game, t=-1.26 — shed relief
  doesn't offset the lost animal revenue enough to net positive, but not
  decisive either.
- v11.21 (hard cap of 40 simultaneously-growing PLANT tiles farm-wide):
  **-$9,346/game**, t=-6.63, 10/10 losses, cleanest rejection of the four —
  a flat production cap costs far more in foregone harvest than it saves
  in shed relief.

**Overall verdict: main_v10.6_radius3.py remains champion, now undefeated
across 41 hypotheses.** This round's convergent evidence (5 independent
themes, 21 attempts, 12 decisive losses) suggests v10.6 sits at a much
broader local optimum than previously known — not just for "siting
refinements" (established in rounds 3-5) but for land/animal/hand
ordering, selling rhythm, and spatial task-dispatch structure too. The one
open thread worth a future look: v11.19's weakened-but-not-reversed
siting-sanity-check result, which may indicate the original v10.5 lever's
effect size has drifted rather than that it's still as strong as when
first measured.

## Round 8 (Aug 7): 7 mathematically-motivated COMBINED hypotheses — ALL REJECTED, v10.6 still champion

Grace's diagnosis of round 7: isolated single-lever tests couldn't tell
whether a mechanism was wrong in principle or just untested in the right
combination — e.g. quadrant-center pasture siting (v11.6) and pinned
per-quadrant crews (v11.18) each lost alone, but neither was ever paired
with the other. Asked for genuine mathematical grounding (a real cost
model for siting, a real capital-budgeting formula for quadrant timing)
and COMBINED hypotheses instead of one-variable-at-a-time tests. Delegated
3 parallel agents. **7 hypotheses, 7 rejections (5 decisive losses, 2 exact
no-ops), zero wins.** v10.6 now undefeated across 48 hypotheses total.

**Mathematical framing used:** a tile's real seasonal labor cost ≈
`visit_frequency × active_lifetime × distance` (×2 for a dedicated round
trip, ~0 marginal if folded into an existing route) — this is the
mechanism behind v10.5/v10.6's validated near-shed rule, and it implies
animals (feeding mandatory daily for their whole 20+ day placed lifetime)
should outrank even STRAWBERRY/TOMATO for the innermost near-shed tiles,
which v10.6 doesn't currently enforce. Quadrant-expansion timing should in
principle be an EV/capital-budgeting calculation — `EV = days_remaining ×
profit/tile/day × ramp-up discount − cost`, compared against the same
dollar's next-best use (animal, hand) — rather than the fixed budget/day
heuristic gates currently in place.

- **v12.1** (`main_v12.1_freq_dist_ranking.py`, unified f×lifetime ranked
  tile-claiming, animals get first claim on innermost tiles via proactive
  reservation): **LOSS**, -$8,458/game, t=-2.13, 95% CI [-16,223, -692],
  2/10 wins. The v10.6 radius sweep already showed over-reservation hurts
  (radius 6 lost to radius 4) — proactive reservation removes a "free
  land use" window ongoing crops were implicitly exploiting between a tile
  going empty and an animal purchase actually needing it.
- **v12.2** (`main_v12.2_local_tour.py`, hands pinned per-quadrant AND
  their pastures co-sited in the same quadrant — combining what v11.6 and
  v11.18 each tested alone): **decisive LOSS**, -$35,383/game, t=-9.16,
  0/10 wins. Narrower than v11.6's isolated -$76k but *worse* than v11.18's
  isolated -$14k — combining made it worse than the better of the two
  isolated pieces. Sacrificing `assign_tasks()`'s global joint-nearest-pair
  optimization (a large, constant cost across the whole game) for a real
  but comparatively small saving on animal-trip distance is structurally
  lopsided.
- **v12.3** (`main_v12.3_ev_land.py`, EV-formula-gated land purchases
  replacing the flat day/budget gates): **decisive LOSS**, -$26,936/game,
  t=-17.18, 0/10 wins. Working the arithmetic backward: at the constants
  used ($20/tile/day, 6-day ramp, 1.2x hurdle), the SE quadrant needs >24
  effective days, essentially never satisfiable — the formula silently
  reproduces the already-rejected v10.14 skip-SE experiment, and SW gets
  squeezed to day≤~7-8 vs the original day≤18. Land pays back on thinner,
  later-realized margins than a clean EV formula assumes; the existing
  heuristic's looser deadlines were closer to correct.
- **v12.4** (`main_v12.4_unified_ev.py`, cross-category EV ranking so
  land/animal/hire compete for budget by $/day score instead of fixed
  priority order): **exact WASH/no-op**, t=0.00, byte-identical action-by-
  action across all 10 seeds. The three categories essentially never
  actually contend for the same turn's budget in this codebase — each
  fires on its own largely non-overlapping gate conditions, and when they
  do coincide, budget already comfortably covers all three. The fixed-
  order assumption round 8 set out to test turns out not to be load-
  bearing in practice.
- **v12.5** (`main_v12.5_predictive_throttle.py`, forecast-based inflow
  projection throttling new purchases before shed_load actually rises,
  not reactive to current load): **exact WASH/no-op**, never triggered
  once across 10 seeds × 2 seat orientations. v10.6's own sell-priority/
  force-dump machinery already keeps shed load comfortably under the
  throttle's trigger point against this specific opponent (itself) —
  doesn't rule out the mechanism mattering against a higher-throughput
  opponent, just that self-play vs v10.6 doesn't stress-test it.
- **v12.6** (`main_v12.6_ev_land_plus_throttle.py`, v12.3's EV gate
  layered with v12.5's throttle, self-contained): **decisive LOSS**,
  -$6,922/game, t=-3.33, 1/10 wins. The EV hurdle blocks/delays land in
  the mid-late game once effective_days shrinks past ~day 15-16 —
  reintroduces the same forgone-revenue failure mode `_land_priority`'s
  scarce-land High band was already built to prevent.
- **v12.7** (`main_v12.7_local_economy.py`, per-quadrant crews +
  per-quadrant throttle, a fully decentralized mini-economy per zone):
  **decisive LOSS**, -$13,866/game, t=-3.00, 2/10 wins, the worst of the
  three shed-combo hypotheses. Fragmenting dispatch into four
  non-cooperating pools sacrifices the joint-nearest-pair optimality
  global `assign_tasks()` was specifically built to capture.

**Two convergent findings worth carrying forward:**

1. **Global `assign_tasks()` dispatch is the single most load-bearing
   piece of this whole architecture** — now confirmed 4 independent ways
   across rounds 7-8 (v11.6 isolated pasture move, v11.18 isolated crew
   pinning, v12.2 combined, v12.7 combined). Every version that
   fragmented or restricted it lost, and combining a fragmentation with a
   compensating co-location benefit (v12.2) still lost worse than the
   better of the two isolated pieces alone. Any future spatial hypothesis
   should treat "keep global dispatch intact" as close to a hard
   constraint, not a variable to test.
2. **Methodological caveat on shed-capacity hypotheses specifically:**
   both v12.4 and v12.5 came back as exact no-ops because the mechanism
   they targeted (budget contention across categories, shed overflow risk)
   never actually arises when the champion plays against itself — v10.6's
   own heuristics already handle those cases adequately in this specific
   matchup. SHED_AT_CAP is real in the broader 100-game aggregate tally
   (mixed real opponents), so this doesn't mean the mechanisms are
   worthless — it means self-play-vs-v10.6 may be the wrong test bed to
   validate them. A future shed-capacity round should consider testing
   against a higher-throughput/more aggressive opponent (e.g. a real
   ladder clone) where the shed actually fills up, rather than v10.6 vs
   v10.6-derived variants.

**Recommendation unchanged: ship main_v10.6_radius3.py.**

## Round 9 (Aug 7): market glut-resistance math — hypothesis REFUTED with a clean mechanism, v10.6 still champion

Grace asked for a from-first-principles mathematical re-derivation using the
raw game-rules table (base prices, T, shape functions, above_target).
Computed realized (not base) $/day for every product from the price-decay
curves: WHEAT and EGG are "glut-proof" (above_target=0.20, log shape —
price barely moves even at 2×T combined oversupply), while STRAWBERRY,
MELON, MILK, WOOL are "glass cannons" (above_target 1.60-3.60 — crash to
the $1 floor past just 1×T combined oversupply, and T is tiny: 100-332
units). Hypothesized that prior rounds' cow/sheep-over-goose and
strawberry/melon-heavy conclusions were measured entirely in self-play
against v10.6 — which doesn't glut the market either — so the real-opponent
glut dynamic was structurally invisible to all 48 prior hypotheses.
Dispatched 2 parallel agents, 5 hypotheses (v13.1-v13.5), tested against
BOTH v10.6 self-play AND `Opponents/opp_scenario_v14.py` (a real
high-throughput ladder clone confirmed via its own code to target a
15-animal fleet) as the actual validation test.

**All 5 hypotheses lost, and REFUTED the glut hypothesis specifically
by the mechanism the test was designed to detect:**
- v13.1 (WHEAT as an actively-planted cash crop, reintroduced after v9.1
  removed it): LOSS both ways — -$19,913/game vs v10.6 (t=-4.26), and
  **-$102,293/game vs opp_scenario_v14** — ~$6,300/game *worse* than the
  v10.6-vs-opp_v14 baseline (-$95,955), the opposite of what glut-resistance
  predicts.
- v13.2 (cut STRAWBERRY/MELON ~50%, reallocate to WHEAT/CARROT): LOSS both
  ways, ~$6,800/game worse than baseline vs opp_scenario_v14.
- v13.3 (v13.1 + larger GOOSE floor, ~40% of fleet): worst of the three,
  ~$24,900/game worse than baseline vs opp_scenario_v14 — effects
  compounded rather than offset.
- v13.4 (aggressive ~50% goose floor, ported COOP plumbing fresh onto
  v10.6): -$29,862/game vs v10.6 self-play, **-$118,447/game vs
  opp_scenario_v14** — ~$22,500/game *worse* than the no-goose baseline in
  the exact matchup meant to favor it.
- v13.5 (live reactive glut-detection, redirect to goose only when
  milk/wool price actually crashes below 30% of base): trigger **never
  fired once**, byte-identical to v10.6 in both matchups — inconclusive by
  construction, but its null result led directly to the real finding below.

**Root cause, found via direct market-inventory instrumentation (not just
theory) across 4 seeds vs opp_scenario_v14:** combined-player MILK/WOOL
market inventory stayed within roughly ±150 units of I0=10,000 for the
ENTIRE 30-day game, even against the 15-animal real opponent — nowhere
close to the ~105-122 additional units needed to meaningfully depress
price, let alone reach the $1 floor. In the sampled games, milk/wool
prices mostly **rose above base** (scarcity, not glut) as the match
progressed. Likely explanation (not separately re-verified but consistent
with the SHOPS table): milk has three demanding shops (Pizza, Ice Cream,
Smoothie) plus town center; wool has a dedicated 2x shop (Yarn Store) plus
town center — town consumption apparently keeps pace with or exceeds
realistic combined player production for these two goods specifically, so
the shared market never actually crosses into glut territory within a
single 30-day game. The I0=10,000 buffer (deliberately set "far above any
single game's realistic production volume" per the rules text) combined
with steady town off-take is enough that T=100-332 unit oversupply
thresholds are never realistically reached.

**Conclusion: the original v10.22 goose finding was correct for the right
reason.** Cow/sheep's revenue really is realized close to sticker price in
practice, even against a real high-volume opponent — not an artifact of
weak self-play testing. Goose/EGG reallocation should be considered
closed unless a much higher-throughput opponent, longer match length, or
different shop-unlock luck is found that can actually push combined
inventory past I0+T. This also refines (not reverses) the round-8
methodological caveat about self-play: it was right that self-play misses
some real dynamics, but wrong to assume market-glut was one of them for
milk/wool specifically — the town-demand floor turns out to be the more
load-bearing mechanism than the raw price-curve shape.

**Recommendation unchanged: ship main_v10.6_radius3.py.** Now undefeated
across 53 hypotheses total.

## Files

- `main_v10.6_radius3.py` — **champion**. v10.5's siting mechanism with
  `NEAR_SHED_RADIUS` tuned 4→3.
- `main_v10.5_siting.py` — prior champion, still a valid, independently
  strong version (movement-aware crop siting on unmodified v9.3).
- `main_v10.6a_radius3.py`/`main_v10.6b_radius6.py`/`main_v10.6c_radius2.py`/`main_v10.6d_radius1.py` —
  the radius-sweep variants (a/c/d statistically tied with the champion,
  b decisively worse).
- `main_v10.7_three_tier.py`, `main_v10.8_quad_scaled.py`,
  `main_v10.9_distance_hire.py`, `main_v10.10_modest_coverage.py`,
  `main_v10.11_melon_near.py`, `main_v10.12_realloc.py`,
  `main_v10.13_fert_reserve.py` — all seven round-3 hypotheses, isolated,
  with the result and reasoning recorded inline in comments.
- `main_v10.py`, `main_v10.1_carrot_boost.py`, `main_v10.2_shop_aware_selling.py`,
  `main_v10.3_fleet12.py`, `main_v10.4_tomato_scale.py` — round-1/2
  rejected hypotheses (kept deliberately, not deleted — the next session
  should not re-test any of these).
- `census_movement.py` — the movement/work/pass unit-turn census script
  used to find the v10.5 lever; reusable for future labor-efficiency
  hypotheses.
- `main_v10.21_goose.py` — GOOSE/EGG plumbing (COOP-aware perceive/
  setup/maintenance/reconcile), goose tried last-resort only. Exact
  no-op vs v10.6 (10/10 identical). Kept for the plumbing, not as a
  standalone candidate.
- `main_v10.22_goose_floor.py` — same plumbing, plus a real
  `GOOSE_FLOOR_BY_FLEET_SIZE` composition guard that forces goose
  purchases. Decisive loss (-$9,444/game, t=-2.32). REJECTED.

## Round 10 (Aug 7): full clone-replica rebuild (v_clonereplica1) — REJECTED, decisively, v10.6 still champion

Grace asked to stop tuning v10.6's own chassis and instead reconstruct the real
ladder opponent's (`Opponents/opp_scenario_v14.py`, a real public-notebook-derived
policy, not a black box) ENTIRE capital-allocation playbook as one coherent
strategy, layered onto v10.6's proven `assign_tasks()` dispatch/movement engine
(kept untouched — round 8 already confirmed 4 independent ways that fragmenting
or replacing it always loses). This differs from every prior "copy one piece of
the real opponent" attempt (v10.14/15/16/17/20, rounds 4-5), which each tested a
single trait against v10.6's own unrelated heuristic timing.

**Extracted ground truth from opp_scenario_v14.py source** (exact constants, not
inferred from replays): `LAND_OPEN_DAYS=(5,9)` (NE day5, SW day9, `MAX_EXTRA_LAND=2`
— never buys SE), staged herd target `CORE_HERD=4`/`MID_HERD=11`/`TARGET_HERD=15`
at day thresholds 7/11 (cap day 18), COW min 3/SHEEP min 1 then price-demand-
crowding-scored fill, `ANIMAL_SLOTS={"NW":4,"NE":7,"SW":4,"SE":0}`, crop mix
**MELON~10 + WHEAT + CARROT only in NW, WHEAT+CARROT filler in NE/SW — no
STRAWBERRY or TOMATO at all, no GOOSE** (matches our own v10.21/22 goose-rejection
finding), `MAX_HANDS=12`, feed stock = herd×3 days (min 8), sell-reserve fractions
per product (WHEAT 0.68, CARROT 0.55, MELON 0.58, MILK 0.42, WOOL 0.40).

**Build 1 (`main_v_clonereplica1.py`) came back confounded by a real bug**, not a
clean read: 0/10 vs v10.6 (−$42,690/game) and 0/10 vs opp_scenario_v14
(−$105,898/game, worse than v10.6's own documented baseline). Diagnosed: the
staged every-hour herd-target re-evaluation exposed a same-turn site-collision
race in the animal-placement dispatch — `taken_sites` was computed once per turn
before farmer's and every hand's `animal_setup_action()` ran, so two site-less
BOUGHT/CARRYING plans dispatched the same turn could both pick the identical
empty tile; only one pasture physically got built, `animal_reconcile()`'s
`site_occupied` check marked both plans ACTIVE off that single pasture, and the
second animal became a claimless "phantom" that got silently dumped to the shed
at end of day and permanently tripped the `unclaimed_in_shed <= 0` purchase gate
for that species — freezing the fleet at 7, even with cash idle ($68k unused by
day 27 in one seed).

**Fixed properly** (root cause, not a symptom patch): replaced the static
`taken_sites` set with a `_taken_sites()` helper recomputed fresh at each of the
three per-turn dispatch call sites, so within-turn site assignments are
immediately visible to the next call. Verified directly via hourly trace on 3
seeds: fleet now reliably reaches 15/15 by day 15-17 (vs spec's day 18), no
further freezing.

**Clean re-test, 10 seeds both-seats — REJECTED, worse than the buggy run:**
0/10 vs v10.6 (**−$68,043/game**, t=−17.38, 95% CI [−75.7k,−60.4k]); 0/10 vs
opp_scenario_v14 (**−$126,202/game**, t≈−45, both 5-seed halves individually
significant). Filling the fleet faster and fuller just ties up more capital in
a 15-animal herd + melon-heavy/no-strawberry mix earlier — v10.6's siting/
dispatch execution out-earns the ported capital-allocation policy on the same
engine regardless.

**Conclusion: the real ladder opponent's edge is NOT reproducible by porting its
land/herd/crop-mix timing onto our engine.** Whatever separates its $130-141k
from our $58-92k is not "buy land and animals in this pattern, skip strawberry" —
it's something else about how it executes at that scale (feeding/watering/
harvesting a bigger, denser operation, or genuinely different labor/movement
mechanics we don't share). This closes the "clone-replica" family of hypotheses
as decisively as the piecewise attempts before it, via a different and more
complete method — reinforces rather than reverses rounds 4-5's finding.
Bug-fix mechanism (same-turn site-collision race in shared mutable dispatch
state) may be worth flagging for future multi-hand-dispatch hypotheses generally,
independent of this round's rejected strategy.

**Recommendation unchanged: ship main_v10.6_radius3.py.** Now undefeated across
54 hypotheses total (53 prior + this round's clone-replica, tested clean after a
real bug fix).

## Round 11 (Aug 7): 4 externally-authored economy-reset variants — ALL REJECTED, v10.6/v10.5 still champion

Grace supplied 4 pre-built candidate files (`main_v11a_compact_livestock.py`,
`main_v11b_berry_factory.py`, `main_v11c_marginal_roi.py`,
`main_v11d_opponent_responsive.py`), each an "economy reset on the v10.6
execution chassis" (dispatch/movement engine kept, capital-allocation layer
replaced). Tested each vs `main_v10.5_siting.py` (as specified) and vs
`Opponents/opp_scenario_v14.py`, 10 seeds both-seats, 4 parallel agents. All
crash-free out of the box. **4/4 rejected, all decisive (t between -10.7 and
-39.4), 0/40 total wins:**

| Candidate | Hypothesis | vs v10.5 | vs opp_scenario_v14 |
|---|---|---|---|
| v11a compact livestock | 10-animal ceiling is a crop-estate ceiling, not a hard cap — shrink crops, buy feed, grow fleet bigger | **-$38,236/game**, t=-17.41, 0/10 | **-$148,374/game**, t=-20.44, 0/10 |
| v11b berry factory | Concentrate almost all crop capital into fertilized near-shed strawberry, bound the pasture fleet | **-$63,101/game**, t=-34.81, 0/10 (tightest/most decisive — stderr only 3% of mean) | **-$150,414/game**, t=-34.32, 0/10 |
| v11c marginal ROI planner | Replace fixed crop/animal targets with a live-price/runway/ROI-derived dynamic allocator | **-$16,741/game**, t=-12.98, 0/10 (smallest loss of the four, still decisive) | **-$161,313/game**, t=-39.41, 0/10 (worst of the four here) |
| v11d opponent-responsive | Allocate crop/animal capacity against live market scarcity instead of a fixed portfolio; land/hiring follow committed work not acreage | **-$43,674/game**, t=-10.74, 0/10 | **-$136,878/game**, t=-38.82, 0/10 |

**Pattern: every one is worse against the real opponent than against v10.5**,
several substantially (v11a/v11c ~4x worse), reinforcing round 10's finding
that reallocation/rebalancing hypotheses don't explain the real-opponent gap
— if anything they widen it. Mechanistically, all four fit the same graveyard
as rounds 4/5/8/9/10: v11a re-confirms the ~10-animal service ceiling isn't a
crop-estate artifact (freeing labor from crops didn't let livestock scale
further); v11b re-confirms crop-mix concentration into one premium ongoing
crop loses (matches v10.10/v10.16's conditional-only finding — unconditional
concentration here is a clean loss); v11c and v11d both replace the fixed,
execution-tuned target discipline with a dynamic/reactive allocator and both
lose decisively, consistent with v12.1-v12.7's finding (round 8) that
anything second-guessing the fixed-target dispatch loses, and round 9's
finding that the market rarely gluts in real 30-day games (so v11d's
scarcity-reactive machinery has little real signal to react to).

**Recommendation unchanged: ship main_v10.6_radius3.py.** Now undefeated
across 58 hypotheses total.
