# R6 — prompt-design spec: recrafted Challenger + purpose-built Gate (EXPLORATORY)

**Status:** design spec, grounded in a verified literature pass (`research/r6-llm-judge-calibration-research.json` — 6 angles, 27 sources, 25 claims adversarially verified, 24 confirmed / 1 refuted, 2026-06-30). To be tuned **eval-driven** on the n=61 candidate harness, **not** shipped as-written. The DV scorer stays **frozen** (the yardstick).

---

## The headline finding (it flips part of my earlier advice)

**The two prompts pull in OPPOSITE directions on how much to reason — and getting that backwards is our bug.**

- **Challenger (detection):** reasoning-before-verdict *helps*. G-Eval (CoT + form-filling) is the canonical, alignment-improving technique (Liu et al., EMNLP 2023). Anthropic concurs ("have the judge think, then discard the reasoning").
- **Gate (admit/reject):** reasoning *hurts*. There is a **named, twice-replicated** failure mode — **"systematic over-correction in requirement-conformance judgement"** — where asking an LLM judge for explanations/fixes and piling on prompt detail makes it flag *more* correct artifacts as defective (GPT-4o accuracy **52% → 11%** under judge+explain+fix prompts; Jin & Chen 2026, arXiv:2603.00539; independently arXiv:2508.12358). Rubric-guided "structured CoT" can *amplify* cue dependence (arXiv:2605.23970).

**That is precisely our gate's 94% flag-rate / 0.19 precision.** I earlier suggested adding chain-of-thought and a rich rubric to the gate — the literature says that would make the over-flagging *worse*. The gate must be **lean, decision-only, default-to-admit, evidence-locked.** (Confidence: the over-correction effect is well-supported — two independent primary sources; the "evidence-lock fixes it" specifics rest on a single recent preprint — cite as emerging.)

---

## Spec 1 — Recrafted CHALLENGER (high recall on material flaws)

Keep the current `CHAL_SYS` spine (material would-ship, not nitpicks, polite-not-pleasing, honest both directions) and **add**: (a) 2-3 worked *not-material* negatives, (b) reason-before-verdict, (c) per-flaw empirical output (severity 1-5 + material y/n) with a forced one-line justification **quoting the offending text** (anchors recall, curbs fabrication), (d) 3-5 relevant+diverse few-shots. Measure **recall against the fixed flaw list**; tune the materiality bar, not the raw flaw count.

**Draft system prompt (v1, to be eval-tuned):**
> You are an adversarial Challenger reviewing a recommendation produced for a hard decision. Work from a different angle and evidence base than the author. Surface only **MATERIAL would-ship flaws**: errors that would change the decision or ship a real defect. NOT material, and must be excluded: style, wording, "consider also" additions, hedges, or anything that wouldn't change what gets shipped. Examples of NOT material: «{2-3 worked negatives}». Be polite, not pleasing — don't soften a real objection, and don't invent objections to fill space; if there is no material flaw, return an empty list. Think the recommendation through before listing anything, then for EACH flaw output: a snake_case handle, a one-sentence statement, the exact quoted text it concerns, a severity 1-5, and material=true/false. (Reasoning may be verbose here — detection benefits from it.)

## Spec 2 — Purpose-built GATE (raise precision, keep recall, default-to-admit)

This is the load-bearing recraft. Apply, in priority order:

1. **Stop reusing the iteration challenger prompt.** (Already the diagnosis from R5.)
2. **Default-to-admit** unless a clear would-ship regression. Frame the *burden of proof* on REJECT.
3. **Judge the DELTA, not the document.** Two crisp questions only: did the revision *resolve the target flaw*, and did it *introduce a NEW would-ship defect absent from the previous version*. A flaw that already existed, or is a nitpick, is **not** grounds to reject.
4. **Evidence-lock before verdict** ("Proof-Before-Preference"): quote the specific delta-text first, *then* decide. **Keep reasoning minimal and decision-only — do NOT let the gate propose fixes or write long explanations** (that is the over-correction trigger).
5. **XML-tag the inputs** (`<previous_version>`, `<candidate>`, `<target_flaw>`, `<rubric>`, `<examples>`).
6. **Explicit materiality + severity auto-grade rule** calibrated to the DV standard.
7. **Binary ADMIT/REJECT + one-line justification** (no graded score).
8. **Replicate / small disjoint-family panel** (PoLL-style) to cut variance + position/self-enhancement bias.
9. **Calibrate few-shots from gate-vs-DV disagreements**, weighted toward *borderline-resolved* and *not-material-regression* negatives — 3-5 only (few-shot calibration is unstable w.r.t. label/order/count; hold a test split).

**Draft system prompt (v1, to be eval-tuned):**
> You are a release GATE. Your only output is a binary ADMIT or REJECT on one proposed revision. You are NOT a critic and NOT an author; you do NOT suggest improvements or fixes. **Default to ADMIT.** Reject ONLY if the revision introduces a NEW would-ship defect — one that on its own changes the decision or ships a real failure — that was absent from the previous version and is at least as severe as the flaw it was meant to fix. A nitpick, a style choice, a pre-existing flaw, or a "could be stronger" is NOT grounds to reject. Quote your evidence before you decide; keep reasoning to those quotes only.

**Draft user prompt (v1):**
> `<previous_version>{champion}</previous_version>`
> `<candidate>{revision}</candidate>`
> `<target_flaw>{the one flaw this revision targets}</target_flaw>`
> `<task>` Judge ONLY the difference. Step 1 — quote the sentence(s) in `<candidate>` that address the target_flaw, and any sentence that introduces a NEW would-ship defect not in `<previous_version>`. Step 2 — ADMIT unless Step 1 found such a new defect of severity ≥ the target flaw's. `</task>`
> Return JSON: `{"evidence_resolves": str, "evidence_new_defect": str|null, "new_defect_severity": 1-5|null, "verdict": "ADMIT"|"REJECT", "reason": str}`

---

## Eval-driven protocol (how we know a recraft helped)

- **Metric: Cohen's κ + balanced accuracy** on the 61 labels — *not* a basket of r/ρ/τ/φ/MCC (on binary verdicts they collapse to one identical number; reporting several is false corroboration — Rao & Callison-Burch, arXiv:2606.00093).
- **The over-flag diagnostic: the κ–φ gap.** `|κ| ≤ |φ|`, equal only when the gate's positive-rate matches ground truth's. Our gate (≈94% flag-rate vs ≈18% true regression-rate) has κ far below φ; **closing the κ–φ gap is the literal target** of the recraft.
- **Train/test split** the 61; cap few-shots; resist adding an example per disagreement (overfitting a 61-item set is real). Final verdict comes on fresh problems, not these 61.
- **Don't trust the gate's self-confidence** as a materiality signal — judges are badly over-confident (ECE ~40 on JudgeBench, arXiv:2508.06225).
- This is also the R6 experiment: A/B the recrafted gate vs the static gate on the 61, sweeping the severity threshold (open question the literature can't answer for us).

## For the paper (per the standing "use these throughout" instruction)
- Methods: cite G-Eval (reasoning judges), CALM/the surveys (bias taxonomy), Rao & Callison-Burch (κ over a coefficient basket), PoLL (panels).
- Limitations: name the judge biases we inherit (position, verbosity, self-enhancement, **over-correction/leniency**, overconfidence) and the mitigations applied; report κ + balanced accuracy + the κ–φ gap; disclose that detection and gating required *opposite* reasoning regimes (a genuine, citable methods point).

## Annotated bibliography (strong → emerging)
- **STRONG / foundational.** Liu et al. 2023, *G-Eval*, EMNLP 2023 (arXiv:2303.16634) — CoT+form-filling judge, Spearman 0.514 (moderate). · Ye et al. 2024, *Justice or Prejudice? (CALM)*, ICLR 2025 (arXiv:2410.02736) — 12 quantified judge biases. · Li et al. 2024, *From Generation to Judgment* survey (arXiv:2411.16594) and Gu et al. 2024/25, *A Survey on LLM-as-a-Judge* (arXiv:2411.15594) — umbrella methods/limitations cites (distinct papers; don't conflate).
- **STRONG (math, safest to cite).** Rao & Callison-Burch, *Agreement Metrics for LLM-as-Judge* (arXiv:2606.00093) — report κ; the κ–φ gap = positive-rate drift. Provable 2×2 identities.
- **STRONG (on-point to our bug).** Jin & Chen 2026, *Systematic Overcorrection in Requirement-Conformance Judgement* (arXiv:2603.00539) + independent corroboration (arXiv:2508.12358) — explanation/detail → over-flagging.
- **MEDIUM (calibration).** arXiv:2508.06225 — judge overconfidence/ECE on JudgeBench (14 models).
- **EMERGING / cite-with-caution (single recent preprints).** arXiv:2605.23970 — structured-CoT amplifies cue dependence; "Proof-Before-Preference" evidence-lock. Promising, not settled.
- **VENDOR (authoritative for Claude, not independently benchmarked).** Anthropic docs: *Develop tests* (rubrics, empirical verdict, reason-then-discard), *XML tags*, *Chain-of-thought*, *Multishot* (3-5 examples), *Demystifying evals for AI agents*.
- **PRACTITIONER.** Hamel Husain (hamel.dev/blog — eval-driven / error-analysis-first; *referenced from our brief but not retrieved in this pass*), Eugene Yan (eugeneyan.com/writing/llm-evaluators), PoLL/juries (Verga et al. 2024).
- **REFUTED — do NOT cite this way:** "pairwise framing is inherently better-calibrated than absolute scoring" (killed 0-3 vs arXiv:2411.15594v6).

## Caveats
Several of the most on-point sources are very recent (2026) arXiv preprints, not peer-reviewed — the over-correction effect has two independent sources (solid); the evidence-lock/structured-CoT-harm specifics are single-study (emerging). G-Eval's 0.514 is moderate. Few-shot calibration is unstable. None of the assembled *specs* are themselves benchmarked end-to-end — that's what the n=61 A/B (R6) is for.
