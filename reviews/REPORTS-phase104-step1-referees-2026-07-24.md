# REPORTS — phase 104 Step 1: the two context-free referee reports (2026-07-24, verbatim)

*Two context-free adversarial referees, run per the standing policy (phase 102: pre-verdict referee pass mandatory for kill-adjacent work). Referee 1 received only the mathematics of the phase-104 §3 "normal-state closure" claim, framework-free. Referee 2 received only the defect-sector construction proposal, framework-free. Both reports are preserved verbatim below; the verdicts they compel are entered in phase104-JOIN4-defect-census.md §7. Referees are AI simulations, not humans — the standing caveat of STATUS-claims-novelty applies.*

---

## Referee 1 — the normal-state closure claim (verify or refute)

# Referee Report

## Task 1 — Proof sketch as far as it goes

**Verdict: CORRECT** (modulo three repairs, none fatal, itemized below).

**(a) Normalization transfer.** For a ∈ A, σ^φ_t(a) = u_t σ^ω_t(a) u_t* = u_t a u_t*, since σ^ω fixes A *pointwise* (elementwise, not merely globally — this is the load-bearing hypothesis). Hence σ^φ_t|_A = Ad(u_t)|_A as maps A → M for **every** t, unconditionally, and

σ^φ_t(A) = A ⟺ u_t A u_t* = A.

So yes: σ^φ_t normalizing A is *equivalent* to Ad(u_t) normalizing A. Correct.

**(b) Group law of the restriction.** The trap flagged in the prompt is real but avoided: Ad(u_t) alone is not a one-parameter group (u_{t+s} = u_t σ^ω_t(u_s) is a cocycle, not a homomorphism), but the sketch never needs it to be. Define T_φ = {t : σ^φ_t(A) = A}. Since σ^φ is a genuine automorphism group, T_φ is a subgroup of ℝ, and for t, s ∈ T_φ the restrictions compose: σ^φ_{t+s}|_A = σ^φ_t|_A ∘ σ^φ_s|_A. One can also verify consistency directly from the cocycle identity: for a ∈ A and u_s normalizing A, σ^ω_t(u_s) a σ^ω_t(u_s)* = σ^ω_t(u_s a u_s*) = u_s a u_s* (using σ^ω_{-t}(a) = a and u_s a u_s* ∈ A), so Ad(σ^ω_t(u_s))|_A = Ad(u_s)|_A and Ad(u_{t+s})|_A = Ad(u_t)|_A ∘ Ad(u_s)|_A. No error.

**Repair 1 (unstated dichotomy on T_φ).** The sketch implicitly assumes T_φ = ℝ. In fact T_φ is a *closed* subgroup: t ↦ σ^φ_t(x) is σ-strongly* continuous, A is strongly closed, so t_n → t with σ^φ_{t_n}(A) = A gives σ^φ_t(A) ⊆ A, and applying the same to −t_n gives equality. Hence T_φ ∈ {{0}, aℤ, ℝ}. The corollary's argument operates only in the case T_φ = ℝ; the discrete case aℤ is silently unaddressed (see Task 4 residue).

**(c) Measurability.** t ↦ u_t = (Dφ:Dω)_t is σ-strongly* continuous (standard property of the Connes cocycle), so t ↦ h_t := σ^φ_t|_A is continuous ℝ → Aut(A) (u-topology). To feed (P2), which wants a *jointly measurable point flow* on (S¹, Leb), one needs a point realization; this is not automatic from continuity in Aut(A) but follows from the Mackey point-realization theorem for continuous actions of locally compact groups on standard measure algebras. Each realized map agrees a.e. with the [R_Γ]-element supplied by (P1), and [R_Γ] is closed under a.e. modification, so the realized flow is [R_Γ]-valued. **Repair 2:** cite Mackey; the sketch's bare word "measurable" papers over this. Then (P2) gives h_t = id for a.e. t, and continuity upgrades to all t. Fine.

**(d) The unitary for (P1).** Explicitly: u_t = (Dφ:Dω)_t ∈ M, unitary (φ, ω both faithful normal *states*, so the cocycle is a σ-strongly* continuous family of unitaries in M), and u_t A u_t* = A on T_φ by (a). So (P1) applies with this unitary. **Repair 3 (citation caveat):** (P1) is attributed to Feldman–Moore, but A = 1 ⊗ L∞(S¹) is *not* a Cartan subalgebra of M = B(H) ⊗̄ N: its relative commutant is B(H) ⊗̄ A ⊋ A, so A is not even maximal abelian in M, and the Feldman–Moore normalizer theorem does not apply verbatim. The statement is nevertheless plausibly true (a normalizing unitary u satisfies (1⊗β(a))u = u(1⊗a), i.e., u is a nonzero element of the β-twisted A-bimodule; the A-bimodule spectrum of B(H) ⊗̄ N is still supported on R_Γ since B(H) carries the trivial A-action, forcing graph(β) ⊂ R_Γ mod null). Since (P1) is *given*, I accept it, but flag that its proof "elsewhere" must be the amplified bimodule argument, not Feldman–Moore as cited.

Consistency check on the setting: a state ω with σ^ω|_A = id exists (ω = ψ ⊗ (μ ∘ E) with E the canonical expectation onto L∞(S¹); its modular flow acts as a u_γ ↦ (dγ⁻¹μ/dμ)^{it} a u_γ, trivial on A). No issue.

## Task 2 — The non-normalizing case

**Verdict: GAP.** The Connes-cocycle argument constrains the non-normalizing case not at all beyond a tautology, and "all translates of A are inner-conjugate to A" is **not** an obstruction to half-sided motion.

**Why inner-conjugacy of translates is vacuous.** σ^φ_t(A) = u_t A u_t* holds for *every* faithful normal φ and every t, automatically, by the computation in 1(a). A statement that holds for all states carries zero discriminating information; it cannot obstruct anything a particular φ might do.

**Why it does not obstruct strict half-sided containment.** The candidate obstruction would be: "u A u* ⊊ A is impossible for a unitary u ∈ M." False in general, and nothing here forces it. A is abelian and not maximal abelian; abelian von Neumann algebras admit proper subalgebras unitarily conjugate to themselves in a large ambient algebra. Checking for a hidden commutant obstruction: if uAu* ⊊ A then A′ ∩ M = B(H) ⊗̄ A ⊆ u(A′ ∩ M)u*, and the inclusion is strict because the centers Z(A′∩M) = A and Z(u(A′∩M)u*) = uAu* differ — a strictly increasing chain of unitarily conjugate copies of L∞(S¹, B(H)), which is a shift-type configuration with no contradiction (type I with diffuse center; analogous to the unilateral-shift picture on Hilbert space). So a "modular endo-motion" σ^φ_t(A) ⊊ A for t > 0 is not excluded by anything in (P1), (P2), or the cocycle relation: (P1) requires an honest automorphism of A (uAu* = A exactly); a strict endomorphism σ^φ_t|_A : A → σ^φ_t(A) ⊊ A is not an element of [R_Γ] and (P2) never engages.

**What IS closed, as a byproduct.** Two-sided semigroup invariance collapses to normalization: if σ^φ_t(A) ⊆ A for *all* t ∈ ℝ, then A = σ^φ_{-t}(σ^φ_t(A)) ⊆ σ^φ_{-t}(A) ⊆ A forces σ^φ_t(A) = A for all t, and the corollary then gives pointwise fixing. Hence any nontrivial motion of A by a modular flow must be *strictly one-sided* (σ^φ_t(A) ⊊ A for t in one half-line only) or *skew* (translates neither contained in nor containing A). The skew case — the generic one — is completely untouched.

**An independent structural remark (not derivable from the sketch).** A *literal* Wiesbrock half-sided modular inclusion with A itself as the small algebra requires the GNS vector Ω_φ to be cyclic for the small algebra. An abelian algebra with a cyclic vector is maximal abelian; A is not maximal abelian on H_φ (B(H) ⊗̄ A ⊆ A′). So Ω_φ is never cyclic for A, and the Borchers–Wiesbrock machinery (which needs the common cyclic separating vector to manufacture the translation group) cannot even be initialized for the pair (σ^φ_1(A), A). This excludes the *technical* hsmi scenario for A itself on general grounds — but (i) this is my observation, not a consequence of the corollary's argument, and (ii) it does not exclude half-sided *motion* σ^φ_t(A) ⊊ A without the cyclicity demand, nor hsmi for other subalgebras built from A (half-arc corners, A ∨ partial group algebras, etc.), which are exactly the physically relevant objects.

**Precise ruling requested:** "all translates inner-conjugate to A" is NOT an obstruction to half-sided modular structures with continuous transverse motion. (Contrast: in a genuine hsmi N ⊂ M the Borchers translations U(a) satisfy U(1)MU(1)* = N ⊊ M, which *does* force U(1) ∉ M — but that is a statement about the ambient pair, not about a small subalgebra A carried around inside M by σ^φ, where the transporting unitaries u_t ∈ M coexist happily with strict containment of the *sub*algebra's translates.)

## Task 3 — Transfer from ω to arbitrary φ

**Verdict: GAP (genuine; no automatic transfer).**

The cocycle relation σ^φ_t = Ad(u_t) ∘ σ^ω_t does not convert φ-half-invariance into ω-half-invariance of any fixed subalgebra: σ^φ_t(B) ⊆ B for t ≤ 0 reads u_t σ^ω_t(B) u_t* ⊆ B with a *time-dependent* u_t; there is no fixed conjugate B̃ = vBv* with σ^ω_t(B̃) ⊆ B̃ unless the time dependence can be gauged away.

**Decisive structural argument.** By Connes' theorem, the modular flows of *any two* faithful normal states on *any* σ-finite von Neumann algebra are related by exactly such a cocycle. If hsmi classifications transferred along cocycle relations, then the existence and classification of half-sided modular inclusions would be a state-independent invariant of the algebra. It is not: hsmi structure is a property of the pair (subalgebra, state/vector), and it is well known from the QFT context that geometric modular action for the vacuum vector does not persist for generic other faithful normal states on the same (even hyperfinite III₁) factor. Cocycle-perturbation invariants are coarse objects (e.g., the flow of weights); hsmi data is strictly finer.

**Exact scope of what does transfer.** The cocycle is a coboundary, u_t = v* σ^ω_t(v) for a unitary v ∈ M, iff φ = ω ∘ Ad(v) (the cocycle determines the state). In that case σ^φ_t = Ad(v*) ∘ σ^ω_t ∘ Ad(v), and σ^φ_t(B) ⊆ B ⟺ σ^ω_t(vBv*) ⊆ vBv*: the ω-classification transfers with dictionary B ↦ vBv* — *provided* the "distinguished" family of subalgebras is itself Ad(v)-stable, which is an additional hypothesis nobody has checked. For φ outside the unitary orbit of ω (the generic case in a type III factor), no transfer mechanism exists in the given material. So: a classification for ω says nothing about hsmi for general φ. Genuine additional gap.

## Task 4 — Strongest correct version and residue

**Strongest theorem provable from (P1)+(P2):**

*Let φ be any faithful normal state on M and T_φ = {t ∈ ℝ : σ^φ_t(A) = A}. Then T_φ is a closed subgroup of ℝ, hence {0}, aℤ, or ℝ, and:*

1. *If T_φ = ℝ — equivalently, if T_φ merely has positive Lebesgue measure, or even just contains a nondiscrete sequence accumulating at 0 — then σ^φ_t(a) = a for all a ∈ A and all t ∈ ℝ; i.e., A ⊆ M_φ (the centralizer of φ). The modular flow of φ, whenever it globally preserves A, fixes A pointwise.*
2. *If σ^φ_t(A) ⊆ A for all t ∈ ℝ (two-sided containment), then already T_φ = ℝ and case 1 applies.*

Proof: as in Task 1 with Repairs 1–3 (closed-subgroup dichotomy; Mackey point realization feeding (P2); the amplified-normalizer version of (P1)). Conversely case 1 is sharp: states with A ⊆ M_φ exist (ω itself), so the conclusion "trivial action on A" cannot be improved to nonexistence of such states.

**Residue — explicitly NOT covered:**

1. **One-sided (half-sided) motion:** φ with σ^φ_t(A) ⊊ A for t > 0 (or t < 0) only. (P1) is inapplicable (endomorphisms of A, not automorphisms; no normalizing unitary), (P2) never engages. Entirely open.
2. **Skew motion:** φ with σ^φ_t(A) neither contained in nor containing A for t ≠ 0. This is the generic position and the physically relevant one (Borchers/Wiesbrock-type flows fail to normalize by design). Entirely open.
3. **Discrete normalizing times:** T_φ = aℤ with σ^φ_a acting on A as a nontrivial element of [R_Γ]. (P2) is a statement about one-parameter groups and says nothing about a single full-group element; nontrivial normalizing unitaries abound (1 ⊗ u_γ). Not excluded.
4. **Subalgebras other than A:** hsmi or motion statements for conjugates uAu*, proper subalgebras of A, half-arc corners, or any non-Cartan distinguished subalgebra. The argument is specific to A.
5. **State transfer:** any ω-specific classification of half-sided modular inclusions extends only to the unitary orbit {ω ∘ Ad(v)} (coboundary cocycles), and even there only if the distinguished family is Ad(v)-stable. All other faithful normal states: open.
6. **Non-modular flows:** arbitrary continuous ℝ-actions on M moving A (outside the corollary's scope, but should not be claimed).
7. **(P1)'s pedigree:** as stated it is not Feldman–Moore, since A is not Cartan in B(H) ⊗̄ N; it requires (and plausibly admits) an amplified A-bimodule-support proof. If the "elsewhere" proof is literally a citation of Feldman–Moore, that proof has a hole.

**Bottom line.** The sketch proves exactly this: *the modular flow of any faithful normal state either fails to preserve A globally, or fixes A pointwise* — "no nontrivial continuous motion *within* A." The claimed slogan "σ^φ cannot implement a nontrivial continuous motion *of* A" is an overclaim: motion of A *through* M — precisely the half-sided/skew regime that modular reconstructions of spacetime live in — is not touched by any part of the argument, and the inner-conjugacy of translates supplied by the cocycle theorem is tautological rather than obstructive.

---

## Referee 2 — the defect-sector proposal (feasibility and known theory)

REFEREE REPORT: "Defect sectors of the Fuchsian-coupled net algebra and their modular data"

PRELIMINARY STRUCTURAL OBJECTION (affects every task below)

The action of Γ on the fiber B(H) is inner (implemented by U(γ) ∈ B(H)). By the standard untwisting isomorphism for crossed products by inner actions,

  M = (B(H) ⊗̄ L∞(S¹)) ⋊_diag Γ ≅ B(H) ⊗̄ (L∞(S¹) ⋊ Γ),

via u_γ ↦ (U(γ) ⊗ 1)(1 ⊗ λ_γ). For Γ cocompact Fuchsian, the boundary action on (S¹, Lebesgue) is essentially free, minimal, ergodic, amenable in Zimmer's sense (boundary actions of lattices; Spatzier/Zimmer [check attribution]), and of type III₁ (ratio set ℝ₊, via ergodicity/mixing of the geodesic flow through the Maharam/Radon–Nikodym cocycle |γ′|; classical, attributed variously to Sullivan/Bowen-circle [check]). Hence L∞(S¹)⋊Γ is the hyperfinite III₁ factor (Krieger + Connes–Haagerup uniqueness), and

  M ≅ B(H) ⊗̄ R_∞.

Consequences the proposal must confront: (i) M itself carries no memory of the net or of Γ beyond this isomorphism class; all content of "base-inertness" lives in the choice of distinguished subalgebras (leg-aligned standard pairs, the Cartan 1⊗L∞) and distinguished states — it is a statement about a decorated algebra, not about M. (ii) A von Neumann algebra has no interesting sector theory: every normal representation of M is quasi-equivalent to a subrepresentation of an amplification of the identity representation. "Solitonic representation of M", read literally, is either normal (hence structurally nothing new) or non-normal (hence discards the von Neumann structure entirely). As stated, the proposal is ill-posed at the vN level. It becomes well-posed only after a C*/net-level recast (see Tasks 3 and 5). This is the central defect of the proposal as written.

TASK 1: MINIMAL HYPOTHESES AND THE VACUUM FOLIUM

Where invariance enters. For a crossed product N ⋊_α Γ with n.s.f. weight φ on N, the Haagerup dual weight φ̂ satisfies (Takesaki Vol. II; Haagerup 1978/79):

  σ_t^{φ̂}|_N = σ_t^φ,  σ_t^{φ̂}(λ_γ) = λ_γ [Dφ∘α_γ : Dφ]_t  (convention-dependent sign/inverse [check]).

Γ-invariance of φ is used at exactly one point: it trivializes the Connes cocycle [Dφ∘α_γ : Dφ]_t ≡ 1, so σ^{φ̂} fixes the λ_γ and restricts legwise; base-inertness then follows because σ^φ of a leg-aligned state fixes 1⊗L∞ and the Wiesbrock/Borchers translations built from half-sided modular inclusions of leg-aligned pairs are fiber-valued (they live in B(H)⊗1, which commutes with 1⊗L∞). A secondary caveat: ω is a pure vector state on B(H), not faithful; dual-weight theory applies only to the faithful leg-aligned local pairs (A(I) is type III with Ω cyclic-separating by Reeh–Schlieder), not to a global "ω on B(H)". The base-inertness statement must be, and presumably is, about local standard pairs.

(a) Locally perturbed vacuum φ = ω∘Ad(v), v ∈ A(I₀) ⊂ B(H)⊗1. Then φ∘α_γ = ω∘Ad(α_γ^{-1}(v)) and

  [Dφ∘α_γ : Dφ]_t = w* σ_t^ω(w) with w = v*α_{γ^{-1}}(v),

a bounded inner cocycle with values in B(H)⊗1. The corrected modular flow is Ad(u_t)∘σ_t^{φ̂} with u_t fiber-valued; since B(H)⊗1 commutes with 1⊗L∞, the base is still fixed pointwise. So for fiber-localized perturbations the answer is stronger than "nothing structurally new": base-inertness persists verbatim. It is correct that Connes cocycle equivalence makes the whole modular theory a bounded (inner) perturbation; the flow of weights, type, and all cocycle-conjugacy invariants are untouched.

However — and the proposal should say this — pointwise base-fixing is NOT a folium invariant. Take ψ = φ̂∘Ad(w) with w a leg-mixing unitary (e.g. w = Σ_j v_j ⊗ χ_j, or w involving λ_γ): the cocycle no longer commutes with 1⊗L∞ and the base moves. But this is a gauge artifact: the standard pair (M, ψ) is unitarily conjugate to (M, φ̂), and the flow fixes the conjugated copy w(1⊗L∞)w*. The invariant formulation of base-inertness is "the modular flow fixes a Cartan-position copy of the base", and that property is stable across the entire folium. Conclusion for (a): yes — nothing structurally new can appear from any normal state; the proposed phenomenon is invisible in the vacuum folium, provably.

(b) Disjoint representations. At the vN level these do not exist normally (see preliminary objection). At the C* level (quasilocal algebra 𝔄 = closure of ∪_I A(I), or 𝔄⊗C(S¹) ⋊_r Γ), disjoint reps genuinely change: π(·)″ can have different type/factoriality, no Connes cocycle connects the states (cocycle theory lives on one algebra), and covariance can degrade to a subgroup with a nontrivial implementing-cocycle obstruction. What "actually changes structurally" is precisely: (i) which subgroup Λ ⊆ Γ is unitarily implemented in π, and (ii) the class of the implementation cocycle in H²(Λ, 𝕋) / the class of the transporter cocycle in a suitable H¹ with local-unitary coefficients. Note a hard rigidity fact the proposal ignores: interval algebras of a conformal net are hyperfinite type III₁ factors (Gabbiani–Fröhlich; Longo), and soliton/DHR reps are locally normal; local normality + III₁ factoriality forces local unitary equivalence with the vacuum on every interval in the domain. Hence ALL local modular data in any sector are unitary conjugates of vacuum modular data. New modular phenomena can only be global — in how the local identifications fail to glue Γ-equivariantly — i.e., cohomological, not dynamical.

TASK 2: WHAT IS KNOWN ABOUT SOLITON MODULAR THEORY

Established:
- Vacuum sector: Bisognano–Wichmann/geometric modular action for conformal nets: Δ_I^{it} = U(δ_I(−2πt)), J_I geometric (Brunetti–Guido–Longo 1993; Gabbiani–Fröhlich 1993; Fröhlich–Gabbiani). Borchers' 1992 commutation theorem: translation covariance + positive energy forces the boost commutation relations between Δ^{it} of a half-line/wedge and translations.
- Covariance of sectors: DHR sectors with finite statistics of a Möbius net are automatically Möbius covariant with positive energy (Guido–Longo, "The conformal spin and statistics theorem", CMP 1996; earlier "An algebraic spin and statistics theorem"). Solitons are covariant at most under the stabilizer of the puncture (translation–dilation group / its cover); Müger and Kawahigashi–Longo–Müger (CMP 2001, multi-interval subfactors) treat solitons of orbifold-type nets; twisted sectors of A appear as solitons permuted by G, with μ-index bookkeeping.
- Charged-sector modular data as cocycles: Longo's Kac–Wakimoto analogue ("An analogue of the Kac–Wakimoto formula and black hole thermodynamics", CMP 1997 [check year]) — for a finite-index sector ρ with left inverse Φ, the state ω∘Φ has modular objects differing from the vacuum's by an explicit cocycle whose "value" carries log d(ρ) (whence S = log d(ρ) as entropy). This is the prototype: sector modular theory = vacuum modular theory + explicit Connes cocycle determined by the sector, never a new geometric flow.
- Coherent/locally-excited states: Longo "Entropy of coherent excitations" (2019), Ciolli–Longo–Ruzzi "The information in a wave" (2019): modular/relative-entropy computations for locally perturbed vacua done entirely by cocycle calculus — direct support for Task 1(a).

Not known / my uncertainty: I know of NO published computation exhibiting a modular flow of a natural state in a soliton sector acting geometrically differently (e.g., moving points it fixes in the vacuum sector). What exists is the negative structural statement (full Möbius covariance fails; only the puncture-stabilizer survives, sometimes with anomalous cocycle) and the positive cocycle-relative statement (local modular data conjugate to vacuum, deviation = computable cocycle). Disorder/twisted-sector modular data in orbifold nets (Xu, "Algebraic orbifold conformal field theories" 2000; Müger, braided crossed G-categories 2005): fusion/braiding fully developed, modular (Tomita) data not, to my knowledge [check]. The proposal's implicit hope — that a defect sector shows qualitatively new modular dynamics on local algebras — contradicts the local III₁ rigidity noted in Task 1(b) unless the novelty is located in the gluing cohomology.

TASK 3: CONSTRUCTION REALITY CHECK FOR INFINITE Γ

- KLM/Xu finite-group orbifolds: require (i) internal symmetries (fixing each A(I) and Ω), (ii) finiteness (finite index, complete rationality for existence/counting of twisted sectors). Fuchsian Γ fails both, and (i) fails structurally: γ maps A(I) to A(γI); "A^Γ" is not a net on any decent quotient — the boundary action is minimal, S¹/Γ is a noncommutative space, which is exactly why the proposal writes L∞(S¹)⋊Γ. Orbifold technology does not bend to this; it breaks.
- Longo–Xu cyclic/permutation orbifolds: internal (permutation) symmetry + finiteness. Same two obstructions.
- Loop-group solitons (discontinuous-gauge/BMT-type constructions; Longo–Witten endomorphisms, "An algebraic construction of boundary QFT" 2011): these twist by a point defect in an internal gauge datum. A Möbius element acts on the source circle, not on an internal target; a "twisted boundary condition by γ ∈ PSL(2,ℝ)" has no positive-energy implementation on H — the would-be twisted field lives on a mapping torus/solenoid, outside net technology. Obstruction: the twisting group is spacetime, not gauge.
- BKLR phase boundaries (Bischoff–Kawahigashi–Longo–Rehren 2015/16): defects = Q-systems, hence finite index by definition. Infinite discrete index is partially available — Del Vecchio–Giorgetti, "Infinite index extensions of local nets and defects" (Rev. Math. Phys. 2018) [check], generalized Q-systems of intertwiners for discrete inclusions — this is the nearest live entry point, but it handles inclusions of nets over the SAME geometry; it does not address a group that moves the intervals.
- Crossed products of nets by infinite discrete groups DO exist when the group acts by localizable (DHR) automorphisms — e.g., the ℤ-extensions of the U(1)-current net by BMT automorphisms yielding lattice boson nets. Obstruction here: Ad U(γ) for γ ∈ Möb is not DHR-localizable; and on B(H) it is inner, so at the fiber level the crossed product untwists (preliminary objection) and nothing solitonic can be stored there.

Decisive geometric obstruction for the Fuchsian case: a soliton needs a puncture set avoiding some interval; Γ-equivariance forces the puncture set to be a Γ-orbit, and every Γ-orbit is DENSE (minimality). There is no interval free of punctures, so the very domain of a "Γ-equivariant soliton net" is empty. Any viable definition must therefore be groupoid-theoretic (twisting along an isotropy group over a null orbit), not interval-geometric. Note also: such defect states are automatically non-normal on L∞(S¹, Leb) (points are null) — consistent with, and forcing, the C*-recast.

TASK 4: THE TOY CASE Γ = ℤ = ⟨γ⟩, γ hyperbolic

Qualitatively different and much easier, for identifiable reasons:
1. The action of ℤ on S¹∖{ξ±} is proper/wandering with fundamental domains on each of the two arcs; the action is dissipative, so L∞(S¹)⋊ℤ ≅ L∞(F)⊗̄B(ℓ²(ℤ)) (type I), F a fundamental domain — versus III₁ for Fuchsian Γ. The coupled algebra is B(H)⊗̄L∞(F)⊗̄B(ℓ²(ℤ)); all modular theory is finite, explicit, and dual-weight formulas close.
2. Crucially, γ IS a modular element: by Bisognano–Wichmann, the hyperbolic one-parameter group with fixed points ξ± is the modular group of A(I_γ) (I_γ the arc from ξ− to ξ+), so U(γ) = Δ_{I_γ}^{is₀}. The toy problem is: crossed product of the net data by a discretized modular flow of one interval — squarely inside Wiesbrock/Borchers half-sided-modular technology.
3. Solitons exist here with EXISTING technology: puncture at ξ+ (or ξ±), i.e., representations of A restricted to ℝ = S¹∖{ξ+}, covariant under the translation–dilation subgroup fixing ξ+ — the classical soliton setting. For A = U(1)-current net, explicit families: BMT-type automorphisms with a charge jump at ξ+, and Longo–Witten solitonic endomorphisms. Since ⟨γ⟩ stabilizes the puncture, ℤ acts on the soliton category, and the twisted/covariant structure is a single cocycle over ℤ — a finite amount of data.

First computation, concretely well-posed: A = U(1)-current net; σ a BMT soliton with charge q jumping at ξ+; φ_σ = ω∘σ (locally normal on the punctured net); compute the Connes cocycle c_t(γ) = [Dφ_σ∘Ad U(γ) : Dφ_σ]_t in closed form (everything quasi-free/Gaussian: the cocycle is a Weyl operator times an explicit phase, computable à la Ciolli–Longo–Ruzzi); insert into the dual-weight formula σ_t(λ_γ) = λ_γ c_t(γ) for the ℤ-coupled algebra with a leg-aligned pair over a fundamental domain; check pointwise fixing of 1⊗L∞. Prediction from the structure: c_t(γ) is fiber-valued (a Weyl operator ⊗ 1), hence commutes with the base — inertness should PERSIST, with the sector detected not by base motion but by the phase/winding of the cocycle, i.e., a class in H¹(ℤ, U(fiber)) ≅ the charge q. That is a falsifiable, one-model, finitely-many-page computation.

TASK 5: VERDICT

Split verdict:
- As literally stated ("representation of M", M a von Neumann algebra): (iii) ill-posed. Normal reps see nothing (Task 1a plus quasi-equivalence); non-normal reps of a vN algebra discard the structure. Must be recast on the C*/groupoid level: 𝔅 = (𝔄 ⊗ C(S¹)) ⋊_r Γ, defect sector := representation induced from a boundary point ξ with stabilizer Γ_ξ, in Effros–Hahn/Mackey style. For ξ a hyperbolic fixed point, Γ_ξ ≅ ℤ, and the fiber datum at ξ is exactly a toy-case soliton for ⟨γ⟩: the Fuchsian defect sector is Ind_{ℤ}^{Γ} (toy soliton). Since a conditional expectation N⋊ℤ → subalgebra exists by Fourier restriction and Takesaki's theorem controls when modular flows pass through, the induced modular computation has a defined route.
- The toy ℤ-case: (i) — well-posed with existing entry points (BW/Wiesbrock, BMT/Longo–Witten solitons, dual weights, quasi-free cocycle calculus).
- The full Fuchsian case: (ii) — presently-nonexistent mathematics with a plausible path (induction from geodesic stabilizers), obstructed as stated by minimality (dense orbits kill interval-geometric solitons) and by the local III₁ rigidity, which makes "new modular dynamics on local algebras" impossible; the honest target is the cohomology class of the covariance/transporter cocycle, not a new flow.

Single most informative first computation: in the ℤ toy case with the U(1)-current net, compute [Dφ_σ∘Ad U(γ) : Dφ_σ]_t for a charge-q BMT soliton σ punctured at the attracting fixed point of γ, and determine whether the dual-weight modular flow of the coupled algebra fixes 1⊗L∞(S¹) pointwise. If (as the fiber-valuedness of the cocycle predicts) it does, the proposal's guiding question is answered negatively even in sectors, and the project should be redirected to the cocycle-cohomology invariant; if it does not, that single example already refutes base-inertness outside the vacuum folium and justifies the full program.

---

*Editorial note (report text above is verbatim and unaltered): Referee 2's Task 1(a) closing claims stability "across the entire folium" and invisibility for "any normal state," but its own argument establishes this only for the unitary orbit of the canonical state (ψ = φ̂∘Ad(w)); Referee 1's Task 3 makes the distinction load-bearing — cocycle transfer holds exactly on the unitary orbit and fails in general, and Referee 1's residue items 1–2 leave skew/one-sided motion by generic normal states open. Where the two reports conflict, Referee 1's finer analysis governs. Logged in phase104 §7 as R2-c1.*
