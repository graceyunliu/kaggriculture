# What main_v7 Actually Does (Plain English)

This walks through the current agent's logic, turn by turn, in the order the code actually runs it. No code, just what it's instructed to do and why.

## Every turn, in order

### 1. Look at the board

Before deciding anything, it scans my farm and the opponent's farm and sorts what it sees into buckets: tiles that desperately need water (missed a watering already — one more miss and the plant dies), tiles that just need routine water, tiles ready to harvest, empty tiles, weeds, and which of my animal pastures have a live animal on them vs. sit empty. It also scans the opponent's visible crops and flags anything that looks like it's about to be harvestable soon — that's my early warning that a price-crashing wave of their crops is coming.

### 2. Make the money decisions

This is the biggest chunk of logic. Every turn it works through a checklist:

- **Buy a cow, but only once, carefully.** Between day 3 and day 20, if I don't already have a cow or a pasture in progress, and I have enough cash cushion, it buys one cow. It will only ever attempt this 3 times total in the whole game (a safeguard against buying cows forever if something goes wrong with the purchase).
- **Expand land aggressively.** Through day 22, it keeps buying the next quadrant of land as soon as I can afford it — but each successive quadrant costs more, and there's a day cutoff on the pricier ones, so it stops chasing land expansion late in the game when it wouldn't pay off in time.
- **Keep just enough wheat on hand to feed animals.** It calculates exactly how much wheat my animals need to eat, buys only that much (plus a small buffer), and — importantly — never lets that reserved wheat get sold off by accident.
- **Sell fertilizer the moment I have any.** No strategy here, just cash it in immediately.
- **Decide what to sell and how much, carefully.** This is the most nuanced part:
  - It never dumps everything into the market at once — flooding the market crashes the price on exactly the thing I'm trying to sell.
  - It watches for two "attack windows" late in day 10 and day 20 (when town demand spikes) and deliberately holds back strawberries and melons beforehand so it can sell a big batch right as demand peaks.
  - Outside those windows, it sells gradually, aiming to keep prices above a target floor (roughly 70–85% of the item's base price), and it sells more cautiously on premium goods like strawberries and melons than on staple crops.
  - If it sees the opponent has a wave of crops about to mature (from step 1), it lowers its own price floor and sells faster — trying to get ahead of their glut instead of getting caught by it.
  - If I'm behind on cash late in the game, it's willing to hold premium goods a bit longer for a better payoff instead of playing it safe.
  - If storage is getting dangerously full (within 15 of the cap) late in the day, or it's near the end of the season, it overrides all of that nuance and just sells everything — better a mediocre price than losing goods to overflow.
- **Hire more hands.** Once a day, it counts how much work is piled up (watering, harvesting, planting, empty land) and hires up to 18 hands total to match the workload — more open tasks means more hires.
- **Buy seeds.** It prioritizes melon, then carrot, then wheat, buying up to a target amount of each based on how much empty land is available and what phase of the game it is — but always keeps a cash reserve untouched so seed-buying can't leave me broke.

### 3. Run the cow pipeline

This is a multi-step process that has to happen in order, and the agent tracks which step it's on:

1. **Buy the cow** (covered above).
2. **Build a pasture** for it — it picks a tile close to the shed (but not one of the four central shed tiles, since those need to stay clear for pickup/dropoff) and builds there.
3. **Walk to the shed, pick up the cow.**
4. **Walk the cow to the pasture and place it.**
5. Once the cow is settled, it switches into **ongoing daily care mode**: feed it (using wheat carried from the shed), care for it, harvest milk when it's ready, collect fertilizer when available, and periodically walk carried milk/wool/fertilizer back to the shed to drop off. This part isn't a rigid script — every turn it just looks at what the cow currently needs and does that one thing next.

If a step doesn't go as expected (say, the purchase doesn't seem to register), it retries a few times before giving up cleanly rather than getting stuck repeating a failed action forever.

### 4. Everyone else works the farm

Whichever worker isn't busy with cow duty (including the farmer, when free) works down a fixed priority list: water anything that's about to die first, then harvest anything ready, then routine watering, then planting empty land, then weeding. Each worker heads for the nearest available task in that category, and once a worker claims a task, no other worker will also head toward it — so I don't get multiple hands walking toward the same tile. Planting stops late in the day (after hour 21) so nothing gets planted too late to be watered before nightfall, and weeding stops in the last few days of the season since it stops mattering.

### 5. Safety net

If literally anything goes wrong and the code would otherwise crash, it's wrapped so the agent just does nothing that turn instead of losing the whole match on a crash. A bad turn is much better than an automatic loss.

## The short version

Every turn: check what needs attention → decide what to buy, sell, and hire → advance the cow project if it's mid-setup or take care of the cow if it's already set up → send every other worker to the highest-priority open task → never crash.
