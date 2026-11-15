# The generator-to-generator residual is not measurable with these tools

**Status: exploratory, and a NEGATIVE RESULT about the instrument rather than a measurement
made with it. Three mechanisms, three failures, three different directions.**
Supersedes the comparison-layer design in [`scoring-design.md`](./scoring-design.md).
Raw: `runs/residual-projected.json`, `runs/residual-structured-membership.json`,
`runs/cross-residual-structured.json`.

---

## 1. What was being attempted

`docs/research/verifiable-trust-rider-claims.md` §3 proposes measuring coverage by running
an independent generator and **counting what it surfaces that the first run missed**. Every
number in that proposal requires one operation: deciding whether something generator B
raised is *the same issue* as something generator A raised.

Three mechanisms were built for that operation. All three failed, and the pattern in the
failures is the finding.

## 2. The three attempts

### Attempt 1 — pooled clustering
Partition every item from every run into clusters; read run membership off the partition.

**Failed by under-merging.** It marked *"Premarital contracts"* and *"Division of
property"*, two items the examiners' answer key also covers (which points, and their weights, are withheld), as issues free generation never
found, when `gpt-5.2` had covered them with 45 distinct labels. Also produced the 27% floor
swing on granularity alone, intermittently unparseable replicates, and a single clustering
that reported itself as a consensus.

Clustering on label + rationale, to bridge vocabularies, moved novelty the **wrong way**
(+0.274 → +0.305): rationales made nearly every item unique, pooled distinct strings rose
281 → 377, and the clusterer got a harder task rather than a better-informed one.

### Attempt 2 — directed membership against each run's list
"Is candidate X present in this list?" — the shape that scores unanimity 1.00 when matching
against the answer key.

**Failed by over-merging, the exact mirror image.** A 10-item walk of broad taxonomy
headings was judged to cover **261 of 281** specific candidates. Tightening the prompt with
explicit anti-inflation instructions ("a broad heading does not make every question under it
present") moved it barely at all. A plausibility guard now flags any run covering >3x its
own item count.

### Attempt 3 — project both sides onto the taxonomy, then exact set arithmetic
Give both generators one externally-fixed coordinate system (350 NCBE nodes), so no
cross-vocabulary matching happens at comparison time.

**Produced plausible numbers and a wrong answer.** Node counts were sane (9–15 per run),
the floor landed at 0.128 in line with earlier estimates, and it reported **LIFT +0.207**
for the structured enumerator.

It is a **filing artifact**. The nine "B-only" nodes include *Contracts > Defenses > Duress
and undue influence*, *Fraud, misrepresentation, and nondisclosure*, and *Illegality,
unconscionability, and public policy* — while `gpt-5.2` explicitly produced *"Defenses:
duress/undue influence"*, *"Defenses: fraud/misrepresentation"*, and *"Unconscionability at
execution"*. Both sides raised the doctrine. The projection filed GPT's under *Family Law >
Premarital contracts* and the walk's under *Contracts > Defenses*, and set difference
reported a gap that does not exist.

**Cause: the taxonomy carries the same doctrine in more than one place.** The coordinate
system is not unique, so projection is not well-defined either.

## 3. The pattern, which is the actual finding

> **When two generators speak at different granularities, "did B raise something A didn't"
> has no determinate answer, and every mechanism that computes it is really reporting how
> it resolved that ambiguity.**

Clustering resolved toward **different** and inflated novelty. Membership resolved toward
**same** and erased it. Projection resolved toward **whichever node the filer chose** and
manufactured a gap from a bookkeeping difference. None of the three is a bug in the usual
sense — each is a defensible reading of an underdetermined question.

This is not "the measurement is noisy." It is **ill-posed**, and no amount of replication,
consensus, or prompt engineering fixes an ill-posed question. That is a stronger and more
useful result than any lift number this study could have produced.

## 4. What still works, and the way forward

**One comparison in this study has been reliable throughout: measurement against the
human-authored answer key.** The matching pass scores **unanimity 1.00** and its positive
control passes at 1.00. It is well-posed for a specific reason: the key is small, fixed,
externally authored, and each of its points is a *question* rather than a *label* — so
"does this list address this question?" has an answer.

So the recommendation is to **stop measuring generator-against-generator and measure every
generator against the key**:

- **Weighted recall against the examiners' points** — already built, already reliable.
- **Yield over what each generator emitted** — already built
  ([`scoring-design.md`](./scoring-design.md)), blinded, with a working positive control.
- A generator's contribution is then *its own* gold-relative score, and two generators are
  compared through their scores rather than through a direct residual between them.

**What is lost, and it is not small.** The gold-relative measure cannot see anything the
examiners did not grade — which is exactly the coverage question the whole line began with:
*what did everyone miss?* A key-relative instrument can measure **how much of a known answer
a generator finds**. It cannot measure **what nobody thought of.**

That may be the honest boundary of what is measurable here. Recording it as such is more
useful than a coverage number that turns out to be a filing convention.

## 5. What this does NOT overturn

- **The same-system floor** ([`self-residual-floor.md`](./self-residual-floor.md)) is
  affected in magnitude but not in kind. It compares runs of the *same* generator in the
  *same* vocabulary at the *same* granularity, so the ambiguity that breaks cross-generator
  comparison is far smaller. The reported spread (0.138–0.175 across clusterings) already
  carries the uncertainty.
- **The cross-vendor null** ([`cross-vendor-null.md`](./cross-vendor-null.md)) was measured
  at matched volume between two free generators using similar descriptive vocabularies —
  the least-exposed of the three comparisons. It should be re-derived gold-relatively before
  being relied on, but there is no specific reason to think it is wrong.
- **The generators themselves** all work as designed. Nothing here is a finding about them.

## 6. What this cannot do

- One fact pattern. The three failures are mechanism failures, demonstrated once each.
- It does not prove no mechanism exists — only that three reasonable ones failed in three
  directions, and that the reason they failed is structural rather than incidental.
- The gold-relative alternative has not yet been run across generators.
