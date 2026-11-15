# A second vendor is worth about the same as running the first model again

**Status: exploratory. One fact pattern, two vendors, 5 runs each, run twice — once at
each vendor's default verbosity, once with output volume matched. The volume-matched
result is the one to quote (§4a); the default-verbosity result is confounded and is kept
for the contrast.**
Rung G3 of the independence ladder ([`design-note.md`](./design-note.md) §4), measured
against the G1 floor ([`self-residual-floor.md`](./self-residual-floor.md)).
Raw: `runs/cross-residual.json`.

---

## 1. Setup

Both vendors' runs are **pooled and clustered together, once**, and every quantity is read
off that single clustering. This is not a convenience: the floor swings 27% on clustering
granularity, so a cross-vendor residual computed under one clustering and compared against
a floor computed under another measures the clusterer, not the vendors.

| | |
|---|---|
| Fact pattern | February 2018 MEE, Family Law |
| Vendor A | `gpt-5.2`, 5 runs — 55, 55, 60, 60, 50 items |
| Vendor B | `claude-opus-4-8`, 5 runs — 22, 21, 24, 24, 20 items |
| Clusterer | `claude-opus-4-8`, k=3 consensus, both vendors together |

## 2. Result

```
joint pool 69      shared 27      A-only 37      B-only 5

one run vs one run, inside this single clustering
  within-A  (the floor)         0.151   [0.100-0.189]
  within-B                      0.160   [0.042-0.240]
  an A run misses, vs a B run   0.038   <- what B ADDS   (the question)
  a B run misses, vs an A run   0.553   <- what B LACKS  (verbosity)

LIFT = 0.038 - 0.151 = -0.114        NO CROSS-VENDOR EFFECT
```

**At each vendor's default verbosity**, a second vendor surfaced less than a rerun of the
first: rerunning `gpt-5.2` surfaced 15% the previous run had missed, while swapping to
`claude-opus-4-8` surfaced 3.8%.

**This number is confounded and is not the study's answer.** `gpt-5.2` emitted 2.5x more
items per run, and a model that says less cannot add much whatever it can see. §4a repeats
the measurement with output volume matched; the corrected lift is **+0.008** — a clean
null rather than a negative. Read §4a.

Note also **within-B ≈ within-A** (0.160 vs 0.151). The run-to-run floor is not a quirk of
one vendor; both are about equally unstable against themselves.

## 3. This is the false-clean, arriving as a result

*(The claim in this section is the one that survives the volume control in §4a — the
controlled lift of +0.008 is still a null. Only the sign and the size changed.)*

The design predicted this failure as a *caveat*:

> A cross-vendor residual structurally cannot detect a blind spot both vendors share.
> Shared pretraining corpora, shared RLHF conventions, shared internet. When that happens
> you get a residual near zero and read it as good coverage.

On this problem it arrived as a *measurement*. The cross-vendor pass — the sharpest form of
independence the design had short of a human, and the rung most practitioners would reach
for first — bought no more coverage than re-rolling the dice on the first model. Note the
controlled version is the *stronger* form of this claim, not the weaker one: the two
vendors demonstrably reach different ground (48 shared clusters against 33 gpt-only and 20
claude-only), and it still makes no difference to how much new any one pass adds.

That is the strongest available argument for the two rungs not yet built: the structured
non-model enumerator and grounded retrieval. With live human evaluation unavailable by
standing constraint, they are the only remaining generators whose failure modes are not
drawn from the same distribution. This result moves them from "nice to have" to the only
thing left.

**It does not license the reverse claim.** Nothing here says vendors share a blind spot.
See §4 — the design cannot yet separate that from a verbosity difference.

## 4. The confound — found, controlled, and the null survived

`gpt-5.2` emitted **2.5x more items per run** than `claude-opus-4-8` on identical prompts
(56 vs 22). A model that says less cannot add much, whatever it can see, so the §2 result
could not distinguish:

> **"Claude added little" (a blind-spot claim) from "Claude said less" (a prompt artifact).**

### 4a. The control, and the corrected result

Both vendors were re-run with the same prompt **and the same explicit item budget** (~55,
gpt-5.2's natural level). The budget went to both sides, not just the quieter model —
stretching one while leaving the other natural would trade one asymmetry for another.

**Claude reached 55-57 items, with a *tighter* run-to-run spread (2) than at its natural
20-24 (spread 4).** It was not straining against a ceiling. The verbosity gap is a
**stylistic default, not a resolution limit** — both models can work this problem at the
same grain when asked, and an identical "be exhaustive" instruction simply does not produce
comparable volume across vendors.

| | default verbosity | volume-matched |
|---|---|---|
| items/run — gpt-5.2 | 56 | 63 |
| items/run — claude-opus-4-8 | 22 | 56 |
| verbosity ratio | 2.5x | **1.1x** |
| joint pool | 69 | 101 |
| shared | 27 | 48 |
| gpt-only | 37 | 33 |
| claude-only | **5** | **20** |
| within-gpt (the floor) | 0.151 | 0.195 |
| within-claude | 0.160 | 0.168 |
| what Claude ADDS | 0.038 | 0.203 |
| **LIFT** | **-0.114** | **+0.008** |

**The null survives, and gets cleaner.** At matched volume a second vendor adds **0.203**
where a rerun of the first adds **0.195** — a lift of **+0.008**, indistinguishable from
zero and far inside the floor's own clustering sensitivity.

Three things this changes:

1. **The -0.114 was partly a volume artifact**, exactly as §4 feared. The honest
   uncontrolled statement was never "a second vendor sees less"; it was "a second vendor
   *said* less." The controlled answer is a clean null, not a negative.
2. **Claude does reach new territory when given the budget** — claude-only clusters rose
   from 5 to 20. The additions are genuine new ground, not just finer slicing of what it
   already had. So the vendors are *not* redundant in what they can reach.
3. **And it does not matter.** gpt-5.2's own rerun opens comparably much new ground. The
   vendors differ in *what* they surface and are equivalent in *how much new* any one pass
   contributes.

**That is the finding, in one line: a second vendor is worth about the same as running the
first model again.** Not less — that was the artifact. Not more. The same.

### 4b. A second-order observation

**within-gpt rose from 0.151 to 0.195 under the larger budget.** Pushed to produce more, the
model became *less* stable against itself. Whatever the extra items are, they are not drawn
from a reliably-reachable reserve — which is consistent with the same-system finding that
roughly half of run-specific issues are churn
([`singleton-strata.md`](./singleton-strata.md)).

## 5. A metric error this run produced, and how it was caught

The first version reported **"lift +0.130, SUBSTANTIAL"** — the opposite verdict, on the
same data.

`mean_pairwise` averaged both directions of the residual. With unequal verbosity, that
fuses two unrelated quantities and reports their mean as a blind-spot effect:

| direction | what it is | value |
|---|---|---|
| what B adds over A | the cross-vendor question | 0.038 |
| what B lacks from A | a granularity difference | 0.553 |

The average, 0.304, cleared the 0.151 floor and printed SUBSTANTIAL. **The number was real;
the label on it was not.**

It was caught by the pool shape, not by the number looking wrong: B-only = 4 clusters
against A-only = 40 is not what a genuine cross-vendor gain looks like. The residual is now
directional, and a verbosity-asymmetry warning fires at >=1.5x saying outright that the two
directions are not interchangeable.

> *Annotation, 2026-09-16.* The figures above are the pool shape recorded for the **first**
> run. The only saved clustering, `runs/cross-residual.json` (one committed version, `689332a7`),
> is from the corrected run and reads **A-only 37, B-only 5** against a joint pool of 69. Cluster
> sets were persisted only after this fix, so the first run's shape cannot be checked against data.
> The catching signal is the same under either figure. Kept as recorded; not rewritten.

Recorded as deviation D9 (*the cross-vendor residual averaged two directions that mean
different things*).

**Third time this session.** `weighted recall 0.00` from a key-id mismatch; a single
clustering labelled a consensus; now a granularity gap labelled a blind spot. Each was a
confident number that meant something other than its name, and each was caught by an
internal check rather than by looking implausible. That is the failure class this study exists to
study, and its own instrument has now produced three instances of it — which is either
reassuring about the checks or alarming about the method, and is worth saying rather than
tidying away.

## 6. What this cannot do

- **One fact pattern.** Nothing generalises.
- **The volume-matched result (§4a) is the one that counts.** The default-verbosity
  numbers in §2 are confounded and are retained only for the contrast.
- **No claim the extra issues are good.** Neither the 20 claude-only clusters nor
  gpt-5.2's rerun additions have been through the blinded stratum scorer. On the
  same-system data roughly half of comparable "extra" items were churn, so a lift of
  0.203 is an upper bound on *useful* additions in both directions.
- **Two vendors, one prompt, one subject, one budget.** ~55 items was chosen as gpt-5.2's
  natural level; a different budget could change the picture, and nothing here says 55 is
  the right grain for this problem.
- **Volume is now a required control for any cross-generator residual.** Nothing in the
  original design said to pin it, and without pinning it the measurement is substantially
  about prompt-response conventions. That generalises beyond this run.
- k = 3 clusterings, not the specified 5.
