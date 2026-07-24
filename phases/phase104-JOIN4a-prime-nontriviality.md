# Phase 104 — JOIN-4a′ (ii): the nontriviality theorem, reduced to one lemma (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-24, continuing phase 104. **Status: [derived by a context-free derivation agent (second run — the first exceeded output limits and was terminated; nothing from it was used); NOT refereed; no verdict entered].** This document preserves verbatim the compact proof-reduction delivered for JOIN-4a′ task (ii): the statement (T) — no unitary in the fiber trivializes the defect coupling against the vacuum coupling — proven modulo one moderate computational lemma (L1) plus standard lemmas, with an unconditional weakening (no Weyl-type trivializer) and the Q = 0 degeneration check passing. One architectural surprise, itself proven: the "twist-matching condition" the room expected to carry the obstruction is VACUOUS — trivialization reduces exactly to a fiber statement, and the cocycle identity is an unconditional consequence, not a constraint. The obstruction mechanism is modular mixing against linear divergence: dilation mixing forces the n-step cocycle's vacuum expectation toward |F(t)|² > 0 while the divergence D = Q²ℓ/2π forces it to 0 — contradiction, consuming Q ≠ 0 exactly once. Goes to the combined referee with the JOIN-4a′ (i) derivation.*

---

## The derivation, verbatim

§1 Theorems actually proven

Notation. A(I) acts in the vacuum representation; by Reeh–Schlieder this is the GNS representation of ω_I := ω|_{A(I)}, with modular group σ_t := σ^{ω_I}_t. By Bisognano–Wichmann (Gabbiani–Fröhlich for chiral nets), the hyperbolic γ with fixed points ∂I satisfies Ad U(γ)|_{A(I)} = σ_τ with τ = −ℓ/2π; in particular ω_I∘AdU(γ) = ω_I and AdU(γ) commutes with σ_t. Write μ_ω = ω_I⊗Leb, μ_φ = φ₂⊗Leb on N_I, and κ_t := [Dφ₂ : Dω_I]_t ∈ A(I) (Connes cocycle).

Theorem 1 (Reduction; proven unconditionally). For a unitary v ∈ N_I the following are equivalent: (i) φ̂_σ = ω̂∘Ad(v); (ii) μ_φ = μ_ω∘Ad(v) on N_I; (iii) there exists a unitary u ∈ A(I) with φ₂ = ω_I∘Ad(u). Moreover: the E₀(x u_γⁿ)-matching conditions for n ≠ 0 are automatically satisfied (both sides vanish), so — contrary to the naive expectation — the "twist condition" is not an independent requirement on v; rather, the identity

  c^{(n)}_t = σ_{nτ}(κ_t)·κ_t*  (n ∈ ℤ, t ∈ ℝ),  c^{(1)}_t = c′_t,

holds unconditionally in A(I), and the entire v-dependent content of (i) is the coboundary equation κ_t = u*σ_t(u).

Theorem 2 (Main; proven modulo Lemmas L1–L2 of §3). Assume L1 (linear growth of the twisted trivializer norms) and L2 (Lebesgue spectrum of the dilation generator on Ω^⊥). Then there is no unitary u ∈ A(I) with φ₂ = ω_I∘Ad(u); hence (T) holds: no unitary v ∈ N_I satisfies φ̂_σ = ω̂∘Ad(v). The proof uses Q ≠ 0 exactly through L1, and the mechanism visibly degenerates at Q = 0 (Proposition 4).

Theorem 3 (Unconditional weakening; proven modulo only the explicit form of c′_t). There is no unitary of the form v = (λW(f))⊗g with f ∈ H(I), g unimodular in L∞(S¹). Sketch: such v gives κ_t = phase·W(δ_t f − f) (δ_t = one-particle modular/dilation transport), and the identity c′_t = σ_τ(κ_t)κ_t* forces ρ_t = (γ_*−1)(δ_t−1)f in H(I); iterating, ρ^{(n)}_t = (γ_*ⁿ−1)(δ_t−1)f, whose norm is bounded by 2‖(δ_t−1)f‖ uniformly in n, contradicting ‖ρ^{(n)}_t‖ → ∞ (which for Weyl vectors follows directly from ‖ζ^{(n)}‖² ~ (Q²ℓ/2π)n and the explicit ζ-dependence of ρ_t, without L1's full strength). [GAP: uses the announced explicit formula ρ_t = T_tζ_in with T_t injective for t ≠ 0.]

Proposition 4 (Q = 0 sanity check; proven). In this family Q = 0 forces c = 0, so η is constant on I, ζ_in = 0, c′_t = 1, φ₂ = ω_I, and v = 1 works. More generally, whenever ‖ζ^{(n)}‖ stays bounded the contradiction of Theorem 2 evaporates (Step 5 fails), consistent with innerness of chargeless defects.

§2 Proof outline

Step 1 (Collapse of the u_γⁿ-coefficient conditions; Theorem 1 (i)⟺(ii)). E₀ is N_I-bimodular: for v ∈ N_I and x = a u_γⁿ, Ad(v)(x) = (v a α_γⁿ(v*)) u_γⁿ has N_I-coefficient in the same Fourier mode, so E₀∘Ad(v) = Ad(v)∘E₀. Hence ω̂∘Ad(v) = (μ_ω∘Ad(v))∘E₀, and since both states factor through the surjection E₀, φ̂_σ = ω̂∘Ad(v) iff μ_φ = μ_ω∘Ad(v) on N_I. In particular both states annihilate every a u_γⁿ, n ≠ 0, so the anticipated "matching of u_γⁿ-coefficients" is vacuous (0 = 0). The obstruction cannot be an extra algebraic condition on v; it must be extracted from the fiber equality by modular theory — which is where the crossed-product data re-enters, now as a tool rather than a constraint.

Step 2 (Fiberwise reduction; Theorem 1 (ii)⟺(iii)). Since A(I) is a factor, N_I = L∞(S¹; A(I)) and Z(N_I) = 1⊗L∞. μ_φ = μ_ω∘Ad(v) is equivalent (Connes: a cocycle determines its state) to [Dμ_φ : Dμ_ω]_t = v*σ^{μ_ω}_t(v) for all t. The left side is κ_t⊗1 (product states over the same base measure), and σ^{μ_ω}_t = σ_t⊗id, so fiberwise κ_t = v(s)*σ_t(v(s)) for a.e. s, for each t; choosing a full-measure set good for all rational t and using σ-weak continuity in t, any good fiber u := v(s₀) satisfies κ_t = u*σ_t(u) for all t, i.e. φ₂ = ω_I∘Ad(u). Conversely u yields v = u⊗1. (Measurable-selection details: Lemma L3, routine.)

Step 3 (The unconditional cocycle identity). Since φ̂_σ = μ_φ∘E₀ and ω̂ = μ_ω∘E₀ share the expectation E₀, Takesaki's theorem gives σ^{ω̂}|_{N_I} = σ^{μ_ω} and [Dφ̂_σ : Dω̂]_t = κ_t⊗1. Then σ^{φ̂_σ}_t(u_γ) = (κ_t⊗1)σ^{ω̂}_t(u_γ)(κ_t⊗1)*; inserting the established formulas for both flows on u_γ, commuting u_γ through (u_γ*(κ_t⊗1)u_γ = α_γ^{-1}(κ_t⊗1)) and using centrality of 1⊗|γ′|^{it} in N_I, we get c′_t = AdU(γ^{-1})(κ_t)·κ_t* = σ_τ(κ_t)κ_t*, an identity in A(I) holding with no assumption on v. Telescoping d_n := σ_{nτ}(κ_t)κ_t* via d_n = σ_{(n−1)τ}(d_1)·d_{n−1} expresses c^{(n)}_t := d_n as an ordered product of dilation-transports of the Weyl operator c′_t = e^{iΘ_t}W(ρ_t); since AdU(γ) acts geometrically on Weyl operators, c^{(n)}_t = e^{iΘ^{(n)}_t}W(ρ^{(n)}_t) with ρ^{(n)}_t = Σ_{k=0}^{n−1} γ^k_*ρ_t. If, as the explicit form of c′_t indicates, ρ_t = T_tζ_in with T_t a function of the one-particle modular data of the standard subspace H(I) (hence commuting with γ_*, the modular transport itself), then ρ^{(n)}_t = T_tζ^{(n)}_in. [GAP: this identification is only as firm as the explicit formula for c′_t; flagged as part of L1.]

Step 4 (Coherent-amplitude decay). For the quasi-free vacuum, |ω(W(h))| = e^{−¼‖h‖²}. Hence |ω(c^{(n)}_t)| = e^{−¼‖ρ^{(n)}_t‖²}. Lemma L1 asserts ‖ρ^{(n)}_t‖² ≥ ε(t)n − C(t) with ε(t) > 0 for all sufficiently small t ≠ 0; heuristically ρ^{(n)}_t = T_tζ^{(n)}_in is a coherent sum of n quasi-orthogonal translates of the fixed nonzero "unit cell" T_tγ^k_*ζ_in, mirroring the established ‖ζ^{(n)}_in‖² = (Q²ℓ/2π)n + O(1); the divergence is proportional to Q², which is where Q ≠ 0 enters irreplaceably. Granting L1: ω(c^{(n)}_t) → 0 as n → ∞, exponentially. [GAP = L1.]

Step 5 (Mixing along the modular orbit). Suppose u ∈ A(I) with κ_t = u*σ_t(u) (Step 2). Substituting into the unconditional identity of Step 3 and using [AdU(γ), σ_t] = 0:

  c^{(n)}_t = σ_{nτ}(u*σ_t(u))·σ_t(u*)u.

Take ω-expectation. Since U(γ)Ω = Ω, ω(σ_{nτ}(a)b) = ⟨a*Ω, U(γ^{−n})bΩ⟩. By Lemma L2 the generator of the dilation subgroup U(γ_s) has purely Lebesgue spectrum on Ω^⊥, so ⟨ξ, U(γ^{−n})ζ⟩ = ω(...)-decomposed matrix elements are Fourier transforms of L¹ densities and vanish as n → ∞ (Riemann–Lebesgue along the discrete sequence). Hence U(γ^{−n}) → |Ω⟩⟨Ω| weakly and

  ω(c^{(n)}_t) = ω(σ_{nτ}(κ_t)·κ_t*·(...)) → ω(u*σ_t(u))·ω(σ_t(u*)u) = |ω(u*σ_t(u))|².

(The second factor is the complex conjugate of the first by σ_t-invariance of ω.)

Step 6 (The contradiction). Combining Steps 4 and 5: |ω(u*σ_t(u))|² = 0 for every t ≠ 0 in a set accumulating at 0 (where ε(t) > 0). But F(t) := ω(u*σ_t(u)) = ⟨uΩ, Δ^{it}uΩ⟩ is continuous in t with F(0) = ‖uΩ‖² = 1, so F(t) ≠ 0 for all small t. Contradiction. Hence no such u exists, and by Theorem 1 no v ∈ N_I intertwines the two couplings: (T) holds. Note the argument never needs Connes–Størmer-type approximate homogeneity to fail — it can't fail; the exact fiber equality is destroyed by its modular consequence, precisely as the "cocycle location" of the obstruction predicted, though the cocycle condition is a consequence of, not a supplement to, fiber equality.

Step 7 (Q = 0 degeneration). If Q = 0 then c = 0, η ≡ const on I, so Ad W(η) is trivial on A(I) (σ(η, f) = 0 for f ∈ C_c^∞(I)), φ₂ = ω_I, ζ_in = 0, c′_t = 1, and v = 1 verifies the equality; Steps 4–6 collapse because ‖ρ^{(n)}_t‖ stays bounded and the limit |F(t)|² = |ω(c^{(∞)}_t)| need not vanish. The proof mechanism is therefore genuinely charge-sensitive.

§3 Missing lemmas for the full (T)

L1 (Twisted trivializer growth; the essential gap; difficulty: moderate, computational). With c′_t = e^{iΘ_t}W(ρ_t) as established and ρ_t = T_tζ_in for the explicit one-particle map T_t (a bounded function of the modular data of H(I), commuting with the dilation transport γ_*): for every t ≠ 0 in some neighborhood of 0 minus {0}, there are ε(t) > 0, C(t) with ‖Σ_{k=0}^{n−1}γ^k_*T_tζ_in‖²_{H^{1/2}} ≥ ε(t)n − C(t). Expected proof: in logarithmic coordinates γ_* is translation by ℓ; write the spectral density of the cell T_tζ_in and show the Fejér-type kernel Σe^{ikℓp} integrates against it to a linearly growing quantity, using that the cell is nonzero (T_t injective for t ≠ 0, ζ_in ≠ 0 since Q ≠ 0) and has decaying autocorrelations (chargeless cell). Risk: exceptional t where the t-transform cancels the divergent ramp mode; one only needs a sequence t_k → 0 avoiding it.

L2 (Spectral lemma; difficulty: easy/standard). The generator of the dilation one-parameter group s ↦ U(γ_s) in the vacuum representation of the U(1)-current net has purely absolutely continuous (indeed Lebesgue) spectrum on Ω^⊥. Proof route: on the one-particle space, dilations are unitarily equivalent to translations in log coordinates (two half-lines), Lebesgue spectrum; second quantization preserves absolute continuity on the vacuum complement (convolution of an a.c. measure with anything is a.c.).

L3 (Measurable selection; difficulty: routine). From κ_t⊗1 = v*(σ_t⊗id)(v) in L∞(S¹; A(I)), extract a single fiber u = v(s₀) with κ_t = u*σ_t(u) for all t simultaneously (rational t + separability + σ-weak continuity), and confirm that a.e. fiber of a unitary is unitary.

L4 (Bookkeeping of the c′_t formula; difficulty: easy given the "established" package). Verify from the explicit c′_t that (a) the phase telescoping in Step 3 is consistent (Weyl phases drop out of |ω(·)|), and (b) T_t commutes with γ_*, so ρ^{(n)}_t = T_tζ^{(n)}_in exactly rather than up to boundary terms; if boundary terms appear, show they are O(1) in norm (enough for L1).

§4 Five-line honest summary

The n ≠ 0 coefficient conditions are vacuous: E₀-bimodularity reduces (T) exactly to a fiber statement — no u ∈ A(I) with φ₂ = ω_I∘Ad(u) — so the "twist condition" is a modular consequence of fiber equality, not an extra hypothesis; this correction to the expected architecture is itself proven. Granting that, the proof is clean: geometric modular action turns the established defect cocycle into the unconditional identity c^{(n)}_t = σ_{nτ}(κ_t)κ_t*; coboundary substitution plus dilation mixing gives ω(c^{(n)}_t) → |ω(u*σ_t(u))|², while the linear divergence ‖ζ^{(n)}‖² ~ (Q²ℓ/2π)n forces ω(c^{(n)}_t) → 0, contradicting continuity of t ↦ ω(u*σ_t(u)) at t = 0. The single substantive gap is L1 — transferring the given linear divergence of ζ^{(n)} to its t-twisted image ρ^{(n)}_t — a one-particle H^{1/2} computation; L2–L4 are standard. Unconditionally, the argument already rules out all Weyl-type v (Theorem 3), and it degenerates exactly at Q = 0, where v = 1 works.
