# Phase 106 — SYNTHESIS: the completed data dictionary (2026-07-26)

*Assembly document, 2026-07-26. **Status: [synthesis of refereed results; contains NO new mathematical claims]** — every boxed statement below was refereed in phases 104–105 (reports verbatim in reviews/); this document only assembles, cross-references, and states the honest boundary. Claim tags: everything in §2 is [derived, refereed] unless marked otherwise; §4's blanks are [open], [conjecture], or [ill-posed] as marked. Adoption status: phases 104–106 are session work on branch claude/program-failure-analysis-a9cc75; signature-block adoption into the main record is the operator's decision, still outstanding.*

---

## 1. What this is

The successor program adopted in phase 105 ("geometry is data, not dynamics") required a **data dictionary**: invariants of matter read off from geometry, with no dynamical claims. The dictionary planned in notes/PLAN-2026-07-26-dictionary-completion.md is now **complete as planned**: seven refereed items, each carrying its own derivation record, adversarial context-free referee report, and corrections ledger. This document assembles them into the single object they form, and names what the dictionary does NOT contain.

The arena throughout: the chiral U(1) current net A(I) on S¹ (Weyl calculus, homogeneous H^{1/2} one-particle space, Bisognano–Wichmann, Haag duality); geodesics = hyperbolic elements γ of PSL(2,ℝ) (anchors ξ∓ = ∂I, translation length ℓ); particles = charged defects AdW(η), charge Q = ∫_I η′; single-geodesic arena M_γ = (A(I)⊗̄L∞(S¹))⋊ℤ.

## 2. The dictionary (all refereed)

| # | Entry | Formula | Kind | Record |
|---|---|---|---|---|
| E1 | **Existence** (erasure rate) | D = Q²ℓ/2π | metric | phase104-JOIN4a-prime-derivation.md |
| E2 | **Relationship** (pair crossing) | D₁₂ = Q₁Q₂·î(γ₁,γ₂) | topological | phase105-D12-cross-invariant.md |
| E3 | **Spin/statistics** | D_spin = ∓Q²/2 + nQ²/2 (D-MS); parity (−1)^q | framed | phase105-Dspin-self-phase.md |
| E4 | **Fusion/binding/annihilation** | D_fus(Q₁+Q₂); ΔD = Q₁Q₂ℓ/π; eraser in A(I) ⟺ Q_tot = 0 | metric | phase105-Dfus-fusion-binding.md |
| E5 | **Conjugation** (antimatter) | J-mirror: Q → −Q, same axis, reflected side, invisible; canonical purification ξ_η ∈ P^♮ | modular | phase105-Dconj-antimatter.md |
| E6 | **Joint arena** | universal no-go (fiber → B(H)); ledger survives as center; D₁₂ recovered internally | structural | phase105-entry6-joint-arena.md |
| E7 | **Class pairing** | D̄₁₂ = Q₁Q₂·⟨[c₁],[c₂]⟩ on H₁(X;ℝ) | homological | phase105-entry7-class-crossing.md |

**Interlocks (each refereed where stated):**
- E1 is the **I-LOCAL** erasure rate — winding/I-local cocycle formulation only; globally compensated single-valued profiles have D = 0 (permanence is local).
- E4's binding is the **polarization** of E1's quadratic form on a single axis; E2 is a pairing **between** axes — two entries of different kind (metric vs topological), not one quadratic form.
- E3 refines the statistics pairing as a **quadratic refinement at framing zero**; monodromy = spin².
- E5's charge flip is a **theorem** (sector conjugation, convention-free), and its one-sided mirror law on E2 (Box 4a) holds in the E2 plateau class (L-MIRROR, proved in E6).
- E6 proves the cross-terms are **real**: D₁₂ reappears inside the joint arena as the central-extension class of the two implementer lines (full real σ; abelian iff no crossing, for nonzero charges) — reproduced internally, not assumed.
- E7 aggregates E2 over double cosets and **descends to homology**: the cross-invariant is the intersection pairing of charge-weighted cycle classes Qᵢ[cᵢ] ∈ H₁(X;ℝ). Diagonal: identity coset carries E1; the off-identity signed sum vanishes identically. The class entry is **data** — no invariant surface-defect state exists (divergence + double ergodicity, divergence-type scope).

**The one object.** The dictionary is a charge lattice fibered over the geodesics of X, equipped with: a metric quadratic form per fiber (E1, length-weighted), whose polarization is binding (E4); a topological/homological antisymmetric pairing between fibers (E2/E7); a framed quadratic refinement (E3); an involution (E5, charge conjugation = modular reflection); and a structure theorem for what carries it all (E6). In one phrase: **a framed quadratic refinement of a charge lattice fibered over geodesics, with an antisymmetric homological pairing and a modular conjugation** — the Arf-invariant setting flagged in the phase-105 adoption, now with every ingredient refereed.

## 3. What the dictionary asserts physically (interpretation, tagged)

[interpretation] A particle is a charged defect anchored on a closed geodesic. Its **existence cost** (how fast coherent local erasure fails) is charge² × length. Its **spin and statistics** are transport phases of the same charge. **Binding** is the cross-term of existence. **Annihilation** is exact local erasability, and happens iff total charge vanishes inside the leg. **Antimatter** is the modular mirror image — same geodesic, opposite charge, other side, invisible from here; matter + its mirror is the canonical (thermofield-double-shaped) purification. **Interaction data** between two particles is exactly the signed crossing of their geodesics — and at the level of whole geodesics on the surface, only homology matters. All of this is *data read from geometry*; none of it is dynamics. Nothing moves, scatters, or decays anywhere in the record — that is the standing boundary drawn by the phase-103/104 kills, not an omission.

## 4. The honest boundary — named blanks

**The two load-bearing blanks (decide whether this is a dictionary or a list):**

**B1 — JOIN-4a″ (completeness).** [open; exported for human referee] Precise statement: *Let A(I) be the interval algebra of the chiral U(1) current net in its vacuum representation (a hyperfinite III₁ factor), ω the vacuum state, and φ = ω∘AdW(η)|_{A(I)} the restriction of a charge-Q ≠ 0 BMT-type defect automorphism (η winding, density in I). Is φ in the exact unitary orbit of ω|_{A(I)} — i.e., does there exist a unitary u ∈ A(I) with φ = ω(u·u*)?* Connes–Størmer transitivity makes the orbit norm-dense; the question is exact membership (Haagerup–Størmer territory). If YES: the dictionary's entries are relational data (state + coupling), consonant with the thesis. If NO: there is a state-level invariant our entries do not see, and the dictionary is incomplete as it stands. **First target of the literature search.**

**B2 — KNOT-Q (the geometry bridge).** [conjecture, registered with kill — phases/phase105-SPAN1-knot-charge.md] The dictionary's left column is defect profiles, not knots. KNOT-Q conjectures the functor from Seifert genus to charge that would make it genuinely geometry → matter. Untested; the phase-57 contact machinery (Bennequin, twist defects) is not yet connected to the defect calculus. Not to be attacked before the literature search (adopted plan, reasons recorded).

**Physics columns with no entry (all honest, none hidden):**
- **Mass** [absent]: no candidate. ℓ is a property of the geodesic, not the defect.
- **Motion/energy/lifetime** [blocked]: removed by the refereed kills (base-inertness + [R_Γ] rigidity). Revival only via JOIN-4b / K-DATA (skew modular flows) — which remains the **standing falsifier** of the adopted thesis: a nontrivial skew flow would restore dynamics and refute "data, not dynamics" in its strong form.
- **Non-abelian charge** [absent]: needs WZW-level current algebras; fusion with multiplicities. A real extension, not a patch.
- **Generations** [absent]: nothing repeats; no mechanism conjectured.
- **Calibration** [absent]: no entry touches a measured number.

**Open registry (technical, from the phase-104/105 corrections ledgers):**
- **Q-FIB** (E6): for a FIXED pair of defects, does the Λ-orbit of the two implementer lines generate B(H), or is there a proper local joint fiber?
- **Q-WIND** (E6): does an intrinsic, convention-free mutual phase exist for genuine winding implementers (sectorial/cocycle-theoretic), and does it agree with the plateau value? (The winding mirror question is [ill-posed] pending this.)
- **C-F3** (E3): the branch–crossing sign correlation (orienting î relative to the ∓ chirality branch) is an independent datum, underived.
- **GAP-7** (E6): nested/disjoint pairs — does a proper local joint fiber exist there?
- **Writhe** (E7): the signed single-count of self-crossings is not definable from double cosets (no canonical branch ordering); the unsigned count is accessible as half the crossing-coset count.
- **Scope notes:** E7's no-invariant-profile dissolution holds for divergence-type groups (all lattices); C-D5 and D-MS are adopted conventions of the dictionary, not theorems.

## 5. Process record

Every entry followed the same pipeline: context-free derivation agent (≤2500 words, gaps over-flagged) → verbatim preservation in phases/ → context-free adversarial referee (independent numerics where applicable) → verdict entered as amendment with corrections ledger → commit. Referee reports verbatim in reviews/ (eleven reports for phases 104–105 plus three for the entries 5–7 sequence). Notable pipeline catches, preserved in the ledgers: the Dconj double-flip risk (pre-flagged, confirmed, then resolved by domain identification in E6); the E7 additive-character gap (pre-flagged, confirmed, repaired by double ergodicity); the Box 5 outerness repair; the universal-vs-fixed-pair re-scoping of the no-go. Standing AI-referee caveat applies to every verdict: all referees were AI agents; no human mathematician has checked any of this.

## 6. Next (per the adopted plan)

The literature search, over all results at once: JOIN-4a″ first (Connes–Størmer, Haagerup–Størmer), then Ceyhan–Faulkner cocycle flows, Longo entropy, BMT sector statistics (bears on Q-WIND directly), chiral-boson mutual statistics, crossed products by modular elements, and the chiral-sector/knot-invariant literature framing KNOT-Q. Then the KNOT-Q campaign decision. Operator decisions outstanding: signature-block adoption of phases 104–106; branch review/merge; the JOIN-4a″ outreach note.
