# AGE-360 — Remaining-horizon ROI for investments and production

**Status:** delivered Sep 11 2026; corrected and extended the same day with a marginal intervention mode.
Tool `tools/horizon_roi.py`, contract tests `tests/test_horizon_roi.py`, artifact
`artifacts/horizon_roi/latest.json`, report section in `evolve/report.py::horizon_roi_section`.

The ticket's question, in the form a human actually asks it:

> Is there enough game left for this purchase to pay back?

The chassis answers that today with hand-tuned proxies — buy until day X, herd until day Y, hire under
condition Z. This delivers the measurement those proxies are standing in for.

---

## 0. Read this first: class ablation is not marginal ROI

The first pass of this work shipped with one mode, `cutoff`, which blocks an entire investment class from
day D onward. That mode answers **"what is this whole subsystem worth?"** It does *not* answer **"what is
the next unit of this decision worth?"**, and the gap between those two questions is not small.

For lumpy capital the distinction barely matters. Blocking `BUY_LAND` from day 14 removes roughly one
purchase, so the cutoff number is already close to a marginal value.

For a class the policy **replenishes continuously** it matters enormously. This chassis places ~267 `HIRE`
orders per game, 11–13 every day, through a `need = hires_target - n_hands` top-up. Blocking `HIRE` from day
26 therefore does not remove the marginal late hire; it removes the workforce for the last four days.
Wheat feed is the same shape at ~1 order/day to day 28: blocking it starves the herd.

So the original headline, "labor and feed never run out of horizon", was measuring the value of *having* a
workforce and *feeding* the animals. Both true. Neither says anything about the current hire or feed
threshold. The `marginal` mode added in the correction asks the real question, and for hiring **the two
modes have opposite signs**:

| | intervention | ROI | reading |
|---|---|---:|---|
| `HIRE` cutoff, day 26 | remove all hiring | **+$12,805** (t=9.78) | having a workforce is worth a lot |
| `HIRE` marginal, day 24 | one fewer hire/day | **−$361** (t=−3.34) | the *last* hire each day costs more than it earns |

Both numbers are correct. Only the second one is about the threshold.

> **Evidence rule.** A class ablation measures the value of removing a subsystem. It must not be read as
> the marginal value of the last unit of investment unless the intervention demonstrably approximates a
> one-unit change. Check the class's orders-per-day before interpreting any cutoff row.

---

## 1. Measurement approach

**Counterfactual, not accounting.** The obvious way to build an ROI matrix is analytic: acquisition cost,
operating cost per remaining hour, expected marginal return per cycle, subtract, divide. Every term in that
formula is a modelling assumption, and the interaction term the ticket asks about ("does buying a worker now
make a later animal purchase more or less valuable?") is exactly the term such a formula cannot carry.

Against a deterministic tape with `KAGG_FIXED_SHOPS=1` the whole game is deterministic, so we run the
counterfactual instead. Three modes:

| mode | what it does | what the number means |
|---|---|---|
| `marginal` | allow at most (base units that day − K) units of T from day D on | realized value of the **last K units per day** of that class — the threshold question |
| `cutoff` | block every order of T from day D to the end | realized value of the **whole class** from day D on — the subsystem question |
| `defer` | block T for days `[D, D+K)`, then allow again | cost of postponing the class by K days; negative means option value in waiting |

`roi = base_final_money − counterfactual_final_money` throughout.

Because the counterfactual policy plays out the entire rest of the game with that cash free to deploy
elsewhere, a single subtraction already nets out all four terms the ticket lists: **acquisition cost** (never
spent), **operating cost** (feed and upkeep never incurred), **opportunity cost** (freed cash reallocated by
the unchanged policy, not left idle), and **interaction with other investments** (downstream purchases see
the changed cash and board). That is the whole argument for this design.

**The marginal cap is calibrated per cell, and per day.** The budget for day d is what *this exact cell's*
base run actually placed on day d, minus K. Two details that are load-bearing:

- *Per cell.* The same policy places different quantities against different tapes. A single global cap would
  be a different-sized intervention in every cell, and the CI would be measuring that variation rather than
  the effect.
- *Per day, not per turn.* These policies re-issue a shortfall later in the same day. A per-turn filter is
  silently absorbed and measures nothing. This failed exactly this way in development.

A third trap: recording order units *before* the intervention logs what the policy **wanted**, not what it
got — and a capped policy asks for *more*, because it keeps falling short of target. The first verification
pass read as "the cap increased purchases". All three are now pinned by
`test_marginal_cap_removes_exactly_k_units_per_day`.

**Payback horizon** is measured on **cash**, not net worth. Net worth counts a just-bought animal at roughly
its purchase price, so it hides the outlay the payback period is defined against. `payback_day` is the first
day *after* the cutoff on which the investing run's cash has overtaken the non-investing run's **and stays
ahead to the end of the game**. Day D itself is excluded: it is sampled at the first turn of the day, before
the blocked orders would have been placed, so delta there is identically zero and would read as instant
payback. A lead that opens and then closes again is not payback.

**Acquisition cost is observed, not assumed.** `HIRE` (fibonacci schedule) and `BUY_LAND` (computed price)
are not market goods, so their cost reports as `n/a` rather than silently as $0.

**Uncertainty.** Each `(candidate, tape, seed, type, day, intervention size)` cell is an *exact*
counterfactual — no sampling error inside a cell, and a repeat returns the identical number. All uncertainty
is *across* cells. So the CI is a real across-the-field CI and n is the cell count, not a game count.
`aggregate` deduplicates by cell **including intervention size**, so a −1 unit/day and a −2 unit/day sweep
cannot pool into one meaningless row.

---

## 2. Integration points

1. **`tools/horizon_roi.py`** — the instrument. Reuses `mini_engine` and the same `networth` valuation as
   `tools/delay_counterfactual.py`, so the two tools' traces are directly comparable.
2. **`--json <file>`** — one JSONL row per cell (`type`, `day`, `mode`, `reduce`/`defer_days`, `tape`,
   `seed`, `base`, `cf`, `roi`, `payback_day`). The collection point: append across runs, pool later.
3. **`--aggregate <jsonl> --emit`** — pools into `artifacts/horizon_roi/latest.json` plus a timestamped
   copy. Also the resume path: a long sweep runs as one `--types` slice per call and pools at the end,
   which is what makes it usable under the sandbox command timeout.
4. **`evolve/report.py::horizon_roi_section`** — renders `latest.json` into the run report, with an
   **intervention column** so a cutoff row can never be mistaken for a marginal one. Wired, not merely
   documented. Nothing in the loop writes the artifact and nothing reads it back into search.

`PANEL` in the tool duplicates the tape list in `evolve/batch_vs_o8.py`. Keep them in sync.

---

## 3. Results — `candidates/O17_ORCH_CAPITAL.py`, 4-tape panel, `KAGG_FIXED_SHOPS=1`

Observed acquisition spend in the base runs, per game: `BUY_SEED:STRAWBERRY` ~$9,771 (days 5–16),
`BUY_PRODUCT:WHEAT` ~$9,729 (days 0–28), `BUY_SEED:MELON` ~$2,894 (0–10), `BUY_ANIMAL:COW` ~$2,867 (0–16),
`BUY_ANIMAL:SHEEP` ~$2,542 (0–11), `BUY_PRODUCT:FERTILIZER` ~$1,931 (14–26), `HIRE` 266.9 orders (0–29,
cost n/a), `BUY_LAND` 2.3 orders (7–14, cost n/a).

### 3.1 Marginal results — the threshold question (n=32–64 cells)

| class | intervention | from day | ROI | t | 95% CI | cells + |
|---|---|---:|---:|---:|---|---:|
| `HIRE` | −1 unit/day | 8 | **−$1,907** | −2.64 | [−3,325, −489] | 28% |
| `HIRE` | −1 unit/day | 12 | **−$2,108** | −6.31 | [−2,763, −1,453] | 12% |
| `HIRE` | −1 unit/day | 16 | **−$832** | −3.82 | [−1,258, −405] | 19% |
| `HIRE` | −1 unit/day | 20 | **−$1,178** | −10.36 | [−1,401, −955] | 8% |
| `HIRE` | −1 unit/day | 24 | **−$361** | −3.34 | [−573, −150] | 9% |
| `HIRE` | −2 unit/day | 12 | +$153 | 0.24 | [−1,080, +1,385] | 59% |
| `HIRE` | −2 unit/day | 20 | −$531 | −1.77 | [−1,119, +58] | 22% |
| `BUY_SEED` | −1 unit/day | 12 | +$825 | 3.29 | [+334, +1,316] | 91% |
| `BUY_SEED` | −1 unit/day | 16 | +$710 | 3.68 | [+331, +1,088] | 91% |
| `BUY_SEED` | −1 unit/day | 20 | +$444 | 4.11 | [+232, +656] | 84% |
| `BUY_SEED` | −1 unit/day | 24 | +$216 | 2.92 | [+71, +360] | 75% |
| `BUY_PRODUCT:WHEAT` | −1 unit/day | 12 | +$246 | 0.71 | [−430, +923] | 44% |
| `BUY_PRODUCT:WHEAT` | −1 unit/day | 16 | +$262 | 1.49 | [−82, +606] | 53% |
| `BUY_PRODUCT:WHEAT` | −1 unit/day | 20 | +$335 | 2.09 | [+20, +649] | 53% |

**Hiring is over-provisioned by about one unit per day, at every point in the game.** Removing one hire per
day is worth $361 to $2,108 depending on the start day, significant everywhere (t = −2.6 to −10.4), and
positive in only 8–28% of cells. This replicates on held-out seeds 9–16 (day 12: −$2,892, t=−7.20, **0% of
cells positive**; day 20: −$1,393, t=−10.06) and shows a clean dose-response: at −2 units/day the gain
collapses to +$153 (t=0.24) at day 12 and weakens to −$531 at day 20. That is the signature of a true local
optimum roughly one unit below where the policy sits, not a monotone "hire less is better" gradient.

This is the only actionable threshold finding in the whole pass, and it is the exact opposite of what the
cutoff table appeared to say.

**The marginal tile earns its cost, through day 24.** `BUY_SEED` at −1 unit/day is positive at every start
day, significant from day 12 (t = 2.9–4.1), positive in 75–91% of cells, decaying toward the buzzer
(+$825 → +$216). See §3.4 for why this matters more than its size suggests.

**Marginal feed is roughly break-even.** +$246 to +$335, CI straddling zero except marginally at day 20.
Neither a lever nor a leak.

### 3.2 Class results — the subsystem question

Read these as "what is this subsystem worth", never as thresholds.

| class | intervention | from day | ROI | t | cells + |
|---|---|---:|---:|---:|---:|
| `HIRE` | class blocked | 26 | +$12,805 | 9.78 | 100% |
| `BUY_PRODUCT` | class blocked | 26 | +$4,647 | 5.85 | 94% |
| `BUY_SEED` | class blocked | 14 | +$6,720 | 7.51 | 97% |
| `BUY_SEED` | class blocked | 22 | +$2,252 | 6.07 | 91% |
| `BUY_SEED` | class blocked | 26 | $0 | — | 0% (no orders placed) |

The exact zero at day 26 is the tool confirming it measures what it claims, and is how to read off the
policy's *implicit* cutoffs: seed purchasing already stops at day 25.

### 3.3 Decomposing the feed class: all wheat, no fertilizer

Splitting `BUY_PRODUCT` (n=32, class-blocked):

| class | from day 16 | day 20 | day 24 |
|---|---:|---:|---:|
| `BUY_PRODUCT:WHEAT` | +$17,487 (t=4.10) | +$10,597 (t=3.75) | +$6,874 (t=4.74) |
| `BUY_PRODUCT:FERTILIZER` | +$105 (t=0.40) | +$274 (t=1.06) | +$156 (t=1.20) |

**Late fertilizer is a null lever.** ~$1,931/game across 17.3 orders, and removing all of it from day 16
changes the outcome by $105 with a CI straddling zero, at every cutoff tested. This is one of the few
classes where the cutoff *is* informative about the decision, because the question is whether to run the
subsystem at all. It is not "stop buying fertilizer and pocket $1,931": the counterfactual already
redeploys that cash, so near-zero ROI means the two uses are a wash and the lever is dead.

That converges with two results reached by different routes: the Phase 2 replay audit deprioritized
`fert_keep`/`fert_buy`/`fert_carry` on behavioural parity (~92% hold in both cohorts), and O14 (melon
late-fertilization) was declined on the tape panel at −2.6k. Parity says "nobody differentiates here"; the
panel says "this specific mechanism loses"; this says "the capital earns nothing either way".

### 3.4 The workload-generation question, answered

Two live hypotheses pointed opposite ways. **(A)** The farm is over-committed: the v10-era execution picture
shows ~58–60% of worker time in movement, so perhaps the farm generates more obligations than its labor can
service, and the bottleneck is workload *generation*, not worker *selection*. **(B)** Additional production
still has economic value.

The marginal seed result discriminates them, and it favours (B): the marginal tile is worth +$825 at day 12
and still +$216 at day 24, positive in 75–91% of cells. The farm is **not** over-planted. It is
inefficiently executing a workload that is nevertheless worth doing.

The marginal hire result completes the picture from the other side: labor is *over*-provisioned by about one
unit per day while the tiles those workers service are *under*-provided at the margin. Taken together these
say the chassis is buying too much labor and putting it to work on too few obligations, which is a different
diagnosis from either hypothesis as originally stated, and it points at the productivity of an added worker
rather than at the number of tiles.

### 3.5 What did not hold up — the depth lesson

The first pass ran on the project's usual 12-cell panel (4 tapes × 3 seeds), the depth used for margin
comparisons, and produced two findings that looked immediately actionable. Both dissolved:

| finding | 12 cells | deeper |
|---|---|---|
| `BUY_ANIMAL` cutoff day 6 | −$2,618 (t=−1.80) | **+$4,372 (t=1.36)**, n=24 — sign flipped |
| `BUY_ANIMAL` cutoff day 10 | −$1,008 (t=−2.03) | absorbed into the noise band |
| `BUY_ANIMAL` defer 3d at day 0 | −$6,357 (t=−4.64) | **−$1,134 (t=−0.80)**, n=32 |

**The 12-cell margin panel is not deep enough for this measurement.** That panel works for its own job
because it is a *paired* comparison: two policies, same tape, same seed, differing by one mechanism, so most
of the game's variance cancels. Blocking or capping an investment class does not cancel — it changes the
trajectory wholesale. `BUY_ANIMAL` and `BUY_LAND` are also the lumpiest classes (2–3 orders/game at
$400–500/unit), so a single cell can swing thousands.

The rule: **lumpy capital classes need ≥24–32 cells before their sign is worth reading; flow classes
(labor, feed, seed — hundreds of orders/game) are stable at 12.** A wide CI here is the instrument telling
you the panel is too thin for that class, not that the class does not matter.

This is also why the tool reports `t`, a CI, *and* the fraction of cells positive. `BUY_PRODUCT` class-blocked
from day 18 has t=3.84 on only 62% of cells — a real effect carried by a minority of large wins, a different
object from `HIRE`'s 100%-of-cells result.

---

## 4. How ROI signals feed into decisions

**Observational only. Nothing here is wired to mutation weighting, and nothing should be.** The artifact is
written by hand and read by `report.py` for display. The search does not see it.

The reason is a limitation, not caution for its own sake: **this instrument can only measure the ROI of what
the policy does, never of what it does not do.** It removes or caps investments; it cannot add them. So it
can say the marginal tile at day 24 earns $216, but it cannot say whether a *second* extra tile would. A
zero crossing in an ROI curve is *not* an optimal threshold — downstream policy behaviour is held fixed.

What it is for is **ranking which thresholds are worth a forward experiment.** The ROI number is the
hypothesis; the paired panel margin is still the verdict, and the promotion gate does not move. This mirrors
how `evolve/deprioritized_params.yaml` already works: a human reads a report and edits a file with a
citation to the specific finding.

It deliberately does not mirror `param_exploration`, whose numbers carry a standing warning that they are
exploration weights and not causal importance. These numbers *are* causal, per cell. Their weakness is
dispersion across cells, handled by reporting n, t, CI and positive fraction rather than by a blanket caveat.

**The list, in priority order:**

1. **One forward candidate is justified: reduce hiring by roughly one unit per day.** −$1,178 at day 20
   (t=−10.36, 8% of cells positive), replicated on held-out seeds at 0% of cells positive, with a
   dose-response that locates the optimum near one unit rather than two. The natural knob is `hires_target`
   / `_hire_plan`. This needs a real candidate through the paired panel, not a threshold edit on the
   strength of this table.
2. **Late fertilizer stays deprioritized** (§3.3), now on a causal footing rather than a parity argument.
   The `evolve/deprioritized_params.yaml` citation can be strengthened with this measurement.
3. **Do not touch seed timing.** The marginal tile pays through day 24 and the class already stops at day 25.
4. **Do not touch feed.** Marginal feed is break-even; there is nothing there in either direction.
5. **`BUY_ANIMAL` and `BUY_LAND` remain unmeasured.** They want a ≥32-cell *marginal* sweep across days 4–12
   before anyone touches the hand-set herd or land thresholds. Cutoff on these classes is closer to marginal
   than it is for labor, but the dispersion (§3.5) is the binding problem, not the intervention shape.

---

## 5. Limitations

- **Removal and capping only.** Cannot price an investment the policy never makes, or a second added unit.
  The forward direction needs a candidate and the promotion gate.
- **Realized, not expected.** These are returns on four specific tapes at specific seeds. The O15/O16
  local-versus-ladder gap is a live reminder that a number true on this panel need not transfer.
- **`marginal` caps units, not decisions.** For a verb-only type (`BUY_SEED` with no item), the cap applies
  to total units across crops per day and the policy's own ordering decides which crop loses the unit. Use
  `VERB:ITEM` when that choice matters.
- **Offline only.** At ~0.5s/game, a 24-turn lookahead is ~17ms; a few per turn across 720 turns is 30–40s
  against a 60s overage budget. Counterfactual reasoning of this kind cannot run at decision time. It has to
  be compiled offline into cheap runtime features.
- **Sell timing is not covered here.** Production *timing* ROI is instrumented by the O12/O13/O15 line and
  the delay counterfactual; blocking `SELL` wholesale is not a meaningful counterfactual. What this tool adds
  on the production side is crop-cycle ROI via `BUY_SEED:<CROP>`.

## 6. Reproducing

```bash
# the marginal (threshold) question -- this is the one that answers "is one more worth it?"
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py candidates/O17_ORCH_CAPITAL.py \
    --tapes panel --seeds 1,2,3,4,5,6,7,8 --mode marginal --reduce 1 \
    --types HIRE --days 8,12,16,20,24 --json artifacts/horizon_roi/marginal.jsonl
# held-out replication and dose-response
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py candidates/O17_ORCH_CAPITAL.py \
    --tapes panel --seeds 9,10,11,12,13,14,15,16 --mode marginal --reduce 1 \
    --types HIRE --days 12,20 --json artifacts/horizon_roi/marginal_check.jsonl
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py candidates/O17_ORCH_CAPITAL.py \
    --tapes panel --seeds 1,2,3,4,5,6,7,8 --mode marginal --reduce 2 \
    --types HIRE --days 12,20 --json artifacts/horizon_roi/marginal_check.jsonl

# the class (subsystem) question, chunked one --types slice per call
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py candidates/O17_ORCH_CAPITAL.py \
    --tapes panel --seeds 1,2,3 --types HIRE,BUY_ANIMAL --days 2,6,10,14,18,22,26 \
    --json artifacts/horizon_roi/cutoff.jsonl --quiet

# pool everything and publish the artifact report.py renders
cat artifacts/horizon_roi/*.jsonl > artifacts/horizon_roi/all.jsonl
KAGG_FIXED_SHOPS=1 python3 tools/horizon_roi.py x --aggregate artifacts/horizon_roi/all.jsonl --emit

KAGG_FIXED_SHOPS=1 python3 tests/test_horizon_roi.py
```

Related: AGE-359 (`tools/delay_counterfactual.py`, marginal cost of a one-hour delay), AGE-361
(do/delay/abandon/switch — the purchase decision is the concrete instance of delay-vs-commit), AGE-362
(uncertainty and option value — `--mode defer` is the first instrument on that ticket's list, and §3.5 is
directly about how much evidence a direction needs before its sign is trustworthy).
