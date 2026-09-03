# Sep 2 frontier refresh — independent review of ChatGPT's V3.13 corpus

Source: `~/Documents/ChatGPT/Kaggriculture/artifacts/v3_13/top_ladder_replay_refresh.json` (33 games, 66 trajectories, 48 from live top-10 players) and the vendored GitHub-master engine.

## Findings that change the picture

**1. The frontier is no longer $130–141k/game.** Game-level mean money in this corpus runs $49.6k–$153k, and it is dominated by the game (seed/config), not the player. Winners' mean $95.7k, losers' $82.1k. V3.11's reference game ($91.7k) sits in the middle of that distribution. The old $130k+ tapes came from a different era/config.

**2. Top-of-ladder games are near mirror matches.** Median absolute margin $3.9k (5.4% of pot); 12 of 32 decided games under $3k; 5 under $1k; one at $8 (Mohammad 49,561 vs Atakan 49,553). Winner seat split 16/16. Within the top-10, winners' and losers' median trajectories (hands, animals, land, cash by day) are indistinguishable through day 20. So "successful vs failed copies" is mostly who-played-whom plus seat, not a survival mechanism — except for the outright collapses (Mohammad's $0 game; Atakan's herd collapse), which are real failure modes but rare. Crop Dusta wins 5/7 with 6.4 deaths/game — churn is tolerated.

Consequence: our engine's ~$2.7k seat bias is the same size as a typical ladder margin. Against a clone, the seat can decide the game. The bar is "beat the frontier script in *both* seats by more than the seat bias," not "make more money."

**3. The 53-buy / 48-sell wheat cycle is a fingerprint, not a mechanism.** Engine quotes BUY_PRODUCT at post-buy inventory ("so a buy/sell round-trip nets zero"). Computed on the price curve (WHEAT: 25 + √deficit): buy 53 then sell 48 costs $133 — exactly the cost of buying 5 wheat directly. It exists because turn 2 already carries the full 10-order cap (SELL, COW, SHEEP, 5×HIRE, WHEAT seed, MELON seed). This is why V3.14 (the cycle alone) could only be a wash-or-loss; nothing to learn from it beyond "it's the same notebook."

**4. The opening is all-in, and hands are almost free.** Frontier hour-2 spend: 2 COW $800 + 2 SHEEP $1,000 + 5 HIRE $12 + 7 WHEAT seed $70 + 12 MELON $960 = $2,842, plus $133 feed = $2,975 of $3,000. V3.11 spends $2,157 at hour 1 and holds $843. Hire cost is fib: $1,1,2,3,5,8,13,21,34,55,89 — 11 hands costs $232/day, 7 costs $33/day. The marginal 8th–11th hand costs $21–$89/day.

**5. The trajectory gap is a 3–5 day earlier herd and labor ramp.**

| day | 0 | 1 | 2 | 3 | 5 | 7 | 10 | 15 | 20 | 25 | 29 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| frontier animals (median) | 4 | 4 | 5 | 5 | 6 | 10 | 15 | 16 | 16 | 16 | 15 |
| V3.11 animals | 2 | 3 | 3 | 3 | 3 | 3 | 11 | 15 | 15 | 14 | 14 |
| frontier hands | 5 | 4 | 4 | 5 | 4 | 8 | 11 | 11 | 12 | 11 | 11 |
| V3.11 hands | 3 | 3 | 3 | 3 | 3 | 4 | 7 | 10 | 8 | 13 | 6 |
| frontier cash | 29 | 88 | 178 | 274 | 52 | 338 | 14.5k | 25.5k | 48.6k | 70.7k | 89.8k |
| V3.11 cash | 843 | 89 | 111 | 105 | 186 | 742 | 47 | 12.8k | 31.7k | 63.7k | 91.7k |

Both are cash-constrained days 0–9. The frontier reaches 10 animals by day 7 (V3.11: 3) and 11 hands by day 10 (V3.11: 7); its cash lead is ~$15k from day 10 through day 20; V3.11 closes it by day 29 with a steeper late slope (melon lump at day 10–15, strawberry later). The early ramp must be funded by early product income (wheat harvest days 2–4, wool day 6+, fertilizer) compounding from the larger day-0 herd — measurable from the raw replays but not in the summary JSON.

Movement rate: frontier 0.44–0.45 of unit-turns, V3.11 0.52, with 11 hands vs 7.

## What this says about next steps

- The frontier opponent for the evaluator should be a tape/script from this corpus (Dmitry or cygn), not the August tapes. If the opening is a shared public notebook — five players with identical day-0 orders says it is — find and extract the source rather than reverse-engineering.
- The discovery bundle is: all-in hour-2 opening (2c/2s/5 hands/7 wheat/12 melon) + herd ramp to ~10 by day 7 + hands to 11 by day 10, as one block on the V3.11 dispatcher. The old clone-replica failure (staged herd on v10.6) is the risk; V3.11's labor model is the reason to expect a different outcome.
- Game-level money varies 3× across episodes. Check whether the ladder varies config per episode (townCenterSellInterval etc.) or whether this is seed alone; the local evaluator must sample whatever the ladder samples.
- Success-vs-failure diffs within the frontier are not informative (mirror matches). The informative diffs are frontier-vs-V3.11 on the same seed, and the rare collapse games.
