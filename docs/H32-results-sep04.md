# H32 wheat-round-trip results (Sep 4)

H32 is H31 with one opening change: buy 30 wheat on turn 0 and sell 25 on turn 1, instead of buying only the five wheat needed for feed. The replay, 75% money-divergence guard, count guards, and C1 fallback are unchanged.

The quantity was selected on seeds 1–12 from a grid of 6, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, and 53. Untouched confirmation used both seats, the master engine, cache disabled, and produced zero agent errors.

## Untouched confirmation against H31

| seeds | margin/game | t | seed W-L |
|---|---:|---:|---:|
| 2001–2060 | **+$3** | **33.13** | **60–0** |

The head-to-head edge is deliberately small: the round trip mostly changes the shared wheat price while leaving the replay intact.

## Straw-hats confirmation

H31's weakest safety matchup was essentially even (−$103/game on seeds 2001–2030). H32 won the untouched seeds 2031–2060 by **+$86,428/game**, t=24.40, 30–0.

## Safety set, seeds 2001–2030

| opponent | margin/game | t | W-L |
|---|---:|---:|---:|
| H10 | +$26,811 | 16.89 | 30–0 |
| H11 | +$29,768 | 18.29 | 30–0 |
| tape_yuan800 | +$5,082 | 3.90 | 22–8 |
| tape_atakan | +$5,783 | 3.54 | 20–10 |
| tape_shirabe | +$22,561 | 13.07 | 30–0 |
| tape_antigone | +$15,787 | 9.05 | 29–1 |
| tape_kiro | +$28,029 | 15.69 | 30–0 |

H32 is a credible H31 challenger: it wins the direct paired comparison on every confirmation seed, preserves positive and statistically strong margins across the safety set, and materially fixes the straw-hats matchup. Its tradeoff is about $3k/game less margin than H31 against H10 and antigone, while remaining decisively ahead of both.
