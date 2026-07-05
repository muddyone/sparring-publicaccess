# SPARRING — public research artifacts

This repository holds the **public reproducibility artifacts** for research on
**SPARRING**, a methodology for structured, adversarial AI deliberation that
addresses compounding LLM failure modes (sycophancy, confirmation bias,
anchoring, blind spots, confidently-wrong output) via a two-role,
verifiable-challenge mechanic.

It is a curated archive, not a working tree: it contains only the material a
reader needs to check the papers' claims and reproduce their numbers.

## Layout

- **[`framework/`](framework/)** — the SPARRING methodology itself (specification,
  reader's and implementation guides). Shared across papers.
- **[`papers/`](papers/)** — one self-contained bundle per paper. Each bundle
  carries the exact pre-registration, data, code, and evidence that paper used.
  - **[`papers/2026-resolver-governance/`](papers/2026-resolver-governance/)** —
    *Auditable adversarial review for AI-in-the-loop decisions* — an empirical
    report on SPARRING's **Resolver** (pre-registered null → governance by
    verifiable challenge).

## De-identification and exposure posture

- **Raters are de-identified.** Study participants appear only as opaque labels
  (`External rater E1`…`E5`) and user ids; no names or emails.
- **No proprietary source.** The mechanism-audit evidence is drawn from the
  author's own commercial codebases; only *derived* artifacts (findings,
  codings, transcripts of the review) are included — never the source itself.
- **Raw per-run transcripts are omitted** where bulky and unaudited; the codings,
  results, and code reproduce every reported number. See each bundle's notes.

## License

Text, data, and figures: **CC-BY-4.0** ([`LICENSE`](LICENSE)). Code: **Apache-2.0**
([`LICENSE-CODE`](LICENSE-CODE)). Cite via [`CITATION.cff`](CITATION.cff).
