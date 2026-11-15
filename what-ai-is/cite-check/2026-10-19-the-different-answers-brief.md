# cite-check report — brief12-different-answers

**Source:** `briefs/2026-10-19-12-different-answers.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **168** citations checked
- existence independently confirmed: **108**
- application evidence-grounded: **106**
- application judged from model knowledge only: **41**
- not independently checkable: **6**
- buckets — clean **37** · problem **82** · disagree **65**

## ⛔ DISAGREE — escalate to human (65)
### c23 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 66)
_Lewis et al. 2020_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — No retrieval match, but Lewis et al. 2020 is almost certainly the well-known Retrieval-Augmented Generation (RAG) paper, which supports the claim that retrieval reduces but does not eliminate errors.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The retrieved evidence contains only a Crossref no-match for an underspecified Lewis et al. 2020 reference. From model knowledge, Lewis et al. 2020 likely refers to RAG and supports retrieval reducing hallucinations/errors, though the exact phrasing 'reduce rather than remove' is a general inference.

### c24 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 67)
_Shuster et al. 2021_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — No retrieval match, but Shuster et al. 2021 'Retrieval Augmentation Reduces Hallucination in Conversation' is a known work directly supporting the claim that retrieval reduces errors without removing them.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The retrieved evidence does not confirm the Shuster et al. 2021 work. From model knowledge, Shuster et al. work on retrieval-augmented dialogue supports retrieval reducing hallucination but not eliminating it, so the claim is broadly supported with caveat.

### c28 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 71)
_Schoenegger et al. 2024_
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No retrieval match; Schoenegger et al. 2024 plausibly covers LLM ensemble/aggregation for forecasting, broadly consistent with 'pooling across models.'
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved evidence does not identify or confirm a Schoenegger et al. 2024 work. No source text was retrieved, and the sparse claim 'pooling across models' cannot be reliably assessed here.

### c32 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 75)
_Smit et al. 2023_
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No retrieval match; Smit et al. (likely 2024) critically examines multi-agent debate vs simpler baselines, broadly consistent with the claim though the year/details cannot be confirmed.
- gpt: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match for the sparse Smit et al. 2023 reference. No source text was retrieved, and I cannot reliably assess the claimed comparison between debate and simpler sampling from the provided evidence.

### c39 — exists SPLIT · applied SPLIT  (line 96)
_Choosing the single most likely next word at every step produces "bland and strangely repetitive" text. Sampling from the "dynamic nucleus" of the probability distribution (nucleus sampling) produces text closer to human writing. Decoding strategy alone changes quality "dramatically", even from exactly the same model._
- **escalate:** existence: verified vs unchecked; application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The quoted phrases 'bland and strangely repetitive', 'dynamic nucleus', and decoding affecting quality 'dramatically' appear directly in the Holtzman et al. abstract (c38), confirming both existence and application.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item contains claim text but no identifiable bibliographic reference or retrieved source evidence. Although the wording resembles Holtzman et al., this record itself is not checkable as a citation.

### c42 — exists SPLIT · applied ✅  · ⚑ degraded  (line 107)
_Five LLMs configured to be deterministic, eight tasks, ten runs each. Accuracy varied by up to 15% across naturally occurring runs, and the gap between best and worst possible performance reached 70%. "None of the LLMs consistently delivers repeatable accuracy across all tasks, much less identical output strings."_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Same source as c41; the retrieved abstract explicitly reports five LLMs, eight tasks, ten runs, up to 15% accuracy variation, up to 70% gap, and non-repeatable output strings.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No bibliographic reference or retrieved source is provided for this entry, so existence cannot be checked. The stated figures match the known abstract-level claims of Atil et al. arXiv:2408.04667, but this assessment is from model knowledge only.

### c45 — exists SPLIT · applied ✅  · ⚑ degraded  (line 116)
_829 coding problems from three benchmarks. The share of problems where repeated requests never produced the same test output was 76%, 51% and 48% on the three benchmarks. Temperature 0 "does not guarantee determinism", though it reduces variation._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Content from the same Ouyang et al. paper; abstract reports 829 problems, zero-equal-output ratios of 75.76%/51.00%/47.56%, and that temperature 0 does not guarantee determinism, matching the claims.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No bibliographic reference or retrieved source is provided for this entry, so existence cannot be checked. The numerical claims match the known abstract of Ouyang et al. arXiv:2308.02828, but this assessment is from model knowledge only.

### c48 — exists SPLIT · applied ✅  · ⚑ degraded  (line 125)
_The usual explanation (parallel computation plus floating-point rounding) is incomplete. The main cause is that the server's arithmetic depends on how many *other* users' requests are batched alongside yours, and server load changes that from moment to moment._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Same blog post; the fetched snippet names the 'concurrency + floating point' hypothesis as incomplete and describes batch-invariance, supporting the batching/server-load claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No bibliographic reference or retrieved source is provided for this entry, so existence cannot be checked. The explanation about batching and batch-dependent arithmetic matches the known argument of the Thinking Machines post, but this assessment is from model knowledge only.

### c49 — exists SPLIT · applied SPLIT  · ⚑ degraded  (line 128)
_Demonstration: 1,000 completions of "Tell me about Richard Feynman" at temperature 0 on one open model gave 80 unique completions. They were identical for the first 102 tokens and split at the 103rd. With purpose-built kernels, all 1,000 were identical, at some cost in speed._
- **escalate:** existence: verified vs unchecked; application: unchecked vs verified
- claude: exists=verified applied=unchecked [model_knowledge_only] — The source blog exists and references experiments, but the retrieved snippet does not include the specific Feynman/80-completions/102-token figures, so those numbers cannot be confirmed from evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — No bibliographic reference or retrieved source is provided for this entry, so existence cannot be checked. The Feynman-completion demonstration is consistent with the known contents of the Thinking Machines post, but this assessment is from model knowledge only.

### c51 — exists ✅ · applied SPLIT  (line 135)
_Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025a). Prompting Science Report 1: Prompt engineering is complicated and contingent. arXiv:2503.04818. https://arxiv.org/abs/2503.04818 **[abstract + report text read]**_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Report exists with matching ID/title/authors; the abstract addresses benchmarking standards and prompting but does not directly mention 'repeating the question 100 times,' which likely appears in report body text.
- gpt: exists=verified applied=unchecked [evidence_text] — The arXiv record and URL match the cited title, authors, year, and arXiv ID. The retrieved abstract supports the broad topic of benchmark measurement and prompting contingency, but it does not mention repeating questions 100 times.

### c79 — exists SPLIT · applied ☐  · ⚑ degraded  (line 362)
_Bommasani et al. 2022 **[report]**_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [model_knowledge_only] — Bare 'Bommasani et al. 2022' with no title; crossref returned no match (existence_status no-match). A relevant algorithmic monoculture work by Bommasani et al. exists, but this entry lacks metadata to confirm.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is too incomplete to identify a specific work, and the only retrieved evidence is a Crossref no-match. With no retrieved source text or confirmed bibliographic record, neither existence nor application can be judged.

### c89 — exists SPLIT · applied ☐  (line 429)
_Ibrahim, Hafner & Rocher 2026 **[report]**_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — No match found in evidence; existence_status is no-match for this forthcoming 2026 work, though absence may reflect its future publication date rather than nonexistence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a Crossref no-match for an incomplete 2026 reference with no title, DOI, URL, or venue, which is insufficient to decisively establish or refute existence. No source text was retrieved to assess the claimed “warmth finding.”

### c90 — exists SPLIT · applied ☐  (line 430)
_Cheng et al. 2026 **[report]**_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — No match found and no claim specified; existence unconfirmed, possibly a forthcoming 2026 work.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is too underspecified and the only lookup is a Crossref no-match, so existence cannot be judged decisively. There are no substantive claims or retrieved source text to assess application.

### c109 — exists SPLIT · applied ☐  (line 562)
_Further detail from a search summary, not checked against the paper: only the newest model approached the conventional 0.8 reliability threshold on one benchmark, and one model gave the same verdict on all three runs in 61.3% of cases. **[secondary]**_
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Author explicitly marks this as a secondary search summary not checked against the paper; no match retrieved, cannot verify the specific 61.3% figure.
- gpt: exists=refuted applied=unchecked [no_basis] — No bibliographic work is identified, and the only lookup returned no Crossref match. No source text was retrieved to assess the specific reliability-threshold or 61.3% claims.

### c110 — exists SPLIT · applied ✅  · ⚑ degraded  (line 586)
_which model, on which kind of task, matters a great deal (essay 01's "jagged frontier", Dell'Acqua et al. 2023 **[report]**)_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — Dell'Acqua et al. 2023 'jagged frontier' is a real HBS working paper on GenAI/knowledge-worker productivity; no match retrieved but the work and claim are well-known.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence does not confirm the report, since Crossref returned no match. From model knowledge only, Dell'Acqua et al.'s 2023 'jagged frontier' report supports the broad claim that AI performance depends heavily on task and context.

### c114 — exists ⚠️ · applied SPLIT  (line 625)
_Paper 1 (the Resolver), Zenodo concept DOI https://doi.org/10.5281/zenodo.21210264. Source read: `pilots/llm-judge-2026-05-02/v2/preprint-draft.md` (read only). It is locked._
- **escalate:** application: unchecked vs nuance
- claude: exists=nuance applied=unchecked [evidence_text] — The Zenodo URL resolves to a real SPARRING Resolver preprint (title matches author's description), but the Crossref 'abstract' retrieved is a wrong magnetic-resolver paper; the DOI/concept exists but metadata is mismatched.
- gpt: exists=nuance applied=nuance [evidence_text] — The DOI lookup via Crossref failed and a low-similarity Crossref result was unrelated, but the DOI URL resolves to a Zenodo record with a title matching an empirical report on SPARRING's Resolver. The URL metadata supports that a Zenodo record exists, but the retrieved evidence does not verify the author's detailed governance caveats or the exact local-source description.

### c115 — exists SPLIT · applied SPLIT  (line 631)
_**A.1 People disagreeing about which answer is better (§4.4).** Ten raters judged pairs of answers blind. Agreement among them was "near zero": Krippendorff's α about −0.05 on one case and +0.01 on the other._
- **escalate:** existence: unchecked vs refuted; application: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — This is the author's own appendix (A.1) pilot data; the retrieved climate-change paper is a spurious low-similarity match, not the referenced work.
- gpt: exists=refuted applied=refuted [evidence_text] — The only retrieved item is a low-similarity article about climate-change disagreement, not the cited A.1 rater-agreement item. Its abstract does not support the claims about ten blind raters or Krippendorff's alpha values.

### c118 — exists SPLIT · applied ☐  (line 645)
_challenger (a fresh AI told to attack from a different angle): 87.1%;_
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own pilot figure (87.1%); no external source to verify, no evidence retrieved.
- gpt: exists=refuted applied=unchecked [no_basis] — The entry is only a statistic line and provides no identifiable bibliographic work; Crossref found no match. No source text was retrieved to assess the 87.1% challenger catch-rate claim.

### c119 — exists SPLIT · applied ☐  (line 646)
_self-review: 67.7%;_
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own pilot figure (67.7%); no external source to verify, no evidence retrieved.
- gpt: exists=refuted applied=unchecked [no_basis] — The entry is only a statistic line and provides no identifiable bibliographic work; Crossref found no match. No source text was retrieved to assess the 67.7% self-review catch-rate claim.

### c120 — exists SPLIT · applied ☐  (line 647)
_neutral fresh reviewer: 54.8%._
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own pilot figure (54.8%); no external source to verify, no evidence retrieved.
- gpt: exists=refuted applied=unchecked [no_basis] — The entry is only a statistic line and provides no identifiable bibliographic work; Crossref found no match. No source text was retrieved to assess the 54.8% neutral-reviewer claim or its interpretation.

### c121 — exists SPLIT · applied ☐  (line 659)
_**A.4 Arguing to agreement doesn't produce a better answer (§6.4, pre-registered).** Iterating challenger and producer until both agree left no fewer net flaws than one challenge and fix (+0.000 same-vendor, −0.125 cross-vendor). It was worse than a quiet second self-revision (+0.375 and +0.750 flaws per output). Detection removed about 87% of original flaws, but revising under adversarial pressure introduced about 2.0–2.6 new flaws per output, against about 1.25 for quiet self-revision._
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — This is an internal appendix section (A.4) of the source document itself, not an external work; the crossref near-match is unrelated. No external evidence can confirm the self-reported study figures.
- gpt: exists=refuted applied=unchecked [no_basis] — The only retrieved Crossref result is a low-similarity 2013 book titled “Arguing to Better Conclusions,” not the cited appendix-like item. No source text was retrieved for the cited claims.

### c122 — exists SPLIT · applied SPLIT  (line 667)
_**A.5 Grounded critique (§7; seeded-defect pilot, pre-registered, grounding machine-checked).** Share of concerns backed by a checkable source:_
- **escalate:** existence: unchecked vs refuted; application: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — This is an internal appendix section (A.5) of the source document; the retrieved crossref 'grounded theory' review is unrelated and does not bear on the seeded-defect pilot claims.
- gpt: exists=refuted applied=refuted [evidence_text] — The retrieved item is an unrelated review article about grounded theory texts, not a work titled “A.5 Grounded critique.” Its abstract does not support the cited seeded-defect pilot claims or percentages.

### c123 — exists SPLIT · applied ☐  (line 669)
_full method: 96.3%;_
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Internal self-reported figure from the source document; no external evidence retrieved and none applicable.
- gpt: exists=refuted applied=unchecked [no_basis] — The entry is only a fragmentary statistic with no bibliographic metadata, and Crossref returned no match. No source text was retrieved to assess the 96.3% claim.

### c124 — exists SPLIT · applied ☐  (line 670)
_tough realistic skeptic: 83.3%;_
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Internal self-reported figure; no external evidence retrieved and none applicable.
- gpt: exists=refuted applied=unchecked [no_basis] — The entry is only a fragmentary statistic with no bibliographic metadata, and Crossref returned no match. No source text was retrieved to assess the 83.3% claim.

### c125 — exists SPLIT · applied ☐  (line 671)
_plain single pass: 58.3%._
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — Internal self-reported figure; no external evidence retrieved and none applicable.
- gpt: exists=refuted applied=unchecked [no_basis] — The entry is only a fragmentary statistic with no bibliographic metadata, and Crossref returned no match. No source text was retrieved to assess the 58.3% claim.

### c141 — exists ✅ · applied SPLIT  (line 757)
_Ji, Z., et al. (2023). Survey of hallucination in natural language generation. ACM Computing Surveys 55(12). https://doi.org/10.1145/3571730 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to exact title/authors/venue; abstract confirms it is a comprehensive hallucination survey as cited.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI, title, authors, journal, year, volume/issue, pages, and abstract. No source-document claim was provided, so application cannot be assessed.

### c142 — exists ✅ · applied SPLIT  (line 758)
_Kadavath, S., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches exact title/authors; abstract supports LLM self-evaluation/calibration framing.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, title, authors, year context, and abstract. No source-document claim was provided, so application cannot be assessed.

### c143 — exists ✅ · applied SPLIT  (line 759)
_Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches title/authors exactly; abstract confirms thesis on why LMs hallucinate.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c145 — exists ✅ · applied SPLIT  (line 761)
_Steyvers, M., et al. (2025). What large language models know and what people think they know. Nature Machine Intelligence 7(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to exact title/authors/venue; abstract confirms calibration gap topic as cited.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI, title, authors, Nature Machine Intelligence venue, year, volume/issue, pages, and abstract. No source-document claim was provided, so application cannot be assessed.

### c146 — exists ✅ · applied SPLIT  (line 762)
_Tian, K., et al. (2023). Just ask for calibration. EMNLP. arXiv:2305.14975. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches (full title truncated in cite); abstract confirms verbalized confidence/calibration from RLHF LMs.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c147 — exists ✅ · applied SPLIT  (line 763)
_Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. Scientific Reports 13. https://doi.org/10.1038/s41598-023-41032-5 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to exact title/authors; abstract confirms ChatGPT fabricated citation study.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI, title, authors, Scientific Reports venue, year, volume/issue, and abstract. No source-document claim was provided, so application cannot be assessed.

### c148 — exists ✅ · applied SPLIT  (line 764)
_Xiong, M., et al. (2024). Can LLMs express their uncertainty? ICLR. arXiv:2306.13063. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches (full title truncated in cite); abstract confirms confidence elicitation in LLMs.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c149 — exists ✅ · applied SPLIT  (line 767)
_Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. Nature 630, 625–630. https://doi.org/10.1038/s41586-024-07421-0 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to exact Nature paper title/authors/pages; abstract confirms semantic entropy hallucination detection.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI, title, authors, Nature venue, year, volume/issue, pages, and abstract. No source-document claim was provided, so application cannot be assessed.

### c150 — exists ✅ · applied SPLIT  (line 768)
_Kim, E., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors in large language models. ICML. arXiv:2506.07962. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches exact title/authors; abstract confirms correlated errors across LLMs.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c151 — exists ✅ · applied SPLIT  (line 769)
_Li, J., Zhang, Q., Yu, Y., Fu, Q., & Ye, D. (2024). More agents is all you need. TMLR. arXiv:2402.05120. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches exact title/authors; abstract confirms sampling-and-voting agent scaling.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c152 — exists ✅ · applied SPLIT  (line 770)
_Manakul, P., Liusie, A., & Gales, M. J. F. (2023). SelfCheckGPT. EMNLP. arXiv:2303.08896. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches (full title in evidence); abstract confirms SelfCheckGPT hallucination detection.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c153 — exists ✅ · applied SPLIT  (line 771)
_Schoenegger, P., Tuminauskaite, I., Park, P. S., Bastos, R. V. S., & Tetlock, P. E. (2024). Wisdom of the silicon crowd. Science Advances 10(45). https://doi.org/10.1126/sciadv.adp1528 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to matching title/authors/venue; abstract confirms LLM ensemble wisdom-of-crowd forecasting.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI, expanded title, authors, Science Advances venue, year, volume/issue, and abstract. No source-document claim was provided, so application cannot be assessed.

### c154 — exists ✅ · applied SPLIT  (line 772)
_Wang, X., et al. (2023). Self-consistency improves chain of thought reasoning. ICLR. arXiv:2203.11171. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches exact title/authors; abstract confirms self-consistency CoT decoding.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c155 — exists ✅ · applied SPLIT  (line 775)
_Basil, S., Shapiro, I., Shapiro, D., Mollick, E., Mollick, L., & Meincke, L. (2025). Prompting Science Report 4: Expert personas don't improve factual accuracy. arXiv:2512.05858. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches title/authors; abstract confirms expert personas don't improve factual accuracy.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c156 — exists ✅ · applied SPLIT  (line 776)
_Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2023). Are you sure? The FlipFlop experiment. arXiv:2311.08596. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches (full title in evidence); abstract confirms FlipFlop sycophancy experiment.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c157 — exists ✅ · applied SPLIT  (line 777)
_Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically ordered prompts. ACL. arXiv:2104.08786. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches (full title in evidence); abstract confirms prompt order sensitivity.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c158 — exists ✅ · applied SPLIT  (line 778)
_Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025c). Prompting Science Report 3: I'll pay you or I'll kill you. arXiv:2508.00614. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches title/authors; abstract confirms tipping/threatening prompting report.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c159 — exists ✅ · applied SPLIT  (line 779)
_Mizrahi, M., et al. (2024). State of what art? A call for multi-prompt LLM evaluation. TACL. arXiv:2401.00595. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches exact title/authors; abstract confirms multi-prompt LLM evaluation call.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c160 — exists ✅ · applied SPLIT  (line 780)
_Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2024). Quantifying language models' sensitivity to spurious features in prompt design. ICLR. arXiv:2310.11324. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches (full title in evidence); abstract confirms prompt formatting sensitivity study.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches the identifier, expanded title, authors, and abstract. No source-document claim was provided, so application cannot be assessed.

### c161 — exists ✅ · applied SPLIT  (line 781)
_Sharma, M., et al. (2023). Towards understanding sycophancy in language models. arXiv:2310.13548. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms title, authors, and abstract on sycophancy driven by human feedback.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID, title, authors, and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c162 — exists ⚠️ · applied SPLIT  (line 782)
_Zheng, M., Pei, J., Logeswaran, L., Lee, M., & Jurgens, D. (2024). Personas in system prompts do not improve performances. Findings of EMNLP, 15126–15154. https://doi.org/10.18653/v1/2024.findings-emnlp.888 [abstract; report] ★_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref and ACL Anthology confirm the EMNLP Findings paper; title shortened but matches full title about personas not improving LLM performance.
- gpt: exists=nuance applied=unchecked [no_basis] — The DOI, authors, venue, year, and pages match, but the cited title is a shortened/incomplete form of the full ACL title. No claim was supplied for this citation, so application cannot be assessed.

### c163 — exists ✅ · applied SPLIT  (line 785)
_Cohen, R., Hamri, M., Geva, M., & Globerson, A. (2023). LM vs LM: Detecting factual errors via cross examination. arXiv:2305.13281. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms title, authors, and abstract on cross-examination for factual error detection.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID, title, authors, and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c164 — exists ✅ · applied SPLIT  (line 786)
_Dhuliawala, S., et al. (2023). Chain-of-verification reduces hallucination. arXiv:2309.11495. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms Chain-of-Verification paper reducing hallucination.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID and authors; the title is the same except for the fuller ending “in Large Language Models.” No claim was supplied for this citation, so application cannot be assessed.

### c165 — exists ⚠️ · applied SPLIT  (line 787)
_Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2023). Multiagent debate. arXiv:2305.14325. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms multiagent debate paper; shortened title but authors and abstract match.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv ID and authors match, but the cited title is a substantially shortened version of the full title. No claim was supplied for this citation, so application cannot be assessed.

### c166 — exists ⚠️ · applied SPLIT  (line 788)
_Gou, Z., et al. (2024). CRITIC. ICLR. arXiv:2305.11738. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms CRITIC paper on tool-interactive self-correction.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv work exists and matches the CRITIC paper, but the citation gives only an abbreviated title and the ICLR venue is not confirmed by the retrieved metadata. No claim was supplied for this citation, so application cannot be assessed.

### c167 — exists ⚠️ · applied SPLIT  (line 789)
_Huang, J., et al. (2024). Large language models cannot self-correct reasoning yet. ICLR. arXiv:2310.01798. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms title, authors, and abstract on LLMs' inability to self-correct reasoning.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv ID, authors, title, and abstract match, but the ICLR venue is not confirmed by the retrieved metadata. No claim was supplied for this citation, so application cannot be assessed.

### c168 — exists ✅ · applied SPLIT  (line 790)
_Kamoi, R., Zhang, Y., Zhang, N., Han, J., & Zhang, R. (2024). When can LLMs actually correct their own mistakes? TACL 12, 1417–1440. https://doi.org/10.1162/tacl_a_00713 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the TACL survey on when LLMs can correct their own mistakes; volume and pages match.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI lookup matches the cited authors, journal, year, volume, pages, title, and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c169 — exists ⚠️ · applied SPLIT  (line 791)
_Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. NeurIPS. arXiv:2005.11401. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms the canonical RAG paper, title, authors, and abstract.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv ID, title, authors, and abstract match, but the NeurIPS venue is not confirmed by the retrieved metadata. No claim was supplied for this citation, so application cannot be assessed.

### c170 — exists ✅ · applied SPLIT  (line 792)
_Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., & Ho, D. E. (2025). Hallucination-free? Journal of Empirical Legal Studies 22(2), 216–242. https://doi.org/10.1111/jels.12413 [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the JELS article on hallucinations in legal AI tools; volume, issue, pages match.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI lookup matches the cited journal article, including authors, title, journal, year, volume/issue, pages, and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c171 — exists ✅ · applied SPLIT  (line 793)
_Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025b). Prompting Science Report 2: The decreasing value of chain of thought. arXiv:2506.07142. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms Prompting Science Report 2 on decreasing value of chain of thought.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID, authors, year, and core title, with only a slightly fuller title in metadata. No claim was supplied for this citation, so application cannot be assessed.

### c172 — exists ✅ · applied SPLIT  (line 794)
_Shuster, K., Poff, S., Chen, M., Kiela, D., & Weston, J. (2021). Retrieval augmentation reduces hallucination in conversation. arXiv:2104.07567. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms title, authors, and abstract on retrieval reducing hallucination in conversation.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID, title, authors, and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c173 — exists ✅ · applied SPLIT  (line 795)
_Smit, A., Duckworth, P., Grinsztajn, N., Barrett, T. D., & Pretorius, A. (2023). Should we be going MAD? arXiv:2311.17371. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms the MAD multi-agent debate paper; shortened title but authors and abstract match.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID and authors; the cited title is the leading portion of the fuller title. No claim was supplied for this citation, so application cannot be assessed.

### c174 — exists ✅ · applied SPLIT  (line 796)
_Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. arXiv:2201.11903. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms the canonical chain-of-thought prompting paper.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID, title, authors, and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c175 — exists ⚠️ · applied SPLIT  (line 799)
_Bavaresco, A., et al. (2025). LLMs instead of human judges? ACL. arXiv:2406.18403. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms the LLMs-as-judges study; shortened title but authors and abstract match.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv work exists and matches the cited authors and title, but the 2025 ACL venue is not confirmed by the retrieved metadata. No claim was supplied for this citation, so application cannot be assessed.

### c176 — exists ⚠️ · applied SPLIT  (line 800)
_Haldar, R., & Hockenmaier, J. (2025). Rating roulette. Findings of EMNLP. arXiv:2510.27106. [abstract; model-level figures secondary]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms Rating Roulette on LLM judge self-inconsistency; consistent with author note about model-level figures.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv lookup matches the cited work, but the title is abbreviated and the Findings of EMNLP venue is not confirmed by the retrieved metadata. No claim was supplied for this citation, so application cannot be assessed.

### c177 — exists ✅ · applied SPLIT  (line 801)
_Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM evaluators recognize and favor their own generations. arXiv:2404.13076. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms title, authors, and abstract on LLM evaluators favoring their own generations.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv lookup matches the cited ID, title, authors, and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c178 — exists ⚠️ · applied SPLIT  (line 802)
_Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. NeurIPS Datasets and Benchmarks. arXiv:2306.05685. [abstract]_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms the canonical MT-Bench/Chatbot Arena LLM-as-judge paper.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv ID, authors, title, and abstract match, but the NeurIPS Datasets and Benchmarks venue is not confirmed by the retrieved metadata. No claim was supplied for this citation, so application cannot be assessed.

### c179 — exists ⚠️ · applied SPLIT  (line 805)
_Bommasani, R., et al. (2022). Picking on the same person. NeurIPS. arXiv:2211.13972. [report] ★_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — ArXiv match confirms the 'Picking on the Same Person' algorithmic monoculture paper; marked cross-reference only.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv work exists and matches the cited authors and core title, but the title is shortened and the NeurIPS venue is not confirmed by the retrieved metadata. No claim was supplied for this citation, so application cannot be assessed.

### c180 — exists ✅ · applied SPLIT  (line 806)
_Cheng, M., et al. (2026). Science. https://doi.org/10.1126/science.aec8352 [report] ★_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Crossref confirms the Science article by Cheng et al. on sycophantic AI; abstract matches the carried cross-reference.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI lookup confirms a Science article by Cheng et al. in 2026 and provides the full title and abstract. No claim was supplied for this citation, so application cannot be assessed.

### c181 — exists SPLIT · applied ☐  (line 807)
_Dell'Acqua, F., et al. (2023). Navigating the jagged technological frontier. HBS Working Paper 24-013. [report] ★_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — The retrieved match is a different work by Westover (2026) in Human Capital Leadership Review, not the real Dell'Acqua et al. (2023) HBS Working Paper 24-013; the abstract shown is from the wrong article. No claims are attached and no cross-reference evidence supports application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved Crossref record is a different 2026 article by Jonathan H. Westover, not the cited 2023 Dell'Acqua et al. HBS Working Paper 24-013, so the cited work is not confirmed by the supplied evidence. No substantive claim was provided to assess application.

## ⚠️ AGREE-problem (82)

_Public copy: two entries (c126, c184) are withheld here. Both point to an unpublished paper; the counts above include them._

### c01 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 32)
_Holtzman et al. 2020_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref did not match, but Holtzman et al. 2020 (The Curious Case of Neural Text Degeneration) is a real paper; the sampling claim is well-established basic LLM behavior.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The retrieved Crossref lookup found no match, which is not enough by itself to disprove existence from this incomplete reference. From model knowledge, Holtzman et al. 2020 is associated with neural text generation/sampling, but the cited claim is a generalization rather than a precise quoted finding.

### c02 — exists ☐ · applied ☐  · ⚑ degraded  (line 33)
_Atil et al. 2024_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No evidence retrieved; the specific 15% accuracy variation at temperature 0 figure cannot be verified from available data.
- gpt: exists=unchecked applied=unchecked [no_basis] — Only a failed Crossref match was retrieved, and the reference is too incomplete to verify or refute existence. No source text or sufficiently reliable model-knowledge basis is available to check the specific 15% variation claim.

### c03 — exists ☐ · applied ☐  (line 34)
_He 2025_
- claude: exists=unchecked applied=unchecked [no_basis] — No match found and no source text; cannot verify the 1,000-run/80-completions claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — Only a failed Crossref match was retrieved, and the reference lacks title or venue details. There is no retrieved source text supporting the specific 1,000-run/80-completion claim.

### c04 — exists ☐ · applied ✅  · ⚑ degraded  (line 37)
_Farquhar et al. 2024_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Farquhar et al. 2024 (semantic entropy, Nature) is a real paper whose core finding is that answer scatter indicates confabulation, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The Crossref no-match does not decisively establish nonexistence for this incomplete citation. From model knowledge, Farquhar et al. 2024 on semantic entropy supports the idea that dispersed semantically different answers indicate higher hallucination/confabulation risk.

### c05 — exists ☐ · applied ✅  · ⚑ degraded  (line 37)
_Manakul et al. 2023_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Manakul et al. 2023 (SelfCheckGPT) is a real paper using sampling consistency to detect hallucination, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved evidence is a failed Crossref lookup, insufficient to judge existence. From model knowledge, Manakul et al. 2023 SelfCheckGPT uses inconsistency across sampled answers as a signal of hallucination, supporting the claim.

### c06 — exists ☐ · applied ✅  · ⚑ degraded  (line 39)
_Farquhar et al._
- claude: exists=unchecked applied=verified [model_knowledge_only] — Farquhar et al. 2024 is real; it explicitly addresses confabulations (a subset of hallucinations), consistent with the limitation claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The failed Crossref lookup is insufficient to verify or refute the incomplete citation’s existence. From model knowledge, Farquhar et al.’s semantic-entropy method is aimed at detecting confabulations/uncertainty-related hallucinations, so saying it detects only a subset is supported.

### c07 — exists ☐ · applied ☐  (line 41)
_Kim et al. 2025_
- claude: exists=unchecked applied=unchecked [no_basis] — No match and common author name; the specific 60% shared-error figure cannot be verified.
- gpt: exists=unchecked applied=unchecked [no_basis] — Only a failed Crossref lookup was retrieved, so existence cannot be judged from the evidence. No source text or reliable basis is available to verify the specific 60% shared-wrong-answer figure.

### c08 — exists ☐ · applied ☐  (line 42)
_A consistent answer can be consistently wrong. **[ours, from those two sources]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] and is_citation=false; this is the authors' own interpretation, intentionally not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and as the authors’ own interpretation. Per instruction, both axes are left unchecked.

### c09 — exists ☐ · applied ✅  · ⚑ degraded  (line 44)
_Ulery et al. 2012_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Ulery et al. 2012 (PNAS, fingerprint examiner repeatability) is a real study reporting roughly 90% intra-examiner repeatability, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The failed Crossref lookup alone is not decisive for existence. From model knowledge, Ulery et al. 2012 studied repeatability/reproducibility of latent fingerprint examiner decisions and reported roughly 89–90% repeatability on retest, matching the claim.

### c10 — exists ☐ · applied ✅  · ⚑ degraded  (line 45)
_Elmore et al. 1994_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Elmore et al. 1994 (NEJM, variability in radiologists' mammogram interpretations) is a real study reporting modest interobserver agreement, consistent with the kappa figure.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Only a Crossref no-match was retrieved, which is insufficient to refute existence. From model knowledge, Elmore et al. 1994 reported variability in mammogram interpretation and a weighted kappa around 0.47, supporting the claim.

### c11 — exists ☐ · applied ✅  · ⚑ degraded  (line 47)
_Elmore et al. 2015_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Elmore et al. 2015 (JAMA, breast biopsy diagnostic concordance) is a real study; roughly 75% overall concordance with lower rates for atypia matches the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref lookup found no match, but that is not decisive for this incomplete reference. From model knowledge, Elmore et al. 2015 on breast biopsy pathology reported about 75% overall concordance and much lower concordance, around 48%, for atypia, supporting the claim.

### c12 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 48)
_Regier et al. 2013_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Regier et al. 2013 (DSM-5 field trials, Am J Psychiatry) is a real paper reporting kappa values, with some diagnoses in low/unacceptable ranges, consistent with the claim.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Only a failed Crossref lookup was retrieved, so existence cannot be judged from evidence. From model knowledge, Regier et al. 2013 reports DSM-5 field trial reliability with some diagnoses in very low agreement ranges, but the exact count and threshold wording require source text to confirm precisely.

### c13 — exists ✅ · applied ✅  · ⚑ degraded  (line 49)
_Kahneman, Sibony & Sunstein 2021_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Noise (Kahneman, Sibony, Sunstein, 2021); the book famously features an insurance company noise audit.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library matches Noise by Daniel Kahneman, Olivier Sibony, and Cass R. Sunstein, published in 2021. From model knowledge, the book discusses noise audits including an insurance-industry example, supporting the claim.

### c14 — exists ☐ · applied ✅  · ⚑ degraded  (line 52)
_Kadavath et al. 2022_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Kadavath et al. 2022 (Language Models (Mostly) Know What They Know) is a real paper showing larger models are reasonably calibrated on some formats.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The failed Crossref lookup is insufficient to judge existence of the incomplete reference. From model knowledge, Kadavath et al. 2022, “Language Models Mostly Know What They Know,” supports that larger models can be reasonably calibrated in some elicitation formats.

### c15 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 53)
_Xiong et al. 2024_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Xiong et al. 2024 (Can LLMs Express Their Uncertainty?) is a real paper finding verbalized confidence tends to be overconfident, matching the claim.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Only a failed Crossref lookup was retrieved, so existence remains unchecked. From model knowledge, Xiong et al. 2024 is consistent with work finding verbalized LLM confidence can be overconfident, though the exact cited framing needs source text for full verification.

### c16 — exists ☐ · applied ☐  · ⚑ degraded  (line 54)
_Steyvers et al. 2025_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No match retrieved; Steyvers has relevant work on LLM calibration/user trust but the specific claim cannot be confirmed from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a Crossref no-match, insufficient to verify or refute existence. No source text or reliable model-knowledge basis is available to confirm the specific claim about longer explanations raising confidence without accuracy.

### c17 — exists ☐ · applied ✅  · ⚑ degraded  (line 56)
_Kalai et al. 2025_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Kalai et al. 2025 (OpenAI, Why Language Models Hallucinate) is a real work arguing training/evaluation reward guessing over abstaining, matching the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The failed Crossref lookup does not decisively address existence for this incomplete citation. From model knowledge, Kalai et al. 2025 argues that evaluation/training incentives can reward guessing over abstention, supporting the claim.

### c18 — exists ☐ · applied ✅  · ⚑ degraded  (line 59)
_Sclar et al. 2024_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Sclar et al. 2024 (prompt format sensitivity, ICLR) is a real paper showing large accuracy swings from formatting changes, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Only a Crossref no-match was retrieved, which is not enough to judge existence. From model knowledge, Sclar et al. 2024 reports large accuracy swings from semantically equivalent prompt-format changes, including very large point differences, supporting the claim.

### c19 — exists ☐ · applied ☐  · ⚑ degraded  (line 60)
_Zheng et al. 2024_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No match and common author name; the persona-ineffectiveness claim is plausible but unverifiable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — Only a failed Crossref lookup was retrieved, and the reference is too incomplete to verify existence. No source text or sufficiently reliable model-knowledge basis is available to confirm that expert personas did not improve factual accuracy.

### c20 — exists ☐ · applied ☐  (line 60)
_Basil et al. 2025_
- claude: exists=unchecked applied=unchecked [no_basis] — No match found and no source text; the persona claim cannot be verified for this reference.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved evidence is only a Crossref no-match, insufficient to judge existence. No source text or reliable basis is available to verify the claim about expert personas and factual-question accuracy.

### c21 — exists ☐ · applied ☐  · ⚑ degraded  (line 61)
_Meincke et al. 2025a, 2025c_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — Crossref returned no match and no metadata, but bare author-year with no title is hard to resolve; Meincke et al. 2025 work on LLM prompting manipulations (politeness/tips/threats) is plausible and consistent with the claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is too underspecified and Crossref returned no match, which is not decisive evidence of nonexistence. No source text was retrieved to assess the claim about politeness, tips, and threats.

### c22 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 63)
_Laban et al. 2023_
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No evidence retrieved; Laban et al. 2023 likely refers to conversational LLM reliability work, and the 'Are you sure?' answer-flipping phenomenon is documented in that line of research though the exact 46% figure cannot be verified.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match for a very sparse reference, so existence is not confirmed from the retrieved evidence. From model knowledge, Laban et al. 2023 is consistent with the reported 'Are you sure?' finding, including frequent answer changes and reduced accuracy.

### c25 — exists ☐ · applied ✅  · ⚑ degraded  (line 68)
_Magesh et al. 2025_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Magesh et al. 2025 is a known Stanford study on legal AI tools reporting hallucination rates in that 17–33% range, consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match and no other metadata was retrieved, so existence is unchecked. From model knowledge, Magesh et al. reported hallucination/wrong or unsupported answer rates around 17–33% for commercial legal AI research tools.

### c26 — exists ☐ · applied ✅  · ⚑ degraded  (line 69)
_Gou et al. 2024_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Gou et al. 2024 is plausibly CRITIC, a known tool-based self-correction framework, consistent with the 'tool-based checking' claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The sparse Gou et al. 2024 reference was not confirmed by the retrieved evidence. From model knowledge, Gou et al. is associated with tool-interactive critique/checking methods, so it plausibly supports 'tool-based checking.'

### c27 — exists ☐ · applied ✅  · ⚑ degraded  (line 70)
_Wang et al. 2023_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Wang et al. 2023 likely refers to Self-Consistency (voting across samples), which directly supports the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref did not match the underspecified Wang et al. 2023 reference, so existence is unchecked. From model knowledge, Wang et al. 2023 on self-consistency supports voting across multiple sampled reasoning paths.

### c29 — exists ☐ · applied ✅  · ⚑ degraded  (line 73)
_Huang et al. 2024_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Huang et al. 2024 'Large Language Models Cannot Self-Correct Reasoning Yet' supports the claim that self-rechecking without new information often fails.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence is only a Crossref no-match, so existence is not verified. From model knowledge, Huang et al. 2024 on LLM self-correction supports the claim that self-rechecking without new information often fails to improve and can worsen performance.

### c30 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 74)
_Kamoi et al. 2024_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Kamoi et al. 2024 is a known survey on LLM self-correction concluding limited ability to self-correct, consistent with the claim.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — No retrieved metadata confirms Kamoi et al. 2024. From model knowledge, Kamoi et al. discusses limits of LLM self-correction/self-checking, broadly supporting the claim, though the exact wording may generalize across multiple findings.

### c31 — exists ☐ · applied ✅  · ⚑ degraded  (line 74)
_Du et al. 2023_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Du et al. 2023 is the known multi-agent debate paper reporting improvements, supporting the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence does not confirm the Du et al. 2023 citation. From model knowledge, Du et al. 2023 on multi-agent debate reports improvements on some tasks, supporting the claim.

### c33 — exists ☐ · applied ☐  (line 82)
_**[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours]: authors' own synthesis, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as [ours] and deliberately uncited, not an external citation. Both existence and application are therefore unchecked.

### c34 — exists ☐ · applied ✅  · ⚑ degraded  (line 83)
_Zheng et al. 2023_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Zheng et al. 2023 is the well-known MT-Bench/LLM-as-judge paper reporting >80% agreement with human preferences, matching human-human agreement, supporting the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence does not confirm the Zheng et al. 2023 work. From model knowledge, Zheng et al. 2023 on LLM-as-a-judge reports GPT-4 judge agreement with humans above 80% and comparable to human agreement.

### c35 — exists ☐ · applied ✅  · ⚑ degraded  (line 85)
_Panickssery et al. 2024_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval match, but Panickssery et al. 2024 is a known paper on LLM self-preference bias in evaluation, supporting the claim that AI judges favour their own outputs.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Crossref no-match does not verify the sparse Panickssery et al. 2024 citation. From model knowledge, Panickssery et al. reports self-preference or favoritism by AI judges toward their own outputs.

### c36 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 86)
_Bavaresco et al. 2025_
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No retrieval match; Bavaresco et al. 2025 ('LLMs instead of Human Judges') surveys judge reliability varying across tasks, broadly consistent with the claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence provides no confirmation beyond a Crossref no-match. From model knowledge, Bavaresco et al. studies LLM-as-judge evaluation and reports substantial task-dependent variation.

### c37 — exists ☐ · applied ☐  · ⚑ degraded  (line 86)
_Haldar & Hockenmaier 2025_
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No retrieval match and no details; the claim about judge run-to-run inconsistency is plausible but cannot be attributed to this specific work with confidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The retrieved evidence does not confirm a Haldar & Hockenmaier 2025 work. No source text was retrieved, so the claim about run-to-run AI judge variability cannot be assessed here.

### c38 — exists ✅ · applied ⚠️  (line 93)
_Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020). The curious case of neural text degeneration. _ICLR 2020_. arXiv:1904.09751. https://arxiv.org/abs/1904.09751 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms the paper and authors; the abstract's emphasis that sampling/decoding strategy dramatically affects generation supports the 'sampling is the design' framing.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv ID and URL resolve to Holtzman et al., 'The Curious Case of Neural Text Degeneration,' matching the citation. The abstract supports that decoding and nucleus sampling are central design choices for fluent generation, though 'Sampling is the design' is a compressed interpretation rather than the paper's exact claim.

### c40 — exists ☐ · applied ☐  (line 100)
_Bearing: variety is not a malfunction. It is how fluent generation was made to work. Each answer is one sample. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours]: authors' interpretation, intentionally uncited.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked [ours] and deliberately uncited as the authors' interpretation. Both axes are therefore unchecked.

### c43 — exists ☐ · applied ☐  (line 111)
_Preprint; peer-review status not confirmed._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an editorial note about peer-review status, not a verifiable citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation and contains only an author note about peer-review status. Both axes are therefore unchecked.

### c44 — exists ✅ · applied ☐  (line 113)
_Ouyang, S., Zhang, J. M., Harman, M., & Wang, M. (2023). An empirical study of the non-determinism of ChatGPT in code generation. arXiv:2308.02828. https://arxiv.org/abs/2308.02828 **[abstract]**_
- claude: exists=verified applied=unchecked [no_basis] — arXiv ID, title, and authors match exactly; no specific claim is attached to this citation record.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record and URL match the cited title, authors, year, and arXiv ID. No specific claims are listed for this citation, so application cannot be assessed.

### c46 — exists ☐ · applied ☐  (line 119)
_Venue after arXiv not confirmed here._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an editorial note on venue, not a verifiable citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation and is only an author note about venue uncertainty. Both axes are therefore unchecked.

### c50 — exists ☐ · applied ☐  (line 131)
_Bearing: a sound, specific explanation of the "even temperature 0 varies" point. It is a company research blog, not peer-reviewed. Its demonstration concerns one open model on one serving stack. Whether commercial assistants behave the same way is not shown._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an editorial 'bearing' note, not a verifiable citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation and contains only an author note about limitations of the blog demonstration. Both axes are therefore unchecked.

### c52 — exists ☐ · applied ☐  · ⚑ degraded  (line 138)
_GPT-4o and GPT-4o-mini, 198 graduate-level multiple-choice questions (GPQA Diamond), each asked 100 times per prompt at temperature 0. Many questions were "not answered correctly consistently". Judged by the strictest standard (right on all 100 attempts), both models scored only about 5 percentage points above the 25% that random guessing would give, a difference that was not statistically significant. Judged by majority vote, GPT-4o scored about 18 points higher than by the strict standard._
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — No evidence retrieved for this record; the detailed GPQA/GPT-4o figures appear in the Meincke et al. report body but cannot be confirmed from retrieved text.
- gpt: exists=unchecked applied=unchecked [no_basis] — No bibliographic reference or retrieved source is provided for this entry, so existence cannot be checked. The detailed GPQA and 100-run claims cannot be judged from the provided evidence.

### c53 — exists ☐ · applied ☐  (line 144)
_Bearing: "how good is this model?" depends on whether you need it right *every* time or *most* of the time. A single run hides that. An unreviewed short report from a university lab._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an editorial 'bearing' note, not a verifiable citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is marked as not a citation and contains only an interpretive author note. Both axes are therefore unchecked.

### c54 — exists ☐ · applied ☐  (line 147)
_**1.6 Not a lookup.** **[ours]** No source above says it this way, but together they support it. The model does not retrieve a stored answer. It generates one, word by word, from probabilities that the question and its wording shape. Whether a fact comes out the same each time depends on how sharply the model's probabilities favour it. Q4 turns that into a usable signal._
- claude: exists=unchecked applied=unchecked [no_basis] — Explicitly marked [ours] and deliberately uncited; the authors' own synthesis, not a citation to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — This entry is deliberately uncited and explicitly marked as the authors' own synthesis. Both axes are therefore unchecked.

### c55 — exists ✅ · applied ⚠️  (line 160)
_Ulery, B. T., Hicklin, R. A., Buscaglia, J., & Roberts, M. A. (2012). Repeatability and reproducibility of decisions by latent fingerprint examiners. _PLoS ONE_, 7(3), e32800. https://doi.org/10.1371/journal.pone.0032800 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI matches exactly; abstract confirms 72 examiners retested on 25 pairs after ~7 months, 89.1%/90.1% repeatability, difficulty effect, no false positives repeated, 30% false negatives repeated.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI and metadata verify the PLoS ONE article, and the abstract directly supports the sample, retest interval, repeatability percentages, difficulty effect, and false-positive/false-negative details. The broader comparison to LLM variation is an author interpretation rather than a claim made by the fingerprint study itself.

### c56 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 171)
_Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). _Noise: A flaw in human judgment._ Little, Brown Spark. [secondary; report]_
- claude: exists=verified applied=nuance [model_knowledge_only] — Book existence confirmed by Open Library; no text retrieved to check the level/occasion noise distinction or the 55% insurance figure, though these are well-known claims in Noise (author notes figures are secondary).
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library verifies the existence of the 2021 book Noise by Kahneman, Sibony, and Sunstein, though the retrieved metadata does not confirm the publisher. The claims about level/occasion noise and the insurance underwriting audit are consistent with the book, but application is assessed from model knowledge only.

### c60 — exists ✅ · applied ⚠️  (line 206)
_Cortes, C., & Lawrence, N. D. (2021). Inconsistency in conference peer review: Revisiting the 2014 NeurIPS experiment. arXiv:2109.09774. https://arxiv.org/abs/2109.09774 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID, title, and authors match; abstract confirms 50% of variation in reviewer scores was subjective and that review was good at identifying poor papers but poor at identifying good ones.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record and URL verify the cited preprint. The abstract directly supports the 50% subjective-variation claim and the conclusion that review was good at identifying poor papers but poor at identifying good ones; the comparison to AI judges is an extrapolative bearing supplied by the citing author.

### c62 — exists ☐ · applied ☐  (line 219)
_**What the comparison can and cannot say.** **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours], authors' own synthesis; is_citation=false, so both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the authors' own synthesis and is_citation=false, so it is intentionally not a cited work. Both axes are therefore unchecked.

### c63 — exists ☐ · applied ☐  (line 224)
_No head-to-head study was found (search 2026-10-19)._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited note that no head-to-head study was found; both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and reports a search result rather than a bibliographic citation. Both axes are therefore unchecked.

### c71 — exists ✅ · applied ☐  · ⚑ degraded  (line 298)
_**3.8** Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Vaughan, J. W. (2024). "I'm not sure, but...": Examining the impact of large language models' uncertainty expression on user reliance and trust. _FAccT 2024_. https://doi.org/10.1145/3630106.3658941 **[abstract; report]**_
- claude: exists=verified applied=unchecked [model_knowledge_only] — DOI and title match confirm existence, but no abstract retrieved to verify the N=404, pre-registered, medical, overreliance-reduction specifics.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, FAccT 2024 venue, and pages. No abstract or source text was retrieved, so the specific claims about preregistration, N=404, medical questions, and effects on reliance/accuracy cannot be assessed from the provided evidence.

### c72 — exists ✅ · applied ⚠️  (line 305)
_Moore & Healy (2008), "The trouble with overconfidence", _Psychological Review_, 115(2), 502–517, https://doi.org/10.1037/0033-295X.115.2.502 **[record]**, is a standard review. Its contents were not checked here; read before citing anything beyond "overconfidence in people is well documented". **[ours]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and metadata match. Abstract documents multiple forms of overconfidence, supporting the modest claim that overconfidence in people is well documented.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and Europe PMC match the DOI, title, authors, journal, volume, issue, pages, and PMID-linked abstract. The abstract supports that human overconfidence is well documented, but it also emphasizes three distinct forms and task-dependent reversals, so the broad claim needs that caveat.

### c75 — exists ✅ · applied ⚠️  (line 328)
_**4.3** Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. _Nature_, 630, 625–630. https://doi.org/10.1038/s41586-024-07421-0 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and metadata match. Abstract contains the quoted phrases about meaning-level uncertainty and confabulations, supporting the 'scatter is the signal' framing and scope limit.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the resolved Nature URL confirm the cited article and metadata. The abstract supports the semantic-entropy, meaning-level uncertainty, confabulation-subset, and cross-task/no-task-specific-data claims; the evaluative phrase that it is the strongest source for 'the scatter is the signal' is an author characterization rather than something established by the source itself.

### c83 — exists ✅ · applied ⚠️  (line 387)
_Zheng, M., Pei, J., Logeswaran, L., Lee, M., & Jurgens, D. (2024). When "a helpful assistant" is not really helpful: Personas in system prompts do not improve performances of large language models. _Findings of EMNLP 2024_, 15126–15154. https://doi.org/10.18653/v1/2024.findings-emnlp.888 **[abstract; report]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and title/authors confirmed; the title itself states personas do not improve performance, consistent with the claim, though specific numbers (162 roles, 2,410 questions) not in retrieved snippet.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and ACL Anthology metadata confirm the cited paper, DOI, venue, authors, and pages. The retrieved text/title supports the broad no-improvement claim, but the supplied snippet does not include the detailed counts or the gender/type/domain accuracy-shift claims.

### c84 — exists ✅ · applied ⚠️  (line 395)
_Basil, S., Shapiro, I., Shapiro, D., Mollick, E., Mollick, L., & Meincke, L. (2025). Prompting Science Report 4: Playing pretend: Expert personas don't improve factual accuracy. arXiv:2512.05858. https://arxiv.org/abs/2512.05858 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms six models, GPQA Diamond and MMLU-Pro, no significant impact for in-domain experts except Gemini 2.0 Flash, degraded mismatched performance, and harmful low-knowledge personas.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited report and authors. The abstract directly supports the six-model/two-benchmark persona findings and tone caveat, while the “independent replication” framing is an interpretive bearing rather than stated verbatim.

### c85 — exists ✅ · applied ⚠️  (line 404)
_Meincke et al. (2025a), see 1.5, and Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025c). Prompting Science Report 3: I'll pay you or I'll kill you — but will you care? arXiv:2508.00614. https://arxiv.org/abs/2508.00614 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms tipping/threatening has no significant effect, per-question prompt variations can significantly affect performance, and it is hard to know in advance; the 2025a politeness finding is referenced elsewhere.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited Prompting Science Report 3. Its abstract directly supports the tipping/threatening and per-question unpredictability claims, but the politeness claim is attributed to a different earlier report and is not established by this retrieved abstract beyond a general cross-reference.

### c86 — exists ☐ · applied ☐  (line 411)
_Bearing: the honest advice on prompt tricks is "contingent". Average effects are near zero, and effects on a single question are large and unpredictable. **[ours]**_
- claude: exists=unchecked applied=unchecked [no_basis] — Authors' own bearing note, not a citation (is_citation=false).
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and appears to be the authors’ own bearing note. Per instruction, both axes are unchecked.

### c88 — exists ✅ · applied ⚠️  (line 422)
_Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., Bowman, S. R., et al. (2023). Towards understanding sycophancy in language models. arXiv:2310.13548. https://arxiv.org/abs/2310.13548 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms five assistants consistently exhibit sycophancy across four tasks and that humans/PMs prefer convincingly-written sycophantic responses over correct ones.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv metadata confirms the cited paper and author list. The abstract directly supports the five-assistant sycophancy and human/preference-model preference claims, while the final “second answer is not an independent check” bearing is an inference combined with other evidence rather than a standalone claim in this abstract.

### c96 — exists ☐ · applied ☐  (line 478)
_**6.6 Evidence on "a specific job, not an identity" is thin outside the author's work.** **[ours]** No external study was found that directly compares a specific task instruction ("check every figure against the brief") with a role label ("you are a careful analyst") on the same work. The nearest evidence is indirect: personas don't help (5.4, 5.5); external checks do (6.7–6.9). The author's own pilot (A.3) is the closest direct test, and it is small and AI-scored. Vendor prompting guides advise specific, explicit instructions; that is advice, not evidence, and was not checked here._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited authors' own observation (is_citation=false, deliberately_uncited=true).
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and is the authors’ own note about an evidence gap. Per instruction, both axes are unchecked.

### c99 — exists ✅ · applied ⚠️  (line 502)
_Gou, Z., Shao, Z., Gong, Y., Shen, Y., Yang, Y., Duan, N., & Chen, W. (2024). CRITIC: Large language models can self-correct with tool-interactive critiquing. _ICLR 2024_. arXiv:2305.11738. https://arxiv.org/abs/2305.11738 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms CRITIC uses tools (search, code interpreter) to consistently enhance performance and highlights the crucial importance of external feedback.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record matches the cited CRITIC paper. The abstract directly supports tool-interactive checking, performance enhancement, and the importance of external feedback, but not the separate “independent questions” phrasing, which is better supported by the following CoVe citation.

### c104 — exists ☐ · applied ☐  (line 529)
_**6.12 Cross-model checking.** **[ours]** The case for asking a *different* model rests on independence. Evidence that it helps comes from aggregation (4.5) and cross-examination (6.10). Evidence that it is weaker than it looks comes from correlated errors (4.6) and self-preference in judges (7.3). No external study was found that cleanly isolates "same model as checker" versus "different model as checker" on everyday tasks. The author's own grid (A.3) is one small attempt._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked [ours] and is_citation=false; author explicitly notes no external study found. Intentionally uncited.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as the author's own uncited claim rather than an external citation. Per instruction, both axes are unchecked.

### c111 — exists ☐ · applied ☐  (line 566)
_## Q8. Testing the claim with the yardstick [ours]

Our reading, to be argued, not a finding._
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own reading (Q8); is_citation=false. Not a verifiable external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and as the author's own reading. Per instruction, both axes are unchecked.

### c112 — exists ☐ · applied ☐  (line 608)
_its tone carries no information about whether it's right (3.5, 3.7)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference (3.5, 3.7) to the author's own document, not an external work; no evidence to judge.
- gpt: exists=unchecked applied=unchecked [no_basis] — The raw text gives only internal section references and no identifiable bibliographic source; Crossref found no match. No source text was retrieved to assess the claim about tone and correctness.

### c113 — exists ☐ · applied ☐  (line 609)
_it can be talked out of a correct answer more readily than the fingerprint data suggest a trained examiner changes a conclusion (5.7 against 2.1; different tasks, so loose)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference (5.7, 2.1) within the author's own document; no external work to verify.
- gpt: exists=unchecked applied=unchecked [no_basis] — The raw text gives only internal section references and no identifiable bibliographic source; Crossref found no match. No source text was retrieved to assess the comparison between being talked out of an answer and fingerprint-examiner changes.

### c116 — exists ☐ · applied ☐  (line 636)
_**A.2 AI judges versus people (§4.1).** Three AI judges from different vendors failed the pre-registered agreement gate with human raters. Only one of six criteria passed (whether an answer cites checkable artifacts, ρ 0.78). On factual accuracy the judges gave every answer the same score (6 of 7), so agreement could not be computed._
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own appendix (A.2) pilot data; the retrieved 1969 police/prosecutors item is a spurious match, not verifiable external evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup result is a low-similarity, unrelated Crossref record, so the cited A.2 item is not confirmed. No relevant source text was retrieved to assess the claims about AI judges and human raters.

### c117 — exists ☐ · applied ☐  (line 642)
_**A.3 Independent challenge versus self-review (§6.3; pilot `pilots/catch-rate-v3-2026-06-28/`, pre-registered).** 8 hard problems, 31 serious flaws confirmed by a three-AI audit panel._
- claude: exists=unchecked applied=unchecked [no_basis] — Author's own appendix (A.3) pilot data; the retrieved self-knowledge paper is a spurious match, cannot verify the pilot figures.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup result is a low-similarity, unrelated Crossref record, so the cited A.3 pilot is not confirmed. No relevant source text was retrieved to assess the hard-problem, recovery-rate, or vendor-alignment claims.

### c127 — exists ☐ · applied ☐  (line 716)
_Hill (2024), the rebuttal named in brief 6, argues opaque AI is opaque differently from humans. Does that also cover *variability*? Unread._
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved for Hill (2024); the author notes it is unread and unverified, so neither axis can be judged.
- gpt: exists=unchecked applied=unchecked [no_basis] — Only an author surname and year are given, and Crossref returned no match, which is insufficient to identify the work decisively. No source text was retrieved to assess the opacity claim.

### c128 — exists ✅ · applied ☐  (line 740)
_Atil, B., et al. (2024). Non-determinism of "deterministic" LLM settings. arXiv:2408.04667. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms the paper by ID, title and abstract. No specific claim is attached to the citation, so application is not assessable.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the cited ID, title, authors, year, and abstract. No specific claim was supplied for application assessment.

### c129 — exists ✅ · applied ☐  (line 741)
_He, H., & Thinking Machines Lab (2025). Defeating nondeterminism in LLM inference. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ [abstract: post read]_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves and matches title/author of the Thinking Machines blog post. No specific claim attached, so application not assessable.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to the cited Thinking Machines Lab post with matching title, author attribution, and date. No specific claim was supplied for application assessment.

### c130 — exists ✅ · applied ☐  (line 742)
_Holtzman, A., Buys, J., Du, L., Forbes, M., & Choi, Y. (2020). The curious case of neural text degeneration. ICLR. arXiv:1904.09751. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms title, authors and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the cited paper, authors, title, and abstract. No specific claim was supplied for application assessment.

### c131 — exists ✅ · applied ☐  (line 743)
_Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025a). Prompting Science Report 1. arXiv:2503.04818. [abstract + report text]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms the Prompting Science Report 1 by ID and authors. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the cited authors and report, with the fuller title “Prompting Science Report 1: Prompt Engineering is Complicated and Contingent.” No specific claim was supplied for application assessment.

### c132 — exists ✅ · applied ☐  (line 744)
_Ouyang, S., Zhang, J. M., Harman, M., & Wang, M. (2023). Non-determinism of ChatGPT in code generation. arXiv:2308.02828. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms title, authors and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the cited ID, authors, year, and title, with a fuller title beginning “An Empirical Study of…”. No specific claim was supplied for application assessment.

### c133 — exists ✅ · applied ☐  (line 747)
_Cortes, C., & Lawrence, N. D. (2021). Inconsistency in conference peer review. arXiv:2109.09774. [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — arXiv match confirms title, authors and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv record matches the cited paper, authors, year, and title with a subtitle. No specific claim was supplied for application assessment.

### c134 — exists ✅ · applied ☐  (line 748)
_Elmore, J. G., et al. (1994). Variability in radiologists' interpretations of mammograms. NEJM 331(22), 1493–1499. https://doi.org/10.1056/NEJM199412013312206 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the exact NEJM article with matching metadata and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC match the DOI, title, journal, year, volume, issue, and pages. No specific claim was supplied for application assessment.

### c135 — exists ✅ · applied ☐  (line 749)
_Elmore, J. G., et al. (2015). Diagnostic concordance among pathologists interpreting breast biopsy specimens. JAMA 313(11), 1122. https://doi.org/10.1001/jama.2015.1405 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the exact JAMA article with matching metadata and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC match the DOI, title, journal, year, volume, issue, and page. No specific claim was supplied for application assessment.

### c136 — exists ✅ · applied ☐  (line 750)
_Grove, W. M., et al. (2000). Clinical versus mechanical prediction. Psychological Assessment 12(1), 19–30. https://doi.org/10.1037/1040-3590.12.1.19 [report] ★_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the exact Grove et al. meta-analysis with matching metadata and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC match the DOI, title, authors, journal, year, volume, issue, and pages. No specific claim was supplied for application assessment.

### c137 — exists ✅ · applied ☐  (line 751)
_Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). Noise. Little, Brown Spark. [secondary; report] ★_
- claude: exists=verified applied=unchecked [no_basis] — Open Library confirms the book Noise (2021) by the three named authors. No specific claim attached; author flags new figures as unverified.
- gpt: exists=verified applied=unchecked [no_basis] — Open Library confirms a 2021 book titled “Noise” by Daniel Kahneman, Olivier Sibony, and Cass R. Sunstein, though the retrieved metadata does not include the publisher. No source text or specific claim was supplied for application assessment.

### c138 — exists ✅ · applied ☐  (line 752)
_Moore, D. A., & Healy, P. J. (2008). The trouble with overconfidence. Psychological Review 115(2), 502–517. https://doi.org/10.1037/0033-295X.115.2.502 [record]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the exact Psychological Review article with matching metadata and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC match the DOI, title, authors, journal, year, volume, issue, and pages. No specific claim was supplied for application assessment.

### c139 — exists ✅ · applied ☐  (line 753)
_Regier, D. A., et al. (2013). DSM-5 field trials, Part II: Test-retest reliability. Am J Psychiatry 170(1), 59–70. https://doi.org/10.1176/appi.ajp.2012.12070999 [abstract; per-diagnosis figures secondary]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the exact DSM-5 field trials Part II article with matching metadata and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC match the DOI, title, journal, year, volume, issue, and pages, with a fuller title than the abbreviated reference. No specific claim was supplied for application assessment.

### c140 — exists ✅ · applied ☐  (line 754)
_Ulery, B. T., Hicklin, R. A., Buscaglia, J., & Roberts, M. A. (2012). Repeatability and reproducibility of decisions by latent fingerprint examiners. PLoS ONE 7(3), e32800. https://doi.org/10.1371/journal.pone.0032800 [abstract]_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to the exact PLoS ONE article with matching metadata and abstract. No specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC match the DOI, title, authors, journal, year, volume, issue, and article number. No specific claim was supplied for application assessment.

### c144 — exists ✅ · applied ☐  (line 760)
_Kim, S. S. Y., Liao, Q. V., Vorvoreanu, M., Ballard, S., & Vaughan, J. W. (2024). "I'm not sure, but…". FAccT. https://doi.org/10.1145/3630106.3658941 [abstract; report] ★_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to matching FAccT paper; no abstract retrieved and no specific claim to assess application against.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI and confirms the full title, authors, FAccT conference venue, year, and pages. No source-document claim was provided, so application cannot be assessed.

### c182 — exists ✅ · applied ☐  (line 808)
_Ibrahim, L., Hafner, F. S., & Rocher, L. (2026). Nature. https://doi.org/10.1038/s41586-026-10410-0 [report] ★_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves directly to the Ibrahim, Hafner & Rocher (2026) Nature paper with matching authors and abstract. No specific claim is attached (cross-reference only), so application cannot be judged.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI directly matches a Nature article by Lujain Ibrahim, Franziska Sofia Hafner, and Luc Rocher with the supplied DOI and publication metadata. No substantive claim was provided to assess application.

### c183 — exists ✅ · applied ☐  (line 811)
_Niedner, B. (2026). Auditable adversarial review for AI-in-the-loop decisions (the Resolver paper). Zenodo. https://doi.org/10.5281/zenodo.21210264. §4.1, §4.4, §6.3, §6.4, §6.5, §7, §8.1. [ours; published]_
- claude: exists=verified applied=unchecked [no_basis] — The Zenodo record resolves and matches the Niedner SPARRING Resolver paper. The citation points to specific sections but no substantive claim text is provided to verify, and the retrieved snippet is only the landing page description.
- gpt: exists=verified applied=unchecked [evidence_text] — The Zenodo URL resolves to a record with the cited title, author Barton Niedner, publication date, and accompanying PDF/artifacts, confirming the work despite the DOI resolving to a different Zenodo record number. The retrieved snippet does not expose the cited sections’ contents, so it cannot verify the section-specific application.

## ✅ AGREE-clean (37)
### c41 — exists ✅ · applied ✅  (line 103)
_Atil, B., Aykent, S., Chittams, A., Fu, L., Passonneau, R. J., Radcliffe, E., et al. (2024). Non-determinism of "deterministic" LLM settings. arXiv:2408.04667 (earlier versions titled "LLM stability: A detailed analysis with some surprises"). https://arxiv.org/abs/2408.04667 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match exactly; abstract states none of the deterministic-configured LLMs delivers repeatable accuracy, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL match the cited title, arXiv ID, and author list, with additional coauthors consistent with 'et al.' The abstract directly states that deterministic settings varied and none of the LLMs consistently delivered repeatable accuracy or identical strings.

### c47 — exists ✅ · applied ✅  (line 121)
_He, H., & Thinking Machines Lab (2025, 10 September). Defeating nondeterminism in LLM inference. _Thinking Machines Lab: Connectionism_ (blog). https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ **[abstract: checked against the post]**_
- claude: exists=verified applied=verified [evidence_text] — The blog post resolves with matching title, author, and date; its snippet explains why temperature 0 still varies, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The URL resolves to the cited Thinking Machines Lab post with the cited title and date. The retrieved snippet explicitly discusses why temperature 0, theoretically greedy and deterministic, is still nondeterministic in practice.

### c57 — exists ✅ · applied ✅  (line 181)
_Elmore, J. G., Wells, C. K., Lee, C. H., Howard, D. H., & Feinstein, A. R. (1994). Variability in radiologists' interpretations of mammograms. _New England Journal of Medicine_, 331(22), 1493–1499. https://doi.org/10.1056/NEJM199412013312206 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; abstract confirms 10 radiologists, 150 mammograms, median 78% agreement (weighted kappa 0.47), and 11–65% workup recommendation range for women without cancer.
- gpt: exists=verified applied=verified [evidence_text] — The DOI metadata verifies the NEJM article. The abstract directly states that ten radiologists interpreted 150 mammograms, median agreement was 78% with weighted kappa 0.47, and immediate-workup recommendations for women without cancer ranged from 11% to 65%.

### c58 — exists ✅ · applied ✅  (line 188)
_Elmore, J. G., Longton, G. M., Carney, P. A., Geller, B. M., Onega, T., Tosteson, A. N. A., et al. (2015). Diagnostic concordance among pathologists interpreting breast biopsy specimens. _JAMA_, 313(11), 1122. https://doi.org/10.1001/jama.2015.1405 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; abstract confirms 115 pathologists, 6900 diagnoses, 75.3% overall concordance, 96% invasive and 48% atypia concordance, and 75% unanimous consensus-panel agreement.
- gpt: exists=verified applied=verified [evidence_text] — The DOI metadata verifies the JAMA article. The abstract directly supports the 115 pathologists, 6900 diagnoses, 75.3% overall concordance, 96% invasive carcinoma concordance, 48% atypia concordance, and 75% unanimous agreement among the consensus panel's independent diagnoses.

### c59 — exists ✅ · applied ✅  (line 195)
_Regier, D. A., Narrow, W. E., Clarke, D. E., Kraemer, H. C., Kuramoto, S. J., Kuhl, E. A., & Kupfer, D. J. (2013). DSM-5 field trials in the United States and Canada, Part II: Test-retest reliability of selected categorical diagnoses. _American Journal of Psychiatry_, 170(1), 59–70. https://doi.org/10.1176/appi.ajp.2012.12070999 [abstract]_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; abstract confirms the kappa-range distribution (5 very good, 9 good, 6 questionable, 3 unacceptable), matching the claim (23 total adult+child diagnoses with adequate samples).
- gpt: exists=verified applied=verified [evidence_text] — The DOI metadata verifies the American Journal of Psychiatry article. The abstract directly supports the test-retest design and the distribution of 23 diagnoses across very good, good, questionable, and unacceptable kappa ranges.

### c61 — exists ✅ · applied ✅  (line 214)
_Grove, W. M., et al. (2000). Clinical versus mechanical prediction: A meta-analysis. _Psychological Assessment_, 12(1), 19–30. https://doi.org/10.1037/1040-3590.12.1.19 [report]_
- claude: exists=verified applied=verified [evidence_text] — DOI and metadata match exactly. Abstract supports that mechanical prediction equals or exceeds clinical prediction, consistent with the reminder that the human side isn't a gold standard.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC match the DOI, title, journal, year, volume, issue, and pages. The abstract reports mechanical predictions were equal or superior to clinical predictions, supporting the reminder that human/clinical judgment is not a gold standard.

### c64 — exists ✅ · applied ✅  (line 236)
_Kalai, A. T., Nachum, O., Vempala, S. S., & Zhang, E. (2025). Why language models hallucinate. arXiv:2509.04664. https://arxiv.org/abs/2509.04664 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. Abstract directly states hallucinations originate as binary classification errors, persist from evaluation grading, and proposes rescoring benchmarks.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL resolve to the cited paper with matching title, authors, and arXiv ID. The abstract directly states the cited claims about binary-classification errors, guessing incentives in evaluations, test-taking optimization, and modifying benchmark scoring.

### c65 — exists ✅ · applied ✅  (line 245)
_Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., et al. (2023). Survey of hallucination in natural language generation. _ACM Computing Surveys_, 55(12), 1–38. https://doi.org/10.1145/3571730 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and metadata match. Abstract confirms it is a comprehensive survey of metrics, mitigations and tasks, supporting the vocabulary claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref matches the DOI, title, authors, journal, volume, issue, pages, and year. The abstract describes a comprehensive survey covering metrics, mitigation methods, and task-specific hallucination research, supporting its use for field vocabulary and overview.

### c66 — exists ✅ · applied ✅  (line 251)
_Walters, W. H., & Wilder, E. I. (2023). Fabrication and errors in the bibliographic citations generated by ChatGPT. _Scientific Reports_, 13. https://doi.org/10.1038/s41598-023-41032-5 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and metadata match. Abstract gives exact figures: 636 citations, 84 papers, 55%/18% fabricated, 43%/24% substantive errors.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the resolved Nature URL confirm the cited Scientific Reports article. The abstract directly gives the 84 papers/636 citations and the fabricated-citation and substantive-error percentages for GPT-3.5 and GPT-4.

### c67 — exists ✅ · applied ✅  (line 259)
_Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D., Perez, E., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221. https://arxiv.org/abs/2207.05221 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. Abstract supports all three claims about calibration, self-evaluation across samples, and P(IK) partial generalization with calibration struggles on new tasks.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the cited preprint with matching title, authors, and arXiv ID. The abstract directly supports the claims about calibration in the right format, improved P(True) after considering many samples, and P(IK) partially generalizing with calibration struggles on new tasks.

### c68 — exists ✅ · applied ✅  (line 270)
_Xiong, M., Hu, Z., Lu, X., Li, Y., Fu, J., He, J., & Hooi, B. (2024). Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. _ICLR 2024_. arXiv:2306.13063. https://arxiv.org/abs/2306.13063 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. Abstract supports overconfidence/human imitation, calibration improving with capability, consistency helping, and struggles on professional-knowledge tasks.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the cited work with matching title, authors, and arXiv ID. The abstract directly supports the claims about verbalized overconfidence, capability-related calibration improvement, consistency/multiple-response strategies, and difficulty on professional-knowledge tasks.

### c69 — exists ✅ · applied ✅  (line 278)
_Tian, K., Mitchell, E., Zhou, A., Sharma, A., Rafailov, R., Yao, H., Finn, C., & Manning, C. D. (2023). Just ask for calibration. _EMNLP 2023_. arXiv:2305.14975. https://arxiv.org/abs/2305.14975 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. Abstract confirms verbalized confidence better-calibrated than conditional probabilities on TriviaQA/SciQ/TruthfulQA, ~50% relative ECE reduction, and notes RLHF probabilities poorly calibrated.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the paper, with the cited title being a shortened form of the retrieved full title. The abstract directly supports the claims about RLHF models' verbalized confidence outperforming conditional probabilities on TriviaQA, SciQ, and TruthfulQA, often reducing ECE by about 50%, and notes prior findings of poor calibration of RLHF conditional probabilities.

### c70 — exists ✅ · applied ✅  (line 289)
_Steyvers, M., Tejeda, H., Kumar, A., Belem, C., Karny, S., Hu, X., Mayer, L. W., & Smyth, P. (2025). What large language models know and what people think they know. _Nature Machine Intelligence_, 7(2), 221–231. https://doi.org/10.1038/s42256-024-00976-7 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and metadata match. Abstract supports overestimation with default explanations, longer explanations raising confidence without accuracy gains, and adjusting explanations narrowing the gap.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the resolved Nature URL confirm the cited article and metadata. The abstract directly states that users overestimate LLM accuracy with default explanations, longer explanations increase confidence without improving accuracy, and confidence-aligned explanations narrow calibration and discrimination gaps.

### c73 — exists ✅ · applied ✅  (line 315)
_**4.1** Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., & Zhou, D. (2023). Self-consistency improves chain of thought reasoning in language models. _ICLR 2023_. arXiv:2203.11171. https://arxiv.org/abs/2203.11171 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. Abstract confirms sampling reasoning paths and taking most consistent answer, with +17.9% on GSM8K.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the cited work with matching title, authors, and arXiv ID. The abstract directly states that self-consistency samples diverse reasoning paths and selects the most consistent answer, with gains including GSM8K +17.9% and other arithmetic/commonsense benchmarks.

### c74 — exists ✅ · applied ✅  (line 321)
_**4.2** Manakul, P., Liusie, A., & Gales, M. J. F. (2023). SelfCheckGPT: Zero-resource black-box hallucination detection for generative large language models. _EMNLP 2023_. arXiv:2303.08896. https://arxiv.org/abs/2303.08896 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. The quoted sentence appears verbatim in the abstract and the black-box (no internals) framing is confirmed.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the cited SelfCheckGPT paper with matching metadata. The abstract directly contains the quoted rationale about consistent samples versus divergent hallucinated facts and says the method works for black-box models in a zero-resource fashion without external databases.

### c76 — exists ✅ · applied ✅  (line 338)
_**4.4** Li, J., Zhang, Q., Yu, Y., Fu, Q., & Ye, D. (2024). More agents is all you need. _Transactions on Machine Learning Research_. arXiv:2402.05120. https://arxiv.org/abs/2402.05120 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. Abstract confirms sampling-and-voting performance scaling with number of agents and enhancement correlated to task difficulty.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the cited work with matching title, authors, and arXiv ID. The abstract directly states that simple sampling-and-voting performance scales with the number of agents and that enhancement is correlated with task difficulty.

### c77 — exists ✅ · applied ✅  (line 344)
_**4.5 Pooling across models, compared with a human crowd.** Schoenegger, P., Tuminauskaite, I., Park, P. S., Bastos, R. V. S., & Tetlock, P. E. (2024). Wisdom of the silicon crowd: LLM ensemble prediction capabilities rival human crowd accuracy. _Science Advances_, 10(45). https://doi.org/10.1126/sciadv.adp1528 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI and metadata match. Abstract confirms 12 LLMs, 31 questions, 925 forecasters, statistically indistinguishable crowds, acquiescence bias, and averaging beating either alone.
- gpt: exists=verified applied=verified [evidence_text] — Crossref matches the DOI, title, authors, journal, year, volume, and issue. The abstract directly supports the claims about 12 LLMs, 31 binary questions, 925 human forecasters, a three-month tournament, statistical indistinguishability from the human crowd, acquiescence bias, and improved accuracy from averaging human and machine forecasts.

### c78 — exists ✅ · applied ✅  (line 355)
_**4.6 The limit: shared errors.** Kim, E., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors in large language models. _ICML 2025_. arXiv:2506.07962. https://arxiv.org/abs/2506.07962 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID and title match. Abstract contains the exact 60%/350-models figures, correlation despite distinct architectures/providers, and downstream LLM-judge and hiring tasks.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the cited preprint with matching title, authors, and arXiv ID. The abstract directly supports the claims about over 350 LLMs, 60% agreement when both models err, highly correlated errors among larger accurate models even across architectures/providers, and downstream effects in LLM-as-judge evaluation and hiring.

### c80 — exists ✅ · applied ✅  (line 366)
_**5.1** Sclar, M., Choi, Y., Tsvetkov, Y., & Suhr, A. (2024). Quantifying language models' sensitivity to spurious features in prompt design. _ICLR 2024_. arXiv:2310.11324. https://arxiv.org/abs/2310.11324 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID matches (full title slightly longer). Abstract confirms up to 76 accuracy points with LLaMA-2-13B few-shot, persistent sensitivity, and weak cross-model format correlation.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the URL confirm the cited paper, with the reference using the main title and omitting the subtitle shown in retrieved metadata. The abstract directly supports the claims about up to 76 accuracy-point differences for LLaMA-2-13B, persistence across size/examples/instruction tuning, and weak correlation of best formats between models.

### c81 — exists ✅ · applied ✅  (line 375)
_Lu, Y., Bartolo, M., Moore, A., Riedel, S., & Stenetorp, P. (2022). Fantastically ordered prompts and where to find them. _ACL 2022_. arXiv:2104.08786. https://arxiv.org/abs/2104.08786 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract explicitly states order can make the difference between near state-of-the-art and random guess performance and that a good permutation for one model is not transferable to another.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited work, authors, and title variant. The abstract directly states that prompt example order can range from near state-of-the-art to random-guess performance and that good permutations do not transfer across models.

### c82 — exists ✅ · applied ✅  (line 381)
_Mizrahi, M., Kaplan, G., Malkin, D., Dror, R., Shahaf, D., & Stanovsky, G. (2024). State of what art? A call for multi-prompt LLM evaluation. _TACL_. arXiv:2401.00595. https://arxiv.org/abs/2401.00595 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 6.5M instances, 20 LLMs, 39 tasks, brittleness of single-prompt evaluations, and the recommendation to use diverse prompt sets.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL resolve to the cited paper. The abstract explicitly reports 6.5M instances, 20 LLMs, 39 tasks, brittleness of single-prompt evaluations, and recommends diverse prompt sets.

### c87 — exists ✅ · applied ✅  (line 414)
_Laban, P., Murakhovs'ka, L., Xiong, C., & Wu, C.-S. (2023). Are you sure? Challenging LLMs leads to performance drops in the FlipFlop experiment. arXiv:2311.08596. https://arxiv.org/abs/2311.08596 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms ten LLMs, seven tasks, 46% average flip rate, and average 17% accuracy drop.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL match the cited preprint. The abstract explicitly reports ten LLMs, seven classification tasks, 46% answer flipping, and a 17% average accuracy drop.

### c91 — exists ✅ · applied ✅  (line 439)
_Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. _NeurIPS 2020_. arXiv:2005.11401. https://arxiv.org/abs/2005.11401 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the founding RAG paper combining a seq2seq model with a Wikipedia dense index and emphasizing knowledge-intensive tasks, provenance, and knowledge updating.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited RAG paper and author list. The abstract states that the authors introduce RAG models using a dense Wikipedia index and emphasizes knowledge-intensive tasks, provenance, and updating knowledge.

### c92 — exists ✅ · applied ✅  (line 446)
_Shuster, K., Poff, S., Chen, M., Kiela, D., & Weston, J. (2021). Retrieval augmentation reduces hallucination in conversation. arXiv:2104.07567. https://arxiv.org/abs/2104.07567 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms retrieval-in-the-loop models substantially reduce knowledge hallucination as verified by human evaluations.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited paper. The abstract explicitly says retrieval-in-the-loop dialogue models, verified by human evaluations, substantially reduce knowledge hallucination.

### c93 — exists ✅ · applied ✅  (line 452)
_Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D., & Ho, D. E. (2025). Hallucination-free? Assessing the reliability of leading AI legal research tools. _Journal of Empirical Legal Studies_, 22(2), 216–242. https://doi.org/10.1111/jels.12413 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms preregistered evaluation, overstated vendor claims, and LexisNexis/Thomson Reuters tools hallucinating 17-33% of the time while reduced relative to GPT-4.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the journal article, DOI, venue, volume, issue, pages, authors, and abstract. The abstract directly supports the preregistered evaluation, vendor hallucination-free claims, reduced-but-not-eliminated hallucinations, and 17%–33% hallucination rates.

### c94 — exists ✅ · applied ✅  (line 464)
_Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. arXiv:2201.11903. https://arxiv.org/abs/2201.11903 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms chain-of-thought exemplars improve arithmetic, commonsense, and symbolic reasoning in large models.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited chain-of-thought paper. The abstract explicitly says chain-of-thought exemplars improve arithmetic, commonsense, and symbolic reasoning performance in large language models.

### c95 — exists ✅ · applied ✅  (line 470)
_Meincke, L., Mollick, E., Mollick, L., & Shapiro, D. (2025b). Prompting Science Report 2: The decreasing value of chain of thought in prompting. arXiv:2506.07142. https://arxiv.org/abs/2506.07142 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract matches the claim quote precisely regarding small improvements with variability for non-reasoning models and marginal gains at higher cost for reasoning models.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited Prompting Science Report 2. The abstract directly supports the claims about small gains and added variability for non-reasoning models, marginal gains for reasoning models, and higher token/time cost.

### c97 — exists ✅ · applied ✅  (line 488)
_Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., & Zhou, D. (2024). Large language models cannot self-correct reasoning yet. _ICLR 2024_. arXiv:2310.01798. https://arxiv.org/abs/2310.01798 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms LLMs struggle to self-correct without external feedback and sometimes degrade after self-correction.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited ICLR 2024 paper. The abstract explicitly states that without external feedback LLMs struggle to self-correct reasoning and sometimes degrade after self-correction.

### c98 — exists ✅ · applied ✅  (line 494)
_Kamoi, R., Zhang, Y., Zhang, N., Han, J., & Zhang, R. (2024). When can LLMs actually correct their own mistakes? A critical survey of self-correction of LLMs. _TACL_, 12, 1417–1440. https://doi.org/10.1162/tacl_a_00713 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms over-evaluation, the quote that no prior work shows successful self-correction with prompted-LLM feedback except exceptionally suited tasks, and that it works with reliable external feedback.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the TACL article, DOI, authors, volume, and pages. The abstract directly supports the over-evaluation critique, the negative finding for prompted-LLM feedback except special tasks, and the positive role of reliable external feedback.

### c100 — exists ✅ · applied ✅  (line 508)
_Also: Dhuliawala, S., et al. (2023). Chain-of-verification reduces hallucination in large language models. arXiv:2309.11495 **[abstract]**. The model drafts, plans verification questions, answers them *independently* "so the answers are not biased by other responses", then revises; hallucinations fell across several tasks._
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms the CoVe draft/plan/answer-independently (not biased by other responses)/revise process and reduced hallucinations across tasks.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited Chain-of-Verification paper and expands the “et al.” author list. The abstract directly describes drafting, planning verification questions, answering them independently to avoid bias, revising, and reducing hallucinations across several tasks.

### c101 — exists ✅ · applied ✅  (line 513)
_Cohen, R., Hamri, M., Geva, M., & Globerson, A. (2023). LM vs LM: Detecting factual errors via cross examination. arXiv:2305.13281. https://arxiv.org/abs/2305.13281 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Arxiv ID and title match exactly; abstract confirms examiner model and outperforming baselines on four benchmarks often by a large gap.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL match the cited title, authors, and identifier. The abstract directly states that another LM acts as examiner, asks questions to find inconsistencies, and outperforms baselines on four benchmarks often by a large gap.

### c102 — exists ✅ · applied ✅  (line 519)
_Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., & Mordatch, I. (2023). Improving factuality and reasoning in language models through multiagent debate. arXiv:2305.14325 **[abstract]**: several model instances debating over rounds improved maths, strategic reasoning and factual validity._
- claude: exists=verified applied=verified [evidence_text] — Metadata matches; abstract confirms multiple instances debating over rounds improved mathematical/strategic reasoning and factual validity.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited title, authors, and identifier. The abstract supports the claim that multiple model instances debate over rounds and improve mathematical reasoning, strategic reasoning, and factual validity.

### c103 — exists ✅ · applied ✅  (line 522)
_Against that, Smit, A., Duckworth, P., Grinsztajn, N., Barrett, T. D., & Pretorius, A. (2023). Should we be going MAD? A look at multi-agent debate strategies for LLMs. arXiv:2311.17371 **[abstract]**: debate systems "do not reliably outperform" self-consistency and ensembling, though some do better after tuning._
- claude: exists=verified applied=verified [evidence_text] — Metadata matches; abstract confirms MAD 'do not reliably outperform' self-consistency/ensembling, with some doing better after tuning.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record matches the cited title, authors, and identifier. The abstract explicitly says MAD systems do not reliably outperform self-consistency and ensembling, while several perform better after hyperparameter tuning.

### c105 — exists ✅ · applied ✅  (line 537)
_Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. _NeurIPS 2023 Datasets and Benchmarks_. arXiv:2306.05685. https://arxiv.org/abs/2306.05685 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Metadata matches; abstract confirms GPT-4 over 80% agreement matching humans, and examination of position/verbosity/self-enhancement biases.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL match the cited work. The abstract directly states the over-80% GPT-4 agreement claim and says the paper examines position, verbosity, and self-enhancement biases.

### c106 — exists ✅ · applied ✅  (line 545)
_Bavaresco, A., Bernardi, R., Bertolazzi, L., Elliott, D., Fernández, R., Gatt, A., et al. (2025). LLMs instead of human judges? A large scale empirical study across 20 NLP evaluation tasks. _ACL 2025_. arXiv:2406.18403. https://arxiv.org/abs/2406.18403 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Metadata matches; abstract confirms 11 LLMs, 20 datasets, substantial variance, and the validation recommendation. Claim of 'eleven LLMs, twenty datasets' aligns.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL match the cited title, authors, and identifier. The abstract explicitly supports the claims about 11 LLMs, 20 datasets, substantial variance, task-dependent reliability, and the need to validate against human judgments.

### c107 — exists ✅ · applied ✅  (line 552)
_Panickssery, A., Bowman, S. R., & Feng, S. (2024). LLM evaluators recognize and favor their own generations. arXiv:2404.13076. https://arxiv.org/abs/2404.13076 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Metadata matches; abstract confirms self-preference bias linked to self-recognition capability.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL match the cited work. The abstract directly defines self-preference as scoring one's own outputs higher when humans rate them equal and links this to self-recognition capability.

### c108 — exists ✅ · applied ✅  (line 557)
_Haldar, R., & Hockenmaier, J. (2025). Rating roulette: Self-inconsistency in LLM-as-a-judge frameworks. _Findings of EMNLP 2025_. arXiv:2510.27106. https://arxiv.org/abs/2510.27106 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — Metadata matches; abstract confirms low intra-rater reliability, 'almost arbitrary in the worst case' quote verbatim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL match the cited title, authors, and identifier. The abstract explicitly states that LLM judges have low intra-rater reliability across runs and can be almost arbitrary in the worst case.
