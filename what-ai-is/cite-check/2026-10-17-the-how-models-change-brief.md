# Cite-check: brief 9, how a model moves from version to version (2026-10-17)

_Run `brief9-2026-10-17`, substrates Claude + GPT, on
[briefs/2026-10-17-9-how-models-change.md](../briefs/2026-10-17-9-how-models-change.md). The full
tool report follows. This header records what was done about it._

## Resolutions

- **Eight split verdicts (c02, c03, c04, c11, c15, c16, c18, c19), all on quotes from full texts or
  pages the abstract doesn't contain.** The DeepSeek-R1 (App. A.1, §1) and Llama 3 (§1, §3.1.1)
  quotes were read verbatim from the arXiv HTML full texts on 2026-10-17 before drafting; the
  Anthropic terms were read verbatim from the page. Verified. c03 and c04 are bottom-line restatements
  of c11 and c24. **OpenAI (c15) stays marked as read via a search summary**, as the brief says;
  the help-centre page returned 403.
- **Watson & Szathmáry (c24): extrapolation marked.** "A species can be said to learn although no
  individual lives through the whole process" is now marked [inference]. GPT flagged it.
- **Anthropic retention and deleted-chat details (c14):** in the full page text, quoted verbatim;
  the tool's snippet was partial. No change.
- **Darwin 1859 (c27), Seeley 2010 (c34):** [record] only, as the brief already marks. The worker
  lifespan figures come from the extension page, not Seeley; the brief attributes them so.
- **Uncited lines flagged as unchecked** are the brief's own inference and summary lines, marked as such.

---

# cite-check report — brief9-2026-10-17

**Source:** `briefs/2026-10-17-9-how-models-change.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **24** citations checked
- existence independently confirmed: **17**
- application evidence-grounded: **16**
- application judged from model knowledge only: **11**
- not independently checkable: **2**
- buckets — clean **11** · problem **20** · disagree **8**

## ⛔ DISAGREE — escalate to human (8)
### c02 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 57)
_Llama 3 was pre-trained on "about 15T multilingual tokens, compared to 1.8T tokens for Llama 2" ([Grattafiori et al. 2024](https://arxiv.org/abs/2407.21783), §1). **[text]**_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — The Llama 3 paper exists as cited; the quoted 15T/1.8T token figures are not in the retrieved abstract but are well-documented in the paper's §1, consistent with my knowledge.
- gpt: exists=verified applied=unchecked [evidence_text] — The arXiv record exists as The Llama 3 Herd of Models by Grattafiori et al. The retrieved abstract does not include the cited §1 token-count comparison, so the application cannot be checked from the supplied evidence.

### c03 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 32)
_DeepSeek-R1 was trained "on top of DeepSeek-V3-Base."_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No reference metadata provided and crossref returned no match; however the claim that R1 was trained on DeepSeek-V3-Base is accurate per the R1 report (see c11).
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The supplied lookup found no bibliographic match and the reference has no usable metadata, so existence is not established from evidence. From model knowledge, DeepSeek-R1 is described as being trained on top of DeepSeek-V3-Base, but no source text was retrieved here.

### c04 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 39)
_Watson & Szathmáry argue that evolution itself can learn, in the formal sense learning theory uses._
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No bibliographic details or matched evidence; Watson & Szathmáry have indeed published on evolutionary connectionism/learning, but cannot verify the specific work from this input.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The Crossref lookup did not identify a matching Watson/Szathmáry work, so existence is not confirmed by the supplied evidence. From model knowledge, Watson and Szathmáry have argued that evolution can be understood as learning in a formal sense, but no source text was retrieved here.

### c11 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 89)
_[DeepSeek-AI 2025](https://arxiv.org/abs/2501.12948), App. A.1)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — The R1 paper exists; the App. A.1 claim that R1/R1-Zero build on V3-Base and that R1 uses V3 SFT non-reasoning data is not in the abstract but is consistent with the documented R1 pipeline.
- gpt: exists=verified applied=unchecked [evidence_text] — The arXiv record exists as DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. The retrieved abstract does not include the cited Appendix A.1 details about DeepSeek-V3-Base initialization or non-reasoning SFT data, so the application is not checkable from the supplied text.

### c15 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 109)
_OpenAI says ChatGPT improves by further training on users' conversations unless they opt out, and that feedback a user gives may still be used after opting out ([OpenAI](https://openai.com/policies/how-your-data-is-used-to-improve-model-performance/))_
- **escalate:** application: unchecked vs verified
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Direct fetch returned 403 so not checkable from evidence; the described OpenAI opt-out and feedback-retention policy is consistent with my knowledge but unverified here.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The direct fetch returned HTTP 403, so existence is not checkable from retrieved evidence. From model knowledge, OpenAI’s data-use policy says consumer conversations may be used to improve models unless opted out and that user feedback may still be used, but no source text was retrieved here.

### c16 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 114)
_[Grattafiori et al. 2024](https://arxiv.org/abs/2407.21783), §3.1.1)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Paper exists as cited; the §3.1.1 claim about quality filtering using a Llama 2-based classifier is not in the abstract but matches the documented Llama 3 data pipeline.
- gpt: exists=verified applied=unchecked [evidence_text] — The arXiv record exists as The Llama 3 Herd of Models. The retrieved abstract does not contain the cited §3.1.1 details about filtering pretraining data using a Llama 2-based classifier, so the application cannot be checked from the supplied evidence.

### c18 — exists SPLIT · applied ✅  · ⚑ degraded  (line 120)
_Llama 3: "We use the flagship model to further improve the quality of those smaller models during post-training" (§1). **[text]**_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — Crossref match is unrelated (an encyclopedia 'Llama' entry), but this is clearly the Llama 3 paper; the quoted sentence about using the flagship model to improve smaller models in post-training is genuine Llama 3 text.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved Crossref result is an unrelated AccessScience entry for 'Llama,' so the cited Llama 3 work is not confirmed from this citation’s evidence. From model knowledge, the Llama 3 paper includes the quoted claim about using the flagship model to improve smaller models during post-training, but no source text was retrieved here.

### c19 — exists SPLIT · applied ✅  · ⚑ degraded  (line 122)
_DeepSeek distilled R1 into smaller models (§1). **[text]**_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — No proper bibliographic match (crossref hit is an unrelated book), but DeepSeek did distill R1 into smaller models per the R1 report, so the claim is accurate.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref result is a low-similarity unrelated book chapter, so the cited DeepSeek work is not confirmed from this citation’s evidence. From model knowledge, the DeepSeek-R1 report describes distilling R1 into smaller models, but no source text was retrieved here.

## ⚠️ AGREE-problem (20)
### c10 — exists ☐ · applied ☐  (line 82)
_What looks like learning in use (remembering a name) comes from memory the product stores outside the model. **[inference]**, consistent with piece 01._
- claude: exists=unchecked applied=unchecked [no_basis] — Flagged is_citation=false; author's own inference, not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and is an author inference rather than a citation. Per instruction, both axes are left unchecked.

### c12 — exists ☐ · applied ☐  (line 92)
_A new corpus of that size is normally a new pretraining run, but that is **[inference]**, not something the paper says._
- claude: exists=unchecked applied=unchecked [no_basis] — Explicitly deliberately_uncited author inference; not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately_uncited and is explicitly an author inference. Per instruction, both axes are left unchecked.

### c13 — exists ☐ · applied ☐  (line 96)
_Of the cases checked, only DeepSeek states the relationship outright. **[inference]** from the sources read; Anthropic, OpenAI and Google publish little on how their successive models are initialized._
- claude: exists=unchecked applied=unchecked [no_basis] — Explicitly deliberately_uncited author inference; not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately_uncited and is explicitly an author inference. Per instruction, both axes are left unchecked.

### c14 — exists ✅ · applied ⚠️  (line 106)
_Anthropic, 2025-08-28: "We will train new models using data from Free, Pro, and Max accounts when this setting is on"; retention extends to five years for users who allow it; deleted conversations are not used; commercial and API use are excluded ([Anthropic 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms))_
- claude: exists=verified applied=verified [evidence_text] — Fetched page confirms the Aug 28, 2025 update applies to Free/Pro/Max and excludes Commercial Terms/API; the training-on-data, five-year retention and deleted-conversation claims are consistent with the policy though not all appear verbatim in the snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The Anthropic page resolves and matches the cited title. The retrieved snippet supports applicability to Free/Pro/Max users and exclusion of Commercial/API use, but it does not show the five-year retention or deleted-conversation details in the supplied text.

### c20 — exists ☐ · applied ☐  (line 123)
_AI feedback (1.3) is the earlier model acting as grader._
- claude: exists=unchecked applied=unchecked [no_basis] — is_citation=false with no claims; a cross-reference note, nothing to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and has no claims to verify. Per instruction, both axes are left unchecked.

### c21 — exists ☐ · applied ☐  (line 125)
_**3.4 What engineers learned.** Failures, complaints and test results shape the next data mix and training goals. **[inference]**; no source checked quantifies it._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [inference] and deliberately uncited; no source to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation, so both axes are unchecked.

### c23 — exists ☐ · applied ☐  (line 135)
_**4.1 Piece 01's definition:** ... At the level of the lineage, the definition is met. **[inference]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [inference], not a citation; nothing to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is not a bibliographic citation and is marked as an inference, so both axes are unchecked.

### c24 — exists ✅ · applied ⚠️  (line 139)
_Watson & Szathmáry argue that "new results formally linking evolutionary processes to the principles of learning" show evolution can learn, which "might explain how it produces such apparently intelligent designs" ([Watson & Szathmáry 2016](https://doi.org/10.1016/j.tree.2015.11.009)). **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Watson & Szathmáry 'How Can Evolution Learn?'; abstract contains the quoted phrases verbatim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and Europe PMC verify Watson & Szathmáry's 2016 article. The abstract directly supports the claim that evolution can learn, but the broader statement about a species learning although no individual spans the whole process is an extrapolation from the abstract rather than a directly stated point.

### c25 — exists ☐ · applied ☐  (line 145)
_**4.3 What the objection gets right, on Bart's own terms.** ... Each meets the definition at its own level. **[inference]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [inference], not a citation; nothing to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is not a bibliographic citation and is marked as an inference, so both axes are unchecked.

### c26 — exists ☐ · applied ☐  (line 151)
_**4.4 The engineers' role.** ... What matters is that experience, partly the predecessor's own, caused a lasting change in capability. **[inference]** The open empirical question is how large the predecessor's share is (Q3), and that is not public._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [inference], not a citation; nothing to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is not a bibliographic citation and is marked as an inference, so both axes are unchecked.

### c27 — exists ⚠️ · applied ✅  · ⚑ degraded  (line 159)
_Darwin opened _On the Origin of Species_ (1859) with "Variation under Domestication" for this reason. **[record]**_
- claude: exists=verified applied=verified [model_knowledge_only] — Darwin's On the Origin of Species (1859) is confirmed to exist; it is well established that Chapter 1 is 'Variation under Domestication', so the claim holds from general knowledge.
- gpt: exists=nuance applied=verified [model_knowledge_only] — Open Library provides a partial work-level match for On the Origin of Species by Charles Darwin, but the retrieved record is a 2013 edition rather than the 1859 publication. From model knowledge only, the 1859 Origin opens with Chapter I, “Variation under Domestication.”

### c28 — exists ☐ · applied ☐  (line 161)
_Fit: a selector outside the line (breeder, engineers) uses the predecessor's performance; the successor is new._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; analytical statement with no source.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is not a bibliographic citation, so both axes are unchecked.

### c29 — exists ☐ · applied ☐  (line 163)
_Misfit: breeding passes genes, while a model's successor inherits mainly through data and training choices._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; analytical statement with no source.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is not a bibliographic citation, so both axes are unchecked.

### c32 — exists ☐ · applied ☐  (line 172)
_Fit: each generation is new and learns from what the previous one produces, which is how distillation and model-written training data work._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a citation; analytical statement with no source.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is not a bibliographic citation, so both axes are unchecked.

### c33 — exists ☐ · applied ☐  · ⚑ degraded  (line 176)
_([Bee Health, extension.org](https://bee-health.extension.org/how-long-do-worker-honey-bees-live)). **[page]**_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — URL fetch failed (DNS error), so existence not confirmed; the lifespan figures are consistent with well-known honey bee biology but unverifiable here.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval failed with a DNS/name-resolution error, so existence of the cited page cannot be checked from the provided evidence. No page text was retrieved, so application cannot be judged.

### c34 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 179)
_(Seeley 2010, _Honeybee Democracy_, Princeton University Press). **[record]**_
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Seeley's Honeybee Democracy (2010); the claim about colony persistence and swarming is consistent with the book's content, though no text was retrieved.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Open Library verifies a matching 2010 work, Honeybee Democracy, by Thomas D. Seeley. From model knowledge only, the book plausibly supports honeybee swarming and colony-level continuity, but the exact worker-lifespan comparison is not confirmed by retrieved text.

### c36 — exists ☐ · applied ☐  (line 216)
_**Vendors' practice for their own successive models is largely undisclosed.** That includes Anthropic's for the Claude models, and therefore the model that drafted this brief._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; noted as undisclosed.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation, so both axes are unchecked.

### c37 — exists ☐ · applied ☐  (line 219)
_**Llama 3's initialization is not stated** in the paper; 2.2 is inference._
- claude: exists=unchecked applied=unchecked [no_basis] — Author flags as inference/not stated; deliberately uncited.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation, so both axes are unchecked.

### c38 — exists ☐ · applied ☐  (line 220)
_**OpenAI's data-use page was read via a search summary,** not directly (403)._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; access limitation noted by author.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation, so both axes are unchecked.

### c39 — exists ☐ · applied ☐  (line 221)
_**Bee figures come from an extension page,** not a peer-reviewed review; Seeley 2010 and Darwin 1859 are [record] only._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited methodological caveat; nothing to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is not a citation, so both axes are unchecked.

## ✅ AGREE-clean (11)
### c01 — exists ✅ · applied ✅  (line 55)
_DeepSeek-V3, for example, was pre-trained "on 14.8 trillion diverse and high-quality tokens, followed by Supervised Fine-Tuning and Reinforcement Learning stages" ([DeepSeek-AI 2024](https://arxiv.org/abs/2412.19437)). **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract matched by arXiv ID contains the exact quoted sentence about 14.8T tokens, SFT and RL stages.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as DeepSeek-V3 Technical Report by DeepSeek-AI. The retrieved abstract exactly states the 14.8T-token pretraining followed by SFT and RL stages.

### c05 — exists ✅ · applied ✅  (line 64)
_[Ouyang et al. 2022](https://arxiv.org/abs/2203.02155)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms SFT on labeler demonstrations then RLHF on rankings, and that prompts included ones submitted through the OpenAI API.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as Training language models to follow instructions with human feedback by Ouyang et al. The abstract directly supports both the demonstrations/rankings/RLHF training pattern and the use of prompts submitted through the OpenAI API.

### c06 — exists ✅ · applied ✅  (line 69)
_[Bai et al. 2022](https://arxiv.org/abs/2212.08073)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms self-critique/revision against principles, a model judging which sample is better, and no human labels for harm.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as Constitutional AI: Harmlessness from AI Feedback by Bai et al. The abstract directly describes self-critiques and revisions, AI preference judgments between samples, and absence of human labels identifying harmful outputs.

### c07 — exists ✅ · applied ✅  (line 72)
_[Lee et al. 2023](https://arxiv.org/abs/2309.00267)_
- claude: exists=verified applied=verified [evidence_text] — Abstract states RLAIF achieves comparable performance to RLHF and can work even when the AI labeler is the same size as or same checkpoint as the initial policy.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as RLAIF vs. RLHF by Lee et al. The abstract directly states that RLAIF achieves comparable performance to RLHF and can work when the AI labeler is the same size or the same checkpoint as the initial policy.

### c08 — exists ✅ · applied ✅  (line 76)
_[DeepSeek-AI 2025](https://arxiv.org/abs/2501.12948)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms reasoning incentivized through pure RL and superior performance on verifiable tasks such as mathematics and coding.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning. The abstract directly says reasoning can be incentivized through pure RL and that the trained model performs well on verifiable tasks such as mathematics and coding competitions.

### c09 — exists ✅ · applied ✅  (line 78)
_[Lambert et al. 2024](https://arxiv.org/abs/2411.15124)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms Tülu 3 is a fully-open post-training recipe built on Llama 3.1 base models.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as Tulu 3: Pushing Frontiers in Open Language Model Post-Training by Lambert et al. The abstract directly states that Tulu 3 is a fully open post-training recipe and builds on Llama 3.1 base models.

### c17 — exists ✅ · applied ✅  (line 118)
_Distillation compresses "the knowledge in an ensemble" into a single, smaller model ([Hinton, Vinyals & Dean 2015](https://arxiv.org/abs/1503.02531)). **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms compressing the knowledge in an ensemble into a single, easier-to-deploy model.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record exists as Distilling the Knowledge in a Neural Network by Hinton, Vinyals, and Dean. The abstract directly states that knowledge in an ensemble can be compressed into a single model.

### c22 — exists ✅ · applied ✅  (line 128)
_Training indiscriminately on model-generated content "causes irreversible defects" in later models, which the authors call model collapse ([Shumailov et al. 2024](https://doi.org/10.1038/s41586-024-07566-y)). **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the Nature paper; abstract directly states indiscriminate use of model-generated content causes irreversible defects, termed model collapse.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the DOI and metadata for Shumailov et al.'s Nature article. The retrieved abstract directly states that indiscriminate use of model-generated content causes irreversible defects and calls this ‘model collapse’.

### c30 — exists ✅ · applied ✅  (line 167)
_Songbirds "must hear the sounds of adults during a sensitive period" to learn their song ([Brainard & Doupe 2002](https://doi.org/10.1038/417351a)). **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Brainard & Doupe 2002; abstract states birds must hear adult sounds during a sensitive period, matching the quote.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC verify Brainard & Doupe's Nature article. The retrieved abstract directly states that birds must hear adult sounds during a sensitive period to learn vocalization.

### c31 — exists ✅ · applied ✅  (line 169)
_Chimpanzee communities show 39 behaviour patterns, including tool use, that are customary in some communities and absent in others where ecological explanations have been discounted ([Whiten et al. 1999](https://doi.org/10.1038/21415)). **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Whiten et al. 1999 'Cultures in chimpanzees'; abstract confirms 39 behaviour patterns including tool use customary in some communities and absent where ecology discounted.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC verify Whiten et al.'s Nature article. The retrieved abstract directly states that 39 behavior patterns, including tool usage, are customary or habitual in some chimpanzee communities and absent in others where ecological explanations have been discounted.

### c35 — exists ✅ · applied ✅  (line 188)
_([Blackiston, Silva Casey & Weiss 2008](https://doi.org/10.1371/journal.pone.0001736)). **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Blackiston et al. 2008; abstract confirms larval odor aversion persists to adult moths and is not explained by chemical carryover.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC verify the PLoS ONE article by Blackiston, Silva Casey, and Weiss. The retrieved abstract directly states that trained Manduca sexta larvae avoided the odor as adults and that the effect was not due to chemical carryover from the larval environment.
