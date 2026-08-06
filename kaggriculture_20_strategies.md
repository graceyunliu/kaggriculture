# Kaggriculture: 20 Strategies for $50+/Tile/Day

All numbers below are computed directly from the game's actual formulas (`kaggriculture.py`), simulated day-by-day over a 30-day season. "$/tile/day" = net profit (revenue minus seed/animal/feed/fertilizer cost) divided by total tile-days the land was occupied, including any fallow days at the end of the season where a new cycle wouldn't finish in time.

**Read this before trusting the numbers as a promise, not just a plan:**

- Every calculation uses each item's *base* market price (its starting price at inventory level 10,000). Real prices fall the more you sell — premium goods (wool, milk, melon, strawberry) crash especially hard on repeated selling. Strategies built around heavy sheep/cow/melon output will earn less than shown once you're actually dumping that much product — pace your sales, don't dump it all in a single burst.
- These are land-efficiency numbers, not turn-efficiency or hand-efficiency numbers. Running several of these tiles at once requires enough turns (and likely hired hands) to actually execute the daily watering/feeding/care routine on all of them.
- "Ongoing" crops (tomato, strawberry) do **not** produce forever — they cap at `max_yield` (4) total production events, then start decaying like any other crop. Budget a replant, not an indefinite income stream.
- Fertilizer is not automatically good. It's a net loss to buy for wheat, carrot, or melon — melon in particular reaches its max yield through watering alone, no fertilizer required. It only pays off when it's free (an animal's `COLLECT_FERTILIZER` byproduct) or on a crop where it shortens a long ongoing-crop cycle (tomato, strawberry).
- Animals never expire on their own — only crops do. As long as you avoid two consecutive missed feedings, an animal keeps producing indefinitely.
- The single most powerful lever in the game is the animal `CARE` action: caring for an animal on top of feeding it banks a bonus that keeps growing every day between production ticks, then pays out in full on the next tick. Longer-interval animals (sheep, every 3 days) benefit the most because the bonus has more days to compound.

---

## Ranked Summary

| # | Strategy | Category | Tiles | $/tile/day |
|---|---|---|---|---|
| 1 | Full daily-care sheep ranch | Pure animal, max effort | 1 | $211.67 |
| 14 | Cow + sheep dual ranch | Premium dual-animal | 2 | $190.67 |
| 2 | Full daily-care cow ranch | Pure animal, max effort | 1 | $169.67 |
| 18 | Delayed-start sheep (carrot bootstrap) | Temporal sequencing | 1 | $169.00 |
| 3 | Triple-animal ranch (goose+cow+sheep) | Diversified ranch | 3 | $146.56 |
| 20 | Goose + sheep dual ranch | Budget+premium pairing | 2 | $135.00 |
| 17 | Melon + full-care cow | Power pairing | 2 | $132.17 |
| 11 | Sheep + free-fert carrot | Crop+animal synergy | 2 | $125.83 |
| 12 | Sheep + free-fert tomato | Crop+animal synergy | 2 | $115.33 |
| 4 | Carrot → melon staggered (same tile) | Staggered single-tile | 1 | $100.33 |
| 5 | Wheat-feeds-cow | Crop+animal synergy | 2 | $95.33 |
| 6 | Pure melon monoculture | Pure crop | 1 | $94.67 |
| 16 | 4-way diversify (wheat+carrot+melon+sheep) | Max diversification | 4 | $88.92 |
| 19 | Town-demand portfolio (wheat+cow+goose) | Market-aligned | 3 | $83.00 |
| 13 | Melon + full-care goose | Diversified, budget animal | 2 | $76.50 |
| 15 | Efficient-sheep + melon | Balanced effort | 2 | $76.09 |
| 9 | Melon + carrot (risk hedge) | Diversified crop | 2 | $61.50 |
| 10 | Melon + sheep-fert strawberry | Crop+animal synergy | 2 | $60.00 |
| 7 | Full daily-care goose coop | Pure animal, low capital | 1 | $58.33 |
| 8 | Efficient every-other-day cared sheep | Pure animal, low effort | 1 | $57.50 |

---

## The Original 10

### 1. Full daily-care sheep ranch — $211.67/tile/day
Day 0: `BUILD_PASTURE`, `BUY_ANIMAL SHEEP`, `PLACE`. Every day after: `FEED` + `CARE`, no exceptions. Harvest immediately the instant production posts — every 3rd day starting day 6. The `CARE` bonus banks +1 every day fed *and* cared for, and keeps accumulating across the whole 3-day gap between ticks — that's why sheep, with the longest interval of the three animals, produces the biggest single-item payout in the game.

### 2. Full daily-care cow ranch — $169.67/tile/day
Same discipline as sheep: `BUILD_PASTURE`, `BUY_ANIMAL COW`, `PLACE` day 0; feed+care every day; harvest on every 2-day production tick starting day 8. Cheaper animal ($400 vs $500) and shorter interval means a smaller bonus per tick, but more frequent payouts.

### 3. Triple-animal ranch (goose + cow + sheep) — $146.56/tile/day
Build a coop and two pastures. Buy and place one of each animal on day 0. Feed and care for all three, every day, for the whole season. Diversifying across egg/milk/wool avoids flooding any single market, and multiple town shops buy each of these three goods, which helps hold prices up.

### 4. Carrot → melon staggered (same tile) — $100.33/tile/day
Days 0–3 and 3–6: two carrot cycles (plant, water daily, harvest day 3, replant same day) for early cash. Day 6: switch to melon (plant, water daily, harvest day 18, replant, harvest again day 30). No fertilizer used — melon hits its cap from watering alone.

### 5. Wheat-feeds-cow (2-tile synergy) — $95.33/tile/day
Tile A: wheat on repeat — plant day 0, water daily, harvest day 4, replant immediately, repeat for the whole season. Tile B: cow, daily fed + cared per strategy #2. Feed the cow directly from tile A's wheat harvest instead of buying wheat at market — this is even better than the modeled number, since it removes the feed cost entirely.

### 6. Pure melon monoculture — $94.67/tile/day
Day 0: `BUY_SEED MELON`, `PLANT`. Water every day. Day 12: `HARVEST` (6 units), replant same day. Repeat — two full cycles fit in 30 days. Skip fertilizer; it drops this to $48/tile/day since melon already reaches its yield cap through watering alone.

### 7. Full daily-care goose coop — $58.33/tile/day
Cheapest animal buy-in ($300). Same daily feed+care discipline as sheep/cow. Harvest daily starting day 4 (goose has a 1-day interval). A good entry point if you don't yet have $500 for a sheep.

### 8. Efficient every-other-day cared sheep — $57.50/tile/day
Feed and care every *other* day instead of daily — the minimum cadence that avoids the animal escaping (2 consecutive missed feedings triggers escape). Cuts feed cost in half versus strategy #1 and still clears $50 — useful if you're short on turns or hands.

### 9. Melon + carrot (risk hedge) — $61.50/tile/day
Run both on separate tiles: melon per #6, carrot per its own repeating 3-day cycle (plant, water, harvest day 3, replant). Carrot alone doesn't clear $50, but it's more forgiving on price gluts than melon, so blending gives you a cheaper, faster-cycling safety valve if you need to dump inventory quickly.

### 10. Melon + sheep-fert strawberry — $60.00/tile/day
Melon on one tile. On a second tile, use `COLLECT_FERTILIZER` from an animal you're running elsewhere to fertilize strawberry for free, shortening its cycle from 17 to 13 days. Strawberry alone only earns about $25/tile/day, but blended with melon it clears $50 while giving you a second, different product to sell.

---

## 10 More

### 11. Sheep + free-fert carrot — $125.83/tile/day
Tile A: full daily-care sheep (per #1). Tile B: carrot, fertilized for free using the sheep's `COLLECT_FERTILIZER` byproduct instead of buying fertilizer at market. One free fertilizer application (applied on day 2, covering days 2–4) pushes carrot to its 4-unit cap; carrot's rate alone jumps from $28/tile/day (unfertilized) to $40/tile/day (free-fertilized). Blended with sheep, the pair clears $125/tile/day.

### 12. Sheep + free-fert tomato — $115.33/tile/day
Same idea as #11, but the second tile runs tomato instead of carrot. Free fertilizer applied once (day 7, covering days 7–9) shortens tomato's cycle from 12 to 10 days, lifting its solo rate from $12.67 to $19/tile/day. Good if you'd rather diversify into tomato (wanted by 3 different town shops) than carrot.

### 13. Melon + full-care goose — $76.50/tile/day
Melon on one tile, a daily-fed-and-cared goose coop on a second. Pairs the strongest pure crop with the cheapest animal that clears $50 on its own — a lower-capital alternative to pairing melon with cow or sheep.

### 14. Cow + sheep dual ranch — $190.67/tile/day
Two pastures, no crop tiles at all — one cow, one sheep, both fed and cared for every day. The second-best pure-animal combination in this list, just behind running two sheep tiles (which isn't listed separately below, but would land close to $211.67 itself since it's the same recipe doubled).

### 15. Efficient-sheep + melon — $76.09/tile/day
Melon on one tile, the *efficient* every-other-day-cared sheep (per #8) on the other, instead of the full daily-care version. Lower total labor than pairing melon with a full-effort sheep, while still clearing $50 comfortably.

### 16. 4-way diversify (wheat + carrot + melon + sheep) — $88.92/tile/day
Four tiles: wheat repeating every 4 days, carrot repeating every 3 days, melon repeating every 12 days, and a full daily-cared sheep. The rate lands below the best 2-tile pairings, but this is the widest hedge against a price crash in this list — no single good is more than a quarter of your output.

### 17. Melon + full-care cow — $132.17/tile/day
Melon on one tile, a full daily-fed-and-cared cow on the other. The strongest pure crop paired with the strongest animal in the $400 price tier — a good "no compromises but not maximum" pairing if $500 for a sheep isn't in the budget yet.

### 18. Delayed-start sheep (carrot bootstrap) — $169.00/tile/day
Same tile, sequenced over time rather than split across tiles: days 0–3 and 3–6, two carrot cycles for quick early cash. Day 6: `BUILD_PASTURE`, `BUY_ANIMAL SHEEP`, `PLACE`; feed + care every day from then on. Even with a 6-day-late start (sheep's first production tick shifts from day 6 to day 12), the season-long rate barely drops from the day-0-start version ($211.67 → $169.00) — proof that prioritizing early cash safety, like we discussed earlier, doesn't meaningfully cost you once the high-value engine gets going.

### 19. Town-demand portfolio (wheat + cow + goose) — $83.00/tile/day
Three tiles: wheat on repeat, a full daily-cared cow, and a full daily-cared goose. Every one of these three goods is wanted by multiple town shops (wheat by four shops, milk and eggs by three each), which cushions their prices against the drops that come from your own repeated selling more than almost any other combination in this list.

### 20. Goose + sheep dual ranch — $135.00/tile/day
A coop and a pasture, both animals daily fed and cared for. Pairs the cheapest entry-cost animal (goose, $300) with the single best per-tile payout (sheep) — a good "budget plus premium" combination if you want exposure to the best strategy without committing two tiles' worth of the most expensive animal.
