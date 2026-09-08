# Replay Mining + State-Conditioned Policy Audit

> **Provenance correction (added after Phase 4A):** "opponent" / "opp"
> throughout this report means the opposing seat observed inside Grace's
> own replay history (`Replays/Auto/mine/`), not an independently sampled
> leaderboard/ladder reference population. See [INDEX.md](INDEX.md) for
> the full correction and what it does and doesn't affect. Numbers and
> verdicts below are unchanged.

Date: 2026-09-08
Author: Claude (forensic audit agent), on behalf of grace.leeu@gmail.com

## Executive summary

**Final status: PARTIAL_EVIDENCE.**

One recurring, state-conditioned, RNG-independent decision divergence was found
with real support across many independent seeds and opponents: at comparable
day/cash/land/labor states in the mid-game, my games plant STRAWBERRY as the
dominant crop while opponent games plant WHEAT as the dominant crop. This
matches (and gives replay-level, per-decision confirmation of) the
already-known DB-aggregate finding (my avg plant_wheat 24.72 vs opponent
77.09). It is DIRECTLY_OBSERVED at the state->action level, not merely an
outcome correlation, and it is RNG-INDEPENDENT for the "which crop to plant
on an available tile" decision itself (crop selection is a pure policy
choice; it does not read the per-day weed/shop RNG object). It does NOT
explain the residual cash gap reported by the P8 diagnosis — if anything
this audit's raw wheat_frac numbers go the OPPOSITE direction of the P8v2
finding (P8v2 over-planted wheat vs C1/P6; here, "mine" collectively
under-plants wheat vs the opponent field). No divergence in hiring behavior
(hires_today) was found in the sampled data; both cohorts had hires_today=0
at every 24-hour-aligned sample point (see Limitations - this is a sampling
artifact, not evidence hiring never happens).

No robust divergence was found in melon admission timing, fertilizer
apply/hold, or labor-constrained chore prioritization at the granularity
this audit could reach in the time/token budget available — this is
reported as NO_ROBUST_SIGNAL for those sub-questions, not as evidence they
don't exist.

## Phase 1 - Replay inventory (what actually exists)

- Replay files: `Replays/Auto/mine/` (my own games), `Replays/Auto/leaderboard-<opponent>/`
  (14 named-opponent directories), `Replays/Leader Replays/Subin An/`, and
  `Replays/Losses/v*/` (a curated loss set). Total JSON replay files found by
  `find Replays -name '*.json'`: **2478**.
- Format: each file is a full Kaggle-environments episode JSON with keys
  `configuration, description, id, info, module_version, name, rewards,
  schema_version, specification, statuses, steps, title, version`.
  - `info.TeamNames` = `[p0_name, p1_name]`, `info.seed` = integer seed,
    `info.EpisodeId` matches the DB `episode_id`.
  - `configuration` carries engine constants used below:
    `turnsPerDay=24`, `townShopUnlockInterval=3`, `weedSpawnChance=0.005`,
    `boardSize=10`, `startingMoney=3000`.
  - `steps` is a list of **720** entries (30 days x 24 hourly turns), each
    entry a 2-list (one dict per player) with keys
    `action, info, observation, reward, status`.
  - `observation` per player-slot contains: `day`, `hour`, `step`,
    `farms` (list of 2 full per-player farm state dicts: `farmer` position,
    `hands` (hired labor slots with per-hand action queues), `hires_today`,
    `money`, `tiles` (10x10 board: null / "LOCKED" / plant-tile dict /
    animal-tile dict), `private.inventories/seeds/shed`), `market`
    (`inventory`, `prices`), `town` (`unlocked_shops`).
  - `action` per player-slot is `{"farmer": [...move...], "hands": [[verb,
    arg?], ...], "market": [...]}` - i.e. **this is a genuine
    action-level trace**, not just a state trace. Phase 3's "compare the
    action chosen" is answerable directly from `steps[i][pid]['action']`,
    though this audit primarily mined the *resulting* tile/board state
    (dominant planted crop, hires_today, wheat fraction) rather than the raw
    verb stream, for tractability in the time available (see Limitations).
- The SQLite DB (`kaggriculture.db`) confirmed as a summary/index only:
  `episodes` (3579 rows) has `episode_id, path, p0, p1, money0, money1,
  winner, my_seat, my_result` - no seed column, no day-by-day data. `path`
  values are stale (point at an old container path
  `/sessions/serene-stoic-gates/...`), so DB rows cannot be joined to local
  replay files by path; joining by `episode_id` embedded in the replay
  filename (`episode-<id>-replay.json`) works for `Replays/Auto/*`.
- Board occupancy and empty-tile count ARE reconstructable per day/hour by
  scanning `farms[pid]['tiles']` for `None` cells vs `"LOCKED"` vs
  populated dict cells.
- Shop-unlock events ARE identifiable: `town['unlocked_shops']` grows by
  one entry on days where `(day+1) % 3 == 0`, per the exact code cited in
  Phase 5 below - this is directly visible in the observation stream
  (compare `town.unlocked_shops` length across consecutive days).
- RNG-path-sensitive days are exactly the days where
  `(day+1) % townShopUnlockInterval == 0` (i.e. `day % 3 == 2`), per the
  engine code in Phase 5.

**Sampling actually performed** (full 2478-file inventory was audited by
directory listing only; deep parsing was sampled for tractability):
`experiments/REPLAY_STATE_POLICY_AUDIT/mine.py` parsed **265 replay files**
(30 from `Replays/Auto/mine`, up to 30 each from the other 14 opponent/leader
directories, seeded-shuffle sample, `random.Random(42)`), covering **84
distinct opponent/team names** and sampling one observation every 24 hourly
steps (i.e. one snapshot per in-game day, `hour==0`) per file. This yielded
900 per-player per-day-bucket observations for the "mine" cohort and 900 for
the "opp" cohort after state binning. A full-corpus run (2478 files, all
hours) was not attempted - see Limitations.

## Phase 2 - Canonical state representation used

Level A (coarse economic state) - the layer actually used for Phase 3-4
mining, chosen because it is directly present in every observation without
further engine knowledge:
- `day_bucket = day // 3` (aligns bucket boundaries with the 3-day shop-unlock
  cycle so RNG exposure can be assessed per bucket)
- `cash_bucket(money)`: `<500 / 500-2k / 2k-5k / 5k-15k / 15k-40k / 40k+`
- `land_tier`: `len(farm.unlocked_quadrants)` (1-4)
- `labor_bucket(len(hands))`: `<=4 / 5-8 / 9-14 / 15+`

State signature = `(day_bucket, cash_bucket, land_tier, labor_bucket)`.

Level B (operational state - board occupancy, pending chores, idle labor,
harvestable inventory) was **not** mined in this pass beyond the crop-mix
and hires_today signals below; the raw per-tile board and per-hand action
queues needed for Level B were confirmed present in the data (see Phase 1)
but full Level B mining (weed count, idle-hand count, harvestable-unit
count per state) was out of scope for the time budget. This is a scope
limitation, not a data-availability limitation - the raw fields exist in
every sampled observation and a follow-up pass can add them (see
experiments/REPLAY_STATE_POLICY_AUDIT/README.md).

Level C (exact/local context) was not needed - no finding below required
tile-level replay to explain.

Per-state-bucket action features recorded: dominant planted crop (mode of
tile `crop` values), wheat-fraction of planted tiles, `hires_today`, money,
and shed WHEAT count.

## Phase 3-4 - State-conditioned action mining + repeated-divergence testing

Method: for every state signature bucket reached by >= 8 "mine" observations
and >= 8 "opp" observations, compare the modal (dominant) planted crop. A
divergence is reported only when both cohorts' modal crop differs AND each
cohort's mode carries >= 40% within-bucket frequency (i.e. it is the real
majority behavior, not a near-tie).

**6 candidate divergence buckets survived this filter**, all showing the
same pattern: STRAWBERRY (mine) vs WHEAT (opp).

| state (day_bucket,cash,land,labor) | mine action | mine freq (n) | opp action | opp freq (n) | mine seeds | opp seeds | opp teams (n) |
|---|---|---|---|---|---|---|---|
| (9, 40k+, land4, <=4hands) | STRAWBERRY | 0.69 (42) | WHEAT | 0.67 (52) | 13 | 17 | 17 |
| (8, 40k+, land3, <=4hands) | STRAWBERRY | 0.63 (35) | WHEAT | 0.60 (48) | 12 | 16 | 16 |
| (7, 15k-40k, land4, <=4hands) | STRAWBERRY | 0.69 (16) | WHEAT | 0.67 (9) | 7 | 3 | 3 |
| (8, 15k-40k, land3, <=4hands) | STRAWBERRY | 0.54 (13) | WHEAT | 0.67 (12) | 6 | 5 | 5 |
| (9, 40k+, land4, <=4hands) [land4 variant] | STRAWBERRY | 0.94 (16) | WHEAT | 0.62 (8) | 6 | 3 | 3 |
| (2, 500-2k, land2, <=4hands) | MELON | (small n) | WHEAT | (small n) | small | small | small |

(Full machine-readable data: `FINDINGS.json`; raw per-record dump:
`artifacts/replay_state_policy_audit/sample_mined_records.jsonl`.)

The two strongest rows (days 8-9, cash tier 40k+, land tier 3-4) have the
best support: 13-17 distinct opponent seeds, 16-18 distinct opponent-side
games, and 16-17 distinct named opponents each - this is a genuinely
repeated pattern across independent matchups, not a one-off from a single
rival.

**Global (all-state) aggregate**, matching and reproducing the earlier DB
finding at the replay level: wheat_frac (fraction of planted tiles that are
WHEAT) averaged over all sampled snapshots = **mine 0.142 (n=900) vs opp
0.294 (n=900)**. This is roughly 2x higher wheat share for opponents,
consistent with the DB aggregate (plant_wheat 24.72 mine vs 77.09 opp)
though not identical in magnitude (different metric: per-snapshot tile
fraction vs per-game total units).

Classification: **OBSERVED** (state -> action divergence, direct replay
evidence, not outcome-derived). No ASSOCIATED-outcome or HYPOTHESIZED-
mechanism claim is made about *why* this happens or whether it is good or
bad - Phase 3's instruction to report only "policy A chose X, policy B chose
Y, with frequency/support N" is followed literally; no causal or
quality claim is attached.

**hires_today divergence: none found.** Both cohorts showed hires_today=0
at 100% of the once-per-day (hour==0) sample points. This is very likely a
**sampling artifact** (hiring happens intraday and the counter appears to
reset at day boundary - `hires_today` is reset to 0 in `_end_of_day` per the
engine code inspected in Phase 5, and hour==0 snapshots are taken right
after that reset), not evidence that no hiring differences exist. Flagged
explicitly as NO_ROBUST_SIGNAL / instrumentation limitation, not as a
negative finding about hiring policy.

**Melon admission timing, fertilizer apply/hold, labor-constrained chore
prioritization, recurring action substitutions**: not analyzed at
sufficient depth in this pass (Level B state needed, see Phase 2) -
NO_ROBUST_SIGNAL, open for follow-up.

## Phase 5 - RNG-aware analysis

Confirmed engine code (read, not modified):
`vendor/kaggle_environments_engine/kaggriculture.py`, function `_end_of_day`
(lines ~837-867):

```python
seed = env.info.get("seed", 0)
rng = random.Random((seed * 1_000_003) ^ day)          # line 848

for player_id, farm in enumerate(obs0.farms):            # line 850
    ...
    _spawn_weeds(farm, board_size, weed_chance, rng)      # line 854 - draws consumed per empty tile, per player, in player order

next_day = day + 1
town = obs0.town
if next_day > 0 and next_day % shop_interval == 0:        # line 864, shop_interval = townShopUnlockInterval = 3
    remaining = [s for s in SHOPS if s not in town["unlocked_shops"]]
    if remaining:
        choice = rng.choice(sorted(remaining))             # line 867
        town["unlocked_shops"].append(choice)
```

This confirms, with exact line numbers, the previously-established
constraint: a single `random.Random` instance is created per day (seeded
from `(seed * 1_000_003) ^ day`), consumed first by `_spawn_weeds` for
player 0 then player 1 (draw count = number of empty tiles per player,
which is policy-dependent via board occupancy), and on days where
`(day+1) % 3 == 0` the *same, already-advanced* rng object is then used for
`rng.choice` over remaining shop options. This is PARTIAL_COUPLING as
previously found - it is now grounded in the vendored engine source rather
than only in the earlier audit memo.

**Classification of the crop-mix divergence found in Phase 3-4:
RNG-INDEPENDENT for the decision itself.** Choosing which crop to plant on
an already-available tile is a pure agent policy decision; it does not read
`env.info["seed"]`, the day RNG object, or `town.unlocked_shops` as an input
in a way that would make the *choice of WHEAT vs STRAWBERRY* itself a
product of the weed/shop RNG chain. However:

- **RNG-EXPOSED (indirectly) for *which tiles are available to plant on*.**
  Weed spawning (policy-dependent draw count) can occupy or clear tiles
  before a planting decision is made, so the *opportunity set* the crop
  choice is made from can be RNG-path-dependent, even though the choice
  given that opportunity set is not. This audit did not attempt to isolate
  opportunity-set effects from preference effects (would require Level B
  weed-count instrumentation, out of scope this pass).
- Four of the six divergence-bucket day_buckets (`day_bucket in {2,7,8,9}`,
  i.e. days 6-9, 21-23, 24-26, 27-29) straddle a `day % 3 == 2` shop-unlock
  trigger day or a `day % 3 == 0` post-unlock day within the 3-day bucket,
  so **all 6 reported divergence buckets are flagged `rng_exposed_daybucket:
  true`** in FINDINGS.json - meaning shop-unlock state could plausibly have
  shifted in a policy-dependent way within that window for at least some of
  the games contributing to the bucket. This does not overturn the crop-mix
  finding (the *decision mechanism* is independent of the RNG) but it means
  the exact game state (which shops are unlocked, exact board layout) that
  each snapshot was drawn from is not guaranteed identical across mine vs
  opp games at the same coarse state bucket, even holding day/cash/land/labor
  fixed.

**Final RNG classification for the crop-mix finding: RNG-EXPOSED (not
RNG-CONFOUNDED, not RNG-INDEPENDENT).** No policy-superiority claim is made
from it, consistent with the hard constraints.

## Phase 6 - Counterfactual/replay experiments

Not performed. The repo has no infrastructure discovered in this pass for
replaying a historical episode from a mid-game checkpoint with a single
action substituted while holding the rest of the trajectory fixed
(`mini_engine.py` and `bench_engine.py` run fresh simulations from day 0
with a given policy pair and seed, not from an arbitrary saved mid-game
state). Building such infrastructure was explicitly out of scope ("Do not
build a large new simulator unless necessary"). **This is documented as a
limitation, per the spec's explicit instruction to document rather than
invent results when controlled counterfactual testing is impossible.**

## Findings by confidence tier

- **DIRECTLY_OBSERVED**: In comparable (day-bucket, cash-bucket, land-tier,
  labor-bucket) states in the mid-late game, my games' modal planted crop is
  STRAWBERRY while the opponent field's modal planted crop is WHEAT, across
  6 state buckets with 8-52 observations per side, 3-17 distinct seeds per
  side, and 3-17 distinct named opponents. Global wheat-tile-fraction:
  mine 0.142 vs opp 0.294 (n=900 each).
- **STRONGLY_SUPPORTED**: none promoted to this tier - the strongest finding
  above is RNG-EXPOSED, so it stays at DIRECTLY_OBSERVED for the *existence*
  of the behavioral divergence, without a causal/quality claim.
  (This is a deliberate choice per the hard constraint against promoting
  ASSOCIATED/HYPOTHESIZED evidence to causal status.)
  Confirmed the specific engine RNG-coupling mechanism (weed-then-shop
  shared `random.Random` per day) at exact source lines is
  STRONGLY_SUPPORTED (direct code read, not inference).
- **PLAUSIBLE_BUT_UNPROVEN**: that the crop-mix divergence is at least
  partly explained by opportunity-set effects (available-tile differences
  from policy-dependent weed spawning) rather than pure crop preference;
  not tested this pass (would need Level B instrumentation + Phase 6
  counterfactual replay).

## Negative findings

- No robust hiring-decision divergence found (instrumentation limitation:
  `hires_today` sampled only at day boundaries, where it is always 0 -
  NO_ROBUST_SIGNAL, not evidence hiring policies are identical).
- No robust divergence found in melon admission timing, fertilizer
  apply/hold, or chore prioritization at the depth this pass reached -
  NO_ROBUST_SIGNAL for these sub-questions specifically, not a claim they
  don't exist.
- No causal or performance claim is attached to the crop-mix finding above -
  per the hard constraints and per the fact that this finding is
  RNG-EXPOSED, not RNG-INDEPENDENT.

## Limitations

1. Sampled 265 of 2478 available replay files (10.7%), one snapshot per
   in-game day (hour==0) rather than every hourly step. A full-corpus,
   full-resolution pass was not attempted given the 45-second-per-call
   device_bash constraint and token budget; the sample already spans 84
   distinct opponent identities and both "mine" and multiple leaderboard
   opponent pools, which is likely sufficient for the coarse Level-A
   question asked, but finer-grained (Level B/C) questions would benefit
   from a larger, hourly-resolution pass.
2. Level B (operational) state - board occupancy/weed counts, idle labor,
   harvestable inventory, pending chores - was confirmed present in the data
   but not mined this pass.
3. `hires_today` sampling is confounded by the day-boundary reset in the
   engine; a mid-day or end-of-day-minus-1 sample would be needed for a real
   hiring-divergence test.
4. No Phase 6 counterfactual testing was performed; no infrastructure exists
   in the repo for resuming simulation from a saved mid-game state with an
   action substituted.
5. "mine" cohort in this sample = replays where `info.TeamNames` contains a
   name in `{graceyunliu, grace, Grace}` (all games in `Replays/Auto/mine/`
   matched this). "opp" cohort = the other player-slot in every sampled
   file, including files entirely between two other named agents (no
   grace-identified side) which were excluded from mine/opp comparison
   (labeled "unk" and dropped) - so the "opp" cohort is a pooled mixture of
   many distinct agents, not a single opponent policy; divergences reported
   are against the pooled opponent field, not against any single rival.
6. DB `episodes.path` values are stale relative to this machine's current
   mount path and could not be used directly to join DB rows to files; this
   audit joined by filename embedded `episode_id` instead where DB
   cross-referencing was attempted informally, and otherwise worked directly
   from replay-file `info` fields (`seed`, `TeamNames`) which are
   self-contained and did not require the DB.

## Recommended next experiments

1. Extend `mine.py` to Level B (per-tile weed count, idle-hand count,
   harvestable-unit count) and re-run the same divergence-mining pass -
   directly answers the open P8 "why does the crop-mix differ" thread with
   more state granularity, and lets the opportunity-set-vs-preference
   question in Phase 5 actually be separated.
2. Re-sample `hires_today` at multiple intraday hours (not just hour==0) to
   get a real hiring-decision divergence test.
3. If a mid-game-state-resume capability is ever added to `mini_engine.py`/
   `bench_engine.py`, use it to test the crop-mix divergence found here as a
   true Phase 6 counterfactual (same seed, same day/board state, alternate
   crop choice, multiple seeds) - this is the only way to escape the
   RNG-EXPOSED classification for this finding.
4. Run the mining pass across the full 2478-file corpus (not just the 265-file
   sample) for statistical power on the smaller-support buckets (e.g. the
   MELON-vs-WHEAT bucket at day_bucket=2 had too few observations to trust).
