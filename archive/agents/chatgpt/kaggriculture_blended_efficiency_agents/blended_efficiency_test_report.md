# Blended efficiency agents — test report

## Method

- Base: `main_v8.3.py`.
- Every challenger combines turn, land, and labor efficiency changes.
- Screening: seed 42, 720 turns, both seats.
- Validation: seeds 1, 7, 42, 99, 123, 720 turns, both seats for the three strongest screens.
- All agents compiled and completed without crashes.

## Screening results

| Rank | Agent | Policy | Margin |
|---:|---|---|---:|
| 1 | `blend_01_balanced8_compact.py` | 8 hands, modest land delay, original portfolio | +19,315 |
| 2 | `blend_04_balanced9_compact.py` | 9 hands, compact land, original portfolio | +15,713 |
| 3 | `blend_19_nine_diverse_compact.py` | 9 hands, compact diversified crop and mixed fleet | -8,344 |
| 4 | `blend_02_balanced8_no_fert.py` | 8 hands, modest land delay, skip fertilizer logistics | -10,664 |
| 5 | `blend_14_nine_smallfleet_compact.py` | 9 hands, small mixed fleet, compact land | -15,075 |
| 6 | `blend_11_cropguard8_compact.py` | 8 hands, compact land, stronger crop protection | -15,150 |
| 7 | `blend_05_balanced10_compact.py` | 10 hands, compact land, original portfolio | -20,180 |
| 8 | `blend_16_eight_latecare_compact.py` | 8 hands, delay care until production ramp | -24,994 |
| 9 | `blend_09_smallcow8_compact.py` | 8 hands, compact land, small cow-only fleet | -26,023 |
| 10 | `blend_12_animallean8_compact.py` | 8 hands, compact land, animal-oriented allocation | -26,639 |
| 11 | `blend_07_melon8_compact.py` | 8 hands, compact land, melon batch core | -27,804 |
| 12 | `blend_10_smallmixed8_compact.py` | 8 hands, compact land, shorter mixed expansion | -28,022 |
| 13 | `blend_03_balanced8_altcare.py` | 8 hands, modest land delay, alternate care | -30,240 |
| 14 | `blend_15_ten_smallfleet_compact.py` | 10 hands, small mixed fleet, compact land | -30,285 |
| 15 | `blend_17_eight_straw_melon_compact.py` | 8 hands, compact premium crop blend | -31,763 |
| 16 | `blend_06_ongoing8_compact.py` | 8 hands, compact land, ongoing crop core | -36,408 |
| 17 | `blend_20_eight_austerity_balanced.py` | 8 hands, strict compactness, reduced optional work | -51,178 |
| 18 | `blend_13_nine_altcare_compact.py` | 9 hands, alternate care, compact land | -51,924 |
| 19 | `blend_08_wheatcow8_compact.py` | 8 hands, compact land, wheat-fed cow fleet | -66,830 |
| 20 | `blend_18_eight_melon_cow_compact.py` | 8 hands, melon emphasis, cow-only small fleet | -77,443 |

## Five-seed validation

| Agent | W-L-T | Mean margin | Rough 95% CI |
|---|---:|---:|---:|
| `blend_01_balanced8_compact.py` | 3-2-0 | +7,828 | [-7,866, +23,522] |
| `blend_04_balanced9_compact.py` | 3-2-0 | +4,972 | [-4,931, +14,875] |
| `blend_19_nine_diverse_compact.py` | 0-5-0 | -29,440 | [-49,629, -9,251] |

## Conclusion

The balanced eight-hand and nine-hand variants are the only positive candidates. The eight-hand variant is stronger on this sample. Both preserve v8.3 crop, animal, care, fertilizer, and land behavior; their effective change is the constrained labor target. The diversified nine-hand agent failed, so production-mix changes did not compound the labor gain.

Neither positive interval excludes zero, so v8.3 remains the statistically validated champion pending a 15-seed validation.