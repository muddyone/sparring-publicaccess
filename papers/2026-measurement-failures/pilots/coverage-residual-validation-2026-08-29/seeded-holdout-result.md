# Hold-out validation of the off-key measure: partly informative, and weaker than designed

**Status: exploratory. The experiment ran, produced a clean-looking number, and on
inspection establishes considerably less than it was built to establish. Both the
mechanism artifact and the design flaw are recorded below.**
Tests the gap named in [`implications-for-the-proposer-paper.md`](./implications-for-the-proposer-paper.md) §3.
Raw: `runs/july-2020-secured-transactions.seeded-holdout.json`.

---

## The gap this was built to close

Off-key discovery — items a blind judge rates sound, raised and material that match no key
point — is the only measure here that looks at ungraded material. It is also the one number
nothing checks: the positive control validates the judge against a human answer, and
off-key is *by definition* outside the region where that answer exists.

**Design:** seeds cannot be authored (model-written seeds are circular; no expert is
available by standing constraint), so the seeds are the examiners' own key points, held out
of the scoring key one at a time. Leave-one-out over every point, nothing cherry-picked.

## Result as printed

```
rung   cases   recovery
g1        30       1.00
g3        30       1.00
g4        30       0.00
OVERALL 90        0.67
```

Recovery was identical (0.67) in every weight band — 10%, 15%, 20%, 25% — which is the
first sign the number is structural rather than substantive.

## 1. The structured walk's 0.00 is undefined, not a failure

```
rung   items   mean key points cited per item   items citing >1 point
g1        33                            1.10                    2/21
g3        20                            1.00                    0/16
g4        11                            2.50                     4/4
```

**Every cited item in the structured walk covers more than one key point.** Hiding one
point therefore leaves the item still matched to the others, so it is removed from the
off-key set and cannot possibly recover the hidden point.

Recovery is **undefined for coarse generators**, and reporting 0.00 for them is wrong. This
is the same granularity disease that broke three comparison mechanisms
([`comparison-layer-negative.md`](./comparison-layer-negative.md)), now inside a validation
rather than a measurement.

The overall 0.67 is therefore meaningless: it is two rungs at 1.00 and one rung that the
metric cannot score, averaged together.

## 2. The 1.00 is weaker than it looks, and this is the design flaw

Recovery decomposes into two conditions:

1. the item matches **only** the held-out point, so hiding that point strands it in off-key;
2. the blind judge rates it **sound + raised + material**.

For a fine-grained generator condition (1) is near-automatic — 1.00 and 1.10 points cited
per item means items map essentially one-to-one onto key points. So the measurement reduces
to condition (2).

**And condition (2) is what the positive control already tested.** The judge never saw the
key in either case; hiding a point from the *scoring* key does not change what the judge was
asked or what it saw. The hold-out changes only the bookkeeping — which bucket the item
lands in — not the judgment being validated.

So the honest statement is:

> **The hold-out confirms that the off-key bookkeeping is sound for fine-grained
> generators: known-material content does not vanish when it is absent from the scoring
> key. It does not independently validate the judge on ungraded material, because every
> seed was an examiner-graded item wearing a disguise.**

The objection it set out to answer — *the control cannot reach the off-key region* — is
only **partly** addressed. The control now reaches items that *could have been* on the key.
It still cannot reach items that never would be, and those are the coverage question.

## 3. What is nonetheless established

- **Off-key does not leak.** For fine-grained generators, 60 of 60 held-out material points
  surfaced as off-key rather than disappearing. A measure that dropped known-material
  content would have shown it here, and it did not.
- **The metric is granularity-bounded**, and now visibly so. Any future use must either
  restrict to generators whose items map near one-to-one onto key points, or replace the
  exclusive-match rule with partial credit.
- **The 0.49 off-key rate reported for the structured walk is not readable** as coverage:
  its items are multi-point by construction, which is exactly the property that makes both
  its off-key rate and its recovery uninterpretable.

## 4. What the real experiment requires

Seeds must satisfy three conditions this design met only two of:

| | held-out key points | what is actually needed |
|---|---|---|
| known-material | **yes** — examiner-weighted | yes |
| outside the scoring key | **yes** — by construction | yes |
| outside the key *entirely*, and outside the model ecosystem | **no** | **yes** |

The third is the one that matters and the one no available source supplies without either
authoring (circular) or an expert (unavailable). Candidate sources that are neither:
contributing-factor lists from accident investigations, documented post-mortems, appellate
opinions reversing on a ground the trial court missed — cases where **the decisive
consideration is on record precisely because someone failed to raise it.**

That is the experiment. It is not blocked by tooling; it is blocked by sourcing, and the
sourcing problem is the same one the corpus recon solved for answer keys
([`corpus-recon.md`](./corpus-recon.md)) — find a domain where somebody already wrote the
answer down for their own reasons.

## 5. What this cannot do

- One fact pattern, three rungs.
- The 1.00 rests on near-1:1 item-to-point matching, which is a property of these
  generators on this key, not a general one.
- Nothing here speaks to obscure content; every seed was mainstream by construction.
