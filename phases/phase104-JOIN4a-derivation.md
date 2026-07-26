# Phase 104 — JOIN-4a derivation: the defect-state census in the toy arena (refereed; kill ENTERED — see Amendment)

*Working session, 2026-07-24, continuing phase 104. This document records the in-room derivation for JOIN-4a (phase104 §7.4): the charge-q soliton state coupled into the single-geodesic arena M_γ, and the test of base-inertness outside the vacuum. **Status: [derived in-room; context-free referee pass dispatched; per the standing pre-verdict policy (phase 102) the kill verdict is NOT entered here and nothing below carries a [refereed] tag].** The derivation went past the plan in one respect: the verdict-relevant part closes by a structural argument (Step A) that needs no quasi-free calculus and covers strictly more than the pre-registered prediction; the Weyl computation (Step C) then delivers the explicit invariant. If the referee refutes Step A, Steps B–C stand independently as the original route.*

---

## Setup (all from phase 102, refereed there)

The toy arena: γ hyperbolic with fixed points ξ± bounding the axis arc I (γI = I); fiber N_I = A(I) ⊗̄ L∞(S¹); coupled algebra M_γ = W*(N_I, u_γ) ≅ N_I ⋊ ℤ with faithful normal expectation E₀: M_γ → N_I; base = 1 ⊗ L∞(S¹). A(I) is a type III₁ factor (Möbius-covariant net, Reeh–Schlieder); Bisognano–Wichmann gives σ^ω_t = Ad U(Λ_I(−2πt)) on A(I), and γ itself lies on this same dilation one-parameter group (its axis endpoints are ∂I) — the T-2π geometry of phase 102.

**Leg-aligned (expectation-compatible) states**: states of the form φ̂ = φ∘E₀ with φ faithful normal on N_I. This is the constructible class the census machinery generates; phase 103's canonical states are the special case φ = (vacuum-type) ⊗ Leb with the Γ-invariance hypothesis.

## Step A — the structural theorem: the base is central in the fiber, so every leg-aligned flow fixes it

**Claim A [derived; to referee].** *For every faithful normal state φ on N_I (no invariance hypothesis of any kind), the modular flow of φ̂ = φ∘E₀ on M_γ fixes the base 1⊗L∞(S¹) pointwise.*

*Argument.* (i) Z(N_I) = Z(A(I)) ⊗̄ Z(L∞(S¹)) = ℂ1 ⊗ L∞(S¹): the base **is the center of the fiber** (A(I) is a factor; L∞ is abelian). (ii) By Takesaki's theorem for expectation-compatible weights, σ^{φ̂} globally preserves N_I and σ^{φ̂}|_{N_I} = σ^φ. (iii) The modular automorphism group of any faithful normal state fixes the center of its algebra pointwise. Chaining (i)–(iii): σ^{φ̂}_t(1⊗a) = σ^φ_t(1⊗a) = 1⊗a. ∎

**Scope, stated with care.** (a) This is *stronger* than the pre-registered prediction: the referee's route predicted inertness for the soliton state via fiber-valuedness of its cocycle; Claim A closes the question for **every** leg-aligned state at once — Γ-invariant or not, vacuum-like or defect-like. The Γ-invariance hypothesis of phase 103's base-inertness mechanism is *not needed* for this class in the toy arena. (b) The same argument transfers verbatim to any crossed product whose fiber has the base as its center — including the full arena 𝒞 with fiber B(H)⊗̄L∞(S¹) — **but only for the global modular flows of expectation-compatible states**; it says nothing about Wiesbrock/Borchers translations built from subalgebra *pairs*, which are not modular flows of the full crossed product (that is where phase 103's finer multi-interval analysis lives), and nothing about non-expectation-compatible states, whose flows need not restrict legwise — exactly Referee 1's open residue (phase 104 §7.1). (c) Consequence if confirmed: within the toy arena, **no leg-aligned state whatsoever — including every constructible defect state — moves the base**; the defect escape, if it exists at all, must be non-leg-aligned. This is the toy-rung kill condition of JOIN-4a.

## Step B — the soliton state is admissible (it IS a leg-aligned state), and where its charge hides

The charge-q BMT-type soliton: an automorphism of the quasilocal algebra of the U(1)-current net of the form α(W(f)) = e^{iL(f)} W(f), L real-linear, whose background density is a step of height ∝ q jumping at the puncture ξ₊; the defect state is φ_σ = ω∘α. Globally α is not unitarily implemented (that is what makes it a sector); but the coupling only ever sees φ_σ **restricted to A(I)** — and there:

1. **The background is constant on I.** The jump sits at ξ₊ ∈ ∂I, not in the interior; restricted to test functions supported in I, L(f) = c_q ∫_I f for a constant c_q ∝ q.
2. **A constant shift on I is locally implementable.** Choose η smooth, compactly supported in an open J ⊃ Ī, with η ≡ c_q on I. Then α|_{A(I)} = Ad W(η)|_{A(I)} (only the pairing against f supported in I matters), so φ_σ|_{A(I)} = ω∘Ad W(η)|_{A(I)} — a **normal, faithful** state on A(I) (vector state of W(η)Ω; faithful by Reeh–Schlieder). Hence φ_σ ⊗ Leb is a legitimate fiber state and Step A applies to it.
3. **The non-split obstruction — where the charge lives.** No implementer supported in Ī exists for q ≠ 0: it would have to be c_q·χ_I-like, and indicator-type jumps are not in the one-particle space (the H^{1/2}-norm of a step diverges logarithmically). The jump at the fixed points **is** the charge, and it cannot be localized away from ∂I = {ξ±}. Locally the soliton is indistinguishable from a coherent excitation — its sector-ness is stored entirely in how the local implementers fail to glue across the fixed points. [This is the toy shadow of Referee 2's dense-orbit obstruction, and it is exactly a gluing-cohomology statement, as the local-III₁-rigidity ceiling requires.]

## Step C — the explicit cocycle: fiber-valued Weyl operator × winding phase

With φ_σ|_{A(I)} = ω∘Ad W(η)|_{A(I)}:

1. **Transport.** Using Möbius invariance of ω (ω∘Ad U(γ) = ω) and Weyl covariance (U(γ)W(η)U(γ)* = W(γη)): φ_σ∘Ad U(γ)|_{A(I)} = ω∘Ad W(γ⁻¹η)|_{A(I)} (γ⁻¹ preserves I, and γ⁻¹η ≡ c_q on I as well — the constant is dilation-invariant, i.e., **the charge is γ-invariant**).
2. **Chain rule.** With the standard cocycle formula [Dω∘Ad(u) : Dω]_t = u*σ^ω_t(u) and the chain rule [Dφ₁:Dφ₂]_t = [Dφ₁:Dω]_t·([Dφ₂:Dω]_t)*-composed appropriately:

> c_t(γ) := [D(φ_σ∘AdU(γ)) : Dφ_σ]_t = W(γ⁻¹η)* · σ^ω_t( W(γ⁻¹η) W(η)* ) · W(η).

3. **Weyl calculus + BW geometry.** σ^ω_t = Ad U(δ_t), δ_t := Λ_I(−2πt) the interval dilation — the same one-parameter group containing γ. Writing every factor as a Weyl operator and collecting with the CCR relation W(a)W(b) = e^{−iσ(a,b)/2}W(a+b):

> **c_t(γ) = e^{iΘ_t(q)} · W( (1 − δ_t)(η − γ⁻¹η) )** — a single Weyl operator of the net leg times a phase.

Two structural facts about ζ := η − γ⁻¹η: it **vanishes on I** (both terms equal c_q there) and vanishes outside J ∪ γ⁻¹J, so supp ζ concentrates in small arcs at the fixed points ξ± — the cocycle's entire content sits **at the endpoints**, where SS-MOD's essential-singularity structure lives. And c_t(γ) is manifestly **fiber-valued** (net leg ⊗ 1): the referee's prediction, now by direct computation.

4. **The dual-weight flow of the soliton-coupled state.** σ_t(x) = σ^{φ_σ⊗Leb}_t(x) for x ∈ N_I, and

> σ_t(u_γ) = u_γ · ( c_t(γ) ⊗ |γ′|^{it} ),

the vacuum's |γ′|^{it} twist (phase 102) now dressed by the soliton cocycle. The base is untouched (Step A; visible here too — both twist factors commute with 1⊗L∞ or act on the other leg).

5. **The surviving invariant.** The defect registers exactly as the class of the ℤ-cocycle n ↦ c(γⁿ) modulo coboundaries — the **winding of the phase Θ**, carrying q. The quantitative evaluation of Θ_t(q) (the explicit q-dependence and its normalization against ℓ(γ) — the candidate "charge × length" pairing) is posed as the follow-on computation **JOIN-4a′**; it is not needed for the verdict.

## Step D — the verdict this compels, NOT entered pending the referee pass

If Steps A–C survive refereeing, the pre-registered JOIN-4a kill condition (phase 104 §7.4) is met at the toy rung, in strengthened form: *every* leg-aligned state — the entire constructible class, defect states included — leaves the base inert; the defect survives only as cohomology (the winding class at the fixed points), never as motion. Per the pre-registration, the matter-sector escape then closes at the toy rung and the honest target becomes the cocycle-cohomology invariant (JOIN-4a′), with the sole remaining dynamical loophole exactly Referee 1's residue: non-leg-aligned (skew) states — JOIN-4b. If the referee refutes Step A, the verdict question reverts to Step C's explicit route; if it refutes Step C's fiber-valuedness, the kill does not fire and that refutation would itself be the discovery.

*Fourth-repetition note, for the eventual phase-105 synthesis: spectrum (lengths in the clock), cohomology (sector data), winding (charge), never flows. Every rung of this program that touches the base returns the same shape of answer — the geometry is data, not dynamics, for everything constructible. This pattern is hereby flagged as itself deserving a formal statement. [Refined by the referee — see Amendment, last item.]*

---

## Amendment (2026-07-24, same session) — referee verdicts entered; the kill fires; three room errors corrected

*Report preserved verbatim in `reviews/REPORTS-phase104-JOIN4a-referee-2026-07-24.md`. Summary: Step A CORRECT in full scope; Steps B–C contained three room errors, all caught and repaired by the referee; the cohomological-residue claim survives in relative form with one honest open burden.*

**The verdict, now entered per the pre-registration (phase 104 §7.4).** Step A is confirmed unconditional: *every leg-aligned state on M_γ — defect states included, no invariance hypothesis — leaves the base inert.* **The JOIN-4a kill is FIRED at the toy rung, in strengthened form.** The matter-sector escape is closed for the entire leg-aligned class; the defect enters the coupled dynamics only through a fiber-valued cocycle on u_γ; the sole remaining dynamical loophole is exactly the non-leg-aligned residue (JOIN-4b, unchanged). This is the fourth self-aimed kill of the extended program and the second of this session's successor gates; it is entered as fired, without softening.

**Corrections ledger — three room errors, all caught by the pre-verdict pass (the standing policy pays for itself again):**
- **C-B2 (the physics error).** The room set the implementer profile η ≡ c_q *constant* on I; the derivative-type symplectic form then gives Ad W(η)|_{A(I)} = id — the soliton state would have been the vacuum in disguise and Step C silently vacuous. Correct profile: **η′ ≡ c_q on I** (a smoothed ramp with compensating image charge in J∖Ī). The background couples through its *derivative*; the room forgot its own current algebra.
- **C-C23 (the cocycle error).** The exhibited unitary e^{iΘ}W((1−δ_t)(η−γ⁻¹η)) is not the Connes cocycle: the room fed non-local implementers (W(η) ∈ A(J), not A(I)) into an in-algebra formula and used the vacuum flow where the perturbed state's flow belongs. The honest cocycle [referee-supplied]: **c′_t(γ) = W(−ζ_in)\* σ^{φ₂}_t(W(−ζ_in))**, where ζ := η − η∘γ vanishes *at* the fixed points (so its Ī-truncation has only kinks — finite H^{1/2} norm — and splits as ζ_in + ζ_out with ζ_in ∈ H(I)), and φ₂ := φ_σ|_{A(I)}. Fiber-valuedness holds by general theory (Connes cocycles live in the algebra). The endpoint-support claim for the cocycle profile is withdrawn; what is anchored at ξ± is the *charge storage* (B3), not supp ζ.
- **C-C5 (the vacuous framing).** The room's invariant ("cohomologous to a γ-invariant state") is empty: **no faithful normal γ-invariant state exists on N_I at all** — a hyperbolic map's invariant probabilities are supported on the Lebesgue-null set {ξ±} (wandering + Poincaré recurrence). The meaningful invariant [referee-supplied]: the **relative class of the ℤ-cocycle n ↦ c′(γⁿ) against the vacuum coupling** (whose net-leg cocycle is ≡ 1 by Möbius invariance).

**What the referee established positively.** The relative class is **nontrivial against all coherent (Weyl) trivializers, with residue exactly the jump height ∝ q**: each single step is inner-adjustable, but the telescoped trivializer is the Ī-truncated ramp — precisely the log-divergent profile of B(3). *The charge is literally the divergence of the would-be trivializer.* The cumulative-not-stepwise structure is the honest content of "cohomological residue."

**What remains open (JOIN-4a′, re-posed):** (i) compute c′_t(γ) explicitly (φ₂-flow on the ramp difference; the quantitative q–ℓ(γ) pairing); (ii) **prove** nontriviality of the relative class against *arbitrary* unitary trivializers — needs a BMT-type sector/charge-conservation argument, and must be exact-cohomological, not approximate (Connes–Størmer transitivity makes approximate equivalence free on III₁, so the burden is real); (iii) close B(3)'s gap (exclude non-Weyl local implementers).

**The pattern statement, refined per the referee (adopted into phase 105 §1):** "data, not dynamics" *simpliciter* overstates — the defect **does** enter the modular dynamics of the coupled algebra, through the fiber-valued cocycle deforming the clock on u_γ. The defensible, and now refereed, form: **the defect is invisible in the base dynamics for every constructible state, and its entry into the clock's dynamics carries, as invariant content, exactly a cohomology class.** The base is data; the clock is the one dynamics; matter is data riding on the clock.
