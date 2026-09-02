# Catch-rate A-v3 (Test B) — results: SPARRING catches the producer's own blind spots

**Date:** 2026-06-28 · **Pre-reg:** [`pre-registration.md`](./pre-registration.md) (LOCKED, tag `catchrate-v3-prereg-2026-06-28`). **Data:** [`problems.json`](./problems.json), [`recommendations.json`](./recommendations.json), [`reviews.json`](./reviews.json), [`audits.json`](./audits.json) → [`consensus-flaws.json`](./consensus-flaws.json) → [`results-aggregate.json`](./results-aggregate.json).

> **Headline (the result, stated honestly).** On 8 genuinely hard problems, a Generator produced a recommendation for each in normal produce-mode; an independent 3-auditor panel found **~4 material would-ship flaws per recommendation** (≥2-of-3 consensus — and the panel was free to find none, so this is an empirical fact, not a setup). Measured the right way:
>
> **A single-pass recommendation carries ~4 material flaws; the producer's own self-review still misses 16–32% of them, and a challenger — especially a *different* model — recovers most of the rest (78–94%).**
>
> This is a controlled, model-level analogue of the §6 mechanism audit, confirming the lived value the synthetic (Test-A) studies structurally could not.
>
> *Note on the baseline: "produce-and-ship catches 0%" is a **definitional anchor**, not a finding — the flaws the audit found in R are by construction still in R if nobody reviews it. The findings are the **self-review and challenger recovery rates**; the 0% only marks that, with no review step, all ~4 flaws/rec reach the decision.*

## Catch-rate on the 31 consensus would-ship flaws (blind-coded)

| Condition | Caught | Catch-rate |
|---|---|---|
| _Produce-and-ship — no review (**definitional anchor**: all flaws reach the decision)_ | 0/31 | _0% by construction_ |
| **NEUTRAL** — a fresh neutral review of R | 17/31 | 54.8% |
| **SELF** — the producer reviews its *own* R | 21/31 | 67.7% |
| **CHAL** — the SPARRING Challenger | 27/31 | **87.1%** |
| _Union (any of the three caught it)_ | 30/31 | 96.8% |

The empirical contest is among the **review** conditions (NEUTRAL / SELF / CHAL); the produce-and-ship row is the anchor, not a competitor.

## The hypotheses

- **The pearl, quantified.** A single-pass recommendation carries **~4 material flaws**. The producer's **own self-review recovers 68%** (so it leaves **~32% of its own material flaws unaddressed**); the **Challenger recovers 87%.** Even when the producer tries to critique its own work, nearly a third of its flaws survive — and a challenger recovers most of the rest. That is the everyday "it catches things a raw prompt wouldn't," measured against the honest comparator (self-review), not against the definitional zero.
- **H1 (CHAL > SELF) — confirmed, and it's the whole point.** The Challenger (87%) beats the producer's *own* self-review (68%). The directional split is decisive: **CHAL caught 8 flaws SELF missed; SELF caught only 2 CHAL missed** (19 both, 2 neither). A producer does **not** catch its own blind spots as well as a fresh adversarial agent does — the asymmetry SPARRING is built to exploit, demonstrated.
- **H2 (decomposition) — the adversarial stance is load-bearing.** CHAL (87%) ≫ NEUTRAL (55%): a 32-point gap over a plain fresh review, so the value is not merely "another set of eyes" — it's the *adversarial, different-angle* posture. (Note SELF 68% > NEUTRAL 55%: a producer critiquing its own reasoning actually beats a neutral outsider — it knows where it cut corners — but still loses to the Challenger.)

## Why this succeeded where Study A saturated

Same model, opposite outcome — because the **question** changed, which was the entire problem:
- **Study A (Test A):** "catch a flaw someone *else* planted." → 100% for everyone → no signal.
- **A-v3 (Test B):** "of the producer's *own* material flaws, how many does each review condition recover?" → a clear, ordered result among the review conditions (neutral 55% → self 68% → challenger 87%).

The producer's own work is exactly where the blind spot lives, and that is where the Challenger earns its keep.

## How the 8 problems were chosen — and what that does and doesn't let us claim

The 8 problems were **authored to fit a difficulty bar, not sampled from an external pool.** The plan we locked before running anything (the pre-registration, §3) set the bar — genuinely hard, open-ended, realistic decision problems with competing constraints, edge cases, and second-order effects — i.e. the conditions under which a strong producer naturally embeds flaws. The specific 8 were then written by the assistant to meet that bar, one per distinct domain (distributed systems / payments, ML / data engineering, databases / online migration, reliability, product growth, supply chain, SaaS pricing, finance / capital allocation). There was **no candidate pool to draw from, and no independent step that picked from it** — this is **a set written on purpose to be the kind of hard where flaws tend to show up** (a *purposive* sample, in survey terms), and the record states that bar but no selection *procedure* beyond author judgment.

Two consequences, kept separate:

- **What this rules out:** any claim about *how often* AI recommendations carry flaws in general. The set was chosen precisely because flaws were likely, so "every recommendation had flaws" is partly a property of the selection, not a base rate. Read every prevalence number as *"on these 8 purpose-built-hard problems,"* never *"AI usually."*
- **What this does NOT touch:** the load-bearing result — the self-review-vs-Challenger comparison. That contest runs *within each problem*, scored against the same flaw set, so however the problems were chosen, the selection bias falls equally on both conditions and cancels out of the comparison.

A stronger future design would pre-specify the selection protocol — draw problems from an independent published source (a decision-problem benchmark, a real RFC / design-doc corpus), or have a separate author generate a larger pool and an independent step sample from it blind — so the problem set demonstrably is not reverse-engineered to the result. Logged as future work alongside human-expert ground truth.

## Honest scope and caveats

- **Single-vendor:** Claude produced, self-reviewed, neutrally-reviewed, challenged, *and* audited. The within-model SELF-vs-CHAL contrast is the cleanest part; cross-vendor generation/audit is future work.
- **The problems were authored by the same vendor that then solved and audited them.** The single-vendor caveat above covers the *solving* loop; this names the *authoring* of the test itself. The test-writer (Claude) is the same model family as the test-taker and the grader, so the problem set may unconsciously favor the kinds of flaws this model produces and catches. Disclosed, not corrected here — the independent-source selection protocol above is the fix.
- **Ground truth is model-established** (3-agent audit, material flaws, ≥2/3 consensus) — not a human expert panel. It is the denominator both SELF and CHAL are scored against, so it does not bias the *comparison*, but the absolute rates depend on the audit's notion of "material flaw."
- **Consensus funnel (how 31 was reached):** the 3 auditors raised a deduped union of **44** distinct flaws; applying the pre-registered ≥2-of-3 bar keeps **31** (15 raised by all three, 16 by exactly two) and drops **13** single-auditor flaws. So the consensus bar did real filtering work — it discarded ~30% of raised concerns. (Caveat for the curious: the file `consensus-flaws.json` stores the full 44-record union with each flaw's auditor count, *not* the 31-record consensus subset — the 31 is the `auditors ≥ 2` slice of it.)
- **Produce-and-ship = 0% is a definitional anchor, not a finding.** The flaws the audit found in R are by construction still in R if nobody reviews it, so the 0% is arithmetic on the setup, not a measured result. Its only legitimate content is the *empirical* baseline fact it sits on — that produced output contains ~4 material flaws/rec (the audit could have returned none). All empirical signal is in the **review** conditions (SELF / NEUTRAL / CHAL), and the load-bearing comparator for the Challenger is **self-review**, not the zero.
- **Blind coding** de-identified the three reviews (A/B/C, shuffled per problem); first-person voice in SELF could partially leak condition — a future fully-blinded re-code is the check.
- n = 31 flaws across 8 problems; directional pilot, no inferential statistics.

## Cross-vendor confirmation (GPT-5.2 actors, Claude audit + coding)

To break the single-vendor caveat, the whole pipeline was re-run with **GPT-5.2** as producer / self-review / neutral / Challenger and **Claude** as the independent 3-agent audit panel and blind coder — so a *different vendor* establishes the ground truth and grades the catches. Same 8 problems; the Claude audit found **31 material would-ship flaws** in GPT-5.2's own recommendations (data: [`gpt-*.json`](./), [`results-aggregate-xvendor.json`](./results-aggregate-xvendor.json)).

| Condition | Claude-internal | Cross-vendor (GPT-5.2 / Claude) |
|---|---|---|
| _Produce-and-ship — no review (anchor)_ | _0%_ | _0%_ |
| Neutral review | 54.8% | 64.5% |
| Self-review | 67.7% | 74.2% |
| **SPARRING Challenger** | **87.1%** | **77.4%** |

> **Reconciliation note.** The cross-vendor column here is the *initial* GPT-gen / Claude-audit pass (`results-aggregate-xvendor.json`). The fuller 2×2×2 grid below later re-ran this cell's neutral and challenger on the **same 31-flaw denominator** (self-review is identical, 74.2%) and is **canonical** for the factorial comparison: it scores that cell's neutral **67.7%** and challenger **83.9%** (vs 64.5% / 77.4% here — a one-to-two-flaw run-to-run difference between two passes, not a contradiction). The qualitative finding — a challenge recovers the large majority of the producer's own flaws, vendor-robust — holds under either.

**What replicates — the practical value (robust).** Same empirical pattern in a second vendor: GPT-5.2 also produces ~4 material flaws/rec, its self-review leaves a chunk unaddressed, and a challenge recovers the large majority (**77% cross-vendor**) — the Challenger is the **top condition in both vendors**. The core lived-value claim — *a challenge recovers the producer's own material flaws that an unreviewed pass leaves in* — is **vendor-robust** (challenger recovery ~77–87%).

**What is vendor-dependent — stated honestly.** The *size* of the Challenger's edge over the producer's **own self-review** (H1) shrinks from **19 pts** (Claude 87 vs 68; CHAL-only 8 / SELF-only 2) to **~3 pts** (GPT-5.2 77 vs 74; CHAL-only 3 / SELF-only 2). **GPT-5.2 self-critiques nearly as well as it challenges**, so the "fresh adversarial agent beats self-review" asymmetry is strong for Claude but marginal for GPT-5.2.

**A confound that partly explains the shrink (don't hide it).** In the Claude-internal run the **Challenger and the audit were the same vendor**, which can inflate the Challenger's apparent catch-rate (challenger and ground-truth-definer agree on what counts as material). The cross-vendor run scores a *GPT* Challenger against a *Claude* audit — removing that alignment — and the Challenger's lead over self-review largely collapses. So part of the dramatic Claude-internal gap was **vendor-alignment, not pure blind-spot**. The honest core that survives both runs: **a challenge recovers most of the producer's ~4 material flaws/rec**; whether a *separate adversarial agent* meaningfully out-recovers the producer's own rigorous self-critique is **model-dependent** (and is settled by the full 2×2×2 below).

## Full 2×2×2 (Generator × Challenger × Audit) — disentangling blind-spot, diversity, and alignment

The whole grid was completed: 2 generators (Claude, GPT-5.2) × 4 review conditions (self, neutral, same-vendor challenger, **cross-vendor challenger**) × 2 audit vendors (Claude, GPT-5.2) establishing ground truth — so every challenger is scored by *both* vendors, and (for the first time) each model's work is challenged by the *other* model. Catch-rate (%) of the producer's own would-ship flaws (data: [`results-2x2-grid.json`](./results-2x2-grid.json)):

| Condition | Claude-gen / Claude-audit | Claude-gen / GPT-audit | GPT-gen / Claude-audit | GPT-gen / GPT-audit |
|---|---|---|---|---|
| _Produce-and-ship — no review (anchor)_ | _0_ | _0_ | _0_ | _0_ |
| Neutral review | 54.8 | 46.7 | 67.7 | 75.0 |
| Self-review | 67.7 | 73.3 | 74.2 | 84.4 |
| Same-vendor Challenger | 90.3 | 80.0 | 83.9 | 81.2 |
| **Cross-vendor Challenger** | **93.5** | **86.7** | 83.9 | 78.1 |

Three findings, separated:

1. **Catch value — robust in all 8 cells.** Of the ~4 material flaws per recommendation, a challenge recovers **78–94%** regardless of generator or auditor, and self-review leaves 16–32% unaddressed. The lived claim is vendor-robust and not in doubt. (The produce-and-ship 0% row is the definitional anchor, not a measured cell.)

2. **Blind-spot (challenge > self-review) is GENERATOR-dependent — and it is NOT mainly an alignment artifact.** Averaged over *both* audits: for **Claude-generated** work, challenge beats self-review by a wide margin (cross-vendor challenger **90.1** vs self **70.5**, +19.6), and crucially this **persists even under the cross-vendor GPT audit** (86.7 vs 73.3) — so it is a *real* Claude self-review blind spot, not Claude-audit favoring a Claude challenger. For **GPT-generated** work the gap nearly vanishes (challenger ~81 vs self ~79, +1.7): **GPT-5.2 catches its own blind spots on self-review almost as well as any challenger.** So *whether a separate challenger out-catches self-review is a property of the generator model* — large for Claude, small for GPT-5.2.

3. **Diversity / the Generator×Challenger combo — a cross-vendor challenger was best-or-tied in 3 of 4 cells, helping most where the generator is blindest.** Cross-vendor vs same-vendor challenger: Claude-gen **+3.2** (93.5 vs 90.3) and **+6.7** (86.7 vs 80.0); GPT-gen/Claude-audit **tied** (83.9 = 83.9); GPT-gen/GPT-audit **−3.1** (78.1 vs 81.2) — the one cell where the different model came in *below* the same-brand challenger, and where GPT's own **self-review (84.4) beat both challengers**. So pointing a *different* model at the work was usually as good or better — strongest exactly where self-review fails (Claude) — but it is **not** a universal win; in a pilot of 8 it was once slightly worse.

4. **Alignment confound — real but small (~2–5 pts), not the explanation.** Pooled, same-vendor reviewer↔auditor pairs score ~2–5 pts higher than cross-vendor pairs — a measurable but minor favoritism. It does **not** account for the blind-spot effect, which survives cross-vendor auditing. (This *revises* the earlier two-cell read: the Claude-vs-GPT difference in the self-vs-challenge gap is driven by the **generator's** self-blindness, not by audit alignment.)

## Verdict

Across the full factorial, the pearl holds: **a single-pass recommendation carries ~4 material flaws; the producer's own self-review still misses 16–32% of them, and a challenger — especially a different model — recovers most of the rest (78–94%, every cell).** That is the lived value, measured against the honest comparator (self-review), confirmed and vendor-robust. **The value of a *separate* challenger over the producer's own self-review is real but generator-dependent** (large for Claude, marginal for GPT-5.2), it **survives cross-vendor auditing** (so it is a genuine blind-spot, not alignment), and **a cross-vendor challenger was best-or-tied in 3 of 4 cells (slightly worse in 1)** — so "use a challenger, preferably a *different* model" is supported as a usually-as-good-or-better default, not a universal law, with the payoff scaling to how blind the generator is to its own work. This is one half of the cohesive story; the other is the **grounding/explainability** result (objections that are checkable and governable). Together: *rigor that is both real and accountable.* Remaining: human-expert ground truth, and the human-in-the-loop process study for the ecological claim.
