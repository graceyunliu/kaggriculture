# M3 general opening sizing — negative result

`candidates/M3_GENERAL_SIZING.py` keeps H32/M2's tape and divergence guard, but replaces M2's opponent-purchase classifier and three-entry sell table. At turn 1 it reads only the live wheat inventory/price, our cash and wheat, and our own recorded purchase plan. It mirrors the engine's documented wheat price curve and integrates the proceeds of selling one unit at a time, because each sale changes the next unit's quote. It then sells the smallest quantity that funds our turn-1 purchases while reserving one day's feed for animals owned or bought in that action plus the chassis's one-unit operational buffer. Thus the quantity responds to price impact and our financing need rather than reconstructing an opponent's turn-0 order. In the evaluated games the rule selected 23 or 24 units, depending on the visible market and our cash.

## Method

The rule and constants were frozen from the master engine's `MARKET_PARAMS["WHEAT"]`, animal/seed/hire prices, and M3's own action plan before running any opponent evaluation. No listed tape was run or inspected to tune the formula. Only after the implementation was frozen was it evaluated with `mini_engine.evaluate()` on the master engine, seeds 11–30, both seats. W-L below counts paired seeds (the two seat margins summed), matching `mini_engine.evaluate()`.

## Never touched during development

| opponent | M3 margin/game | t | W-L | H32 margin/game | M3 − H32 |
|---|---:|---:|---:|---:|---:|
| V3_12 | +$36,390 | 11.89 | 20-0 | +$45,527 | −$9,137 |
| E1 | +$32,975 | 10.49 | 20-0 | +$32,636 | +$339 |
| C1 | +$32,506 | 12.30 | 20-0 | +$33,273 | −$767 |
| H10 | +$27,238 | 14.97 | 20-0 | +$27,222 | +$16 |

This is not a meaningful general improvement over H32's fixed sell of 25. Averaged equally across these four opponents, M3 is $2,387/game worse, driven mainly by the V3_12 regression. Per the stopping rule, no post-result tuning was performed and this candidate should not replace H32.

## Opponents used to build M2 (do not use these to tune)

| opponent | M3 margin/game | t | W-L | published M2 margin/game |
|---|---:|---:|---:|---:|
| tape_yuan800 | +$3,550 | 2.30 | 10-10 | +$65,911 |
| tape_atakan | +$6,264 | 4.33 | 18-2 | +$147,315 |
| tape_strawhats | +$67,357 | 17.89 | 20-0 | +$109,345 |
| tape_kiro | +$23,028 | 10.73 | 20-0 | +$23,027 |
| tape_antigone | +$10,042 | 5.44 | 20-0 | +$14,589 |

As expected, the general rule gives up most of M2's fitted advantage against yuan800, atakan, and strawhats. The much smaller results are reported deliberately rather than using those tapes to recover the old thresholds.

## Verification

- `python3 -m py_compile candidates/M3_GENERAL_SIZING.py`: passed.
- All nine evaluations completed with zero candidate errors.
- Two uncached runs of M3 vs V3_12 at seed 17 produced identical full result/trace data (excluding elapsed time): final money `$68,882` vs `$27,051`, 719 steps.
- `replay_verify.py` reproduced `episode-101822124-replay.json` exactly on the master engine: no first divergence, maximum absolute difference `$0`, and final money `$79,889` / `$84,636` matched. This confirms the engine/shim determinism used by the unchanged tape/guard machinery.
