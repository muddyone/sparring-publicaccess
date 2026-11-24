# Essay 08: three sources checked against the originals (2026-11-23)

_The three items brief 14 flagged to check before the essay leaned on them. Checked by a research agent
against primary text; quotes are from the sources named._

| Source | Result | What the essay says now |
|---|---|---|
| Bastani et al. 2025, PNAS, and its correction (e2518204122) | **Verified.** The correction fixes one author's affiliation only ("due to a production error, the affiliation for Osbert Bastani appeared incorrectly"; Europe PMC PMC12403119). The figures "48% improvement in grades for GPT Base", "17% reduction in grades for GPT Base" and "nearly a thousand high school math students" are in the abstract (PMC12232635). | Unchanged. |
| FAA SAFO 13002 (4 Jan 2013) | **Verified** from the PDF itself. "This SAFO encourages operators to promote manual flight operations when appropriate." "…identified an increase in manual handling errors." "…continuous use of those systems does not reinforce a pilot's knowledge and skills in manual flight operations." It also credits automation with improved safety. | Quotes the SAFO directly; "when appropriate" kept. |
| Brynjolfsson, Li & Raymond 2025, QJE ("evidence that AI assistance facilitates worker learning") | **Partly verified.** QJE page refused (403); read arXiv 2304.11771 v2, whose abstract matches the QJE abstract on Crossref, and NBER w31161. Learning is measured by chat handling time during outages, against the worker's own baseline; it holds for high-adherence workers only; "AI outages are rare and not necessarily random"; estimates "are noisy". No test of workers who lost access for good. | Adds those limits in one sentence. |

**Addendum (11-23, after panel round 1).** The essay's "after three months with it" is from the same check:
arXiv 2304.11771 v2, "if an outage occurs after three months of exposure to AI recommendations, workers handle
the chat faster—even though they are not receiving direct AI assistance." "Rare" and "not necessarily random"
are the paper's words.

**Addendum (11-24): why the developers were slower (Becker et al. 2025).** Read in arXiv 2507.09089 v2 HTML,
§3.3 Table 1 and §4.1. The authors list 21 candidate factors and name no single cause ("we strongly caution
against over-indexing on the basis of any individual pieces of evidence"). Likely contributors include high
familiarity ("Developers slowed down more on issues they are more familiar with"), large and complex repositories
(average ">1,100,000 lines of code", about 10 years old), low AI reliability ("Developers accept <44% of AI
generations"; "9% of time spent reviewing/cleaning AI outputs"; majority made "major changes to clean up AI
code"), and implicit context. §4.1: results "are consistent with small greenfield projects or development in
unfamiliar codebases seeing substantial speedup from AI assistance." The "<44%" renders as "<<44%" in the HTML;
read as "under 44%" (essay: "fewer than half").
