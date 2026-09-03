# Kaggriculture efficiency-agent set

Base agent: `main_v8.3.py`

## Measurement definitions

- **Turn efficiency:** expected revenue per scarce unit action. These agents reduce recurring care, fertilizer logistics, replanting, travel, or structure maintenance.
- **Labor efficiency:** expected revenue per hired hand-day. These agents constrain the hand pool and adapt crop/animal policy to that smaller team.

## Turn-efficient agents

1. `turn_01_ongoing_crop_core.py` — strawberry/tomato-heavy; fewer replants.
2. `turn_02_melon_batch_farming.py` — infrequent high-value melon harvest batches.
3. `turn_03_wheat_batch_feed.py` — wheat-first, cow-only, simpler feed loop.
4. `turn_04_minimal_optional_animal_work.py` — no CARE or fertilizer collection.
5. `turn_05_alternate_care.py` — animal care every other day.
6. `turn_06_production_window_care.py` — selective care cadence.
7. `turn_07_compact_farm.py` — delayed land expansion to reduce travel.
8. `turn_08_small_cow_fleet.py` — small cow-only premium fleet.
9. `turn_09_no_fertilizer_logistics.py` — removes fertilizer collection route.
10. `turn_10_crop_only_batch.py` — no animals; melon/strawberry crop batches.

## Labor-efficient agents

1. `labor_01_six_hand_cap.py` — strict six-hand ceiling.
2. `labor_02_eight_hand_cap.py` — eight-hand ceiling.
3. `labor_03_ten_hand_cap.py` — moderate ten-hand ceiling.
4. `labor_04_crop_protected_small_team.py` — eight hands with high crop protection.
5. `labor_05_animal_specialist_small_team.py` — eight hands weighted toward animals.
6. `labor_06_ongoing_crops_eight_hands.py` — ongoing crops under an eight-hand cap.
7. `labor_07_melon_eight_hands.py` — melon-heavy farm under an eight-hand cap.
8. `labor_08_cow_wheat_eight_hands.py` — home-fed cows under an eight-hand cap.
9. `labor_09_alternate_care_eight_hands.py` — eight hands and alternate-day care.
10. `labor_10_four_hand_austerity.py` — extreme four-hand frontier.

## Validation performed

- All 20 scripts compile.
- All 20 completed a 48-turn, seed-42, both-seats engine smoke test against v8.3 without crashes.
- These smoke tests verify mechanics, not full-season economic superiority.
