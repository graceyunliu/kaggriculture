# Replay-Audit Promotion Criteria

Standing checklist for when a finding from the replay-mining audit chain
(`artifacts/replay_state_policy_audit/` - Phases 1, 2, 3, 4A, 4B, and any
future phase) is allowed to influence the evolve loop, mutation weighting,
parent selection, or the champion, versus when it must remain a documented
hypothesis only. Written after Phase 4B, which is the audit chain's own
worked example of a finding that reached a real intervention test and
**still did not clear this bar** - the gaps it exposed are what this
checklist is built from.

## The bar

A finding may inform `evolve/cascade.py`, mutation weighting, parent
selection, or champion code **only if all of the following are true, and
only with explicit human sign-off on top of all of them**:

1. **Minimal, isolated intervention.** The test changed exactly one
   decision point, not a broad policy rewrite - verified as a byte-for-byte
   diff against a baseline (Phase 4B's variant files are the template: a
   single `KNOBS[...]` line changed, nothing else).
2. **Baseline genuinely represents the policy in question.** The baseline
   tested against must actually exhibit the behavior the finding is about,
   not merely be a convenient existing candidate. **Phase 4B's own failure
   mode belongs here as the canonical counter-example**: it tested the
   melon-floor knob against `candidates/C1.py`, a baseline whose OR-gated
   sell condition (`price >= floor OR day >= 27 OR shed_load > 75`) already
   sells melon almost unconditionally - nothing like the ~96%-hold behavior
   Phase 4A actually measured in Grace's real games. The test therefore
   measured the knob's effect on the wrong reference policy. **Any future
   finding must show the baseline's own behavior at decision-resolution
   (opportunity-conditioned action rate) is checked against the audit
   finding it's meant to represent, before results are trusted.**
3. **Matched-seed evaluation, then fresh-seed validation.** Both required,
   in that order, using the repo's existing seat-bias-controlled harness
   (`mini_engine.py --both-seats` or `seeded_h2h.py --both-seats`) - never
   a single-seat or `--swap-half` comparison (established repo-wide bias,
   see `seeded_h2h.py` module docstring).
4. **All relevant predictions checked separately, not collapsed.** At
   minimum: (a) does the isolated decision itself change, (b) does the
   intended downstream metric change (e.g. revenue, units), (c) does it
   produce the expected resource/cash consequence, (d) does any score
   effect survive fresh seeds. **A partial pass (e.g. (a) passes but
   (b)-(d) don't) is a distinct, reportable outcome - it must be reported
   as such, never rounded up to a single verdict.** Phase 4B is the
   template for this table shape.
5. **Explicit RNG classification carried through**, using the four-value
   taxonomy established in Phases 2-4 (`RNG_INDEPENDENT / RNG_EXPOSED /
   RNG_COUPLED / UNKNOWN`), **plus a side-effect audit for downstream
   RNG-pathway contamination even when the initial decision gate is
   `RNG_INDEPENDENT`.** Phase 4B found exactly this: the melon-sell gate
   itself is RNG-independent, but the intervened farm's own weed-spawn
   sequence diverged from baseline self-play in 2/20 seeds late-game - a
   downstream RNG-pathway effect a gate-level classification alone would
   have missed. Any future finding must run this same same-player /
   cross-player weed-sequence comparison before claiming RNG independence
   all the way through to the score effect.
6. **No promotion into mutation weighting, parent-selection bonuses, or
   champion code without all of the above AND explicit human sign-off.**
   This restates the project's established pattern (see
   `evolve/cascade.py`'s own docstring note, "Never used for selection of
   parents - reporting only," and `evolve/space.py::mutate`'s docstring:
   "There is NO automatic weighting by param_importance... Any future
   attempt to bias mutation using observational signals from the archive
   must be introduced behind an explicit flag and tested against uniform
   mutation with a controlled ablation"). Nothing in the replay-audit chain
   changes that pattern; it reinforces it.

## Current status of every audit-chain finding against this checklist

| Finding | Tier reached | (1) isolated | (2) representative baseline | (3) matched+fresh | (4) predictions separated | (5) RNG classified+side-effect audit | (6) human sign-off for promotion | What's missing before promotion |
|---|---|---|---|---|---|---|---|---|
| **Crop-mix** (strawberry vs wheat) | DIRECTLY_OBSERVED (Phase 1-2), never causally tested | N | N/A | N | N | RNG_EXPOSED/RNG_COUPLED (gate-level only) | N/A | No isolated intervention has ever been built or tested (Phases 1-4B never touched crop-mix as an intervention target - Phase 4B is melon-selling only). Status stays "observed, repeatable, RNG-exposed, not causal" per explicit instruction across Phases 3-4B; nothing here clears even criterion (1). |
| **Melon-selling** | STRONGLY_SUPPORTED for behavioral divergence (4A); intervention tested (4B) but **failed criterion (2)** | Y (4B) | **N - flagged failure mode above** | Y (4B, 20 matched + 10 fresh) | Y (4B reports (1)-(4) separately) | Y (RNG_INDEPENDENT gate + RNG_EXPOSED downstream side-effect found and reported) | Not sought / not applicable - 4B's own result doesn't support promotion | Needs a re-run of Phase 4B's intervention against a baseline whose opportunity-conditioned melon-sell rate actually resembles the audit's real finding (~96% hold), not C1's near-always-sell profile. Until that baseline-mismatch is fixed, this finding cannot advance past "diagnostic, inconclusive." |
| **Fertilizer** (apply/hold) | DIRECTLY_OBSERVED genuine parity, decision-resolution (Phase 2) | N/A (negative finding, no intervention attempted) | N/A | N/A | N/A | RNG_EXPOSED (gate-level, per Phase 2) | N/A | Never tested as an intervention (correctly - Phase 2's own parity result is the reason no further work was recommended). Per Part B of this doc, this is a candidate for *deprioritization*, not promotion - a fundamentally different checklist (see the companion proposal doc) applies to "spend less search budget here," not to "change the champion." |
| **Chore** (idle vs assigned) | DIRECTLY_OBSERVED genuine parity, decision-resolution (Phase 2) | N/A | N/A | N/A | N/A | UNKNOWN (Phase 2 could not classify chore-assignment RNG exposure confidently) | N/A | Same status as fertilizer: a parity finding, not a promotion candidate. RNG classification is the weakest of any finding in this chain (`UNKNOWN`) - if this dimension were ever revisited for any reason, resolving that classification would be a prerequisite even before considering deprioritization mechanics. |
| **Hiring** | NO_ROBUST_SIGNAL, and explicitly an *incomplete test* (Phase 2 and 3 both flag this, not a clean negative) | N/A | N/A | N/A | N/A | RNG_INDEPENDENT (gate fully reconstructed, Phase 3) | N/A | Not a promotion candidate and not (yet) a confirmed parity/deprioritization candidate either - Phase 3 reconstructed the true opportunity gate and found a small, non-alarming global rate gap (5.76% vs 6.97%), but this was never pushed to the same statistical rigor Phase 4A gave melon-selling. If anyone wants to act on hiring in either direction, it needs its own Phase 4A-equivalent scale-up first. |

**Summary**: as of this writing, **no finding in this audit chain has cleared
the full checklist** - melon-selling got the furthest (through criteria
1, 3, 4, 5) but failed criterion 2, and no finding has reached criterion 6
regardless. This is the expected, intended state: the checklist is
deliberately hard to clear, matching this project's demonstrated caution
about touching `evolve/cascade.py`, mutation weighting, or parent
selection.
