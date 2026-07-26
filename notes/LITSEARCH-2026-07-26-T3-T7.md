# LITERATURE SEARCH — targets T3–T7 (scout report, 2026-07-26, verbatim)

*Second of the two parallel literature scouts dispatched per the adopted plan (notes/PLAN-2026-07-26-dictionary-completion.md step 5): T3 BMT/mutual statistics + Q-WIND; T4 spin-statistics/framing; T5 Fuchsian×conformal-net marriages; T6 crossed products; T7 KNOT-Q anchoring. The scout was bound by citation-honesty rules (verified vs snippet-inferred labeled; no fabricated references). The T1–T2 scout (JOIN-4a″ exact orbits; erasure-rate prior art) reports separately. Report preserved verbatim below; the synthesized novelty assessment is deferred until both scouts are in. Standing caveat: this is an AI web-search pass, not a MathSciNet sweep by a specialist; NOT FOUND verdicts are coverage-limited.*

---

# Novelty-Assessment Report: Literature Scout for T3–T7

**Method note (honesty).** All findings below come from web searches (multiple query variants per target) plus a small number of abstract fetches. I mark each claim as either [abstract read], [snippet], or [background knowledge — standard result, citation from memory]. Searches used a US search index; arXiv, Springer/CMP, and Project Euclid results dominated. I did not obtain full text of any paywalled paper.

---

## T3 — BMT sectors, mutual/braiding statistics, intrinsic winding phase

**(a) Is the mutual monodromy of charged chiral-boson sectors standard? YES.**

- Buchholz, Mack, Todorov, "The current algebra on the circle as a germ of local field theories," Nucl. Phys. B (Proc. Suppl.) 5B (1988) 20–56. Confirmed [snippet + publisher page]: classifies the sectors of the U(1) current algebra and their (anyonic) statistics; the charged automorphisms and their braiding are the founding example of abelian braid statistics in the algebraic setting.
- Fredenhagen, Rehren, Schroer, "Superselection sectors with braid group statistics and exchange algebras I: General theory," Comm. Math. Phys. 125 (1989) 201–226; and "II: Geometric aspects and conformal covariance," Rev. Math. Phys. 4 (1992) 113–157 [snippet]. Part II handles precisely the circle-geometry subtleties (localization on S¹, 2π rotation) relevant to your setting.
- Longo, "Index of subfactors and statistics of quantum fields I," Comm. Math. Phys. 126 (1989) 217–247 [publisher page only].
- For the chiral boson specifically, the statistics/monodromy phase e^{2πi q₁q₂} and h = q²/2 are textbook-level; vertex operator V_α = e^{iαφ} has dimension α²/2 [snippet confirmation across several sources].

So: the *number* Q₁Q₂ (mod-1 phase) attached to a pair of charged sectors is fully standard DHR/BMT material. I found **nothing** attaching that phase to the *signed crossing number of hyperbolic axes* of PSL(2,ℝ) elements — see T5.

**(b) Intrinsic, convention-free mutual phase for winding ("solitonic") implementers?**

- The intrinsic object in the standard framework is the DHR monodromy ε(ρ₁,ρ₂)ε(ρ₂,ρ₁), which is convention-free for *localized, transportable* sectors (FRS I). For non-localized implementers (Bogoliubov implementers fixed only up to phase), the pairwise commutator phase is cocycle-dependent; the classical reference for implementer cocycles is Carey, Ruijsenaars, "On fermion gauge groups, current algebras and Kac–Moody algebras," Acta Appl. Math. 10 (1987) 1–86 [snippet; treats nonzero-winding loops explicitly].
- Closest hit for winding-dependent phases: Mund, Schrader, "Local quantum fields for anyons on the circle leading to non-relativistic anyons in two dimensions" (arXiv:1405.4154) [snippet]: local covariant net of anyon fields on the circle via implementable Bogoliubov transformations, with commutation relations that "depend on the relative winding number of localization regions." This is materially close to Q-WIND and should be read in full before claiming novelty there.
- Solitonic-sector statistics generally: Fröhlich, "New super-selection sectors ('soliton-states') in two dimensional Bose quantum field models," Comm. Math. Phys. 47 (1976) 269–310 [snippet]; Streater–Wilde sectors of the massless scalar; Rehren et al. on soliton spin-statistics-CPT (arXiv:hep-th/9711085) [snippet].

**NOVELTY VERDICT (T3):** Mutual phase e^{2πiq₁q₂} for BMT sectors: **KNOWN** (BMT 1988; FRS 1989/1992). Geodesic-axis indexation: not found (see T5). Intrinsic phase for winding implementers: **KNOWN IN DIFFERENT FORM** (Mund–Schrader arXiv:1405.4154, winding-number-dependent commutation relations; DHR monodromy as the intrinsic invariant per FRS) — a definitive intrinsic answer to Q-WIND *as you pose it* was **NOT FOUND**, but Mund–Schrader is a mandatory read before claiming it.

---

## T4 — Spin-statistics for chiral sectors and framing

- Guido, Longo, "An algebraic spin and statistics theorem," Comm. Math. Phys. 172 (1995) 517–533, and "The conformal spin and statistics theorem," Comm. Math. Phys. 181 (1996) 11–35 [abstract read via search summary]: equality of statistics phase and conformal univalence e^{2πiL₀} for finite-index sectors of conformal nets. Your statistics parity (−1)^q with h = q²/2 is exactly this theorem instantiated on the U(1) net.
- h = q²/2 for chiral-boson charged sectors: standard (BMT; vertex-operator dimension α²/2) [snippet].
- Framing shift: Witten, "Quantum field theory and the Jones polynomial," Comm. Math. Phys. 121 (1989) 351–399 [background knowledge + snippet]: a change of framing by n units multiplies a Wilson-line expectation by e^{2πi n h_R}; for the abelian theory h = q²/2, giving precisely a +nQ²/2 shift. The framing anomaly as regularization of self-linking is his; the structure ∓Q²/2 + nQ²/2 is the standard "conformal weight + framing units" pattern (also visible in the modular T = e^{−2πi(h−c/24)} story) [snippet, arXiv:2601.04318 and Rutgers lecture notes].

What I did **not** find: any operator-algebraic construction of the spin phase by a *minimal-subtraction transport of a charged implementer along a geodesic* inside a conformal net, with the framing integer emerging as the ambiguity of the subtraction. The ingredients and the answer are known; that specific derivation route appears unpublished. Searches: "framing" + "conformal net", "transport along geodesic" + "sector", several variants — no hits.

**NOVELTY VERDICT (T4):** D_spin = ∓Q²/2 + nQ²/2 as a *value*: **KNOWN** (Guido–Longo 1995/96 spin-statistics; Witten 1989 framing; h = q²/2 standard). The minimal-subtraction geodesic-transport *construction*: **NOT FOUND** (coverage: multiple targeted queries; absence of evidence, moderately confident).

---

## T5 — Geodesics/Fuchsian structure married to conformal nets

**The geometry is classical, as you suspected.**

- Goldman, "Invariant functions on Lie groups and Hamiltonian flows of surface group representations," Invent. Math. 85 (1986) 263–302 [background knowledge; confirmed via snippets]: Lie bracket on free homotopy classes of loops = signed sum over intersection points. Chas (arXiv:1209.0634) proves the Goldman bracket *determines* intersection numbers [abstract read]. Chas–Sullivan string topology is the chain-level generalization [snippet]. For an abelian weighting (your Q₁Q₂ Î), the Goldman bracket abelianizes exactly to the homological intersection pairing weighted bilinearly — your class-level sum over double cosets of axis crossings reproduces this classical structure (double cosets ↔ intersection points of closed geodesics is standard hyperbolic geometry; cf. geodesic-intersection literature, e.g. arXiv:1709.08958 [snippet]).
- Interval ↔ geodesic dictionary: the *kinematic space* program — Czech, Lamprou, McCandlish, Sully, "Integral geometry and holography," JHEP 10 (2015) 175 (arXiv:1505.05515) [abstract read via search summary] — identifies CFT intervals with bulk H² geodesics and organizes CFT data (entanglement, modular Hamiltonians) on the space of geodesics. This is the closest published "marriage" of geodesics to interval-indexed chiral CFT data. It does **not** treat superselection charges, commutator phases of implementers, or Fuchsian quotients/double cosets.
- Direct searches for "conformal net" + Fuchsian/geodesic/intersection-number sector indexing returned nothing on point. Nearest operator-algebraic item: Bhardwaj–Brisky–Chuah–Kawagoe–Keslin–Penneys–Wallick, "Superselection sectors for posets of von Neumann algebras," Comm. Math. Phys. 406 (2025), arXiv:2410.21454 [abstract read]: braided sector categories from geometric posets (cones in ℝ², à la Gabbiani–Fröhlich) — geometric indexing of sector theory, but no Fuchsian groups, no geodesic intersection numbers.

**NOVELTY VERDICT (T5):** Î = homological intersection number and the bilinear charge-weighted pairing: **KNOWN** (classical; Goldman 1986, Chas 2012 — your class-level result is a rediscovery of the abelianized Goldman/intersection structure, as you suspected). The interval↔geodesic indexation idea: **KNOWN IN DIFFERENT FORM** (kinematic space, Czech et al. 2015 — no charges, no operator algebras of implementers). The operator-algebraic realization (commutator phases of Weyl implementers on a net, indexed by Fuchsian axes, summed over double cosets): **NOT FOUND** (coverage: ~6 query variants across arXiv/Springer; confident nothing mainstream exists).

---

## T6 — Crossed products by modular/geometric group elements; boundary crossed products

Two well-developed adjacent strands exist; their *mixture* does not appear.

- **Boundary crossed products:** C(∂Γ) ⋊ Γ for Γ free or Fuchsian: Spielberg (free-group boundary actions give Cuntz–Krieger algebras); Laca–Spielberg and Anantharaman-Delaroche, "Purely infinite C*-algebras arising from crossed products" (Bull. SMF 125, 1997; ETDS) — C(∂Γ)⋊Γ purely infinite simple [snippets]. Von Neumann version: boundary actions of lattices w.r.t. Lebesgue measure are amenable type III, L∞(S¹)⋊Γ hyperfinite III (confirmed generically via "Type III actions on boundaries of Ã_n buildings," J. Operator Theory 49 (2003) [snippet]; the Fuchsian/S¹ case is classical folklore in that literature).
- **Crossed products of QFT algebras by geometric/modular flows:** Witten, "Gravity and the crossed product," JHEP (2022) (arXiv:2112.12828) [snippet]; Chandrasekaran, Longo, Penington, Witten, "An algebra of observables for de Sitter space," JHEP 02 (2023) 082 (arXiv:2206.10780) [abstract read]: crossed product of a type III₁ local algebra by its modular (boost) flow ⋊ℝ, giving type II. This is the nearest conceptual relative of your (A(I)⊗L∞(S¹))⋊ℤ — but it is a crossed product by the *continuous* modular group with an observer's clock, not by a *discrete* hyperbolic element acting simultaneously on a net algebra and on the boundary circle.
- Doplicher–Roberts field nets and Longo–Rehren inclusions are crossed products by *sector categories*, a different animal [snippets].
- Searches for "conformal net" + "crossed product" + hyperbolic/Möbius element, and for net-tensor-boundary constructions like (B(H)⊗L∞(S¹))⋊F₂, returned nothing on point.

**NOVELTY VERDICT (T6):** Each ingredient **KNOWN** (boundary crossed products: Spielberg, Laca–Spielberg, Anantharaman-Delaroche; modular-flow crossed products: Witten 2022, CLPW 2023); the mixed net×boundary discrete crossed product (A(I)⊗L∞(S¹))⋊ℤ and (B(H)⊗L∞(S¹))⋊⟨γ₁,γ₂⟩: **NOT FOUND** (coverage: ~5 query variants; moderately confident, but the C*/vN-dynamics literature is vast — a targeted MathSciNet sweep would raise confidence).

---

## T7 — KNOT-Q: Seifert genus vs charge

- The standard CS/WZW story colors knots by *representations* and computes invariants from holonomies/braiding: Witten 1989 [confirmed]; Guadagnini–Martellini–Mintchev, Reshetikhin–Turaev quantum-group invariants [background knowledge]. "Seifert" appears in the literature almost exclusively as *Seifert-fibered 3-manifolds* (Beasley localization, arXiv:1012.5064; arXiv:1812.10966; arXiv:1902.07538) [snippets] — not Seifert *genus*.
- No paper found relating **Seifert genus → charge/representation label**. Multiple query variants ("Seifert genus" + charge/label/Chern–Simons) produced nothing of the kind. The genus enters quantum-invariant territory only via *bounds and detection*: (i) Bennequin inequality sl(K) ≤ 2g(K)−1 for transverse knots (Bennequin 1983; skein-theoretic versions: Ng, arXiv:0709.2141; comparisons: arXiv:2010.01673) [snippets — consistent with your earlier Bennequin-based program]; (ii) the Alexander polynomial (genus lower bound, fiberedness) arises from U(1,1) Chern–Simons / Reidemeister torsion: Rozansky–Saleur-adjacent work, arXiv:hep-th/9209073 [snippet] — the nearest QFT-side object that "knows" genus-adjacent data; (iii) knot Floer homology detects genus exactly (Ozsváth–Szabó, "Holomorphic disks and genus bounds," Geom. Topol. 8 (2004)) [background knowledge — not from this search session] — but that is gauge-theoretic/Heegaard-Floer, not charge labels in CFT.

**NOVELTY VERDICT (T7):** genus→charge: **NOT FOUND** — KNOT-Q's specific claim is unanchored in the literature. This cuts both ways: no rediscovery risk, but also no external support; the only literature bridges from genus to QFT data are inequalities (Bennequin-type, consistent with your program's earlier use) and the Alexander polynomial via U(1,1) CS. Treat KNOT-Q as genuinely speculative.

---

## Summary table

| Target | Our result | Verdict |
|---|---|---|
| T3a | pair phase Q₁Q₂ for BMT sectors | KNOWN (BMT '88, FRS '89) — novelty only in geodesic indexation |
| T3b | intrinsic phase for winding implementers (Q-WIND) | KNOWN IN DIFFERENT FORM (Mund–Schrader '14) / NOT FOUND as posed |
| T4 | D_spin = ∓Q²/2 + nQ²/2 | value KNOWN (Guido–Longo '96, Witten '89); geodesic minimal-subtraction construction NOT FOUND |
| T5 | class-level charge-weighted intersection pairing | geometry KNOWN (Goldman '86, classical); operator-algebraic realization NOT FOUND; interval↔geodesic dictionary KNOWN IN DIFFERENT FORM (kinematic space '15) |
| T6 | net×boundary crossed products | ingredients KNOWN (Spielberg/Laca–Spielberg/A-D; Witten '22, CLPW '23); mixed object NOT FOUND |
| T7 | KNOT-Q genus→charge | NOT FOUND — unanchored; nearest: Bennequin bounds, Alexander/U(1,1) CS |

Sources: BMT germ paper (ScienceDirect) · FRS I (Project Euclid) · Guido–Longo conformal spin-statistics (arXiv:hep-th/9505059) · Mund–Schrader anyons on the circle (arXiv:1405.4154) · Carey–Ruijsenaars (Springer) · Chas, Goldman bracket determines intersection numbers (arXiv:1209.0634) · Czech–Lamprou–McCandlish–Sully (JHEP/OSTI) · Penneys et al. posets (arXiv:2410.21454) · Anantharaman-Delaroche (Bull. SMF) · CLPW (arXiv:2206.10780) · Beasley Seifert loops (arXiv:1012.5064) · U(1,1) CS / Alexander (arXiv:hep-th/9209073) · Ng skein Bennequin (arXiv:0709.2141) · Fröhlich soliton sectors (Springer) · framing anomaly lattice CS (arXiv:2601.04318)
