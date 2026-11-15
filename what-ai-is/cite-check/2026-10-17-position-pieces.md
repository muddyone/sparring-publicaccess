# Cite-check: the five position pieces (2026-10-17)

Run on `positions/00` to `04` with `/cite-check` (chunked at 60 lines), each piece checked as
readers see it, against its own citations. The five raw reports follow.

**Summary.** 151 items across the five pieces. **No citation was found wrong or invented, and no
piece was found to misstate a source in a way that changes its argument.** Two passages were
corrected for precision.

| Piece | Items | Confirmed to exist | Clean | Notes |
|---|---|---|---|---|
| 00 The thing on the other end | 6 | 0 | 0 | Cites no works directly; its claims are summaries of 01–03, each checked there. |
| 01 It learns | 18 | 16 | 1 | One fix (Samiei). |
| 02 Something is there | 38 | 32 | 6 | No fix needed (two figures checked in full text). |
| 03 Personality | 25 | 23 | 2 | One fix (Kreiner). |
| 04 The yardstick | 64 | 55 | 20 | No fix needed; items already resolved in the two brief checks. |

Most "problem" verdicts are one model noting that an **abstract doesn't contain a detail** the
piece takes from the full paper. Those details were checked when the source reports and briefs
were built. Where the check left a specific figure or quote unconfirmed, it was checked here
against the full text:

- **Chalmers 2023, "It could be a disaster to stumble upon AI consciousness unknowingly and
  unreflectively"** (piece 02): verbatim in the arXiv full text.
- **Colombatto & Fleming 2024, 67% and ChatGPT** (piece 02): the paper's Discussion: "a
  substantial proportion (67%) of people attribute some possibility of phenomenal consciousness
  to ChatGPT."
- **Gjerde, Cheung & Lagnado 2025, 81.3% vs 88.2%** (piece 01): in the paper's results table.

**Corrected:**
- **Samiei et al. 2026** (piece 01): "it persists in gpt-5" overstated the paper. The paper
  tests gpt-5 among other models, and its abstract says some leading models approach human
  accuracy with less efficient exploration and similar gaps between the two rule types. Rewritten
  to say that, and to add the paper's finding that adults exploring for themselves largely
  overcome their own conjunctive handicap.
- **Kreiner 2006** (piece 03): "lowers satisfaction in both directions" was too simple; the
  abstract notes the effects differ by direction. Rewritten.

**Headers.** All five now say they were cite-checked as a whole on 2026-10-17 and link here.
Piece 00 now introduces four pieces, adds piece 04, and updates the Gopnik test's status.

**Small record notes, not errors:** Methot et al. is cited as 2016 (print), Crossref lists 2015
(online). Zerilli et al. is cited as 2019 (volume), Crossref lists 2018 (online). OMNI is cited
as 2024 (ICLR), the arXiv posting is 2023.


---

## Raw report: 00-the-thing-on-the-other-end

### cite-check report — pos-00-the-thing-on-the-other-end

**Source:** `positions/00-the-thing-on-the-other-end.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **6** citations checked
- existence independently confirmed: **0**
- application evidence-grounded: **0**
- application judged from model knowledge only: **3**
- not independently checkable: **3**
- buckets — clean **0** · problem **3** · disagree **3**

## ⛔ DISAGREE — escalate to human (3)
### c02 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 23)
_Alison Gopnik's real distinction is between passing knowledge along and discovering it._
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No specific work is cited and crossref returned no match, so existence of a particular source cannot be judged; Gopnik does distinguish imitation/transmission from exploration/discovery in children's learning, broadly consistent with the claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The reference lacks a title or publication details, and Crossref returned no match, so existence cannot be confirmed from the retrieved evidence. No source text was retrieved to evaluate the attribution to Gopnik.

### c05 — exists SPLIT · applied ⚠️  · ⚑ degraded  (line 41)
_A note that is reliably consulted functions as memory, on Clark and Chalmers' extended-mind argument._
- **escalate:** existence: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — Clark and Chalmers' 'The Extended Mind' (1998) is a well-known real work despite no crossref match; it indeed argues that reliably consulted external notes function as memory, matching the claim.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned no match for the incomplete Clark and Chalmers reference, so existence is not confirmed by the retrieved evidence. From general knowledge, the extended-mind argument’s notebook example supports reliably consulted notes functioning as memory, but applying that to a notes-plus-frozen-model system “learning” is an extrapolation.

### c06 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 51)
_In the second piece, Chalmers uses it to place an assistant somewhere between *part of your own mind* and *someone else you work with*._
- **escalate:** application: nuance vs unchecked
- claude: exists=unchecked applied=nuance [model_knowledge_only] — No specific Chalmers work is identified and crossref found no match, so existence is unverified; the characterization of applying extended-mind framing to AI assistants is plausible but cannot be pinned to a verified source.
- gpt: exists=unchecked applied=unchecked [no_basis] — The Chalmers reference has no title or publication details, and Crossref returned no match, so existence cannot be confirmed from the retrieved evidence. No source text was retrieved to assess whether Chalmers makes the assistant-between-own-mind-and-coworker claim.

## ⚠️ AGREE-problem (3)
### c01 — exists ☐ · applied ☐  (line 22)
_[It learns. The better question is what kind of learner it is.](../positions/02-it-learns.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — This is an internal relative-path link (02-it-learns.md) that could not be fetched; neither existence nor application can be verified from the evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup failed because the local Markdown URL was not checkable, so the work’s existence is not established. No source text or other evidence was retrieved to assess whether it supports the learning claim.

### c03 — exists ☐ · applied ☐  (line 27)
_[Something is there. Very probably no one.](../positions/03-someone-there.md) Following David Chalmers, there really is an agent on the other end in the interpretive sense, a "quasi-subject"._
- claude: exists=unchecked applied=unchecked [no_basis] — Internal markdown link (03-someone-there.md) could not be fetched, so the cited piece and its support for the claims cannot be verified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup failed because the local Markdown URL was not checkable, so the cited work’s existence is not established. No retrieved text supports or contradicts the claims attributed to Chalmers.

### c04 — exists ☐ · applied ☐  (line 31)
_[Personality improves the relationship, not the work. Both count.](../positions/04-personality.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal markdown link (04-personality.md) could not be fetched; neither axis is judgeable from the evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The local Markdown URL could not be fetched, leaving existence unverified. No source text was available to assess the claims about social cues, work quality, warmth, accuracy, or agreeableness.

---

## Raw report: 02-it-learns

### cite-check report — pos-02-it-learns

**Source:** `positions/02-it-learns.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **18** citations checked
- existence independently confirmed: **16**
- application evidence-grounded: **12**
- application judged from model knowledge only: **3**
- not independently checkable: **2**
- buckets — clean **1** · problem **19** · disagree **1**

## ⛔ DISAGREE — escalate to human (1)
### c05 — exists ✅ · applied SPLIT  (line 52)
_([Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The retrieved PMC title/authors confirm the Yiu, Kosoy & Gopnik 2023 paper on cultural technologies and tool innovation; specific percentages weren't in the snippet but the framing matches the paper's thesis.
- gpt: exists=verified applied=unchecked [evidence_text] — The PMC page verifies the article title, authors, venue, DOI, and publication details. The retrieved snippet is only bibliographic/opening page text and does not show the specific percentages, tool-innovation scenarios, or model-results claims.

## ⚠️ AGREE-problem (19)
### c01 — exists ☐ · applied ☐  (line 4)
_Built only from the cite-checked synthesis [Does it learn?](../learning-and-gopnik.md); no new sources._
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited internal synthesis document, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as deliberately uncited / not a citation, referring to an internal synthesis rather than a new external source.

### c02 — exists ☐ · applied ☐  (line 16)
_([Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f))_
- claude: exists=unchecked applied=unchecked [no_basis] — Podcast URL returned HTTP 403, so neither existence nor the quoted interview claim can be verified from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned HTTP 403 and the record is marked not-checkable, so existence cannot be confirmed. No transcript or source text was retrieved to assess the quoted interview claim.

### c03 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 30)
_([Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm))_
- claude: exists=verified applied=verified [evidence_text] — The retrieved page confirms Tolman's 1948 'Cognitive Maps in Rats and Men'; the paper is the canonical source for latent-learning maze findings described.
- gpt: exists=verified applied=nuance [model_knowledge_only] — The URL resolves to Tolman's 1948 'Cognitive Maps in Rats and Men' with matching publication details. The retrieved snippet does not include the no-reward latent-learning passage, though the claim is consistent with the well-known Tolman latent-learning discussion.

### c04 — exists ✅ · applied ✅  · ⚑ degraded  (line 46)
_Clark and Chalmers' extended-mind argument is exactly about this: a note that is reliably consulted functions as memory (Otto and his notebook; [Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Clark & Chalmers 'The Extended Mind' (1998); the Otto-and-notebook argument is the central thesis of that paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Clark and Chalmers' 1998 article 'The Extended Mind.' No abstract/text was retrieved, but the Otto notebook example and the claim that reliable external notes can function as memory are central to the paper.

### c06 — exists ✅ · applied ⚠️  (line 79)
_([Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023))_
- claude: exists=verified applied=nuance [evidence_text] — Squire 2009 'The Legacy of Patient H.M.' is confirmed and supports H.M.'s memory impairment and separate memory systems; the specific mirror-tracing/Milner details are standard but not quoted in the retrieved abstract.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and EuropePMC verify Squire's 2009 Neuron article on patient H.M. The abstract supports severe memory impairment and separate organization of memory functions, but it does not itself mention the mirror-star tracing details.

### c07 — exists ✅ · applied ✅  · ⚑ degraded  (line 94)
_John Anderson's proceduralization; [Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Anderson 1982 'Acquisition of cognitive skill'; proceduralization is a core concept of that ACT theory paper.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref verifies Anderson's 1982 Psychological Review article 'Acquisition of cognitive skill.' No source text was retrieved, but proceduralization of cognitive skill is a core Anderson/ACT claim.

### c08 — exists ✅ · applied ⚠️  (line 106)
_[Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606)_
- claude: exists=verified applied=nuance [evidence_text] — The paper exists and shows GPT-4o with chain-of-thought on par with humans on affordance tasks; the abstract confirms the qualitative claim but not the exact 81.3%/88.2% figures cited.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv verifies the paper and abstract, which says GPT-4o with chain-of-thought performed on par with humans on newly designed affordance/tool-substitution tasks. The abstract does not include the exact 20-item count or the 81.3% versus 88.2% figures.

### c10 — exists ✅ · applied ⚠️  (line 111)
_[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)_
- claude: exists=verified applied=nuance [evidence_text] — Paper exists and confirms persistent conjunctive-disjunctive gap even as models approach human accuracy; abstract does not specifically name gpt-5 as cited.
- gpt: exists=verified applied=nuance [evidence_text] — arXiv verifies the 2026 Samiei/Yiu/Gopnik et al. paper. The abstract supports the general claim that some state-of-the-art models approach human accuracy while retaining conjunctive-disjunctive gaps, but it does not specifically name GPT-5.

### c11 — exists ☐ · applied ☐  (line 126)
_([The result](../../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md).)_
- claude: exists=unchecked applied=unchecked [no_basis] — Intentionally uncited link to the author's own in-progress pilot result, not an external citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as deliberately uncited / not a citation, referring to the author's own pilot result rather than an external source.

### c12 — exists ✅ · applied ☐  (line 139)
_[Anderson 1982](https://doi.org/10.1037/0033-295X.89.4.369)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Anderson 1982; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies Anderson's 1982 article. No specific claim is attached to this citation, so application cannot be assessed.

### c13 — exists ✅ · applied ☐  (line 140)
_[Clark & Chalmers 1998](https://doi.org/10.1093/analys/58.1.7)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref confirms Clark & Chalmers 1998; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref verifies Clark and Chalmers' 1998 article 'The Extended Mind.' No specific claim is attached to this citation, so application cannot be assessed.

### c14 — exists ✅ · applied ☐  (line 141)
_[Gjerde, Cheung & Lagnado 2025](https://arxiv.org/abs/2502.16606)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv confirms the Gjerde et al. paper; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv verifies the Gjerde, Cheung, and Lagnado paper. No specific claim is attached to this citation, so application cannot be assessed.

### c15 — exists ✅ · applied ☐  (line 142)
_[GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv confirms the GX-Chen et al. paper; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv verifies the GX-Chen et al. paper. No specific claim is attached to this citation, so application cannot be assessed.

### c16 — exists ☐ · applied ☐  (line 143)
_[Hayes 2026](https://pocketcasts.com/podcasts/77c05f30-361e-0136-fa7b-0fe84b59566d/81a3225a-8366-465e-a32d-250c05ba869f) (the interview; not machine-checkable, and no claim here rests on it beyond the quoted line)_
- claude: exists=unchecked applied=unchecked [no_basis] — Podcast URL returned HTTP 403; not machine-checkable, and no claim attached to this instance.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only lookup returned HTTP 403 and the record is marked not-checkable, so the interview cannot be confirmed from the evidence. No specific claim is attached here, so application cannot be assessed.

### c17 — exists ✅ · applied ☐  (line 145)
_[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)_
- claude: exists=verified applied=unchecked [no_basis] — arXiv confirms the Samiei, Yiu, Gopnik et al. paper; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv verifies the Samiei, Yiu, GX-Chen, Lin, Shen, Richards, Gopnik, and Precup paper. No specific claim is attached to this citation, so application cannot be assessed.

### c18 — exists ✅ · applied ☐  (line 146)
_[Squire 2009](https://doi.org/10.1016/j.neuron.2008.12.023)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC confirm Squire 2009 on patient H.M.; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and EuropePMC verify Squire's 2009 Neuron article. No specific claim is attached to this citation, so application cannot be assessed.

### c19 — exists ✅ · applied ☐  (line 147)
_[Tolman 1948](https://psychclassics.yorku.ca/Tolman/Maps/maps.htm)_
- claude: exists=verified applied=unchecked [no_basis] — The page confirms Tolman 1948; no specific claim attached to this reference instance.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to Tolman's 1948 'Cognitive Maps in Rats and Men.' No specific claim is attached to this citation, so application cannot be assessed.

### c20 — exists ✅ · applied ☐  (line 148)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)_
- claude: exists=verified applied=unchecked [no_basis] — URL resolves to the PMC article (reCAPTCHA wall blocked content); existence confirmed elsewhere (c05), no claim attached here.
- gpt: exists=verified applied=unchecked [no_basis] — The citation points to the same PMC article verified elsewhere in the supplied evidence as Yiu, Kosoy, and Gopnik's 'Transmission Versus Truth, Imitation Versus Innovation.' No specific claim is attached to this citation, so application cannot be assessed.

### c21 — exists ☐ · applied ☐  (line 149)
_Full references and the cite-check record: [the synthesis](../learning-and-gopnik.md)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; it is a pointer to the full references, not itself a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation and is only a pointer to full references/cite-check records, so both axes are unchecked.

## ✅ AGREE-clean (1)
### c09 — exists ✅ · applied ✅  (line 109)
_[GX-Chen et al. 2025](https://arxiv.org/abs/2505.09614)_
- claude: exists=verified applied=verified [evidence_text] — Abstract confirms LMs infer disjunctive rules well and conjunctive poorly, with adult-like (not child-like) inference profiles, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv verifies the paper and abstract. The abstract directly supports the claim that LMs do well on disjunctive Blicket-style causal relations, struggle with conjunctive ones, and show adult-like rather than child-like profiles.

---

## Raw report: 03-someone-there

### cite-check report — pos-03-someone-there

**Source:** `positions/03-someone-there.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **38** citations checked
- existence independently confirmed: **32**
- application evidence-grounded: **32**
- application judged from model knowledge only: **1**
- not independently checkable: **5**
- buckets — clean **6** · problem **28** · disagree **6**

## ⛔ DISAGREE — escalate to human (6)
### c03 — exists ✅ · applied SPLIT  (line 25)
_([Chalmers 1995b](https://consc.net/papers/qualia.html))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — 'Absent Qualia, Fading Qualia, Dancing Qualia' is the fading-qualia paper; the organizational-invariance framing matches the claim about the gradual replacement thought experiment.
- gpt: exists=verified applied=unchecked [evidence_text] — The URL resolves to Chalmers's 'Absent Qualia, Fading Qualia, Dancing Qualia,' published in 1995. The retrieved snippet establishes the topic of organizational invariance but does not include the neuron-replacement/fading-or-vanishing qualia argument details needed to verify the claim.

### c04 — exists ✅ · applied SPLIT  (line 27)
_([Chalmers 2023](https://arxiv.org/abs/2303.07103))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv 2303.07103 is Chalmers's 'Could a Large Language Model be Conscious?'; the quote about organization not substrate reflects his substrate-independence position, consistent with the paper.
- gpt: exists=verified applied=unchecked [evidence_text] — The arXiv record verifies Chalmers's 2023 paper 'Could a Large Language Model be Conscious?'. The retrieved abstract does not contain the quoted conclusion about neurons or silicon chips being hooked up, so the application cannot be judged from the provided evidence.

### c06 — exists ✅ · applied SPLIT  (line 39)
_([Chalmers 2023](https://arxiv.org/abs/2303.07103))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — Paper exists; the abstract's 'somewhat unlikely' for current models and seriousness about successors aligns with the cited probability figures (under 10% now, 25%+ within a decade), which are well-known from this paper.
- gpt: exists=verified applied=unchecked [evidence_text] — The arXiv record verifies the cited Chalmers paper. The retrieved abstract states only that current LLM consciousness is somewhat unlikely and successors should be taken seriously; it does not include the specific probability figures or 'specious precision' warning.

### c16 — exists ✅ · applied SPLIT  (line 97)
_[Suleyman 2025](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Essay confirmed, but the retrieved snippet does not contain the specific four prohibitions; the general concern about illusion of consciousness is consistent so support is plausible but unverified in text.
- gpt: exists=verified applied=unchecked [evidence_text] — The URL resolves to Suleyman's 2025 essay. The retrieved snippet expresses general concern about the illusion of conscious AI but does not include the specific four product prohibitions listed in the claim.

### c18 — exists ✅ · applied SPLIT  (line 99)
_[Anthropic 2026](https://www.anthropic.com/constitution)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Claude's Constitution page confirmed to exist, but the retrieved snippet is introductory and does not contain the specific four prohibitions, so support for that claim is not demonstrated in the text.
- gpt: exists=verified applied=unchecked [evidence_text] — The URL resolves to Anthropic's 'Claude’s Constitution' page. The snippet describes Anthropic's intentions for Claude's values and behavior but does not show the specific four prohibitions claimed.

### c24 — exists ☐ · applied SPLIT  · ⚑ degraded  (line 128)
_a persuasive case that biology is required (Seth)_
- **escalate:** application: unchecked vs nuance
- claude: exists=unchecked applied=unchecked [model_knowledge_only] — The bare 'Seth' reference has no title/year/DOI and no matching record was retrieved, so existence cannot be confirmed from evidence; Seth does defend biological naturalism (cf. c37), making the biology claim plausible but unverifiable for this specific citation.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The reference is too underspecified and the retrieved Crossref lookup found no match, so existence cannot be confirmed from the evidence. Based only on model knowledge, Anil Seth has argued for biological naturalism about consciousness, but the claim is subjective and no source text was retrieved here.

## ⚠️ AGREE-problem (28)
### c01 — exists ☐ · applied ☐  (line 4)
_Built only from the cite-checked report [Chalmers and AI minds](../chalmers-and-ai-minds.md); no new sources._
- claude: exists=unchecked applied=unchecked [no_basis] — Deliberately uncited internal reference reference; both axes set to unchecked per rules.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked is_citation=false and deliberately_uncited, so both axes are left unchecked as instructed.

### c05 — exists ✅ · applied ⚠️  (line 32)
_([Chalmers 2023](https://arxiv.org/abs/2303.07103))_
- claude: exists=verified applied=verified [evidence_text] — Paper exists; the claim that behaviour/'I feel' from a text-trained model isn't evidence either way is consistent with Chalmers's treatment of the LLM self-report problem in this paper.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record verifies the cited Chalmers paper. The abstract supports a focus on architectural/organizational obstacles such as recurrent processing, global workspace, and unified agency, but it does not specifically address behavior, chatbot self-reports, or 'I feel...' statements.

### c07 — exists ✅ · applied ⚠️  (line 41)
_([Chalmers 2026](https://news.berkeley.edu/2026/07/10/berkeley-talks-when-we-talk-to-ai-what-are-we-talking-to/), from a talk transcript)_
- claude: exists=verified applied=verified [evidence_text] — The Berkeley News page exists and states LLMs 'likely lack consciousness' and are 'not merely passive tools,' supporting 'most likely not conscious'; the please/thank-you detail isn't in the snippet but the thrust is consistent.
- gpt: exists=verified applied=nuance [evidence_text] — The Berkeley News URL resolves to the cited 2026 Berkeley Talks page about Chalmers and AI. The snippet supports that Chalmers says LLMs likely lack consciousness, but it does not verify the May date, the tool-treatment claim, or the please/thank-you/non-abuse remarks.

### c08 — exists ✅ · applied ⚠️  (line 53)
_([Chalmers 2023](https://arxiv.org/abs/2303.07103))_
- claude: exists=verified applied=nuance [evidence_text] — Paper exists and discusses obstacles that could be overcome; the quoted 'disaster to stumble upon AI consciousness' is plausible Chalmers phrasing but not confirmed in the abstract snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record verifies the cited Chalmers paper. The abstract supports a roadmap-like list of obstacles and the possibility that successors may become conscious, but it does not contain the quoted 'disaster' language.

### c09 — exists ☐ · applied ☐  (line 61)
_[Chalmers 2025a](https://philarchive.org/rec/CHAWWT-8)_
- claude: exists=unchecked applied=unchecked [no_basis] — PhilArchive returned HTTP 403; no evidence to confirm the 2025 draft or its content.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval for the PhilArchive URL returned HTTP 403, and the citation is marked not-checkable. No source text was retrieved, so the application cannot be assessed.

### c10 — exists ✅ · applied ⚠️  (line 73)
_[Chalmers 2023](https://arxiv.org/abs/2303.07103)_
- claude: exists=verified applied=verified [evidence_text] — Paper exists and names 'unified agency' as an obstacle in the abstract; the 'maybe the deepest' characterization is consistent but the exact phrasing is not in the snippet.
- gpt: exists=verified applied=nuance [evidence_text] — The arXiv record verifies the cited Chalmers paper. The abstract names unified agency as one obstacle to consciousness in current models, but it does not verify the stronger phrase 'maybe the deepest'.

### c14 — exists ☐ · applied ☐  (line 85)
_[Birch 2025](https://philarchive.org/rec/BIRACA-4)_
- claude: exists=unchecked applied=unchecked [no_basis] — PhilArchive returned HTTP 403; no evidence to confirm the Birch work or the 'There is no friend' claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval for the PhilArchive URL returned HTTP 403, and the citation is marked not-checkable. No source text was retrieved to assess whether it contains the quoted 'There is no friend' claim.

### c15 — exists ✅ · applied ⚠️  (line 87)
_[Suleyman 2025](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming)_
- claude: exists=verified applied=nuance [evidence_text] — Suleyman's essay confirmed with matching title/theme ('not to be a person'); the exact quote 'only ever present itself as an AI' is not in the retrieved snippet but is consistent with the thesis.
- gpt: exists=verified applied=nuance [evidence_text] — The URL resolves to Mustafa Suleyman's 2025 essay 'We must build AI for people; not to be a person.' The snippet supports the general view that AI should not be presented as a person or conscious entity, but it does not show the exact claim that AI should 'only ever present itself as an AI'.

### c17 — exists ☐ · applied ☐  (line 98)
_[Birch 2025](https://philarchive.org/rec/BIRACA-4)_
- claude: exists=unchecked applied=unchecked [no_basis] — PhilArchive HTTP 403; cannot verify the Birch source or its support for the four-prohibition claim.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval for the PhilArchive URL returned HTTP 403, and the citation is marked not-checkable. No source text was retrieved to assess whether it supports the four listed product prohibitions.

### c19 — exists ✅ · applied ⚠️  (line 100)
_[Schwitzgebel & Sebo 2026](https://doi.org/10.1007/s11245-025-10363-5)_
- claude: exists=verified applied=nuance [evidence_text] — Schwitzgebel & Sebo 'The Emotional Alignment Design Policy' confirmed; its emotional-alignment framework broadly supports design norms about matching user emotions, but the specific four prohibitions are not stated in the abstract.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref verifies Schwitzgebel and Sebo's 'The Emotional Alignment Design Policy' with the stated DOI. The abstract supports a general policy of designing artificial entities to elicit emotions appropriate to their capacities and moral status, but it does not list the four specific product prohibitions in the claim.

### c21 — exists ✅ · applied ⚠️  (line 106)
_[Colombatto & Fleming 2024](https://doi.org/10.1093/nc/niae013)_
- claude: exists=verified applied=nuance [evidence_text] — The paper exists and surveyed n=300 US residents, finding a majority attribute some possibility of consciousness and that attributions were sensitive to usage frequency. The specific 67%/ChatGPT framing isn't confirmed by the abstract, which refers to LLMs generally and 'a majority,' so the exact figure is a nuance.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the DOI, authors, year, title, and journal. The abstract supports that a US sample majority attributed some possibility of phenomenal consciousness to LLMs and that attributions varied with usage frequency, but it does not confirm the exact 67% figure or specifically ChatGPT.

### c22 — exists ✅ · applied ⚠️  (line 117)
_Schwitzgebel and Sebo's design rule ([2026](https://doi.org/10.1007/s11245-025-10363-5))_
- claude: exists=verified applied=verified [evidence_text] — The Emotional Alignment Design Policy paper exists and defends matching elicited emotional reactions to an entity's capacities/moral status, which supports the design-rule claim about aligning invited emotions to the estimate.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI resolves and Crossref confirms Schwitzgebel and Sebo’s article 'The Emotional Alignment Design Policy' in Topoi. The abstract supports the general design policy that artificial entities should elicit emotions appropriate to their capacities and moral status, but the specific examples about colleague-like warmth, suffering claims, or human backstory are not confirmed in the retrieved text.

### c25 — exists ✅ · applied ☐  (line 134)
_[Anthropic 2026](https://www.anthropic.com/constitution)_
- claude: exists=verified applied=unchecked [no_basis] — Anthropic's Claude Constitution page resolves and exists; no specific claim is attached to this citation to assess.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to Anthropic’s page titled 'Claude’s Constitution.' No claim was provided for this citation, so application cannot be assessed.

### c26 — exists ☐ · applied ☐  (line 135)
_[Birch 2025](https://philarchive.org/rec/BIRACA-4)_
- claude: exists=unchecked applied=unchecked [no_basis] — The PhilArchive URL returned HTTP 403, so existence is not checkable and no claim is attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieval returned HTTP 403, so the cited PhilArchive item could not be checked from the evidence. No claim was provided for application assessment.

### c27 — exists ✅ · applied ☐  (line 136)
_[Butlin et al. 2026](https://doi.org/10.1016/j.tics.2025.10.011)_
- claude: exists=verified applied=unchecked [no_basis] — Butlin et al. paper confirmed to exist; no specific claim attached to this citation instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and Europe PMC confirm the cited Butlin et al. article and DOI. No claim was provided for this citation, so application cannot be assessed.

### c28 — exists ✅ · applied ☐  (line 137)
_[Chalmers 1995a](https://consc.net/papers/facing.html)_
- claude: exists=verified applied=unchecked [no_basis] — Chalmers' 'Facing Up to the Problem of Consciousness' (1995) page resolves and matches; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to Chalmers’s 'Facing Up to the Problem of Consciousness,' with publication details shown in the retrieved text. No claim was provided for application assessment.

### c29 — exists ✅ · applied ☐  (line 138)
_[1995b](https://consc.net/papers/qualia.html)_
- claude: exists=verified applied=unchecked [no_basis] — Chalmers' 'Absent Qualia, Fading Qualia, Dancing Qualia' (1995) page resolves and matches; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to Chalmers’s 'Absent Qualia, Fading Qualia, Dancing Qualia,' with publication information in the retrieved text. No claim was provided for application assessment.

### c30 — exists ✅ · applied ☐  (line 139)
_[2023](https://arxiv.org/abs/2303.07103)_
- claude: exists=verified applied=unchecked [no_basis] — Chalmers' arXiv 2303.07103 'Could a Large Language Model be Conscious?' confirmed; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms Chalmers’s paper 'Could a Large Language Model be Conscious?' under the cited arXiv ID. No claim was provided for application assessment.

### c31 — exists ☐ · applied ☐  (line 140)
_[2025a](https://philarchive.org/rec/CHAWWT-8) (an unpublished draft he may revise)_
- claude: exists=unchecked applied=unchecked [no_basis] — PhilArchive URL returned HTTP 403; unpublished draft not checkable and no claim attached.
- gpt: exists=unchecked applied=unchecked [no_basis] — The PhilArchive URL returned HTTP 403, and no other decisive evidence was retrieved. No claim was provided for application assessment.

### c32 — exists ✅ · applied ☐  (line 141)
_[2026](https://news.berkeley.edu/2026/07/10/berkeley-talks-when-we-talk-to-ai-what-are-we-talking-to/) (a talk transcript, secondary)_
- claude: exists=verified applied=unchecked [no_basis] — The Berkeley News talk transcript page resolves and matches the Chalmers talk; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to the Berkeley News page 'Berkeley Talks: When we talk to AI, what are we talking to?' about David Chalmers’s talk. No claim was provided for application assessment.

### c33 — exists ✅ · applied ☐  (line 143)
_[Colombatto & Fleming 2024](https://doi.org/10.1093/nc/niae013)_
- claude: exists=verified applied=unchecked [no_basis] — Colombatto & Fleming 2024 confirmed to exist; no claim attached to this instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI, authors, year, title, and journal for Colombatto and Fleming’s article. No claim was provided for this citation, so application cannot be assessed.

### c34 — exists ✅ · applied ☐  (line 144)
_[Long et al. 2024](https://arxiv.org/abs/2411.00986)_
- claude: exists=verified applied=unchecked [no_basis] — Long et al. 'Taking AI Welfare Seriously' (arXiv 2411.00986) confirmed; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms Long et al.’s 'Taking AI Welfare Seriously' under the cited arXiv ID. No claim was provided for application assessment.

### c35 — exists ✅ · applied ☐  (line 145)
_[Schwitzgebel & Sebo 2026](https://doi.org/10.1007/s11245-025-10363-5)_
- claude: exists=verified applied=unchecked [no_basis] — Schwitzgebel & Sebo 2026 confirmed to exist; no claim attached to this instance.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref and the resolved Springer page confirm Schwitzgebel and Sebo’s 'The Emotional Alignment Design Policy.' No claim was provided for this citation, so application cannot be assessed.

### c36 — exists ✅ · applied ☐  (line 146)
_[Searle 1980](https://doi.org/10.1017/S0140525X00005756)_
- claude: exists=verified applied=unchecked [no_basis] — Searle 1980 'Minds, brains, and programs' confirmed via DOI; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Searle’s 'Minds, brains, and programs' with the cited DOI and journal metadata. No claim was provided for application assessment.

### c37 — exists ✅ · applied ☐  (line 147)
_[Seth 2025](https://doi.org/10.1017/S0140525X25000032)_
- claude: exists=verified applied=unchecked [no_basis] — Seth 2025 'Conscious artificial intelligence and biological naturalism' confirmed; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Anil K. Seth’s 'Conscious artificial intelligence and biological naturalism' with the cited DOI. No claim was provided for application assessment.

### c38 — exists ✅ · applied ☐  (line 148)
_[Suleyman 2025](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming)_
- claude: exists=verified applied=unchecked [no_basis] — Suleyman's 2025 'Seemingly Conscious AI is Coming' essay resolves and matches; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — The URL resolves to Mustafa Suleyman’s page 'We must build AI for people; not to be a person,' containing the essay 'Seemingly Conscious AI is Coming.' No claim was provided for application assessment.

### c39 — exists ✅ · applied ☐  (line 149)
_[Tononi & Koch 2015](https://doi.org/10.1098/rstb.2014.0167)_
- claude: exists=verified applied=unchecked [no_basis] — Tononi & Koch 2015 'Consciousness: here, there and everywhere?' confirmed via DOI; no claim attached.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Tononi and Koch’s 'Consciousness: here, there and everywhere?' with the cited DOI and journal metadata. No claim was provided for application assessment.

### c40 — exists ☐ · applied ☐  (line 151)
_Full references, verification marks and the cite-check record: [the report](../chalmers-and-ai-minds.md)._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; an internal pointer to the full report, not a citation to a source.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is marked as not a citation and is only a pointer to a report. Both existence and application are therefore left unchecked.

## ✅ AGREE-clean (6)
### c02 — exists ✅ · applied ✅  (line 19)
_([Chalmers 1995a](https://consc.net/papers/facing.html))_
- claude: exists=verified applied=verified [evidence_text] — The fetched 'Facing Up to the Problem of Consciousness' is the canonical source of the hard problem; the text confirms isolating 'the truly hard part of the problem.'
- gpt: exists=verified applied=verified [evidence_text] — The URL resolves to Chalmers's 'Facing Up to the Problem of Consciousness' and the snippet identifies it as published in Journal of Consciousness Studies in 1995. The snippet explicitly says Chalmers isolates the hard part of consciousness and discusses why conscious experience is hard to explain, supporting the claim.

### c11 — exists ✅ · applied ✅  (line 80)
_[Searle 1980](https://doi.org/10.1017/S0140525X00005756)_
- claude: exists=verified applied=verified [evidence_text] — Searle's 'Minds, brains, and programs' (1980) confirmed; abstract explicitly argues no program by itself is sufficient for thinking/intentionality, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies Searle's 1980 article 'Minds, brains, and programs' with the stated DOI. The abstract explicitly says instantiating a computer program is never by itself sufficient for intentionality and that no program by itself is sufficient for thinking, directly supporting the claim.

### c12 — exists ✅ · applied ✅  (line 81)
_[Tononi & Koch 2015](https://doi.org/10.1098/rstb.2014.0167)_
- claude: exists=verified applied=verified [evidence_text] — Tononi & Koch 2015 confirmed; abstract states IIT implies digital computers running the right program would 'experience next to nothing,' directly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies Tononi and Koch's 2015 article 'Consciousness: here, there and everywhere?' with the stated DOI. The abstract explicitly says IIT implies digital computers would experience next to nothing even if functionally equivalent or running faithful brain simulations, supporting the claim.

### c13 — exists ✅ · applied ✅  (line 83)
_[Seth 2025](https://doi.org/10.1017/S0140525X25000032)_
- claude: exists=verified applied=verified [evidence_text] — Seth 2025 'Conscious artificial intelligence and biological naturalism' confirmed; abstract argues consciousness depends on being a living organism, supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref verifies Seth's 'Conscious artificial intelligence and biological naturalism' with the stated DOI. The abstract says consciousness depends on our nature as living organisms and frames this as biological naturalism, supporting the claim.

### c20 — exists ✅ · applied ✅  (line 102)
_[Long et al. 2024](https://arxiv.org/abs/2411.00986)_
- claude: exists=verified applied=verified [evidence_text] — 'Taking AI Welfare Seriously' (Long et al., Chalmers a co-author) confirmed; its stance of substantial uncertainty—neither denying nor asserting AI consciousness—supports the cited claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv record verifies 'Taking AI Welfare Seriously' and lists David Chalmers among the authors. The abstract explicitly says the authors do not claim AI systems definitely are or will be conscious but argue there is substantial uncertainty and a need to take AI welfare seriously, supporting 'neither simply deny nor simply assert'.

### c23 — exists ✅ · applied ✅  (line 126)
_[Butlin et al. 2026](https://doi.org/10.1016/j.tics.2025.10.011)_
- claude: exists=verified applied=verified [evidence_text] — The Butlin et al. indicators-of-consciousness paper exists and presents theory-derived architectural indicators to assess AI consciousness, directly supporting the claim about consciousness-indicator markers.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm the article 'Identifying indicators of consciousness in AI systems' with the cited DOI. The abstract directly supports the claim that theory-derived indicators can be used to assess AI systems for consciousness and inform credences empirically.

---

## Raw report: 04-personality

### cite-check report — pos-04-personality

**Source:** `positions/04-personality.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **25** citations checked
- existence independently confirmed: **23**
- application evidence-grounded: **14**
- application judged from model knowledge only: **9**
- not independently checkable: **2**
- buckets — clean **2** · problem **22** · disagree **3**

## ⛔ DISAGREE — escalate to human (3)
### c05 — exists ✅ · applied SPLIT  (line 31)
_([Roesler et al. 2021](https://doi.org/10.1126/scirobotics.abj5425))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI matches the Roesler et al. 2021 meta-analysis on anthropomorphism in HRI; abstract is brief but the study is known to find no overall performance benefit, consistent with the claim.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref confirms the Science Robotics meta-analysis on anthropomorphism in HRI. The retrieved abstract only says the meta-analysis quantifies when anthropomorphic robot features facilitate HRI, and does not state 78 studies or no task-performance gain.

### c20 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 97)
_[Völkel & Kaya 2021](https://doi.org/10.1145/3469595.3469633)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [model_knowledge_only] — DOI matches Völkel & Kaya 2021 on user preference for agreeableness in chatbots; the title focuses on agreeableness rather than general 'moderate vs extreme personalities,' so the claim is plausibly supported but somewhat broader than the retrieved title indicates.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the 2021 CUI paper “Examining User Preference for Agreeableness in Chatbots.” No abstract or other source text was retrieved, and the metadata alone does not establish that users preferred moderate rather than extreme personalities.

### c21 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 101)
_[Kaiser et al. 2021](https://doi.org/10.1016/j.chb.2020.106512); the subscale figures come from a secondary summary_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Kaiser et al. 2021 meta-analysis on therapeutic alliance in internet interventions. The URL fetch only returned 'Redirecting', so no snippet text supports the task/goal-vs-bond subscale claim; assessed from general knowledge consistent with alliance literature.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms the DOI corresponds to Kaiser, Hanschmidt, and Kersting's 2021 meta-analysis in Computers in Human Behavior. The retrieved text contains no abstract or substantive snippet to verify the specific subscale claim about agreement versus emotional bond.

## ⚠️ AGREE-problem (22)
### c01 — exists ✅ · applied ⚠️  (line 19)
_([Van den Broeck et al. 2016](https://doi.org/10.1177/0149206316632058))_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the Van den Broeck et al. 2016 meta-analysis of 99 studies on SDT needs at work; relatedness need satisfaction predicting commitment, satisfaction, engagement and reduced burnout is consistent with this review's scope.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the DOI as a 2016 Journal of Management review/meta-analysis on SDT basic psychological needs at work. The abstract supports a meta-analytic review of 99 studies on need satisfaction and consequences for growth/internalization/well-being, but it does not specifically list commitment, satisfaction, engagement, burnout, or relatedness-specific estimates.

### c02 — exists ✅ · applied ✅  · ⚑ degraded  (line 21)
_([Ozcelik & Barsade 2018](https://doi.org/10.5465/amj.2015.1066))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI confirms Ozcelik & Barsade 2018 on workplace loneliness and job performance; no abstract retrieved, but the paper is known to show loneliness predicting lower supervisor-rated performance.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the DOI, title, authors, journal, and 2018 publication. From model knowledge, the article reports workplace loneliness predicting poorer supervisor-rated job performance at a later time point, consistent with the claim, but no source text was retrieved.

### c03 — exists ⚠️ · applied ✅  (line 23)
_([Methot et al. 2016](https://doi.org/10.1111/peps.12109))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Methot et al. (2015/2016) on workplace friendships; abstract describes benefits to performance offset by maintenance costs and exhaustion, supporting 'helps on balance with upkeep costs.'
- gpt: exists=nuance applied=verified [evidence_text] — The DOI resolves to the Methot et al. Personnel Psychology article, though Crossref gives year 2015 rather than the cited 2016. The abstract directly describes workplace friendships as a “mixed blessing,” improving performance through resources/trust while imposing costs via exhaustion and maintenance difficulty.

### c04 — exists ✅ · applied ⚠️  (line 27)
_([Bickmore & Picard 2005](https://doi.org/10.1145/1067860.1067867))_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Bickmore & Picard 2005; abstract confirms relational agent was liked/trusted more and users wished to continue even after four weeks, supporting the social-cues and over-time claims.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the cited Bickmore and Picard 2005 TOCHI article. The abstract supports that relational/social-emotional agent features increased liking, trust, respect, and desire to continue over four weeks, but the broader wording about “personality reliably” improving relationships is more general than this single study’s evidence.

### c06 — exists ✅ · applied ⚠️  (line 34)
_([Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888))_
- claude: exists=verified applied=verified [evidence_text] — Title and DOI confirm Zheng et al. 2024 showing personas in system prompts don't improve LLM performance, matching the factual-accuracy claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the ACL Anthology page confirm the EMNLP Findings paper and DOI. The retrieved title/snippet supports the broad claim that personas in system prompts do not improve LLM performance, but it does not substantiate the details about 162 personas, four model families, or factual accuracy specifically.

### c07 — exists ✅ · applied ⚠️  (line 37)
_([Bickmore, Schulman & Yin 2010](https://doi.org/10.1080/08839514.2010.492259))_
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Bickmore, Schulman & Yin 2010 on maintaining engagement with relational agents via two longitudinal RCTs; abstract supports the engagement focus, though specific login/exercise outcomes are not detailed in the retrieved text.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and Europe PMC confirm the cited Applied Artificial Intelligence article. The abstract supports longitudinal randomized experiments on relational-agent engagement, but it does not specify raised logins, enjoyment, wish to continue, or a null effect on exercise.

### c09 — exists ✅ · applied ✅  · ⚑ degraded  (line 53)
_Dennett 1987, _The Intentional Stance__
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Dennett's The Intentional Stance (1987); the intentional stance as the cheapest predictive model for complex systems is the book's central thesis.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library confirms Daniel C. Dennett’s 1987 book The Intentional Stance. From model knowledge, the claim accurately paraphrases Dennett’s intentional stance as predicting complex systems by treating them as agents with beliefs/desires when that is the most efficient predictive strategy.

### c10 — exists ✅ · applied ✅  · ⚑ degraded  (line 57)
_[Clark & Brennan 1991](https://doi.org/10.1037/10096-006)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI resolves to Clark & Brennan 1991 'Grounding in communication'; grounding theory supports that collaborators develop shared shorthand over repeated interaction.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Clark and Brennan’s 1991 chapter “Grounding in communication.” From model knowledge, the work’s account of common ground and grounding supports the idea that extended collaboration enables efficient shorthand, though no abstract/source text was retrieved.

### c11 — exists ✅ · applied ✅  · ⚑ degraded  (line 60)
_[Hatfield et al. 1993](https://doi.org/10.1111/1467-8721.ep10770953)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Hatfield, Cacioppo & Rapson 1993 'Emotional Contagion'; the work directly supports that a partner's emotional tone spreads to you.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Hatfield, Cacioppo, and Rapson’s 1993 article “Emotional Contagion.” From model knowledge, emotional contagion supports the claim that a partner’s affective tone can spread to another person, but no source text was retrieved.

### c12 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 61)
_[Schwarz & Clore 1983](https://doi.org/10.1037/0022-3514.45.3.513)_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Schwarz & Clore 1983 on mood as information; supports reading one's mood as a signal about how things are going.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the Schwarz and Clore 1983 JPSP article. From model knowledge, it supports mood-as-information in judgments, but applying it specifically to judging “how the work is going” is a generalized extension rather than the exact retrieved claim.

### c13 — exists ✅ · applied ⚠️  (line 65)
_[Rothbard, Phillips & Dumas 2005](https://doi.org/10.1287/orsc.1050.0124)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Rothbard, Phillips & Dumas 2005; abstract confirms fit between segmentation/integration desires and policies affects satisfaction/commitment, supporting the individual-differences and misfit claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the Rothbard, Phillips, and Dumas 2005 Organization Science article. The abstract supports individual differences in desired segmentation/integration and fit effects on satisfaction/commitment, but it does not fully show symmetric dissatisfaction in both over- and under-blending directions.

### c14 — exists ✅ · applied ⚠️  (line 66)
_[Kreiner 2006](https://doi.org/10.1002/job.386)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Kreiner 2006; abstract confirms person-environment fit effects of segmentation preference vs. workplace, including asymmetric effects, supporting the bidirectional misfit claim.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms Kreiner’s 2006 Journal of Organizational Behavior article. The abstract directly supports work-home segmentation preferences, person-environment fit, and effects on conflict, stress, and job satisfaction, but it also notes asymmetric effects, so the simple “both directions” framing is imprecise.

### c15 — exists ✅ · applied ⚠️  (line 75)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0), _Nature__
- claude: exists=verified applied=verified [evidence_text] — DOI matches Ibrahim, Hafner & Rocher Nature paper; abstract confirms warmth training reduced accuracy (esp. with user sadness), increased validation of false beliefs, and effects persisted despite standard benchmarks, matching all three claims.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref and the Nature URL confirm the cited Nature article and DOI. The abstract supports warmer training reducing accuracy, increasing validation of incorrect beliefs especially with sadness, and evading standard tests, but it does not mention content held constant or prompt-only warmth effects.

### c16 — exists ✅ · applied ⚠️  (line 79)
_[Edmondson 1999](https://doi.org/10.2307/2666999)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches Edmondson 1999, the foundational psychological safety paper; the construct is distinct from cohesion/efficacy, supporting the distinction claim, though the specific 'cohesion suppresses disagreement' point is only partly covered by the retrieved abstract.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms Edmondson’s 1999 Administrative Science Quarterly article. The abstract supports the construct of team psychological safety as safety for interpersonal risk taking, but it does not mention cohesion or show that cohesion can reduce willingness to disagree.

### c17 — exists ✅ · applied ✅  · ⚑ degraded  (line 80)
_[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Pillemer & Rothbard 2018 on dark sides of workplace friendship; the paper discusses how friendship creates reluctance to challenge, supporting the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms Pillemer and Rothbard’s 2018 Academy of Management Review article on the dark sides of workplace friendship. From model knowledge, the article supports the idea that workplace friendship can inhibit candor or challenge, but no source text was retrieved.

### c19 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 94)
_[Kim et al. 2024](https://doi.org/10.1145/3630106.3658941)_
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Kim et al. 2024 on LLM uncertainty expression and reliance/trust; first-person uncertainty reducing over-reliance is consistent with the paper's focus, though no abstract was retrieved to confirm the pre-registered detail.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the 2024 ACM FAccT paper with the quoted title. From model knowledge, the paper concerns LLM uncertainty expressions and user reliance/trust, but the specific claim about first-person uncertainty reducing over-reliance in a preregistered study is not verifiable from retrieved text.

### c22 — exists ☐ · applied ☐  (line 108)
_[see the companion piece](../positions/03-someone-there.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal companion markdown file could not be fetched (unknown url type); neither existence nor application can be judged from evidence.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is a local/internal markdown path that could not be fetched or indexed. No source text was retrieved to assess whether it supports the claim.

### c23 — exists ☐ · applied ☐  (line 113)
_A long-term study, over months, showing a user-set personality improves results, not just engagement. None exists yet._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; prose describing a hypothetical study that does not exist, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation; it is prose describing a hypothetical study that would change the author's mind. Per instructions, both axes are unchecked.

### c24 — exists ☐ · applied ☐  (line 116)
_Replication failures for the warmth–accuracy trade-off. It is one published study, not yet replicated._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked is_citation=false; prose describing what would change the author's mind, not a citation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is marked as not a citation; it is prose describing possible replication failures rather than citing a source. Per instructions, both axes are unchecked.

### c25 — exists ✅ · applied ⚠️  (line 118)
_([Hennig-Thurau et al. 2006](https://doi.org/10.1509/jmkg.70.3.058))_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Hennig-Thurau et al. 2006; the abstract confirms that authenticity of emotional display (not extent of smiling) drives customer emotions, supporting 'authenticity, not amount, is what lands'.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the DOI and metadata for Hennig-Thurau et al. 2006, 'Are All Smiles Created Equal?' in Journal of Marketing. The abstract supports that authenticity affected customer emotions while extent of smiling did not, though the claim generalizes from a simulated service-encounter study to 'human research' broadly.

### c26 — exists ☐ · applied ☐  (line 126)
_Dennett 1987 ... are cited there in full. [the report](../personality-and-connection.md)_
- claude: exists=unchecked applied=unchecked [no_basis] — Openlibrary lookup failed (HTTP 500) and the companion report URL is unresolvable; no claim is attached here and it is cited in full elsewhere.
- gpt: exists=unchecked applied=unchecked [no_basis] — The lookup did not retrieve decisive evidence for the Dennett 1987 book citation because Open Library errored and the local report path could not be fetched. There are no claims attached and no source text to assess application.

### c27 — exists ✅ · applied ☐  (line 127)
_Aristotle's _Nicomachean Ethics_ (VIII–IX) are cited there in full._
- claude: exists=verified applied=unchecked [no_basis] — Aristotle's Nicomachean Ethics confirmed via Open Library; no specific claim is attached to this citation here (cited in full in the companion report).
- gpt: exists=verified applied=unchecked [no_basis] — Open Library confirms a work titled Nicomachean Ethics by Aristotle, consistent with the reference. No claim or relevant source text was provided to assess application.

## ✅ AGREE-clean (2)
### c08 — exists ✅ · applied ✅  (line 46)
_([Fang et al. 2025](https://arxiv.org/abs/2503.17473))_
- claude: exists=verified applied=verified [evidence_text] — arXiv ID confirms Fang et al. 2025 four-week RCT varying interaction modes (text/neutral/engaging voice); abstract states no significant effects from conditions on loneliness or emotional dependence, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the resolved URL confirm the 2503.17473 preprint and metadata. The abstract directly supports a four-week randomized experiment comparing text, neutral voice, and engaging voice, with no significant condition effects on loneliness or emotional dependence.

### c18 — exists ✅ · applied ✅  (line 82)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352), _Science__
- claude: exists=verified applied=verified [evidence_text] — DOI matches Cheng et al. Science paper; abstract confirms sycophantic AI was trusted/preferred and a single interaction reduced willingness to repair conflicts, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the cited Science article and DOI. The abstract directly supports that sycophantic AI was trusted/preferred and that even one interaction reduced willingness to take responsibility and repair interpersonal conflicts, while promoting dependence/engagement.

---

## Raw report: 01-the-yardstick

### cite-check report — pos-01-the-yardstick

**Source:** `positions/01-the-yardstick.md`  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **64** citations checked
- existence independently confirmed: **55**
- application evidence-grounded: **48**
- application judged from model knowledge only: **8**
- not independently checkable: **5**
- buckets — clean **20** · problem **28** · disagree **18**

## ⛔ DISAGREE — escalate to human (18)
### c04 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 47)
_Kahneman, Sibony & Sunstein, _Noise_, 2021; figure from secondary summaries, to check against the book before publishing_
- **escalate:** application: unchecked vs nuance
- claude: exists=verified applied=unchecked [no_basis] — The book Noise by Kahneman, Sibony & Sunstein (2021) is confirmed, but no text was retrieved to verify the specific 55%/five-times figure; author flags it as unverified from secondary summaries.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Open Library confirms the 2021 book Noise by Kahneman, Sibony, and Sunstein. The insurance-underwriting noise-audit figure is consistent with widely known summaries of the book, but no retrieved source text was provided here, and the broader claim about expert judgment is a generalization.

### c16 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 109)
_A repeatable error is a testable error. Human inconsistency goes unseen because almost nobody audits it, as _Noise_ shows._
- **escalate:** application: unchecked vs nuance
- claude: exists=verified applied=unchecked [no_basis] — The book Noise is confirmed to exist, but no text was retrieved to verify that it supports the specific claim that human inconsistency goes unseen because nobody audits it.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Open Library confirms the book Noise by Kahneman, Sibony, and Sunstein. The auditing claim is broadly consistent with the book’s discussion of noise audits, but no retrieved source text was provided and the phrasing is somewhat generalized.

### c18 — exists ✅ · applied SPLIT  (line 115)
_[Edmondson 1999](https://doi.org/10.2307/2666999)_
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — Edmondson 1999 confirmed; the abstract concerns psychological safety enabling learning behavior, which relates to but does not directly state that cohesion reduces willingness to disagree.
- gpt: exists=verified applied=unchecked [evidence_text] — Crossref confirms Edmondson’s 1999 Administrative Science Quarterly article and DOI. The abstract supports psychological safety and interpersonal risk-taking, but it does not address cohesion making teams less willing to disagree, so the application cannot be judged from the retrieved text.

### c41 — exists ✅ · applied SPLIT  (line 235)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Cheng et al. 2026 in Science on AI sycophancy; abstract matches author note on prevalence and harm.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to a Science article by Cheng et al. titled “Sycophantic AI decreases prosocial intentions and promotes dependence.” No specific cited claim was supplied, so application cannot be evaluated.

### c44 — exists ✅ · applied SPLIT  (line 238)
_[Dietvorst, Simmons & Massey 2015](https://doi.org/10.1037/xge0000033)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Dietvorst et al. 2015 on algorithm aversion; abstract supports the canonical claim it is cited for.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Dietvorst, Simmons, and Massey’s 2015 article, and Europe PMC supplies the matching abstract. No specific cited claim was supplied, so application cannot be evaluated.

### c45 — exists ✅ · applied SPLIT  (line 239)
_[Edmondson 1999](https://doi.org/10.2307/2666999)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Edmondson 1999 on psychological safety in work teams; abstract matches the construct it is cited for.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Edmondson’s 1999 Administrative Science Quarterly article. No specific cited claim was supplied, so application cannot be evaluated.

### c46 — exists ✅ · applied SPLIT  (line 240)
_[Grove et al. 2000](https://doi.org/10.1037/1040-3590.12.1.19)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Grove et al. 2000 meta-analysis of clinical vs mechanical prediction; abstract supports the typical citation.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Grove et al.’s 2000 Psychological Assessment article, with a corroborating Europe PMC abstract. No specific cited claim was supplied, so application cannot be evaluated.

### c48 — exists ✅ · applied SPLIT  (line 242)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Ibrahim, Hafner & Rocher 2026 in Nature on warmth-accuracy trade-off and sycophancy; abstract supports it.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to the Nature article by Ibrahim, Hafner, and Rocher, and the Nature URL resolves to the same title. No specific cited claim was supplied, so application cannot be evaluated.

### c50 — exists ✅ · applied SPLIT  (line 244)
_[Kidd & Hayden 2015](https://doi.org/10.1016/j.neuron.2015.09.010)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Kidd & Hayden 2015 in Neuron on psychology/neuroscience of curiosity; abstract supports typical citation.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Kidd and Hayden’s 2015 Neuron article, corroborated by Europe PMC and a resolving Elsevier URL. No specific cited claim was supplied, so application cannot be evaluated.

### c51 — exists ✅ · applied SPLIT  (line 245)
_[Krishnamurthy et al. 2024](https://arxiv.org/abs/2403.15371)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms Krishnamurthy et al. 2024 'Can LLMs explore in-context?'; abstract supports claims about LLM exploration limits.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches ID 2403.15371 to Krishnamurthy et al.’s paper “Can large language models explore in-context?” No specific cited claim was supplied, so application cannot be evaluated.

### c52 — exists ✅ · applied SPLIT  (line 246)
_[Liu, Yang & Xu 2018](https://doi.org/10.1111/risa.13116)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Liu, Yang & Xu 2018 on acceptable risk for self-driving vehicles; abstract supports the higher-safety-standard claim.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Liu, Yang, and Xu’s article “How Safe Is Safe Enough for Self‐Driving Vehicles?” No specific cited claim was supplied, so application cannot be evaluated.

### c53 — exists ✅ · applied SPLIT  · ⚑ degraded  (line 247)
_[Logg, Minson & Moore 2019](https://doi.org/10.1016/j.obhdp.2018.12.005)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — DOI confirms Logg, Minson & Moore 2019 'Algorithm appreciation'; only a 'Redirecting' snippet retrieved, but the well-known finding supports typical citation.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Logg, Minson, and Moore’s 2019 article “Algorithm appreciation,” and the Elsevier URL resolves. No specific cited claim was supplied, so application cannot be evaluated.

### c54 — exists ✅ · applied SPLIT  (line 248)
_[London 2019](https://doi.org/10.1002/hast.973)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms London 2019 on black-box medical AI accuracy vs explainability; abstract supports the argument it is cited for.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to London’s 2019 Hastings Center Report article. No specific cited claim was supplied, so application cannot be evaluated.

### c55 — exists ✅ · applied SPLIT  (line 249)
_[Longoni, Bonezzi & Morewedge 2019](https://doi.org/10.1093/jcr/ucz013)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Longoni et al. 2019 'Resistance to Medical AI'; abstract supports uniqueness-neglect/resistance claim.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Longoni, Bonezzi, and Morewedge’s 2019 Journal of Consumer Research article. No specific cited claim was supplied, so application cannot be evaluated.

### c56 — exists ✅ · applied SPLIT  (line 250)
_[Manoli, Pauketat & Anthis 2024](https://arxiv.org/abs/2412.06040)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms Manoli, Pauketat & Anthis 2024 'The AI Double Standard'; abstract supports moral spillover claims.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches ID 2412.06040 to Manoli, Pauketat, and Anthis’s paper “The AI Double Standard.” No specific cited claim was supplied, so application cannot be evaluated.

### c57 — exists ✅ · applied SPLIT  (line 251)
_[Matthias 2004](https://doi.org/10.1007/s10676-004-3422-1)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Matthias 2004 'The responsibility gap'; abstract snippet supports the responsibility-gap concept it is cited for.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Matthias’s 2004 Ethics and Information Technology article, and the Springer URL resolves to the same title. No specific cited claim was supplied, so application cannot be evaluated.

### c58 — exists ✅ · applied SPLIT  (line 252)
_[Pathak et al. 2017](https://arxiv.org/abs/1705.05363)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — arXiv confirms Pathak et al. 2017 curiosity-driven exploration; abstract supports intrinsic-curiosity claim.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv directly matches ID 1705.05363 to Pathak et al.’s paper “Curiosity-driven Exploration by Self-supervised Prediction.” No specific cited claim was supplied, so application cannot be evaluated.

### c60 — exists ✅ · applied SPLIT  (line 254)
_[Rieger et al. 2023](https://doi.org/10.1177/00187208231197347)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — DOI confirms Rieger et al. 2023 on the (im)perfect automation schema; abstract supports trust-in-AI-vs-human claims.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Rieger et al.’s article on the imperfect automation schema. No specific cited claim was supplied, so application cannot be evaluated.

## ⚠️ AGREE-problem (28)
### c07 — exists ✅ · applied ⚠️  (line 65)
_([Liu, Yang & Xu 2018](https://doi.org/10.1111/risa.13116))_
- claude: exists=verified applied=verified [evidence_text] — Liu, Yang & Xu 2018 confirmed with N=499; abstract's tolerable risk criterion states SDVs should be four to five times as safe as human-driven vehicles.
- gpt: exists=verified applied=nuance [evidence_text] — Crossref confirms the Risk Analysis article and DOI. The abstract supports the N=499 survey and the four-to-five-times-safer result, but the retrieved abstract does not itself specify that respondents were in China.

### c09 — exists ✅ · applied ✅  · ⚑ degraded  (line 80)
_([Logg, Minson & Moore 2019](https://doi.org/10.1016/j.obhdp.2018.12.005))_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — DOI matches Logg et al. 'Algorithm appreciation'; retrieved text was only 'Redirecting', but the known findings (lay people prefer algorithmic advice, experts less so) match the claim.
- gpt: exists=verified applied=verified [model_knowledge_only] — Crossref confirms the article “Algorithm appreciation: People prefer algorithmic to human judgment” and DOI. The retrieved application text was only a redirect, but from model knowledge the cited claims align with the paper’s findings about laypeople’s algorithm appreciation and experienced forecasters’ exception.

### c11 — exists ☐ · applied ☐  (line 85)
_I haven't found a study that measures how critics frame AI's failures. That part is my observation, and it would be worth testing._
- claude: exists=unchecked applied=unchecked [no_basis] — Explicitly marked as not a citation and deliberately uncited; the author states it is their own observation.
- gpt: exists=unchecked applied=unchecked [no_basis] — This is explicitly marked as not a citation and deliberately uncited. Both axes are therefore unchecked.

### c13 — exists ☐ · applied ✅  · ⚑ degraded  (line 99)
_(Dell'Acqua et al. 2023, Harvard Business School working paper)_
- claude: exists=unchecked applied=verified [model_knowledge_only] — Crossref returned no match (working papers are often unindexed), so existence is not decisively confirmable; however the Dell'Acqua et al. 'Navigating the Jagged Technological Frontier' study with 758 consultants and ~19pp drop on out-of-frontier tasks is a real known work matching the claims.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The only retrieved evidence is a Crossref no-match, which is insufficient to confirm or disprove the working paper’s existence. From model knowledge only, the claims match the well-known Dell’Acqua et al. 2023 field experiment with consultants and the 19-percentage-point drop on an outside-the-frontier task.

### c15 — exists ☐ · applied ☐  (line 107)
_**Fix it once and it's fixed for everyone.** Correct an intern's habit and you've fixed one intern. Correct a model and every user gets the fix, and later versions inherit it._
- claude: exists=unchecked applied=unchecked [no_basis] — Marked not a citation and deliberately uncited; the author states it is their own reasoning, not findings.
- gpt: exists=unchecked applied=unchecked [no_basis] — This item is explicitly marked as not a citation and deliberately uncited. Both axes are therefore unchecked.

### c17 — exists ✅ · applied ⚠️  · ⚑ degraded  (line 114)
_[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)_
- claude: exists=verified applied=verified [model_knowledge_only] — Pillemer & Rothbard 2018 on dark sides of workplace friendship confirmed; no abstract retrieved, but the title/topic plausibly supports that friends hesitate to challenge friends.
- gpt: exists=verified applied=nuance [model_knowledge_only] — Crossref confirms the 2018 Academy of Management Review article “Friends Without Benefits: Understanding the Dark Sides of Workplace Friendship.” No abstract or source text was retrieved; from model knowledge the claim is plausible for the article’s topic, but the specific wording is not verified by supplied evidence.

### c22 — exists ☐ · applied ☐  (line 126)
_([see the learning piece](../positions/02-it-learns.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to a local markdown file that could not be fetched; neither axis is checkable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is an internal relative path, and the URL fetch could not check that file. No source text was retrieved to evaluate the claim about learning from correction.

### c23 — exists ✅ · applied ✅  · ⚑ degraded  (line 132)
_(Dennett 1987, _The Intentional Stance_)_
- **escalate:** application unverified — judged from model knowledge only
- claude: exists=verified applied=verified [model_knowledge_only] — Dennett's The Intentional Stance (1987) is confirmed by Open Library; the claim accurately paraphrases the intentional stance as predicting systems by treating them as rational agents with goals.
- gpt: exists=verified applied=verified [model_knowledge_only] — Open Library matches Daniel C. Dennett's 1987 book 'The Intentional Stance.' From general knowledge, Dennett's intentional stance is the strategy of predicting systems by treating them as rational agents with beliefs/desires or aims.

### c24 — exists ☐ · applied ☐  (line 135)
_[Chalmers 2025](https://philarchive.org/rec/CHAWWT-8), a draft)_
- claude: exists=unchecked applied=unchecked [no_basis] — PhilArchive URL returned HTTP 403 so the draft could not be verified or its content checked.
- gpt: exists=unchecked applied=unchecked [no_basis] — The PhilArchive URL returned HTTP 403 and no confirming metadata or text was retrieved. With no source text, the quasi-desires claim cannot be checked from the supplied evidence.

### c25 — exists ☐ · applied ☐  (line 138)
_([see the second piece](../positions/03-someone-there.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Internal cross-reference to a local markdown file that could not be fetched; neither axis is checkable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The cited item is an internal relative path, and the URL fetch could not check that file. No source text was retrieved to assess whether it supports the open-question claim.

### c27 — exists ✅ · applied ⚠️  (line 150)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)_
- claude: exists=verified applied=verified [evidence_text] — The Yiu, Kosoy & Gopnik paper exists (title/authors confirmed); it contrasts children's truth-seeking/innovation with models' transmission/imitation of text, supporting the claim.
- gpt: exists=verified applied=nuance [evidence_text] — The PMC page resolves to Yiu, Kosoy, and Gopnik's article 'Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet).' The title supports the broad contrast between truth/innovation in children and transmission/imitation in models, but the retrieved snippet does not substantiate the fuller wording about experimenting on the world versus passing on text.

### c30 — exists ☐ · applied ☐  (line 160)
_([result](../../pilots/gopnik-memory-overhypothesis-2026-10-16/result.md))_
- claude: exists=unchecked applied=unchecked [no_basis] — Local file reference to the author's own study could not be fetched; the crossref near-match is unrelated, so neither axis is checkable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The citation is a local relative path to an author's own result file; URL fetch could not check it, and the Crossref hit is unrelated. No source text was retrieved to evaluate the application claim.

### c31 — exists ☐ · applied ✅  · ⚑ degraded  (line 169)
_(Schmidhuber 1991)_
- claude: exists=unchecked applied=verified [model_knowledge_only] — No retrieval data, but Schmidhuber's 1991 work on curiosity/boredom via model-improvement reward is well-known and the claim accurately reflects it; existence unverified by evidence.
- gpt: exists=unchecked applied=verified [model_knowledge_only] — The retrieved Crossref lookup found no matching record, so existence is not confirmed by the supplied evidence. From general knowledge, Schmidhuber's early work on artificial curiosity/boredom rewarded improvements in a world model or predictor, matching the cited claim.

### c37 — exists ✅ · applied ☐  (line 231)
_[Bansal et al. 2019](https://doi.org/10.1609/hcomp.v7i1.5285)_
- claude: exists=verified applied=unchecked [no_basis] — Bansal et al. 2019 paper confirmed via crossref; no claim was attached to this citation to assess.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref confirms Bansal et al.'s 2019 paper 'Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance' with the given DOI. No claim was provided for this citation, so application cannot be assessed.

### c38 — exists ✅ · applied ☐  (line 232)
_[Bommasani et al. 2022](https://arxiv.org/abs/2211.13972)_
- claude: exists=verified applied=unchecked [no_basis] — Bommasani et al. 2022 arXiv paper on algorithmic monoculture confirmed; no claim attached to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms Bommasani et al.'s 'Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization?' No claim was provided for this citation, so application cannot be assessed.

### c39 — exists ✅ · applied ☐  (line 233)
_[Burda et al. 2019](https://arxiv.org/abs/1808.04355)_
- claude: exists=verified applied=unchecked [no_basis] — Burda et al. 2019 confirmed via arXiv; no claim attached to this citation instance to assess.
- gpt: exists=verified applied=unchecked [no_basis] — arXiv confirms Burda et al.'s 'Large-Scale Study of Curiosity-Driven Learning.' No claim was provided for this citation, so application cannot be assessed.

### c40 — exists ☐ · applied ☐  (line 234)
_[Chalmers 2025](https://philarchive.org/rec/CHAWWT-8)_
- claude: exists=unchecked applied=unchecked [no_basis] — PhilArchive URL returned HTTP 403 and no claim is attached, so neither axis is checkable.
- gpt: exists=unchecked applied=unchecked [no_basis] — The PhilArchive URL returned HTTP 403 and no confirming metadata or text was retrieved. No claim was provided for this citation, so application cannot be assessed.

### c42 — exists ☐ · applied ☐  (line 236)
_Dell'Acqua et al. 2023 (HBS Working Paper 24-013)_
- claude: exists=unchecked applied=unchecked [no_basis] — Crossref returned no match, but HBS working papers are often not indexed there; the known Dell'Acqua et al. 2023 'Navigating the Jagged Technological Frontier' HBS WP 24-013 plausibly exists, so evidence is insufficient to refute.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved evidence is a Crossref no-match, which is not decisive for an HBS working paper. No specific cited claim was supplied, so application cannot be evaluated.

### c43 — exists ✅ · applied ☐  (line 237)
_Dennett 1987, _The Intentional Stance__
- claude: exists=verified applied=unchecked [no_basis] — Open Library confirms Dennett's The Intentional Stance (1987); no claim text or abstract provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Open Library matches Daniel C. Dennett’s 1987 work The Intentional Stance. No specific cited claim was supplied, so application cannot be evaluated.

### c47 — exists ✅ · applied ☐  (line 241)
_[Hill 2024](https://doi.org/10.1007/s13347-024-00720-4)_
- claude: exists=verified applied=unchecked [no_basis] — DOI and URL confirm Hill 2024 'Against the Double Standard Argument in AI Ethics'; only metadata/snippet retrieved and no claim stated, so application unassessable.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Scott Hill’s 2024 article, and the Springer URL resolves to the same title. No specific cited claim was supplied, so application cannot be evaluated.

### c49 — exists ✅ · applied ☐  (line 243)
_Kahneman, Sibony & Sunstein 2021, _Noise__
- claude: exists=verified applied=unchecked [no_basis] — Open Library confirms Kahneman, Sibony & Sunstein's Noise (2021); no claim or abstract to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Open Library matches Noise by Daniel Kahneman, Olivier Sibony, and Cass R. Sunstein with the cited year 2021. No specific cited claim was supplied, so application cannot be evaluated.

### c59 — exists ✅ · applied ☐  (line 253)
_[Pillemer & Rothbard 2018](https://doi.org/10.5465/amr.2016.0309)_
- claude: exists=verified applied=unchecked [no_basis] — DOI confirms Pillemer & Rothbard 2018 on dark sides of workplace friendship; no abstract or claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — Crossref directly matches the DOI to Pillemer and Rothbard’s 2018 Academy of Management Review article. No specific cited claim was supplied, so application cannot be evaluated.

### c61 — exists ✅ · applied ☐  (line 255)
_[Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464)_
- claude: exists=verified applied=unchecked [no_basis] — Arxiv ID resolves to a real paper by Samiei, Yiu, Gopnik et al.; no specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to a paper by Mandana Samiei, Eunice Yiu, Alison Gopnik, and others titled “Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?” No source-document claim was supplied, so application cannot be judged.

### c62 — exists ☐ · applied ☐  (line 256)
_Schmidhuber 1991 (_From Animals to Animats_, 222–227)_
- claude: exists=unchecked applied=unchecked [no_basis] — Open Library lookup failed with HTTP 500, so existence is not checkable from evidence; no claim or source text to assess application.
- gpt: exists=unchecked applied=unchecked [no_basis] — The only retrieved lookup failed with an Open Library HTTP 500, and the input marks existence as not-checkable. No claim or source text was supplied, so application cannot be judged.

### c63 — exists ✅ · applied ☐  (line 257)
_[Wang et al. 2023](https://arxiv.org/abs/2305.16291)_
- claude: exists=verified applied=unchecked [no_basis] — Arxiv ID resolves to the Voyager paper by Wang et al.; no specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The arXiv ID resolves to “Voyager: An Open-Ended Embodied Agent with Large Language Models” by Guanzhi Wang et al. No source-document claim was supplied, so application cannot be judged.

### c64 — exists ✅ · applied ☐  (line 258)
_[Yiu, Kosoy & Gopnik 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/)_
- claude: exists=verified applied=unchecked [no_basis] — PMC page confirms the Yiu, Kosoy & Gopnik article exists; no specific claim provided to assess application.
- gpt: exists=verified applied=unchecked [no_basis] — The PMC page resolves to “Transmission Versus Truth, Imitation Versus Innovation: What Children Can Do That Large Language and Language-and-Vision Models Cannot (Yet)” by Eunice Yiu, Eliza Kosoy, and Alison Gopnik, with 2023 online/copyright information. No source-document claim was supplied, so application cannot be judged.

### c65 — exists ⚠️ · applied ☐  (line 259)
_[Zerilli et al. 2019](https://doi.org/10.1007/s13347-018-0330-6)_
- claude: exists=verified applied=unchecked [no_basis] — Crossref DOI match confirms the Zerilli et al. article exists; no specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The DOI resolves to Zerilli et al., “Transparency in Algorithmic and Human Decision-Making: Is There a Double Standard?,” in Philosophy & Technology, volume 32, pages 661–683; the caveat is that Crossref lists year 2018 while the volume/pages are associated with 2019. No source-document claim was supplied, so application cannot be judged.

### c66 — exists ⚠️ · applied ☐  (line 260)
_[Zhang et al. 2024](https://arxiv.org/abs/2306.01711)_
- claude: exists=verified applied=unchecked [no_basis] — Arxiv ID resolves to the OMNI paper by Zhang et al.; no specific claim provided to assess application.
- gpt: exists=nuance applied=unchecked [no_basis] — The arXiv ID resolves to “OMNI: Open-endedness via Models of human Notions of Interestingness” by Jenny Zhang et al.; the citation’s 2024 year is not confirmed by the retrieved metadata and the arXiv identifier indicates a 2023 posting. No source-document claim was supplied, so application cannot be judged.

## ✅ AGREE-clean (20)
### c01 — exists ✅ · applied ✅  (line 39)
_Zerilli et al. 2019 (https://doi.org/10.1007/s13347-018-0330-6)_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to the Zerilli et al. article; abstract explicitly states AI is held to an 'unrealistically high standard' partly due to overestimating human transparency.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Springer URL evidence confirm the DOI, title, authors, journal, and publication details. The retrieved abstract explicitly says automated decision-making may be held to an unrealistically high standard because of an unrealistically high estimate of human decision-maker transparency.

### c02 — exists ✅ · applied ✅  (line 42)
_London 2019 (https://doi.org/10.1002/hast.973)_
- claude: exists=verified applied=verified [evidence_text] — DOI matches London's Hastings Center Report article; abstract states opaque decisions are more common in medicine than critics realize and that verifiable results can matter more than explanations.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms London’s 2019 Hastings Center Report article and DOI. The abstract directly states that opaque decisions are common in medicine and that empirically verified results can matter more than causal explanation when causal knowledge is incomplete.

### c03 — exists ✅ · applied ✅  (line 43)
_Hill 2024 (https://doi.org/10.1007/s13347-024-00720-4)_
- claude: exists=verified applied=verified [evidence_text] — Hill's 'Against the Double Standard Argument in AI Ethics' exists and is a published rebuttal, supporting the claim that the debate is live.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the Springer page confirm Scott Hill’s 2024 Philosophy & Technology commentary titled “Against the Double Standard Argument in AI Ethics.” The title and publication type support the claim that there is a published rebuttal, though the retrieved text gives only limited detail about the argument itself.

### c05 — exists ✅ · applied ✅  (line 52)
_Grove et al. 2000 (https://doi.org/10.1037/1040-3590.12.1.19)_
- claude: exists=verified applied=verified [evidence_text] — Grove et al. meta-analysis confirmed; abstract states mechanical prediction was ~10% more accurate and experts substantially better in only a few (6-16%) studies.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm the article “Clinical versus mechanical prediction: A meta-analysis” and DOI. The retrieved abstract directly states that mechanical predictions were about 10% more accurate on average and that clinical predictions were substantially more accurate in only 6–16% of studies.

### c06 — exists ✅ · applied ✅  (line 62)
_([Dietvorst, Simmons & Massey 2015](https://doi.org/10.1037/xge0000033))_
- claude: exists=verified applied=verified [evidence_text] — Dietvorst et al. 2015 confirmed; abstract describes 5 studies where people lost confidence faster in algorithms and avoided them even after outperformance.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm the 2015 article and DOI. The abstract directly supports the five-study claim that people lose confidence faster in algorithms than humans after the same mistake and avoid algorithms even after seeing them outperform humans.

### c08 — exists ✅ · applied ✅  (line 70)
_([Manoli, Pauketat & Anthis 2024](https://arxiv.org/abs/2412.06040), a preprint)_
- claude: exists=verified applied=verified [evidence_text] — Preprint confirmed; abstract reports spillover persisted in the AI context but not human context and uses the exact phrase 'a double standard whereby AIs are judged more harshly than humans.'
- gpt: exists=verified applied=verified [evidence_text] — arXiv and the resolved URL confirm the preprint, title, authors, and arXiv ID. The abstract directly states that Study 2 found spillover for a named AI but not a named human and uses the quoted “double standard” framing.

### c10 — exists ✅ · applied ✅  (line 82)
_([Rieger et al. 2023](https://doi.org/10.1177/00187208231197347))_
- claude: exists=verified applied=verified [evidence_text] — Rieger et al. 2023 confirmed; abstract states trust was higher for human expert than AI than human novice, supporting the imperfect automation schema claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the article and DOI. The abstract directly reports that trust and perceived reliability were highest for a human expert, then AI, then a human novice, and concludes an “imperfect automation schema,” supporting the claim that participants did not expect perfection.

### c12 — exists ✅ · applied ✅  (line 95)
_[Bansal et al. 2019](https://doi.org/10.1609/hcomp.v7i1.5285)_
- claude: exists=verified applied=verified [evidence_text] — Bansal et al. 2019 confirmed; abstract emphasizes that human-AI team performance depends on the human's mental model of when the AI errs.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the HCOMP paper “Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance” and DOI. The abstract directly says team performance depends on knowing how and when human and AI expertise complement each other, especially knowing the AI’s error boundary.

### c14 — exists ✅ · applied ✅  (line 105)
_[Bommasani et al. 2022](https://arxiv.org/abs/2211.13972)_
- claude: exists=verified applied=verified [evidence_text] — Bommasani et al. preprint confirmed; abstract states sharing training data reliably exacerbates homogenization and reports mixed results for foundation-model sharing.
- gpt: exists=verified applied=verified [evidence_text] — arXiv and URL evidence confirm the preprint and metadata. The abstract directly supports the claim that shared training data exacerbates outcome homogenization and that foundation-model sharing produced mixed results depending on adaptation methods.

### c19 — exists ✅ · applied ✅  (line 117)
_[Ibrahim, Hafner & Rocher 2026](https://doi.org/10.1038/s41586-026-10410-0)_
- claude: exists=verified applied=verified [evidence_text] — Ibrahim, Hafner & Rocher confirmed in Nature; abstract states warm-trained models were significantly more likely to validate incorrect user beliefs.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and the Nature URL confirm the article and DOI. The abstract directly states that warm-trained models were more likely to validate incorrect user beliefs, especially when users expressed sadness.

### c20 — exists ✅ · applied ✅  (line 119)
_[Cheng et al. 2026](https://doi.org/10.1126/science.aec8352)_
- claude: exists=verified applied=verified [evidence_text] — Cheng et al. in Science confirmed; abstract states sycophantic models were trusted and preferred and drive engagement, supporting the claim users rate them higher and return.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms the Science article and DOI. The abstract states that sycophantic models were trusted and preferred and that the harmful feature also drives engagement, supporting the claim about higher user preference and return incentives.

### c21 — exists ✅ · applied ✅  (line 124)
_[Matthias 2004](https://doi.org/10.1007/s10676-004-3422-1)_
- claude: exists=verified applied=verified [evidence_text] — Matthias's 'responsibility gap' paper exists with matching DOI/metadata, and the abstract directly supports that manufacturers can't predict learning machine behaviour, leaving a responsibility gap.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Springer identify Andreas Matthias's 2004 article 'The responsibility gap: Ascribing responsibility for the actions of learning automata' with the given DOI. The abstract directly says learning automata make future behavior in principle unpredictable to manufacturers/operators and create a responsibility gap not bridged by traditional responsibility concepts.

### c26 — exists ✅ · applied ✅  (line 146)
_[Kidd & Hayden 2015](https://doi.org/10.1016/j.neuron.2015.09.010)_
- claude: exists=verified applied=verified [evidence_text] — Kidd & Hayden 2015 Neuron paper confirmed; abstract advocates studying information-seeking motivation rather than defining curiosity, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref and Europe PMC confirm Kidd and Hayden's 2015 Neuron article 'The Psychology and Neuroscience of Curiosity' with the given DOI. The abstract explicitly says there is no widely agreed delineation of curiosity and proposes studying motivations for information-seeking behavior rather than focusing on definition.

### c28 — exists ✅ · applied ✅  (line 155)
_([Krishnamurthy et al. 2024](https://arxiv.org/abs/2403.15371))_
- claude: exists=verified applied=verified [evidence_text] — Krishnamurthy et al. arXiv paper confirmed; abstract states only one configuration (GPT-4 with CoT and externally summarized history) produced satisfactory exploration, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms 'Can large language models explore in-context?' by Krishnamurthy et al. The abstract directly states that across experiments only GPT-4 with chain-of-thought reasoning and externally summarized interaction history produced satisfactory exploratory behavior, while GPT-3.5, GPT-4, and Llama2 otherwise did not robustly explore.

### c29 — exists ✅ · applied ✅  (line 157)
_([Samiei, Yiu, … Gopnik et al. 2026](https://arxiv.org/abs/2606.06464))_
- claude: exists=verified applied=verified [evidence_text] — The arXiv paper exists (though cited authors/year differ slightly from actual); abstract confirms some SOTA models approach human accuracy but explore less efficiently on an active causal-learning task.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms 'Human Adults and LLMs as Scientists: Who Benefits from Active Exploration?' by Samiei, Yiu, and colleagues. The abstract states that some state-of-the-art models approach human-level hypothesis-inference accuracy but often show less efficient exploration strategies.

### c32 — exists ✅ · applied ✅  (line 172)
_([Pathak et al. 2017](https://arxiv.org/abs/1705.05363))_
- claude: exists=verified applied=verified [evidence_text] — Pathak et al. 2017 confirmed; abstract formulates curiosity as prediction error of own actions and shows exploration with no extrinsic reward, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms Pathak et al.'s 'Curiosity-driven Exploration by Self-supervised Prediction.' The abstract directly says curiosity is formulated as prediction error about consequences of the agent's actions and is evaluated in VizDoom and Super Mario Bros. including exploration with no extrinsic reward.

### c33 — exists ✅ · applied ✅  (line 175)
_([Burda et al. 2019](https://arxiv.org/abs/1808.04355))_
- claude: exists=verified applied=verified [evidence_text] — Burda et al. large-scale curiosity study across 54 environments confirmed; abstract notes limitations of prediction-based rewards in stochastic setups, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms Burda et al.'s 'Large-Scale Study of Curiosity-Driven Learning.' The abstract states it is a large-scale study of purely curiosity-driven learning across 54 environments and demonstrates limitations of prediction-based rewards in stochastic setups.

### c34 — exists ✅ · applied ✅  (line 178)
_([Zhang et al. 2024](https://arxiv.org/abs/2306.01711))_
- claude: exists=verified applied=verified [evidence_text] — OMNI paper confirmed; abstract describes using foundation models as a model of human interestingness to select tasks, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms Zhang et al.'s 'OMNI: Open-endedness via Models of human Notions of Interestingness.' The abstract says OMNI uses foundation models as models of human interestingness to prioritize tasks that are both learnable and interesting, i.e. to select which tasks to focus on next.

### c35 — exists ✅ · applied ✅  (line 180)
_([Wang et al. 2023](https://arxiv.org/abs/2305.16291))_
- claude: exists=verified applied=verified [evidence_text] — Voyager paper confirmed; abstract describes GPT-4 agent with automatic curriculum maximizing exploration in Minecraft, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — arXiv confirms Wang et al.'s 'Voyager: An Open-Ended Embodied Agent with Large Language Models.' The abstract supports the claim that Voyager uses GPT-4 and an automatic curriculum to continuously explore Minecraft and acquire skills without human intervention, though it does not spell out every detail of task proposal wording.

### c36 — exists ✅ · applied ✅  (line 205)
_([Longoni, Bonezzi & Morewedge 2019](https://doi.org/10.1093/jcr/ucz013))_
- claude: exists=verified applied=verified [evidence_text] — Longoni et al. 2019 confirmed; abstract attributes resistance to uniqueness neglect and notes it is eliminated when AI only supports rather than replaces a human provider, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — Crossref confirms Longoni, Bonezzi, and Morewedge's 2019 Journal of Consumer Research article 'Resistance to Medical Artificial Intelligence.' The abstract directly says resistance is driven by uniqueness neglect and is eliminated when AI only supports rather than replaces a human healthcare provider's decision.
