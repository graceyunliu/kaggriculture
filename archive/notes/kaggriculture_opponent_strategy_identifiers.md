# Kaggriculture Opponent Strategy Identifiers

Derived from full 720-step (30-day) replay data, not from the strategy-catalog document alone. Parsed 234 replay files, 227 successfully (7 truncated/corrupt JSON skipped), yielding **440 opponent-farm instances across 133 distinct named accounts** (your own `graceyunliu` side excluded everywhere, per your instruction). For every instance, every day's tile grid, animal state, market action, and land state was reconstructed day-by-day across the full season, then cross-tabulated: what an opponent does in the first 0–10 days against what their farm looks like on day 29.

**Headline finding, and the single most important thing to build detection around:** this replay set is not 133 independent strategies. It is overwhelmingly *one shared/cloned script* running under 100+ different Kaggle usernames, plus a couple of consistent forks of that same script, plus a small tail of genuinely distinct openings. 410/440 instances (93.2%) match one exact fingerprint down to the day. Detecting "is this the clone?" should be your first and highest-value classifier — everything else is a tail case.

Identifiers below are grouped by what they detect. Each gives the observable signal, the sample it's based on, and a confidence level. Sample sizes under ~10 are flagged explicitly as low-confidence even when the percentage looks clean, per your instructions.

---

## A. The dominant meta-clone (93.2% of the field, n=410/440)

If you see the day-0/day-7 signals in group A.1–A.4 together, you can stop looking — you are playing the clone, and everything else in this section tells you exactly what it will do for the rest of the game.

1. **Simultaneous COW+SHEEP buy on day 0.** `BUY_ANIMAL COW` and `BUY_ANIMAL SHEEP` both fire on turn 0, same day as `BUILD_PASTURE`. 409/410 clone instances (99.8%). Confidence: **very high (~93% this predicts the full clone profile below).** Counter: this opponent's animal income is capped at exactly 1 cow + 1 sheep for the whole game (see #11) — don't over-invest in animal-market defense, their livestock output is fixed and predictable from day 0.

2. **Day-0 dual crop planting: WHEAT + MELON together.** WHEAT day-0 in 97% of clone instances, MELON day-0 in 96% of *all* 440 instances (clone and non-clone alike). Confidence: **high**, but see #24 — the specific crop chosen on day 0 is noisier than it looks.

3. **MELON is a bootstrap, not a strategy.** Despite being planted turn 0 in 96% of all instances, MELON is present in the final-day tile snapshot of **0/410** clone farms. It is planted for early cash flow only and fully converted away by mid-game. Confidence: **very high.** Do not read early melon tiles as a "pure melon monoculture" commitment (strategy doc #6) — in this dataset that read is wrong essentially every time.

4. **Immediate, continuous hiring.** First `HIRE` action always lands on day 0 (100% of clones), and clone instances issue at least one hire action on **all 30 days** of the season (409/410). Confidence: **very high.** This is the single cheapest tell to check — an opponent hiring every single day, starting day 0, is almost certainly the clone.

5. **Fixed 3-stage land schedule: NW (day 0) → NE (day 7) → SW (day 10) → stop.** 100% of clone instances follow exactly this quadrant order; 98.5% buy the 2nd quadrant on exactly day 7; 97.6% buy the 3rd on exactly day 10. Confidence: **very high.**

6. **Land purchases stop at 3 quadrants — SE is never touched.** 421/440 (95.7%) of *all* instances (clone or not) cap at exactly 3 quadrants. If you see an opponent building fast through day 10 and then land purchases go quiet, expect no further land expansion for the rest of the game. Confidence: **very high.**

7. **STRAWBERRY planted day 4, becomes the primary crop.** 97% of clones plant their first strawberry tile on day 4 specifically (2 days after wheat, on schedule). By day 29 the modal strawberry tile count is 6 (69% of clones land on 4–7 tiles). Confidence: **high.**

8. **WHEAT is deliberately kept small — one tile, feeding the cow.** 67% of clone instances end the game with exactly 1 wheat tile, not scaled up as an income crop. This matches the "wheat-feeds-cow" synergy (reference doc #5): wheat isn't grown to sell, it's grown to avoid buying feed. Confidence: **moderate-high (67%)**, remainder mostly have 5–7 tiles instead (see #9 as the split).

9. **A large-wheat sub-variant exists but is a minority.** ~29% of clones end with 5–7 wheat tiles instead of 1 — likely running wheat as a secondary cash crop, not just cow feed. If wheat tile count grows past 2–3 by mid-game, downgrade your confidence that they're minimizing wheat, and expect wheat to show up as a real, recurring sell item rather than an occasional surplus dump. Confidence: **moderate (~29% of clones, n≈118).**

10. **Exactly one of each animal, never a scaled herd.** 100% of clone instances hold precisely 1 cow + 1 sheep for the entire 30 days — they never buy a second cow or second sheep. Confidence: **very high.** Counter: this bot's animal-market footprint (WOOL/MILK demand and supply) is fixed and small; if you're competing for animal-product shelf space, this opponent will never scale up to challenge you there.

11. **Fertilizer comes from `COLLECT_FERTILIZER`, not the market.** Clone instances average 318 collect-fertilizer actions across the game; only 23% (95/410) ever use `BUY_PRODUCT FERTILIZER` at all. Confidence: **high.**

12. **Bought-fertilizer users run smaller strawberry patches.** Among clones, instances that do buy fertilizer average 4.7 strawberry tiles vs. 6.0 for those that don't (n=95 vs. 315) — an intensify-fewer-tiles-faster trade rather than extensify-more-tiles-slower. Confidence: **moderate (clear directional split, modest sample).**

13. **Near-perfect feed/care discipline.** Feed ratio and care ratio sit at 0.93–1.0 on every day an animal is present, in 99.5% of *all* 440 instances (not just clones). Confidence: **very high, and important as a negative signal** — see #34.

14. **Low weed accumulation (clean tile management).** Clone instances average 52.5 "tile-weed-days" over the season vs. 167.8 for non-clone instances — a 3.2x gap. Confidence: **high.** Weedy tiles are one of the fastest visual tells that you are *not* facing the optimized clone.

15. **Predictable cash curve.** Median cash on hand: day 7 ≈ $920, day 10 ≈ $3,140, day 15 ≈ $22,900, day 20 ≈ $50,100, day 29 ≈ $127,000, with tight variance (day-29 range mostly $47k–$186k). Confidence: **high.** If an opponent you've flagged as "clone-like" is badly behind this curve by day 15, re-check — you may be facing a fork (Section B) instead.

16. **Sells a fixed core basket every game, a variable fringe basket sometimes.** WHEAT, WOOL, MILK, MELON, STRAWBERRY, and FERTILIZER are sold in 100% of clone instances; CARROT, EGG, and TOMATO only in 70–74%. Confidence: **high.** The fringe goods are byproduct/opportunistic sales, not planned income — don't expect this opponent to compete hard for carrot/egg/tomato shelf space.

17. **Sells are paced, not dumped.** Median per-transaction sell size is 4–8 units; only 1/410 clone instances ever sold ≥500 units in one order, and when it happened it landed on day 28–29 (end-of-season liquidation only). Confidence: **high.** This opponent will not crash a market with a surprise bulk dump mid-game — if you see a large dump before day 25, it's not this bot.

18. **Land size scales hiring, not the other way around.** Hire cadence (daily, every day) is identical across 1-, 2-, 3-, and 4-quadrant instances — hiring is constant regardless of farm size, so hire frequency alone does not tell you how much land an opponent holds. Confidence: **high**, and useful mainly as a negative/don't-bother signal.

---

## B. The "budget fork" — a second, smaller clone (1.8% of the field, n=8/440)

This is not noise. Eight different named accounts produce an *identical* fingerprint distinct from Section A, strongly suggesting a second shared/forked script rather than eight independent human strategies.

19. **Cow-only, no sheep, ever.** Buys `BUY_ANIMAL COW` day 0 (matching the main clone) but never buys a sheep. Confidence: **high (n=8, internally 100% consistent).**

20. **Second land purchase delayed to day 10, and it's the last one.** Where the main clone buys 2nd land on day 7 and 3rd on day 10, this fork buys its *only* 2nd quadrant on day 10 and stops — it never reaches a 3rd quadrant. Confidence: **high (8/8 in this sub-group).**

21. **Identical feed/care ratios down to the decimal: 0.9667 feed, 0.9333 care.** This exact repeated value across unrelated accounts is strong evidence of shared code, not coincidence. Confidence: **high.**

22. **Still converges on WHEAT+STRAWBERRY as final crops** — same crop endgame as the main clone, just reached with half the land. Confidence: **high.**

23. **Meaningfully weaker economically.** Day-29 median cash ≈ $36,000–42,000 vs. the main clone's ≈$127,000 — roughly a third. Confidence: **high.** Counter: this opponent is beatable on land/animal economics alone; you don't need a special counter-strategy, just outland and out-diversify them.

24. **The tell shows up as early as day 10.** By day 10, if an opponent has bought exactly one land parcel (not two) and holds only a cow (no sheep), you can call this fork with reasonable confidence rather than waiting for the full game. Confidence: **moderate-high (early read, n=8).**

---

## C. Genuine divergent openings (the true minority, ~6.8% of the field)

These are the closest thing to "real" alternative strategies in the dataset — each still small-sample, called out with confidence accordingly.

25. **Sheep-rush opener.** Buys SHEEP before or without COW on day 0, prioritizing the single highest $/tile/day asset (reference doc #1) over the wheat-feeds-cow combo. n=3/30 deviants (0.7% overall). Confidence: **low-moderate (n=3).** Counter: this opponent has committed capital to their best per-tile asset early — expect them to be cash-tight in the early game since they skipped the cheaper cow.

26. **Goose budget-entry opener.** First animal is GOOSE (cheapest, $300) rather than cow/sheep, sometimes as late as day 10. n=2/30. Confidence: **low (n=2, flagging as directional only).** Matches reference doc #7/#13/#20 (budget-animal pairings); in this sample, goose-openers never scaled to a second animal type.

27. **Land-conservative, 2-quadrant permanent cap** — distinct from the Section B fork because these buy their 2nd quadrant *on day 7* (clone timing) rather than day 10, then still stop at 2. n≈4 of the 12 two-quadrant deviants don't match Section B's day-10 fingerprint. Confidence: **moderate (n≈4).**

28. **Land-aggressive, full 4-quadrant expansion.** Buys all 4 quadrants, with the 3rd and 4th typically landing on the same day or one day apart (e.g., days 11/11, 7/11/11) rather than gradually — reads as a "buy remaining land in one shot once a cash threshold is hit" rule. n=7/30 (23% of deviants, 1.6% overall). Confidence: **moderate.**

29. **4-quadrant opponents diversify less, not more, despite having the extra land.** Counterintuitively, the 4-quadrant deviant group sells CARROT only 50% of the time and TOMATO only 17% of the time, vs. 74%/70% for the standard 3-quadrant clone — the extra land goes to more wheat/strawberry, not more crop variety. Confidence: **moderate (n=7).** Counter: don't assume a big land grab means a diversified opponent; it more often means a bigger monoculture.

30. **Diversifier (4+ simultaneous crop types).** A small group ends the game running WHEAT+CARROT+MELON+TOMATO or similar 4-crop spreads, matching reference doc #16's hedge logic. n=2/30. Confidence: **low (n=2), flagged explicitly per your instructions.**

31. **Late first-animal purchase (day ≥10) while land/crop timing otherwise looks clone-like.** A "crop-first, animal-second" bootstrap: land and crops track the normal schedule, but the first animal purchase is pushed to day 10–11. In every case observed (n=3) this correlated with ending the game with only one animal type instead of the full pair. Confidence: **moderate (n=3, but the correlation with an incomplete animal roster was 3/3).**

32. **Single-quadrant, zero-crop "broken bot."** Never buys land beyond the starting NW quadrant, never plants a single crop the entire game, yet still feeds/cares for one animal at ~90% and continuously tries to hire (60 hire attempts across 30 days) while buying wheat from the market to resell rather than growing it. n=1, but the signature is unmistakable and worth watching for. Confidence: **low sample (n=1) but very high signature-specificity if seen** — this reads as a crashed, timed-out, or misconfigured opponent, not a deliberate strategy. Counter: this is a free win on land and crop income; you can safely ignore them as a market threat.

---

## D. Cross-cutting tells (apply regardless of which archetype above)

33. **Opening-day crop choice (which crop is planted first on day 0) is a weak signal on its own.** At least 10 instances plant WHEAT, CARROT, STRAWBERRY, or TOMATO first instead of MELON on day 0, yet otherwise match the main clone's land timing, animal pair, and final crop mix exactly. Confidence: **high that day-0 crop choice alone is *not* reliable** — treat it as tile-order noise, and wait for the day-7 land purchase and day-0 animal purchase to actually classify the opponent.

34. **Feed/care discipline essentially never drops below ~0.9 among competitive opponents.** 99.5% of all 440 instances (not just clones) maintain near-perfect feed/care ratios. Confidence: **very high, and it inverts a reference-doc strategy** — the "efficient every-other-day cared sheep" and "neglect" approaches from the catalog essentially don't appear in real competitive play here. If you do see a sustained sub-0.6 feed ratio from an opponent already holding animals, treat it as a bug/lag/disconnection on their end, not an intentional efficiency play.

35. **Heavy weed accumulation is a reliable "this is not the optimized bot" flag.** Already covered as #14, but worth stating as its own rule: a 3x+ gap in weed-tile-days (52 vs. 168) is one of the fastest, purely-visual signals available — you don't need to wait for market or animal data.

36. **Constant daily hiring is close to universal, so hire *frequency* doesn't discriminate — hire *timing relative to land purchases* does.** Nearly everyone (clone and most deviants) hires every day; what actually separates archetypes is whether hiring precedes or lags land expansion, and whether the opponent ever reaches a stable "no more hiring needed" plateau (none in this dataset do within 30 days).

37. **A day-29 cash figure far below ~$100k for an opponent showing clone-like day-0/day-7 behavior signals a fork or a disrupted game, not the standard clone.** Use the Section A cash curve (#15) as your benchmark and Section B's ~$36–42k as the fork benchmark; anything meaningfully below both suggests either a weaker independent strategy or a game where the opponent got outcompeted for market share/prices.

38. **A market dump (single sell order ≥500 units) before day 25 is essentially never seen from the dominant clone (1/410) and should be read as a distinct behavior**, not an intensified version of the standard strategy — likely a genuinely different (possibly human or less-optimized) trader liquidating for a specific reason. Confidence: **high given the near-total absence in the base rate.**

39. **Fertilizer-buying (vs. pure free-collection) correlates with running less land per crop, not with running more crops overall.** Already detailed in #12; stated generally, if you see FERTILIZER purchases from the market, expect a tighter, faster-cycling STRAWBERRY/TOMATO operation on fewer tiles rather than an expansion play.

40. **Quadrant unlock order is essentially fixed (NW→NE→SW) across the entire dataset — SE is the "if ever" quadrant.** No instance in this corpus unlocked quadrants out of this order, and only the aggressive 4-quadrant minority (#28) ever reaches SE at all, always last. Confidence: **very high.** Practically: you can usually predict which physical part of the board an opponent will expand into next without needing to observe their actual `BUY_LAND` action.

41. **Animal count is a near-perfect proxy for "is this the standard clone" vs. everything else.** Any opponent holding more than 1 cow or more than 1 sheep at any point falls completely outside both the main clone (#10) and the budget fork (#19) — in this dataset, herd-scaling beyond 1-of-each simply doesn't happen among the top-tier bots. If you see 2+ of the same animal, you are looking at a genuinely different (and likely less common/more experimental) opponent. Confidence: **very high (0/418 clone+fork instances scaled a herd).**

42. **Strawberry tile count at day 29 is a reasonable proxy for "how committed is this opponent to the standard playbook."** 4–7 tiles = mainline clone behavior (69%+ of clones); 0 tiles at endgame (crops fully cleared) correlates strongly with either the broken-bot pattern (#32) or an animal-only endgame — worth checking crop tiles specifically, not just animal tiles, before concluding an opponent has "no crop income."

43. **Second-quadrant purchase day is your fastest single early-game classifier.** Day 7 → mainline clone (or a near-clone with an unusual opening crop, see #33). Day 10 → almost certainly the budget fork (Section B) or a land-conservative deviant. Any other day, or never → genuinely atypical opponent, worth extra scouting before committing a counter-strategy. Confidence: **high**, and this alone is checkable earlier (day 7–10) than most other signals in this list.

44. **Across 133 distinct named accounts, real strategic diversity is concentrated in under 10% of the field.** Practically: build your primary opponent-detection logic around confirming/ruling out the Section A fingerprint first (cheap, observable by day 7–10), fall back to Section B's fingerprint second, and only invest in more expensive per-opponent modeling for the residual ~5–7% that clears both filters. Confidence: **very high, this is a direct restatement of the 410/440 + 8/440 split** and should shape how much engineering effort your detector spends on the long tail vs. the head.

---

## Practical takeaway for your detector

Given how concentrated this field is, the highest-leverage detector isn't 44 independent checks running in parallel — it's a short decision path: (1) check for simultaneous COW+SHEEP + pasture build on day 0 → if yes, you're very likely facing Section A, predict the rest of their game from items 1–18; (2) if day 0 shows COW-only with no sheep, watch for a day-10 (not day-7) second land purchase to confirm Section B; (3) anything that clears both checks gets flagged for the Section C/D signals, which are individually weaker but still each above your 70% bar except where explicitly marked otherwise (#26, #30, #32 are noted as low-sample and should be weighted down accordingly in any scoring function).
