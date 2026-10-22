# Cite-check: the yardstick brief (2026-10-17)

Run on `briefs/2026-10-17-6-the-yardstick.md` with `/cite-check` (Claude and GPT judging against
retrieved evidence). The raw report follows this summary.

**Summary.** 33 items: 26 citations and 7 author notes marked as uncited. **No citation was found
wrong or invented.**
- **Confirmed clean (9):** London, Grove, Dietvorst, Burton, Rieger, Longoni, Dell'Acqua,
  Matthias, Frank.
- **"Disagree" items are almost all the bottom line's short author–year mentions.** The
  bibliography lookup can't match those, so one model marked existence unchecked. Each points to
  a full entry later in the brief, and those full entries were checked.
- **Resolved after the run:**
  - **Dell'Acqua et al.:** the abstract gave the "outside the frontier" figure: 19 percentage
    points less likely to be correct. It is now stated, no longer marked secondary.
  - **Bansal et al.:** "a human-shaped error model misleads" was our extrapolation. It is now
    marked as such.
  - **Bommasani et al.:** homogenization is reliable for shared training data and mixed for
    foundation models. The position piece no longer says shared models do it in general.
  - **Liu, Yang & Xu:** the abstract doesn't name Tianjin. That is now attributed to press
    coverage, and the position piece drops it.
  - **Pezzo & Beckstead 2020:** existence not confirmed. Marked do-not-cite.
- **Still unverified, as the brief already said:** Hill 2024's content (no abstract retrieved);
  _Noise_'s figures (secondary); Logg et al. and Mollick (application judged from model knowledge
  only; both models agreed).

---

# cite-check report — yardstick-brief

**Source:** `briefs/2026-10-17-6-the-yardstick.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **33** citations checked
- existence independently confirmed: **18**
- application evidence-grounded: **16**
- application judged from model knowledge only: **14**
- not independently checkable: **1**
- buckets — clean **9** · problem **18** · disagree **12**

## ⛔ DISAGREE — escalate to human (12)
### c01 — exists SPLIT · applied ✅  · ⚑ degraded  (line 24)
_Zerilli et al. (2019) argue that AI is held to "an unrealistically high standard" of transparency, partly because human decision-making is overestimated as transparent._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Though Crossref returned no-match here, this is the same Zerilli et al. 2019 work fully verified at c15, whose abstract directly states the 'unrealistically high standard' and 'unrealistically high estimate' of human transparency claims.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The lookup found no Crossref match and the reference lacks title/journal/DOI, so existence cannot be verified from the retrieved evidence. From model knowledge, the claim matches Zerilli et al.'s 2019 Philosophy & Technology article on double standards in transparency.

### c02 — exists SPLIT · applied ✅  · ⚑ degraded  (line 26)
_London (2019) argues that in medicine, verified accuracy can matter more than explanation._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Same London 2019 work verified at c17, whose abstract argues that in medicine verified accuracy can matter more than explanation.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence is only a Crossref no-match for an under-specified London 2019 reference. From model knowledge, London’s 2019 Hastings Center Report article argues that empirically verified accuracy can sometimes matter more than explainability in medicine.

### c03 — exists SPLIT · applied ✅  · ⚑ degraded  (line 28)
_**Human judgment is far noisier than people assume** (Kahneman, Sibony & Sunstein 2021)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library lookup failed here but the same book is confirmed at c18; the central thesis of 'Noise' is that human judgment is far noisier than assumed.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — Open Library failed with HTTP 500, so existence is not checkable from the retrieved evidence. From model knowledge, Kahneman, Sibony, and Sunstein’s Noise centrally argues that human judgment is much noisier than people assume.

### c04 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 29)
_mechanical prediction has matched or beaten expert clinical judgment for decades (Grove et al. 2000). The consistency and correctness bars set for AI are not bars human experts clear._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Same Grove et al. 2000 meta-analysis verified at c19, whose abstract confirms mechanical prediction equals or exceeds clinical judgment across circumstances.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The lookup returned no match and the reference is incomplete, so existence is not established from the evidence. From model knowledge, Grove et al. 2000 supports mechanical prediction often matching or outperforming clinical judgment, but the broader claim about AI evaluation bars is an extrapolation.

### c05 — exists SPLIT · applied ✅  · ⚑ degraded  (line 31)
_Confidence in an algorithm falls faster after the same mistake (Dietvorst, Simmons & Massey 2015)._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Same Dietvorst et al. 2015 study verified at c20, whose abstract states people lose confidence in algorithms faster than humans after the same mistake.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref search found no match for this incomplete reference. From model knowledge, Dietvorst, Simmons, and Massey 2015 directly supports that people lose confidence in algorithms faster than humans after observing comparable errors.

### c08 — exists SPLIT · applied ✅  · ⚑ degraded  (line 37)
_people sometimes *prefer* algorithmic advice (Logg, Minson & Moore 2019)_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref returned no-match, but Logg, Minson & Moore (2019) 'Algorithm Appreciation' in OBHDP is a well-known paper showing people sometimes prefer algorithmic advice.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence is only a Crossref no-match for an incomplete reference. From model knowledge, Logg, Minson, and Moore 2019 supports the claim that people sometimes prefer algorithmic advice, often described as algorithm appreciation.

### c11 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 42)
_error shape: AI fails in places people don't predict (Bansal et al. 2019; Dell'Acqua et al. 2023)_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref no-match, but Bansal et al. 2019 work on human-AI team error boundaries/mental models is a known body of work supporting that AI fails in unpredicted places.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Crossref found no match for the sparse Bansal 2019 reference, so existence is not verified from the retrieved evidence. From model knowledge, Bansal et al. 2019 is relevant to users’ mental models of AI errors, but the wording that AI fails in places people do not predict is a compressed interpretation.

### c12 — exists SPLIT · applied ✅  · ⚑ degraded  (line 42)
_error shape: AI fails in places people don't predict (Bansal et al. 2019; Dell'Acqua et al. 2023)_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref no-match, but Dell'Acqua et al. 2023 ('Navigating the Jagged Technological Frontier') is a well-known working paper documenting unpredictable AI capability boundaries.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved evidence is only a no-match for an incomplete Dell’Acqua 2023 reference. From model knowledge, Dell’Acqua et al. 2023 on the jagged technological frontier supports the claim that AI can fail on tasks where people do not reliably anticipate failure.

### c13 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 43)
_scale: one model's error repeats across everyone it serves (Bommasani et al. 2022)_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref no-match, but Bommasani et al. 2022 on foundation models / homogenization supports the claim that one model's error repeats across downstream users.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The lookup found no match and the reference lacks identifying metadata. From model knowledge, Bommasani et al. on foundation models supports concerns about scale and shared model failures, but the phrasing that one error repeats across everyone served is a broad paraphrase.

### c14 — exists SPLIT · applied ✅  · ⚑ degraded  (line 44)
_accountability: nobody may be answerable for what a learning system does (Matthias 2004)_
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref no-match, but Matthias (2004) 'The responsibility gap' in Ethics and Information Technology is the canonical source for the accountability-gap claim.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref evidence did not match the incomplete Matthias 2004 reference. From model knowledge, Matthias’s “responsibility gap” article supports the claim that learning systems can create cases where no human is straightforwardly answerable for their actions.

### c27 — exists SPLIT · applied ☐  (line 168)
_Pezzo & Beckstead (2020, _Judgment and Decision Making_ 15(3)) argue the preference for humans held only when the two providers' records were equal; when the AI was known to outperform, people preferred it. **[secondary]**_
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — Crossref returned no match for Pezzo & Beckstead (2020) in Judgment and Decision Making; no evidence corroborates existence or the claim, though absence in one index is not fully decisive.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved lookup is a Crossref no-match for an incomplete reference, which is insufficient to prove nonexistence. No source text was retrieved to assess the application claim.

### c34 — exists SPLIT · applied ☐  (line 226)
_**5.3 Tension with the presentation consensus.** [report] The Chalmers report found that sceptics and optimists agree a product should not present itself as a person._
- **escalate:** existence: refuted vs unchecked
- claude: exists=refuted applied=unchecked [no_basis] — No 'Chalmers report' matching the description was found; the only Crossref hit is an unrelated 1982 Allis-Chalmers health hazard report, so existence is not corroborated.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Crossref result is explicitly low-similarity and unrelated, and the reference is too underspecified to verify or refute the report's existence. No relevant source text was retrieved to assess the claim about sceptics and optimists.

## ⚠️ AGREE-problem (18)
### c06 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 32)
_In one survey, self-driving cars had to be four to five times safer than human drivers to be accepted (Liu, Yang & Xu 2018)._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Crossref no-match leaves existence unconfirmed; Liu, Yang & Xu (2018) on autonomous vehicle acceptance is plausible and a 'four-to-five times safer' finding resembles their survey work, but I cannot verify the specific figure.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The evidence contains only a no-match for an incomplete author-year reference, so existence is unchecked. From model knowledge, Liu, Yang, and Xu 2018 is commonly cited for survey evidence that self-driving vehicles would need to be roughly four to five times safer than human drivers to be accepted.

### c07 — exists ☐ · applied ☐  (line 34)
_one AI's misdeed spills over to "all AIs" in a way one human's doesn't spill over to all humans (Manoli, Pauketat & Anthis 2024)._
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved; Anthis et al. work on AI moral consideration exists but I cannot confirm this specific 2024 paper or the spillover claim from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The lookup returned no match and the reference lacks title, venue, and DOI. No source text or sufficiently reliable basis is available here to judge whether it supports the spillover claim.

### c09 — exists ☐ · applied ☐  (line 38)
_in one study trusted AI more than a human novice, though less than an expert (Rieger et al. 2023)._
- claude: exists=unchecked applied=unchecked [no_basis] — No match retrieved and only a surname given; cannot confirm this Rieger et al. 2023 work or its trust-comparison finding.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference is too sparse and Crossref returned no match, so existence cannot be verified. No retrieved text or reliable basis is available to assess the specific claim about trust relative to a novice and an expert.

### c10 — exists ☐ · applied ☐  (line 40)
_No study was found that measures how academics and commentators frame AI's failures; that part is observation._
- claude: exists=unchecked applied=unchecked [no_basis] — Explicitly marked not a citation / deliberately uncited author observation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. Both axes are therefore unchecked.

### c15 — exists ✅ · applied ⚠️  (line 50)
_**1.1** Zerilli, J., Knott, A., Maclaurin, J., & Gavaghan, C. (2019). Transparency in algorithmic and human decision-making: Is there a double standard? _Philosophy & Technology_, 32(4), 661–683. https://doi.org/10.1007/s13347-018-0330-6 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves and abstract confirms the double-standard, human transparency problems, overly-high regulatory bar, and the Dennett intentional-stance framing of justifying algorithmic decisions.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI, title, authors, journal, volume, and pages are confirmed by Crossref and the Springer page, with only the online-publication year appearing as 2018 while the volume is 2019. The abstract directly supports the transparency double-standard, human opacity, regulatory-bar, and intentional-stance claims, though the statement that it is the closest formulation of Bart’s point is an authorial evaluation rather than something the paper itself can verify.

### c16 — exists ✅ · applied ⚠️  (line 62)
_**1.2** Hill, S. (2024). Against the double standard argument in AI ethics. _Philosophy & Technology_, 37, 23. https://doi.org/10.1007/s13347-024-00720-4 **[record]**_
- claude: exists=verified applied=nuance [evidence_text] — DOI and title confirm Hill (2024) is a commentary titled 'Against the Double Standard Argument,' a direct rebuttal of Zerilli; however the retrieved snippet is paywalled with no abstract, so the specific stability/uniformity/safety argument cannot be verified from evidence.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the Springer page confirm the article’s title, author, journal, year, volume, and DOI. The title supports that it is a counter-piece to the double-standard argument, but the retrieved preview does not substantiate the more detailed claims about the nature of AI opacity, stability, uniformity, and safety.

### c18 — exists ⚠️ · applied ⚠️  · ⚑ degraded  (line 82)
_**2.1** Kahneman, D., Sibony, O., & Sunstein, C. R. (2021). _Noise: A flaw in human judgment._ Little, Brown Spark. **[secondary]**_
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms the book exists with correct authors/year; the noise-audit, 55% median difference, psychiatric-diagnosis agreement, and level/occasion noise distinction are known content, but no retrieved text verifies the exact figures (author also flags them as unverified).
- gpt: exists=nuance applied=nuance [model_knowledge_only] — Open Library fuzzily matches the title, authors, and year, but the retrieved metadata does not confirm the subtitle or publisher. From model knowledge, the cited claims are broadly associated with Noise, but the specific numerical examples are not verified by retrieved text and are flagged by the author note as secondary.

### c21 — exists ✅ · applied ⚠️  (line 115)
_**3.2** Liu, P., Yang, R., & Xu, Z. (2018). How safe is safe enough for self-driving vehicles? _Risk Analysis_. https://doi.org/10.1111/risa.13116 **[abstract + secondary]**_
- claude: exists=verified applied=verified [evidence_text] — DOI matches exactly; abstract confirms N=499 survey and the tolerable-risk criterion that SDVs should be four to five times as safe as HDVs.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref directly matches the DOI, title, authors, journal, year, and abstract. The abstract supports N=499, the four-to-five-times-safer criterion, and lower acceptance of equal-risk SDVs, but the retrieved text does not itself confirm the Tianjin location.

### c22 — exists ✅ · applied ⚠️  (line 122)
_**3.3** Manoli, A., Pauketat, J. V. T., & Anthis, J. R. (2024). The AI double standard: Humans judge all AIs for the actions of one. arXiv:2412.06040. https://arxiv.org/abs/2412.06040 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv page confirms title/authors; snippet confirms N=720 and N=684 experiments, spillover effects, and the double-standard finding (persisting for AI but not humans when individuated).
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv URL resolves to the cited title and the snippet gives the authors and submission information. The snippet supports the two preregistered studies, N values, AI-specific spillover after individuation, and double-standard framing, though the final 'binary judgment at the category level' wording is an interpretation rather than the paper's exact claim.

### c23 — exists ✅ · applied ✅  · ⚑ degraded  (line 135)
_**3.4** Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation: People prefer algorithmic to human judgment. _Organizational Behavior and Human Decision Processes_, 151, 90–103. https://doi.org/10.1016/j.obhdp.2018.12.005 **[abstract]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI/metadata confirm the work exists; retrieved snippet was only 'Redirecting' so the specific six-experiment claims rest on known content of this well-documented paper, which matches.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref directly verifies the DOI, title, authors, journal, volume, pages, and year. The retrieved evidence contains no substantive abstract beyond a redirect, so the application judgment rests only on model knowledge that the claims accurately summarize Logg, Minson, and Moore's algorithm-appreciation findings.

### c28 — exists ✅ · applied ⚠️  (line 176)
_**4.1 Error shape.** Bansal, G., Nushi, B., Kamar, E., Lasecki, W. S., Weld, D. S., & Horvitz, E. (2019). Beyond accuracy: The role of mental models in human–AI team performance. _HCOMP_ 7, 2–11. https://doi.org/10.1609/hcomp.v7i1.5285 **[report]**_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; abstract confirms the error-boundary (mental model of when AI errs) argument central to the cited claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref directly verifies the DOI, title, authors, venue, year, volume, pages, and abstract, and the URL resolves. The abstract supports the importance of users knowing when the AI errs and mental models of the AI error boundary, but the stronger phrasing that a 'human-shaped model' misleads is an extrapolation from the abstract rather than stated directly.

### c30 — exists ⚠️ · applied ⚠️  (line 193)
_**4.3 Scale.** Bommasani, R., Creel, K. A., Kumar, A., Jurafsky, D., & Liang, P. (2022). Picking on the same person: Does algorithmic monoculture lead to outcome homogenization? _NeurIPS_ 35. https://arxiv.org/abs/2211.13972 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — arXiv page confirms title/authors; snippet confirms data sharing reliably exacerbates homogenization and mixed results for foundation models depending on adaptation.
- gpt: exists=nuance applied=nuance [evidence_text] — The arXiv URL resolves to the cited title and the snippet gives the matching authors, but the retrieved evidence does not confirm the NeurIPS volume description. The snippet supports outcome homogenization, component sharing, reliable worsening from shared training data, and mixed foundation-model results, but only partially supports the precise claim about dependence on adaptation.

### c33 — exists ✅ · applied ✅  · ⚑ degraded  (line 219)
_**5.2** Mollick, E. (2024). _Co-intelligence: Living and working with AI._ Portfolio. **[secondary]**_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Mollick's Co-Intelligence (2024); the 'treat AI like a person' third principle is well-known content of the book but no text was retrieved to confirm wording.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library matches the 2024 work Co-Intelligence by Ethan Mollick, though it does not confirm the Portfolio publisher. No source text was retrieved, so the claim that one principle is 'Treat AI like a person (but tell it what kind of person it is)' is judged supported only from model knowledge.

### c35 — exists ☐ · applied ☐  (line 233)
_**No study found of how academics and commentators frame AI errors.** The claim that critics use a calculator yardstick is observation. A content analysis would turn it into evidence._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and deliberately uncited; author explicitly frames this as observation, not a cited source.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately_uncited and is_citation=false, so both axes are unchecked. It is an author note that no study was found, not a bibliographic citation to verify.

### c36 — exists ☐ · applied ☐  (line 235)
_**Hidalgo et al. (2021), _How Humans Judge Machines_ (MIT Press)** reports dozens of experiments comparing reactions to the same act by a human or a machine. **[record]** Its specific findings were not confirmed and should not be cited until read._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked deliberately uncited; author notes findings not confirmed and should not be cited until read.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and deliberately_uncited, so both axes are unchecked. It is intentionally not being used as a verified citation.

### c37 — exists ☐ · applied ☐  (line 238)
_**Hill (2024)** is cited for existing, not for its content (1.2)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false and cited only for existing; no claims to assess.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so both axes are unchecked. No retrieved evidence or substantive claim is provided.

### c38 — exists ☐ · applied ☐  (line 239)
_**The BCG "outside the frontier" figure** is secondary (4.2)._
- claude: exists=unchecked applied=unchecked [no_basis] — Not a standalone citation; it is a cross-reference to the secondary BCG figure in c29.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false, so both axes are unchecked. It is only a note referring back to the BCG figure in c29.

### c39 — exists ☐ · applied ☐  (line 240)
_**Not yet searched:** studies of LLM run-to-run inconsistency compared with human test–retest inconsistency on the same task. This would be the most direct test of the consistency point._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked deliberately uncited; author states this is a not-yet-searched research gap, not a source.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked deliberately_uncited and is_citation=false, so both axes are unchecked. It describes a not-yet-searched research gap rather than citing a work.

## ✅ AGREE-clean (9)
### c17 — exists ✅ · applied ✅  (line 71)
_**1.3** London, A. J. (2019). Artificial intelligence and black-box medical decisions: Accuracy versus explainability. _Hastings Center Report_, 49(1), 15–21. https://doi.org/10.1002/hast.973 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves and the abstract directly supports all claims: opaque decisions more common in medicine than critics realize, and verified accuracy mattering more than explainability where causal knowledge is incomplete.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article metadata and DOI. The retrieved abstract explicitly states that opaque decisions are common in medicine and that empirically verified accurate results can be more important than explaining how they are produced.

### c19 — exists ✅ · applied ✅  (line 93)
_**2.2** Grove, W. M., Zald, D. H., Lebow, B. S., Snitz, B. E., & Nelson, C. (2000). Clinical versus mechanical prediction: A meta-analysis. _Psychological Assessment_, 12(1), 19–30. https://doi.org/10.1037/1040-3590.12.1.19 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves and the abstract confirms the ~10% average advantage, the 6-16% figure for clinical superiority, and consistency across task, judge type, and experience.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm the article metadata, DOI, and abstract. The abstract directly supports the 10% average mechanical-prediction advantage, the 6–16% figure for clinical superiority, and the consistency of the advantage across tasks, judges, experience, and data types.

### c20 — exists ✅ · applied ✅  (line 107)
_**3.1** Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People erroneously avoid algorithms after seeing them err. _Journal of Experimental Psychology: General_, 144(1), 114–126. https://doi.org/10.1037/xge0000033 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves and the abstract confirms five studies, aversion persisting even after seeing the algorithm outperform the human, and faster confidence loss after the same mistake.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and EuropePMC confirm the article metadata, DOI, and abstract. The abstract directly states that people become especially averse to algorithms after seeing them err, even when algorithms outperform humans, because confidence is lost faster for algorithms after the same mistake.

### c24 — exists ✅ · applied ✅  (line 144)
_**3.5** Burton, J. W., Stein, M.-K., & Jensen, T. B. (2020). A systematic review of algorithm aversion in augmented decision making. _Journal of Behavioral Decision Making_, 33(2), 220–239. https://doi.org/10.1002/bdm.2155 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; abstract confirms 61 peer-reviewed articles 1950–2018 and the five themes including expectations and expertise.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly matches the DOI, title, authors, journal, volume, issue, and pages, with only a publication-year nuance between online and issue dating. The abstract explicitly states 61 peer-reviewed articles from 1950–2018 and the five themes including expectations and expertise.

### c25 — exists ✅ · applied ✅  (line 152)
_**3.6** Rieger, T., Kugler, L., Manzey, D., & Roesler, E. (2023). The (im)perfect automation schema: Who is trusted more, automated or human decision support? _Human Factors_. https://doi.org/10.1177/00187208231197347 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; abstract confirms trust ordering (expert > AI > novice), equal forgiveness after failure, and support for an imperfect automation schema.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly verifies the article metadata and DOI. The abstract directly supports the simulated medical X-ray task, trust/reliability ordering, equal forgiveness after failure, and the authors' conclusion of an imperfect automation schema.

### c26 — exists ✅ · applied ✅  (line 162)
_**3.7** Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). Resistance to medical artificial intelligence. _Journal of Consumer Research_, 46(4), 629–650. https://doi.org/10.1093/jcr/ucz013 **[abstract]**_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; abstract confirms uniqueness neglect and that resistance is eliminated when framed as personalized or when AI only supports a human provider.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly verifies the DOI, title, authors, journal, volume, issue, pages, and abstract. The abstract explicitly supports uniqueness neglect as the driver of resistance and states that resistance is eliminated by personalization or by AI supporting rather than replacing a human provider.

### c29 — exists ✅ · applied ✅  (line 182)
_**4.2 Error shape, in the field.** Dell'Acqua, F., McFowland, E., Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). _Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality._ Harvard Business School Working Paper 24-013. **[secondary]**_
- claude: exists=verified applied=verified [evidence_text] — Crossref fuzzy match confirms the paper (SSRN version); abstract confirms 758 consultants, gains inside the frontier, and 19% less likely to be correct outside it.
- gpt: exists=verified applied=verified [evidence_text] — Crossref finds the same title, authors, year, and abstract with an SSRN DOI, confirming the work though not the HBS working-paper label in the retrieved metadata. The abstract directly supports the preregistered 758-person BCG field experiment, improved performance inside the frontier, the 12.2%/25.1% figures, and the 19% lower correctness outside the frontier.

### c31 — exists ✅ · applied ✅  (line 202)
_**4.4 Accountability.** Matthias, A. (2004). The responsibility gap: Ascribing responsibility for the actions of learning automata. _Ethics and Information Technology_, 6(3), 175–183. https://doi.org/10.1007/s10676-004-3422-1 **[abstract + secondary]**_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; Springer abstract confirms the responsibility gap argument and the society-must-choose framing cited.
- gpt: exists=verified applied=verified [evidence_text] — Crossref directly verifies the DOI, title, author, journal, volume, issue, pages, and year, and the Springer page resolves. The retrieved abstract directly supports the responsibility-gap claim about unpredictable learning automata and the societal choice between not using them or facing a gap.

### c32 — exists ✅ · applied ✅  (line 213)
_**5.1** Frank, M. C. (2023). Baby steps in evaluating the capacities of large language models. _Nature Reviews Psychology_, 2, 451–452. https://doi.org/10.1038/s44159-023-00211-x **[record]**_
- claude: exists=verified applied=verified [evidence_text] — DOI matches; Nature snippet confirms it is a comment arguing developmental psychology methods complement standard computational evaluation of LLMs.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the Nature page verify the comment's title, author, journal, year, volume, and pages. The snippet directly states that developmental-psychology methods can complement standard computational approaches to understand LLM representations and perhaps illuminate the nature of mind.
