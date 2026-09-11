# AGE-360 — Remaining-horizon ROI for investments and production

**Status:** delivered, Sep 11 2026. Tool `tools/horizon_roi.py`, contract tests `tests/test_horizon_roi.py`,
artifact `artifacts/horizon_roi/latest.json`, report section in `evolve/report.py::horizon_roi_section`.

The ticket's question, in the form a human actually asks it:

> Is there enough game left for this purchase to pay back?

The chassis answers that today with hand-tuned proxies — buy until day X, herd until day Y, hire under
condition Z. This delivers the measurement those proxies are standing in for.

---

## 1. Measurement approach

**Counterfactual, not accounting.** The obvious way to build an ROI matrix is analytic: acquisition cost,
operating cost per remaining hour, expected marginal return per cycle, subtract, divide. Every term in that
formula is a modelling assumption, and the interaction term the ticket asks about ("does buying a worker now
make a later animal purchase more or less valuable?") is exactly the term such a formula cannot carry.

Against a deterministic tape with `KAGG_FIXED_SHOPS=1` the whole game is deterministic, so we can just run
the counterfactual instead. Two modes:

| mode | what it blocks | what the number means |
|---|---|---|
| `cutoff` | every order of investment type T from day D to the end of the game | realized remaining-horizon return of continuing to invest in T from day D onward |
| `defer` | type T for days `[D, D+K)`, then allowed again | cost of postponing that class by K days — negative means waiting was free or better, i.e. option value |

`roi = base_final_money − counterfactual_final_money`.

Because the counterfactual policy plays out the entire rest of the game with that cash free to deploy
elsewhere, a single subtraction already nets out all four terms the ticket lists:

- **acquisition cost** — the cash is never spent in the counterfactual
- **operating cost** — feed, fuel and upkeep for the asset are likewise never incurred
- **opportunity cost** — the freed cash is reallocated by the unchanged policy, not left idle
- **interaction with other investments** — downstream purchases see the changed cash and board state

That is the whole argument for this design. It is also the reason the number is a *realized* return on these
tapes rather than an expectation, which matters for how far it can be pushed (§5).

**Payback horizon** is measured on **cash**, not net worth. Net worth counts a just-bought animal at roughly
its purchase price, so it hides the outlay the payback period is defined against; the cash series shows the
dip and its recovery. `payback_day` is the first day *after* the cutoff on which the investing run's cash has
overtaken the non-investing run's **and stays ahead to the end of the game**. Day D itself is excluded: it is
sampled at the first turn of the day, before the blocked orders would have been placed, so delta there is
identically zero and would read as instant payback. A lead that opens and then closes again is not payback.
Both traps produced plausible-looking wrong tables during development and are pinned by tests.

**Acquisition cost is observed, not assumed.** The tool records every investment order the base runs actually
place, with quantity, estimated cost and day range. `HIRE` (fibonacci schedule) and `BUY_LAND` (computed
price) are not market goods, so their cost is reported as `n/a` rather than silently as $0.

**Uncertainty.** Each `(candidate, tape, seed, type, day)` cell is an *exact* counterfactual — there is no
sampling error inside a cell, and a repeat run returns the identical number. All the uncertainty is *across*
cells: different tapes and seeds are different games. So the CI is a genuine across-the-field CI, and n is
the cell count, not a game count. `aggregate` deduplicates by cell so that chunked or repeated runs cannot
inflate n.

---

## 2. Integration points

1. **`tools/horizon_roi.py`** — the instrument. Reuses `mini_engine` and the same `networth` valuation as
   `tools/delay_counterfactual.py`, so the two tools' traces are directly comparable.
2. **`--json <file>`** — one JSONL row per cell (`type`, `day`, `tape`, `seed`, `base`, `cf`, `roi`,
   `payback_day`). This is the collection point: append across runs, pool later.
3. **`--aggregate <jsonl> --emit`** — pools a JSONL into `artifacts/horizon_roi/latest.json` plus a
   timestamped copy. Also the resume path: a long sweep runs as one `--types` slice per call and pools at
   the end, which is what makes this usable under the sandbox's command timeout.
4. **`evolve/report.py::horizon_roi_section`** — renders `latest.json` into the run report if present, with
   the caveat text attached. Wired, not merely documented. It is a reading aid: nothing in the loop writes
   the artifact and nothing reads it back into search.

Note on `--tapes panel`: the 4-tape list is duplicated from `evolve/batch_vs_o8.py`. Keep them in sync.

---

## 3. Example analysis — `candidates/O17_ORCH_CAPITAL.py`, 4-tape panel, `KAGG_FIXED_SHOPS=1`

Observed acquisition spend in the base runs, per game:

| class | orders | units | est. cost | days active |
|---|---:|---:|---:|---|
| `BUY_SEED:STRAWBERRY` | 9.2 | 56.6 | ~$9,771 | 5–16 |
| `BUY_PRODUCT:WHEAT` (feed) | 31.7 | 243.0 | ~$9,729 | 0–28 |
| `BUY_SEED:MELON` | 2.0 | 11.5 | ~$2,894 | 0–10 |
| `BUY_ANIMAL:COW` | 3.1 | 7.2 | ~$2,867 | 0–16 |
| `BUY_ANIMAL:SHEEP` | 2.1 | 5.1 | ~$2,542 | 0–11 |
| `BUY_PRODUCT:FERTILIZER` | 17.3 | 46.3 | ~$1,931 | 14–26 |
| `HIRE` | 266.9 | 266.9 | n/a | 0–29 |
| `BUY_LAND` | 2.3 | 2.3 | n/a | 7–14 |

### 3.1 What holds up (n=32 cells: 4 tapes × 8 seeds)

| class | from day | ROI | t | 95% CI | cells + | payback |
|---|---:|---:|---:|---|---:|---|
| `HIRE` | 14 | +$58,984 | 8.97 | [+46,102, +71,867] | 100% | by day 15 |
| `HIRE` | 18 | +$44,291 | 9.10 | [+34,746, +53,835] | 100% | by day 19 |
| `HIRE` | 22 | +$27,209 | 7.39 | [+19,990, +34,427] | 100% | by day 23 |
| `HIRE` | 26 | +$12,805 | 9.78 | [+10,238, +15,371] | 100% | by day 27 |
| `BUY_PRODUCT` | 14 | +$22,151 | 4.29 | [+12,032, +32,269] | 78% | by day 19 |
| `BUY_PRODUCT` | 18 | +$13,697 | 3.84 | [+6,709, +20,685] | 62% | by day 22 |
| `BUY_PRODUCT` | 22 | +$10,598 | 4.44 | [+5,916, +15,279] | 81% | by day 25 |
| `BUY_PRODUCT` | 26 | +$4,647 | 5.85 | [+3,090, +6,205] | 94% | by day 29 |
| `BUY_SEED` | 14 | +$6,720 | 7.51 | [+4,966, +8,474] | 97% | by day 24 |
| `BUY_SEED` | 18 | +$3,991 | 6.01 | [+2,689, +5,293] | 94% | by day 26 |
| `BUY_SEED` | 22 | +$2,252 | 6.07 | [+1,525, +2,979] | 91% | by day 29 |
| `BUY_SEED` | 26 | $0 | — | — | 0% | never (no orders placed) |

Three readings:

**Labor and feed never run out of horizon.** With four days left, blocking hiring still costs $12,805 and
blocking feed still costs $4,647, both at t≈6–10 and on 94–100% of cells, both paying back the next day or
two. The "is there enough game left" question has a clean answer for these classes: yes, always, right up to
day 29. Any threshold that tapers labor or feed toward the end of the game is giving away money, and the
counterfactual says how much.

**Seed is the one class with a visible horizon limit.** Its ROI decays by roughly half per four days
(+$6,720 → +$3,991 → +$2,252) and its payback day marches toward the buzzer (day 24 → 26 → 29). The last
purchases the policy makes, around day 22–25, are recovering their cost on day 29 — the final day. That is
the real "buy until day X" boundary, measured rather than tuned, and the policy has landed close to it.

**The instrument reproduces the known result on its own terms.** `BUY_SEED` from day 26 is exactly $0 on
every cell because the policy places no seed orders after day 25. Exact zeroes are the tool confirming it is
measuring the right thing, and they are how you read off what the policy's *implicit* cutoffs already are.

### 3.2 Decomposing the feed result: it is all wheat, none of it fertilizer

`BUY_PRODUCT` covers two very different things — wheat bought as animal feed, and fertilizer. Splitting them
(n=32) shows the aggregate number was entirely one of them:

| class | from day | ROI | t | 95% CI | cells + |
|---|---:|---:|---:|---|---:|
| `BUY_PRODUCT:WHEAT` | 16 | +$17,487 | 4.10 | [+9,124, +25,850] | 66% |
| `BUY_PRODUCT:WHEAT` | 20 | +$10,597 | 3.75 | [+5,059, +16,135] | 59% |
| `BUY_PRODUCT:WHEAT` | 24 | +$6,874 | 4.74 | [+4,033, +9,715] | 91% |
| `BUY_PRODUCT:FERTILIZER` | 16 | +$105 | 0.40 | [−409, +620] | 38% |
| `BUY_PRODUCT:FERTILIZER` | 20 | +$274 | 1.06 | [−231, +779] | 47% |
| `BUY_PRODUCT:FERTILIZER` | 22 | +$201 | 1.42 | [−76, +479] | 44% |
| `BUY_PRODUCT:FERTILIZER` | 24 | +$156 | 1.20 | [−99, +411] | 25% |

**Feed is load-bearing to the last day; late fertilizer is a null lever.** The policy spends ~$1,931 per game
on fertilizer across 17.3 orders, and blocking all of it from day 16 onward changes the outcome by $105 with
a CI that straddles zero — and does so at *every* cutoff tested. Read correctly this is not "stop buying
fertilizer and pocket $1,931": the counterfactual already lets the policy redeploy that cash, so a near-zero
ROI means the two uses are a wash. It means the lever is dead — money in, roughly the same money out,
whichever way it is set.

That converges with two results reached by completely different routes. The replay state-policy audit
(Phase 2) deprioritized `fert_keep` / `fert_buy` / `fert_carry` in `evolve/deprioritized_params.yaml` on a
*behavioural parity* argument — my play and the opponent field resolve fertilizer decisions the same ~92% of
the time. And O14 (melon late-fertilization on O12) was declined on the tape panel at −2.6k. Parity says
"nobody differentiates here"; the panel says "one specific late-fert mechanism loses"; this says "the capital
itself earns nothing either way, at any late cutoff". Three independent arguments, same conclusion.

### 3.3 What did not hold up — and why that is the headline

The first pass ran on the project's usual 12-cell panel (4 tapes × 3 seeds), the same depth used for margin
comparisons, and produced two findings that looked immediately actionable:

- `BUY_ANIMAL` from day 6: **−$2,618**, and from day 10 **−$1,008 (t = −2.03)** — buying animals past day 6
  appears to destroy value, against a policy that buys cows to day 16.
- `BUY_ANIMAL` deferred 3 days at day 0: **−$6,357 (t = −4.64)** — the opening animal purchase appears to be
  worth $6.4k *more* if made three days later.

Both dissolved on re-measurement:

| finding | 12 cells | deeper |
|---|---|---|
| `BUY_ANIMAL` cutoff day 6 | −$2,618 (t=−1.80) | **+$4,372 (t=1.36)**, n=24 — sign flipped |
| `BUY_ANIMAL` cutoff day 10 | −$1,008 (t=−2.03) | absorbed into the same noise band |
| `BUY_ANIMAL` defer 3d at day 0 | −$6,357 (t=−4.64) | **−$1,134 (t=−0.80)**, n=32 |

**The 12-cell margin panel is not deep enough for this measurement.** That panel works for its own job
because it is a *paired* comparison: two policies, same tape, same seed, differing by one mechanism, so most
of the game's variance cancels. Blocking an entire investment class does not cancel — it changes the
trajectory wholesale, and the across-cell dispersion is correspondingly fat. `BUY_ANIMAL` and `BUY_LAND` are
also the lumpiest classes (2–3 orders per game, $400–500 a unit), so a single cell can swing thousands.

The practical rule: **lumpy capital classes need ≥24–32 cells before their sign is worth reading; flow
classes (labor, feed, seed — hundreds of orders per game) are stable at 12.** A wide CI in this table is the
instrument telling you the panel is too thin for that class, not that the class does not matter.

This is also why the tool reports `t`, a CI, *and* the fraction of cells positive. `BUY_PRODUCT` from day 18
has t=3.84 on only 62% of cells — a real effect carried by a minority of large wins, which is a different
object from `HIRE`'s 100%-of-cells result and should not be read the same way.

---

## 4. How ROI signals feed into decisions

**Observational only. Nothing here is wired to mutation weighting, and nothing should be.** The artifact is
written by hand and read by `report.py` for display. The search does not see it.

The reason is a limitation, not caution for its own sake: **this instrument can only measure the ROI of what
the policy does, never of what it does not do.** It removes investments; it cannot add them. So it can tell
you that the last seed purchases around day 22–25 pay back on day 29, but it cannot tell you whether a
purchase on day 26 would have. A zero crossing in the ROI curve is *not* an optimal cutoff day — downstream
policy behaviour is held fixed, and the optimum is off the end of what the counterfactual can see.

What it is for is **ranking which thresholds are worth a forward experiment.** The workflow:

1. Run the sweep; read which classes still have positive ROI at their current implicit cutoff (§3.1's exact
   zeroes show where each cutoff currently sits).
2. A class whose ROI is still clearly positive at the last day it is used is a candidate for *extending* —
   propose a candidate with the cap raised and put it through the normal promotion gate.
3. A class whose ROI has gone flat or negative well before its last use is a candidate for *tightening*.
4. Either way the ROI number is the hypothesis; the paired panel margin is still the verdict. The promotion
   gate does not move.

This mirrors how `evolve/deprioritized_params.yaml` already works — a human reads a report, and edits a file
with a citation to the specific finding. It deliberately does not mirror `param_exploration`, whose numbers
carry a standing warning that they are exploration weights and not causal importance. These numbers *are*
causal, per cell. Their weakness is dispersion across cells, which is a different failure mode and is handled
by reporting n, t, CI and positive fraction rather than by a blanket caveat.

On the current evidence the honest list is short, and most of it is *not* a call to change code:

- **Labor and wheat feed are already right, and that is worth knowing.** Both return thousands from day 26
  with next-day payback, and per-day order counts show neither actually tapers — hiring rises to ~13
  orders/day by day 24 and wheat feed holds ~1 order/day out to day 28. So there is no late-game taper to
  remove. The contribution here is negative-result confidence: two of the largest spending lines need no
  horizon guard at all, and time spent tuning one is time wasted.
- **Late fertilizer is a confirmed dead lever** (§3.2), now on a causal footing rather than a parity
  argument. It stays deprioritized; the citation in `evolve/deprioritized_params.yaml` can be strengthened
  with this measurement, and nothing else changes.
- **No tightening elsewhere is justified.** Neither animal nor land purchasing has a defensible negative ROI
  at adequate depth; the apparent ones were lottery noise (§3.3).
- **One measurement gap, and it is the only item that needs work:** `BUY_ANIMAL` and `BUY_LAND` want a
  32-cell sweep across days 4–12 before anyone touches the herd or land thresholds, which are currently set
  by hand and are the two classes this pass could not resolve.

Note what the table does *not* contain: a threshold to change today. That is the expected outcome for a first
pass on a chassis whose flow-investment thresholds have already been tuned hard. The value delivered is
knowing which of them are load-bearing (labor, feed, seed timing), which are inert (late fertilizer), and
which are still unmeasured (animals, land).

---

## 5. Limitations

- **Removal only.** As above: cannot price an investment the policy never makes. The forward direction needs
  a candidate and the promotion gate.
- **Realized, not expected.** These are the returns on four specific tapes at specific seeds. The O15/O16
  local-versus-ladder gap is a live reminder that a number true on this panel need not transfer.
- **Class-level, not unit-level.** `cutoff` blocks a whole class from day D. It does not price the *marginal*
  Nth worker or Nth cow. Per-event marginal pricing is `tools/delay_counterfactual.py`'s job, at one-hour
  resolution.
- **Sell timing is not covered here.** Production *timing* ROI is already instrumented by the O12/O13/O15
  line of work and the delay counterfactual; blocking `SELL` wholesale is not a meaningful counterfactual.
  What this tool adds on the production side is crop-cycle ROI via `BUY_SEED:<CROP>` cutoffs.
- **Panel duplication.** `PANEL` in the tool restates the tape list in `evolve/batch_vs_o8.py`.

## 6. Reproducing

```bash
# broad sweep, chunked to fit the command timeout; one --types slice per call
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py candidates/O17_ORCH_CAPITAL.py \
    --tapes panel --seeds 1,2,3 --types HIRE,BUY_ANIMAL --days 2,6,10,14,18,22,26 \
    --json artifacts/horizon_roi/cutoff.jsonl --quiet
# ... repeat for the other --types slices, appending to the same jsonl ...

# depth check on the classes whose CI looked tight
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py candidates/O17_ORCH_CAPITAL.py \
    --tapes panel --seeds 1,2,3,4,5,6,7,8 --types BUY_SEED --days 10,14,18,22,26 \
    --json artifacts/horizon_roi/deep.jsonl --quiet

# option value
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py candidates/O17_ORCH_CAPITAL.py \
    --mode defer --defer-days 3 --types BUY_ANIMAL,BUY_LAND --days 0,2,4,6,8,10 \
    --json artifacts/horizon_roi/defer.jsonl

# pool everything and publish the artifact report.py renders
cat artifacts/horizon_roi/cutoff.jsonl artifacts/horizon_roi/deep.jsonl > artifacts/horizon_roi/all_cutoff.jsonl
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py x --aggregate artifacts/horizon_roi/all_cutoff.jsonl --emit

KAGG_FIXED_SHOPS=1 python3 tests/test_horizon_roi.py
```

Related: AGE-359 (`tools/delay_counterfactual.py`, marginal cost of a one-hour delay), AGE-361
(do/delay/abandon/switch — the purchase decision is the concrete instance of delay-vs-commit), AGE-362
(uncertainty and option value — `--mode defer` is the first instrument on that ticket's list, and §3.3's
depth finding is directly about how much evidence a direction needs before its sign is trustworthy).
