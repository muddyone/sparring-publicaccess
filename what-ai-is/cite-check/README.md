# cite-check reports

Output of Loom's `/cite-check` on the research reports. Each citation is
resolved against live sources (Crossref, arXiv, Europe PMC, Open Library, the
cited URL). Two models from different vendors then judge each one separately:
does the source exist, and does it support the claim it is cited for?

- [2026-10-15 · Personality and connection](2026-10-15-personality-and-connection.md):
  75 citations, 71 confirmed to exist, none wrong or invented.
- [2026-10-15 · Chalmers and AI minds](2026-10-15-chalmers-and-ai-minds.md):
  79 citations, 61 confirmed to exist, none wrong or invented.

**How to read them.** Read the coverage block first. A verdict marked
"model knowledge only" or "⚑ degraded" is not a verification. Most "problem"
and "disagree" entries mean the checker could reach only the abstract, so a
figure or quote from the body of a paper could not be confirmed. The rest are
pages that blocked it (PhilArchive, openai.com).

**Corrections made after the 2026-10-15 run.** The reports show the text as it
was checked. Three statements in the personality report were corrected
afterwards:

- The Woebot bond moved to the short-studies column of the table. It was
  measured within 5 days.
- The MIT/OpenAI trial varied the chatbot's voice and the kind of
  conversation, not its "personality".
- The warmth figures (7 and 12 points) are now attributed to the preprint's
  results, alongside the 10–30 point range in the published *Nature* abstract.
- [2026-10-16 · Does it learn? (learning-and-gopnik)](2026-10-16-learning-and-gopnik.md):
  16 citations, none wrong or invented; claims the tool could not reach were then checked by hand
  against full texts (addendum), which corrected one overstatement and replaced a dead link.
- [2026-10-19 · essay 04, own-work passage in words](2026-10-19-piece-04-own-work-directional.md):
  the passage was rewritten in words, and the figures moved to a note. 5 citations, none wrong.
  The two "refuted" verdicts are lookups that failed on the author's own figures. Those were
  checked by hand against the report (§6.3 87.1 / 67.7 / 54.8, §7 96.3 / 83.3 / 58.3; both pilots
  pre-registered).
- 2026-10-19 · essay 05, two claims checked by hand against the papers (no tool run). **Li et al.
  2026** (JESP 125, 104911), from the full published text: it confirms the two-week randomized design
  with first-semester students, that loneliness fell only in the human-peer arm, and that the
  chatbot did no better than journaling. It shows the negative-mood benefit is exploratory, that the
  peer was a randomly paired fellow student (they had met once in the lab, so not a stranger), and
  that the chatbot was built to "embody the qualities of an ideal friend". **Heinz et al. 2025**
  (NEJM AI): the published abstract confirms N=210, a 4-week trial and a waitlist control. The
  outcomes, from the 2024 preprint, were depression, anxiety, and symptoms in people at high risk
  for an eating disorder. The published Results were behind a 403, so the 51%/31% figures and the
  lead author's "not ready" remark stay attributed to the Dartmouth press release. The essay's
  "paper not checked" notes were removed.
- 2026-10-19 · essay 05, Fang et al. 2025 checked by hand against the full arXiv text. It confirms
  "no limits beyond the required usage duration" (a five-minute daily minimum), and that the study
  used "OpenAI's existing safety guardrails". It contradicts the essay's earlier claim that nothing
  "steered anyone back toward people": prosocial behaviour "mostly appeared through empathetic
  responses and behaviors that encourage social connection", and replies advising limits on AI use
  ran at about 0.5–0.7%. The bullet was corrected to match.
