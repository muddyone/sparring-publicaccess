# Sources — LLM-as-judge prompt-upgrade discussion (reference)

Every source cited in the R6 prompt-design work, with a one-line summary and a strength tag.
Verified via the deep-research pass 2026-06-30 (raw: `research/r6-llm-judge-calibration-research.json`).
Strength: **STRONG** = peer-reviewed or mathematically provable / multi-source · **MEDIUM** = solid single primary · **EMERGING** = single recent preprint, cite with caution · **VENDOR** = first-party docs · **PRACTITIONER** = reputable blog.

## Academic / foundational
- **G-Eval** — Liu et al., *G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*, EMNLP 2023. arXiv:2303.16634. **STRONG.** Chain-of-thought + form-filling judge; Spearman 0.514 with humans (moderate). The canonical "reasoning-before-verdict helps the *detection* judge" result.
- **CALM / "Justice or Prejudice?"** — Ye et al., ICLR 2025. arXiv:2410.02736. **STRONG.** Identifies & quantifies **12 judge biases** (position, verbosity, self-enhancement, authority, sentiment, chain-of-thought, refinement-aware, …) via automated perturbation; shows biases persist task-by-task even in strong models.
- **"From Generation to Judgment" (survey)** — Li et al., 2024. arXiv:2411.16594. **STRONG.** Umbrella survey organizing the field by what-to-judge / how-to-judge / how-to-benchmark. Good single methods/limitations cite. (Distinct from the next item — adjacent IDs, don't conflate.)
- **"A Survey on LLM-as-a-Judge"** — Gu et al., 2024/2025. arXiv:2411.15594. **STRONG.** The other canonical survey; reliability, bias mitigation, prompt engineering. (Also the source that *refuted* "pairwise is inherently better-calibrated than absolute scoring.")

## Calibration & agreement metrics
- **Judge overconfidence / ECE** — arXiv:2508.06225 (Aug 2025). **MEDIUM.** On JudgeBench (14 models), judges cluster confidence at 90–100% while accuracy is far lower (GPT-4o ECE ≈ 39–47). ⇒ don't trust a judge's self-reported confidence as a materiality signal.
- **Agreement Metrics for LLM-as-Judge** — Rao & Callison-Burch (UPenn). arXiv:2606.00093. **STRONG (provable).** On binary verdicts, Pearson r / Spearman ρ / Kendall τ / φ / MCC collapse to one number — report **Cohen's κ** instead. `|κ| ≤ |φ|`, equal only when judge & truth positive-rates match ⇒ **the κ–φ gap is the over-flag drift metric.** Safest thing to cite.

## The over-flagging failure mode (most on-point to our gate)
- **Systematic Overcorrection in Requirement Conformance Judgement** — Jin & Chen, 2026. arXiv:2603.00539. **STRONG (named effect).** LLM judges misclassify *correct* artifacts as defective; accuracy falls 52%→11% when the judge is asked to judge **+ explain + propose fixes**. The direct mechanism behind our 94% flag-rate / 0.19 precision.
- **Independent replication** — arXiv:2508.12358 (Aug 2025). **STRONG (corroboration).** Separate group: judges issue false-negative conformance verdicts, worsening as prompts get more complex (GPT-4o −41pp).
- **Faithful or Fabricated? (structured-CoT / Proof-Before-Preference)** — arXiv:2605.23970. **EMERGING.** Single recent preprint: rubric-guided "structured CoT" *amplifies* label/cue dependence; an evidence-lock-before-verdict ordering ("Proof-Before-Preference") nearly removes it. Promising, not settled — cite as emerging.

## Vendor guidance (authoritative for Claude, not independently benchmarked)
- **Anthropic — Define success criteria & build evaluations** (docs.anthropic.com/.../test-and-evaluate/develop-tests). **VENDOR.** Detailed auto-grade rubrics; force an empirical verdict (binary or 1–5, never purely qualitative); have the judge reason then discard the reasoning.
- **Anthropic — Use XML tags** (.../prompt-engineering/use-xml-tags). **VENDOR.** Wrap distinct inputs (`<previous_version>`, `<candidate>`, `<target_flaw>`, `<rubric>`, `<examples>`) in their own tags to cut misinterpretation.
- **Anthropic — Chain-of-thought** (.../prompt-engineering/chain-of-thought). **VENDOR.** Prefer general "think thoroughly" over hand-written step plans (helps detection; note the over-correction caveat for the gate).
- **Anthropic — Multishot prompting** (.../prompt-engineering/multishot-prompting). **VENDOR.** 3–5 examples, **relevant + diverse** (cover edge/borderline cases).
- **Anthropic — Demystifying evals for AI agents** (anthropic.com/engineering/demystifying-evals-for-ai-agents). **VENDOR.** Agent-eval framing.

## Practitioner
- **Hamel Husain — evals FAQ / LLM-as-judge** (hamel.dev/blog/posts/evals-faq, /llm-judge). **PRACTITIONER.** Eval-driven / error-analysis-first judge development; draft pass/fail rubric, label a shared set, measure inter-annotator agreement. *(Referenced from our brief; not retrieved in the verification pass — verify before citing in the paper.)*
- **Eugene Yan — LLM evaluators** (eugeneyan.com/writing/llm-evaluators). **PRACTITIONER.** Binary/low-precision verdicts over fine-grained scales; calibrate against labels.
- **Panel of LLM evaluators (PoLL)** — Verga et al. 2024 (practitioner writeup: orq.ai/blog/llm-juries-in-practice). **PRACTITIONER/primary.** Three small disjoint-family judges + aggregation beat one large judge — supports the gate panel/ensemble.

## Excluded (refuted in verification)
- ✗ "Pairwise framing is inherently better-calibrated than absolute scoring" — killed 0-3 against arXiv:2411.15594v6. Do not assert.
