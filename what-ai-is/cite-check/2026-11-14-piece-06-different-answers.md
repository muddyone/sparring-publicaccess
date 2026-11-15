# cite-check report: essay 06 (why you get different answers), after the first panel

**Source:** `docs/research/what-ai-is/drafts/2026-11-14-06-different-answers.md` at the post-panel revision (worklist W-5), checked 2026-11-14. Substrates: claude-opus-4-8 + gpt-5.5-2026-04-23.

**Reading (drafter).** Nothing in the essay body was refuted. Body citations c01–c27: 21 clean in both substrates. Two splits, c03 (He 2025, the 80-versions demonstration) and c17 (Paper 1 §6.4), are retrieval gaps, not errors: brief 12 checked He against the post itself, and the panel's numbers reviewer (Vera) checked §6.3 and §6.4 against Paper 1's text. c25 (Paper 1 §6.3) is the same retrieval gap. c06 (Wang et al. 2023): the 57-to-74 figures and the 40 samples were read in the paper's table (PaLM-540B on GSM8K, 56.5 to 74.4 with 40 sampled paths), not only its abstract. Two wordings were narrowed after this run: c20 (Lewis is now the best-known form of retrieval-augmented generation, not the origin of the general idea) and c18 (Smit: 'having several AIs debate', not 'more rounds'). c11 and c13 were judged on title or snippet evidence for one source each and stand. The extraction also picked up the Sources list and internal links (c30 onward); those entries carry no claims and are not read here. Not re-run after the two narrowings.

## Coverage (read this first)
- **56** citations checked
- existence independently confirmed: **53**
- application evidence-grounded: **53**
- application judged from model knowledge only: **0**
- not independently checkable: **3**
- buckets — clean **19** · problem **38** · disagree **2**

## ⛔ DISAGREE — escalate to human (2)
### c03 — exists ✅ · applied SPLIT  (line 46)
_([He & Thinking Machines Lab 2025](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/))_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The blog exists and discusses temperature-zero nondeterminism, but the retrieved snippet does not confirm the specific '1,000 runs, 80 distinct versions' figure, so the precise claim is only partially verifiable.
- gpt: exists=verified applied=unchecked [evidence_text] — The URL resolves to the cited Thinking Machines Lab post by Horace He. The retrieved snippet supports the general topic of temperature-zero nondeterminism but does not include the specific 1,000-run/80-version demonstration, so the application cannot be confirmed from the provided evidence.

### c17 — exists ✅ · applied SPLIT  (line 124)
_([Niedner 2026](https://doi.org/10.5281/zenodo.21210264), section 6.4)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The Zenodo record exists (though at a different record number than the cited DOI and described as a pre-registered null on SPARRING's Resolver); the snippet confirms the general pre-registered adversarial-review study but does not detail the specific per-flaw comparison figures.
- gpt: exists=verified applied=unchecked [evidence_text] — The DOI URL resolves to a Zenodo record matching Niedner’s preprint title and authorship, despite Crossref not resolving it. The retrieved snippet mentions pre-registration and SPARRING artifacts but does not include the detailed section 6.4 findings about challenges, flaws, pressured rewrites, or comparison with quiet rewrites.

## ⚠️ AGREE-problem (38)
### c06 — exists ✅ · applied ⚠️  (line 70)
_([Wang et al. 2023](https://arxiv.org/abs/2203.11171))_
- claude: exists=verified applied=verified [evidence_text] — Self-consistency samples multiple reasoning paths and takes the majority answer, improving GSM8K by +17.9%; the specific 57→74 figures align with the paper's known PaLM results and the +17.9% gain.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record confirms Wang et al.’s self-consistency paper. The abstract supports the core claim that sampling multiple reasoning paths and taking the most consistent answer improves GSM8K by 17.9 points, but it does not itself state the 40 samples or the exact 57-to-74 figures.

### c11 — exists ✅ · applied ⚠️  (line 103)
_([Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888)_
- claude: exists=verified applied=verified [evidence_text] — The paper's title and venue confirm personas in system prompts do not improve LLM performance, supporting that 'you are an expert' didn't improve factual answers.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the ACL URL confirm the cited Findings of EMNLP paper. The title/snippet supports the general claim that personas in system prompts do not improve LLM performance, but the retrieved evidence does not specifically show the factual-answer or “you are an expert” condition.

### c13 — exists ⚠️ · applied ⚠️  (line 106)
_(Meincke et al. [2025a](https://arxiv.org/abs/2503.04818) and [2025c](https://arxiv.org/abs/2508.00614))_
- claude: exists=verified applied=nuance [evidence_text] — Both reports exist (Report 1 on politeness being mixed, Report 3 on tipping/threatening); the retrieved abstract supports the politeness claim, and Report 3's title corroborates the tipping/threatening finding, though its abstract was not retrieved.
- gpt: exists=nuance applied=nuance [evidence_text] — The first cited Meincke et al. arXiv work is confirmed, and the second URL resolves to a related Prompting Science Report 3 title, though only title-level evidence is provided for the second work. The abstract supports the politeness part, but the retrieved evidence does not substantively verify the tipping/threatening no-effect result beyond the second title’s topic.

### c18 — exists ✅ · applied ⚠️  (line 126)
_([Smit et al. 2023](https://arxiv.org/abs/2311.17371))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states multi-agent debate does not reliably outperform self-consistency and ensembling multiple reasoning paths, matching the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record confirms Smit et al.’s paper on multi-agent debate strategies. The abstract supports that current multi-agent debate systems do not reliably outperform self-consistency or ensembling, though the specific phrasing about “more rounds” is not directly stated in the retrieved abstract.

### c20 — exists ✅ · applied ⚠️  (line 133)
_[Lewis et al. 2020](https://arxiv.org/abs/2005.11401)_
- claude: exists=verified applied=verified [evidence_text] — This is the foundational RAG paper introducing retrieval-augmented generation, supporting the claim that answering from provided documents was introduced here.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record confirms Lewis et al.’s Retrieval-Augmented Generation paper. The abstract supports that the paper introduces RAG models combining generation with retrieved Wikipedia passages, but the broader claim that it introduced the general idea of giving models documents to answer from is imprecise.

### c25 — exists ✅ · applied ☐  (line 151)
_[Niedner 2026](https://doi.org/10.5281/zenodo.21210264), section 6.3_
- claude: exists=verified applied=unchecked [evidence_text] — The Zenodo record (Niedner 2026, SPARRING Resolver report) exists and matches the author's self-citation, but the retrieved landing-page snippet does not contain the specific flaw counts (31/27/21/17) to verify the detailed claims.
- gpt: exists=verified applied=unchecked [evidence_text] — The DOI URL resolves to a Zenodo record titled 'Auditable adversarial review for AI-in-the-loop decisions...' by Barton Niedner, published in 2026, though Crossref did not resolve it. The retrieved snippet describes the record and artifacts but does not include section 6.3 or the specific numerical findings claimed.

### c28 — exists ☐ · applied ☐  (line 177)
_I couldn't find a study that settles the comparison, with the same task given twice to both a model and a group of experts, so I can only argue it._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author explicitly states no such study was found.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and is the author's statement that no settling study was found. Per instructions, both axes are unchecked.

### c29 — exists ☐ · applied ☐  (line 218)
_That people who check more actually decide better. I found no study of real users testing that._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; author states no study of real users was found.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and reports the author's inability to find a real-user study. Per instructions, both axes are unchecked.

### c30 — exists ☐ · applied ☐  (line 260)
_[Why does the same AI give different answers?](../briefs/2026-10-19-12-different-answers.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path link could not be resolved; existence not checkable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only URL is a relative local path and the fetch failed as an unknown URL type, so existence is not checkable from the retrieved evidence. No source text was retrieved to assess whether it supports the claim.

### c31 — exists ☐ · applied ☐  (line 263)
_[check](../cite-check/2026-10-19-the-different-answers-brief.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path link could not be resolved; existence not checkable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a relative local path and the fetch failed as an unknown URL type, so existence cannot be judged from the evidence. No text was retrieved to assess the claim about the checking tool.

### c32 — exists ☐ · applied ☐  (line 265)
_[review](../panel/2026-11-14-piece-06-different-answers/)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal relative-path link could not be resolved; existence not checkable from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited review is a relative local path and the fetch failed as an unknown URL type, so existence is not checkable. No source text was retrieved to assess the claim about five AI reviewers.

### c33 — exists ☐ · applied ☐  (line 265)
__[The essay's own cite-check: to come.]__
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited; marked as in-progress work to come.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately uncited and in progress as 'to come.' Per instructions, both axes are unchecked.

### c34 — exists ✅ · applied ☐  (line 269)
_[Atil et al. 2024](https://arxiv.org/abs/2408.04667)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2408.04667 (Atil et al., non-determinism of deterministic LLM settings) confirmed to exist; no specific claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Atil et al., 'Non-Determinism of "Deterministic" LLM Settings.' No claim was supplied for this citation, so application cannot be assessed.

### c35 — exists ✅ · applied ☐  (line 270)
_[Basil et al. 2025](https://arxiv.org/abs/2512.05858)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2512.05858 exists (Prompting Science Report 4); note the lead author is 'Basil, Savir' so 'Basil et al.' reflects a given/surname confusion, but the work is confirmed. No specific claim to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Basil et al., 'Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy.' No claim was supplied for this citation, so application cannot be assessed.

### c36 — exists ✅ · applied ☐  (line 271)
_[Elmore et al. 1994](https://doi.org/10.1056/NEJM199412013312206)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Elmore et al. 1994; no specific claim attached to this instance to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI verifies Elmore et al. 1994 in the New England Journal of Medicine. No claim was supplied for this citation, so application cannot be assessed.

### c37 — exists ✅ · applied ☐  (line 272)
_[Farquhar et al. 2024](https://doi.org/10.1038/s41586-024-07421-0)_
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves to Farquhar et al. 2024 Nature (semantic entropy); confirmed to exist; no specific claim attached to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the URL verify Farquhar et al. 2024 in Nature, 'Detecting hallucinations in large language models using semantic entropy.' No claim was supplied for this citation, so application cannot be assessed.

### c38 — exists ✅ · applied ☐  (line 273)
_[Gou et al. 2024](https://arxiv.org/abs/2305.11738)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 2305.11738 (CRITIC) confirmed; no specific claim attached to this instance to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Gou et al., 'CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing.' No claim was supplied for this citation, so application cannot be assessed.

### c39 — exists ✅ · applied ☐  (line 274)
_[He & Thinking Machines Lab 2025](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)_
- claude: exists=verified applied=unchecked [no_basis] — Thinking Machines Lab blog post by Horace He on defeating nondeterminism in LLM inference confirmed to exist at the given URL; no specific claim attached to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to the Thinking Machines Lab post 'Defeating Nondeterminism in LLM Inference' by Horace He in collaboration with others, dated Sep. 10, 2025. No claim was supplied for this citation, so application cannot be assessed.

### c40 — exists ✅ · applied ☐  (line 275)
_[Holtzman et al. 2020](https://arxiv.org/abs/1904.09751)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv 1904.09751 (Holtzman et al., The Curious Case of Neural Text Degeneration) confirmed to exist; no specific claim attached to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to Holtzman et al., 'The Curious Case of Neural Text Degeneration.' No claim was supplied for this citation, so application cannot be assessed.

### c41 — exists ✅ · applied ☐  (line 276)
_[Huang et al. 2024](https://arxiv.org/abs/2310.01798)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv ID 2310.01798 matches 'LLMs Cannot Self-Correct Reasoning Yet' by Huang et al. No specific claim was provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Large Language Models Cannot Self-Correct Reasoning Yet' by Jie Huang et al. No claim was supplied for this citation, so application cannot be evaluated.

### c42 — exists ✅ · applied ☐  (line 277)
_[Kim et al. 2025](https://arxiv.org/abs/2506.07962)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2506.07962 'Correlated Errors in Large Language Models' by Kim et al. confirmed. No claim text supplied to judge application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Correlated Errors in Large Language Models' by Elliot Kim et al. No claim was supplied for this citation, so application cannot be evaluated.

### c43 — exists ✅ · applied ☐  (line 278)
_[Laban et al. 2023](https://arxiv.org/abs/2311.08596)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2311.08596 FlipFlop experiment paper by Laban et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment' by Philippe Laban et al. No claim was supplied for this citation, so application cannot be evaluated.

### c44 — exists ✅ · applied ☐  (line 279)
_[Lewis et al. 2020](https://arxiv.org/abs/2005.11401)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2005.11401 RAG paper by Lewis et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks' by Patrick Lewis et al. No claim was supplied for this citation, so application cannot be evaluated.

### c45 — exists ✅ · applied ☐  (line 280)
_[Magesh et al. 2025](https://doi.org/10.1111/jels.12413)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Magesh et al. legal AI hallucination study in Journal of Empirical Legal Studies. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, journal, year, volume, issue, pages, and abstract for Magesh et al.'s 2025 Journal of Empirical Legal Studies article. No claim was supplied for this citation, so application cannot be evaluated.

### c46 — exists ✅ · applied ☐  (line 281)
_[Manakul et al. 2023](https://arxiv.org/abs/2303.08896)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2303.08896 SelfCheckGPT by Manakul et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models' by Potsawee Manakul et al. No claim was supplied for this citation, so application cannot be evaluated.

### c47 — exists ✅ · applied ☐  (line 282)
_[Meincke et al. 2025a](https://arxiv.org/abs/2503.04818)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2503.04818 Prompting Science Report 1 by Meincke et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Prompting Science Report 1: Prompt Engineering is Complicated and Contingent' by Lennart Meincke et al. No claim was supplied for this citation, so application cannot be evaluated.

### c48 — exists ✅ · applied ☐  (line 283)
_[Meincke et al. 2025c](https://arxiv.org/abs/2508.00614)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2508.00614 Prompting Science Report 3 by Meincke et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Prompting Science Report 3: I'll pay you or I'll kill you -- but will you care?' by Lennart Meincke et al. No claim was supplied for this citation, so application cannot be evaluated.

### c49 — exists ✅ · applied ☐  (line 284)
_[Niedner 2026](https://doi.org/10.5281/zenodo.21210264)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref failed but Zenodo URL resolves to the Niedner 2026 SPARRING report; DOI slightly differs from redirected record but the work clearly exists. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI URL resolves to a Zenodo record titled 'Auditable adversarial review for AI-in-the-loop decisions...' with author/creator Barton Niedner and 2026 publication details, despite Crossref not finding it. No claim was supplied for this citation, so application cannot be evaluated.

### c50 — exists ✅ · applied ☐  (line 285)
_[Schoenegger et al. 2024](https://doi.org/10.1126/sciadv.adp1528)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Schoenegger et al. 'Wisdom of the silicon crowd' in Science Advances. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, title, authors, journal, year, and abstract for Schoenegger et al.'s 2024 Science Advances article. No claim was supplied for this citation, so application cannot be evaluated.

### c51 — exists ✅ · applied ☐  (line 286)
_[Sclar et al. 2024](https://arxiv.org/abs/2310.11324)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2310.11324 prompt formatting sensitivity paper by Sclar et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design...' by Melanie Sclar et al. No claim was supplied for this citation, so application cannot be evaluated.

### c52 — exists ✅ · applied ☐  (line 287)
_[Sharma et al. 2023](https://arxiv.org/abs/2310.13548)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2310.13548 sycophancy paper by Sharma et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Towards Understanding Sycophancy in Language Models' by Mrinank Sharma et al. No claim was supplied for this citation, so application cannot be evaluated.

### c53 — exists ✅ · applied ☐  (line 288)
_[Shuster et al. 2021](https://arxiv.org/abs/2104.07567)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2104.07567 retrieval augmentation paper by Shuster et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Retrieval Augmentation Reduces Hallucination in Conversation' by Kurt Shuster et al. No claim was supplied for this citation, so application cannot be evaluated.

### c54 — exists ✅ · applied ☐  (line 289)
_[Smit et al. 2023](https://arxiv.org/abs/2311.17371)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2311.17371 multi-agent debate paper by Smit et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs' by Andries Smit et al. No claim was supplied for this citation, so application cannot be evaluated.

### c55 — exists ✅ · applied ☐  (line 290)
_[Steyvers et al. 2025](https://doi.org/10.1038/s42256-024-00976-7)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Steyvers et al. in Nature Machine Intelligence. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and URL evidence confirm Steyvers et al.'s 2025 Nature Machine Intelligence article 'What large language models know and what people think they know.' No claim was supplied for this citation, so application cannot be evaluated.

### c56 — exists ✅ · applied ☐  (line 291)
_[Ulery et al. 2012](https://doi.org/10.1371/journal.pone.0032800)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Ulery et al. latent fingerprint examiner study in PLoS ONE. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref, Europe PMC, and URL evidence confirm Ulery et al.'s 2012 PLoS ONE article 'Repeatability and Reproducibility of Decisions by Latent Fingerprint Examiners.' No claim was supplied for this citation, so application cannot be evaluated.

### c57 — exists ✅ · applied ☐  (line 292)
_[Wang et al. 2023](https://arxiv.org/abs/2203.11171)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2203.11171 self-consistency paper by Wang et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Self-Consistency Improves Chain of Thought Reasoning in Language Models' by Xuezhi Wang et al. No claim was supplied for this citation, so application cannot be evaluated.

### c58 — exists ✅ · applied ☐  (line 293)
_[Xiong et al. 2024](https://arxiv.org/abs/2306.13063)_
- claude: exists=verified applied=unchecked [no_basis] — ArXiv 2306.13063 confidence elicitation paper by Xiong et al. confirmed. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv and URL evidence confirm the work 'Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs' by Miao Xiong et al. No claim was supplied for this citation, so application cannot be evaluated.

### c59 — exists ✅ · applied ☐  (line 294)
_[Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888)_
- claude: exists=verified applied=unchecked [no_basis] — DOI matches Zheng et al. personas-in-system-prompts paper in EMNLP 2024 Findings. No claim provided.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and ACL URL evidence confirm Zheng et al.'s 2024 Findings of ACL: EMNLP paper 'When “A Helpful Assistant” Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models.' No claim was supplied for this citation, so application cannot be evaluated.

## ✅ AGREE-clean (19)
### c01 — exists ✅ · applied ✅  (line 36)
_([Holtzman et al. 2020](https://arxiv.org/abs/1904.09751))_
- claude: exists=verified applied=verified [evidence_text] — The abstract explicitly states likelihood decoding yields text 'bland and strangely repetitive' and nucleus sampling produces more human-like text, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv lookup confirms Holtzman et al., The Curious Case of Neural Text Degeneration. The abstract directly says likelihood/greedy-style decoding leads to text that is “bland and strangely repetitive” and that nucleus sampling better demonstrates human-like text quality.

### c02 — exists ✅ · applied ✅  (line 42)
_([Atil et al. 2024](https://arxiv.org/abs/2408.04667))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms five LLMs, eight tasks, 10 runs, and accuracy variations up to 15%, matching the claim closely.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Atil et al. 2024, Non-Determinism of “Deterministic” LLM Settings. The abstract directly reports five LLMs, eight tasks, 10 runs, deterministic settings, and accuracy variation up to 15%.

### c04 — exists ✅ · applied ✅  (line 63)
_([Manakul et al. 2023](https://arxiv.org/abs/2303.08896))_
- claude: exists=verified applied=verified [evidence_text] — SelfCheckGPT is a zero-resource black-box method exploiting that sampled responses diverge for hallucinations, matching the claim exactly.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Manakul et al.’s SelfCheckGPT paper. The abstract directly supports black-box hallucination detection by sampling multiple responses and using divergence/contradiction among them to identify non-factual outputs.

### c05 — exists ✅ · applied ✅  (line 65)
_([Farquhar et al. 2024](https://doi.org/10.1038/s41586-024-07421-0))_
- claude: exists=verified applied=verified [evidence_text] — Nature paper uses meaning-level (semantic) entropy to detect confabulations—arbitrary incorrect generations—across tasks, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the Nature article Detecting hallucinations in large language models using semantic entropy. The abstract directly states that semantic entropy measures uncertainty at the level of meaning to detect confabulations, a subset of hallucinations that are arbitrary and incorrect, across tasks.

### c07 — exists ✅ · applied ✅  (line 82)
_([Farquhar et al. 2024](https://doi.org/10.1038/s41586-024-07421-0))_
- claude: exists=verified applied=verified [evidence_text] — The abstract explicitly states the method detects a subset of hallucinations—confabulations—which are arbitrary and incorrect, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the cited Nature paper. The abstract plainly says the method detects a subset of hallucinations—confabulations—which are arbitrary and incorrect generations.

### c08 — exists ✅ · applied ✅  (line 87)
_([Kim et al. 2025](https://arxiv.org/abs/2506.07962))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms over 350 models, 60% agreement when both err on one leaderboard, and larger/more accurate models having correlated errors across providers.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Kim et al., Correlated Errors in Large Language Models. The abstract directly reports evaluation of over 350 LLMs, 60% agreement when both models err on one leaderboard dataset, and highly correlated errors among larger, more accurate models even across distinct architectures and providers.

### c09 — exists ✅ · applied ✅  (line 97)
_([Xiong et al. 2024](https://arxiv.org/abs/2306.13063))_
- claude: exists=verified applied=verified [evidence_text] — Abstract explicitly notes LLMs tend to be overconfident when verbalizing confidence, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Xiong et al.’s paper on confidence elicitation. The abstract directly states that LLMs verbalizing confidence tend to be overconfident.

### c10 — exists ✅ · applied ✅  (line 99)
_([Steyvers et al. 2025](https://doi.org/10.1038/s42256-024-00976-7))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states longer explanations increased user confidence even when extra length did not improve accuracy, matching the claim exactly.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the Nature Machine Intelligence article by Steyvers et al. The abstract directly states that longer explanations increased user confidence even when the extra length did not improve answer accuracy.

### c12 — exists ✅ · applied ✅  (line 104)
_[Basil et al. 2025](https://arxiv.org/abs/2512.05858))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms expert personas showed no significant/consistent improvement in factual accuracy, matching the claim; arxiv id format is unusual but the record resolves.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Basil et al., Prompting Science Report 4: Playing Pretend. The abstract directly states that expert personas generally did not improve accuracy relative to a no-persona baseline, with no consistent benefit across models.

### c14 — exists ✅ · applied ✅  (line 108)
_([Sclar et al. 2024](https://arxiv.org/abs/2310.11324))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states performance differences up to 76 accuracy points from meaning-preserving formatting changes on LLaMA-2-13B, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Sclar et al.’s paper on prompt formatting sensitivity. The abstract directly states that subtle meaning-preserving formatting changes produced performance differences up to 76 accuracy points for LLaMA-2-13B.

### c15 — exists ✅ · applied ✅  (line 114)
_([Laban et al. 2023](https://arxiv.org/abs/2311.08596))_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms 'Are you sure?' causes 46% answer flips and accuracy deterioration across all models, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Laban et al.’s FlipFlop experiment paper. The abstract directly reports that models flip answers on average 46% of the time after prompts like “Are you sure?” and that all models’ accuracy deteriorated from first to final prediction.

### c16 — exists ✅ · applied ✅  (line 115)
_([Sharma et al. 2023](https://arxiv.org/abs/2310.13548))_
- claude: exists=verified applied=verified [evidence_text] — Abstract documents sycophancy—models matching user beliefs over truth—supporting the claim that assistants tell people what they want to hear.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Sharma et al., Towards Understanding Sycophancy in Language Models. The abstract directly supports the claim that AI assistants exhibit sycophancy, meaning responses that match user beliefs or what users appear to want over truthful answers.

### c19 — exists ✅ · applied ✅  (line 127)
_([Huang et al. 2024](https://arxiv.org/abs/2310.01798))_
- claude: exists=verified applied=verified [evidence_text] — Abstract states LLMs struggle to self-correct without external feedback and sometimes performance degrades, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record confirms Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet. The abstract directly states that without external feedback LLMs struggle to self-correct and sometimes degrade in performance.

### c21 — exists ✅ · applied ✅  (line 135)
_[Shuster et al. 2021](https://arxiv.org/abs/2104.07567)_
- claude: exists=verified applied=verified [evidence_text] — arXiv 2104.07567 is the Shuster et al. retrieval-augmentation paper; its abstract confirms retrieval substantially reduces (not eliminates) hallucination, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Shuster et al., 'Retrieval Augmentation Reduces Hallucination in Conversation.' The abstract states that retrieval-in-the-loop architectures substantially reduce knowledge hallucination in chatbots, supporting the claim; 'doesn't remove them' is consistent with the wording 'reduce' rather than eliminate.

### c22 — exists ✅ · applied ✅  (line 138)
_[Magesh et al. 2025](https://doi.org/10.1111/jels.12413)_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Magesh et al. 2025 in JELS; abstract explicitly states tools hallucinate 17% to 33% of the time, exactly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the 2025 Journal of Empirical Legal Studies article by Magesh et al. The abstract directly states that Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI hallucinate between 17% and 33% of the time despite provider claims about hallucination-free RAG tools.

### c23 — exists ✅ · applied ✅  (line 141)
_[Gou et al. 2024](https://arxiv.org/abs/2305.11738)_
- claude: exists=verified applied=verified [evidence_text] — arXiv 2305.11738 is the CRITIC paper; abstract confirms tool-based self-correction (search/code) consistently improves performance and stresses external feedback, matching claim and author note.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to Gou et al., 'CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing.' The abstract describes LLMs using tools such as search engines and code interpreters to validate and revise outputs, and says this consistently enhances performance while emphasizing external feedback.

### c24 — exists ✅ · applied ✅  (line 145)
_[Schoenegger et al. 2024](https://doi.org/10.1126/sciadv.adp1528)_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Schoenegger et al. 2024 in Science Advances; abstract confirms 12-LLM ensemble on 31 questions vs 925 humans was statistically indistinguishable and averaging did better.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies the Science Advances article by Schoenegger et al. The abstract directly reports an ensemble of 12 LLMs making predictions on 31 binary questions compared with 925 human forecasters, statistically indistinguishable performance, and improved accuracy by averaging human and machine forecasts.

### c26 — exists ✅ · applied ✅  (line 170)
_[Ulery et al. 2012](https://doi.org/10.1371/journal.pone.0032800)_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Ulery et al. 2012; abstract confirms ~7-month retest, ~89-90% repeated decisions (about one in ten changed), most to inconclusive, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI and metadata verify Ulery et al. 2012 in PLoS ONE. The abstract says 72 examiners were retested after about seven months, repeated roughly 89–90% of key decisions, and most changed decisions became inconclusive.

### c27 — exists ✅ · applied ✅  (line 173)
_[Elmore et al. 1994](https://doi.org/10.1056/NEJM199412013312206)_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Elmore et al. 1994; abstract states immediate-workup recommendations ranged 11% to 65% for women without cancer, exactly matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The DOI verifies Elmore et al. 1994 in the New England Journal of Medicine. The abstract directly states that among women without cancer, radiologists' recommendations for immediate workup ranged from 11% to 65%.
