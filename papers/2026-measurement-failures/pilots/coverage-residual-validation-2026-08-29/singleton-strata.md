# Is run-to-run variance lost coverage, or churn?

**Status: exploratory. One fact pattern, one system. Answers the follow-up left open by
[`self-residual-floor.md`](./self-residual-floor.md).**
Raw: `runs/february-2018-family-law.g1.rALL.self-residual.strata.json`.

---

## The question

The floor measurement found that a fifth of the pooled issues appeared in **exactly one**
of five runs of the same system. Those singletons are either genuine rare insight or
sampling garbage, and the answer decides what the floor means.

## Method

The **stable core** — issues all five runs found — is scored alongside the singletons as a
reference. A singleton rate alone is uninterpretable: without a reference there is no way
to tell "55% is poor" from "55% is what this generator's audited output looks like."

Both strata went to the judge as **one shuffled list**. The judge never learned that strata
existed. Scoring them separately, or in order, would let it infer the hypothesis from the
batch shape.

Judge: `claude-opus-4-8`, cross-vendor from the `gpt-5.2` generator, k=3, blind to the
answer key. Judgments are `sound` / `raised` / `material`, per
[`scoring-design.md`](./scoring-design.md) §3.

## Result

```
stratum       n  signal   rate   unsound  unraised  immaterial
core         30      26   0.87         0         2           4
singleton    11       6   0.55         0         3           5

gap  +0.32          mean unanimity 0.99
```

**MIXED**, on the pre-committed bands (≤0.15 lost coverage, ≥0.35 churn). Near the churn
end, but not there.

Concretely: **6 of the 11 issues that only one run found were sound, raised, and material.**
A single run of this system missed six real, material issues that a rerun of the *same
model* caught.

## What it means for the floor

The floor is **part real coverage, part churn** — and it should be reported as both rates,
never as one corrected number.

- The variance is not noise. Rerunning the same model surfaces material issues, which makes
  a second run of the same system a genuine coverage intervention — possibly a cheaper one
  than reaching for a second vendor, though nothing here tests that comparison.
- The variance is not all coverage either. Singletons are meaningfully worse than the
  reliably-repeated output (0.55 against 0.87), so the raw single-run coverage figure
  overstates what a rerun buys.

Note what is *not* in the failure column: **zero unsound items in either stratum.** The
generator is not inventing law. Its fill is real doctrine that these particular facts do
not raise, or that cannot move the analysis — which is a very different failure from
hallucination, and a more tractable one.

## A control I mis-specified, corrected after seeing the number

The first reading gated on "core signal rate ≥ 0.90" and fired at 0.87 as CONTROL WEAK.
**That threshold was wrong, and it was wrong for a reason visible independently of the
result.**

The 0.90 floor was transplanted from the **key-based** control in
[`scoring-design.md`](./scoring-design.md) §5, where the items are known-material *by
construction* because NCBE's examiners assigned them percentage weights. The stable core
has no such guarantee: "all five runs said it" does not mean "it matters."

The four core items rated non-signal bear that out. None was unsound:

| item | verdict |
|---|---|
| Waiver of disclosure | sound, **not raised** — David *did* disclose |
| Commingling of inherited stocks | sound, **not raised** |
| Writing and signature | sound, raised, **not material** — nothing disputes it |
| Goodwill valuation | sound, raised, **not material** |

Those are correct judgments about an over-generating generator, not judge failures.

**The judge's actual validation already exists and passed.** The key-based control ran on
this same fact pattern with this same judge model and scored **1.00** — it recognised a
material item covering every one of the examiners' five weighted points. The core rate is a
*reference distribution*, not a gold standard, and that is how it is now used.

**The gap bands were not touched.** The ≤0.15 / ≥0.35 thresholds decide the actual question
and stay exactly where they were pre-committed; +0.32 reads MIXED under the original bands.
Correcting a mis-specified control after seeing a number is only legitimate because the
mis-specification stands on its own; moving the decision thresholds would not have been,
and was not done.

Recorded as deviation D8 (*the stable-core control borrowed a threshold that did not apply
to it*).

## What this cannot do

- **One fact pattern, one system, 11 singletons.** Eleven items cannot support a rate to
  two decimals. The finding is directional: singletons are worse than the core, and roughly
  half are real.
- **The strata are defined by the clusterer**, so both depend on the semantic-matching weak
  joint. A coarser clustering would produce fewer, larger clusters and fewer singletons.
- **No claim that a rerun is cheaper than a second vendor.** That comparison needs the
  cross-vendor rung, which has not run against this floor.
- k = 3, not the specified 5.
