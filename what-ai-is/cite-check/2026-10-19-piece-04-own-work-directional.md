# cite-check report — piece04-own-work-directional

_Public-copy note: the two "refuted" verdicts below (c04, c05) are failed lookups on the figures from the author's own published report ([Paper 1](https://doi.org/10.5281/zenodo.21210264)), not wrong sources. The figures were checked by hand against the report (see the [cite-check index](README.md))._

**Source:** a working draft of one passage of `positions/04-personality.md` (`04-own-work-directional.md`, not kept)  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **5** citations checked
- existence independently confirmed: **3**
- application evidence-grounded: **3**
- application judged from model knowledge only: **0**
- not independently checkable: **0**
- buckets — clean **0** · problem **2** · disagree **3**

## ⛔ DISAGREE — escalate to human (3)
### c02 — exists ✅ · applied SPLIT  (line 11)
_([my published report](https://doi.org/10.5281/zenodo.21210264), sections 6 and 7; figures in the notes)_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [evidence_text] — The Zenodo DOI resolves to Niedner's SPARRING empirical report containing a pre-registration, rater study, and seeded-defect governance pilots, consistent with the adversarial-review findings cited; the Crossref 'null paper' snippet is a false match.
- gpt: exists=verified applied=unchecked [no_basis] — The DOI URL resolves to a Zenodo record for an empirical report, despite Crossref not having the DOI and returning an unrelated low-similarity item. The retrieved application text is from that unrelated Crossref item and does not provide source text from the Zenodo report supporting the specific section 6/7 claims.

### c04 — exists SPLIT · applied ☐  (line 19)
_**Catching flaws (section 6):** the AI told to attack the draft caught 87% of its serious flaws. The AI that wrote the draft caught 68% reviewing its own work, and a neutral second reader 55%._
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — This references section 6 of the author's own report; no specific text or figures were retrieved to confirm the exact percentages.
- gpt: exists=refuted applied=unchecked [no_basis] — No identifiable bibliographic work, DOI, URL, or matched record is provided, and the only lookup found no match. No source text was retrieved to assess the numerical claims.

### c05 — exists SPLIT · applied ☐  (line 21)
_**Backing objections (section 7):** reviews required to back each objection with something checkable did so 96% of the time. A tough skeptic managed 83%, and a plain single pass 58%._
- **escalate:** existence: unchecked vs refuted
- claude: exists=unchecked applied=unchecked [no_basis] — This references section 7 of the author's own report; no specific text or figures were retrieved to confirm the exact percentages.
- gpt: exists=refuted applied=unchecked [no_basis] — No identifiable bibliographic work, DOI, URL, or matched record is provided, and the only lookup found no match. No source text was retrieved to assess the numerical claims.

## ⚠️ AGREE-problem (2)
### c01 — exists ✅ · applied ⚠️  (line 3)
_([Zheng et al. 2024](https://doi.org/10.18653/v1/2024.findings-emnlp.888))_
- claude: exists=verified applied=verified [evidence_text] — DOI resolves to Zheng et al. 2024 EMNLP Findings paper, whose title states personas in system prompts do not improve LLM performance, supporting the role-prompt claim.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI resolves and Crossref/ACL metadata identify the 2024 Findings EMNLP paper by Zheng et al. The retrieved title supports the broad claim that personas in system prompts do not improve LLM performance, but the snippet does not verify the specific details about 162 role prompts, four model families, or factual-question accuracy.

### c03 — exists ✅ · applied ⚠️  (line 17)
_([report](https://doi.org/10.5281/zenodo.21210264))_
- claude: exists=verified applied=verified [evidence_text] — Same report resolves on Zenodo and explicitly describes a locked pre-registration and governance pilots, supporting the claim that the pilots were small and pre-registered.
- gpt: exists=verified applied=nuance [evidence_text] — The DOI resolves to a Zenodo record titled as an empirical report on SPARRING's Resolver. The snippet supports that the record includes a locked pre-registration and governance pilots, but it does not verify that both pilots were small or that AI did the scoring.
