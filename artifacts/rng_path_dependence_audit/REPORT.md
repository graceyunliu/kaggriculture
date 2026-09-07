# RNG Path-Dependence Audit — Kaggriculture Engine

**Scope:** Methodology/diagnostic audit only. No claim is made about any policy's superiority. This document assesses whether observed "policy advantage" in evaluation could instead be RNG-stream path-dependence artifact.

## Executive Summary

The production engine (`vendor/kaggle_environments_engine_master/kaggriculture.py`) uses **exactly one RNG call site pair that shares a stream within a day**: weed spawning and the periodic town-shop unlock draw, both drawn from a single `random.Random` object created fresh each day inside `_end_of_day()`. Because the weed-spawn draw is **short-circuited to fire only on empty (`None`) board tiles**, the *number* of RNG draws consumed before the shop-unlock draw depends on how many tiles are occupied at end-of-day -- which is policy-dependent (a policy that plants/builds more leaves fewer empty tiles). A minimal, structurally faithful analogue (Phase 2 script) demonstrates that two policies differing only in board occupancy, under the **identical seed**, produce **different shop-unlock outcomes on 7 of 10 checkpoints tested**. This is DIRECTLY_OBSERVED for the analogue and SUPPORTED (by direct code inspection, not by running the full production engine end-to-end) for the production engine itself, since the analogue reproduces the exact code shape (same short-circuit condition, same per-day reseeding formula, same draw ordering) found in production.

Critically, the per-day RNG is **reseeded fresh every day** from `(seed * 1_000_003) ^ day` -- it is NOT a single persistent stream running the whole game. So the coupling is **local to each day's weed/shop draw pair**, not a compounding cross-day drift of one running stream. However, its effect is NOT local in consequence: once a shop unlocks a particular way on a given day, `town["unlocked_shops"]` is permanent state that affects all subsequent days' market/shop economy for the rest of the game. So a single diverged draw, caused purely by tile-occupancy differences, can permanently alter the town's shop composition and downstream economy for the rest of the episode -- this is a real vector by which two different policies under the "same seed" can experience different game economies, unrelated to any causal quality of the policy itself.

No other RNG coupling was found. Market prices (`market_price()`) are a **deterministic function of inventory** -- no randomness at all. Demand/sale mechanics found in the engine are also deterministic. The `random_agent`/example agents in the same file use their own unseeded `random.Random()` instances, unrelated to the interpreter's engine RNG, and are not part of the evaluated production path (they're example/reference agents, not the champion/family policies under test).

**Final status: PARTIAL_COUPLING_FOUND**

---

## Phase 1 — Engine RNG Inventory

### 1. Where randomness is generated

- File: `vendor/kaggle_environments_engine_master/kaggriculture.py` (also mirrored, apparently identically, in `vendor/kaggle_environments_engine/kaggriculture.py` -- not separately audited, treat as duplicate; see Limitations).
- `import random` at line 3 (Python stdlib `random` module -- no numpy usage anywhere in this file).
- The interpreter's only seeded, game-relevant RNG object is created **inside `_end_of_day()`**:

```python
# kaggriculture.py:869-871
# Stable RNG keyed off env.info["seed"] + day so replays reproduce.
seed = env.info.get("seed", 0)
rng = random.Random((seed * 1_000_003) ^ day)
```

This `random.Random` instance is constructed **fresh on every call to `_end_of_day`** (i.e., once per game day), seeded deterministically from the episode seed XORed with the day index. It is a local variable, not stored on `env` or `state` -- it does not persist across days.

- Episode seed source: `seed = resolve_episode_seed(env)` at line 249, inside `_initialize()`, imported from `kaggle_environments.utils`. This determines `env.info["seed"]`, which is what `_end_of_day` reads back out at line 870.

- Separately, `random_agent()` (an example/reference agent, not a production policy) creates its own **unseeded** `random.Random()` at line 1028 -- this is agent-side randomness for that specific toy agent, disconnected from the engine's per-day `rng` and from any policy under evaluation in the family comparison.

### 2. One shared stream, or multiple independent streams?

**One shared stream per day**, reused for two purposes within that single `_end_of_day()` call:
1. Weed spawning across all players' boards (`_spawn_weeds`, called once per player in a loop)
2. The periodic town-shop unlock draw (`rng.choice(sorted(SHOPS))`)

There is no separate/independent RNG instance for weeds vs. shops -- both draw from the same `rng` object, in this fixed order: weeds first (for player 0, then player 1, ... in farm-index order), shop-unlock draw last, only on days where `(day+1) % shop_interval == 0`.

Because the object is reconstructed every day from `(seed*1_000_003) ^ day`, this is **multiple independent per-day streams across days** (day N's rng has nothing to do with day N+1's rng), but **one shared stream across mechanics within a day**.

### 3. Enumeration of every RNG call site

| # | File:line | Call | Purpose |
|---|-----------|------|---------|
| 1 | `kaggriculture.py:839` | `rng.random()` (inside `_spawn_weeds`, called from line 877) | Weed-spawn roll, once per empty tile, per player, per day |
| 2 | `kaggriculture.py:891` | `rng.choice(sorted(SHOPS))` | Town shop-unlock draw, on unlock-interval day boundaries |
| 3 | `kaggriculture.py:1028` | `random.Random()` (unseeded) | Constructs `rng` local to `random_agent()`, an example/reference agent -- separate object, not engine state |
| 4 | `kaggriculture.py:1041-1046` | `rng.random()`, `rng.choice()` (x2) | Inside `random_agent()`'s own decision logic -- agent-side, not engine RNG |
| 5 | `kaggriculture.py:1042`/`1046` | (same object as #3/#4) | same as above |

Only call sites #1 and #2 are part of the interpreter/engine itself and thus affect the actual game state seen by every policy under evaluation. #3-#5 belong to one specific reference agent's own decision code and are irrelevant to the family comparison unless that reference agent itself is one of the two policies being compared (not stated in this task's background).

No `np.random.*`, `numpy` import, `shuffle()`, or `randint()` calls exist anywhere in this file.

### 4. Call order within a day -- does weed generation feed the same stream later consumed by shops?

Yes. Trace of `_end_of_day(state, env, day)` (lines 860-891):

```python
rng = random.Random((seed * 1_000_003) ^ day)          # line 871: fresh per-day RNG

for player_id, farm in enumerate(obs0.farms):           # line 873
    _daily_refresh_plants(farm, day, turns_per_day)      # no RNG
    _daily_refresh_animals(farm, day)                    # no RNG
    _spawn_weeds(farm, board_size, weed_chance, rng)      # line 877: consumes rng.random() per empty tile
    _drop_inventories_to_shed(private, shed_cap)          # no RNG
    ...

next_day = day + 1
if next_day > 0 and next_day % shop_interval == 0:        # line 886
    if len(town["unlocked_shops"]) < MAX_SHOP_INSTANCES:
        town["unlocked_shops"].append(rng.choice(sorted(SHOPS)))  # line 891: consumes from SAME rng object
```

Order is fixed: weed spawning for every player's board happens first (consuming a variable number of draws depending on how many `None` tiles exist), then -- only on qualifying days -- exactly one `rng.choice()` draw for the shop unlock, from the **same, already-partially-consumed** `rng` object.

This is DIRECTLY_OBSERVED from the source.

### 5. Could two policies with different actions cause divergent future draws given the same seed?

Yes, mechanically, for the following reason (DIRECTLY_OBSERVED in code, SUPPORTED as an in-production effect by the faithful minimal analogue in Phase 2):

`_spawn_weeds` only calls `rng.random()` when `farm["tiles"][y][x] is None` (line 839, short-circuited `and`). A policy that plants/builds on more tiles by end-of-day leaves fewer `None` tiles, so it causes **fewer** `rng.random()` calls that day, before the shared shop-unlock draw executes. A sparser policy leaves more empty tiles and consumes **more** draws first. Since both policies start the day from the identical `random.Random(seed_and_day)` state, but consume different counts of draws via `_spawn_weeds` before reaching the shop draw, the internal RNG state handed to `rng.choice()` differs between the two policies -- producing a different shop pick despite the identical initial seed.

### 6. Intentional semantics or accidental artifact?

The seeding comment ("Stable RNG keyed off env.info['seed'] + day so replays reproduce") indicates the **per-day reseeding** was deliberate, intended to make each day's weed/shop randomness reproducible given (seed, day). However, there is no comment or evidence suggesting the designer intended or was aware that **sharing one rng object between weed-spawning and the shop-unlock draw, combined with the tile-occupancy-dependent short-circuit, makes the shop draw policy-dependent** even though the day's rng seed is fixed. This reads as an **unintended engineering side-effect** of a reasonable-looking reproducibility design (PLAUSIBLE -- I cannot inspect commit history or design docs to confirm intent either way; UNRESOLVED on developer intent specifically, though the mechanical effect itself is DIRECTLY_OBSERVED).

---

## Phase 2 — Minimal Reproduction

Script: `experiments/RNG_PATH_DEPENDENCE_AUDIT/repro_rng_path_dependence.py` (**MINIMAL ANALOGUE**, explicitly labeled as such -- it does NOT invoke the production `kaggriculture.py` engine; it reimplements the exact code shape of `_end_of_day`'s weed-spawn + shop-unlock logic in isolation, at the same board size, same weed chance, same per-day seeding formula, same short-circuit condition and draw order).

Design: two synthetic "policies" differing only in board occupancy fraction (10% occupied vs. 90% occupied, simulating a sparse-planting vs. dense-planting policy), same seed (`12345`), evaluated day-by-day for 30 days. At each shop-unlock-interval day boundary (every 3rd day), the script records the number of weed-loop `rng.random()` draws consumed and the resulting shop pick for both policies.

### Actual output (full run, this session)

```
Total shop-unlock checkpoints: 10
Diverged (different shop unlocked despite identical seed): 7
Same pick despite different draw counts: 3
```

Detail (draws_A = sparse policy, draws_B = dense policy):

| day | draws A | draws B | shop A | shop B | result |
|---|---|---|---|---|---|
| 2 | 91 | 11 | BUTCHER | BUTCHER | same |
| 5 | 90 | 13 | PIZZA_SHOP | ICE_CREAM_SHOP | **diverged** |
| 8 | 93 | 8 | PIZZA_SHOP | PIZZA_SHOP | same |
| 11 | 82 | 11 | BUTCHER | FARM_SUPPLY | **diverged** |
| 14 | 89 | 13 | DAIRY | DAIRY | same |
| 17 | 93 | 16 | PIZZA_SHOP | FARM_SUPPLY | **diverged** |
| 20 | 85 | 11 | GENERAL_STORE | BUTCHER | **diverged** |
| 23 | 94 | 17 | DAIRY | ICE_CREAM_SHOP | **diverged** |
| 26 | 91 | 5 | GENERAL_STORE | DAIRY | **diverged** |
| 29 | 82 | 7 | BUTCHER | SMOOTHIE_SHOP | **diverged** |

Full JSON output saved alongside the script at run time (`rng_path_dependence_results.json`).

**Conclusion of Phase 2:** DIRECTLY_OBSERVED for the analogue -- the shared-stream, occupancy-gated draw-count mechanism produces different downstream random outcomes (shop unlocks) from an identical seed, purely as a function of how many board tiles a policy leaves empty. Because the analogue is a structural copy of the real code (not just "inspired by" it), this result is SUPPORTED, not merely PLAUSIBLE, as a description of what the production engine would do under analogous divergent occupancy -- but it has not been verified by running the actual multi-thousand-line production engine end-to-end with two real competing policies and diffing internal RNG call counts, so full production confirmation remains UNRESOLVED pending such a run.

---

## Causal Diagram

```
                  seed, day
                     |
        rng = Random((seed*1_000_003) ^ day)
                     |
        _spawn_weeds(...)
          for each tile:
            if tile is None:        <-- POLICY-DEPENDENT
                draw = rng.random()      (occupied tiles differ per
                (consumes 1 draw)          policy => draw COUNT differs)
                     |
                     | (rng internal state now depends on draw
                     |  COUNT, which depends on POLICY)
                     v
        if unlock day:
            town.shops.append(
               rng.choice(SHOPS))    <-- DIVERGES
                     |
                     v
        town["unlocked_shops"] permanently changed
        -> alters market/shop economy for ALL
           remaining days of the episode
```

---

## Phase 3 — Evaluation-Methodology Options

| Option | Causal question answered | Changes game semantics? | Implementation cost | Risks | Separates robust effect from path-luck? |
|---|---|---|---|---|---|
| **Fresh-seed default comparison** (status quo, presumably) | "Does policy A score higher than B, averaged over many independent seeds?" | No | None (already the default) | Path-dependent single-seed differences wash out only if many seeds are run; a small seed sample still risks exactly this artifact | Partially -- only with a large enough seed sample; does not diagnose *why* an advantage exists |
| **Paired-seed evaluation** (same seed, run both policies, compare per-seed deltas, paired t-test) | "Within-seed, does A beat B, on average across seeds?" | No | Low | The exact mechanism documented here means "same seed" does NOT guarantee "same trajectory realization" once policies diverge in occupancy -- so paired evaluation can still inherit RNG-path luck baked in after divergence | No -- this is precisely the setup that is vulnerable to the artifact; must be combined with another control below |
| **RNG stream separation** (give weed-spawn and shop-unlock independent `random.Random` instances, seeded independently) | Removes the specific coupling found in Phase 1 entirely | **Yes** -- changes engine semantics (shop unlock timing/identity would differ from current games, breaking backward comparability with prior results) | Low code change, but re-invalidates all historical seed-based comparisons | Must re-run baselines; changes what "seed X" means going forward | Yes, directly eliminates this specific mechanism (does not address other potential path-dependence sources, if any exist) |
| **Deterministic replay / counterfactual eval** (record full action log, replay it with instrumented RNG-call counters) | "Exactly how many draws did each policy consume, and where did outcomes diverge?" | No | Moderate (needs engine instrumentation/hooks) | None significant; purely observational | Yes -- this is the diagnostic tool, not a fix; needed to confirm/deny the artifact on a per-run basis |
| **Recording RNG draw counts per game** (log `rng` call count per day per side) | Direct evidence of divergence magnitude per real game | No | Low (add counters around lines 839/891) | None | Yes -- necessary supporting evidence for any of the above |
| **Common Random Numbers (CRN) design** (force both policies to consume shop-unlock draws from a stream NOT contaminated by their own action-dependent weed-draw count -- e.g., draw shop pick from a stream keyed only on `(seed, day)` with no other consumption) | Same as RNG stream separation, but the minimal-cost version of it (keep weeds coupled to occupancy, only insulate the shop draw) | **Yes**, in the specific narrow sense that shop-unlock outcomes would differ from current behavior | Very low (change line 891 to use a second, independent `Random((seed, day, 'shop'))` object) | Same backward-comparability caveat as full stream separation | Yes for this specific mechanism |

---

## Phase 4 — Minimal Protocol for Future Evolutionary/TDAS Experiments

Distinguish, for any claimed mechanism/intervention:

- **ACTION DIFFERENCE**: the intervention measurably changes the policy's chosen actions (e.g., more tiles planted, different day-14 branch taken). Evidence: action logs/diffs.
- **TRAJECTORY DIFFERENCE**: the predicted intermediate game-state changes (weed counts, shop-unlock identity/timing, market state) actually occur, not just final score. Evidence: per-day state diffs, RNG draw-count logs (per Phase 3 above).
- **ROBUST CAUSAL MECHANISM**: the final advantage (1) is evidenced at the action level, (2) produces the predicted trajectory changes, (3) **survives fresh-seed re-evaluation across a reasonably large, independent seed sample** (not just the original seed(s) the advantage was found on), and (4) is not explainable solely by one policy having, on the specific seeds tested, gotten a favorable path-dependent draw sequence (e.g., a lucky shop unlock) that had nothing to do with the intervention's intended mechanism.

Recommended minimal protocol:

1. Require (1) and (2) above as a prerequisite before running any larger seed sweep -- cheap to check, catches "no-op" interventions early (as prior audits in this repo's memory have found: e.g., render() silently dropping params, block-pair mutation always offering a no-op).
2. Run the candidate on a **fresh, disjoint seed set** from whatever seed(s) it was discovered/tuned on. An advantage that only appears on the discovery seed(s) is a strong path-luck red flag given the mechanism documented in this report.
3. Where feasible, instrument and log RNG draw counts (weed-loop draws before each shop-unlock checkpoint) for both arms of a comparison. A shop-unlock divergence coincident with a reported "town demand path" divergence (as in this task's background: divergence starting ~day 14) is a specific, checkable fingerprint of this exact mechanism -- check whether `town["unlocked_shops"]` differs between the two branches' game logs at/after the day the behavioral divergence starts.
4. Treat any comparison run on a single seed or a small paired-seed set as PRELIMINARY, not confirmatory, given the demonstrated mechanism. Escalate to a larger fresh-seed sample before treating a result as a robust causal claim.
5. If a claimed mechanism's advantage disappears or reverses under a fresh, larger seed sample, classify the original finding as PATH-DEPENDENT LUCK, not a robust policy effect, and document it as such (do not chase the original number back, mirroring the existing project precedent on the M2 exploit-vs-general finding already recorded in project memory).

---

## Limitations / Open Questions

- This audit inspected `vendor/kaggle_environments_engine_master/kaggriculture.py` as **the** production engine, based on it containing `resolve_episode_seed` (a `kaggle_environments` framework hook) and the interpreter/state-machine shape expected of a Kaggle environment. A near-identical file exists at `vendor/kaggle_environments_engine/kaggriculture.py`; it was not separately line-diffed against the `_master` copy in this audit -- if the two differ in the RNG-relevant sections, this report's line citations may not apply to whichever copy is actually invoked by the evaluation harness the "within-family root-cause audit" used. **UNRESOLVED**: confirm which of the two vendored copies is actually imported/run by the harness that produced the $25,507 gap finding.
- Phase 2 is an explicitly-labeled **minimal analogue**, not an execution of the full production engine with two real family-member policies. It demonstrates the mechanism is real and reproducible in isolation; it does not by itself prove that the specific $25,507 gap in the original within-family comparison was caused by this mechanism. That would require instrumenting the actual engine run(s) that produced the original finding (per the Phase 3/4 recommendations) -- **UNRESOLVED** as a specific causal explanation of that particular number, though PLAUSIBLE given the day-14 divergence timing cited in the background matches exactly the kind of state (`town["unlocked_shops"]`) this mechanism can permanently alter.
- No other RNG call sites of consequence were found in the engine file beyond weeds/shop-unlock; deterministic market pricing was verified by reading `market_price()` and `_refresh_prices()` directly (no randomness). This does not rule out randomness in other engine-adjacent files (e.g., `kaggle_environments` framework internals, not vendored/audited here) -- **UNRESOLVED** whether the framework itself (outside this repo's vendored copy) introduces any additional RNG behavior (e.g., in `resolve_episode_seed` itself, which was imported, not defined, in this file, and whose implementation was not located/audited in this repo).
- Developer intent behind the shared-stream design (Phase 1, Q6) is **UNRESOLVED** -- inferred from a code comment only, not from commit history, issue tracker, or design docs.

---

## Conclusion Labeling Summary

| Claim | Label |
|---|---|
| Engine RNG uses Python stdlib `random.Random`, not numpy | DIRECTLY_OBSERVED |
| Per-day RNG is freshly seeded from `(seed*1_000_003) ^ day`, not a single persistent stream | DIRECTLY_OBSERVED |
| Weed-spawn and shop-unlock draws share one `rng` object within a day | DIRECTLY_OBSERVED |
| Weed-spawn draw count is gated by tile occupancy (short-circuit `and`) | DIRECTLY_OBSERVED |
| This can make the shop-unlock draw diverge between policies despite identical seed | SUPPORTED (via structurally faithful minimal analogue; not yet run against the real multi-policy production engine) |
| Divergence is confined to that day's shop-unlock draw, but `town["unlocked_shops"]` persists, so consequences propagate for the rest of the game | DIRECTLY_OBSERVED (persistence) + SUPPORTED (propagation to downstream economy, not separately re-simulated end-to-end here) |
| Market prices/demand are deterministic, not randomized | DIRECTLY_OBSERVED |
| This specific mechanism explains the reported $25,507 gap / day-14 divergence | PLAUSIBLE, UNRESOLVED as definitive causal attribution |
| Coupling was an intentional design choice | UNRESOLVED |

---

**FINAL STATUS: PARTIAL_COUPLING_FOUND**

---

## Implemented Evaluation Protocol (added Sep 7, follow-on session)

Per this report's Phase 4 recommendation, reusable tooling was built at
`experiments/RNG_PATH_DEPENDENCE_AUDIT/eval_protocol.py` (CLI + importable
`compare_paired()` function), documented in
`experiments/RNG_PATH_DEPENDENCE_AUDIT/README.md`. It runs a paired/common-seed
comparison of two candidate policies against a fixed common opponent, on the
**actual production engine** (via `mini_engine.py`'s existing shim -- not a
synthetic analogue like this report's own Phase 2 script), instrumenting
real per-day weed-spawn draw counts and shop-unlock outcomes by monkeypatching
`_end_of_day`/`_spawn_weeds` (same pattern `mini_engine.py` already uses for
`_commit_unit`, restored after each call, nothing written to disk). Output
separates ACTION DIFFERENCE (did the candidate's board occupancy actually
differ?), TRAJECTORY DIFFERENCE (did `town["unlocked_shops"]` actually diverge
between the two arms despite the identical seed?), and the $ OUTCOME
(paired-seed mean delta, stdev, t-stat, win/loss/tie), per this report's
Phase 4 vocabulary.

**Validated against the real engine, not just scaffolding**: it was run
end-to-end this session (`--engine master`) with three throwaway demo
agents built only to exercise the harness (a board-sweeping "planter", an
always-PASS "passive" agent, both against a fixed carrot-loop opponent
copied from the engine's own `starter_agent`), 6 seeds:

```
n=6 paired games   mean delta $-47   stdev $5   t=-22.14
action-diverged: 6/6 games      trajectory-diverged: 6/6 games (seeds 1-6)
```

This confirms the harness runs cleanly against the real engine, correctly
detects the candidates' occupancy difference (`action_diverged`), and
correctly flags every seed here as `trajectory_diverged` -- expected, since
the two demo agents were deliberately built to maximize occupancy contrast
(a near-worst-case for this coupling), not chosen to demonstrate a "typical"
comparison. **Not yet validated**: no real champion/candidate/family-member
comparison has been run through this tool -- that was out of scope for this
task (pure eval-methodology tooling, no strategy claims). Known TODOs (full
list in the README): no direct candidate-vs-candidate mode without a common
opponent; only the one known coupling mechanism (`unlocked_shops`) is
checked for divergence; not yet wired into `evolve/`'s loop or any existing
regression harness.
