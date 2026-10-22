# cite-check report — p01-rev2

**Source:** `positions/02-it-learns.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **34** citations checked
- existence independently confirmed: **23**
- application evidence-grounded: **20**
- application judged from model knowledge only: **3**
- not independently checkable: **6**
- buckets — clean **5** · problem **31** · disagree **1**

## ⛔ DISAGREE — escalate to human (1)
### c21 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 285)
_Gopnik is right that the hard test is discovery._
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No bibliographic details or matched evidence to verify a specific Gopnik work; the general attribution that discovery/innovation is the hard test aligns with Gopnik's well-known arguments, assessed from knowledge only.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference gives only an author name and no identifiable work; the retrieved Crossref lookup found no match, but that is not decisive for nonexistence. No source text or identifiable work was available to assess the claim about discovery.

## ⚠️ AGREE-problem (31)
### c01 — exists ☐ · applied ☐  (line 16)
_([Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f))_
- claude: exists=unchecked applied=unchecked [no_basis] — URL returned HTTP 403, so the podcast episode and the specific quote cannot be verified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned HTTP 403 and the record is marked not-checkable, so existence cannot be confirmed from the evidence. No source text was retrieved to assess the podcast claim.

### c03 — exists ☐ · applied ☐  (line 43)
_(sources in [the brief](../briefs/2026-10-18-10-when-assistants-began-to-remember.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path brief could not be fetched, so neither existence nor application can be judged from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a relative local path that could not be fetched or indexed. No text was retrieved to evaluate whether it supports the claim about AI memory in 2024–2025 tools.

### c04 — exists ✅ · applied ⚠️  (line 55)
_([Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm))_
- claude: exists=verified applied=nuance [evidence_text] — The 1948 Tolman paper exists and the URL resolves; the retrieved snippet confirms the maze experiments but does not quote the specific latent-learning (no-reward exploration) result, which is a well-known finding from that paper.
- gpt: exists=verified applied=nuance [evidence_text] — The fetched York page identifies Tolman's 1948 'Cognitive Maps in Rats and Men' and states it was first published in Psychological Review. The supplied snippet confirms rat-maze experiments generally, but it does not include the specific no-reward/food-appears latent-learning passage.

### c05 — exists ✅ · applied ✅  · ⚑ degraded  (line 74)
_([Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — The Extended Mind (Clark & Chalmers 1998) is confirmed by Crossref; the Otto-and-notebook thought experiment is the paper's central example, though no abstract text was retrieved.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Clark and Chalmers' 1998 article 'The Extended Mind' in Analysis. The Otto notebook example is a well-known central example from that paper, but no retrieved source text was available, so application is judged from model knowledge only.

### c06 — exists ✅ · applied ⚠️  (line 86)
_([Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521))_
- claude: exists=verified applied=verified [evidence_text] — The paper exists and argues an LLM cannot be conscious; the abstract confirms its thesis, and the weights-no-longer-change quotation is consistent with the paper's argument though not verbatim in the abstract.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI resolves to Shardlow and Przybyła's PLOS ONE article on whether language models can be conscious. The abstract supports the broad claim that they argue pretrained LLMs cannot be conscious, but the retrieved text does not verify the quoted wording about weights no longer changing or no capacity to learn.

### c07 — exists ☐ · applied ☐  (line 96)
_([brief](../briefs/2026-10-17-9-how-models-change.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path brief could not be fetched; cannot judge either axis from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited brief is a relative local path that could not be fetched. No source text was retrieved to assess the claim about how model versions are shaped.

### c09 — exists ✅ · applied ⚠️  (line 106)
_([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/))_
- claude: exists=verified applied=nuance [evidence_text] — The Yiu/Kosoy/Gopnik paper exists and its title matches the cultural-technology/truth-seeker framing; the retrieved snippet confirms the thesis but does not show the specific 85%/76% figures, which cannot be verified from the available text.
- gpt: exists=verified applied=nuance [evidence_text] — The PMC page resolves to Yiu, Kosoy, and Gopnik's article with the stated title and bibliographic information. The retrieved snippet supports the broad topic but does not include the detailed numerical results or all substantive claims, so support is only partial from the supplied evidence.

### c10 — exists ✅ · applied ⚠️  (line 144)
_([Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023))_
- claude: exists=verified applied=nuance [evidence_text] — Squire 2009 on patient H.M. exists; the abstract confirms H.M.'s memory impairment but does not detail the specific mirror-tracing/star experiment, which is a well-documented Milner finding typically attributed to earlier sources.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI is verified as Squire's 2009 Neuron article on patient H.M. The abstract supports H.M.'s severe memory impairment and importance to memory research, but it does not include the specific mirror-star learning details across three days.

### c11 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 165)
_the psychologist John Anderson described ([Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369))_
- claude: exists=verified applied=verified [model_knowledge_only] — Anderson 1982 'Acquisition of cognitive skill' is confirmed; its ACT theory of procedural knowledge (turning declarative rules into automatic skills) supports the claim that people turn rules into reflexes.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref verifies Anderson's 1982 Psychological Review article 'Acquisition of cognitive skill.' The claim paraphrases Anderson's proceduralization/skill-acquisition account, but no retrieved abstract or text was available, and 'rules into reflexes' is an imprecise popularization.

### c12 — exists ✅ · applied ⚠️  (line 183)
_([Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606))_
- claude: exists=verified applied=nuance [evidence_text] — The affordance-reasoning paper exists and describes GPT-4o with chain-of-thought performing on par with humans, but the precise figures (81.3% vs 88.2%, 86.0%) are not stated in the abstract and cannot be fully verified.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv verifies Gjerde, Cheung, and Lagnado's 2025 paper on affordance reasoning. The abstract supports the qualitative claim that GPT-4o with chain-of-thought performed on par with humans on novel tool/affordance tasks, but it does not verify the exact 20-item setup or the cited percentages.

### c16 — exists ☐ · applied ☐  (line 215)
_([the result](../../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal pilot result file could not be fetched; neither axis can be judged from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited result is a relative local path that could not be fetched. No source text was retrieved to assess the claim about model performance on 240 machines.

### c17 — exists ☐ · applied ☐  (line 222)
_([details](../../pilots/gopnik-followup-2026-10-17/README.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal pilot README could not be fetched; neither axis can be judged from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited details file is a relative local path that could not be fetched. No source text was retrieved to assess the claims about the harder task or notes-versus-no-notes results.

### c18 — exists ☐ · applied ☐  (line 242)
_What they changed is closer to Gopnik's point: Claude spent its few tests the way a learner who knows the rule would. That is the efficiency gap her group found_
- claude: exists=unchecked applied=unchecked [no_basis] — This is an informal in-text allusion to Gopnik's efficiency-gap point with no formal reference or retrievable evidence; the underlying finding is covered by c15.
- gpt: exists=unchecked applied=unchecked [no_basis] — The record gives no identifiable title, year, DOI, URL, or specific work, and the lookup found no match. No evidence was retrieved to assess the claim about Gopnik's group's efficiency gap.

### c19 — exists ☐ · applied ☐  (line 245)
_Its notes held the rule, like the rats' map, until the next machine called for it._
- claude: exists=unchecked applied=unchecked [no_basis] — As the author note states, this is an analogy/allusion to the rats' map rather than a formal citation, and no evidence is retrievable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The author note indicates this is an allusion or analogy rather than a formal citation, and no bibliographic work was matched. No retrieved evidence supports the claim about the notes holding the rule.

### c20 — exists ☐ · applied ☐  (line 271)
_If choosing one's own experiments turns out to be what matters most, and models keep falling short of it, Gopnik's claim is the deeper point_
- claude: exists=unchecked applied=unchecked [no_basis] — An informal reference to Gopnik's broader claim with no formal work cited and no retrievable evidence to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The record gives no identifiable cited work beyond a vague reference to Gopnik, and the lookup found no match. No evidence was retrieved to assess the hypothetical claim about choosing one's own experiments.

### c22 — exists ☐ · applied ☐  (line 300)
_[Does it learn?](../learning-and-gopnik.md), a summary of the research with its sources_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an internal companion link, not a verifiable external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so it is treated as intentionally uncited/internal context rather than a citation to verify. No application claim is supplied.

### c23 — exists ☐ · applied ☐  (line 302)
_[How a model moves from version to version](../briefs/2026-10-17-9-how-models-change.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an internal companion link, not a verifiable external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so it is treated as intentionally uncited/internal context rather than a citation to verify. No application claim is supplied.

### c24 — exists ☐ · applied ☐  (line 303)
_[When AI assistants began to remember](../briefs/2026-10-18-10-when-assistants-began-to-remember.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an internal companion link, not a verifiable external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so it is treated as intentionally uncited/internal context rather than a citation to verify. No application claim is supplied.

### c25 — exists ✅ · applied ☐  (line 318)
_[Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI match confirms Anderson 1982 'Acquisition of cognitive skill,' Psychological Review; no specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1037/0033-295X.89.4.369 as John R. Anderson’s 1982 Psychological Review article “Acquisition of cognitive skill.” No specific claim is provided for application assessment.

### c26 — exists ✅ · applied ☐  (line 319)
_[Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms) (consumer terms, 2025-08-28)_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to Anthropic's Aug 28, 2025 consumer terms update page as described; no specific claim to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to Anthropic’s “Updates to Consumer Terms and Privacy Policy” page dated Aug. 28, 2025, matching the reference. No specific claim is provided for application assessment.

### c27 — exists ✅ · applied ☐  (line 321)
_[Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI confirms Clark & Chalmers 1998 'The Extended Mind,' Analysis; no specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1093/analys/58.1.7 as Clark and Chalmers’ 1998 Analysis article “The Extended Mind.” No specific claim is provided for application assessment.

### c28 — exists ✅ · applied ☐  (line 322)
_[Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2502.16606 confirmed as Gjerde, Cheung & Lagnado 2025 on affordance reasoning; no specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms 2502.16606 as “Reasoning about Affordances: Causal and Compositional Reasoning in LLMs” by Gjerde, Cheung, and Lagnado. No specific claim is provided for application assessment.

### c29 — exists ✅ · applied ☐  (line 323)
_[GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2505.09614 confirmed as GX-Chen et al. 2025 on LLM causal reasoning biases; no specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms 2505.09614 as “Language Agents Mirror Human Causal Reasoning Biases. How Can We Help Them Think Like Scientists?” with Anthony GX-Chen et al. No specific claim is provided for application assessment.

### c30 — exists ☐ · applied ☐  (line 324)
_[Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f) (the interview; not machine-checkable, and no claim here rests on it beyond the quoted line)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403; existence not-checkable as the author notes, and no claim rests on it.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval attempt returned HTTP 403 and the item is marked not-checkable, so existence cannot be verified from the supplied evidence. No specific claim is provided for application assessment.

### c31 — exists ✅ · applied ☐  (line 326)
_[Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010) (Lucas, Bridgers, Griffiths & Gopnik, _Cognition_)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC confirm Lucas, Bridgers, Griffiths & Gopnik 2014 in Cognition; no specific claim provided to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm DOI 10.1016/j.cognition.2013.12.010 as the 2014 Cognition article by Lucas, Bridgers, Griffiths, and Gopnik. No specific claim is provided for application assessment.

### c32 — exists ✅ · applied ☐  (line 328)
_[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2606.06464 confirmed with Samiei, Yiu, Gopnik et al. among authors; no specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms 2606.06464 as “Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?” with Samiei, Yiu, Gopnik, and others. No specific claim is provided for application assessment.

### c33 — exists ✅ · applied ☐  (line 329)
_[Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521) (_PLOS ONE_; quotes checked against the published text 2026-10-17)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI and URL confirm Shardlow & Przybyła 2024 in PLOS ONE; no specific claim provided to evaluate.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms DOI 10.1371/journal.pone.0307521 as Shardlow and Przybyła’s 2024 PLOS ONE article “Deanthropomorphising NLP: Can a language model be conscious?” No specific claim is provided for application assessment.

### c34 — exists ✅ · applied ☐  (line 331)
_[Shinn et al. 2023](https://arxiv.org/abs/2303.11366) (Reflexion)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2303.11366 confirmed as Reflexion by Shinn et al. 2023; no specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms 2303.11366 as Shinn et al.’s “Reflexion: Language Agents with Verbal Reinforcement Learning.” No specific claim is provided for application assessment.

### c35 — exists ✅ · applied ☐  (line 332)
_[Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC confirm Squire 2009 'The Legacy of Patient H.M.' in Neuron; no specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm DOI 10.1016/j.neuron.2008.12.023 as Larry R. Squire’s 2009 Neuron article “The Legacy of Patient H.M. for Neuroscience.” No specific claim is provided for application assessment.

### c36 — exists ✅ · applied ☐  (line 333)
_[Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm)_
- claude: exists=verified applied=unchecked [no_basis] — URL fetch confirms Tolman (1948) 'Cognitive Maps in Rats and Men,' Psychological Review; no specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to a Classics in the History of Psychology page for Edward C. Tolman’s 1948 “Cognitive Maps in Rats and Men,” matching the reference. No specific claim is provided for application assessment.

### c37 — exists ⚠️ · applied ☐  (line 334)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)_
- claude: exists=nuance applied=unchecked [no_basis] — PMC page confirms Yiu, Kosoy & Gopnik article, but it is published 2023/2024 in Perspectives on Psychological Science rather than the generic 'journal' type with 2023 date—substance matches, minor date/venue imprecision; no specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The PMC page resolves and identifies “Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet)” by Yiu, Kosoy, and Gopnik, matching the reference. No specific claim is provided for application assessment.

## ✅ AGREE-clean (5)
### c02 — exists ✅ · applied ✅  (line 41)
_([Shinn et al. 2023](https://arxiv.org/abs/2303.11366))_
- claude: exists=verified applied=verified [evidence_text] — Reflexion paper exists and its abstract describes maintaining reflective text in an episodic memory buffer, supporting the claim of AI with written memory.
- gpt: exists=verified applied=verified [evidence_text] — arXiv ID 2303.11366 resolves to Shinn et al.'s Reflexion paper. The abstract explicitly describes agents maintaining reflective text in an episodic memory buffer, supporting the claim that AI systems with written memory existed earlier.

### c08 — exists ✅ · applied ✅  (line 98)
_([Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms))_
- claude: exists=verified applied=verified [evidence_text] — The Anthropic consumer-terms update exists and its text confirms users can choose to allow their data to train Claude.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic URL resolves to the stated consumer-terms update. The retrieved text says users may choose to allow their data to be used to improve Claude and future models, matching the claim.

### c13 — exists ✅ · applied ✅  (line 192)
_([Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010))_
- claude: exists=verified applied=verified [evidence_text] — Lucas et al. 2014 exists; the abstract confirms children more readily generalize the unusual conjunctive ('needs two') relationship while adults are biased toward disjunctive, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI resolves to Lucas et al.'s 2014 Cognition article. The abstract directly states that children were more likely than adults to generalize the unusual conjunctive relationship, supporting the 'needs two' versus 'each cause alone' claim.

### c14 — exists ✅ · applied ✅  (line 193)
_([GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614))_
- claude: exists=verified applied=verified [evidence_text] — The blicket-test LLM paper exists and its abstract confirms models reliably infer disjunctive ('any one') but struggle with conjunctive ('needs two') rules, mirroring adult biases.
- gpt: exists=verified applied=verified [evidence_text] — arXiv ID 2505.09614 resolves to the stated GX-Chen et al. paper. The abstract explicitly says LMs infer disjunctive relationships reliably, struggle with conjunctive ones, and show adult-like rather than child-like profiles.

### c15 — exists ✅ · applied ✅  (line 197)
_([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464))_
- claude: exists=verified applied=verified [evidence_text] — The Samiei/Yiu/Gopnik paper exists; the abstract confirms models approach human accuracy but explore less efficiently with the same conjunctive gap, and that active exploration improves adults' conjunctive reasoning while still requiring more tests.
- gpt: exists=verified applied=verified [evidence_text] — arXiv ID 2606.06464 resolves to the stated Samiei, Yiu, GX-Chen, Lin, Shen, Richards, Gopnik, and Precup paper. The abstract directly supports both claims: active exploration improves adults' conjunctive reasoning, conjunctive rules still require more tests, and state-of-the-art models approach human accuracy while exploring less efficiently with similar gaps.
