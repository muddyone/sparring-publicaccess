# SPARRING -- Professional Distribution

The polished, citation-ready document set for SPARRING. These are the artifacts to cite in papers, submit to academic venues, hand to peers, or ship as a release bundle PDF.

## Where this fits

SPARRING has two layers of documentation, and they serve different purposes:

| Layer | Location | Audience | Cadence |
|---|---|---|---|
| **Working notes** (continuously evolving) | Private working material (`notes.md`, `reference-deployment.md`, `deployment-walkthrough.md`, `decision-frameworks.md`, `monte-carlo-design.md`). Not included in this repository. | The project's own working layer: in-flight refinements, failure-mode discoveries, and ongoing design decisions. | Updated as SPARRING evolves. |
| **Professional distribution** (versioned, citation-ready) | This directory. | Readers who want a frozen, versioned reference -- academics evaluating SPARRING, peers reading it linearly, anyone citing it formally. | Updated only at versioned releases. |

Only the professional distribution is public; the working notes are private working material, and this repository does not include them. If you want to *cite* SPARRING in a paper, cite this directory at a tagged version.

## Reading order

**New readers should start with the Reader's Guide.** It identifies the document set, the intended audiences, and recommends reading paths by reader role.

| Document | Purpose |
|---|---|
| [`sparring-readers-guide.md`](sparring-readers-guide.md) | Meta-navigation and reader's guide. Recommended entry point for any reader not yet certain which document fits their purpose. |
| [`sparring-specification.md`](sparring-specification.md) | Formal specification of the methodology. Primary artifact for academic submission (arXiv preprint, workshop paper). |
| [`sparring-implementation-guide.md`](sparring-implementation-guide.md) | Reference architecture for deploying SPARRING as a CLI tool. Primary artifact for engineering practitioners. |
| [`refs.bib`](refs.bib) | BibTeX bibliography for citation processing during pandoc conversion. |

## Generating PDFs

All three documents convert cleanly to PDF via pandoc with `--citeproc` against `refs.bib`. Required apt packages on Debian/Ubuntu:

```
sudo apt-get install -y pandoc texlive-latex-base texlive-fonts-recommended texlive-latex-recommended texlive-latex-extra
```

Generation commands (run from the repo root):

```bash
DIR=framework/professional-distribution

pandoc "$DIR/sparring-readers-guide.md" \
    --citeproc \
    --bibliography="$DIR/refs.bib" \
    --metadata title="The SPARRING Methodology: Reader's Guide" \
    --metadata author="Barton Niedner" \
    -o sparring-readers-guide.pdf

pandoc "$DIR/sparring-specification.md" \
    --citeproc \
    --bibliography="$DIR/refs.bib" \
    --metadata title="The SPARRING Methodology: Specification" \
    --metadata author="Barton Niedner" \
    -o sparring-specification.pdf

pandoc "$DIR/sparring-implementation-guide.md" \
    --citeproc \
    --bibliography="$DIR/refs.bib" \
    --metadata title="The SPARRING Methodology: Reference Implementation" \
    --metadata author="Barton Niedner" \
    -o sparring-implementation-guide.pdf
```

The same commands generate HTML or LaTeX by changing the output extension (`.html`, `.tex`).

## Versioning and provenance

Each document carries its own version and date in its header: the Specification is at 1.5 (2026-11-14), and the Reader's Guide and the Reference Implementation are at 1.0.

These documents were derived from the working-notes layer cited above. Future versioned releases of this directory will carry their own version numbers and dates; the working notes will continue to evolve in between releases. Use a tagged version of this repo when citing the polished forms in any context where citation stability matters.

## License

All documents in this directory are licensed CC BY 4.0 (Creative Commons Attribution 4.0 International), matching the rest of the SPARRING documentation in this repository. See the repository [`LICENSE`](../LICENSE) for the full text. Free to share, adapt, and build upon, including for commercial purposes, with attribution to Barton Niedner / Resource Forge LLC.
