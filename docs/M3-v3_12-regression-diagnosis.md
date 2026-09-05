# M3 vs V3_12 regression diagnosis

## Conclusion

Classification: **(b), genuine tradeoff**. M3's smaller turn-1 sale does not leave M3 short of cash, cancel any opening purchase, delay a hire, or cause an unfed animal. It changes the shared wheat inventory by one unit, which pushes V3_12 across a discontinuity in V3_12's own adaptive crop allocator on day 1. The resulting opponent crop plan changes later herd growth and the shared product-price paths. Selling 25 happens to steer this particular policy onto a less profitable branch on average; choosing 25 for that reason would recreate the opponent-response fingerprinting that M3 was designed to remove. No candidate change is made.

## Instrumentation and matched trajectories

I monkeypatched `mini_engine.load_agent` following `tools/sell_shift.py::shed_trace` and captured, before every action, cash, wheat market inventory and price, shed wheat, hires, animals, `fed_today`/`consecutive_unfed`, private seed inventory, and the complete returned action. I compared M3-vs-V3_12 with H32-vs-V3_12 for identical seeds and seats. Detailed traces were inspected for seeds 11, 12, 15, 17, 20, 26, and 29 in both seats; seeds 11–30 were also rerun both seats with `--no-cache` to confirm the aggregate result.

The opening difference is stable across the inspected cases:

| observation/action point | M3 | H32 |
|---|---:|---:|
| turn 1 wheat sale requested | 24 | 25 |
| turn 2 M3/H32 cash after all opening orders | $16 | $44 |
| turn 2 M3/H32 shed wheat | 6 | 5 |
| turn 2 shared wheat inventory | 9,988 | 9,989 |
| missed turn-1 purchases | none | none |

The extra H32 sale receives $28. M3's modeled minimum of 24 is therefore sufficient to execute the entire ten-order opening; the 25th unit provides idle cash rather than unlocking another own purchase. M3 retains that unit as feed inventory. Through the inspected opening, both versions make the same hire and feed requests and show the same unfed/consecutive-unfed counts. Across the representative seeds, M3's focal requested actions are identical to H32's from turn 2 through turn 718; later state differences arise from market execution and prices, not a different taped decision.

## Causal chain

The first downstream policy divergence is on V3_12's side at turn 25 (day 1, hour 1):

| live input / V3_12 output | versus M3 | versus H32 |
|---|---:|---:|
| V3_12 cash | $1,079 | $1,080 |
| shared wheat inventory | 9,985 | 9,986 |
| displayed wheat price | $29 | $29 |
| seed orders | 3 carrot + 1 wheat | 4 carrot |

Although the rounded displayed price is equal, V3_12's allocator uses the live inventory reservoir and its cash/reserve calculation. The one inventory unit and one dollar difference cross a discrete affordability/allocation boundary. At turn 38 V3_12 consequently plants wheat against M3 but carrot against H32. At turn 49 it requests a carrot seed against M3 but a wheat seed against H32, and at turn 55 it again plants carrot versus wheat. From there its adaptive crop, herd, and market decisions separate.

This is amplified because both agents trade into the same nonlinear markets. Concrete examples:

- Seed 15, focal seat 0: M3 itself finishes at $156,238 versus H32's $100,800, but V3_12 finishes at $110,031 versus $40,825. V3_12 reaches 20 animals against M3 versus 14 against H32. M3 gains $55,438, but its opponent gains $69,206, so relative margin is $13,768 worse.
- Seed 20, focal seat 0: M3/H32 finish at $155,230/$140,542, while V3_12 finishes at $152,503/$106,150. The opponent-side gain dominates and reduces the margin by $31,665.
- Seed 26, focal seat 0: M3/H32 finish at $93,259/$133,167, while V3_12 finishes at $84,356/$77,921. Different shared milk, wool, and strawberry price paths hurt M3 as well as helping V3_12; the margin is $46,343 worse.

The direction is not consistent seed by seed. For example, on seed 11 seat 0 the same branch raises M3's relative margin from $36,156 to $53,053. Random town/shop schedules determine whether the alternate V3_12 crop/herd path is valuable. This variance is why a few-seed inspection can suggest the opposite conclusion even though the complete paired evaluation shows the reported regression.

Across seeds 11–30 and both seats, the fresh evaluation reproduces the original totals:

| candidate vs V3_12 | candidate money/game | V3_12 money/game | margin/game | t | W-L |
|---|---:|---:|---:|---:|---:|
| M3 | $111,872 | $75,482 | +$36,390 | 11.89 | 20-0 |
| H32 | $106,421 | $60,894 | +$45,527 | 18.75 | 20-0 |

M3 actually earns **$5,451/game more itself** than H32. Its reported relative regression occurs because V3_12 earns **$14,588/game more**, yielding the net −$9,137/game margin difference. That decomposition rules out the proposed own-cash-shortfall explanation.

## Why no fix is legitimate

M3's financing rule does what it claims in the observed state: it integrates its own sale proceeds along the wheat curve, sells the minimum needed to fund every planned purchase, and retains feed. There is no generally excessive reserve exposed by this matchup. The only demonstrated benefit of selling the additional unit is that V3_12's private policy reacts badly to the resulting public state. An arbitrary extra-cash buffer or a branch keyed to inventory 9,985/9,986 would be a disguised V3_12-opening detector, not a correction to M3's valuation.

Because the cause is classification (b), the candidate was left unchanged and no nine-opponent retuning/evaluation was performed.

## Determinism check

`replay_verify.py` reproduced `episode-101822124-replay.json` exactly on the master engine: no first divergence, maximum absolute difference $0, and final money $79,889 / $84,636 matched. The tape/guard machinery remains unchanged.
