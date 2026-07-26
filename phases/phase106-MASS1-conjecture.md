# Phase 106 — MASS-1: mass as carrier length (registered conjecture; 2026-07-26)

*Registration document. **Status: [conjecture; registered with kill conditions; NOT derived, NOT refereed].** Nothing here is a result. The supporting observations in §2 cite refereed entries and standard facts; the conjecture itself is a proposed assignment of the dictionary's empty mass column, registered so it can be tested and killed honestly. Origin: operator's proposal (2026-07-26) that mass might be knot complexity ("winds/twists"), sharpened in session: winds and twists are already assigned (charge and framing), so the unclaimed complexity dial is carrier length.*

---

## 1. Statement

**MASS-1(a).** The dictionary's mass column is filled by a strictly monotone function M(ℓ) of the translation length ℓ of the carrier's primitive closed geodesic. (The specific function is NOT conjectured; only monotone dependence on ℓ and independence from the charge data.)

**MASS-1(b) (generations).** Generations are distinct primitive closed geodesics in a common homology class: particles with identical charge Q, identical spin/statistics data, identical class-level interaction data D̄₁₂ against everything (by E7's homological blindness), distinguished only by ℓ — i.e., only by mass and by the existence cost D = Q²ℓ/2π.

## 2. Why this candidate (supporting observations, with tags)

1. **The other complexity dials are taken** [refereed]. Winding = charge (E1: Q is the winding of the profile). Twisting = framing (E3: n in D_spin). If mass were either, it would collapse into charge or spin — contradicting the basic phenomenological pattern (e.g. e vs μ: same charge and spin, different mass). The unclaimed dial is length/self-crossing complexity, and for closed geodesics on a hyperbolic surface these grow together (self-intersection counts grow ~ℓ² generically [others', heuristic]) — one dial, measured by ℓ.
2. **Discreteness for free** [others' — standard]. The length spectrum of a hyperbolic surface is countable and rigid. If M = M(ℓ), the mass spectrum is automatically discrete — not imposed, inherited from geometry.
3. **Generations for free** [corollary of refereed E1 + E7 + standard geometry]. E7 (refereed): the cross-pairing D̄₁₂ sees only the homology class — homologous carriers are interaction-indistinguishable. E1 (refereed): D = Q²ℓ/2π distinguishes them through ℓ. Each homology class contains infinitely many distinct primitive closed geodesics of increasing length [others' — standard]. So the formalism already contains families with identical quantum numbers differing only in ℓ: the generations pattern. What phase 106 listed as E7's limitation ("homological blindness") is, under MASS-1, the mechanism that makes room for generations.
4. **Sensible reading through E1** [interpretation]. D = Q² × (ℓ/2π): existence cost = charge² × mass-like factor; longer (more complex) carriers cost proportionally more to erase locally.

## 3. First test, worked through: fusion and additivity

**Same-axis fusion (from refereed E4).** Two defects fused on one geodesic form a single defect of charge Q₁+Q₂ on the SAME carrier — same ℓ. Under MASS-1, the composite's mass is M(ℓ), not M(ℓ) + M(ℓ): **mass is maximally non-additive within a single axis.** Adopted reading [interpretation]: mass is *carrier-bound* — a property of the geodesic, not of the charge riding it. Same-axis "composites" are not two particles but one particle with more charge; that they have one mass is then consistent, not anomalous.

**Cross-axis systems.** A genuine two-particle system (two carriers) has masses M(ℓ₁), M(ℓ₂), total M(ℓ₁) + M(ℓ₂) — exactly additive, because the dictionary contains **no cross-axis metric coupling**: D₁₂/D̄₁₂ is topological/homological and carries no length [refereed]. Consequence, stated as the conjecture's sharpest exposure rather than hidden: **binding energy (mass defect of composites) has no carrier in the current dictionary.** Real composite masses are not additive; under MASS-1 as it stands they would be. This is a named blank the conjecture inherits, not a refutation — but any future refereed cross-axis metric entry becomes the natural place where MASS-1 must either find binding or die (see K-MASS-2).

## 4. Kill conditions (registered)

**K-MASS-1 (independence kill).** If a refereed result forces ℓ to be a function of the charge/homology data on admissible carriers — in particular, if the eventual geometry bridge (KNOT-Q or successor) maps complexity to charge in a way that locks ℓ to Q — then mass and charge are not independent dials, MASS-1(b)'s generations collapse, and MASS-1 is dead. (MASS-1 therefore *requires* KNOT-Q's genus→charge and MASS-1's length→mass to be independent coordinates on carriers; this is a checkable structural requirement, not a hope.)

**K-MASS-2 (binding kill).** If a refereed cross-axis metric coupling is ever derived (a length-carrying analogue of D₁₂) and its induced composite-mass correction is inconsistent with any monotone M(ℓ) assignment, MASS-1 is dead.

**K-MASS-3 (assignment kill).** If a refereed dynamical or calibration result fills the mass column with a quantity provably not monotone in ℓ, MASS-1 is dead.

## 5. Literature context (VERIFIED 2026-07-26 — scout report verbatim in notes/LITSEARCH-2026-07-26-MASS1-verification.md)

All four flagged citations verified; none is load-bearing for the registration, but the picture they paint:

- **Buniy–Kephart** [verified]: "A model of glueballs," Phys. Lett. B 576 (2003) 127–134, arXiv:hep-ph/0209339, + follow-ups (IJMPA 2005; arXiv:2407.11731 review, 2024). Glueball mass ∝ ropelength of the tight knot/link of the QCD flux tube, one fitted parameter. **Direct prior art for "mass ∝ tight-knot length" in a different framework** — and apparently the only sustained such program.
- **Faddeev–Niemi** [verified]: Nature 387 (1997) 58–61 (hopfions). **Vakulenko–Kapitanskii** [verified]: Sov. Phys. Dokl. 24 (1979) 433, E ≥ c|Q|^{3/4}, with matching upper bound (Lin–Yang). **Structural nuance adopted into the record: the growth there is SUBLINEAR in charge (power 3/4)** — a caution against assuming any particular functional form for M; MASS-1 deliberately conjectures only monotonicity.
- **Cantarella–Kusner–Sullivan** [verified]: Invent. Math. 150 (2002) 257–286 — ropelength minimizers exist per knot type; the "mass-like functional on knot types" mathematics is solid.
- **Bilson-Thompson** [verified]: arXiv:hep-ph/0503213 — twist = electric charge (±e/3 per ribbon twist); **mass is NOT addressed in the helon model**. Consistent with our assignment (winds/twists = charge/framing; the complexity dial left for mass).
- **Sweep result**: no published proposal identifying particle mass with closed-geodesic length on a hyperbolic surface was found. Closest mainstream anchor: the AdS₃/CFT₂ heavy-operator relation Δ ↔ bulk geodesic length (conical defects; heavy-light Virasoro blocks, e.g. arXiv:1410.1392) — dimension-as-mass tied to geodesic length, the nearest established cousin of MASS-1's assignment. MASS-1's specific proposal appears unclaimed.

## 6. Relation to the standing program

MASS-1 does not touch the kills (no dynamics is claimed; M(ℓ) is data). It composes with KNOT-Q as the complementary half of the geometry bridge: KNOT-Q proposes complexity-as-genus → charge; MASS-1 proposes complexity-as-length → mass; K-MASS-1 records that they must be independent to coexist. The phase-106 synthesis's mass blank is now annotated with this registration; the blank is filled only if MASS-1 survives testing and refereeing, which has not happened.
