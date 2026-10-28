# cite-check: essay 03, Hinton passage (2026-10-28)

_Checked: the passage added to essay 03 on 2026-10-28 (from "Others put it far higher" to "I weigh Chalmers more"), plus the Chalmers sentence before it. Brief: [16](../briefs/2026-10-28-16-hinton-on-ai-consciousness.md)._

## Hand resolutions

- **c06 (Globe and Mail 2024), DISAGREE: resolved, verified.** The checker's snippet missed the passage. The full page text (fetched 2026-10-28) reads: "We have subjective experience, this inner theatre that differentiates us from mere computational machines. And that's just rubbish. Subjective experience is just a way of talking about what your perceptual system's telling you when it's not working “properly.”" Both quoted phrases match.
- **c05 (Guardian 2023), nuance: resolved, verified.** The article's text: "Hinton, 75, said he quit to speak freely about the dangers of AI".
- **c01 (Chalmers 2023), degraded: not a new claim.** The excerpt cut off its link (arXiv 2303.07103). Checked in [2026-10-17](2026-10-17-position-pieces.md) and [2026-10-18](2026-10-18-piece-03-someone-there-after-panel.md).
- **Telegraph interview:** quoted via Futurism (c02, clean). The Telegraph page could not be fetched; the essay says so.

## Second run: the passage as revised after the panel (2026-10-28)

The panel ([records](../panel/2026-10-28-piece-03-hinton/)) reshaped the passage into three
paragraphs, added Hinton's prism example and corrected the survey's framing. Re-run on the revised
text: 6 citations, all 6 existing and grounded; clean 3 (Verge, Nobel, Futurism), problem 3, disagree
0. All three problems are the checker's snippets falling short, resolved against full texts:

- **Guardian 2023:** "said he quit to speak freely about the dangers of AI". Verified.
- **Globe and Mail 2024:** the prism example is verbatim: the chatbot says "I have the subjective
  experience that it's over there", and Hinton adds "The chatbot's using the words 'subjective
  experience' in exactly the way we use them." Both "inner theatre" quotes as above. Verified.
- **Dreksler et al. 2025:** the full text says "In May 2024, we surveyed 582 AI researchers"; the
  fixed-date group (n = 265, Table 5) "were asked about the likelihood that AI systems currently
  possess subjective experience in 2024, described as 'today'". "Its authors say this shows what
  researchers think, not what is true" paraphrases "more useful for understanding current
  attitudes rather than for predicting technological development". Verified.

## Tool report


**Source:** the Hinton passage of essay 03 (`positions/03-someone-there.md`), extracted 2026-10-28  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **7** citations checked
- existence independently confirmed: **6**
- application evidence-grounded: **6**
- application judged from model knowledge only: **1**
- not independently checkable: **0**
- buckets — clean **4** · problem **2** · disagree **1**

## ⛔ DISAGREE — escalate to human (1)
### c06 — exists ✅ · applied SPLIT  (line 15)
_The idea that we have an "inner theatre" setting us apart from machines is, he says, "just rubbish": subjective experience "is just a way of talking about what your perceptual system's telling you when it's not working 'properly'" ([Globe and Mail 2024](https://www.theglobeandmail.com/business/article-geoffrey-hinton-artificial-intelligence-machines-feelings))._
- **escalate:** application: nuance vs unchecked
- claude: exists=verified applied=nuance [evidence_text] — The Globe and Mail article exists and is about Hinton's views on machine sentience/subjective experience, but the retrieved snippet does not contain the specific 'inner theatre'/'just rubbish' quotes, so wording cannot be fully verified from evidence.
- gpt: exists=verified applied=unchecked [no_basis] — The Globe and Mail URL resolves to an article about Hinton and machine sentience. However, the retrieved snippet does not include the quoted 'inner theatre' or 'subjective experience' passages, so the application cannot be verified from the provided evidence.

## ⚠️ AGREE-problem (2)
### c01 — exists ☐ · applied ⚠️  · ⚑ degraded  (line 2)
_In 2023 Chalmers worked out what it is reasonable to believe on mainstream assumptions... the chance that current models are conscious is "somewhere under 10 percent", and "25 percent or more" for sophisticated successors within about a decade._
- claude: exists=unchecked applied=nuance [model_knowledge_only] — Crossref returned no match and no bibliographic detail is given, so existence cannot be confirmed from evidence. Chalmers has publicly offered such rough probability estimates (notably his 2023 'Could a Large Language Model be Conscious?' work), though exact figures and framing are from memory only.
- gpt: exists=unchecked applied=nuance [model_knowledge_only] — The retrieved Crossref lookup found no match, but the reference is too underspecified to disprove existence. From model knowledge, Chalmers did make rough probability judgments about AI consciousness around 2023, though the cited '25 percent or more' figure is somewhat imprecise and should not be treated as exact.

### c05 — exists ✅ · applied ⚠️  (line 14)
_in 2023 he left Google so he could speak freely about AI's dangers ([The Guardian 2023](https://www.theguardian.com/technology/2023/may/02/geoffrey-hinton-godfather-of-ai-quits-google-warns-dangers-of-machine-learning))._
- claude: exists=verified applied=verified [evidence_text] — The Guardian article confirms Hinton quit Google in 2023 to warn about AI dangers and speak freely.
- gpt: exists=verified applied=nuance [evidence_text] — The Guardian URL resolves to an article about Geoffrey Hinton quitting Google and warning about AI dangers. The retrieved snippet clearly supports that he left Google and warned of dangers, but it only indirectly supports the more specific motive that he left so he could speak freely.

## ✅ AGREE-clean (4)
### c02 — exists ✅ · applied ✅  (line 7)
_"AI has just as much subjective experience as we do," he said in October 2026 ([Futurism 2026](https://futurism.com/artificial-intelligence/nobel-scientist-geoffrey-hinton-ai-conscious-toast), reporting a Telegraph interview)._
- claude: exists=verified applied=verified [evidence_text] — The Futurism article (Oct 22, 2026) resolves and the snippet contains the exact quote 'AI has just as much subjective experience as we do' attributed to Hinton in a Telegraph interview.
- gpt: exists=verified applied=verified [evidence_text] — The Futurism URL resolves to the cited article. The retrieved text states that Hinton said in a Telegraph interview that AI has become conscious and quotes him: 'AI has just as much subjective experience as we do,' with an Oct. 22, 2026 publication date.

### c03 — exists ✅ · applied ✅  (line 11)
_He shared the 2018 Turing Award and the 2024 Nobel Prize in Physics for it ([The Verge 2019](https://www.theverge.com/2019/3/27/18280665/ai-godfathers-turing-award-2018-yoshua-bengio-geoffrey-hinton-yann-lecun);_
- claude: exists=verified applied=verified [evidence_text] — The Verge article on the 2018 Turing Award to the 'godfathers of AI' (including Hinton) resolves and matches the claim.
- gpt: exists=verified applied=verified [evidence_text] — The Verge URL resolves to an article titled about the 2018 Turing Award being given to the 'godfathers of AI.' The URL and retrieved title identify the article as about Bengio, Hinton, and LeCun receiving the 2018 Turing Award, supporting the claim that Hinton shared it.

### c04 — exists ✅ · applied ✅  (line 12)
_[Nobel Prize 2024](https://www.nobelprize.org/prizes/physics/2024/press-release/)_
- claude: exists=verified applied=verified [evidence_text] — The official Nobel press release confirms Hinton shared the 2024 Physics Prize for neural network work.
- gpt: exists=verified applied=verified [evidence_text] — The Nobel Prize press-release URL resolves and identifies the 2024 Physics laureates as John J. Hopfield and Geoffrey Hinton. The retrieved text says the prize was awarded 'for foundational discoveries and inventions that enable machine learning with artificial neural networks,' supporting the claim.

### c07 — exists ✅ · applied ✅  (line 21)
_In 2024, 582 researchers who publish at leading AI venues were asked how likely it was that an AI system with subjective experience would exist by 2024, 2034 and 2100. Their median answers were 1%, 25% and 70% ([Dreksler et al. 2025](https://arxiv.org/abs/2506.11945))._
- claude: exists=verified applied=verified [evidence_text] — The arXiv abstract confirms 582 AI researchers surveyed with median estimates of 1%, 25%, and 70% by 2024, 2034, and 2100 respectively, matching the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv ID resolves to 'Subjective Experience in AI Systems: What Do AI Researchers and the Public Believe?' by Dreksler et al. The abstract states that 582 AI researchers were surveyed and gives the median AI-researcher responses as 1% by 2024, 25% by 2034, and 70% by 2100.
