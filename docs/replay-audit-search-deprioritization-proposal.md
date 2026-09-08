# Proposal: How Replay-Audit Parity Findings Could Inform Search Deprioritization

> **IMPLEMENTED (2026-09-08, after Grace's approval): Option A below has
> been built.** `evolve/deprioritized_params.yaml` is the human-maintained
> exclusion list; `evolve/space.py::mutate()` now takes a
> `respect_deprioritized` parameter (default: on, via the
> `EVOLVE_RESPECT_DEPRIORITIZED` env var — see `_deprioritization_default()`
> and `mutate()`'s docstring in `evolve/space.py` for the full reasoning).
> Only the two seeded `params:` entries (`fert_keep`, `fert_buy`,
> `fert_carry`) are actively enforced; the `blocks:` entry for chore's
> `dispatch` execution block is documented in the YAML file but **not yet
> wired** (would require touching `evolve/operators.py`, which this pass
> deliberately left untouched). A correctness smoke test (mutate() with the
> flag on/off, ~1000 sampled mutations) is done; **the controlled ablation
> study `mutate()`'s docstring calls for is explicitly not done and remains
> future work.** The rest of this document is the original proposal,
> preserved as written before implementation.

**Status (as originally written): PROPOSAL ONLY. Nothing in this document
has been implemented.** `evolve/cascade.py`, `evolve/space.py`,
`evolve/operators.py`, and every other mutation/search file were
unmodified at the time this document was first published. This document
existed for Grace to read and decide on, not as a spec already acted on -
see the IMPLEMENTED note above for what has since changed.

Motivating question: fertilizer and chore came back as genuine
decision-resolution parity (Phase 2 - no behavioral divergence between
Grace's play and the pooled opponent field). How would the evolution
engine actually "know" to stop spending mutation/search budget on those
dimensions?

## 1. How mutation/search currently decides what to perturb (as found in code)

Read `evolve/space.py`, `evolve/operators.py`, `evolve/crossover.py`,
`evolve/cascade.py`. Concretely:

- **The search space is a flat dict** (`space.SPACE = {**KNOB_SPACE,
  **CONST_SPACE}`, `evolve/space.py` lines ~55-112) - ~50 named parameters
  (`melon_floor`, `fert_keep`, `fert_buy`, `fert_carry`, `wheat_cap`,
  `spec_units_STRAWBERRY`, `MAX_HANDS`, etc.), each with a declared type
  (`int`/`float`/`cat`) and range/choice set.
- **`space.mutate()`** (lines 202-225) is a **uniform random mutator**:
  each active param is independently mutated with probability `rate`
  (default 0.2), or if none hit, exactly one is chosen uniformly at random
  (`rng.choice(names)`). Categorical params jump to a uniformly-chosen
  different value; numeric params get Gaussian noise scaled to the
  param's own range. **The function's own docstring is explicit: "There
  is NO automatic weighting by param_importance, score spread, or recent
  failure patterns. Any future attempt to bias mutation using
  observational signals from the archive must be introduced behind an
  explicit flag and tested against uniform mutation with a controlled
  ablation."** This is the single most load-bearing fact for this
  proposal - the project has already pre-committed, in code comments, to
  exactly the caution Grace has shown throughout this audit.
- **`operators.py::paired_mutate`** (lines 103-116) forces every mutation
  to touch one key from `ECON_KEYS` and one from `EXEC_KEYS` -
  `EXEC_KEYS` is a small, hand-picked, explicitly-named set (`min_hands,
  load_per_hand, early_hire_days, harvest_min, MAX_HANDS, ROUTE_LEN,
  CROP_SWEEP_LEN, CROP_SWEEP_RADIUS, NEAR_RADIUS` - lines 36-39);
  everything else in `SPACE` (including `fert_keep`/`fert_buy`/
  `fert_carry`/`melon_floor`) falls into `ECON_KEYS` by exclusion (line
  51: `ECON_KEYS = sorted(_ALL_SPACE_KEYS - EXEC_EXPLICIT -
  UNKNOWN_EXPLICIT)`). Within each pool, selection is still uniform
  (`rng.choice(econ_pool)`, `rng.choice(exec_pool)`).
- **`operators.py::block_pair_mutate`** (lines 139-160) additionally swaps
  one "execution block" (`sweep, animal_routing, dispatch,
  crop_admission` - `EXEC_BLOCK_NAMES`, line 63) for a uniformly-chosen
  alternative implementation from `evolve/blocks/`. **Chore-priority
  ordering, specifically, is not a named `SPACE` parameter at all** - it
  most plausibly lives inside the `dispatch` execution block's
  implementation, not as a tunable knob, which means it is currently
  reachable by mutation only via a full block swap, never a targeted
  parameter nudge. This is worth flagging as a structural gap independent
  of the deprioritization question: there may be no clean "chore
  dimension" to deprioritize at the parameter level at all.
- **`cascade.py`** evaluates and reports on candidates but its own comment
  (line 11) states it is "**Never used for selection of parents --
  reporting only**." Parent selection is a separate mechanism this
  document did not need to re-trace in full, since every option below
  only touches the mutation-*proposal* stage (`space.mutate` /
  `operators.paired_mutate` / `block_pair_mutate`), not parent selection,
  consistent with the hard constraint not to touch parent-selection logic.

**Bottom line**: there is currently no weighting mechanism of any kind -
every parameter and every execution block is equally likely to be chosen
for mutation, all the time, regardless of any audit finding. A "deprioritize
fertilizer and chore" signal does not yet have anywhere to plug in.

## 2. Three concrete, minimally-invasive options

### Option A - Human-maintained exclusion/low-weight list

A small, hand-edited file (e.g. `evolve/deprioritized_dimensions.json` or
a new section in `evolve/RULES.md`, which already documents empirical
constraints like the "Routing oracle" note cited in `operators.py`'s
docstring) listing parameter names and execution-block names a human has
decided to exclude or down-weight, with a one-line citation to the audit
finding that justifies each entry. `space.mutate()` / `operators.py`'s
pools would read this list at import time and either remove listed names
from `_active_names()`/`ECON_KEYS`/`EXEC_KEYS`, or (softer) give them a
reduced selection probability instead of a hard exclusion.

- **Risk**: low. A human reads an audit report, writes a few lines to a
  plain file, and can revert or edit it in one line at any time. No
  automated pipeline reads or writes replay data.
- **Reversibility**: trivial - delete the line, or the whole file.
- **Fits the existing pattern**: yes - this is structurally identical to
  how `evolve/RULES.md` already encodes hand-verified empirical findings
  ("Routing oracle": freeing the router is ~0 EV; copying opponent
  allocation loses -$68k) that shape `operators.py`'s `EXEC_EXPLICIT` set.
  This option is not a new mechanism, it is the same mechanism the project
  already uses, applied to a new source of findings.

### Option B - Automated weight-adjustment fed by FINDINGS.json

A script reads `artifacts/replay_state_policy_audit/FINDINGS*.json` files,
maps each finding's subject (crop, fertilizer, chore, hiring, melon) to
`SPACE` parameter names via a lookup table, and automatically computes a
per-parameter mutation-probability multiplier (e.g. parity findings ->
multiplier < 1, unresolved/promising findings -> multiplier = 1) that
`space.mutate()` consults instead of uniform `rng.choice`.

- **Risk**: high. This directly contradicts `space.mutate()`'s own
  docstring warning (quoted above) unless the "explicit flag and
  controlled ablation" precondition it names is built first - and even
  then, it means search behavior silently changes whenever a new
  `FINDINGS*.json` file is written, without a human reviewing the specific
  new content. A malformed or premature finding (this audit chain has
  already produced several PLAUSIBLE_BUT_UNPROVEN and later-corrected
  findings - see the Phase 4A provenance correction) would automatically
  and silently reshape search.
- **Reversibility**: moderate - the code change itself is revertible, but
  any candidates/archive state produced while it was active is not
  cleanly undoable, and diagnosing *why* a given run behaved differently
  becomes harder once weighting is a moving, data-driven target rather
  than a fixed, readable table.
- **Fits the existing pattern**: no - this is a new class of mechanism the
  project has not built anywhere else, and its introduction is exactly
  what `space.mutate()`'s docstring pre-emptively gates behind conditions
  ("explicit flag," "controlled ablation... measuring both held-out
  performance and diversity/novelty metrics") that neither this proposal
  nor any prior audit phase has satisfied.

### Option C - Manual, one-time parameter-range narrowing (a middle ground)

Rather than an ongoing weighting mechanism (automated or list-based), a
human periodically reviews audit findings and, for a *specific* parameter
confirmed at parity (e.g. `fert_keep`/`fert_buy`/`fert_carry`), manually
edits that parameter's entry in `KNOB_SPACE`/`CONST_SPACE` to a narrower
range or a single fixed value (effectively freezing it), the same way a
human would tune any other knob's declared range. No new file, no new
selection mechanism - just a direct, reviewed edit to the existing
`SPACE` table, functionally removing the parameter from consideration
without adding a parallel weighting layer.

- **Risk**: low-moderate. Lower than Option B (no automated pipeline), but
  higher than Option A (it changes `SPACE` itself rather than reading a
  side list, so it is a direct edit to `evolve/space.py`, the file this
  whole checklist is most cautious about).
- **Reversibility**: easy (revert the range in a follow-up edit) but less
  granular than Option A - it is an edit to core search-space code, not a
  standalone, diffable exclusion list a non-engineer could review at a
  glance.
- **Fits the existing pattern**: partially - `SPACE` ranges are already
  hand-tuned by a human (see the existing range choices throughout
  `KNOB_SPACE`/`CONST_SPACE`), so this is not a new mechanism, but it
  conflates "audit-driven deprioritization" with "ordinary knob tuning" in
  a way that would make it harder to later ask "which ranges were narrowed
  *because of a replay-audit finding* specifically."

## 3. Not implemented

Per the explicit instruction, none of the above was implemented.
`evolve/space.py`, `evolve/operators.py`, `evolve/cascade.py`, and every
other search/mutation file remain exactly as they were before this
document was written - verified via `git status` alongside this document's
publication (no diff against any file under `evolve/`).

## 4. Worked example: fertilizer and chore under each option

Using the real parameters found in step 1 (`fert_keep`, `fert_buy`,
`fert_carry` in `KNOB_SPACE`; chore has no dedicated `SPACE` parameter,
only the `dispatch` execution block):

- **Option A** (human-maintained list): add three lines to
  `evolve/deprioritized_dimensions.json` (or a new `evolve/RULES.md`
  section) naming `fert_keep`, `fert_buy`, `fert_carry`, each citing
  "Phase 2 parity finding, `REPORT_PHASE2.md`," with a hard exclusion (or
  a 0.2x multiplier) from `ECON_KEYS`'s effective pool. For chore: since
  there is no dedicated parameter, the entry would instead target the
  `dispatch` block in `EXEC_BLOCK_NAMES`'s pool for `block_pair_mutate`,
  again citing Phase 2 - though this is a coarser lever (it deprioritizes
  the *entire* dispatch-block-swap axis, not a specific chore-priority
  sub-behavior, since none is separately named in code).
- **Option B** (automated): a lookup table entry mapping the string
  `"fertilizer"` -> `["fert_keep", "fert_buy", "fert_carry"]` and
  `"chore"` -> `["dispatch"]` (block name), with a script that scans
  `FINDINGS_PHASE2.json` for confidence-tier `DIRECTLY_OBSERVED` +
  parity-shaped `observed` text, and mechanically reduces those
  parameters'/blocks' selection weight. This is exactly the kind of
  "observational signal from the archive" `space.mutate()`'s docstring
  says must not happen without an explicit flag and ablation study first
  - so this worked example itself illustrates why Option B is the
  higher-risk choice, not a neutral one.
- **Option C** (range narrowing): edit `KNOB_SPACE["fert_keep"]`,
  `["fert_buy"]`, `["fert_carry"]` in `evolve/space.py` directly - e.g.
  collapse each `("int", lo, hi, step)` to a single fixed value at its
  current default, removing it from effective mutation. Chore again has
  no clean lever here, for the same reason as Option A.

## Recommendation

**Option A (human-maintained exclusion/low-weight list).** This follows
directly from what was actually found in the code, not asserted:
`space.mutate()`'s own docstring already states the project's policy on
observational-signal-driven weighting almost verbatim ("must be introduced
behind an explicit flag and tested against uniform mutation with a
controlled ablation") - a policy Option B does not satisfy and this
proposal does not attempt to satisfy on Option B's behalf. `evolve/RULES.md`
already demonstrates the project encodes exactly this kind of
human-verified, citation-backed empirical constraint today (the "Routing
oracle" note), so Option A is not a new pattern being introduced for this
purpose - it is the existing pattern, applied to a new source (this audit
chain) of the same kind of finding. It is also the cheapest to reverse and
the easiest for a non-engineer (including a future reader who is not
Grace) to audit at a glance, which matches the caution this project has
shown at every phase of this audit chain (the promotion-criteria doc's own
finding that nothing has cleared the bar for automated promotion applies
with equal force here - Option B is, structurally, a form of automated
promotion of audit findings into search behavior). Option C is a reasonable
fallback if Grace later wants deprioritization to look like ordinary knob
tuning rather than a separate, explicitly-audit-sourced list, but Option A
is the better default because it keeps the audit-provenance visible as its
own artifact rather than folding it into `SPACE`'s general tuning history.
