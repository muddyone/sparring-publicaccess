# The structured non-model enumerator — built, run, and its comparison is not yet trustworthy

**Status: exploratory. The generator works and behaves as designed. The measurement
comparing it to free generation is CONFOUNDED and its headline number should not be
quoted. §4 says why and what to do instead.**
Rung G4 of the independence ladder ([`design-note.md`](./design-note.md) §4).
Raw: `runs/february-2018-family-law.g4.r*.json`, `runs/cross-residual-structured.json`.

---

## 1. Why this rung is load-bearing

With live human evaluation unavailable by standing constraint, and the cross-vendor pass
measured as worth no more than re-running the first model
([`cross-vendor-null.md`](./cross-vendor-null.md)), this is the **first generator in the
ladder whose failure mode is not drawn from the same distribution as the others.**

A free generator does two things at once: it *thinks of* candidate issues, and it *decides*
which apply. Both draw on the model's distribution, so two vendors can fail identically at
the first step and nothing downstream detects it.

This rung deletes the first step. The candidate set is the **NCBE MEE Subject Matter
Outline** — 350 nodes across all 14 subjects, written by examiners as an exhaustive
statement of the domain, years before this study existed. The model never invents a
candidate; it answers, per node, *do these facts raise this?*

**So it cannot fail by not thinking of something.** That is a structural difference, not a
prompt trick.

**And its limit, which travels with it:** recognition is still a model judgment. It can
fail to *see* that a node applies, and that failure could still be shared across vendors.
This removes one of two shared-failure channels, not both. It is also bounded by the
taxonomy — an issue outside the outline cannot surface.

## 2. Design choices

- **Same vendor as the baseline** (`gpt-5.2`), deliberately. Switching vendors here would
  make any lift unattributable between "structure helps" and "a different vendor helps" —
  and the cross-vendor rung already showed the latter is worth nothing. Holding the vendor
  fixed makes any effect attributable to **structure**.
- **All 14 subjects walked**, not just the question's own. Restricting would leak which
  subject matters — information no other generator was given — and would forfeit exactly
  the cross-subject issues this rung is best placed to find.
- **Blind to the answer key**, like every other rung.

## 3. What it did

```
r1  10/350 nodes raised    Family Law 7,  Contracts 2,  Real Property 1
r2  14/350                 Family Law 8,  Contracts 5,  Real Property 1
r3  15/350                 Family Law 8,  Contracts 5,  Real Property 2
r4  13/350                 Family Law 7,  Contracts 5,  Real Property 1
r5  12/350                 Family Law 8,  Contracts 3,  Real Property 1
```

It works, and it does reach across subjects — Contracts and Real Property nodes on a
Family Law question, consistently in all five runs.

It is also **small by construction**: 10–15 items against the free generators' 55–65. The
taxonomy holds 39 Family Law nodes in total, so it *cannot* produce 55 of them.
Volume-matching, the control that rescued the cross-vendor comparison, is **not available
here**.

That asymmetry forced a second metric. Fraction-of-union understates a small generator
because the union is dominated by the larger side, so **novelty rate** — *of what this
generator raises, what share did the other lack?* — is reported alongside it. Denominator
is the generator, not the union.

## 4. Why the comparison is not trustworthy yet

The run reports **novelty lift +0.305** (46% of what the walk raises is absent from a free
run, against 15% for a free run against another free run). **Do not quote that number.**

Inspection of what the walk supposedly found and free generation supposedly missed:

```
Premarital contracts          <- also on the examiners' answer key
Division of property          <- also on the examiners' answer key
Consideration (bargained-for exchange)
Mutual assent (offer and acceptance ...)
Discharge of the mortgage
Controversies arising in anticipation of marriage
```

The first two are **items the examiners' answer key also covers** (which points, and their weights, are withheld), and
`gpt-5.2` covered them with 45 distinct labels — *"Equitable distribution factors"*,
*"Classification: separate vs marital property"*, *"Division of closely held business"*.
They cannot be novel. The measurement is wrong, not the generator.

**Diagnosis: cross-vocabulary clustering.** The structured walk emits terse formal
doctrinal headings; free generators emit descriptive, fact-tied phrases. Clustering across
those two vocabularies **under-merges**, inflating apparent novelty.

**The attempted fix failed, and the failure is informative.** Clustering on label *plus*
its one-line rationale — to give the clusterer a factual bridge between vocabularies —
moved novelty lift the wrong way (+0.274 → +0.305). The reason is mechanical: rationales
made nearly every item unique, so pooled distinct strings rose from **281 short labels to
377 long ones**, the exact-duplicate saving disappeared, and the clusterer was handed a
*harder* task, not a better-informed one.

### What to do instead

**Stop clustering a large pool; use directed membership queries.** The most reliable
measurement in this study is the matching pass in
[`scoring-design.md`](./scoring-design.md) — *"does this candidate list contain key point
K?"* — which scored **unanimity 1.00** across replicates. Closed-set membership against a
fixed reference list works. Open clustering of a 300–400 item pool has been the source of
every instability recorded here: the 27% floor swing, the intermittent unparseable
replicates, and now this.

So the residual should be measured as: *for each item generator B raised, does generator
A's list contain it?* — one directed question per item, against a fixed list, instead of
one global partition of everything. That is a redesign of the comparison layer, not of the
generators, and every generator run already collected stays valid under it.

Recorded as deviation D10 (*pooled clustering under-merges across vocabularies*).

## 5. What stands

- The **generator is built, runs, and behaves as designed** — bounded by its taxonomy,
  reaching across subjects, never inventing a candidate.
- **`LIFT = -0.030`** on the fraction-of-union metric, which is *less* exposed to the
  under-merge problem than novelty rate (both sides share the same inflated pool). It is
  consistent with the structured walk adding no more than a rerun, but it is measured
  through the same broken clustering and is not independent evidence.
- **Nothing yet says whether structure buys coverage.** That is the question this rung
  exists to answer, and it is open pending the measurement fix.

## 6. What this cannot do

- One fact pattern, one subject, one taxonomy.
- The comparison layer is known-broken (§4); the generator is not.
- Whether the walk's items are *good* has not been scored — the blinded stratum scorer has
  not been run on them.
- Recognition failure remains a shared-vendor channel (§1).
