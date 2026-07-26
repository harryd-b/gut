# Phase 108 — JOIN-4a″ consultation: claimed resolution in the NEGATIVE (consultation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-26. An expert-persona operator-algebraist agent was consulted on the outreach note (outreach/OUTREACH-JOIN4a2-2026-07-26.md). **Status: [claimed theorem by consultant agent; NOT refereed; no verdict entered].***

*Headline claims (pre-verdict): (1) JOIN-4a″ RESOLVED IN THE NEGATIVE — φ = ω∘α is NOT in the exact unitary orbit of ω, by an infrared/van Hove phase-rigidity argument: a hypothetical implementer u yields a vector fixed by the one-parameter group V_t = e^{iΘ_t}W(k_t)Δ^{it}; the unique candidate invariant normal state is forced to be the η-coherent shift of vacuum; but the limiting phase functional ℓ(f) = Im∫η̂̄f̂ is UNBOUNDED precisely because η̂ ∉ L² (⟺ Q ≠ 0 ⟺ outerness ⟺ D > 0), giving vectors f_n with ‖f_n‖ → 0 yet phase π — contradiction (E(W(f_n)) → 1 and → −1 simultaneously). (2) Corollaries: α ∉ Inn·Mod; α is not pointwise inner; (ω, ω∘α) is an EXPLICIT witness pair for the failure Isono 2024 guarantees abstractly; the sharp mechanism is orbit membership ⟺ η ∈ H ⟺ Q = 0, so **D is precisely the obstruction density — an honest state-level invariant of the pair (ω, φ)**. (3) The session's own proposed route (weak-nullity of the cocycle) is REFUTED as stated: coboundaries u*σ_t(u) with ω(u) = 0 also tend weakly to zero (Prop. 1: σ_t(u) → ω(u)·1 WOT by Riemann–Lebesgue on the a.c. dilation spectrum), so decay alone can never obstruct — the working obstruction is phase rigidity, not size. (4) Four gaps flagged by the consultant (G1 Lebesgue spectrum citation; G2 Tauberian extraction — only η̂ ∉ L² is truly needed; G3 Weyl constants; G4 strong continuity), plus a four-item verification map. If this survives refereeing, it closes the dictionary's completeness question in the strongest form: the dictionary's first invariant D is itself the exact obstruction to erasing a particle into vacuum by any local unitary. Goes to a context-free adversarial referee before any verdict.*

---

## The consultation, verbatim

# Consultation report: JOIN-4a″ — exact unitary orbit of ω vs. φ = ω∘α

**Executive verdict: (i) — resolvable now, in the negative.** φ = ω∘α is **not** in the exact unitary orbit of ω, by an infrared/van Hove-type argument I sketch below with all gaps flagged. Corollary: α ∉ Inn(A)·Mod(A), answering Task 1 (client's belief confirmed), and (ω, ω∘α) is an *explicit* witness pair for the failure of pointwise innerness — complementing Isono, which only guarantees an unspecified witness. One warning first: the client's proposed obstruction in 2b (weak-nullity of the cocycle) is **refuted as stated**; the repaired argument works for a different reason.

## 0. Reductions [proved here, elementary]

(R1) If α = Ad(u)∘σ^ω_T (i.e. α ∈ Inn·Mod), then ω∘α = ω(v·v*) with v = σ^ω_{−T}(u) ∈ A, since ω∘σ_T = ω. So **α ∈ Inn·Mod ⟹ φ ∈ exact orbit**; contrapositive: a negative answer to JOIN-4a″ settles Task 1 negatively. The two tasks are not independent — 2 ⟹ 1.

(R2) φ = ω(u·u*) = ω∘Ad(u) iff β := Ad(u*)∘α satisfies ω∘β = ω. So **JOIN-4a″ ⟺ α ∈ Inn(A)·Aut(A, ω)**, and Inn·Mod ⊆ Inn·Aut(A,ω). The pair-question is exactly "inner modulo the ω-preserving group".

(R3) [standard, Connes; Takesaki VIII] φ = ω(u·u*) ⟺ (Dφ:Dω)_t = u*σ^ω_t(u) for all t (coboundary). I take the client's refereed formula as input: (Dφ:Dω)_t = e^{iΘ_t}W(k_t), k_t = η − η∘δ_{−2πt}, ‖k_t‖² ~ Dt, D = Q²ℓ/2π. [client-verified input]

(R4) On Haagerup–Størmer (Adv. Math. 83, 1990), Task 2c: their equivalence machinery routes state equivalence through the flow of weights; for III₁ the flow is trivial (one-point), so their invariants collapse and one recovers only Connes–Størmer *approximate* transitivity. No exact-orbit information for III₁. [checked against my knowledge of the literature; I did not re-fetch the paper — flag if you want a line-by-line citation.]

## 1. The weak-nullity route (client's 2b) — refuted, then repaired

**Proposition 1 [proved here].** For every u ∈ A, σ^ω_t(u) → ω(u)·1 in the weak operator topology as |t| → ∞.

*Proof.* Test on the dense set A′Ω (Ω cyclic for A′ = A(I′) by Reeh–Schlieder / Haag duality [standard]). For b′ ∈ A′: ⟨ξ, σ_t(u)b′Ω⟩ = ⟨b′*ξ, Δ^{it}uΩ⟩ (using Δ^{it}Ω = Ω, [σ_t(u), b′] = 0). By Bisognano–Wichmann, Δ^{it} = Γ(one-particle dilation), whose spectrum on Ω^⊥ is absolutely continuous (Lebesgue) [standard for the chiral current net; gap G1: cite e.g. the Mellin diagonalization of the dilation generator], so Riemann–Lebesgue gives Δ^{it}uΩ → ⟨Ω,uΩ⟩Ω weakly. Uniform boundedness extends to all of H. ∎

**Consequence (negative).** If c_t = u*σ_t(u) is a coboundary, then c_t → ω(u)u* WOT. If ω(u) = 0 this limit is 0. So **coboundaries CAN tend weakly to 0**, and "‖k_t‖ → ∞ ⟹ W(k_t) → 0 weakly ⟹ not a coboundary" is invalid as posed. (That W(k_t) → 0 weakly is true: |⟨W(g)Ω, W(k_t)W(h)Ω⟩| = e^{−‖k_t+h−g‖²/4} → 0 on a dense set [proved here].) Comparing expectations only teaches ω(u) = 0; every finer WOT test I ran collapses to consistency at this order. The obstruction must be phase-rigidity, not decay — see below.

## 2. Main theorem

**Theorem [proved here, modulo flagged gaps].** There is no unitary (indeed no isometry, no nonzero vector) implementing φ = ω∘α from ω. Hence φ ∉ exact unitary orbit of ω, and by (R1) α ∉ Inn·Mod; by (R2) α ∉ Inn·Aut(A,ω); α is not pointwise inner.

**Proof sketch (numbered).**

1. Suppose φ = ω(u·u*). By (R3) and the client's formula, u*σ_t(u) = e^{iΘ_t}W(k_t) *exactly* (both sides are THE Connes cocycle; no phase freedom). Taking adjoints and applying to Ω: the vector ξ := u*Ω (unit) satisfies Δ^{it}ξ = e^{−iΘ_t}W(−k_t)ξ, i.e. **V_tξ = ξ** where V_t := e^{iΘ_t}W(k_t)Δ^{it}. The σ-cocycle identity for c_t (including its scalar phases) says precisely that (V_t) is a strongly continuous one-parameter unitary group [proved here]. So JOIN-4a″ ⟺ existence of a V-invariant unit vector (with an A′-marginal side condition I will not even need).

2. Physically, V_t = e^{itH} with H = dΓ(κ) + Φ(h) + const: the second-quantized dilation generator linearly coupled to a field whose form factor h has nonvanishing "zero mode" iff Q ≠ 0. This is an exactly solvable van Hove Hamiltonian (κ with two-sided Lebesgue spectrum); the question is whether 0 is an eigenvalue. The divergence of the formal dressing profile η (the client's outerness datum) is exactly the infrared criterion ĥ/ν ∉ L². [framing; the proof below is self-contained]

3. **Rigidity of the invariant state.** Let E := ⟨ξ, ·ξ⟩, a *normal* state on B(H), invariant under Ad V_t. For f in the full-line one-particle space K: V_t W(f) V_t* = e^{iφ(t,f)}W(f_t), with f_t the one-particle dilation flow and φ(t,f) = −Im⟨k_t, f_t⟩ (Weyl relations; the scalar Θ_t cancels). Invariance: E(W(f)) = e^{iφ(t,f)}E(W(f_t)) for all t.

4. **Limit.** The one-particle flow has a.c. (Lebesgue) spectrum [G1 again], so f_t → 0 weakly in K, hence W(f_t) → e^{−‖f‖²/4}·1 in WOT (coherent-vector matrix elements; [proved here]). By normality, E(W(f_t)) → e^{−‖f‖²/4} ≠ 0. Since the left side of Step 3 is t-independent: E(W(f)) ≠ 0, the phases e^{iφ(t,f)} = E(W(f))/E(W(f_t)) converge, and
  **E(W(f)) = e^{iφ_∞(f)} e^{−‖f‖²/4}**, φ_∞(f) := lim_t φ(t,f),
 for every f for which φ_∞ exists. The invariant normal state, if any, is *unique* and explicitly determined: it is the formal η-coherent shift of the vacuum.

5. **The phase functional is unbounded.** In the spectral (Mellin) representation of the flow, k̂_t(ν) = η̂(ν)(1 − e^{iνt}), and the client's linear growth ‖k_t‖² = ∫|η̂|²|1−e^{iνt}|² ~ Dt forces |η̂|² ~ (D/2π)ν^{−2} near ν = 0; in particular **η̂ ∉ L²** (this is exactly Q ≠ 0 / outerness). For f̂ smooth, compactly supported *away from ν = 0*: φ(t,f) = −Im∫η̂̄ f̂ (e^{iνt}−1) dν → Im∫η̂̄ f̂ dν =: ℓ(f) (Riemann–Lebesgue on the L¹ integrand; no PV needed on this class). Since η̂ ∉ L² by divergence at ν = 0, sup{|ℓ(f)| : ‖f‖ ≤ 1, f̂ supported in |ν| > ε} = ‖η̂·χ_{|ν|>ε}‖ → ∞. So there exist smooth f_n with ‖f_n‖_K → 0 and ℓ(f_n) = π (rescale; use if to align phases — K is a complex space, allowed).

6. **Contradiction.** ‖f_n‖ → 0 ⟹ W(f_n) → 1 strongly [standard] ⟹ E(W(f_n)) → 1. But Step 4 gives E(W(f_n)) = e^{iπ}e^{−‖f_n‖²/4} → −1. Contradiction. No invariant vector exists; no u exists. ∎

**Sanity checks [performed].** (a) If Q = 0 and η ∈ H (finite norm), η̂ ∈ L², φ_∞ is bounded, no contradiction — and indeed φ = ω(W(η)·W(η)*) is in the orbit. The mechanism is sharp: orbit membership ⟺ the unique V-invariant state (the η-coherent one) is normal ⟺ η ∈ H ⟺ Q = 0. (b) The argument never needed the A′-marginal condition, PD tests, or Θ_t explicitly — the phases enter only through the group law and cancel.

**Gaps flagged.** (G1) A.c./Lebesgue spectrum of the one-particle I-dilation generator on all of K — standard for the U(1) current net (hyperbolic flow with two fixed points, Mellin-conjugate to translation, Lebesgue spectrum, multiplicity 2), but should be cited or verified once; used twice (Prop. 1 and Step 4). (G2) The spectral representation k̂_t = η̂(1−e^{iνt}) and the Tauberian extraction |η̂|² ~ cν^{−2} — this is the client's own refereed calculus; only η̂ ∉ L² is truly needed, which is equivalent to sup_t‖k_t‖ = ∞, weaker than the exact linear law. (G3) Weyl-convention constants (factors of 2, sign of Im⟨·,·⟩) — checked to be irrelevant to unboundedness. (G4) Strong continuity of (V_t) — follows from strong continuity of t ↦ W(k_t) (norm-continuity of t ↦ k_t in H) and of Δ^{it}; routine.

## 3. Task 1 adjudication

**α ∉ Inn·Mod: YES, proved** via (R1) + Theorem — not via sector/charge language, which as the client suspected is slippery on a single local algebra. Of the client's proposed routes: (a) Connes–Takesaki module — vacuous, the flow of weights of III₁ is a point [standard]; (b) index/statistical dimension — blind, d(α) = 1, as the client says; (c) the cocycle route — this is the one that works, but through phase rigidity (Steps 3–6), not through asymptotic size alone (Section 1 shows size alone cannot suffice); (d) BW covariance — used implicitly: it is what makes σ_t geometric and delivers the explicit k_t. Note also T(A) = {0} for III₁ [standard], so σ_T itself is outer for T ≠ 0, but that alone never decides Inn·Mod membership of α; only the Theorem does.

## 4. What the client should verify (attack map for refereeing)

1. Re-derive V_tV_s = V_{t+s} from the refereed phases Θ_t (Step 1) — this is where an error in Θ would surface, though the proof survives any correct choice of phases.
2. Pin down G1 with a citation (one-particle modular theory of the current net; Longo's standard subspace machinery or direct Mellin computation).
3. Check my ξ = u*Ω bookkeeping: from u*σ_t(u) = e^{iΘ_t}W(k_t), adjoint gives σ_t(u*) = e^{−iΘ_t}W(−k_t)u*, then apply to Ω. One-line check.
4. Optional strengthening: the same argument excludes ξ = wΩ for any isometry/partial isometry w, i.e. φ is not even of the form ω(w·w*) with w an isometry in A; and it localizes the failure as an infrared theorem: **the invariant D is precisely the obstruction density** — D > 0 ⟺ φ ∉ orbit. This makes D an honest invariant of the pair (ω, φ), which is presumably what SPAN-1/KNOT-Q wants.

**Overall labels:** Theorem and Propositions — [proved here] modulo [client-verified] cocycle formula and [standard] items G1, Reeh–Schlieder, BW second quantization, strong continuity of Weyl systems. Refutation of naive 2b — [proved here]. Flow-of-weights remark — [standard, not re-fetched]. Nothing in this report is [open]: JOIN-4a″ is, in my judgment, closed in the negative once G1–G4 are written out, an afternoon's work for the client.
