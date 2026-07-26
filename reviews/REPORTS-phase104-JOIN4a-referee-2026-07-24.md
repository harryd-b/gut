# REPORT — phase 104 JOIN-4a: the defect-state census referee pass (2026-07-24, verbatim)

*Context-free adversarial referee on the JOIN-4a derivation (phases/phase104-JOIN4a-derivation.md), run per the standing pre-verdict policy. Verdict summary: Step A CORRECT in full scope (the kill-relevant clause is unconditional); Steps B–C contain three room errors, all repaired by the referee (corrections entered in the derivation document's amendment); the cohomological-residue claim survives in relative form with one genuinely open burden. Report preserved verbatim below. Referees are AI simulations, not humans — the standing caveat applies.*

---

# Referee Report

## Summary of verdicts

- **Step A: CORRECT.** All four sub-claims check out; scope is as claimed. This is the strongest and only fully proven component.
- **Step B: (1) CORRECT (with a formulation caveat); (2) WRONG as stated** — the profile condition "η ≡ c_q on I" makes Ad W(η) *trivial* on A(I); the correct condition is η′ ≡ c_q on I. **(3) Conclusion standard, argument a GAP** (excludes only Weyl implementers).
- **Step C: conventions all verified CORRECT; the explicit cocycle identification is WRONG as written** (non-local implementers fed into an in-algebra formula; the resulting unitary does not lie in A(I)); the support claim for ζ fails under the repaired Step B. **(4) structural formula CORRECT, identification inherits the flaw. (5) framing WRONG as posed** (the "invariant-state" criterion is vacuous for this base), repaired version plausible but unproven.
- **Overall claim:** first half proven, second half plausible-but-open after repair.

---

## Step A

**(i) Tensor center.** Z(M ⊗̄ N) = Z(M) ⊗̄ Z(N) is a corollary of the Tomita commutation theorem (M ⊗̄ N)′ = M′ ⊗̄ N′: Z(M⊗̄N) = (M⊗̄N) ∩ (M′⊗̄N′), and the intersection computes to Z(M)⊗̄Z(N) (standard; uses the commutation theorem, which is a genuinely nontrivial input but true for von Neumann tensor products). With A(I) a factor and L∞ abelian: Z(N_I) = ℂ1 ⊗̄ L∞(S¹) = base. **Correct.** Note carefully: the base is the center of the *fiber* N_I, not of M_γ; the argument as chained only uses the former. Fine.

**(ii) Takesaki.** The precise statement (Takesaki 1972; Takesaki vol. II, Thm. IX.4.2): for N ⊆ M and ψ a faithful normal state on M, N is globally σ^ψ-invariant **iff** there exists a (then unique) faithful normal conditional expectation E: M → N with ψ∘E = ψ; and in that case σ^ψ|_N = σ^{ψ|_N}. The derivation uses the direction "expectation-compatible ⇒ invariant + restriction." Hypotheses: φ̂ = φ∘E₀ is normal (composition of normal maps) and faithful (E₀(x*x) ≥ 0; φ faithful ⇒ E₀(x*x) = 0; E₀ faithful ⇒ x = 0). φ̂∘E₀ = φ∘E₀∘E₀ = φ̂ automatically. E₀ itself is the canonical Fourier-coefficient expectation of a discrete crossed product, faithful and normal — standard. φ̂|_{N_I} = φ. So σ^{φ̂}(N_I) = N_I and σ^{φ̂}|_{N_I} = σ^φ. **Correct.** (For states no semifiniteness caveats arise; the weight version would need φ̂|_N semifinite.)

**(iii) Modular flow fixes the center.** Exactly true for faithful normal states: with GNS vector Ω cyclic and separating, z ∈ Z(M) lies in both M and M′, so SzΩ = z*Ω = FzΩ, forcing Δ^{1/2}zΩ = Δ^{−1/2}zΩ, hence ΔzΩ = zΩ, hence σ_t(z)Ω = zΩ, and Ω separating gives σ_t(z) = z. Also true for f.n.s. weights (classical). **Correct.** The chain σ^{φ̂}_t(1⊗a) = σ^φ_t(1⊗a) = 1⊗a is valid; note it is essential that the argument routes through the modular group *of the fiber* — which is exactly what (ii) licenses.

**(iv) Scope.** No Γ-invariance of φ is used anywhere: Takesaki's theorem needs only φ̂∘E₀ = φ̂, which holds for every faithful normal φ. The only hidden hypotheses are faithfulness and normality of φ (without faithfulness σ^{φ̂} is not defined as stated; a support-projection version would be a different claim). **The claimed full scope is legitimate.** The transfer remark is also correct and in fact needs no crossed-product structure at all: for any inclusion N ⊆ M with f.n. expectation E and any state φ∘E, the flow fixes Z(N) pointwise; a fortiori any abelian subalgebra of Z(N). And the argument indeed says nothing about (a) Borchers/Wiesbrock-type translation unitaries (these are not modular flows of leg-aligned states) or (b) states on M_γ not factoring through E₀ — the negative-scope statements are accurate.

**Verdict A: CORRECT, full scope, no gaps.**

---

## Step B

**Preliminary convention audit.** For the current net, the symplectic form is the derivative pairing (σ(f,g) = ∫ f g′ dθ up to normalization; equivalently 2 Im⟨f,g⟩ in the H^{1/2} one-particle space, which carries only the k ≥ 1 modes, so Weyl labels are defined modulo constants). CCR gives

  W(a)W(b)W(a)* = e^{−iσ(a,b)} W(b).

**(1)** With the density ρ ≡ c_q on I and supp f ⋐ I (compact support in the open interval — the standard generating convention), L(f) = c_q ∫_I f, and the jump at ξ₊ ∈ ∂I is invisible: even a delta or worse *at* the endpoint pairs to zero with f vanishing near ∂I. **No distributional subtlety. Correct.** One formulation flaw worth recording: a "step of height q with a single jump at ξ₊" is incoherent as a *density* on S¹ (jumps of a single-valued piecewise-constant function must sum to zero), and L(f) = c∫f is not even well defined on the global phase space (labels are classes mod constants, but L(f + const) ≠ L(f)). The coherent reading — which the derivation clearly intends and which makes everything else parse — is: the *step of height ∝ q at ξ₊ sits in the primitive (the potential)*; the density is ≡ c_q on a neighborhood of Ī; and α is an automorphism of the quasilocal algebra of the punctured circle S¹∖{ξ₊}, where "mod constants" causes no ambiguity. Under that reading (1) is right.

**(2) WRONG as stated — this is the central computational error of the derivation.** For supp f ⊂ I:

  Ad W(η)(W(f)) = e^{−iσ(η,f)} W(f), −σ(η,f) = −∫ η f′ = ∫ η′ f.

If η ≡ c_q (constant) on I ⊇ supp f, then η′ ≡ 0 on supp f, so σ(η,f) = 0 and **Ad W(η)|_{A(I)} = id**. There is no convention that rescues this: any derivative-type symplectic form annihilates the pair (function constant on supp f, f), because σ must kill constants (W is defined mod constants). Taken literally, B(2) yields φ_σ|_{A(I)} = ω|_{A(I)}, which trivializes all of Step C (both cocycles become 1).

**Correct version:** η smooth, compactly supported in J ⊃ Ī, with **η′ ≡ c_q on I** (a smoothed ramp; note ∫_{S¹} η′ = 0 forces compensating "image charge" −c_q|I| in J∖Ī — this is the standard local-implementer picture). Then ∫η′f = c_q∫f = L(f) on generators, and since Ad W(η) is a normal automorphism of B(H) agreeing with α on the generators of A(I), α|_{A(I)} = Ad W(η)|_{A(I)} on the von Neumann algebra. The claim "depends only on the pairings σ(η,f), f ∈ K_I" is itself correct — and is precisely what falsifies the stated profile.

**Faithfulness/normality (with the fix): correct.** φ_σ|_{A(I)}(x) = ⟨W(−η)Ω, x W(−η)Ω⟩ is a vector state, hence normal. Separating: for x ∈ A(I) ⊆ A(J), xW(−η) ∈ A(J) and Ω is separating for A(J) (Reeh–Schlieder), so xW(−η)Ω = 0 ⇒ xW(−η) = 0 ⇒ x = 0. One only needs Ω cyclic/separating for A(J), not for A(I) with the perturbed vector directly.

**(3) Conclusion standard; argument as given is a GAP.** Two corrections: (a) under the consistent conventions the profile a Ī-supported *Weyl* implementer would need is a *truncated ramp* (slope c_q inside, 0 outside), not c_q·χ_I; but the obstruction is identical — the truncation creates jump discontinuities at ∂I, and a jump has logarithmically divergent H^{1/2}-norm (Σ k|f̂_k|², |f̂_k| ∼ 1/k). So no W(h) with h in the closed local one-particle subspace H(Ī) implements α|_{A(I)}; and H(Ī) = H(I) for this net (H^{1/2} admits no point-supported elements), so the weak closure adds nothing. (b) However, this excludes only *coherent* (Weyl) implementers. Ruling out an arbitrary unitary v ∈ A(Ī) with Ad v|_{A(I)} = α|_{A(I)} requires a charge/sector argument (e.g., BMT-type charge transport, or: any implementer must equal W(η)·w with w ∈ A(I)′ ∩ A(J) = A(J∖Ī) by strong additivity + duality, then show W(η)w ∉ A(Ī)). Not supplied. The physical conclusions — charge stored at the boundary jump, local indistinguishability from a coherent excitation — are right (the second is literally B(2) after the fix).

**Coupled state:** φ_σ|_{A(I)} ⊗ Leb is faithful and normal on N_I (tensor product of faithful normal states is faithful and normal on the vN tensor product; Leb is faithful normal on L∞(S¹)). **No issue.**

**Verdict B: (1) CORRECT (modulo the punctured-circle formulation); (2) WRONG as stated, correct after η ↦ ramp; (3) conclusion right, proof gap for non-Weyl implementers.**

---

## Step C

**(1) Transport.** For x ∈ A(I) (using γI = I so U(γ)xU(γ)* ∈ A(I)):
φ_σ(U(γ)xU(γ)*) = ω(W(η)U(γ)xU(γ)*W(η)*) = ω(U(γ)*W(η)U(γ) · x · U(γ)*W(η)*U(γ)) = ω(W(γ⁻¹η)xW(γ⁻¹η)*), using ω∘Ad U(γ) = ω and covariance (γ⁻¹η = η∘γ for the weight-1 current). **Transport identity correct.** But "γ⁻¹η ≡ c_q on I still" inherits B(2)'s error: with the corrected η, (η∘γ)′ = γ′·(η′∘γ) = c_q γ′ on I — the *density is not γ-invariant*; only the total charge is: ∫_I (η∘γ)′ = η(ξ₊) − η(ξ₋) = c_q|I|. Right conclusion (charge invariant), wrong mechanism.

**(2) Conventions: all verified correct in the abstract.**
- [D(ω∘Ad u):Dω]_t = u*σ^ω_t(u), for **u a unitary in the algebra**: matrix check with [Dφ:Dω]_t = ρ_φ^{it}ρ_ω^{−it}, σ^ω_t = Ad ρ_ω^{it}: φ = ω(u·u*) gives ρ_φ = u*ρ_ω u, so ρ_φ^{it}ρ_ω^{−it} = u*ρ_ω^{it}uρ_ω^{−it} = u*σ^ω_t(u). Also satisfies the cocycle identity c_{t+s} = c_tσ^ω_t(c_s) and Ad c_t∘σ^ω_t = Ad u*∘σ^ω_t∘Ad u = σ^{ω∘Ad u}_t. The variant convention φ = ω(u*·u) gives u σ_t(u*)-type expressions; all structural conclusions survive either convention (uniform conjugation/adjoint).
- Chain rule [Dφ₁:Dφ₃]_t = [Dφ₁:Dφ₂]_t[Dφ₂:Dφ₃]_t and [Dω:Dφ]_t = ([Dφ:Dω]_t)*: both correct (Connes), so [Dφ₁:Dφ₂]_t = [Dφ₁:Dω]_t([Dφ₂:Dω]_t)* is right, and the claimed combination
  c_t(γ) = W(γ⁻¹η)* σ^ω_t(W(γ⁻¹η)W(η)*) W(η)
is the algebraically correct assembly of those formulas.

**FATAL APPLICATION FLAW:** the formula u*σ_t(u) requires u ∈ A(I), the algebra carrying the two states, and σ_t the modular flow of ω|_{A(I)}. Here W(η), W(γ⁻¹η) ∈ A(J)∖A(I), while σ^ω_t = Ad U(δ_t), δ_t = Λ_I(−2πt), is A(I)'s modular flow, extended geometrically to everything. The derivation silently mixes these. The resulting c_t(γ) is a perfectly well-defined unitary on H, but it is **not shown — and is in fact not — the Connes cocycle of the two states on A(I)**, because a Connes cocycle between faithful normal states of A(I) lies in A(I) (balanced-weight construction), and:

**(3) Weyl recombination:** the identity c_t(γ) = e^{iΘ_t}W((1−δ_t)ζ), ζ = η − γ⁻¹η, is formally correct (σ^ω_t(W(g)) = W(δ_t g) exactly by covariance, no extra phase; the CCR phases are real scalars). But the support analysis breaks both ways:
- With the *stated* (erroneous) η: ζ ≡ 0 on I, ζ = 0 outside J∪γ⁻¹J, so supp((1−δ_t)ζ) ⊆ I′ — the "cocycle" lies in A(I′) ⊆ A(I)′. A unitary Connes cocycle of A(I) lying in the commutant must be scalar — and indeed, consistently, with the erroneous η the two states coincide (both = ω|_{A(I)}) and the true cocycle is ≡ 1. The nontrivial-looking Weyl factor is spurious.
- With the *corrected* η: ζ|_I = c_q(ℓ − ℓ∘γ)|_I (ℓ the angle primitive), which is **not constant on I** (γ ≠ id on the interior), so **ζ does not vanish on I**; supp ζ is spread over J∪γ⁻¹J, not concentrated at the endpoints; and (1−δ_t)ζ straddles I and I′. The claimed support structure fails.

**What is actually true (salvage):** ζ = η − η∘γ is globally smooth and vanishes *at* the fixed points ξ± (γξ± = ξ±). Hence the sharp truncation χ_Ī·ζ has only kinks, no jumps, at ∂I — finite H^{1/2}-norm — so ζ splits as ζ = ζ_in + ζ_out with ζ_in ∈ H(I), ζ_out ∈ H(I′). Then φ_σ∘AdU(γ)|_{A(I)} = (φ_σ|_{A(I)})∘Ad W(−ζ_in) with W(−ζ_in) ∈ A(I), and the honest relative cocycle is

  c′_t(γ) = W(−ζ_in)* σ^{φ₂}_t(W(−ζ_in)), φ₂ := φ_σ|_{A(I)},

with the **φ₂-modular flow, not the vacuum flow**, and profile ζ_in, not (1−δ_t)ζ. Fiber-valuedness (c′_t ∈ A(I), commuting with the base) holds by *general theory*, not "manifestly" from the derivation's formula. So the qualitative claims (cocycle exists, lives in the net leg, is Weyl-shaped up to the modular-flow deformation, and is anchored to the charge stored near ξ±) are recoverable; the specific formula is wrong.

**(4) Dual weight.** For M_γ = N_I ⋊ ℤ, φ f.n. state on N_I, φ̂ = φ∘E₀ equals the (normalized) Haagerup dual weight, and σ^{φ̂}_t(λ_g) = λ_g[Dφ∘α_g:Dφ]_t is the standard formula (the variant σ^{φ̂}_t(λ_g) = [Dφ:Dφ∘α_{g⁻¹}]_tλ_g is equivalent via [Dψ∘α:Dχ∘α]_t = α⁻¹([Dψ:Dχ]_t)). Tensor splitting [Dψ₁⊗ψ₂:Dχ₁⊗χ₂]_t = [Dψ₁:Dχ₁]_t⊗[Dψ₂:Dχ₂]_t is standard, and [D(Leb∘γ):DLeb]_t = |γ′|^{it} is the abelian Radon–Nikodym computation. So σ^{φ̂}_t(u_γ) = u_γ(c′_t ⊗ |γ′|^{it}) with c′_t = [D(φ_σ∘AdU(γ)|_{A(I)}):D(φ_σ|_{A(I)})]_t ∈ A(I). **Structure CORRECT**; consistency with Step A ✓ (the twist is fiber-valued, so σ^{φ̂} fixes the base while moving u_γ). Convention flips (left/right λ, cocycle adjoints) shuffle c′ by α_γ-conjugation/adjoints and cannot affect fiber-valuedness or base-fixing. But "the net-leg factor is the c_t(γ) of (2)–(3)" inherits the (2)–(3) flaw: the true c′_t is not the exhibited Weyl operator.

**(5) The invariant. WRONG as framed; repairable; nontriviality plausible but unproven.**

Decisive structural fact the derivation misses: **there is no faithful normal α_γ-invariant state on N_I at all.** Proof: such a ψ restricts to a faithful normal γ_*-invariant state on the center 1⊗L∞(S¹), i.e., a γ-invariant probability measure equivalent to Lebesgue. But a hyperbolic Möbius map's only invariant probability measures are supported on {ξ₊, ξ₋} (every other point wanders; Poincaré recurrence confines invariant probabilities to the non-wandering set), which are Lebesgue-null. Contradiction. (Only an *infinite* invariant measure ∼ dθ/|(θ−ξ₊)(θ−ξ₋)| exists in the Lebesgue class.)

Consequences: (a) "φ_σ-coupled is/isn't cohomologous to a γ-invariant state" is a **vacuous criterion** — it fails for the *vacuum* coupling equally, for a purely base-geometric reason independent of q. As posed, this cannot be the carrier of the charge. (b) The meaningful invariant is the **relative class against the vacuum coupling**: ω|_{A(I)}⊗Leb has net-leg cocycle ≡ 1 (Möbius invariance of ω), same base factor |γ′|^{it}; the defect data is whether the net-leg cocycle n ↦ c′(γⁿ) is a twisted coboundary v*·α-shifted·v with v ∈ N_I (equivalently whether φ̂_σ and ω̂ are conjugate by a unitary of M_γ compatibly with E₀).

Judgment on triviality: each *single* step is inner-adjustable (ζ_in ∈ H(I), as shown above), so the class is invisible at finite order; the obstruction is the divergence of the telescoped trivializer — formally v "=" W(η_in) with η_in the Ī-truncated ramp, which is exactly the log-divergent profile excluded in B(3). So: **the class is nontrivial against all coherent (Weyl) trivializers, with residue exactly the jump height ∝ q; this genuinely supports the "cohomological residue" philosophy — the obstruction is cumulative, not stepwise.** However, excluding *arbitrary* unitary trivializers v ∈ N_I is not established by anything in the derivation; it would follow from a BMT-type sector/charge-conservation argument (charge as an invariant of states mod inner perturbations on A(I)) which must be supplied. As it stands: plausible, consistent with BMT classification of sectors by q, **not proven**. Note also that on a type III₁ factor Connes–Størmer transitivity makes states *approximately* unitarily equivalent, so any nontriviality proof must be genuinely cohomological/exact, not approximate — a real, non-cosmetic burden.

---

## Overall ruling

- **Proven:** Step A in full. "Every leg-aligned state — defect states included — leaves the base inert" is **correct and unconditional** (given φ faithful normal), and is the strongest statement in the derivation. Also proven: the dual-weight twist structure σ^{φ̂}_t(u_γ) = u_γ(c′_t⊗|γ′|^{it}) with fiber-valued c′_t (C4, general theory), and the finiteness/normality/faithfulness bookkeeping (B2-faithfulness, coupled state).
- **Wrong as written:** B(2)'s profile (η ≡ c_q on I ⇒ Ad W(η)|_{A(I)} = id, collapsing Step C to the vacuum case); C(1)'s density-invariance; C(2)–(3)'s identification of the exhibited Weyl unitary with the Connes cocycle (non-local implementers + wrong modular flow; the exhibited unitary is not in A(I)); C(3)'s support claim for ζ under the repaired profile; C(5)'s "invariant-state" formulation (vacuous — no invariant f.n. state exists on N_I for any charge).
- **Repairable:** all of the above have correct analogues (η′ ≡ c_q; cocycle via ζ_in ∈ H(I) and the φ₂-flow; relative class vs. vacuum coupling), and the repaired picture coherently locates the residue at the divergent truncation ∝ q.
- **Open after repair:** nontriviality of the relative class against arbitrary (non-coherent) trivializers — needed for "the defect survives *as* the cohomology class" to be a theorem rather than a conjecture. Also B(3)'s exclusion of non-Weyl local implementers.
- **Final claimed verdict:** first clause proven; second clause is a correct-in-spirit but only partially substantiated claim, and only in the relative (vacuum-normalized) formulation.
- **"Data, not dynamics" gloss:** half fair. Accurate form: the defect is *invisible in the base dynamics* for every leg-aligned state (Step A, exact), and it *does* enter the modular dynamics of the coupled algebra — but only through the fiber-valued cocycle deforming σ^{φ̂} on u_γ, whose invariant content is (modulo the open coboundary question) the charge class. "Registers as cohomological data rather than base dynamics" is defensible; "not dynamics" simpliciter overstates, since the cocycle *is* part of σ^{φ̂}.
