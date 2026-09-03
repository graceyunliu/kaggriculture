# Sep 2 — evaluator built, frontier tape built, V3.11 gap decomposed

## What was built (all in the Kaggriculture project folder)

**`mini_engine.py`** — runs the vendored engine with no `kaggle_environments` install (shims the one import). ~1.3 s/game, parallel, cached, both-seats paired evaluation, per-day trace for both players (money, hands at end of day, animals, land, shed, per-item sales and buys with realized prices). Picks the engine: `--engine master` (the ladder engine) or `1.32`.

**`replay_verify.py`** — feeds a recorded ladder episode's actions through the local engine and checks money step by step. Two recent ladder replays reproduce **exactly** (max diff $0). So: the shim is faithful, `vendor/kaggle_environments_engine_master` is what the ladder runs, and the engine is deterministic given (seed, actions).

**`make_tape_agent.py`** — turns any replay + seat into a replay-tape opponent (720-entry action list, zlib+b85), the same construction the public "2900+", "V16-RC5", and "V14 Clone Preemption" notebooks ship. Tapes in `Opponents/`: `tape_yuan800_104892947` ($122k in source), `tape_atakan_104893687` ($107k), `tape_curiosity_104893687` ($116k), `tape_icelemon_104892947`. A tape pair from one replay reproduces that replay's money exactly.

**`candidates/V3_11.py`, `candidates/V3_12.py`** — copied from the ChatGPT lineage so both folders' agents run under one harness.

## Findings

**1. The ladder frontier is literally tapes.** The top public notebooks are `_ACTIONS` lists replayed turn by turn. That is why five "players" share one day-0 order sequence to the unit, and why mirror matches end $8 apart. A tape against itself ties to the dollar in both seats on this engine (no seat bias for identical action streams).

**2. Game-level money variance is seed alone.** All recent replays carry one identical configuration. The same tape pair scores $64k / $85k / $101k / $107k on seeds 2 / 3 / 1 / 646805430 — town-shop draws and weeds do the rest. The evaluator must average over seeds; a config sweep is unnecessary.

**3. V3.11 loses to every frontier tape, 0-30, by ~$45k/game.** Ten seeds, both seats:

| opponent | V3.11 mean | tape mean | margin/game | t |
|---|---|---|---|---|
| tape_yuan800 | $54.9k | $100.6k | −$45.7k | −8.5 |
| tape_atakan | $55.2k | $99.7k | −$44.5k | −12.4 |
| tape_curiosity | $46.2k | $90.6k | −$44.4k | −10.2 |
| (control) opp_scenario_v14 | $83.3k | $73.7k | +$9.6k | 1.4 |
| (control) v10.6 | $112.9k | $52.0k | +$60.9k | 6.8 |

The controls confirm the harness (V3.11 beats the August clone and v10.6 as memory records). Tape vs tape (yuan vs atakan): +$3.7k, 8-2 — the ladder's own margin scale.

Note the market coupling: V3.11 makes $113k against v10.6, $83k against the August clone, $55k against the frontier tape. Its income is set largely by what the opponent sells into the shared market.

**4. Where the $46k goes (10-seed mean, V3.11 vs tape_yuan800, same market).**

| item | V3.11 units / $ / avg price | tape units / $ / avg price | revenue gap |
|---|---|---|---|
| WHEAT | 3 / $154 / $51 | 416 / $19,078 / $46 | **−$18.9k** |
| STRAWBERRY | 270 / $22,711 / $84 | 269 / $35,421 / $132 | **−$12.7k** |
| MILK | 162 / $9,934 / $61 | 214 / $18,113 / $85 | −$8.2k |
| FERTILIZER | 245 / $11,487 | 321 / $16,428 | −$4.9k |
| MELON | 100 / $12,604 / $126 | 72 / $17,440 / $242 | −$4.8k |
| EGG | 0 | 64 / $4,073 | −$4.1k |
| WOOL | 208 / $29,570 / $142 | 138 / $17,209 / $125 | +$12.4k |
| sales total | | | −$41.9k |
| buys: WHEAT | 317 units, $14,045 ($44/u) | 374 units, $8,336 ($22/u) | −$5.7k |
| buys: other | more strawberry seed, more sheep | fertilizer $2.9k, 2 geese | −$0.4k |
| **total** | **$54.2k** | **$100.2k** | **−$46.0k** |

Mean sale day (units-weighted): MILK 22.4 vs 19.1, WOOL 20.6 vs 18.9, STRAWBERRY 24.8 vs 21.8, MELON 13.4 vs 10.2. V3.11 sells every perishable ~3 days later than the tape, into prices that fall monotonically all game (milk $195 on day 8 → $5 on day 29; strawberry $220 → $74; melon $246 on day 10 → $87 by day 14). Wheat is the one price that *rises* (town demand drains it: $30 → $53), which is why the tape grows ~400 units and dumps 112 of them on day 29.

So the gap is three mechanisms, in order:

- **Wheat economy, ~$25k.** Grow wheat instead of buying feed; buy the little you need early when it's $22, not $44; sell the surplus late as the price climbs. V3.11 never plants wheat.
- **Sell timing on perishables, ~$20k.** Same units of strawberry, fewer of milk/melon, sold three days later into a collapsing price. This is deposit/sale latency — the DROP lifecycle ChatGPT flagged — plus first-mover advantage in the shared market (the tape's 60 melons on day 10 at $246 knock V3.11's day-11 batch to $182 and its day-14 batch to $87).
- **Early herd / eggs / fertilizer, ~$10k.** 4 animals on day 0 and 10 by day 7 produce fertilizer and milk earlier; two geese add $4k; buying $2.9k of fertilizer to apply is net positive.

Offsetting: V3.11's 8 sheep vs 5 earn +$12k of wool — the one thing it does better.

## What this changes

The bar is a tape, and we can now evaluate against it in 10 seconds per 20 games. The discovery bundle is no longer a guess: wheat production + same-day selling + all-in day-0 herd, on the V3.11 chassis. The labor-per-obligation/routing hypothesis is not what the decomposition points at first — sell latency and crop choice are — so the oracle-bound planner experiment can wait.

Seed set for candidates: 1–10 are now the dev set (used here); hold out 11–30 and never tune on them.
