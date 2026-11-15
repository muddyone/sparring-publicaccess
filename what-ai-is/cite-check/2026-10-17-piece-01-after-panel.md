# Cite-check: piece 01 after panel revision (2026-10-17)

_Run `piece01-2026-10-17c`, substrates Claude + GPT, on
[positions/02-it-learns.md](../positions/02-it-learns.md) (revised after the
[panel](../panel/2026-10-17-piece-01/)). The full tool report follows._

## Resolutions

- **Nothing refuted.** 32 citations; existence confirmed for 22; the rest are internal links,
  header references and source-list entries with no claim attached.
- **New: Anthropic 2025 (consumer terms).** Verified on both substrates against the page.
- **Three splits, all previously resolved by hand:** Shardlow & Przybyła (quotes checked against
  the published text), Yiu, Kosoy & Gopnik and Squire 2009 (figures and the mirror-star detail
  checked against full texts for the synthesis). Gjerde et al.'s 86.0% was checked against the
  paper's Table 3 by Vera Tukey (an AI review agent) (panel record `3-vera.md`).
- **Model-knowledge-only:** Clark & Chalmers (Otto) and Anderson 1982 (proceduralization), both
  standard attributions.
- **Probe 2c numbers** are our own pilot data, not checkable by the tool; checked by hand against
  `pilots/gopnik-followup-2026-10-17/runs/probe4c/probe4.json` and the notes.

---

# cite-check report — piece01-2026-10-17c

**Source:** `positions/02-it-learns.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **32** citations checked
- existence independently confirmed: **22**
- application evidence-grounded: **18**
- application judged from model knowledge only: **3**
- not independently checkable: **7**
- buckets — clean **4** · problem **28** · disagree **3**

## ⛔ DISAGREE — escalate to human (3)
### c11 — exists ✅ · applied SPLIT  (line 71)
_Shardlow and Przybyła, arguing that a language model can't be conscious, put it plainly: once trained, "the weights no longer change," so models "have no capacity to learn beyond their initial training" ([Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Shardlow & Przybyła 2024 arguing an LLM cannot be conscious; the abstract supports the paper's framing that models don't update after training, consistent with the quoted claim.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref and the resolved PLOS page verify the article. The retrieved abstract supports the paper's general anti-sentience/consciousness position, but it does not contain the specific quoted claims about fixed weights or no learning after training.

### c14 — exists ✅ · applied SPLIT  (line 93)
_Her published case is more careful than the two-year-old who outsmarts the best AI ([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/))_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Yiu, Kosoy & Gopnik 2023 confirmed; title and framing (cultural technologies, imitation vs innovation) support the general claims, but the specific numeric figures (85%, 76%, teapot/stove details) cannot be verified from the retrieved snippet alone.
- gpt: exists=verified applied=unchecked [evidence_text] — The PMC page verifies the article title, authors, venue timing, and DOI. The retrieved snippet gives only metadata/title-level information and does not show the detailed task descriptions, percentages, or model results claimed.

### c15 — exists ✅ · applied SPLIT  (line 130)
_([Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023))_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Squire 2009 'Legacy of Patient H.M.' confirmed; abstract establishes H.M.'s memory impairment but does not specifically detail the mirror-drawing task, so the precise claim is plausible but not directly evidenced in the snippet.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref and Europe PMC verify Squire's 2009 Neuron article on patient H.M. The abstract confirms the article concerns H.M.'s legacy and memory impairment, but it does not specifically mention Milner's mirror-star tracing result across three days.

## ⚠️ AGREE-problem (28)
### c01 — exists ☐ · applied ☐  (line 4)
_the cite-checked synthesis [Does it learn?](../learning-and-gopnik.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path reference could not be fetched; no evidence to judge either axis.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative URL could not be fetched and the work is marked not-checkable. No source text was retrieved to assess whether it supports the stated provenance claim.

### c02 — exists ☐ · applied ☐  (line 5)
_the brief [How a model moves from version to version](../briefs/2026-10-17-9-how-models-change.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal brief reference not fetchable; no evidence to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative URL could not be fetched and the work is marked not-checkable. No source text was retrieved to assess the claim.

### c03 — exists ☐ · applied ☐  (line 6)
_Shardlow & Przybyła 2024_
- claude: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match, but this stub appears duplicated with c11 (a verified DOI); insufficient evidence to refute existence independently.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup produced no Crossref match for this incomplete author-year reference, which is insufficient to verify or decisively refute existence. There is no application evidence beyond the revision note.

### c04 — exists ☐ · applied ☐  (line 6)
_Lucas et al. 2014_
- claude: exists=unchecked applied=unchecked [no_basis] — No-match stub that corresponds to c18 (verified DOI); not enough to refute on its own.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup produced no Crossref match for this incomplete author-year reference, which is insufficient to verify or decisively refute existence. There is no application evidence beyond the revision note.

### c05 — exists ☐ · applied ☐  (line 6)
_Anthropic 2025_
- claude: exists=unchecked applied=unchecked [no_basis] — No-match stub corresponding to c13 (verified web source); insufficient evidence to refute alone.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup produced no Crossref match for this incomplete reference, which is insufficient to verify or decisively refute existence. There is no application evidence beyond the revision note.

### c06 — exists ☐ · applied ☐  (line 8)
_Cite-checked 2026-10-17 ([first](../cite-check/2026-10-17-position-pieces.md), [after revision](../cite-check/2026-10-17-piece-01-revised.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cite-check records not fetchable; no evidence to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — Both cited relative URLs could not be fetched and are marked not-checkable. No source text was retrieved to verify the cite-check-date claim.

### c07 — exists ☐ · applied ☐  (line 10)
_revised after panel review ([records](../panel/2026-10-17-piece-01/))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal panel-record directory not fetchable; no evidence to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative panel-review URL could not be fetched and is marked not-checkable. No source text was retrieved to verify the panel-review claim.

### c08 — exists ☐ · applied ☐  · ⚑ degraded  (line 25)
_In May 2026 Alison Gopnik told Chris Hayes that a two-year-old routinely outsmarts the best AI models ([Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f))_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Podcast URL returned HTTP 403, so neither the episode's existence nor the specific quoted claim can be verified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The podcast URL fetch returned HTTP 403, so the work is not checkable from the retrieved evidence. No transcript or other source text was available to assess the quoted claim.

### c09 — exists ✅ · applied ⚠️  (line 41)
_Edward Tolman's rats learned a maze while exploring it for no reward, and showed it only when food appeared ([Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm))_
- claude: exists=verified applied=verified [evidence_text] — Tolman (1948) 'Cognitive Maps in Rats and Men' confirmed at the URL; the snippet describes maze-learning experiments consistent with the latent-learning claim.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to Tolman's 1948 'Cognitive Maps in Rats and Men' with publication details. The snippet supports that Tolman discusses rat maze learning, but it does not explicitly show the no-reward/food-appears latent-learning detail.

### c10 — exists ✅ · applied ✅  · ⚑ degraded  (line 60)
_Clark and Chalmers' extended-mind argument applies the same logic to people: for Otto, a man with memory loss who relies on a notebook he always carries, the notebook functions as memory ([Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Clark & Chalmers 'The Extended Mind' (1998) confirmed via Crossref; the Otto-and-notebook thought experiment is the paper's central and well-known argument.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Clark and Chalmers' 1998 article 'The Extended Mind' in Analysis. The Otto-notebook memory example is a central part of that article, but this application judgment relies on model knowledge because no abstract or usable source text was retrieved.

### c12 — exists ☐ · applied ☐  (line 83)
_([brief](../briefs/2026-10-17-9-how-models-change.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal brief not fetchable; no evidence to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The relative URL could not be fetched and is marked not-checkable. No source text was retrieved to assess the claim about how new models are shaped.

### c16 — exists ✅ · applied ✅  · ⚑ degraded  (line 151)
_John Anderson's proceduralization; [Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Anderson 1982 'Acquisition of cognitive skill' confirmed; this work is the standard source for proceduralization in skill acquisition (ACT theory).
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Anderson's 1982 Psychological Review article 'Acquisition of cognitive skill.' The attribution of proceduralization in cognitive skill acquisition to Anderson is supported by model knowledge, since no source text was retrieved.

### c17 — exists ✅ · applied ⚠️  (line 167)
_([Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606))_
- claude: exists=verified applied=nuance [evidence_text] — arXiv paper on affordance reasoning confirmed and matches the tool-innovation theme with GPT-4o near human performance, but the specific figures (81.3%, 88.2%, 86.0%) are not stated in the retrieved abstract.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv page resolves and verifies the title and authors. The abstract supports the general claim that GPT-4o with chain-of-thought performed on par with humans on newly designed affordance tasks, but the retrieved snippet does not verify the exact 20-item setup or percentages.

### c21 — exists ☐ · applied ☐  (line 201)
_([The result](../../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md).)_
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited author's own pilot study (is_citation=false, deliberately_uncited); not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as deliberately uncited / not a bibliographic citation, so both axes are unchecked.

### c22 — exists ☐ · applied ☐  (line 204)
_([details](../../pilots/gopnik-followup-2026-10-17/README.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited author's own follow-up study; not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as deliberately uncited / not a bibliographic citation, so both axes are unchecked.

### c23 — exists ✅ · applied ☐  (line 254)
_[Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Anderson (1982), 'Acquisition of cognitive skill', Psychological Review 89(4):369-406, matching the DOI. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Anderson's 1982 Psychological Review article “Acquisition of cognitive skill” with the cited DOI. No claim was supplied for application checking.

### c24 — exists ✅ · applied ☐  (line 255)
_[Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms) (consumer terms, 2025-08-28)_
- claude: exists=verified applied=unchecked [no_basis] — URL fetch confirms Anthropic's 'Updates to Consumer Terms and Privacy Policy' dated Aug 28, 2025, matching the citation. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The Anthropic URL resolves to “Updates to Consumer Terms and Privacy Policy” dated Aug. 28, 2025. No claim was supplied for application checking.

### c25 — exists ✅ · applied ☐  (line 257)
_[Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Clark & Chalmers (1998), 'The Extended Mind', Analysis 58(1):7-19, matching the DOI. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Clark and Chalmers, “The Extended Mind,” Analysis 58(1), 1998, with the cited DOI. No claim was supplied for application checking.

### c26 — exists ✅ · applied ☐  (line 258)
_[Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv page confirms Gjerde, Cheung & Lagnado (2025) paper at 2502.16606. No specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv URL resolves to arXiv:2502.16606, “Reasoning about Affordances: Causal and Compositional Reasoning in LLMs,” by Gjerde, Cheung, and Lagnado. No claim was supplied for application checking.

### c27 — exists ✅ · applied ☐  (line 259)
_[GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv page confirms GX-Chen et al. (2025) at 2505.09614 on LLM causal reasoning biases. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv URL resolves to arXiv:2505.09614, “Language Agents Mirror Human Causal Reasoning Biases. How Can We Help Them Think Like Scientists?” with Anthony GX-Chen and coauthors. No claim was supplied for application checking.

### c28 — exists ☐ · applied ☐  (line 260)
_[Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f) (the interview; not machine-checkable, and no claim here rests on it beyond the quoted line)_
- claude: exists=unchecked applied=unchecked [no_basis] — URL fetch returned HTTP 403; existence not checkable per author note, and no claim rests on it.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval for the Pocket Casts URL returned HTTP 403, and the item is marked not-checkable. No claim was supplied for application checking.

### c29 — exists ✅ · applied ☐  (line 262)
_[Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010) (Lucas, Bridgers, Griffiths & Gopnik, _Cognition_)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC confirm Lucas, Bridgers, Griffiths & Gopnik (2014), Cognition, matching the DOI. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm the 2014 Cognition article by Lucas, Bridgers, Griffiths, and Gopnik with the cited DOI. No claim was supplied for application checking.

### c30 — exists ✅ · applied ☐  (line 264)
_[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv page confirms Samiei, Yiu, ... Gopnik et al. (2026) at 2606.06464. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv URL resolves to arXiv:2606.06464, “Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?” by Samiei, Yiu, and coauthors. No claim was supplied for application checking.

### c31 — exists ✅ · applied ☐  (line 265)
_[Shardlow & Przybyła 2024](https://doi.org/10.1371/journal.pone.0307521) (_PLOS ONE_; quotes checked against the published text 2026-10-17)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and PLOS ONE confirm Shardlow & Przybyła (2024) matching the DOI. No specific claim provided to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the resolved PLOS page confirm Shardlow and Przybyła’s 2024 PLOS ONE article with the cited DOI. No claim was supplied for application checking.

### c32 — exists ✅ · applied ☐  (line 267)
_[Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC confirm Squire (2009), 'The Legacy of Patient H.M. for Neuroscience', Neuron, matching the DOI. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm Squire’s 2009 Neuron article “The Legacy of Patient H.M. for Neuroscience” with the cited DOI. No claim was supplied for application checking.

### c33 — exists ⚠️ · applied ☐  (line 268)
_[Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm)_
- claude: exists=verified applied=unchecked [no_basis] — URL fetch confirms Tolman (1948) 'Cognitive Maps in Rats and Men', Psychological Review 55(4), hosted at the cited archive. No specific claim provided.
- gpt: exists=nuance applied=unchecked [no_basis] — The URL resolves to a Classics in the History of Psychology page for Tolman’s 1948 “Cognitive Maps in Rats and Men,” though the parsed title “Maps” is abbreviated/imprecise. No claim was supplied for application checking.

### c34 — exists ✅ · applied ☐  (line 269)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)_
- claude: exists=verified applied=unchecked [no_basis] — PMC page confirms Yiu, Kosoy & Gopnik article (published 2023, issue 2024), matching authors; note the journal is Perspect Psychol Sci not simply unknown. No specific claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The PMC page resolves and identifies the article “Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet)” by Yiu, Kosoy, and Gopnik, published online in 2023. No claim was supplied for application checking.

### c35 — exists ☐ · applied ☐  (line 270)
_Full references and the cite-check records: [the synthesis](../learning-and-gopnik.md) and [brief 9](../briefs/2026-10-17-9-how-models-change.md)._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal pointer to synthesis and cite-check records, not a bibliographic citation (is_citation=false).
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a bibliographic citation, but rather a pointer to full references and cite-check records. Both axes are therefore unchecked.

## ✅ AGREE-clean (4)
### c13 — exists ✅ · applied ✅  (line 85)
_Anthropic, for one, trains new models on consumer conversations when users allow it ([Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms))_
- claude: exists=verified applied=verified [evidence_text] — Anthropic's consumer-terms update page confirms users can opt in to let their data train Claude models, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The Anthropic URL resolves to 'Updates to Consumer Terms and Privacy Policy.' The snippet states that users can choose to allow their data to improve Claude and future models, matching the claim with the caveat that it applies to covered consumer plans.

### c18 — exists ✅ · applied ✅  (line 174)
_([Lucas et al. 2014](https://doi.org/10.1016/j.cognition.2013.12.010))_
- claude: exists=verified applied=verified [evidence_text] — Lucas et al. 2014 confirmed; abstract states children more readily generalize the unusual conjunctive relationship than adults, directly supporting the 'needs two' claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC verify the Lucas et al. 2014 Cognition article. The abstract states that children were more likely than adults to generalize the unusual conjunctive causal relationship, supporting the 'needs two' claim.

### c19 — exists ✅ · applied ✅  (line 175)
_([GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614))_
- claude: exists=verified applied=verified [evidence_text] — arXiv 2505.09614 confirmed; abstract describes LMs reliably inferring disjunctive but struggling with conjunctive rules, mirroring adult bias, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv page resolves and verifies the cited paper. The abstract directly says LMs reliably infer disjunctive relationships but struggle with conjunctive ones, and that a similar bias appears in adult humans.

### c20 — exists ✅ · applied ✅  (line 179)
_([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464))_
- claude: exists=verified applied=verified [evidence_text] — arXiv 2606.06464 (Samiei, Yiu, Gopnik et al.) confirmed; abstract states models approach human accuracy but explore less efficiently and active exploration improves adults' conjunctive reasoning though still requiring more tests, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv page resolves and verifies the cited paper and authors. The abstract directly supports the claims that active exploration improves adults' conjunctive reasoning, conjunctive rules still take more tests, and leading models approach human accuracy while exploring less efficiently and showing similar gaps.
