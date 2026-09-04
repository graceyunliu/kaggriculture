# H31 guarded full-tape results (Sep 4)

H31 is H30 with one behavioral change: the money-divergence guard now exits the recorded tape only when live cash is more than 75% below the recorded cash, rather than 50% below. Animal and hand-count guards are unchanged. An a65aa fallback experiment added no supported value (+$17/game, t=1.00 versus the one-line variant) and was excluded.

Development seeds 1-5 selected the 75% threshold from a small guard grid. All confirmation below used the frozen one-line candidate, both seats, master ladder engine, cache disabled, and zero agent errors.

## Untouched confirmation against H30

| seeds | margin/game | t | seed W-L |
|---|---:|---:|---:|
| 2001-2030 | **+$1,290** | **2.57** | 6-0 (24 ties) |
| 2031-2060 | **+$1,266** | **2.29** | 5-0 (25 ties) |

The many exact ties are expected: H31 and H30 execute identical actions unless the money guard would have fired between the old and new thresholds.

## Safety set, untouched seeds 2001-2030

| opponent | margin/game | t | W-L |
|---|---:|---:|---:|
| H10 | +$29,761 | 18.29 | 30-0 |
| H11 | +$29,766 | 18.29 | 30-0 |
| tape_strawhats | -$103 | -0.16 | 15-15 |
| tape_yuan800 | +$3,941 | 3.07 | 19-11 |
| tape_atakan | +$5,512 | 3.45 | 20-10 |
| tape_shirabe | +$22,558 | 13.07 | 30-0 |
| tape_antigone | +$18,920 | 9.45 | 30-0 |
| tape_kiro | +$27,386 | 14.98 | 30-0 |

H31 replaces H30 as the strongest validated ladder candidate. It is replay-based, like H30; it is not an own-code replacement. a65aa remains the strongest validated replay-free candidate from this search line.
