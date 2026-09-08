# Replay Mining Phase 4A: Statistical Confirmation of the Melon-Opportunity Divergence

> **Provenance correction (added after Phase 4A):** "opponent" / "opp"
> throughout this report means the opposing seat observed inside Grace's
> own replay history (`Replays/Auto/mine/`), not an independently sampled
> leaderboard/ladder reference population. See [INDEX.md](INDEX.md) for
> the full correction and what it does and doesn't affect. Numbers and
> verdicts below are unchanged.

Date: 2026-09-08. Follow-on to `REPORT.md`, `REPORT_PHASE2.md`,
`REPORT_PHASE3.md` - read those first. This phase answers exactly one
question, per Grace's scope: **does the melon-sell-when-opportunity-exists
divergence found in Phase 3 (0.63% mine vs 3.65% opp, n=24 action events)
reliably exist as a behavioral difference, once properly powered?** It does
NOT ask or answer whether melon-selling is good, and makes no performance
or causal claim. **Phase 4B (causal intervention) was explicitly not
started - see "Hard constraints" below.**

**Final status: CONFIRMED** (the divergence reliably exists as a
statistically robust, RNG_INDEPENDENT behavioral difference at the pooled
level) **with an important heterogeneity caveat** (see "Per-opponent-cohort
breakdown" - it is not a uniform trait shared narrowly by all opponents,
but a broad, majority-consistent pattern across a large and varied set of
distinct opponents, amplified by a subset of near-always-sell agents).

## Pre-registered analysis plan (written before results were computed)

Decided and written down before running `analyze_phase4a.py`:

1. **Opportunity/action definitions**: reuse Phase 3's `shed.MELON > 0`
   opportunity gate and `OBSERVED_ACTION`/`OBSERVED_ABSTENTION` tagging
   unchanged (`kaggriculture.py:_commit_unit` SELL branch, lines 626-635) -
   no new decision types, no redefinition.
2. **Point estimates + uncertainty**: report each cohort's action rate with
   a **Wilson score 95% CI** (chosen over the normal/Wald interval because
   it stays valid at small-to-moderate sample proportions and doesn't
   produce out-of-bounds intervals).
3. **Significance test**: **Fisher's exact test (two-sided)** on the 2x2
   contingency table (mine action/abstain x opp action/abstain), computed
   directly via exact hypergeometric summation in log-space (no `scipy`
   available on this machine) rather than a normal-approximation
   chi-square/z-test - chosen specifically per Grace's instruction to
   prefer an exact test over large-sample-normal-approximation methods,
   decided in advance of seeing whether the scaled-up sample was still
   sparse.
4. **Effect size**: report both a **rate ratio** (opp rate / mine rate,
   log-scale delta-method 95% CI) and an **odds ratio** (Haldane-Anscombe
   0.5 continuity correction if any cell is zero, log-scale Wald 95% CI) -
   not a bare point-estimate ratio.
5. **Non-independence**: events within one replay (same seed, same
   opponent identity) are not independent draws. A **cluster bootstrap
   resampling whole replays** (not individual events), 2000 resamples,
   percentile 95% CI on the rate ratio, is used to check whether the
   point-estimate CI above (which assumes independent events) is
   overstating precision.
6. **Per-opponent-cohort check**: report the melon action rate separately
   for every distinct opponent identity with >=30 opportunity observations,
   to check whether the pooled divergence is broad across many opponents or
   driven by one or two outliers.
7. **RNG classification**: unchanged from Phase 3 - `RNG_INDEPENDENT` is
   asserted before results are computed (the opportunity gate is a pure
   shed-count check, no RNG read; see Phase 3 code citation), and will only
   be revised if re-examination of the code surfaces something new.
8. Decision on "reliably exists" verdict will be made using: Fisher's exact
   p-value, whether both the delta-method AND the cluster-bootstrap CI on
   the rate ratio exclude 1.0, and whether the per-opponent breakdown shows
   a majority-consistent direction (not 1-2-opponent-driven). All four
   were fixed as the decision criteria before the numbers below were seen.

## Replay scale-up

**Source**: `Replays/Auto/mine/` only. Before running the scale-up, this
phase discovered and confirms as a finding in its own right (see
"Negative/methodological finding" below): **the opponent-leaderboard
directories used in Phases 1-3 sampling
(`Replays/Auto/leaderboard-*/`, `Replays/Leader Replays/Subin An/`, 304
files total) contain zero games featuring `graceyunliu`** - every replay in
those directories is a game between two other Kaggle competitors, not
involving Grace at all. This phase's `mine_phase4a.py` confirmed this by
scanning all 304 such files (`/tmp/phase4a_opp.jsonl`, 3
device_bash-chunked runs) and finding 0 files with a `graceyunliu`-tagged
`TeamNames` entry. **All of Phases 1-3's "mine" vs "opp" comparisons were
therefore already drawing "opp" exclusively from the non-Grace seat within
`Replays/Auto/mine/` games** - this phase's scale-up correctly targets that
same, only-relevant, directory.

`Replays/Auto/mine/` has **2,133** replay files available (vs the 15-30
sampled per phase in Phases 1-3). This phase scanned **358** of them
(seeded shuffle, `random.Random(42)`, same seed as prior phases so the
first ~15-30 files overlap with earlier samples; 3 device_bash-chunked runs
of 120 files each) - a **~12x increase** in scanned "mine" replays over
Phase 3's effective sample, yielding a melon-opportunity dataset far beyond
175 files / 1,576 rows / 24 action events:

- **35,577 total melon-opportunity rows** across both cohorts (vs 1,576 in
  Phase 3).
- **2,238 total action events** (vs 24 in Phase 3) - a ~93x increase in the
  quantity that was previously the binding constraint on statistical power.
- **306 distinct opponent identities** represented (vs the pooled,
  less-enumerated field in Phase 3).

No new decision types were opened; only melon-opportunity scanning was
scaled, per Grace's scope. `mine_phase4a.py` is melon-only (it does not
compute HIRE, FERTILIZE, PLANT, or CHORE events at all this phase).

## Opportunity and action counts per cohort

| cohort | opportunities | OBSERVED_ACTION | OBSERVED_ABSTENTION | action rate | Wilson 95% CI |
|---|---|---|---|---|---|
| mine (graceyunliu) | 24,033 | 894 | 23,139 | 3.72% | [3.49%, 3.97%] |
| opp (pooled, 306 identities) | 11,544 | 1,344 | 10,200 | 11.64% | [11.07%, 12.24%] |

## Statistical test

**Fisher's exact test (two-sided), computed exactly via log-space
hypergeometric summation**: **p = 7.1e-169**. (For context: this is far
below any conventional significance threshold; the exact computation, not
a normal approximation, was used per the pre-registered plan, satisfying
Grace's instruction to prefer an exact test.)

## Effect size with uncertainty

- **Rate ratio (opp rate / mine rate)**: **3.13**, 95% CI **[2.88, 3.40]**
  (log-scale delta method, treating each event as an independent Bernoulli
  draw - see cluster-bootstrap section below for a non-independence-aware
  version of this same interval).
- **Odds ratio (mine action-odds vs opp action-odds)**: **0.293**, 95% CI
  **[0.269, 0.320]** (i.e. mine's odds of selling-when-opportunity are
  about 0.29x opponents' - equivalently opponents' odds are ~3.4x mine's).

Both intervals exclude 1.0 (no-difference) by a wide margin.

## Non-independence: cluster bootstrap by replay

Events within one replay share a seed and an opponent identity and are not
independent draws. A cluster bootstrap resampling **whole replays** (not
individual events), 2000 resamples, each resample summing action/abstain
counts across the resampled replay set before recomputing the rate ratio:

- **Median cluster-bootstrap rate ratio: 3.16** (matches the point estimate
  closely).
- **Cluster-bootstrap 95% CI: [2.09, 4.77]** - wider than the
  event-independent delta-method CI ([2.88, 3.40]) as expected, since
  clustering reduces effective sample size, but **still excludes 1.0 by a
  comfortable margin**. This is the single most important number in this
  report: even after explicitly accounting for non-independence at the
  replay/opponent level, the divergence does not disappear.

## Per-opponent-identity breakdown (broad pattern, not outlier-driven - with a heterogeneity caveat)

**61 distinct opponent identities** had >=30 melon-opportunity observations
each (10,119 of the pooled 11,544 opponent-side opportunities, 87.7%,
came from these 61 well-sampled identities).

- **35 of 61 (57%)** individually show a melon-sell rate *above* my overall
  3.72% rate; **26 of 61 (43%)** are at or below it. This is a majority,
  not a near-even split, but **not near-unanimous** either - this is
  reported plainly as a genuine mixed-but-majority pattern, not spun as
  "opponents uniformly sell more melon."
- **The pooled 11.64% rate is substantially inflated by a subset of
  near-always-sell opponents**: the highest-rate identities with >=30
  observations include `Harith Al-Ani` (94/98 = 95.9%), `Akshay V`
  (88/94 = 93.6%), `Jiman Kwon` (31/35 = 88.6%), `林益民_li` (45/51 =
  88.2%) - these read as agents whose policy is close to "always sell
  melon on sight," not a subtle behavioral tilt.
- At the same time, a comparable number of well-sampled opponents show
  *near-zero* melon-sell rates: `Shailaja J` (0/363 = 0%),
  `Ram Chandra Gupta` (0/220 = 0%), `Legend Brothers` (1/455 = 0.2%),
  `Mason Mahar` (1/222 = 0.5%) - these read as near-"never sell" policies,
  similar in character to what this audit's own play looks like.
- **Median melon-sell rate among the 61 well-sampled opponents: 4.44%** -
  much closer to my 3.72% rate than the 11.64% *pooled-mean* rate suggests.
  The pooled mean is pulled upward by the heavy right tail of
  near-always-sell opponents.

**Honest characterization**: the divergence is real, statistically robust,
and present in a majority of individually-tested opponents (not 1-2
outliers) - but the *magnitude* commonly quoted (3.13x pooled rate ratio)
is driven substantially by a subset of opponents running what looks like a
near-deterministic "always sell melon" policy, pulling the pooled average
well above the *typical* (median) opponent's rate, which is much closer to
mine. Both statements are true simultaneously and neither is more "real"
than the other - they describe different aspects (pooled-population-level
divergence vs typical-individual-level divergence) of the same data.

## RNG classification

**RNG_INDEPENDENT**, unchanged from Phase 3 and confirmed, not revised,
this phase: the melon-opportunity gate (`shed.MELON > 0`) and sale price
(`market_price()`) remain pure functions of inventory/configuration with no
RNG read, per the code cited in `REPORT_PHASE3.md`. This phase did not
re-examine the engine code further (no new decision type was opened), so
this classification is carried forward rather than re-derived.

## Findings by confidence tier

- **DIRECTLY_OBSERVED / STRONGLY_SUPPORTED**: the melon-opportunity action-
  rate divergence (mine 3.72% vs opp 11.64% pooled) is now
  **STRONGLY_SUPPORTED** - promoted from Phase 3's PLAUSIBLE_BUT_UNPROVEN
  tier because it now clears a pre-registered exact significance test
  (p=7.1e-169), a pre-registered effect-size-with-CI requirement (rate
  ratio 3.13, CI excludes 1 both by delta method and by cluster bootstrap),
  and a pre-registered per-opponent-cohort robustness check (majority,
  57%, of well-sampled individual opponents individually replicate the
  direction). This promotion is about the **existence and robustness of
  the behavioral divergence only** - it is explicitly NOT a promotion to
  any causal or performance claim, which remains out of scope for 4A.
- **PLAUSIBLE_BUT_UNPROVEN**: any claim about *why* the divergence exists,
  or whether it reflects a coherent "policy trait" versus a mixture of very
  different opponent policies (some near-always-sell, some near-never-sell)
  - the heterogeneity data above is descriptive, not explanatory.

## Negative / methodological finding

The 304 opponent-leaderboard-directory replay files used for sampling in
Phases 1-3 (`Replays/Auto/leaderboard-*/`, `Replays/Leader Replays/`)
**contain zero `graceyunliu` games** and contributed **zero** rows to any
mine-vs-opp comparison in any phase to date - they were scanned (and
inflated file-count totals reported in earlier phases) but structurally
could not produce paired data, since this audit's "opp" cohort is defined
as the non-Grace seat within Grace's own games. This does not invalidate
any earlier finding (the "opp" data in Phases 1-3 was always correctly
sourced from `Replays/Auto/mine/`), but it means the "84 distinct
opponent identities" / "265-file sample" language in Phase 1 and similar
counts in Phase 2-3 reports overstate the *directory* diversity of the
comparison; the true opponent-identity diversity (up to 306 distinct
names, confirmed this phase) came entirely from the variety of rivals
Grace has played, not from the extra leaderboard directories. Flagged here
explicitly per the instruction to surface anything that clarifies or
qualifies earlier phases' methodology, without re-litigating their
substantive findings.

## Limitations

1. The rate-ratio delta-method CI treats events as independent; the
   cluster-bootstrap CI is the more defensible interval given known
   within-replay non-independence, and is wider (as expected) but still
   excludes 1.0.
2. "Opportunity" is still the coarse `shed.MELON > 0` gate from Phase 3 -
   it does not verify price favorability at the moment of the opportunity;
   a below-cost or unfavorable-price melon "opportunity" is counted the
   same as a favorable one.
3. Per-opponent breakdown is restricted to identities with >=30
   observations (61 of 306) for statistical stability; the long tail of
   thinly-sampled opponents is not individually characterized.
4. No performance, outcome, or causal analysis was performed - explicitly
   out of scope for 4A.
5. Fisher's exact p-value at this scale (N in the tens of thousands) is
   expected to be extremely small for even modest true differences; the
   effect-size CIs (rate ratio, odds ratio, cluster bootstrap) are the more
   informative numbers than the p-value itself for judging practical
   magnitude.

## Hard constraints - explicitly confirmed not violated

No code, champion, submission, `evolve/cascade.py`, or parent-selection
logic was modified or even read-for-modification-purposes this phase. No
mutation weighting, complexity-gate preference, parent-selection bonus, or
"sell melons more" heuristic was written, proposed in code, or integrated
anywhere. This phase is pure statistical analysis of existing + newly-mined
replay data, per Grace's explicit 4A-only scope; **Phase 4B (causal
intervention / policy modification) was not started, and no performance or
causal claim is made anywhere in this report.**

## Recommended next steps (not acted on; Phase 4B requires separate authorization)

1. If Phase 4B is ever authorized, the melon divergence found here is now
   the best-supported candidate to test causally (e.g. via a controlled
   counterfactual replay, per Phase 1's "Phase 6" infrastructure gap note) -
   but that authorization has not been given and nothing here should be
   read as recommending it.
2. A finer opportunity gate (accounting for price favorability at the
   moment of the opportunity, not just stock > 0) would sharpen the
   "opportunity" definition further, purely as a measurement improvement.
3. The opponent-heterogeneity finding (bimodal near-always-sell vs
   near-never-sell opponent sub-populations) could itself be worth a
   dedicated descriptive pass if useful for understanding the competitive
   field generally - noted as an observation, not a recommendation to act.
