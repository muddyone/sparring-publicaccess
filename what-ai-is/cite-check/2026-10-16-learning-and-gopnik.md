# cite-check report — learning-and-gopnik

**Source:** `learning-and-gopnik.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **16** citations checked
- existence independently confirmed: **5**
- application evidence-grounded: **10**
- application judged from model knowledge only: **2**
- not independently checkable: **4**
- buckets — clean **2** · problem **15** · disagree **2**

## ⛔ DISAGREE — escalate to human (2)
### c05 — exists SPLIT · applied ✅  · ⚑ degraded  (line 139)
_proceduralization, Anderson's ACT-R_
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=verified [model_knowledge_only] — Lookup returned no match (irrelevant Crossref hit), but Anderson's ACT-R and proceduralization are well-established in cognitive science and the claim is accurately attributed.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The Crossref lookup did not retrieve evidence for Anderson's ACT-R, only an unrelated result, so existence is not established from the supplied evidence. From general model knowledge, ACT-R is associated with Anderson and with proceduralization/production compilation, but no retrieved source text supports it here.

### c18 — exists SPLIT · applied ☐  (line 251)
_Buchsbaum, Bridgers, Weisberg & Gopnik 2012._
- **escalate:** existence: nuance vs unchecked
- claude: exists=nuance applied=unchecked [no_basis] — Crossref returned no match, but Buchsbaum, Bridgers, Weisberg & Gopnik 2012 ('The power of possibility: causal learning, counterfactual reasoning, and pretend play') is a real and well-known paper; no claim attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Crossref lookup returned no match, and no other retrieved evidence confirms the Buchsbaum, Bridgers, Weisberg, and Gopnik 2012 work. No specific claim is attached to this entry beyond the note that another article builds on it.

## ⚠️ AGREE-problem (15)
### c01 — exists ☐ · applied ☐  (line 20)
_Alison Gopnik's May 2026 interview with Chris Hayes ([Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f))_
- claude: exists=unchecked applied=unchecked [no_basis] — URL returned HTTP 403, no metadata retrieved; cannot verify the podcast interview exists or supports the claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Pocket Casts URL could not be checked because the fetch returned HTTP 403. No episode text or metadata was retrieved to assess the interview-content claim.

### c02 — exists ✅ · applied ⚠️  (line 45)
_In Edward Tolman's classic maze studies, rats that explored without any reward learned the layout and only showed it once food appeared ([Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm))_
- claude: exists=verified applied=verified [evidence_text] — The classic Tolman 1948 paper resolves and matches; the full-text confirms the maze studies, and latent-learning (unrewarded exploration) is the well-known content of this paper.
- gpt: exists=verified applied=nuance [evidence_text] — The PsychClassics page identifies Tolman's 1948 'Cognitive Maps in Rats and Men' as first published in Psychological Review 55(4), 189-208. The retrieved snippet confirms the paper discusses rat maze experiments, but the excerpt provided does not itself show the specific no-reward/food-introduction latent-learning result.

### c03 — exists ✅ · applied ⚠️  (line 56)
_Her published work makes the case more carefully ([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/))_
- claude: exists=verified applied=nuance [evidence_text] — The paper exists and supports the cultural-technology/imitation framing and blicket/innovation contrasts; however, the precise numerical figures (85%, GPT-4 76%, Claude 58%) are not confirmed by the retrieved snippet, and the author note flags these were checked separately.
- gpt: exists=verified applied=nuance [evidence_text] — The PMC page confirms the article title, authors, journal, and DOI metadata for Yiu, Kosoy, and Gopnik. The retrieved text supports the broad children-versus-AI framing but does not include the detailed experimental percentages and task-specific results listed in the claims.

### c06 — exists ⚠️ · applied ⚠️  · ⚑ degraded  (line 145)
_([McClelland, McNaughton & O'Reilly 1995](https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf))_
- claude: exists=verified applied=verified [model_knowledge_only] — The McClelland, McNaughton & O'Reilly 1995 CLS paper is confirmed by the resolving PDF and Crossref title/author match; the fast-hippocampus/slow-neocortex replay claim is the core thesis (PDF was binary so content judged from knowledge).
- gpt: exists=nuance applied=nuance [evidence_text] — The PDF URL resolves and Crossref finds a closely related later version with matching authors and expanded title, but the retrieved metadata does not directly confirm the 1995 Psychological Review article details. The evidence supports the general complementary-learning-systems topic, but the supplied readable text does not substantiate the specific replay-and-weight-change claim.

### c07 — exists ☐ · applied ☐  (line 152)
_How much each version builds on the previous one's weights is not published (unconfirmed)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked deliberately uncited and not a citation; both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as deliberately uncited and unconfirmed. No citation evidence is provided to verify either existence or application.

### c08 — exists ☐ · applied ☐  (line 165)
_([McGill, The Neuro](https://www.mcgill.ca/neuro/node/3007))_
- claude: exists=unchecked applied=unchecked [no_basis] — The McGill URL returned HTTP 404; cannot verify this specific page or its support for the H.M. mirror-tracing claim from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The McGill URL returned HTTP 404, so the cited web page was not checked. No retrieved source text supports the H.M. mirror-tracing claim for this citation.

### c09 — exists ☐ · applied ☐  (line 181)
_The explainer also carried a diagram, "How your assistant learns · notes, nightly tidy-up, new versions". It lives in the working document and was not brought in._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked deliberately uncited and not a citation; both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as deliberately uncited and refers to an internal diagram not provided. There is no evidence to assess existence or application.

### c11 — exists ☐ · applied ☐  (line 225)
_Her published results are from 2023 models. No newer results on the same tasks have been found._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked deliberately uncited and not a citation; both axes unchecked.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is deliberately uncited and reports that no newer results were found. No source evidence is supplied for either axis.

### c12 — exists ✅ · applied ☐  (line 236)
_[Clark & Chalmers 1998](https://en.wikipedia.org/wiki/Extended_mind_thesis). Andy Clark and David Chalmers, "The Extended Mind," _Analysis_ 58. Linked to an overview; the paper is [doi:10.1093/analys/58.1.7](https://doi.org/10.1093/analys/58.1.7)._
- claude: exists=verified applied=unchecked [no_basis] — DOI resolves directly to Clark & Chalmers, Analysis 58(1), 7-19, 1998, confirming existence; no specific claim is attached to this reference entry.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly confirms Clark and Chalmers, 'The Extended Mind,' Analysis 58(1), 7-19, DOI 10.1093/analys/58.1.7. No specific claim is attached to this bibliography-only entry, so application cannot be assessed.

### c13 — exists ☐ · applied ☐  (line 239)
_[Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f). "The AI End Game: Two-Year-Olds vs. AI with Alison Gopnik," _Why Is This Happening?_, 19 May 2026._
- claude: exists=unchecked applied=unchecked [no_basis] — Podcast URL returned HTTP 403 and name lookup inconclusive; cannot verify this episode exists from evidence. No specific claim attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Pocket Casts fetch returned HTTP 403 and the other lookup was inconclusive, so the podcast episode is not verified from the evidence. No claim is attached to this bibliography-only entry.

### c14 — exists ⚠️ · applied ☐  (line 242)
_[McClelland, McNaughton & O'Reilly 1995](https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf). "Why There Are Complementary Learning Systems in the Hippocampus and Neocortex," _Psychological Review_ 102._
- claude: exists=verified applied=unchecked [no_basis] — The McClelland et al. 1995 paper is confirmed by resolving PDF and Crossref title/author match; no specific claim attached to this reference entry.
- gpt: exists=nuance applied=unchecked [no_basis] — The URL resolves and Crossref finds a closely related later publication with the same authors and expanded title, but the supplied metadata does not directly verify the 1995 Psychological Review citation. No specific claim is attached to this bibliography-only entry.

### c15 — exists ☐ · applied ☐  (line 245)
_[McGill, The Neuro](https://www.mcgill.ca/neuro/node/3007). Brenda Milner and patient H.M.'s mirror-tracing results._
- claude: exists=unchecked applied=unchecked [no_basis] — McGill URL returned HTTP 404; cannot verify the page from evidence. No specific claim attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited McGill URL returned HTTP 404, so the web item could not be checked. No specific claim is attached to this bibliography-only entry.

### c16 — exists ✅ · applied ☐  (line 247)
_[Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm). Edward C. Tolman, "Cognitive Maps in Rats and Men," _Psychological Review_ 55._
- claude: exists=verified applied=unchecked [no_basis] — The Tolman 1948 Psychological Review 55 paper is confirmed by the resolving full-text page; no specific claim attached to this reference entry.
- gpt: exists=verified applied=unchecked [no_basis] — The PsychClassics page confirms Tolman's 1948 'Cognitive Maps in Rats and Men' and states it was first published in Psychological Review 55(4), 189-208. No specific claim is attached to this bibliography-only entry.

### c17 — exists ✅ · applied ☐  (line 249)
_[Wente, Gopnik et al. 2022](https://sites.brown.edu/cocodevlab/files/2023/03/Causal-learning-counterfactual-reasoningand-pretend-play.pdf). "Causal learning, counterfactual reasoning and pretend play: a cross-cultural comparison." Builds on Buchsbaum, Bridgers, Weisberg & Gopnik 2012._
- claude: exists=verified applied=unchecked [no_basis] — The Wente & Gopnik 2022 paper is confirmed via Crossref and resolving PDF; no specific claim attached to this reference entry.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the 2022 Wente, Gopnik, Fernández Flecha, Garcia, and Buchsbaum article with matching title substance and DOI. No specific claim is attached to this bibliography-only entry.

### c19 — exists ✅ · applied ☐  (line 252)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/). "Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet)," _Perspectives on Psychological Science_ 19._
- claude: exists=verified applied=unchecked [no_basis] — The Yiu, Kosoy & Gopnik 2023 paper is fully confirmed via Crossref (DOI, volume, pages) and resolving PMC page; no specific claim attached to this reference entry.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and PMC confirm the Yiu, Kosoy, and Gopnik article, including title, journal, volume/issue, pages, year, and DOI. No specific claim is attached to this bibliography-only entry.

## ✅ AGREE-clean (2)
### c04 — exists ✅ · applied ✅  (line 134)
_([Clark & Chalmers 1998](https://en.wikipedia.org/wiki/Extended_mind_thesis))_
- claude: exists=verified applied=verified [evidence_text] — The Clark & Chalmers 1998 Extended Mind thesis is confirmed via the Wikipedia overview; the Otto's-notebook argument that a reliably consulted note functions as memory is the central example of this work.
- gpt: exists=verified applied=verified [evidence_text] — The retrieved overview states that Clark and Chalmers proposed the extended mind thesis in their 1998 paper 'The Extended Mind.' It also says external information-storing objects such as diaries can be part of cognitive processes, supporting the notebook-as-memory application, though the citation links an overview rather than the original paper.

### c10 — exists ✅ · applied ✅  (line 210)
_([Wente, Gopnik et al. 2022](https://sites.brown.edu/cocodevlab/files/2023/03/Causal-learning-counterfactual-reasoningand-pretend-play.pdf))_
- claude: exists=verified applied=verified [evidence_text] — The Wente & Gopnik 2022 paper is confirmed via Crossref and resolving PDF; the abstract directly supports the claim linking children's pretend play to counterfactual/causal reasoning.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the 2022 article with matching authors, title, journal, and DOI. The abstract explicitly links pretend play with causal inference and counterfactual reasoning, supporting the claim.

---

## Addendum: hand verification, 2026-10-16

Run after the automated check, against full texts, for the claims it could not reach.

| Claim | Source checked | Result |
|---|---|---|
| Children chose the functional object ~85% (c03) | Yiu, Kosoy & Gopnik 2023, full text via Europe PMC (PMC11373165) | Confirmed: M children = 85.2%, averaged across tool scenarios; the compass/teapot case is the paper's example |
| GPT-4 76%, Claude 58% (c03) | same | Confirmed: GPT-4 75.9%, Claude 58.16% |
| "The 2023 models more often picked the ruler" (c03) | same | **Overstated.** GPT-4 and Claude chose the functional object most of the time; two of five models (davinci 8.87%, Flan 45.7%) fell below half. Synthesis corrected. |
| Blicket: 4-year-olds learned from a handful of tries; LLMs did not (c03) | same | Confirmed: "only a handful of observations"; "LLMs did not produce the correct causal overhypotheses" |
| Tolman: unrewarded rats learned the layout (c02) | Tolman 1948, full text at psychclassics.yorku.ca | Confirmed: latent-learning experiments (Blodgett 1929) are the paper's first group |
| H.M. mirror drawing over three days (c08) | McGill link returned 404; replaced with Squire 2009, _Neuron_ 61, full text via NCBI (PMC2649674) | Confirmed: star traced in a mirror, "excellent retention across 3 days", no recollection; surgery in 1953 |
| ACT-R, proceduralization (c05) | Anderson 1982, _Psychological Review_ 89, doi:10.1037/0033-295X.89.4.369 (Crossref) | Exists; citation added |
| Buchsbaum et al. 2012 (c18) | doi:10.1098/rstb.2012.0122 (Crossref) | Exists; DOI added |
| McClelland, McNaughton & O'Reilly 1995 (c06, c14) | doi:10.1037/0033-295X.102.3.419 (Crossref) | Exists, _Psychological Review_ 102; DOI added |
| Hayes 2026 interview (c01, c13) | Pocket Casts returns 403 to automated fetches | **Unchecked.** No claim in the synthesis rests on it alone. |
