# OUTREACH NOTE — JOIN-4a″: exact unitary orbit of the vacuum under a BMT automorphism (2026-07-26)

*Prepared per the adopted plan and the operator's instruction. Intended audience: an operator algebraist familiar with type III factors and/or algebraic QFT. Self-contained; no framework content. Status of the question: exported open problem of the record (JOIN-4a″), adjudicated genuinely open by a literature pass on 2026-07-26 (notes/LITSEARCH-2026-07-26-T1-T2.md). Per the record's outreach rule, nothing mails without a human signature; this note may be consulted internally without one.*

## The question

Let A = A(I) be the interval algebra of the chiral U(1) current net in its vacuum representation — the unique hyperfinite type III₁ factor — and let ω be the vacuum state restricted to A. Let α = α_η be a Buchholz–Mack–Todorov charged automorphism with charge Q ≠ 0 localized in I: α(W(f)) = e^{i∫ρf}W(f) with ρ = η′ supported in I, Q = ∫ρ ≠ 0. (α is outer on A; its implementers are not Weyl operators of the net.)

> **Question (JOIN-4a″).** Is φ := ω∘α in the EXACT unitary orbit of ω — i.e., does there exist a unitary u ∈ A with φ = ω(u · u*)?

Equivalently: does the vacuum witness the failure of pointwise-innerness of α?

## Why the question is sharply posed now (the literature placement)

- **Density is classical**: Connes–Størmer (JFA 28, 1978) — the unitary orbit of any faithful normal state on a III₁ factor is norm-dense in the faithful normal states; this characterizes III₁. So φ is a norm-limit of states ω(uₙ·uₙ*); the question is exact membership.
- **Exactness holds for the inner∘modular class**: Haagerup–Størmer (JFA 92, 1990; Adv. Math. 83, 1990) — modular automorphisms are *pointwise inner* (θ(φ) unitarily equivalent to φ for EVERY normal positive functional).
- **The converse is now a theorem on this factor**: Isono (Compositio 160, 2024; arXiv:2309.05279), resolving the Haagerup–Størmer conjecture for III₁ factors with trivial bicentralizer — which includes the hyperfinite III₁ factor by Haagerup (Acta Math. 158, 1987): **every pointwise inner automorphism is inner∘modular.**
- **Consequence**: if α_η ∉ Inn(A)·{σᵗ_φ}, then α_η is NOT pointwise inner — some normal positive functional ψ has ψ∘α outside the exact unitary orbit of ψ. But Isono's theorem produces an unspecified witness ψ (not guaranteed faithful, let alone the vacuum). **No theorem in the literature we could find decides exact-orbit membership for a specified state pair (ω, ω∘α).**

## The two sub-questions we would ask

**(1) Is α_η inner∘modular on A?** We believe not (α_η changes the superselection charge; modular automorphisms of (A, φ) are trivial on sector data; a proof would presumably run through the BMT sector classification — the conjugate sector of charge Q is −Q ≠ Q — or through Connes' Γ/mod invariants), but we have not proven it, and we flag that the question is about α_η *restricted to a single interval algebra*, where sector language needs care: the restriction of a DHR automorphism to its localization algebra is an honest automorphism of A, and what "sector data" survives that restriction is part of the question.

**(2) If α_η is not inner∘modular, is the VACUUM a witness?** I.e., can one upgrade Isono's existence-of-a-witness to the specific pair (ω, ω∘α_η)? Any structural criterion for exact-orbit membership of a given faithful normal state pair on R_{III₁} — even a partial one (e.g., via the natural cone: φ = ω(u·u*) iff the cone representatives are related by u J u J) — would be of independent interest to us.

## Why we care (one paragraph, for context only)

The record this exports from maintains a "data dictionary" of invariants distinguishing charged defect states from the vacuum by their coupling to a discrete hyperbolic-element flow (a growth rate D = Q²ℓ/2π of truncated Connes-cocycle norms — cf. Longo's entropy of coherent excitations, LMP 109 (2019), for the continuous/entropy cousin). JOIN-4a″ is the dictionary's completeness question: if ω∘α is exactly unitarily equivalent to ω on A, then no state-level invariant on A alone separates the defect from vacuum, and everything our dictionary measures is *relational* (state + flow) — a clean and welcome answer. If it is not, there is a state-level invariant our dictionary does not yet contain. Either resolution is decisive for us.

## What we can offer

The full derivation records (self-contained, with adversarial referee reports) for: the cocycle-growth invariant and its I-local formulation; the outerness of α_η on A(I) via the divergent H^{1/2} winding norm; and the positive-cone purification of the defect state. Available on request.

*[SIGNATURE BLOCK — human signatory required before external circulation, per outreach/SIGNATURE-block-template.md. Unsigned: internal consultation only.]*
