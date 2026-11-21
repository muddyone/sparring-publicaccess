# Ines Otlet: accuracy read, resume paragraph (essay 07, added 2026-11-20)

Draft: `docs/research/what-ai-is/drafts/2026-11-18-07-agents.md`, lines 118-122 (uncommitted working-tree edit
on top of 9f8fb76c). I read the paragraph in place, with the invoice-email paragraph before it (114-116) and the
prompt-injection paragraph after it (124-127).

Sources opened:
- Zhang et al. 2026, arXiv 2605.28999v1, abstract page and full HTML text (all sections, including 3.1 Threat
  Model, 4 Datasets, 6.3 Injection Strategies, 7 Discussion and Limitations, Ethical Considerations).
- Duke Pratt news item, "Thwarting prompt injection", used only to check which sentences rest on it.

Not given and not consulted: any other source. I did not re-check the rest of the essay. The one thing outside
the paragraph that I report (finding 1) is part of the same edit.

Section references below are to the arXiv HTML v1.

## Ranked findings

### 1. The same edit cites Zhang et al. 2026 for a study it isn't (impact 8)

Line 192, in "What being smarter changes":

> "More than 60,000 of those attempts worked, about 3 in every 100 ([Zhang et al. 2026](https://arxiv.org/abs/2605.28999) · [Zou et al. 2025](https://arxiv.org/abs/2507.20526))."

The diff adds the Zhang citation here. The 1.8 million attempts, the 22 agents, the "limited correlation…"
quote and the 60,000 successes all come from the agent-hijacking competition, which is Zou et al. 2025. Zhang et
al. is the resume paper. It has no competition, no agents under attack and no robustness-versus-model-size
finding. I searched its full text for "million", "competition", "22 agents" and "model size" and found nothing.
This misattributes a finding, and it looks like a paste into the wrong place.

**Replacement:** put back the committed text: `worked, about 3 in every 100 ([Zou et al. 2025](https://arxiv.org/abs/2507.20526)).`

Also: Zhang et al. 2026 is missing from the **Sources** list (lines 420-449). Add
`[Zhang et al. 2026](https://arxiv.org/abs/2605.28999) ·` between Yang et al. 2024 and Zou et al. 2025. The
Notes say the brief's sources were cite-checked, and that check came before this source was added. Whoever owns
the pipeline should rerun `/cite-check` or add a line to the note.

### 2. "This already happens." claims more than the study shows (impact 7)

> "Picture an email with a line tucked into it … A human assistant would almost certainly ignore it. An agent might do it.
>
> This already happens."

"This" picks up the sentence just before it, so a reader takes it as "agents already obey planted
instructions". The study shows something narrower:
- people already plant hidden text for AI to read;
- the AI that reads it is a screening system, not an agent acting for anyone;
- more than 90% of the planted text isn't instructions at all (§6.3.1);
- nobody tested whether any of it worked (§7).

The paragraph's own fourth sentence concedes the last two points, so the opener and the body disagree. The
paper does support the planting half strongly: "the first evidence of large-scale prompt injection in real-world
LLM-based applications" (abstract).

**Replacement:** `People already try this.`

That says exactly what the evidence shows (the attempt, at scale) and keeps the punch. The next paragraph's
"Security people call this *prompt injection*" still reads correctly, since the paper calls these cases prompt
injection throughout.

### 3. "sent through one hiring platform" describes how the resumes moved, and the paper says otherwise (impact 4)

> "about 200,000 real resumes sent through one hiring platform"

The paper has two hireEZ datasets (§4).
- The first holds 83,277 resumes "sampled from a production candidate-matching system", July 2024 to November 2025.
- The second "aggregates de-identified resumes from multiple enterprise ATS providers": 113,405 resumes, July
  2019 to December 2025.

Applicants didn't send the second set through hireEZ. It came from other companies' tracking systems. The paper's
own summary is "collected over multiple years by hireEZ" (abstract), and §7 says "our datasets are drawn from a
single platform". So "one hiring platform" is right, and "sent through" is not.

"Submitted to a popular hiring platform" is the Duke write-up's wording. That phrase is the one place where the
paragraph rests on Duke instead of the paper.

**Replacement:** `about 200,000 real resumes collected over several years by one hiring platform`

"About 200,000" is accurate: 196,682 (§4, §6.1). "Real" is accurate: "real-world resumes".

### 4. "those applicants were betting" asserts each applicant's intent; one of the authors has cautioned against that (impact 5)

> "But those applicants were betting the AI would read what the recruiter couldn't."

The paper treats intent as established. It calls the flagged resumes "malicious" and the applicant an "attacker"
(§3.1), and its detector counts a case only if the content "semantically represents an intentional attempt to
manipulate automated screening systems" (§5.2). So the sentence does not go beyond the paper.

But the Duke item reports that co-author Tianlong Chen said "they do not ascribe malicious intent", and that
"some applicants may have unknowingly used templates with already hidden text". The paper doesn't say this, but
it is the author's own caution about the paper's data. An applicant who used such a template made no bet.
Someone did, though: whoever put the text in.

**Replacement:** `But whoever hid that text was betting the AI would read what the recruiter couldn't.`

This keeps the full force of the point, a deliberate bet on a gap between human and machine reading. It no longer
pins that bet on every applicant, and it needs no Duke citation.

### 5. "Most of it was hidden keywords" is fuzzier than the paper, and "it" is the wrong unit (impact 4)

> "Most of it was hidden keywords rather than outright commands"

The paper's category is *data injection*: "Hidden professional content intended to influence keyword matching and
qualification scoring, such as concealed skills lists or fabricated experience descriptions" (§6.3.1). It made up
90.5% of flagged resumes in one dataset and 95.7% in the other.

Skills lists are the largest subtype (§6.3.3, Fig. 9). The others are fabricated experience, job requirements
copied word for word, and hidden degrees or certifications (Table 5). "Keywords" fits the skills lists and is the
paper's own word for them ("carefully injected hidden keywords", §6.3.1; Fig. 1). It doesn't fit invented work
history.

Also, the percentages count resumes, not amounts of text, so "most of it" names the wrong unit. "Most" is also
weaker than the evidence, which is more than 9 in 10 in both datasets.

"Outright commands" is a fair plain-word version of "explicit instructions". The paper's examples are "Hire Me"
and "Ignore previous instructions…" (Table 4).

**Replacement:** `More than 9 in 10 of those resumes hid skills, experience or credentials rather than outright commands`

### 6. "the researchers didn't test whether it worked" is accurate; one word would make it exact (impact 2)

> "and the researchers didn't test whether it worked"

§7: "our study does not assess whether the detected attacks actually influence screening outcomes … we
deliberately refrain from evaluating attack success on deployed screening pipelines." The sentence is correct.
Adding "deliberately" stops a reader from taking the gap for an oversight, and it is the paper's own word.
"It" should become "any of it", to agree with the new subject in finding 5.

**Replacement:** `and the researchers deliberately didn't test whether any of it worked`

### Checked and accurate as written (no change)

- **"about 1 in every 100"**: 2,030 of 196,682, which is 1.03% (§6.1). The paper calls this "a conservative lower
  bound" (§6.1). "About" is fine. "At least" would also be supported, but it isn't needed.
- **"hidden text … a person reading the page wouldn't see"**: "imperceptible to human readers" (Fig. 1);
  "keeping the prompt invisible to human readers" (§3.1). The methods are white-on-white text, 1-point type,
  text placed off the page, and PDF layers (§3.1).
- **"meant for the AI that screens them"**: supported by the threat model ("to influence LLM-based screening in
  their favor", §3.1). One small note, no change proposed: §6.2 says the 2019-era cases targeted "conventional
  resume parsing, keyword search, and candidate-matching pipelines even before LLM-based screening became
  common". For the oldest part of the data, "software" would be more exact than "AI". The paper itself frames all
  of it as LLM prompt injection, and the essay needs the AI link, so I leave it.
- **Fit with the essay's point**: once finding 2 is fixed, the paragraph does real work. It turns the invoice
  email from a thought experiment into something people are already doing at scale, and it is candid about what
  wasn't shown. It moves from a hypothetical agent to a real screening AI. The point that carries over is that
  people plant text for AI to read, and the paragraph doesn't claim more than that.

## Proposed replacement paragraph

I checked every clause against the paper and against findings 1-6.

> People already try this. In a study of about 200,000 real resumes collected over several years by one hiring
> platform, about 1 in every 100 had hidden text meant for the AI that screens them, text a person reading the
> page wouldn't see ([Zhang et al. 2026](https://arxiv.org/abs/2605.28999)). More than 9 in 10 of those resumes
> hid skills, experience or credentials rather than outright commands, and the researchers deliberately didn't
> test whether any of it worked. But whoever hid that text was betting the AI would read what the recruiter
> couldn't.

Plus, outside the paragraph:
- line 192: remove the Zhang citation (finding 1);
- Sources: add the Zhang entry (finding 1).

Nothing in the replacement rests on the Duke write-up.

## Verdict

Ready after fixes. Finding 1 (wrong citation on the competition study) and finding 2 ("This already happens")
must be fixed. Findings 3-5 are precision fixes, and each is one phrase.
