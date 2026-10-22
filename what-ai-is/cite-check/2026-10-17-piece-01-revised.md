# Cite-check: piece 01, it learns, after revision (2026-10-17)

_Run `piece01-2026-10-17b`, substrates Claude + GPT, on the revised
[positions/02-it-learns.md](../positions/02-it-learns.md) (opening rewritten around "function, not
form", probe 2c added, two new sources). The full tool report follows below. This header records
what was done about it._

## Coverage

25 citations (13 in the body, 12 in the source list). Existence independently confirmed for 19;
application grounded in retrieved text for 16, judged from model knowledge only for 3, not
checkable for 5 (three internal links, the podcast, one list entry).

## Resolutions applied to the piece

- **Samiei et al. 2026: overstatement corrected.** "Adults who explore for themselves largely
  overcome their own 'needs two' handicap" became "get much better at 'needs two', though it still
  takes them more tests"; "the same gap" became "a similar gap". The abstract says active
  exploration "substantially improves" conjunctive reasoning, "although conjunctive rules still
  require more tests", and that models show "similar" gaps. Flagged by GPT.
- **Header: "no new sources" was no longer true.** The piece now names the two sources added in
  revision and the follow-up pilot. Flagged by the extraction (c01).

## Split verdicts, resolved by hand

- **Shardlow & Przybyła 2024 (c06).** GPT marked application unchecked because the quote is not in
  the abstract. Both quoted phrases were checked against the published PLOS ONE full text on
  2026-10-17, under the subsection "Once trained, an LLM never learns or remembers." Verified.
- **Tolman 1948 (c04).** GPT marked application unchecked from the snippet. The full text at the
  linked URL describes the latent-learning experiments (Blodgett 1929, unrewarded rats running a
  maze) as the first of its five heads. Verified.

## Flagged, no change needed

- **Yiu, Kosoy & Gopnik (c07), Gjerde et al. (c10), Squire 2009 (c08):** the specific figures
  (85%/76%; 81.3%/88.2%; the mirror-star detail) are not in the abstracts. They were checked by
  hand against the full texts for the synthesis
  ([Does it learn?](../learning-and-gopnik.md), header note), and were unchanged in this revision.
- **Yiu, Kosoy & Gopnik year (c25):** published online 2023, issue dated 2024. The piece keeps
  2023, matching the synthesis.
- **Anderson 1982 (c09):** proceduralization, judged from model knowledge; the standard source.
- **Lucas et al. 2014 (c11), GX-Chen et al. 2025 (c12):** clean on both axes.
- **Not checkable:** the Hayes podcast (403, as the piece already says) and the internal links
  to the synthesis, the earlier report and the pilot result.

---

# cite-check report — piece01-2026-10-17b

**Source:** `positions/02-it-learns.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **25** citations checked
- existence independently confirmed: **19**
- application evidence-grounded: **16**
- application judged from model knowledge only: **3**
- not independently checkable: **5**
- buckets — clean **2** · problem **21** · disagree **2**

## ⛔ DISAGREE — escalate to human (2)
### c04 — exists ✅ · applied SPLIT  (line 35)
_([Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Tolman (1948) 'Cognitive Maps in Rats and Men' confirmed at the resolving URL; the paper's latent-learning findings support the claim that learning can sit quietly until needed.
- gpt: exists=verified applied=unchecked [evidence_text] — The URL resolves to Tolman's 1948 'Cognitive Maps in Rats and Men' and the snippet identifies its original Psychological Review publication. The retrieved snippet establishes that the article discusses rat maze experiments, but it does not include the specific no-reward/latent-learning result cited.

### c06 — exists ✅ · applied SPLIT  (line 61)
_Shardlow and Przybyła, arguing that a language model can't be conscious, put it plainly: once trained, "the weights no longer change," so models "have no capacity to learn beyond their initial training" ([Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Shardlow & Przybyła 2024 arguing a language model cannot be conscious, matching the cited framing; the specific quote about weights not changing is consistent with that argument though not in the abstract.
- gpt: exists=verified applied=unchecked [evidence_text] — The DOI resolves to Shardlow and Przybyła's 2024 PLOS ONE article 'Deanthropomorphising NLP: Can a language model be conscious?' The abstract supports that the paper argues against LLM consciousness, but it does not contain the specific quoted statement about weights no longer changing or no learning beyond initial training.

## ⚠️ AGREE-problem (21)
### c01 — exists ☐ · applied ☐  (line 4)
_Does it learn?](../learning-and-gopnik.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path synthesis document not fetchable; cannot verify existence or application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a relative internal path that could not be fetched, and existence_status is not-checkable. No source text was retrieved to assess whether it supports the claim about the piece being based only on a cite-checked synthesis.

### c02 — exists ☐ · applied ☐  (line 4)
_report](../cite-check/2026-10-17-position-pieces.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cite-check report path not resolvable; nothing to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited cite-check report is a relative internal path that could not be fetched, and existence_status is not-checkable. No evidence was retrieved to assess the claim that it was cite-checked on 2026-10-17 and not panel-reviewed.

### c03 — exists ☐ · applied ☐  · ⚑ degraded  (line 20)
_([Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Podcast URL returned HTTP 403 and author flags it as not machine-checkable; the quoted characterization is plausible but unverifiable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Pocket Casts URL returned HTTP 403 and existence_status is not-checkable. No transcript or metadata was retrieved to verify the May 2026 quoted claim.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 54)
_(Otto and his notebook; [Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Clark & Chalmers 1998 'The Extended Mind' confirmed via DOI; the Otto-and-notebook example is the paper's central thought experiment, consistent with the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Clark and Chalmers, 'The Extended Mind,' Analysis 58(1), 7-19, DOI 10.1093/analys/58.1.7. No source text was retrieved, but from general knowledge the Otto notebook example is central to the paper's extended-mind argument.

### c07 — exists ✅ · applied ⚠️  (line 71)
_Her published case is more careful than the two-year-old who outsmarts the best AI ([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/))_
- claude: exists=verified applied=verified [evidence_text] — Yiu, Kosoy & Gopnik 2023 confirmed at PMC; the cultural-technologies vs truth-seekers framing matches the paper, though the specific 85%/76% figures are not in the retrieved snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The PMC URL resolves to Yiu, Kosoy, and Gopnik's article 'Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet).' The retrieved text supports the broad topic, but it does not include the cited numerical results or detailed claims about specific model performance.

### c08 — exists ✅ · applied ⚠️  (line 106)
_Yet when Brenda Milner had him trace a star seen only in a mirror, he learned the skill and kept it across three days, with no memory of ever having practised ([Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023))_
- claude: exists=verified applied=nuance [evidence_text] — Squire 2009 'Legacy of Patient H.M.' confirmed; it establishes H.M.'s amnesia and memory principles, but the specific mirror-tracing-star detail is attributed to Milner and may be summarized rather than detailed in this short review.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and Europe PMC verify Squire's 2009 Neuron article 'The Legacy of Patient H.M. for Neuroscience.' The abstract supports H.M.'s severe memory impairment and importance for memory science, but it does not specifically mention Milner's mirror-star tracing result across three days.

### c09 — exists ✅ · applied ✅  · ⚑ degraded  (line 126)
_John Anderson's proceduralization; [Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Anderson 1982 'Acquisition of cognitive skill' confirmed via DOI; this is the canonical source for proceduralization/knowledge compilation, supporting the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Anderson's 1982 Psychological Review article 'Acquisition of cognitive skill.' No source text was retrieved, but from general knowledge Anderson's cognitive-skill theory includes proceduralization of knowledge into production-like skills.

### c10 — exists ✅ · applied ⚠️  (line 139)
_([Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606))_
- claude: exists=verified applied=nuance [evidence_text] — Gjerde, Cheung & Lagnado 2025 confirmed; abstract supports GPT-4o with chain-of-thought matching humans on tool-affordance tasks, but the specific 81.3%/88.2% figures are not in the abstract.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv verifies 'Reasoning about Affordances: Causal and Compositional Reasoning in LLMs' by Gjerde, Cheung, and Lagnado. The abstract supports that GPT-4o with chain-of-thought performed on par with humans on newly designed affordance tasks, but it does not provide the exact 20-item, 81.3%, or 88.2% figures.

### c13 — exists ✅ · applied ⚠️  (line 150)
_([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464))_
- claude: exists=verified applied=verified [evidence_text] — Samiei, Yiu, Gopnik et al. 2026 confirmed on arXiv; abstract supports that active exploration improves adults' conjunctive reasoning and that top models approach human accuracy but explore less efficiently with similar gaps.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv verifies 'Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?' by Samiei, Yiu, GX-Chen, Lin, Shen, Richards, Gopnik, and Precup. The abstract supports that state-of-the-art models approach human accuracy but explore less efficiently with similar conjunctive-disjunctive gaps, while adults improve substantially under active exploration; 'largely overcome' slightly overstates the remaining conjunctive difficulty.

### c14 — exists ☐ · applied ☐  (line 167)
_([The result](../../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md).)_
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own pilot result at a relative path not fetchable; cannot verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited pilot result is a relative internal path that could not be fetched, and existence_status is not-checkable. No evidence was retrieved to assess the reported preregistered study result.

### c15 — exists ✅ · applied ☐  (line 203)
_[Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)_
- claude: exists=verified applied=unchecked [no_basis] — Anderson 1982 confirmed via DOI; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies Anderson's 1982 Psychological Review article 'Acquisition of cognitive skill.' No claim is attached to this bibliography-style citation, so application cannot be assessed.

### c16 — exists ✅ · applied ☐  (line 204)
_[Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7)_
- claude: exists=verified applied=unchecked [no_basis] — Clark & Chalmers 1998 confirmed via DOI; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies Clark and Chalmers' 1998 Analysis article 'The Extended Mind.' No claim is attached to this bibliography-style citation, so application cannot be assessed.

### c17 — exists ✅ · applied ☐  (line 205)
_[Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606)_
- claude: exists=verified applied=unchecked [no_basis] — Gjerde et al. 2025 confirmed on arXiv; no specific claim attached to this reference-list instance.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv verifies Gjerde, Cheung, and Lagnado's 'Reasoning about Affordances: Causal and Compositional Reasoning in LLMs.' No claim is attached to this bibliography-style citation, so application cannot be assessed.

### c18 — exists ✅ · applied ☐  (line 206)
_[GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)_
- claude: exists=verified applied=unchecked [no_basis] — GX-Chen et al. 2025 confirmed on arXiv; no specific claim attached to this reference-list instance.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv verifies GX-Chen et al.'s 'Language Agents Mirror Human Causal Reasoning Biases. How Can We Help Them Think Like Scientists?' No claim is attached to this bibliography-style citation, so application cannot be assessed.

### c19 — exists ✅ · applied ☐  (line 207)
_[Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010) (Lucas, Bridgers, Griffiths & Gopnik, _Cognition_)_
- claude: exists=verified applied=unchecked [no_basis] — Lucas, Bridgers, Griffiths & Gopnik 2014 in Cognition confirmed via DOI; no specific claim attached to this reference-list instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC verify Lucas, Bridgers, Griffiths, and Gopnik's 2014 Cognition article. No claim is attached to this bibliography-style citation, so application cannot be assessed.

### c20 — exists ☐ · applied ☐  (line 209)
_[Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f) (the interview; not machine-checkable, and no claim here rests on it beyond the quoted line)_
- claude: exists=unchecked applied=unchecked [no_basis] — Podcast URL returned HTTP 403; author notes it is not machine-checkable and no claim is attached here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Pocket Casts URL returned HTTP 403 and existence_status is not-checkable. No claim is attached to this bibliography-style citation, so application cannot be assessed.

### c21 — exists ✅ · applied ☐  (line 211)
_[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2606.06464 resolves to a real paper with matching Samiei/Yiu/Gopnik authorship. No specific claim is listed to evaluate application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves and the retrieved metadata match the listed authors, year, and arXiv URL. No claims were provided for this citation, so application cannot be assessed.

### c22 — exists ✅ · applied ☐  (line 212)
_[Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521) (_PLOS ONE_; quotes checked against the published text 2026-10-17)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the Shardlow & Przybyła 2024 PLOS ONE article as described. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI resolves to a 2024 PLOS ONE article by Matthew Shardlow and Piotr Przybyła with matching metadata. No claims were provided for this citation, so application cannot be assessed.

### c23 — exists ✅ · applied ☐  (line 214)
_[Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Squire 2009 'The Legacy of Patient H.M. for Neuroscience' in Neuron as described. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI resolves to Larry R. Squire's 2009 Neuron article, 'The Legacy of Patient H.M. for Neuroscience,' with matching bibliographic metadata. No claims were provided for this citation, so application cannot be assessed.

### c24 — exists ✅ · applied ☐  (line 215)
_[Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm)_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to Tolman (1948) 'Cognitive Maps in Rats and Men' as cited. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to a York University Classics in the History of Psychology page for Edward C. Tolman's 1948 'Cognitive Maps in Rats and Men,' and the snippet identifies its original Psychological Review publication. No claims were provided for this citation, so application cannot be assessed.

### c25 — exists ⚠️ · applied ☐  (line 216)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)_
- claude: exists=verified applied=unchecked [no_basis] — PMC URL resolves to Yiu, Kosoy & Gopnik article; note the published issue date is 2024 though copyright 2023, a minor year nuance. No specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The PMC page resolves and the snippet identifies the article by Yiu, Kosoy, and Gopnik with online publication in 2023, though it also lists a 2024 issue date. No claims were provided for this citation, so application cannot be assessed.

## ✅ AGREE-clean (2)
### c11 — exists ✅ · applied ✅  (line 146)
_([Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010))_
- claude: exists=verified applied=verified [evidence_text] — Lucas et al. 2014 confirmed; abstract directly supports that children take up the unusual conjunctive ('needs two') rule more readily than adults.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC verify Lucas, Bridgers, Griffiths, and Gopnik's 2014 Cognition article. The abstract directly supports that children were more likely than adults to generalize the unusual conjunctive causal relationship, matching the claim about children learning the 'needs two' rule more readily.

### c12 — exists ✅ · applied ✅  (line 147)
_([GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614))_
- claude: exists=verified applied=verified [evidence_text] — GX-Chen et al. 2025 confirmed; abstract states LMs reliably infer disjunctive ('any one') but struggle with conjunctive ('needs two'), matching adult profiles, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv verifies 'Language Agents Mirror Human Causal Reasoning Biases. How Can We Help Them Think Like Scientists?' The abstract directly supports that LMs infer disjunctive relationships reliably, struggle with conjunctive ones, and exhibit adult-like rather than child-like inference profiles.
