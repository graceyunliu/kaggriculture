# v7.3 — Replay-proven policy corrections

Four surgical fixes to `main_v7.2.py`, ordered by evidence strength. Test each independently; pass the champion/challenger gate separately before combining.

## 1. Fix the force-dump firesale

`force_dump` in `economy()` (line 356): once shed load crosses `SHED_CAP - 15` after hour 18, the code dumps the entire remaining quantity of an item regardless of price.

**Evidence:** across all 6 replay losses, this fired 11 separate SELL orders totaling 800 units at ~$1/unit (the market price floor), mostly MELON, in the day 23–28 window. In the closest loss (seed 90010183, lost by $243), the log shows a 78-unit sale at $13 immediately followed by a 90-unit sale at $1 — more than the entire losing margin. Strongest, most concretely evidenced finding in the review; worth more than the other three combined.

**Fix:**
- Give the shed-overflow dump a real price floor — sell down to capacity at the best achievable price instead of liquidating everything at whatever the market bears.
- Gate the dump by actual price and expected near-term supply, not just capacity threshold.
- Throttle melon production earlier so the shed doesn't reach 85/100 capacity in the first place.
- Preserve the rest of the current sell policy (attack windows, price floors, opponent-glut response) unchanged.

**Test:** replay the 6 losing seeds (648705106, 421738759, and the other 4) against v7.1 as a stand-in opponent. Not the real opponents' code, but same-seed testing isolates the mechanism. Check whether the fix realizes meaningfully better melon prices and more total money in that day 23–28 window.

## 2. Wheat planting priority

WHEAT is last in `PLANT_PRIORITY` (`["MELON", "STRAWBERRY", "CARROT", "WHEAT"]`, line 149) — bought every game, planted 0–2 times. Four of six opponents sell hundreds of units of it.

**Fix, test both:**
- Stop buying wheat seeds that go unused, or reorder priority / bump the seed target so purchased wheat actually gets planting capacity.
- Test whether wheat is best used for feed, direct sale, or both — don't assume direct sale is the only justification for the reorder.

## 3. Land timing (+ cow-purchase timing, same root cause)

v7.2 finishes all land purchases on day 11 every game — budget-gated, not chosen. Two of the six winners bought land on day 0.

**Budget competition:** `economy()` uses a single shared cash pool (`me["money"]`), checked in this order each turn: animal purchase → land → feed wheat → hiring → seeds (line 300-432). Starting money is 3,000; land costs scale 1,000 / 2,000 / 4,000 for quadrants 2/3/4 — the third and fourth purchases alone exceed the entire starting bankroll.

**Root cause, traced in replay (episode 90010183, seed 1010599194):** day 0 (hires + full seed slate) drops money from 3,000 to 728 by day 1. Melon (the primary crop, `first: 10, max_day: 12`) hasn't matured yet, so there's no revenue for the next ~10 days — money just drifts down from ongoing small hire/seed costs: 728 → 636 → 624 by day 3, continuing down to 388 by day 10. Both the cow (`budget > 700`, gated from day 3) and land quadrant 2 (`budget > 1,000`) sit blocked below their thresholds the entire time. On day 11, the first melon harvest sells (90 units at ~$230/unit) and money jumps from 388 to 21,006 in one step — clearing every blocked gate at once, so `BUY_ANIMAL`, `BUY_LAND` ×3, and a fresh seed round all fire in the same turn. Land and cow aren't independently timed; they're both just waiting on the same first paycheck.

**Fix — cow:** lower `ANIMAL_SPECS["COW"]["start_day"]` from 3 to 1 (or 0). The buffer actually clears the $700 gate on day 1 (728) — it's only day 3's check that fails (624), because two more days of erosion happen in between. Since the animal-purchase check runs first in `economy()`, ahead of all other spending that turn (line 306), an earlier `start_day` lets it claim the cash before erosion, no reserve/floor logic needed. This is a one-line constant change. Flagged as an open, untested parameter in the design doc (previously only "test day 3 vs 6 vs 10" was considered — the replay evidence flips the direction worth testing to earlier, not later). Fallback if a sweep shows day 0/1 isn't reliably enough across seeds: a shared cash floor (~$750-800) applied to day-0-through-3 discretionary spend (both hiring and seed top-ups — in the traced game the erosion was mostly one extra melon-seed purchase, not hiring, so a hiring-only cut isn't a reliable general fix).

**Fix — land:** still test buying land before the first seed spend rather than whenever budget happens to be leftover, but don't add a matching cash reserve for land — land's cutoffs (`day <= 18` / `day <= 16`) already tolerated the day-11 delay in the traced game (nothing was missed, tiles just got fewer productive cycles), and reserving land's larger threshold (1,000+) upfront risks shrinking the very day-0 seed spend that produces the day-11 windfall in the first place.

**Test:** sweep COW `start_day` ∈ {0, 1, 3} in local self-play and against the 6 replay seeds — confirm day-0/1 money reliably clears $700 across seeds, not just the one traced game. For land, measure whether the extra early tiles are actually used productively (planted/watered in time), not just that land closes earlier.

## 4. Fleet ceiling re-test

Highest effort, most uncertain payoff. Do last — the other three changes may alter the economy enough that the earlier 6-animal collapse trace doesn't reproduce the same way.

**Fix:** try 4, 6, 8, and a survival-gated dynamic cap. Expansion should not be blocked on hitting every feed/care tick on schedule — occasional late feeding or delayed care is acceptable as long as the animal doesn't die. The only hard gate is survival: if animals start dying, stop expanding; if they don't, imperfect care isn't a reason to hold back the cap. This time, isolate whether the earlier 6-animal collapse was caused by feed-wheat cost or tile-reservation crop-crowding — don't just crank the number up again, since that already failed once without knowing the cause.

**Test:** track animal survival and product output per fleet size, not just end-game cash.

## Testing protocol (all fixes)

- Local seeded self-play against v7.1, v7.2, and starter for regression safety: no crashes, no worse than current baseline.
- The 6 real replay seeds against v7.1 as stand-in opponent, to directly measure the targeted metric per fix (melon realized price, wheat units sold, land-use productivity, animal survival/output).

## Promotion gate

No regressions · real improvement on the targeted metric for each fix · zero new crashes or animal deaths. Combine only after each fix clears this individually.
