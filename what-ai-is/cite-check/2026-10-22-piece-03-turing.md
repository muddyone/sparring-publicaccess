# cite-check report — 03-turing-addition-2

_Hand check, 2026-10-22: the checker could not read the regulation (the Federal Register site served a CAPTCHA), so c02 was checked by hand against the official text of 45 CFR 46.116(f)(3)(i), (ii), (iv) and (v), retrieved through eCFR's renderer API: minimal risk; not practicable without the alteration; no adverse effect on rights and welfare; and, whenever appropriate, additional pertinent information after participation. It matches the sentence. An earlier draft cited APA Ethics Code Standard 8.07, which could not be retrieved and whose paraphrase one judge flagged; it was replaced._

**Source:** a draft of the Turing-test passage of `positions/03-someone-there.md` (`03-turing-addition.md`, not kept)  ·  prompt `v1`  ·  substrates `claude-opus-4-8` + `gpt-5.5-2026-04-23`

## Coverage (read this first)
- **2** citations checked
- existence independently confirmed: **2**
- application evidence-grounded: **2**
- application judged from model knowledge only: **1**
- not independently checkable: **0**
- buckets — clean **1** · problem **0** · disagree **1**

## ⛔ DISAGREE — escalate to human (1)
### c02 — exists ⚠️ · applied SPLIT  · ⚑ degraded  (line 10)
_([45 CFR 46.116(f)](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-46/section-46.116))_
- **escalate:** application: verified vs unchecked
- claude: exists=verified applied=verified [model_knowledge_only] — The eCFR URL resolved but returned a bot-block page with no substantive text; 45 CFR 46.116(f) is a real regulation whose waiver/alteration criteria (minimal risk, infeasibility, no adverse effect on rights/welfare, debriefing where appropriate) match the described claim from my knowledge.
- gpt: exists=nuance applied=unchecked [no_basis] — The URL lookup reached an official Federal Register/eCFR access-gate page, which is consistent with the cited regulatory source but does not display or confirm the specific section text. The retrieved snippet is only a CAPTCHA/access message and contains no substantive text of 45 CFR 46.116(f), so it cannot be used to verify the claim.

## ✅ AGREE-clean (1)
### c01 — exists ✅ · applied ✅  (line 6)
_([Jones & Bergen 2025](https://arxiv.org/abs/2503.23674))_
- claude: exists=verified applied=verified [evidence_text] — The arXiv abstract matches by ID and directly states GPT-4.5 with a humanlike persona was judged to be the human 73% of the time, exactly supporting the claim.
- gpt: exists=verified applied=verified [evidence_text] — The arXiv lookup by ID confirms the work exists as 'Large Language Models Pass the Turing Test' by Cameron R. Jones and Benjamin K. Bergen. The retrieved abstract directly states that GPT-4.5, when prompted to adopt a humanlike persona, was judged human 73% of the time.
