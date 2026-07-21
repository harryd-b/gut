# arXiv submission notes — DTAB paper

Everything you need to get [`DTAB-PAPER.tex`](DTAB-PAPER.tex) onto arXiv. The `.tex` is a faithful conversion of [`DTAB-PAPER.md`](DTAB-PAPER.md); no mathematical content was changed, only notation (Unicode → LaTeX) and structure (theorem environments, bibliography).

## Proposed metadata

| Field | Value |
|---|---|
| **Title** | The Heegaard Floer $d$-invariants of circle bundles over surfaces |
| **Primary category** | `math.GT` (Geometric Topology) |
| **Cross-list** | `math.SG` (Symplectic Geometry) — justified by the contact/Eliashberg–Thurston question (§7 Q3) |
| **MSC 2020** | Primary 57K18; Secondary 57R57, 57K31, 53D10 |
| **License** | CC BY 4.0 (to match the repository's content license) |

The abstract in the `.tex` is submission-ready. Authors, affiliation, and email are placeholders — fill them before compiling.

## The one blocker: endorsement

arXiv requires **endorsement** for a submitter's *first* paper in a subject area, unless you're auto-endorsed (typically via a recognized academic email domain / institutional affiliation). If you have a university affiliation and email, you are very likely auto-endorsed for `math.GT` and can skip this.

If not, you'll need an endorsement from an established `math.GT` author. Options, in order of ease:
1. **Use an institutional email** when registering — this usually grants automatic endorsement.
2. **Ask a co-author or colleague** who has posted to `math.GT` to endorse you (arXiv gives you an endorsement code to pass along).
3. **Reach a listed author** in the field — the natural candidates are people whose work this paper builds on directly (the surgery-formula and $\Sigma\times S^1$ literature). A short, specific request that names the result usually lands.

This is the single reason to sort submission out *before* you need it — endorsement can take a few days.

## Pre-submission checklist

- [ ] Fill in author name, affiliation, and email in `DTAB-PAPER.tex` (`\author`, `\address`, `\email`).
- [ ] Complete the **signature block** and the graded verification statement at the end (currently `[SIGNATURE BLOCK …]`).
- [ ] Decide how to include the data: either paste the tables from [`DTAB-DATA-2026-07-19.md`](DTAB-DATA-2026-07-19.md) into the marked "Data section" in the `.tex`, **or** upload the data file as an arXiv *ancillary file* and reference it. Ancillary is cleaner for 70 rows.
- [ ] **AI-use disclosure:** the paper already states it was "drafted with substantial AI assistance." arXiv's policy requires disclosing significant AI/LLM contribution — keeping this sentence satisfies that. Do **not** remove it.
- [ ] Compile locally to confirm it's clean: `pdflatex DTAB-PAPER.tex` twice (resolves refs/bibliography). It uses only `amsart` + `amsmath/amssymb/amsthm/geometry/hyperref` — all standard on arXiv's TeX Live.
- [ ] Optionally regenerate the tables from the scripts (`scripts/dtab*_calc.py`) as a final reproducibility check before upload.
- [ ] Verify the `[MT]` reference (Mark–Tosun, arXiv:2512.04278) resolves and the arXiv number is correct at submission time.

## Submitting

1. Register / log in at [arxiv.org](https://arxiv.org) (use your institutional email if you have one).
2. Start a new submission → category `math.GT`, cross-list `math.SG`.
3. Upload `DTAB-PAPER.tex` (plus the data as an ancillary file if you chose that route). arXiv compiles it server-side; fix any log warnings it flags.
4. Confirm the auto-extracted title/abstract/authors, set the license to CC BY 4.0, and submit. It goes on hold for moderation and typically posts the next business day.
5. Once it has an arXiv ID, add it to the repo — update `CITATION.cff` and link it from the README so the two artifacts point at each other.
