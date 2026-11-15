# Coverage-instrument study — does the coverage residual find the things worth finding?

*(Exploratory design note. This study has no short code: "C1" already means the resolver
line's contested-item list C1-C12, and a colliding label is worse than none. The directory
name is the identifier.)*

**Status: EXPLORATORY. Not a pre-registration. Nothing here is locked, and nothing here needs to be.**
**Opens** the coverage line. First study on the Proposer/coverage subject; no parent study.
**Governance:** a Proposer-line study. Routes to the **Measurement paper** (Paper 2, renumbered 2026-08-30) and to the coverage instrument. **Not** errata for the published Resolver paper (`10.5281/zenodo.21210264`, locked). Origin: the 2026-08-28 register entry *"Improving the rider raises misplaced confidence when coverage is poor"* (`docs/research/paper-1-followups-register.md`) and `docs/research/verifiable-trust-rider-claims.md` §3.

---

## 0. Why this is exploratory, and why that is the correct status

Same reasoning R8 gives, applied one subject over: **this study's entire subject is whether an instrument works.** Pre-registering a measurement check applies the apparatus of confirmation to the step whose purpose is to find out whether confirmation is possible yet.

The specific risk it guards against here is worse than usual. `docs/research/verifiable-trust-rider-claims.md` §3 proposes the coverage residual as the analogue of the grounding verifier — *"coverage is verified by generating again somewhere the system does not control"* — and puts a residual count on the same footing as the grounding rate. **That framing is half wrong in a way that matters.** The *generation* is independent. The *measurement* is not: computing what run 2 raised that run 1 missed requires deciding whether two differently-worded considerations are the same consideration. That is an open-set semantic judgment of unmeasured reliability.

Which makes the residual, as currently specified, the analogue of **the rubric** — the thing R8 exists because nobody validated — not the analogue of the model-free existence check. Building and reporting it without validating it first would repeat this program's most expensive mistake one layer up: a confident number from a ruler of unknown resolution.

So: exploration, labelled as exploration. §9 states what would have to become true for this line to earn confirmatory status.

## 1. The question

The coverage residual exists to catch **the error of the third kind** — the well-made answer to the wrong problem, the decisive consideration nobody raised. Its structural weakness is that it is measured by generators which may share the blind spot being measured. Two vendors trained on overlapping corpora, both blind to the same thing, produce a residual of zero, and zero reads as *good coverage*.

That is a **false-clean**, and it is the same recursive failure the coverage idea was invented to catch, now sitting inside the instrument.

> **Q1 (primary).** Against a human-authored gold set, what is each generator's recall — **stratified by how obscure the gold item is**? Does recall hold on the rare items, or collapse there?
>
> **Q2 (only if Q1 leaves a workable signal).** Where the true total is known, does a multi-generator capture–recapture estimate predict the unseen count accurately, or is it biased — and in which direction?
>
> **Q3 (descriptive, runs alongside).** How much do the generators actually overlap? How many *independent* observers do four generators buy?

Q2 is the one that cannot be asked anywhere else. Capture–recapture's fatal assumption is independence of capture, and **in the field that assumption is uncheckable** — verifying it would require knowing what everyone missed, which is the quantity being estimated. On a known-answer corpus it is checkable. That is the whole reason this study exists.

## 2. Sample — a corpus with a frozen human answer key

**Law-school issue-spotter exams with published model answers.** Selected against four requirements, and this corpus is the only candidate that meets all four cheaply:

1. **An enumerated gold set.** The model answer lists the issues. Coverage becomes recall against a fixed list rather than an open-set matching judgment — the same reliability gain multiple-choice has over free response, and it is the single change that makes the measurement tractable.
2. **A built-in obscurity gradient.** Issue-spotters are *designed* with buried issues most candidates miss. The phenomenon under study is present by construction rather than by luck.
3. **A human-authored materiality weighting.** Grading rubrics assign points per issue. That is a frozen human judgment of which issues matter most — a partial gold standard for the flip test (`docs/research/verifiable-trust-rider-claims.md` §5), the one component otherwise unvalidatable without a live expert.
4. **Availability in volume, at no recruitment cost.** See §3.

**Target n ≈ 20–30 fact patterns**, with a floor of 15. The reasoning is descriptive adequacy, not power: a typical issue-spotter carries 8–15 gold issues, so 20 problems yields roughly 200–300 gold items, or 60–100 per obscurity band at three bands. That supports describing a recall curve. **It supports no inference test, and none is claimed.**

**Selection caveat carried forward, as in R8:** these are teaching instruments authored to a pedagogical bar, not sampled from any population of decisions. Nothing here supports a population claim.

## 3. The human-evaluation constraint, and how this design satisfies it without one

**SPARRING has no live human-evaluation capability.** Not deferred-for-budget — unavailable. It bit Paper 1, it is restated as standing in `pilots/resolver-dv-reliability-2026-08-28/design-note.md` §4 and §8, and Matthew Niedner MD, the one outside methods reader, has been unavailable since 2026-08-28. Any design that quietly assumes an expert has to be rebuilt after the fact.

This design needs an anchor outside the model ecosystem — otherwise "coverage" is defined circularly as *what models collectively mention*. It gets one **without a person in the loop**, by distinguishing two things that were being conflated:

| | Available? | What it is |
|---|---|---|
| **Live human evaluation** | **No.** Deferred and disclosed, as in Paper 1. | Recruit experts, have them rate *our* outputs, measure inter-rater agreement. |
| **Frozen human judgment** | **Yes, now.** | A gold set a human already authored and published, for their own reasons, before this system existed. |

Every corpus considered here is the second kind. Issue-spotter model answers are professor-authored; FMEA and HAZOP libraries are committee-enumerated; NTSB contributing-factor lists are investigator-enumerated. The epistemic function — an answer key not produced by the thing being tested — is identical. The cost, availability risk, and scheduling exposure are not.

**One genuine advantage over live evaluation, worth stating:** the answer key was written before this system existed and cannot have been influenced by it. Live raters looking at our outputs could be.

## 4. The generators — the independence ladder, minus the rung we do not have

A residual is only as meaningful as the independence of the second look. Four rungs, and what each one's independence actually rests on:

| | Generator | Independence rests on | Role here |
|---|---|---|---|
| **G1** | Same system, new seed | stochastic variation only | the **floor** — run-to-run wobble |
| **G3** | Different vendor, blind | training distribution — **partially**; shared-corpus blind spots survive | the conventional cross-vendor pass |
| **G4** | Structured non-model enumeration — a fixed doctrinal issue taxonomy walked against the fact pattern; HAZOP-style guide words | **procedural.** Not sampling from a distribution at all | breaks distributional correlation |
| **G5** | Grounded retrieval over a doctrine/case index | **evidential.** Retrieved from an index, not generated | breaks it differently |
| — | ~~Live domain expert~~ | — | **deferred and disclosed** (§3) |

**G4 and G5 are load-bearing, not garnish.** With no person available they are the only generators left whose failure modes are not drawn from the same well as G3's. They are also the two things this project already knows how to build: G4 is structured enumeration, which is SPARK's own machinery pointed at a fixed taxonomy instead of an open field; G5 is the citation verifier's retrieval pattern aimed at coverage instead of sources.

**G1 is reported, not subtracted.** R8 treats replicate variance as nuisance to remove. Here it is a finding in its own right: if a run misses what the *same system* finds on a rerun, that is a real coverage failure — milder than a systematic blind spot, but real, and it is the direct evidence on whether a single run can be trusted. The systematic component is isolated as the difference above G1, and **both numbers are reported.**

## 5. Measurement

Structure imported wholesale from `pilots/resolver-dv-reliability-2026-08-28/design-note.md` §3, which is itself Matthew Niedner's measurement critique of 2026-07-30. It survives his unavailability because it arrived in writing.

**No composite.** There is no single "coverage score." Each quantity is reported with its own reliability.

**Primary endpoint: recall against gold, stratified by obscurity band.** Not a raw residual count. A count without a denominator is uninterpretable across problems — missing 3 of 5 and missing 3 of 40 are different results — and the gold set is precisely what supplies the denominator.

**Operationalising obscurity, without circularity.** This is the subtle step and it has an available trap.

- **Primary axis — corpus frequency.** How often the doctrine/issue appears across the gold sets of the *other* fact patterns in the corpus. A doctrine appearing in 2 of 30 problems is rarer than one appearing in 26 of 30. Mechanical, computable, and **independent of anything any generator did.**
- **Rejected as a definition — cross-generator hit rate.** "An item few generators found is obscure" defines obscurity by the very quantity being measured, and would guarantee the finding. It is recorded and reported as a **result**, never used to build the bands.
- **Validity check where available** — model answers and rubrics that explicitly flag an issue as commonly missed. Used to check the corpus-frequency banding, not to replace it.

**The matching step gets its own reliability estimate.** Deciding whether a generator's output contains gold item K is the residual method's weak joint, so it is measured rather than assumed: **k = 5 replicate matching passes**, each blind to the others and to which generator produced the output, **cross-vendor adjudication on disagreement**, and a working floor of **ρ ≥ 0.70** to enter any aggregate. **Criteria falling below the floor are reported, not silently dropped.** Anchored scale points with worked examples, per R8 §3.4.

**Off-gold items are recorded and never scored.** A professor's answer key is exhaustive over what is *graded*, not over all sound observations. An item a generator raises that is not on the key may be genuine insight. It is counted and reported separately, scored neither right nor wrong — and the resulting bias direction is stated with every recall figure: **recall against a fixed key understates coverage whenever the system generates good off-list material.**

**Disagreement is a result, not dirt.** Where and how often the matching passes disagree gets reported. A band needing heavy adjudication is telling us something about the instrument.

**Secondary quantities.** Pairwise overlap matrix across G1/G3/G4/G5 (Q3); the capture–recapture estimate of the unseen, compared against the actual unseen (Q2).

## 6. Contamination — the largest threat to validity

Published model answers are likely in training data. A generator may **recall** a buried issue rather than **generate** it — and that inflates recall precisely on the obscure band, which is the band the whole study is about. Untreated, this study would report its best-looking result on its least trustworthy measurement.

Mitigations, applied in order of preference:

1. **Prefer sources unlikely to be indexed** — recent exam cycles, paywalled or institution-internal banks, materials published after the generators' training cutoffs where those are known.
2. **Perturb the fact patterns.** Change names, jurisdictions, dates, and incidental facts so that memorised retrieval of the published answer does not transfer while the doctrinal reasoning does. Perturbed and unperturbed versions of the same problem are run as a **paired contrast**; a large gap between them *is a contamination measurement*, not a nuisance.
3. **Report a contamination-risk tier per source** and break the headline recall figures out by tier. If recall is high only in the high-risk tier, the finding is about memorisation, not coverage, and gets reported that way.

**Contamination cannot be eliminated, only bounded and disclosed.** §8 carries it as a standing limit.

## 7. What we expect, stated in advance

Not hypotheses. Written down before data so it is visible whether the expectation moved to fit the result — the honesty function of pre-registration, kept, with the inferential function dropped because none is claimed.

- Recall is high on common issues and **materially lower** on rare ones.
- **G3 overlaps G1 heavily** — a different vendor buys much less independence than its label suggests. Four generators will not be four independent observers.
- **Capture–recapture underestimates** the unseen, from correlated capture and heterogeneous catchability. Direction stated in advance because both known biases point the same way — optimistic — which is the wrong direction for a safety measure.
- **G4 and G5 out-perform G3 on the obscure band specifically**, and roughly match or trail it elsewhere. This is the load-bearing expectation: if the non-model generators add nothing where it matters, the ladder collapses to the vendors and the false-clean problem has no remedy in this design.

## 8. Both outcomes, reported with equal prominence

Written now, because it will be tempting later to frame whichever result reads better.

- **If recall holds on the obscure band and the estimator tracks truth:** the coverage residual is usable in the field, with a stated correction factor and a measured discount on clean results. `docs/research/verifiable-trust-rider-claims.md` §3 stands, with §5's open questions answered.
- **If recall collapses on the obscure band, or the estimator is badly biased:** **the coverage residual as specified cannot do the job it was invented for.** Detecting the considerations that were easy to raise anyway is not the point. This would mean §3 needs rewriting, the "coverage as a fifth rider type" proposal is not yet buildable, and the honest interim position is that coverage is **named but unmeasured** — which is still better than the current position, where it is named and *assumed* measurable.

Both are worth knowing. Neither is a disappointment. The second is more valuable to know before building than after.

## 9. Stop rule

**Phase 1 (Q1) completes before Phase 2 (Q2) is designed in detail.**

If the model generators' **collective** recall on the most-obscure tercile is **below 50%**, Phase 2 does not run and this study reports Phase 1 alone. Estimating an unseen population from a sample that misses more than half of the stratum of interest produces a number with no defensible interpretation.

The threshold is written now precisely because it will be tempting to move it after seeing the number.

## 10. What this cannot do

- It **cannot** measure field coverage. A closed, known answer set is easier than an open problem, so recall here is an **upper bound** on field performance. The asymmetry is useful: an upper bound that is already bad is decisive; one that is good is only weakly reassuring.
- It **cannot** score good-but-off-gold generation (§5). Bias direction is stated: understates coverage.
- It **cannot** generalise beyond enumerable domains. Domains that keep published answer keys are the well-structured ones; the messy strategic decisions SPARRING targets are not like that. **This validates the ruler, not the field coverage of anything measured with it** — the same boundary R8 draws between *stable* and *right*.
- It **cannot** eliminate contamination, only bound and disclose it (§6).
- It **cannot** establish that a gold set is exhaustive over sound observations. It is exhaustive over what is graded.
- It **cannot** substitute for live expert evaluation, which stays deferred and disclosed (§3).

## 11. What would earn confirmatory status later

This line becomes a candidate for a genuine pre-registered study when **all three** hold — not before:

1. **The matching step clears the reliability floor** (ρ ≥ 0.70) on a named primary endpoint. That is this study's output, and without it nothing downstream has an error term.
2. **The obscurity banding is validated against something other than corpus frequency** — a second operationalisation that agrees.
3. **There is a claim worth defending publicly** — a coverage figure an outside reader would challenge, where being wrong in print would cost something.

Until then, exploration reported honestly is the more useful and more truthful output.

## 12. Outside review

Matthew Niedner MD's measurement critique of 2026-07-30 is **already incorporated** (§5) from his written review; it applies here as directly as it did to R8. He is **unavailable** as of 2026-08-28 and is not on this study's path.

More importantly, and unlike R8, this study does not merely *lack* outside human review — it is designed around the standing absence of human evaluation entirely (§3). That is a disclosed structural limit of the whole line, not a scheduling problem to be solved later. If this line reaches §11 and a real pre-registration is cut, an outside methods reader should see it then, when the review can still change something.

## 13. Deviations

Any departure from this note gets recorded in `deviations.md` with its date and reason. Cheap to keep, and the only thing that makes an exploratory result auditable after the fact.
