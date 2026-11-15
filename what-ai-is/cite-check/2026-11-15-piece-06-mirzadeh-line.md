# cite-check report: essay 06, the PaLM paragraph after the Mirzadeh line (W-29)

**Source:** `docs/research/what-ai-is/positions/06-different-answers.md`, the paragraph beginning "The same idea also works in the other direction" (2026-11-15). Substrates: claude-opus-4-8 + gpt-5.5-2026-04-23. The Mirzadeh et al. 2024 abstract was fetched from arXiv (2410.05229) before the edit. The Wang et al. 2023 figures (PaLM, 40 samples, 56.5 to 74.4) were read in that paper's table on 2026-11-14; the abstract gives only +17.9.

## Coverage (read this first)
- **2** citations checked
- existence independently confirmed: **2**
- application evidence-grounded: **2**
- application judged from model knowledge only: **0**
- not independently checkable: **0**
- buckets — clean **1** · problem **1** · disagree **0**

## ⚠️ AGREE-problem (1)
### c01 — exists ✅ · applied ⚠️  (line 4)
_([Wang et al. 2023](https://arxiv.org/abs/2203.11171))_
- claude: exists=verified applied=nuance [evidence_text] — The self-consistency paper exists and reports a +17.9% boost on GSM8K via sampling multiple reasoning paths, consistent with the claim's framing; but the abstract doesn't confirm the specific 57→74 PaLM figures or the '40 times' count, so exact numbers are unverified from this evidence.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record and URL confirm the paper 'Self-Consistency Improves Chain of Thought Reasoning in Language Models' by Wang et al. exists. The abstract supports the general claim that self-consistency improves GSM8K by +17.9%, consistent with roughly 57 to 74, but the retrieved text does not itself state PaLM, 40 samples, or the exact 74/57 figures.

## ✅ AGREE-clean (1)
### c02 — exists ✅ · applied ✅  (line 6)
_([Mirzadeh et al. 2024](https://arxiv.org/abs/2410.05229))_
- claude: exists=verified applied=verified [evidence_text] — The GSM-Symbolic paper exists and the abstract explicitly states performance declines when only the numerical values in a question are altered, directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record and URL confirm the paper 'GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models' by Mirzadeh et al. exists. The abstract directly says models show variance across instantiations of the same question and that performance declines when only numerical values are altered.
