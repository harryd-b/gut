# gut — a geometry-first physics research program

*The complete working record of a personal research program: the bet that physics is, at bottom, the geometry of a manifold — and the honest account of how far that bet got.*

**Status: the record is closed at phase 103 (2026-07-19).** The framework's deepest gate — the join — was answered in the negative for everything constructible, and a pre-registered kill fired. What survives is stated in §"What stands" below.

---

## What this is

Over 103 numbered working phases the program pursued a single thesis: that a smooth 3-manifold Σ (with time emergent as modular flow) is ontologically primitive, and that forces, quantum structure, matter, and the arrow of time are *derived from* that geometry rather than added to it. The organizing discovery was that geometry fixes physics only on a **protected stratum**, and the central conjecture (**Plank IV**) was that the protecting structure is the **stiffness** of spacetime — the Godbillon–Vey invariant of a codimension-1 foliation — whose modular flow is the clock.

The program was run under **standing honesty rules**, and those rules are the reason this repository is worth reading even where the physics failed:

- Every claim carries a tag: **[proved]** / **[established (others')]** / **[conjecture]** / **[interpretation]** / **[fitted]**.
- Predictions were **pre-registered with kill conditions** before the data.
- Negative results are reported plainly, never buried or tuned away.
- Kill tests were armed in advance and **honored when they fired**.
- No fabricated numbers, assignments, or derivations — compute, cite, or say "unknown."

Four red-team campaigns (two internal, two context-free adversarial) audited the record; their reports are preserved verbatim.

## Start here

| Read this | For |
|---|---|
| `core/CORE-geometry-first-v7.md` | **the authoritative core document** (7th issue; supersedes v6 and all earlier `CORE-*`) |
| `status/STATUS-plain-english-2026-07-17.md` | the program in ordinary language |
| `essays/ESSAY-the-fully-wound-world.md` / `essays/fully-wound-world.html` | the narrative essay version |
| `status/STATUS-claims-novelty-publishability-2026-07-18.md` | what can honestly be claimed, what is novel, what is publishable |
| `notes/QUESTIONS-2026-07-19.md` | the complete open-problem ledger — who could answer each, and what dies if the answer is wrong |
| `planning/PREDICTIONS-LEDGER-2026-07-17.md` | the falsifiable commitments, with referees and dates |
| `planning/research-map-MASTER.md` + `planning/research-map-ADDENDUM-2026-07-17.md` | phase-by-phase index of all 103 phases |

`core/CORE-geometry-first-FINAL.md/.pdf`, `core/CORE-geometry-first-and-the-protected-stratum.md/.pdf`, and `core/CORE-final-v2.md` are **superseded**; they are kept for provenance only.

## What stands

**Mathematics, refereed and independently verified.**

- **DTAB — the Heegaard Floer d-invariants of circle bundles over surfaces** (`data/DTAB-PAPER.md`, data in `data/DTAB-DATA-2026-07-19.md`, computations in `scripts/dtab*_calc.py`). A standalone mathematics paper with no framework content: the graded 𝔽[U]-module structure of HF⁺(Y(g,n), 𝔰) for every torsion spin^c structure. The program's most credible artifact — printed proofs, runnable scripts, checkable in an afternoon.
- **The base-inertness theorem and the constructive census** (`phases/phase103-JOIN3c-census-closed.md`): every canonical modular flow and Wiesbrock/Borchers translation from leg-aligned subalgebras fixes the base pointwise. This is the theorem that closed the program's central hope — and it is the cleanest thing the join chapter produced.
- **NOTE-1** (`notes/NOTE-1-cpt-commutant.md`): the Boyle–Turok involution as modular conjugation of a constructed standard form. Two independent referees searched for prior art and found none.
- `notes/REMARK-1-circle-bundles.md`, `notes/NOTE-2-unique-KMS.md` — smaller results, correctly attributed.

**Negative results, which are results.**

- **The κ go/no-go: NO-GO** (`phases/phase38-tier2-2B-kappa-go-no-go.md`). Sorkin triple-path interference κ = C·gτ/ħ computed explicitly at leading order; all three Godbillon–Vey enhancement routes closed. κ is Planck-suppressed and retired as a fingerprint.
- **The AMK predictivity audit: negative** (`phases/phase42-T2-verdict.md`). The exotic-smoothness numerical channel is retrodictive fitting dressed in rigid invariants — no shared continuous modulus exists to eliminate.
- **The Hodge-weight obstruction, the global-hyperbolicity divide** — theorems, not bugs; stated rather than fixed.

**Live cosmological commitments** (`planning/PREDICTIONS-LEDGER-2026-07-17.md`), registered with timestamps and kill conditions before the data: rigid dark energy (w₀, wₐ) = (−1, 0), with a pre-filed successor if it evolves. Referee: the sky.

## What does not stand

**The framework as physics.** Every external referee located the reason identically: the dictionary — the functor joining the geometric layer to the observable net — does not exist. The named gaps (EQ, the join, F-GAP, T-2π, A1) are precisely where the physics would have been. The geometry did not become physics, and the record says so in its own last line.

## Repository layout

The archive is organized into folders by document type:

| Folder | Contents |
|---|---|
| `core/` | `CORE-*` — the core document across seven issues (v7 authoritative), plus superseded issues kept for provenance |
| `phases/` | `phase1`–`phase103-*.md` — the working record, in order |
| `reviews/` | `REPORTS-fresh-red-team-*.md` (the adversarial referee campaigns, verbatim) and `REVIEW-*.md` |
| `notes/` | `NOTE-*`, `REMARK-*` standalone mathematics; plus `QUESTIONS-*`, `CODA-*`, `torsion-U1-*` |
| `data/` | `DTAB-*` — the d-invariant paper and its data |
| `essays/` | `ESSAY-*`, `INTERPRETATIONS-*`, `fully-wound-world.html` — narrative/plain-language versions |
| `outreach/` | `PACKET-outreach-v*.md`, `SIGNATURE-block-template.md` — correspondence infrastructure |
| `scripts/` | `*_calc.py` — every computation, reproducible |
| `papers/` | `*.pdf` — source papers cited throughout (BHMM *Gravitizing the Quantum* 2203.17137; Asselmeyer-Maluga–Król; and others) |
| `status/` | `STATUS-*` — status and plain-English summaries |
| `planning/` | `TIER-2-KICKOFF.md`, `TIER-3-PLAN.md`, `RESEARCH-PLAN.md`, `research-map-*`, `PREDICTIONS-LEDGER-*` — the plans (all executed) and the phase index |

## Reproducing

The Python scripts are self-contained and depend only on the standard library plus `sympy`/`numpy` where noted:

```bash
python3 scripts/i3_calc.py        # the leading-order Sorkin I₃ computation (phase 38)
python3 scripts/dtab4b_calc.py    # the d-invariant sweep engine (DTAB paper)
```

PDFs are built from the Markdown with pandoc + xelatex:

```bash
pandoc IN.md -o OUT.pdf --pdf-engine=xelatex -V geometry:margin=1in \
  -V fontsize=11pt -V colorlinks=true --toc
```

## Contributing

This is an open research record and collaboration is welcome — corrections, new calculations, referee-style critiques, and attacks on the open problems in `notes/QUESTIONS-2026-07-19.md` especially. Before opening an issue or PR, please read [`CONTRIBUTING.md`](CONTRIBUTING.md): the program runs under **standing honesty rules** (claim tags, pre-registered kill conditions, no fabricated numbers, negative results reported plainly), and contributions are held to the same bar. Open-ended discussion belongs in **Discussions**; specific problems and proposed fixes in **Issues**.

## License

This repository is dual-licensed:

- **Written content** — all Markdown documents, notes, essays, data tables, and the `.pdf` write-ups authored here — is licensed under [**Creative Commons Attribution 4.0 International (CC-BY-4.0)**](LICENSE-CC-BY-4.0.txt). You may share and adapt it, including commercially, with attribution.
- **Code** — everything under `scripts/` — is licensed under the [**MIT License**](LICENSE).

Third-party PDFs under `papers/` are the property of their respective authors and publishers; they are included under fair-use/fair-dealing for citation and are **not** covered by the licenses above. To cite this work, see [`CITATION.cff`](CITATION.cff).

## A note on what this repository is for

It is not a claim to have found a theory of everything. It is a complete, timestamped, adversarially audited record of a serious attempt that failed at a specific, identifiable place — plus the handful of theorems that are true whether or not the universe agrees. The method, not the conclusion, is the part offered for use.
