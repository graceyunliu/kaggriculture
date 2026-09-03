# LABOR EFFICIENCY AGENT 05: animal_specialist_small_team
# Base: main_v8.3.py
# Objective: Use fewer workers but devote a larger share to high-value animal maintenance.
# Isolated policy changes: Eight-hand cap, low crop protection, animal workload counted at weight three.

import math
import random
import sys

# =====================================================================
# MAIN V8.3 -- SHEEP as pure fleet ADDITION, ISOLATED. Base: main_v8.2.py,
# byte-identical except for the animal-species-selection block below.
#
# --- Why (real-ladder diagnosis, Aug 5 evening) ---
#
# Pulled main_v8.py's real 17-game ladder record plus fresh replays from
# the current top-5 leaderboard teams. Finding: the visible top of the
# ladder (15+ distinct team names checked, all converging on one
# fingerprint) is running WOOL at ~163 units/game as part of a ~1200-
# unit-total economy, alongside MILK ~229 -- i.e. cow AND sheep together,
# not cow alone. Our v8/v8.2 lineage has always shipped SHEEP_ENABLED =
# False. See project memory (kaggriculture-real-ladder-diagnosis.md) for
# the full replay data.
#
# --- Why this isn't just flipping SHEEP_ENABLED = True ---
#
# main_v7.8.py tried exactly that (different, older code) and was
# rejected (D68 in project memory): 1/6 seeded games, mean -$11,912.
# Root cause was NOT species economics in the abstract -- COW nets
# ~$80.0/day vs SHEEP's ~$66.7/day per pasture slot, but that's a modest
# 17% gap, not enough alone to explain a $12k/game swing. The real
# mechanism was DISPLACEMENT: v7.8's species-selection picked whichever
# species passed one shared, species-agnostic feasibility gate, so every
# sheep bought was a slot the same gate would otherwise have given to a
# cow -- ~90 MILK units traded for ~58 WOOL units, a strictly-worse
# swap, with TOTAL fleet size basically unchanged (D68: 11/10, 7/11,
# 8/8, 10/9, 10/9 across 5 seeds). D67/D68 explicitly flagged the
# out: "frontier proves wool is worth $242/unit... when ADDITIVE to a
# 15-animal fleet... revisit only after fleet size moves." Fleet size
# has since moved twice (main_v8.py's global task assignment, +$10,238/
# game vs v7.11; main_v8.2.py's wheat/strawberry reweight opening up
# idle-tile capacity, +$4,482/game vs v8) -- this is that revisit.
#
# Confirming main_v8.2.py's OWN code has the identical latent bug: the
# species-selection loop in economy() iterates ANIMAL_SPECIES_ORDER =
# ["COW", "SHEEP"] and calls the SAME _animal_expansion_feasible(), which
# takes no species argument -- so COW always wins the check first
# whenever one more animal fits at all, and SHEEP is unreachable dead
# code regardless of SHEEP_ENABLED's value. Confirmed by inspection, not
# just inference: the function signature has no species parameter, so
# feasibility(COW) == feasibility(SHEEP) on every call, and COW is always
# tried first.
#
# --- The change ---
#
# 1. COW's own purchase path is left COMPLETELY untouched: same trigger,
#    same _animal_expansion_feasible() gate, same priority -- this
#    guarantees cow count is never reduced by this change. That's what
#    makes this "pure addition" rather than a re-run of v7.8's swap.
#
# 2. SHEEP gets a SEPARATE gate, _sheep_expansion_feasible(), tried only
#    once COW's own (unchanged) gate has already said no this turn.
#    Four of its five checks (survival, wheat-budget, crop-neglect,
#    crop-space) are identical and unrelaxed -- those are safety/real-
#    constraint checks, not the thing D67-D69/D71 identified as the
#    actual ceiling. Only the hand-capacity projection ceiling
#    (`HAND_TARGET_MAX`) is raised, by SHEEP_HAND_HEADROOM, specifically
#    so sheep purchases can continue past the exact point where cow's
#    own growth already plateaus for that reason -- additional capacity,
#    not a substitute for it.
#
# 3. ANIMAL_SPECIES_ORDER's for-loop (dead code per the above) is
#    replaced with this explicit two-gate sequence. SHEEP_ENABLED is
#    flipped True; the flag itself is unchanged in meaning (a kill
#    switch for the whole species).
#
# --- What could make this fail ---
#
# SHEEP_HAND_HEADROOM is a guess (4), not derived from real ladder labor
# data -- if it's too generous, sheep maintenance could crowd out crop
# work the same way animal upkeep did before v7.6a's protected-hand
# fix (a different mechanism than v7.8's displacement, but the same
# family of failure: more animals than the real hand pool can service).
# If it's too stingy, sheep may rarely or never fire and this becomes a
# null result rather than a real test. Both are informative either way.
#
# --- Test protocol ---
#   Seeded --both-seats vs main_v8.2.py, same 15-seed set used for every
#   v8.x round (1,7,42,99,123,202,303,555,2024,8080,17,2025,3001,3002,
#   3003). Mechanism check: fleet composition (COW vs SHEEP count) and
#   WOOL/MILK units sold, to confirm this is actually additive (total
#   fleet size should be >= v8.2's own, not just recomposed) rather than
#   a repeat of v7.8's swap. Smoke tests: starter/pass 720-turn, starter
#   48-turn truncated, all must stay DONE/DONE.
# =====================================================================
#
# =====================================================================
# MAIN V8.2 -- WHEAT/STRAWBERRY demand-headroom reweight, ISOLATED. Base:
# main_v8.py, byte-identical except for two `want[...]` seed-target
# constants in economy(). Per kaggriculture-v8-architecture.md section
# 5.3: the labor-fix gate that used to block this test ("only re-test
# crop reweights if a labor fix clearly wins") is moot now that BOTH
# labor-fix attempts (v7.13/v7.15 per-unit locking) failed and a THIRD,
# different-axis fix (main_v8.py's global per-turn task assignment, 15/15
# seeded win vs v7.11) has since landed and become the champion -- so
# this reweight is now tested directly on top of the better base, not
# gated on anything.
#
# --- The change (ported from main_v8_candidateB3.py, never tested) ---
#
#  want["STRAWBERRY"]: min(space,6/10) -> min(space,8/14)  (Candidate B's
#                       original bump, v7.9 base -- statistical wash
#                       there, +$5,384/11 seeds, t=1.52, not significant.
#                       Kept unchanged in B3; not itself the untested
#                       variable here.)
#  want["WHEAT"]:       8 -> min(space, 40)  (the untested half: B's
#                       min(space,25) was part of the same statistical-
#                       wash result as the STRAWBERRY bump above; B2 then
#                       tuned WHEAT DOWN to min(space,16) and lost
#                       decisively, -$30,757/11 seeds -- since
#                       want[crop]=min(space,X) is usually bound by real
#                       idle-tile count (36-50/day measured most of the
#                       match), a lower X directly means more empty tiles
#                       when space>X, i.e. pure forgone revenue against
#                       WHEAT's 635-unit town demand pool, the largest in
#                       the game. B3 tested pushing X UP to 40 instead --
#                       built, but never run to a verdict. This file is
#                       that test, on the current (not v7.9) base.
#
# MELON, TOMATO, CARROT targets and everything else in economy() /
# perceive() / dispatch are untouched -- this stays a two-constant,
# two-crop change so a result can be attributed to it cleanly, per the
# project's single-variable testing discipline (architecture doc sec 7).
#
# --- Test protocol ---
#   Seeded --both-seats vs main_v8.py, same 15-seed set used for the
#   v8-vs-v7.11 and v8.1-vs-v8 rounds (1,7,42,99,123,202,303,555,2024,
#   8080,17,2025,3001,3002,3003). Smoke tests: starter/pass 720-turn,
#   starter 48-turn truncated, all must stay DONE/DONE.
# =====================================================================
#
# =====================================================================
# MAIN V8 -- global per-turn task assignment, ISOLATED. Base: v7.11,
# byte-identical except for: (1) a new GLOBAL_TASK_ASSIGNMENT flag,
# (2) a new assign_tasks() function, (3) _agent()'s dispatch loop, which
# now defers any unit that falls through to ordinary crop-task duty
# (i.e. has no animal-setup/maintenance work this turn) into ONE batched
# call to assign_tasks() instead of calling unit_action() per unit in a
# fixed roster order. unit_action() itself is left in the file,
# untouched, and is still what runs when GLOBAL_TASK_ASSIGNMENT=False --
# that flag-off path is a required byte-for-byte behavioral no-op
# against main_v7.11.py (see test protocol below). Nothing else
# changes: economy(), the animal pipeline, task_order()/weed-priority
# escalation, and the reserved-crop-hand split are all untouched.
#
# --- The problem this targets ---
#
# Every version measured so far, including v7.11, spends 66-70% of all
# unit-turns on MOVEMENT and only 26-32% on WORK (trace_v711_movement.py
# and successors). This is the single largest identified constraint on
# production volume: the v7.11 lineage sells 731 units/match against a
# strong fixed opponent's 1,921 (D67), despite realizing BETTER prices
# on what it does sell -- a throughput problem, not a pricing problem.
# SHED_AT_CAP is also the dominant tag on real ladder losses (31/41,
# Aug 5 sync) -- consistent with the same root cause seen from the
# other side: uneven per-turn labor allocation produces harvest in
# bursts that can outrun the existing overflow-relief selling logic even
# while average production trails the opponent tier. Full writeup:
# kaggriculture-v8-architecture.md, section 3.
#
# --- What's already been tried and rejected (do not re-derive) ---
#
# Two rebuilds already targeted this exact ratio by giving individual
# units MEMORY of what they were walking toward, so a fresh per-turn
# perception rebuild wouldn't retarget them mid-walk:
#   - main_v7.13.py (unconditional per-unit target locking): retarget
#     rate dropped 32.2%->12.9% as designed, but LOST 5/20 vs v7.11,
#     -$13,492/game, t=-3.42 -- locking kills priority-preemption, so a
#     freshly-urgent task can't pull in a unit already committed to
#     something lower-priority.
#   - main_v7.15.py (priority-preemptible locking): urgent-task response
#     time genuinely improved, but LOST WORSE, 0/20 vs v7.11, -$19,571/
#     game, t=-11.28 -- the preemption check was global-existence, not
#     nearest-unit: every locked unit below a newly-urgent task
#     independently abandoned its walk, but only the first-processed
#     unit actually claimed it, so the "fix" produced MORE idle time
#     (pass-rate 3.6%->7.9%) than the churn it targeted.
#
# Both failures are about CROSS-TURN persistence, and this build
# deliberately does NOT reintroduce that idea -- tasks (the per-turn
# urgent_water/harvest/water/weeds/plant lists) are still fully rebuilt
# from live perception every single turn here, exactly as in v7.11; no
# unit remembers what it was walking toward last turn.
#
# --- What this build actually changes ---
#
# A different, previously-untested axis: whether a SINGLE turn's
# already-existing task pool is divided up well among that turn's
# already-idle units. main_v7.11.py's unit_action() processes units one
# at a time in a fixed roster order (farmer, then hand0, hand1, ...);
# each unit independently claims its OWN nearest available task and
# removes it from the shared pool before the next unit in line even
# looks. This is sequential greedy, and processing order can force a
# later unit into a materially worse match than a jointly-optimal
# pairing would -- e.g. two units near two different tasks can fail to
# cross-match if the first-processed unit happens to grab whichever
# target is nearer to IT specifically, even when swapping would shorten
# both units' total walk.
#
# assign_tasks() replaces that with one joint nearest-pair matching per
# task tier, computed across ALL of that tier's currently-unassigned
# units and currently-available tiles at once: build every candidate
# (unit, tile) pair, sort by ascending Manhattan distance, and confirm
# pairs greedily in that order (skipping either side once claimed).
# Units already standing exactly on a pending task tile still claim it
# for free before any walking is considered, in tier-priority order --
# matching unit_action()'s original "standing beats walking regardless
# of tier rank" behavior exactly. task_order()'s existing tier priority
# (urgent_water > harvest > water > plant/weeds, weed-count-escalated)
# is unchanged; this only changes HOW targets within a tier are divided
# up among units, not the priority ordering itself.
#
# --- What could make this fail ---
#
# This is architecturally different from v7.13/v7.15, but it is still
# the third attempt at this specific ratio on this project, and the
# first two were decisive, not close losses. Possible failure modes:
# the per-turn optimality gain may simply be too small to matter (hands
# already cluster near the shed most of the day, limiting how much
# cross-matching can help); or tier-by-tier consumption of unassigned
# units could itself leave a later tier's matching worse if an earlier
# tier "used up" a unit that would have been a much better match one
# tier down (not modeled here -- tiers are still matched independently,
# highest-priority first, same as v7.11). Budget for a rejection on the
# same tier as v7.13/v7.15's; this is included because it targets a
# genuinely different mechanism, not because it's expected to obviously
# win.
#
# --- Deliberately NOT included in this build ---
#
# The Phase-1 state/decision-log foundation (build_state(),
# analyze_opponent(), DecisionLog) from the prior main_v8.py is not
# folded in here. That foundation's fork point (main_v7.6.py) is stale
# and needs its own rebase onto v7.11 -- kept as a separate, later step
# (kaggriculture-v8-architecture.md section 6.1/8) specifically so it
# doesn't confound this result. The previous main_v8.py (Phase 1
# foundation) is preserved as main_v8_phase1_foundation.py rather than
# overwritten.
#
# --- Test protocol ---
#
#   1. No-op check (REQUIRED FIRST): with GLOBAL_TASK_ASSIGNMENT=False,
#      this file must reproduce main_v7.11.py exactly --
#      `seeded_h2h.py main_v8.py main_v7.11.py --seeds ... --both-seats`
#      must return exactly 0.0 on every seed.
#   2. Real test: GLOBAL_TASK_ASSIGNMENT=True vs main_v7.11.py,
#      --both-seats, >=8 seeds, plus a mechanism check (movement/work
#      ratio) -- per kaggriculture-v8-architecture.md section 7, money
#      and mechanism are separate questions and both need answering.
#   3. Smoke tests vs starter/pass, 720 and 48 turns, zero crashes.
# =====================================================================
#
# =====================================================================
# MAIN V7.11 -- cost-of-delay order sort, ISOLATED. Base: v7.9,
# byte-identical except for the market-order assembly at the end of
# economy(). Nothing else is touched: no selling-quantity change, no
# animal change, no labor change, no crop-mix change.
#
# --- The bug it replaces ---
#
# v7.9 (inherited from v7.2) assembled the turn's market orders by
# concatenating fixed buckets -- (strategic, feed, sell) first, then
# (hire, seed) -- and truncating at MAX_MARKET_ORDERS=10. Whichever
# bucket happened to fill slots 1-10 first won; whatever landed at
# index 10+ was dropped regardless of what it actually was. The one
# exception, "if hire/seed overflow, steal the last SELL slot instead
# of just dropping the order", was a single hand-patched special case
# for one specific collision (hire/seed vs. sell) that left every other
# possible collision (e.g. a routine good-price sell crowding out an
# animal about to miss its second unfed day) unhandled.
#
# --- The fix ---
#
# Every order gets a priority score at the point it's built, reflecting
# what NOT placing it today actually costs (cost of delay), not how
# large its payoff is. All orders go into one list; at the end the list
# is sorted by score descending and truncated to MAX_MARKET_ORDERS. Slot
# contention now always drops the least valuable order in the whole
# turn, not whichever bucket lost the race for index 10.
#
# Priority bands (highest to lowest cost of delay if skipped today):
#   ENORMOUS  feed wheat, an animal already missed a feeding day --
#             the next miss is an escape ($400-500 gone + all future
#             yield from that animal).
#   HIGH      sell that relieves shed-at-capacity overflow (incoming
#             harvest would otherwise be blocked/firesold); sell in the
#             final turns (unsold stock scores nothing); sell during a
#             demand-timing attack window (this match's price spike for
#             that item, gone if delayed); hire (a hire not placed
#             today is a hand-day gone -- hands wipe nightly).
#   MEDIUM,   seed purchase as its crop's planting cutoff approaches --
#   rising    past cutoff it can never mature, so the same order's
#             value rises turn over turn as the deadline nears.
#   MEDIUM    buy animal (one day of yield foregone, ~$80 for a cow) /
#             routine feed-wheat restock (no animal at risk yet).
#   NEAR ZERO ordinary paced sell at a decent price while the shed has
#             room -- goods keep, the only cost is however the price
#             drifts before the next opportunity.
#   ZERO      buy land while empty tiles sit idle -- more land we can't
#             work yet buys nothing.
#
# See kaggriculture-agent-design.md / project memory for the review
# note ("Sort — build the market list by value...") this implements.
# =====================================================================
#
# =====================================================================
# MAIN V7.9 -- strawberry scale-up, ISOLATED. Base: v7.6, byte-identical
# except for the two crop-mix constants noted below. Nothing else is
# touched: no selling change, no animal change, no labor change.
#
# --- Why (demand-side analysis, Aug 5) ---
#
# Market inventory is shared, persistent, starts at I0=10000, and the
# TOWN drains it faster than either player supplies. In all 5 real v7.5
# ladder loss replays final inventory ends BELOW I0 for nearly every
# product, so prices INFLATE over the match: final STRAWBERRY $243-309
# (base 120), WOOL $244-252 (200), MILK $193-249 (160), WHEAT $54-60
# (25). Only MELON and FERTILIZER end oversupplied. This game is
# supply-constrained, not price-constrained.
#
# Simulating the real shop-unlock schedule (`SHOPS` +
# TOWN_CENTER_DEMAND_SCHEDULE, 8 shops one per 3 days) gives the units
# the town absorbs per match before price falls below base:
#
#   WHEAT 635 | STRAWBERRY 534 | MILK 440 | CARROT 431 | EGG 341
#   WOOL 336  | TOMATO 335     | MELON 140 | FERTILIZER 0
#
# MELON is in NO shop (town-center drain only). We give it
# PLANT_PRIORITY[0] -- first pick of every tile -- i.e. the smallest
# demand pool in the game gets our best land.
#
# Measured per-game revenue across those 5 loss replays:
#   STRAWBERRY: us $2,517 (12 units) vs opponents $28,578 (116 units),
#               both realizing $217-246/unit.  Gap ~$26k/game.
#
# --- The bug ---
#
# v7.6 line ~368: want["STRAWBERRY"] = 3, commented "ongoing crop, small
# standing patch is enough". The premise is wrong. Read the engine:
# a strawberry plant produces exactly max_yield=4 times (interval 2, on
# days 10/12/14/16 of its life), then `_daily_refresh_plants` sets
# max_lifespan_step and it dies. It is NOT perpetual. 3 seeds in stock
# x 4 units = ~12 units/game, exactly what the replays show.
#
# Compounding it: `plantable_crops()` returns PLANT_PRIORITY order and
# the planting task always takes the FIRST entry, so strawberry only
# ever reaches a tile after melon stock hits zero. Raising the seed
# target alone would just stockpile seeds.
#
# --- The change (exactly two constants) ---
#
#  1. PLANT_PRIORITY: STRAWBERRY moved ahead of MELON.
#  2. want["STRAWBERRY"]: 3 -> min(space, 6 if early else 10), the same
#     shape melon already uses.
#
# MELON's own target is deliberately NOT reduced -- melon still gets
# every tile strawberry doesn't claim. That keeps this a strawberry
# change rather than a confounded strawberry-up/melon-down swap.
#
# --- What could make this fail ---
#
# Per tile-day at OBSERVED average prices melon is competitive
# (strawberry 4 units/16 days x $246 = ~$62/tile-day; melon 6 units/13
# days x $166 = ~$76/tile-day). The bet is on the MARGINAL unit, not the
# average: melon's `af` curve is "sq" against a 140-unit pool and our
# melon market already ends oversupplied, so our marginal melon is worth
# far less than $166 -- while our marginal strawberry is still worth
# ~$250 because we sell 12 into a 534-unit pool. If that reasoning is
# wrong the A/B will say so.
#
# --- Inherited from v7.6 (unchanged) ---
# MAIN V7.6 -- ships Variant A ("protected crop hands") after A/B testing
# against Variant B (hiring-formula-only, main_v7.6b.py) -- see decision
# log / project memory. Variant A won 7/8 seeded games vs v7.5 (mean
# margin +$6,081); Variant B lost to v7.5, 3/8 (mean margin -$2,667).
#
# Base: v7.5, unchanged except for labor allocation. Real ladder loss
# replays (5/5, episodes 90064167/90066909/90068269/90070304/90070988)
# showed a reproducible late-game collapse: seed inventory freezes
# ~day 10-15 through day 29, WEED tiles climb from single digits to
# 20-37/100, planted-crop tiles collapse from a mid-game peak of 33-45
# down to 0-8, while WATER actions fall from ~20-38/day to near zero
# and FEED+CARE actions climb from ~2/day to 9-11/day over the same
# window. Root cause confirmed by reading the code: `animal_maintenance
# _action` has unconditional first claim on every hand and the farmer,
# every turn (v7.5's `_agent` loop), regardless of whether crops are
# already neglected -- so as the fleet's maintenance burden grows, crop
# watering/weeding/planting gets crowded out and never recovers. Two
# more contributing bugs, also fixed here: (1) weeds were last in
# TASK_ORDER and excluded entirely for day > 27; (2) hiring's own
# workload formula and the animal-expansion neglect gate both ignore
# weeds, so a heavily-weeded farm doesn't hire more or block further
# animal purchases because of it (see v7.6b for that fix in isolation).
#
# v7.6a's fix: reserve a protected fraction of hands for crop work only.
# Reserved hands may still respond to feed-critical animal needs
# (an animal already missed a feeding, or is due today) since animal
# survival should still preempt crops -- but they never do the
# *optional* animal work (CARE, HARVEST, COLLECT_FERTILIZER, product
# deposit) that was crowding out watering/weeding in the replays. The
# farmer and any hands beyond the reserved count keep v7.5's original
# unconditional-maintenance-first behavior. Weed removal is also
# promoted ahead of ordinary watering (and, once severe, ahead of
# planting) once weed count crosses a threshold, and the day<=27 cutoff
# on weed-clearing is removed.
#
# Full version history, replay evidence, and decision rationale for this
# and every prior version: see kaggriculture-agent-design.md and
# kaggriculture-v7.3-plan.md in the project folder.
# =====================================================================

PRICE_FLOOR = 1
I0 = 10_000
SHED_CAP = 100
LIQUIDATE_DAY = 28
MAX_MARKET_ORDERS = 10

BOARD = 10
CENTER_TILES = [(4, 4), (4, 5), (5, 4), (5, 5)]

# Animal fleet config (verified against engine's ANIMALS dict: COW cost=400,
# SHEEP cost=500; both use structure="PASTURE", so no separate site-type
# bookkeeping is needed for either species).
ANIMAL_SPECS = {
    # COW starts day 0 (claims cash before ordinary day-1/2 spend erodes
    # it); SHEEP stays day 3.
    "COW":   {"cost": 400, "min_money": 700, "start_day": 0,  "last_day": 22},
    "SHEEP": {"cost": 500, "min_money": 800, "start_day": 3,  "last_day": 22},
}
# v8.3: COW keeps its own unchanged gate (_animal_expansion_feasible);
# SHEEP now gets a separate, ADDITIONAL gate (_sheep_expansion_feasible)
# tried only after COW's own gate says no this turn -- see file header.
# ANIMAL_SPECIES_ORDER's old species-agnostic-feasibility loop is gone;
# it was dead code (SHEEP could never win a shared feasibility check that
# COW was always tried against first).
SHEEP_ENABLED = True
SHEEP_HAND_HEADROOM = 4   # extra hand-target ceiling allowed specifically
                           # for sheep purchases once cow's own (unchanged)
                           # growth has plateaued under HAND_TARGET_MAX.

# v8: master flag for this file's one functional change. False reproduces
# main_v7.11.py's unit_action() dispatch exactly (required no-op check);
# True routes crop-duty units through assign_tasks() instead. See file
# header for full rationale.
GLOBAL_TASK_ASSIGNMENT = True

# Dynamic fleet expansion: no fixed animal-count cap. Each next purchase is
# gated live by _animal_expansion_feasible() (survival/wheat/hands/crop-space
# checks) instead of a hardcoded target.
EXPANSION_WHEAT_BUDGET_FRAC = 0.15   # next animal's feed shortfall can't cost
                                      # more than this fraction of current cash
EXPANSION_MIN_CROP_TILES_PER_QUAD = 8   # crop-land reserve, scales with
                                          # unlocked quadrants

# A flat animal-count cap was tried and rejected -- it helped one opponent
# and hurt another by roughly the same amount, so no single number
# generalizes (see design doc). CROP_NEGLECT_TASKS_PER_HAND instead checks
# real current hand count against real current crop backlog -- a direct
# symptom check, not a forecast.
CROP_NEGLECT_TASKS_PER_HAND = 5      # matches hiring formula's work/5 scaling
ANIMAL_WORK_WEIGHT = 3               # pasture visit weight vs. one crop tile
                                       # (a round trip costs more hand-turns)

SETUP_STAGE_TIMEOUT = 12
SETUP_MAX_RETRIES = 3
FEED_CARRY_TARGET = 2
PRODUCT_DEPOSIT_AT = 3         # PLACE milk/wool when carrying this many

# Real hiring cost model (kaggriculture.py: FARM_HAND_COST_MULT=1, fib(0)=1,1,2,3,5,...)
FARM_HAND_COST_MULT = 1
HAND_TARGET_MIN = 3
HAND_TARGET_MAX = 8

# Market-order category slot reservations
MAX_HIRE_SLOTS = 8
MAX_SEED_SLOTS = 5   # fits MELON/STRAWBERRY/TOMATO/WHEAT/CARROT

# --- v7.6a: protected crop-hand reservation ---
# Fraction of the current hand count that is walled off for crop-only work
# (watering/weeding/harvest/planting), scaled up once the farm is showing
# real symptoms of neglect rather than always being a flat number.
WEED_RATIO_HIGH = 0.10          # weeds / unlocked-tile-count threshold
CROP_PRESSURE_HAND_MULT = 4     # crop backlog vs. hand count threshold
PROTECTED_FRACTION_LOW = 0.30
PROTECTED_FRACTION_HIGH = 0.45
MIN_RESERVED_CROP_HANDS = 2
TILES_PER_QUAD = 25              # 10x10 board / 4 quadrants

# Weed-priority escalation thresholds (tune TASK_ORDER as infestation grows).
WEED_PRIORITY_THRESHOLD = 5     # promote weeds ahead of ordinary planting
WEED_URGENT_THRESHOLD = 20      # promote weeds ahead of ordinary watering too

CROPS = {
    "WHEAT":      {"seed": 10,  "first": 2,  "max_day": 4,  "interval": 0, "max_yield": 6, "ongoing": False},
    "CARROT":     {"seed": 20,  "first": 2,  "max_day": 3,  "interval": 0, "max_yield": 4, "ongoing": False},
    "TOMATO":     {"seed": 50,  "first": 8,  "max_day": 8,  "interval": 1, "max_yield": 4, "ongoing": True},
    "STRAWBERRY": {"seed": 100, "first": 10, "max_day": 10, "interval": 2, "max_yield": 4, "ongoing": True},
    "MELON":      {"seed": 80,  "first": 10, "max_day": 12, "interval": 0, "max_yield": 6, "ongoing": False},
}

MARKET_PARAMS = {
    "WHEAT":      {"base": 25,  "T": 400, "bf": "sqrt",   "bt": 0.80, "af": "log",    "at": 0.20},
    "CARROT":     {"base": 35,  "T": 450, "bf": "log",    "bt": 0.20, "af": "sqrt",   "at": 0.70},
    "TOMATO":     {"base": 60,  "T": 200, "bf": "linear", "bt": 0.40, "af": "sqrt",   "at": 0.60},
    "STRAWBERRY": {"base": 120, "T": 100, "bf": "sqrt",   "bt": 0.70, "af": "linear", "at": 1.60},
    "MELON":      {"base": 250, "T": 300, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.60},
    "EGG":        {"base": 50,  "T": 332, "bf": "linear", "bt": 0.40, "af": "log",    "at": 0.20},
    "MILK":       {"base": 160, "T": 122, "bf": "sqrt",   "bt": 0.60, "af": "linear", "at": 1.60},
    "WOOL":       {"base": 200, "T": 105, "bf": "log",    "bt": 0.20, "af": "sq",     "at": 3.20},
    "FERTILIZER": {"base": 100, "T": 200, "bf": "linear", "bt": 0.40, "af": "linear", "at": 0.40},
}

CUTOFF = {"WHEAT": 25, "CARROT": 26, "MELON": 16, "STRAWBERRY": 18, "TOMATO": 20}
# v7.9 change 1 of 2: STRAWBERRY ahead of MELON. plantable_crops() returns
# this order and the plant task always takes the first entry, so whatever
# sits at index 0 gets first claim on every empty tile. MELON has a
# 140-unit/match town demand pool (it is in no shop); STRAWBERRY has 534.
PLANT_PRIORITY = ["STRAWBERRY", "MELON", "TOMATO", "WHEAT", "CARROT"]
PREMIUM_CROPS = {"STRAWBERRY", "MELON"}
ANIMAL_PRODUCTS = ("MILK", "WOOL", "EGG", "FERTILIZER")


def _shape(func, x):
    x = max(0.0, x)
    if func == "linear": return x
    if func == "sq":     return x * x
    if func == "sqrt":   return math.sqrt(x)
    if func == "log":    return math.log(1.0 + x)
    if func == "log10":  return math.log10(1.0 + x)
    return x


def market_price(item, inventory):
    if item not in MARKET_PARAMS:
        return PRICE_FLOOR
    p = MARKET_PARAMS[item]
    base, T = p["base"], p["T"]
    if inventory < I0:
        amp = p["bt"] * base / _shape(p["bf"], T)
        price = base + amp * _shape(p["bf"], I0 - inventory)
    else:
        amp = p["at"] * base / _shape(p["af"], T)
        price = base - amp * _shape(p["af"], inventory - I0)
    return max(PRICE_FLOOR, int(round(price)))


def units_sellable_above(item, inventory, min_price, cap):
    n = 0
    while n < cap and market_price(item, inventory + n) >= min_price:
        n += 1
    return n


def _fib(n):
    """Matches engine's _fib: fib(0)=1, fib(1)=1, fib(2)=2, fib(3)=3, fib(4)=5, ..."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


class DemandTimingEngine:
    def __init__(self, match_seed=42):
        self.rng = random.Random(match_seed)
        self.d10_target_turn = 9 * 24 + self.rng.randint(-2, 2)
        self.d20_target_turn = 19 * 24 + self.rng.randint(-2, 2)
        self.dump_ratio = self.rng.uniform(0.65, 0.85)

    def is_holding_phase(self, day, hour):
        t = day * 24 + hour
        return (7 * 24 <= t < self.d10_target_turn) or (17 * 24 <= t < self.d20_target_turn)

    def is_attack_turn(self, day, hour):
        t = day * 24 + hour
        return t in (self.d10_target_turn, self.d20_target_turn)


# =====================================================================
# PERCEPTION
# =====================================================================

def perceive(me, opp, day):
    urgent_water, water, harvest, empty, weeds = [], [], [], [], []
    my_pastures = []          # (pos, tile) for pastures WITH an animal
    empty_pastures = []

    for y, row in enumerate(me["tiles"]):
        for x, t in enumerate(row):
            if t is None:
                empty.append((x, y))
                continue
            if not isinstance(t, dict):
                continue
            kind = t.get("kind")
            if kind == "WEED":
                weeds.append((x, y))
            elif kind == "PASTURE":
                if t.get("animal"):
                    my_pastures.append(((x, y), t))
                else:
                    empty_pastures.append((x, y))
            elif kind == "PLANT":
                if not t.get("watered_today", False):
                    if t.get("consecutive_unwatered", 0) >= 1:
                        urgent_water.append((x, y))
                    else:
                        water.append((x, y))
                c = CROPS.get(t.get("crop"))
                if c:
                    age = day - t.get("planted_day", day)
                    yu = t.get("yield_units", 0)
                    ready = c["ongoing"] or (age >= c["first"] and
                            (yu >= c["max_yield"] or age >= c["max_day"]))
                    if yu > 0 and ready:
                        harvest.append((x, y))

    imminent = {}
    for row in opp["tiles"]:
        for t in row:
            if isinstance(t, dict) and t.get("kind") == "PLANT":
                c = CROPS.get(t.get("crop"))
                if c:
                    age = day - t.get("planted_day", day)
                    if c["first"] - 2 <= age <= c["max_day"]:
                        imminent[t["crop"]] = imminent.get(t["crop"], 0) + 1

    return {
        "urgent_water": urgent_water, "water": water, "harvest": harvest,
        "empty": empty, "weeds": weeds,
        "my_pastures": my_pastures, "empty_pastures": empty_pastures,
        "opp_imminent": imminent,
    }


# =====================================================================
# ECONOMY
# =====================================================================

def phase(day):
    return 0 if day < 10 else (1 if day < 20 else 2)


def plantable_crops(seeds, day):
    return [c for c in PLANT_PRIORITY if seeds.get(c, 0) > 0 and day <= CUTOFF.get(c, -1)]


def live_price(obs, item):
    prices = obs.get("market", {}).get("prices") or {}
    if item in prices:
        return prices[item]
    return market_price(item, obs.get("market", {}).get("inventory", {}).get(item, I0))


def _pending_animal_work(view):
    """Count of pastures with an actual pending need this turn (unfed, ready
    to harvest, needs care, or has fertilizer waiting)."""
    return sum(1 for _pos, t in view["my_pastures"]
               if (not t.get("fed_today", True)) or t.get("yield_units", 0) > 0
                  or (not t.get("cared_today", True)) or t.get("fertilizer_available", False))


def _animal_expansion_feasible(obs, view, budget, shed, n_animals, n_hands, quads):
    """Gate for buying the (n_animals+1)th animal. All five must hold:
      1. Survival: no existing pasture is already missing a feeding.
      2. Wheat affordability: the market-buy needed to cover one more
         animal's feed shortfall, after home-grown wheat, must stay small
         relative to current cash.
      3. Hand capacity (formula): a projected hiring target, covering crops
         plus animal workload, must stay under HAND_TARGET_MAX.
      4. Crops not already neglected (real, not projected): do the hands we
         actually have right now already have their hands full with crop
         backlog alone?
      5. Crop space: reserving one more near-shed tile for a pasture must
         still leave enough open land for crops.
    """
    if any(not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
           for _pos, t in view["my_pastures"]):
        return False

    next_target_wheat = (n_animals + 1) * 2 + FEED_CARRY_TARGET
    have = shed.get("WHEAT", 0)
    shortfall = max(0, next_target_wheat - have)
    shortfall_cost = shortfall * live_price(obs, "WHEAT")
    if shortfall_cost > EXPANSION_WHEAT_BUDGET_FRAC * max(budget, 1):
        return False

    animal_work = _pending_animal_work(view)
    neglect_work = len(view["water"]) + len(view["urgent_water"]) + len(view["harvest"])
    crop_work = neglect_work + len(view["empty"])
    projected_work = crop_work + (animal_work + 1) * ANIMAL_WORK_WEIGHT
    if math.ceil(projected_work / 5) > HAND_TARGET_MAX:
        return False

    if neglect_work > n_hands * CROP_NEGLECT_TASKS_PER_HAND:
        return False

    available_for_crops = len(view["empty"]) - len(reserved_sites) - 1
    if available_for_crops < EXPANSION_MIN_CROP_TILES_PER_QUAD * quads:
        return False

    return True


def _sheep_expansion_feasible(obs, view, budget, shed, n_animals, n_hands, quads):
    """v8.3: SHEEP's own gate, tried only after _animal_expansion_feasible()
    (COW's unchanged gate) has already returned False this turn. Checks
    1 (survival), 2 (wheat budget), 4 (crop neglect), 5 (crop space) are
    identical to COW's -- those are real/safety constraints, not the
    thing this build targets. Only check 3 (hand-capacity projection) is
    relaxed, by SHEEP_HAND_HEADROOM, so sheep purchases can add fleet
    capacity past the exact ceiling that already stopped cow growth,
    instead of competing for cow's own slot (that competition is what
    made main_v7.8.py's SHEEP_ENABLED=True a straight cow-for-sheep swap
    -- see file header, D68 in project memory)."""
    if any(not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
           for _pos, t in view["my_pastures"]):
        return False

    next_target_wheat = (n_animals + 1) * 2 + FEED_CARRY_TARGET
    have = shed.get("WHEAT", 0)
    shortfall = max(0, next_target_wheat - have)
    shortfall_cost = shortfall * live_price(obs, "WHEAT")
    if shortfall_cost > EXPANSION_WHEAT_BUDGET_FRAC * max(budget, 1):
        return False

    animal_work = _pending_animal_work(view)
    neglect_work = len(view["water"]) + len(view["urgent_water"]) + len(view["harvest"])
    crop_work = neglect_work + len(view["empty"])
    projected_work = crop_work + (animal_work + 1) * ANIMAL_WORK_WEIGHT
    if math.ceil(projected_work / 5) > HAND_TARGET_MAX + SHEEP_HAND_HEADROOM:
        return False

    if neglect_work > n_hands * CROP_NEGLECT_TASKS_PER_HAND:
        return False

    available_for_crops = len(view["empty"]) - len(reserved_sites) - 1
    if available_for_crops < EXPANSION_MIN_CROP_TILES_PER_QUAD * quads:
        return False

    return True


def _grow_reserved_sites(view):
    """Claim exactly one more near-shed tile for the fleet, called only when
    a new animal purchase actually fires. Picks the nearest still-unclaimed
    empty tile to the shed."""
    candidates = [t for t in view["empty"]
                  if t not in CENTER_TILES and t not in reserved_sites]
    if not candidates:
        return
    candidates.sort(key=lambda t: _dist(t, _nearest_center(t)))
    reserved_sites.append(candidates[0])


# --- v7.11: cost-of-delay order priority scores ---
# See the header comment for the full table this implements. Bands are
# numeric ranges, not single points, so orders within a band can still
# be ranked against each other by magnitude/urgency.
PRIORITY_ENORMOUS         = 1000   # animal about to escape
PRIORITY_HIGH             = 700    # floor of the High band
PRIORITY_HIGH_CAPACITY    = 760    # sell that relieves shed overflow
PRIORITY_HIGH_FINAL       = 730    # sell in the final turns
PRIORITY_HIGH_ATTACK      = 715    # sell during a demand-timing attack
PRIORITY_HIGH_HIRE        = 700    # hire (lowest of the High rows)
PRIORITY_MEDIUM_RISING_LO = 400    # seed buy, far from its cutoff
PRIORITY_MEDIUM_RISING_HI = 690    # seed buy, right at its cutoff --
                                     # stays under the High floor
PRIORITY_MEDIUM           = 320    # buy animal
PRIORITY_FEED_ROUTINE     = 340    # feed wheat, no animal at risk yet
PRIORITY_NEAR_ZERO        = 80     # good-price sell, shed has room
PRIORITY_LAND_IDLE        = 15     # buy land while tiles sit idle
PRIORITY_LAND_SCARCE      = 320    # buy land when tiles are actually
                                     # the binding constraint

LAND_IDLE_TILE_THRESHOLD = 15   # empty tiles at/above this = land isn't
                                  # the bottleneck; below it, it might be


def _land_priority(view):
    """Cost of delaying a land purchase. High only when empty tiles are
    actually scarce -- with ~40 idle tiles (the common case here, see
    project memory's demand-side analysis) more land buys nothing."""
    idle = len(view["empty"])
    return PRIORITY_LAND_SCARCE if idle < LAND_IDLE_TILE_THRESHOLD else PRIORITY_LAND_IDLE


def _seed_priority(crop, day):
    """Cost of delaying a seed purchase: zero urgency right after the
    window opens, rising toward (but never reaching) the High band as
    the crop's planting cutoff approaches -- past cutoff it can't
    mature at all."""
    cutoff = CUTOFF.get(crop, day)
    span = max(1, cutoff)
    days_left = max(0, cutoff - day)
    urgency = 1.0 - min(1.0, days_left / span)
    return PRIORITY_MEDIUM_RISING_LO + urgency * (PRIORITY_MEDIUM_RISING_HI - PRIORITY_MEDIUM_RISING_LO)


def _feed_priority(view):
    """Cost of delaying a feed-wheat purchase. Enormous the moment any
    pasture has already missed a feeding today -- the next miss is an
    escape ($400-500 gone plus every future yield from that animal).
    Same trigger _animal_expansion_feasible already uses to halt fleet
    growth."""
    if any(not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
           for _pos, t in view["my_pastures"]):
        return PRIORITY_ENORMOUS
    return PRIORITY_FEED_ROUTINE


def _sell_priority(reason, shed_load):
    """Cost of delaying a sell order. The three trigger conditions
    (capacity relief, final turns, attack window) are High -- each one
    means the alternative is a blocked/firesold harvest, unsold stock
    scoring nothing, or missing this match's price spike for that item.
    Everything else is an ordinary paced sell: goods keep in the shed,
    so the only real cost of delay is shed pressure -- score rises
    toward (but stays under) the Medium-rising band as the shed fills
    toward its force-dump trigger, instead of sitting flat at near-zero
    regardless of how full the shed actually is."""
    if reason == "capacity":
        return PRIORITY_HIGH_CAPACITY
    if reason == "final":
        return PRIORITY_HIGH_FINAL
    if reason == "attack":
        return PRIORITY_HIGH_ATTACK
    room = max(0, SHED_CAP - shed_load)
    fullness = 1.0 - min(1.0, room / SHED_CAP)
    return PRIORITY_NEAR_ZERO + fullness * (PRIORITY_MEDIUM_RISING_LO - PRIORITY_NEAR_ZERO)


def economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans):
    budget = me["money"]
    shed = obs["private"]["shed"]
    inv = obs["market"]["inventory"]
    behind = me["money"] < opp["money"] - 500
    quads = len(me["unlocked_quadrants"])
    # Needed early now that land/seeds run before animal purchase.
    shed_load = sum(n for n in shed.values() if isinstance(n, (int, float)) and n > 0)

    # v7.11: one scored list replaces the old strategic/feed/sell/hire/seed
    # buckets. Every append is (priority_score, order); the final assembly
    # sorts descending and truncates -- see header comment + priority
    # helpers above.
    priced_orders = []
    seed_orders_n = 0   # still tracked for MAX_SEED_SLOTS, no bucket needed

    # --- Land expansion ---
    if 1 <= day <= 22:
        land_score = _land_priority(view)
        if quads == 1 and budget > 1000:
            priced_orders.append((land_score, ["BUY_LAND"])); budget -= 1000
        elif quads == 2 and budget > 2000 and day <= 18:
            priced_orders.append((land_score, ["BUY_LAND"])); budget -= 2000
        elif quads == 3 and budget > 4000 and day <= 16:
            priced_orders.append((land_score, ["BUY_LAND"])); budget -= 4000

    # --- Seed pipeline ---
    ph = phase(day)
    space = len(view["empty"]) + 2
    want = {}
    if day <= CUTOFF["MELON"] and budget > 700:
        melon_target = min(space, 6 if ph == 0 else 10)
        # Throttle new MELON seeds once shed is nearly full, to reduce
        # future force-dump firesales.
        if shed_load > SHED_CAP - 30:
            melon_target = min(melon_target, 3)
        want["MELON"] = melon_target
    if day <= CUTOFF["STRAWBERRY"] and budget > 900:
        # v8.2 (Candidate B/B3): raised further from v8's 6/10 -- still
        # well under the 534-unit town demand pool headroom.
        want["STRAWBERRY"] = min(space, 8 if ph == 0 else 14)
    if day <= CUTOFF["TOMATO"] and budget > 600:
        want["TOMATO"] = 3   # ongoing crop, same small-standing-patch approach
    if day <= CUTOFF["CARROT"]:
        want["CARROT"] = 4
    if day <= CUTOFF["WHEAT"]:
        # v8.2 (Candidate B3): v8's flat 8 was tiny against a 635-unit
        # pool (the largest in the game) and WHEAT is last in
        # PLANT_PRIORITY, so this only fills tiles the premium crops
        # don't claim first -- targets the 36-50/100 idle tiles measured
        # sitting empty most days. B2's lower min(space,16) lost
        # decisively (-$30,757/11 seeds); this tests the untested
        # higher-X direction instead.
        want["WHEAT"] = min(space, 40)

    reserve = 500 if ph == 0 else 200
    for crop, tgt in want.items():
        if seed_orders_n >= MAX_SEED_SLOTS:
            break
        have = seeds.get(crop, 0)
        if have < tgt:
            k = tgt - have
            cost = CROPS[crop]["seed"] * k
            if budget - reserve >= cost:
                priced_orders.append((_seed_priority(crop, day), ["BUY_SEED", crop, k]))
                seed_orders_n += 1
                budget -= cost

    # --- Animal fleet purchase ---
    # Serialized: only start a new purchase (or retry a stalled one) if
    # nothing is currently BOUGHT/CARRYING -- one farmer can only
    # build+carry+place one animal at a time.
    n_animals = (len(view["my_pastures"]) +
                 sum(1 for p in animal_plans if p["stage"] in ("BOUGHT", "CARRYING")))
    in_progress = any(p["stage"] in ("BOUGHT", "CARRYING") for p in animal_plans)
    if not in_progress:
        target_plan = next((p for p in animal_plans if p["stage"] == "NONE"), None)
        if target_plan is None:
            # v8.3: COW's own gate first, unchanged from v8.2 -- cow count
            # is never reduced by SHEEP existing. SHEEP only gets a look
            # once COW's own gate has already said no this turn, and uses
            # its own separate (relaxed-ceiling) gate -- see file header.
            if _animal_expansion_feasible(obs, view, budget, shed, n_animals, len(me["hands"]), quads):
                target_plan = {"species": "COW", "stage": "NONE", "site": None,
                                "stage_turn": None, "retries": 0}
            elif SHEEP_ENABLED and _sheep_expansion_feasible(obs, view, budget, shed, n_animals, len(me["hands"]), quads):
                target_plan = {"species": "SHEEP", "stage": "NONE", "site": None,
                                "stage_turn": None, "retries": 0}
        if target_plan is not None:
            spec = ANIMAL_SPECS[target_plan["species"]]
            if (spec["start_day"] <= day <= spec["last_day"]
                    and shed.get(target_plan["species"], 0) == 0
                    and budget > spec["min_money"]):
                priced_orders.append((PRIORITY_MEDIUM, ["BUY_ANIMAL", target_plan["species"], 1]))
                if target_plan not in animal_plans:
                    animal_plans.append(target_plan)
                _advance(target_plan, "BOUGHT", day, hour)
                budget -= spec["cost"]
                _grow_reserved_sites(view)  # claim a tile now that we've committed

    # --- JIT feed wheat (FEED consumes carried wheat, staged via shed) ---
    if n_animals > 0:
        target_wheat = n_animals * 2 + FEED_CARRY_TARGET
        have = shed.get("WHEAT", 0)
        if have < target_wheat:
            qty = min(target_wheat - have, 10)
            cost = qty * live_price(obs, "WHEAT")
            if budget >= cost:
                priced_orders.append((_feed_priority(view), ["BUY_PRODUCT", "WHEAT", qty]))
                budget -= cost

    # --- Fertilizer straight to market ---
    fert = shed.get("FERTILIZER", 0)
    if fert > 0:
        priced_orders.append((_sell_priority("paced", shed_load), ["SELL", "FERTILIZER", fert]))

    # --- Paced selling + demand-timing attack ---
    # force_dump relieves shed overflow by selling only the amount needed,
    # at a real price floor, instead of dumping an item's entire quantity.
    DUMP_TARGET_LOAD = SHED_CAP - 20
    force_dump = shed_load > SHED_CAP - 15 and hour >= 18
    dump_overflow = max(0, shed_load - DUMP_TARGET_LOAD) if force_dump else 0
    is_attack = timing_engine.is_attack_turn(day, hour)
    is_holding = timing_engine.is_holding_phase(day, hour)

    feed_reserve = n_animals * 2 + (FEED_CARRY_TARGET if n_animals else 0)
    sellable = []
    for i, n in shed.items():
        if not (isinstance(n, (int, float)) and n > 0):
            continue
        if i not in MARKET_PARAMS or i == "FERTILIZER" or i in ("COW", "SHEEP", "GOOSE"):
            continue
        if i == "WHEAT":
            n = n - feed_reserve
            if n <= 0:
                continue
        sellable.append((i, n))

    for item, n in sorted(sellable, key=lambda kv: -live_price(obs, kv[0])):
        base = MARKET_PARAMS[item]["base"]
        price_now = live_price(obs, item)
        reason = "paced"
        if is_attack and item in PREMIUM_CROPS:
            qty = max(1, int(n * timing_engine.dump_ratio))
            reason = "attack"
        elif is_holding and item in PREMIUM_CROPS and not force_dump:
            continue
        elif day >= LIQUIDATE_DAY:
            qty = int(n)
            reason = "final"
        elif price_now >= 1.05 * base:
            # Good price, but not urgent by itself -- goods keep in the
            # shed. _sell_priority scores this by shed pressure below,
            # not as a flat "final"/"capacity" event.
            qty = int(n)
        elif force_dump and dump_overflow > 0:
            # Sell only enough to relieve the actual overflow, at a real
            # price floor (50% of base) first; dip below it only for
            # whatever residual is still needed.
            dump_floor = 0.5 * base
            want_qty = min(int(n), int(dump_overflow))
            qty = units_sellable_above(item, inv.get(item, I0), dump_floor, want_qty)
            if qty < want_qty:
                qty += min(int(n) - qty, want_qty - qty)
            dump_overflow -= qty
            reason = "capacity"
        elif force_dump:
            # Overflow already relieved by earlier (higher-priced) items
            # this turn -- fall through to normal paced selling.
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if view["opp_imminent"].get(item, 0) >= 4:
                frac -= 0.25
            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, int(n))
        else:
            frac = 0.85 if item in PREMIUM_CROPS else 0.70
            if view["opp_imminent"].get(item, 0) >= 4:
                frac -= 0.25
            if behind and item in PREMIUM_CROPS and day >= 20:
                frac += 0.10
            floor = frac * base
            relax = max(0.0, 1.0 - max(0, shed_load - 40) / 50.0)
            qty = units_sellable_above(item, inv.get(item, I0), floor * relax, int(n))
        if qty > 0:
            priced_orders.append((_sell_priority(reason, shed_load), ["SELL", item, qty]))

    # --- Hiring: real Fibonacci cost, counts animal maintenance workload
    # alongside crops so the hand pool scales with the fleet too. ---
    if hour == 0 and day < 29:
        animal_work = _pending_animal_work(view)
        work = (len(view["water"]) + len(view["urgent_water"]) +
                len(view["harvest"]) + len(view["empty"]) +
                animal_work * ANIMAL_WORK_WEIGHT)
        target = max(HAND_TARGET_MIN, min(HAND_TARGET_MAX, math.ceil(work / 6)))
        need = max(0, target - len(me["hands"]))
        n = 0
        hire_count = 0
        while n < need and hire_count < MAX_HIRE_SLOTS:
            cost = FARM_HAND_COST_MULT * _fib(n)
            if budget < cost:
                break
            priced_orders.append((PRIORITY_HIGH_HIRE, ["HIRE"]))
            hire_count += 1
            budget -= cost
            n += 1

    # v7.11: sort by cost-of-delay, highest first, then truncate. Python's
    # sort is stable, so orders with equal scores keep the relative order
    # they were built in above. This replaces the old fixed-bucket
    # concatenation + "steal the last SELL slot" special case -- whichever
    # order is genuinely least valuable this turn is the one that gets
    # dropped, not whichever bucket happened to land past index 10.
    priced_orders.sort(key=lambda po: -po[0])
    orders = [order for _score, order in priced_orders[:MAX_MARKET_ORDERS]]
    return orders


# =====================================================================
# MOVEMENT
# =====================================================================

def _step_toward(pos, target):
    x, y = pos
    tx, ty = target
    if x < tx: return "EAST"
    if x > tx: return "WEST"
    if y < ty: return "SOUTH"
    if y > ty: return "NORTH"
    return None


def _nearest(pos, targets):
    if not targets:
        return None
    return min(targets, key=lambda t: abs(t[0] - pos[0]) + abs(t[1] - pos[1]))


def _dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _nearest_center(pos):
    return _nearest(pos, CENTER_TILES)


# =====================================================================
# ANIMAL PIPELINE (farmer-owned)
#
# Setup stages per plan: NONE -> BOUGHT -> (build) -> CARRYING -> ACTIVE;
# ABANDONED on repeated failure. Only one plan is ever BOUGHT/CARRYING at
# a time. Maintenance is stateless and fleet-wide: it always operates on
# the nearest tile in view["my_pastures"], which naturally includes every
# ACTIVE plan's site regardless of species or how many are active.
# =====================================================================

def _fail_stage(plan, fallback_stage):
    plan["retries"] += 1
    if plan["retries"] > SETUP_MAX_RETRIES:
        plan["stage"] = "ABANDONED"
    else:
        plan["stage"] = fallback_stage


def _advance(plan, stage, day, hour, **kv):
    plan["stage"] = stage
    plan["stage_turn"] = day * 24 + hour
    plan["retries"] = 0
    plan.update(kv)


def animal_reconcile(plan, view, shed, farmer_carry, day, hour):
    """Verify last turn's animal-setup action against the new observation."""
    species = plan["species"]
    stage = plan["stage"]
    turn = day * 24 + hour
    timed_out = plan.get("stage_turn") is not None and turn - plan["stage_turn"] >= SETUP_STAGE_TIMEOUT
    site = plan.get("site")

    site_occupied = site is not None and any(pos == site for pos, _tile in view["my_pastures"])
    if site_occupied:
        if stage != "ACTIVE":
            _advance(plan, "ACTIVE", day, hour)
        return

    if stage == "BOUGHT":
        if shed.get(species, 0) > 0 or farmer_carry.get(species, 0) > 0:
            pass  # good; setup action logic moves us forward
        elif timed_out:
            _fail_stage(plan, "NONE")
    elif stage == "ACTIVE":
        # Engine only clears the "animal" key (2 consecutive unfed days),
        # never the tile itself -- should be rare, but treat as abandoned
        # if the animal's gone and we're not carrying a replacement.
        if shed.get(species, 0) == 0 and farmer_carry.get(species, 0) == 0:
            _advance(plan, "ABANDONED", day, hour)
    elif stage == "CARRYING" and farmer_carry.get(species, 0) == 0 and shed.get(species, 0) > 0:
        _fail_stage(plan, "BOUGHT")
    elif timed_out and stage not in ("NONE", "ABANDONED"):
        _fail_stage(plan, "NONE" if shed.get(species, 0) == 0 else "BOUGHT")


def animal_setup_action(pos, view, shed, farmer_carry, plan, day, hour, reserved_sites=()):
    """Multi-turn setup for the one in-progress plan. Returns an op, or None
    to release the farmer to maintenance/crop work."""
    species = plan["species"]
    stage = plan["stage"]
    if stage in ("NONE", "ABANDONED", "ACTIVE"):
        return None

    carrying = farmer_carry.get(species, 0) > 0

    site = plan.get("site")
    if site is None or (site not in view["empty"] and site not in view["empty_pastures"]):
        candidates = [t for t in (view["empty_pastures"] or view["empty"])
                      if t not in CENTER_TILES]
        if not candidates:
            return None
        # Prefer a still-unclaimed reserved near-shed slot over the nearest
        # fallback, so daily walks stay short even for late purchases.
        pool = [t for t in reserved_sites if t in candidates] or candidates
        site = min(pool, key=lambda p2: _dist(p2, _nearest_center(p2)))
        plan["site"] = site

    # 1. Build the pasture first (animal waits safely in the shed).
    if site not in view["empty_pastures"]:
        if pos != site:
            return [_step_toward(pos, site)]
        return ["BUILD_PASTURE"]

    # 2. Pick the animal up at a center (shed) tile.
    if not carrying:
        if shed.get(species, 0) == 0:
            return None  # reconcile will retry/abandon
        center = _nearest_center(pos)
        if pos not in CENTER_TILES:
            return [_step_toward(pos, center)]
        _advance(plan, "CARRYING", day, hour)
        return ["PICKUP", species, 1]

    # 3. Walk it to the pasture and place it. VERIFIED format: no qty arg.
    if pos != site:
        return [_step_toward(pos, site)]
    return ["PLACE", species]


def _pasture_priority(pos, farmer_pos, tile):
    """Rank a pasture's urgency (lower = more urgent): overdue-unfed >
    unfed > ready-to-harvest > needs-care > fertilizer-waiting > nothing
    pending, distance as tiebreak."""
    fed = tile.get("fed_today", True)
    urgent = (not fed) and tile.get("consecutive_unfed", 0) >= 1
    if urgent:
        rank = 0
    elif not fed:
        rank = 1
    elif tile.get("yield_units", 0) > 0:
        rank = 2
    elif not tile.get("cared_today", True):
        rank = 3
    elif tile.get("fertilizer_available", False):
        rank = 4
    else:
        rank = 5
    return (rank, _dist(pos, farmer_pos))


def animal_maintenance_action(pos, view, shed, carry, day, hour, exclude=(), critical_only=False):
    """Stateless daily care across the whole active fleet. Targets whichever
    pasture has the most urgent pending need (see _pasture_priority).

    Works for any worker (`carry` is that worker's own carry inventory).
    `exclude` is the set of pasture positions already claimed by an earlier
    worker this turn, so multiple workers don't converge on the same
    animal.

    `critical_only` (v7.6a): when True, this worker will only engage with
    feed-related survival work (an animal due for feeding today, or
    already overdue) -- never CARE, HARVEST, COLLECT_FERTILIZER, or
    carried-product deposit trips. This is what lets a reserved crop hand
    still respond to an animal-death risk without being pulled into
    optional animal upkeep that isn't a survival matter. Real ladder
    replays showed exactly this optional work (CARE/HARVEST/FERTILIZER
    collection climbing from ~2/day to 9-11/day) crowding out crop
    watering/weeding as the fleet grew.

    Returns (op_or_None, claimed_pos_or_None) -- callers should add the
    claimed position to their `exclude` set before calling this for the
    next worker."""
    candidates = [(p, t) for p, t in view["my_pastures"] if p not in exclude]
    if critical_only:
        candidates = [(p, t) for p, t in candidates if not t.get("fed_today", True)]
    if not candidates:
        return None, None
    (ppos, tile) = min(candidates, key=lambda pt: _pasture_priority(pt[0], pos, pt[1]))

    needs_feed = not tile.get("fed_today", True)
    needs_care = (not critical_only) and (not tile.get("cared_today", True))
    has_yield = (not critical_only) and tile.get("yield_units", 0) > 0
    has_fert = (not critical_only) and tile.get("fertilizer_available", False)
    urgent_feed = needs_feed and tile.get("consecutive_unfed", 0) >= 1
    # Only claim ppos if it has real pending work.
    claim = ppos if (needs_feed or needs_care or has_yield or has_fert) else None

    carry_wheat = carry.get("WHEAT", 0)
    carry_products = {} if critical_only else {i: carry.get(i, 0) for i in ANIMAL_PRODUCTS if carry.get(i, 0) > 0}
    deposit_due = sum(carry_products.values()) >= PRODUCT_DEPOSIT_AT or (
        carry_products and (needs_feed and carry_wheat == 0))
    fetch_wheat_due = needs_feed and carry_wheat == 0 and shed.get("WHEAT", 0) > 0

    if pos == ppos:
        if needs_feed and carry_wheat > 0:
            return ["FEED"], claim
        if has_yield:
            return ["HARVEST"], claim
        if needs_care:
            return ["CARE"], claim
        if has_fert:
            return ["COLLECT_FERTILIZER"], claim

    if pos in CENTER_TILES:
        if fetch_wheat_due and urgent_feed:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))], claim
        if carry_products:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]], claim
        if fetch_wheat_due:
            return ["PICKUP", "WHEAT", min(FEED_CARRY_TARGET, shed.get("WHEAT", 0))], claim

    if fetch_wheat_due and urgent_feed:
        return [_step_toward(pos, _nearest_center(pos))], claim
    if fetch_wheat_due or deposit_due:
        return [_step_toward(pos, _nearest_center(pos))], claim
    if (needs_feed and carry_wheat > 0) or has_yield or needs_care or has_fert:
        return [_step_toward(pos, ppos)], claim

    if day >= LIQUIDATE_DAY and carry_products:
        if pos in CENTER_TILES:
            item = max(carry_products, key=carry_products.get)
            return ["PLACE", item, carry_products[item]], claim
        return [_step_toward(pos, _nearest_center(pos))], claim

    return None, None  # nothing pending for this worker -- falls back to crops


# =====================================================================
# CROP TASK ALLOCATION
# =====================================================================

TASK_ACTION = {
    "urgent_water": ["WATER"],
    "harvest": ["HARVEST"],
    "water": ["WATER"],
    "weeds": ["DIG"],
}


def _task_order(n_weeds):
    """v7.6a: weeds start last (matches v7.5) but get promoted as
    infestation grows -- ahead of ordinary planting once there are a
    few, ahead of ordinary watering too once it's severe. Real replays
    showed weed count climbing unchecked to 20-37/100 tiles while weeds
    stayed lowest priority the whole match."""
    if n_weeds >= WEED_URGENT_THRESHOLD:
        return ["urgent_water", "harvest", "weeds", "water", "plant"]
    if n_weeds >= WEED_PRIORITY_THRESHOLD:
        return ["urgent_water", "harvest", "water", "weeds", "plant"]
    return ["urgent_water", "harvest", "water", "plant", "weeds"]


def unit_action(pos, tasks, seeds, day, task_order):
    """v7.11's original per-unit dispatch: sequential, one unit at a time,
    each independently grabbing its own nearest available task and
    removing it from the shared pool before the next unit even looks.
    Kept byte-identical and still used when GLOBAL_TASK_ASSIGNMENT=False,
    so that flag-off path is a true no-op vs main_v7.11.py. See
    assign_tasks() below for the v8 replacement."""
    x, y = pos
    for key in task_order:
        if (x, y) in tasks[key]:
            tasks[key].remove((x, y))
            if key == "plant":
                for crop in plantable_crops(seeds, day):
                    seeds[crop] -= 1
                    tasks["urgent_water"].append((x, y))  # same-day water invariant
                    return ["PLANT", crop]
                continue
            return TASK_ACTION[key]

    for key in task_order:
        tgt = _nearest((x, y), tasks[key])
        if tgt:
            step = _step_toward((x, y), tgt)
            if step:
                tasks[key].remove(tgt)
                return [step]

    fallback = _step_toward((x, y), (4, 4))  # idle drift toward shed
    return [fallback] if fallback else ["PASS"]


def assign_tasks(unit_positions, tasks, seeds, day, task_order):
    """v8: joint per-turn task assignment across every unit that fell
    through to ordinary crop duty this turn (already resolved as having
    no animal-setup/maintenance work). Same task tiers and same actions
    as unit_action() -- this only changes HOW one turn's already-existing
    task pool is divided up among that turn's idle units, not the tier
    priority order and not what a unit does once standing on its target.
    See the file header for full rationale and what this deliberately
    does NOT change (no cross-turn memory -- task lists are still
    rebuilt from perception every turn, exactly as in v7.11).

    Pass 1: any unit already standing exactly on a pending task tile
    (any tier) claims it for free before any walking is considered --
    matches unit_action()'s "standing beats walking, regardless of tier
    rank" rule.

    Pass 2: remaining units get ONE joint nearest-pair match per tier,
    across all of that tier's still-unassigned units and still-available
    tiles at once (every candidate pair sorted by ascending distance,
    confirmed greedily), instead of each unit independently grabbing its
    own nearest target in a fixed roster order.

    Returns a list of ops, same length and order as unit_positions.
    """
    n = len(unit_positions)
    assigned_tile = [None] * n
    assigned_key = [None] * n
    unassigned = set(range(n))

    # Pass 1: standing-on-task claims, tier by tier.
    for key in task_order:
        if not unassigned:
            break
        pool = tasks.get(key) or []
        if not pool:
            continue
        pool_set = set(pool)
        claimed = set()
        for i in list(unassigned):
            pos = unit_positions[i]
            if pos in pool_set and pos not in claimed:
                assigned_tile[i] = pos
                assigned_key[i] = key
                unassigned.discard(i)
                claimed.add(pos)
        if claimed:
            tasks[key] = [t for t in pool if t not in claimed]

    # Pass 2: joint nearest-pair matching, tier by tier, over what's left.
    for key in task_order:
        if not unassigned:
            break
        pool = tasks.get(key) or []
        if not pool:
            continue
        pairs = []
        for i in unassigned:
            pos = unit_positions[i]
            for t in pool:
                pairs.append((_dist(pos, t), i, t))
        if not pairs:
            continue
        pairs.sort(key=lambda p: p[0])   # stable: ties keep this build order
        used_tiles = set()
        for _d, i, t in pairs:
            if i not in unassigned or t in used_tiles:
                continue
            assigned_tile[i] = t
            assigned_key[i] = key
            used_tiles.add(t)
            unassigned.discard(i)
        if used_tiles:
            tasks[key] = [t for t in pool if t not in used_tiles]

    # Convert assignments to ops -- same action set as unit_action().
    ops = [None] * n
    for i, pos in enumerate(unit_positions):
        tile, key = assigned_tile[i], assigned_key[i]
        if tile is None:
            fallback = _step_toward(pos, (4, 4))  # idle drift toward shed
            ops[i] = [fallback] if fallback else ["PASS"]
            continue
        if pos == tile:
            if key == "plant":
                op = None
                for crop in plantable_crops(seeds, day):
                    seeds[crop] -= 1
                    tasks["urgent_water"].append(tile)  # same-day water invariant
                    op = ["PLANT", crop]
                    break
                ops[i] = op if op else ["PASS"]
            else:
                ops[i] = TASK_ACTION[key]
        else:
            step = _step_toward(pos, tile)
            ops[i] = [step] if step else ["PASS"]
    return ops


# =====================================================================
# ENTRY
# =====================================================================

timing_engine = DemandTimingEngine(match_seed=42)
animal_plans = []    # fleet state -- list of per-animal plan dicts, mutated in place
reserved_sites = []  # near-shed tiles claimed for the fleet, grown incrementally
                      # by _grow_reserved_sites (one per animal actually purchased)


def _init_reserved_sites(view):
    """Accessor for the fleet's currently-reserved near-shed tiles."""
    return reserved_sites


def _reserved_crop_hand_count(view, seeds, day, n_hands, quads):
    """v7.6a: how many of the current hands are walled off for crop-only
    work this turn. Scales with real symptoms of neglect (weed density,
    crop backlog relative to hand count) rather than a flat number."""
    if n_hands <= 0:
        return 0
    unlocked_tiles = max(1, TILES_PER_QUAD * max(1, quads))
    weed_ratio = len(view["weeds"]) / unlocked_tiles
    plantable = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in plantable)
    crop_pressure = (len(view["urgent_water"]) + len(view["water"]) +
                      len(view["weeds"]) + min(len(view["empty"]), n_plantable))
    if weed_ratio >= WEED_RATIO_HIGH or crop_pressure > n_hands * CROP_PRESSURE_HAND_MULT:
        fraction = PROTECTED_FRACTION_HIGH
    else:
        fraction = PROTECTED_FRACTION_LOW
    return min(n_hands, max(MIN_RESERVED_CROP_HANDS, math.ceil(n_hands * fraction)))


def _agent(obs):
    p = obs["player"]
    me, opp = obs["farms"][p], obs["farms"][1 - p]
    day, hour = obs["day"], obs["hour"]
    seeds = dict(obs["private"]["seeds"])
    shed = obs["private"]["shed"]

    inventories = obs["private"].get("inventories") or []
    farmer_carry = inventories[0] if inventories else {}

    view = perceive(me, opp, day)
    sites = _init_reserved_sites(view)
    for plan in animal_plans:
        animal_reconcile(plan, view, shed, farmer_carry, day, hour)

    market = economy(obs, me, opp, view, seeds, day, hour, timing_engine, animal_plans)

    crops_now = plantable_crops(seeds, day)
    n_plantable = sum(seeds.get(c, 0) for c in crops_now)

    task_order = _task_order(len(view["weeds"]))
    tasks = {
        "urgent_water": list(view["urgent_water"]),
        "harvest": list(view["harvest"]),
        "water": list(view["water"]),
        "plant": (view["empty"][:n_plantable] if crops_now and hour < 21 else []),
        # v7.6a: weed-clearing no longer shuts off for the last two days --
        # replays showed the collapse was already well underway by day 25,
        # long before that cutoff mattered, and disabling it just let the
        # infestation stand unchallenged during the final push.
        "weeds": list(view["weeds"]),
    }
    # Never plant on an in-progress pasture site or an unclaimed reserved
    # near-shed slot -- keeps it available/close for whenever the next
    # purchase actually fires.
    claimed_sites = {pl["site"] for pl in animal_plans if pl.get("site") and pl["stage"] != "ABANDONED"}
    excluded = claimed_sites | set(sites)
    if excluded:
        tasks["plant"] = [t for t in tasks["plant"] if t not in excluded]

    quads = len(me["unlocked_quadrants"])
    n_hands = len(me["hands"])
    reserved_count = _reserved_crop_hand_count(view, seeds, day, n_hands, quads)

    farmer_pos = tuple(me["farmer"])
    active_setup_plan = next((pl for pl in animal_plans if pl["stage"] in ("BOUGHT", "CARRYING")), None)
    # An urgent feed need on an already-placed pasture preempts setup work
    # for the turn, so setting up animal N+1 can't starve animal N.
    urgent_existing_feed = any(
        not t.get("fed_today", True) and t.get("consecutive_unfed", 0) >= 1
        for _pos, t in view["my_pastures"]
    )
    claimed_pastures = set()
    farmer_op = None
    farmer_needs_crop = False
    if active_setup_plan is not None and not urgent_existing_feed:
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        # Farmer keeps v7.5's original unconditional (critical_only=False)
        # maintenance-first behavior -- only the hand pool is split below.
        farmer_op, claim = animal_maintenance_action(farmer_pos, view, shed, farmer_carry, day, hour, claimed_pastures)
        if claim is not None:
            claimed_pastures.add(claim)
    if farmer_op is None and active_setup_plan is not None:
        # Nothing urgent for maintenance (e.g. no wheat staged yet) -- fall
        # back to setup work rather than idling.
        farmer_op = animal_setup_action(farmer_pos, view, shed, farmer_carry, active_setup_plan, day, hour, sites)
    if farmer_op is None:
        if GLOBAL_TASK_ASSIGNMENT:
            farmer_needs_crop = True
        else:
            farmer_op = unit_action(farmer_pos, tasks, seeds, day, task_order)

    # v7.6a: the first `reserved_count` hands are walled off for crop work
    # -- they may still answer a feed-critical animal need (critical_only
    # still checks fed_today), but never the optional maintenance
    # (CARE/HARVEST/COLLECT_FERTILIZER/product deposit) that was crowding
    # out watering/weeding in the real loss replays. Remaining hands keep
    # v7.5's original full-priority behavior.
    hand_ops = [None] * len(me["hands"])
    hand_needs_crop = []   # list of (index, pos), in roster order
    for i, h in enumerate(me["hands"]):
        hand_pos = tuple(h)
        hand_carry = inventories[i + 1] if len(inventories) > i + 1 else {}
        is_reserved = i < reserved_count
        op, claim = animal_maintenance_action(hand_pos, view, shed, hand_carry, day, hour,
                                                claimed_pastures, critical_only=is_reserved)
        if op is not None:
            hand_ops[i] = op
            if claim is not None:
                claimed_pastures.add(claim)
        else:
            if GLOBAL_TASK_ASSIGNMENT:
                hand_needs_crop.append((i, hand_pos))
            else:
                hand_ops[i] = unit_action(hand_pos, tasks, seeds, day, task_order)

    # v8: one batched joint assignment for every unit (farmer + hands)
    # that fell through to ordinary crop duty this turn, instead of each
    # calling unit_action() independently in roster order. Farmer is kept
    # first in the input list (then hands in roster order) purely for
    # deterministic tie-breaking -- the matching itself is order-
    # independent except for exact-distance ties.
    if GLOBAL_TASK_ASSIGNMENT and (farmer_needs_crop or hand_needs_crop):
        crop_unit_positions = ([farmer_pos] if farmer_needs_crop else []) + [pos for _i, pos in hand_needs_crop]
        crop_ops = assign_tasks(crop_unit_positions, tasks, seeds, day, task_order)
        k = 0
        if farmer_needs_crop:
            farmer_op = crop_ops[k]
            k += 1
        for (i, _pos) in hand_needs_crop:
            hand_ops[i] = crop_ops[k]
            k += 1

    return {"farmer": farmer_op, "hands": hand_ops, "market": market}


def agent(obs, configuration=None):
    """Kaggle submission entry point with top-level crash guard."""
    try:
        return _agent(obs)
    except Exception as exc:
        import traceback
        print(f"GUARD swallowed exception: {exc!r}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        return {"farmer": ["PASS"], "hands": [], "market": []}
