# Phase 104 — JOIN-4a′ (i)+(iii-adjacent): the explicit cocycle and the divergence-rate invariant D = Q²ℓ/2π (REFEREED — all four claim groups CORRECT; see Amendment at end)

*Working session, 2026-07-24, continuing phase 104. **Status: [derived by a context-free derivation agent; NOT refereed; per standing policy no verdict is entered and nothing here carries a [refereed] tag until the pass completes].** This document preserves verbatim the derivation delivered for JOIN-4a′ task (i) — the explicit modular flow σ^{φ₂}, the explicit relative cocycle c′_t(γ), and the divergence-rate invariant of the telescoped trivializer. The derivation was produced context-free (pure operator algebras, no framework content) from the repaired setup of the JOIN-4a amendment. Six [GAP] flags are the agent's own; they are part of the record. The companion derivation (JOIN-4a′ (ii) nontriviality + B(3) closure) is running separately; the combined material goes to a fresh context-free referee before any verdict.*

**The headline, stated with its tag: [derived, unrefereed].** The candidate first entry of the data dictionary exists and is computed three independent ways with agreeing coefficient:

> **D(c, ℓ) = lim_{n→∞} ‖ζ^{(n)}_in‖²/n = Q²ℓ/2π, Q = c|I| (the charge).**

The cost of coherently erasing the n-step defect record grows *linearly*: **charge² × geodesic translation length per step, over 2π** — equivalently, rate Q² per unit of modular time 2πt. The 2π is the same T-2π normalization the record derived in phase 102; the pairing couples the defect's charge to the clock at a rate quadratic in the charge. [The agent's GAP-6 flags the plausible identification of D with relative-entropy production per γ-step (Longo's coherent-state entropy technology) as asserted, not derived — if that identification holds, the physical reading is: *erasing matter from the record costs entropy at rate charge² × length* — but that reading is NOT yet earned.]

---

## The derivation, verbatim

# Derivation report: modular flow, Connes cocycle, and winding invariant for the charged-ramp perturbation of the U(1) current net

## 0. Conventions (fixed once)

- Fourier: f̂_k = (1/2π)∫₀^{2π} f(θ)e^{−ikθ}dθ; f real ⇒ f̂_{−k} = conj(f̂_k). Labels mod constants (f̂₀ dropped), except that elements of H(I) are represented by the unique representative supported in Ī.
- One-particle inner product: ⟨f,g⟩ := 2π Σ_{k≥1} k conj(f̂_k) ĝ_k, ‖f‖² = ⟨f,f⟩. Then σ(f,g) = ∫ f g′ dθ = −2 Im⟨f,g⟩, and ω(W(f)) = e^{−‖f‖²/2}. (Any rescaling of ‖·‖ rescales the Task-3 rate accordingly; I state everything in this convention.)
- Gagliardo identity (verified on e^{ikθ} via the Fejér integral ∫(sin(kw/2)/sin(w/2))²dw = 2πk):
  ∬_{S¹×S¹} (f(u)−f(v))²/(4sin²((u−v)/2)) du dv = 8π² Σ_{k≥1} k|f̂_k|² = 4π‖f‖².
- Modular/dilation flow: σ^ω_t on A(I) is Ad Δ_I^{it}; write σ^ω_t(W(f)) = W(δ_t f) with δ_t f := f∘λ_t^{−1}, where λ_t is the Möbius dilation flow of I (λ_t ξ± = ξ±, λ_t(I)=I). Multiplier of λ_t at the endpoints: e^{±2πt}.
- γ = λ_{t₀} with translation length ℓ = 2π|t₀| > 0; multiplier e^{ℓ} at the repelling endpoint ξ₊, e^{−ℓ} at the attracting endpoint ξ₋. Write u_γ = δ_{t₀} (one-particle transport, u_γ f = f∘γ^{−1}).
- ζ_s := η − η∘λ_s; ζ := ζ_{t₀} = η − η∘γ; ζ^{(n)} := η − η∘γⁿ = Σ_{k=0}^{n−1} ζ∘γ^k (telescoping). Truncations: for a function g vanishing at ξ±, g_in := g·χ_Ī ∈ H(I) (kinks only). Since λ_sξ± = ξ±, every ζ_s vanishes at ξ±, so ζ_{s,in} ∈ H(I).
- Key pointwise identity: for θ ∈ I both θ and λ_sθ lie in I where η′ ≡ c, and the arc between them lies in I, so
  ζ_s(θ) = c(θ − λ_sθ), ζ(θ) = c(θ − γθ), θ ∈ Ī.  (∗)
- Q := ∫_I η′ dθ = η(ξ₊) − η(ξ₋) = c|I| (the charge; coordinate-invariant).

Throughout, β := Ad W(η)|_{A(I)}: note β(W(f)) = e^{−iσ(η,f)}W(f) ∈ A(I), so β is a *-automorphism of A(I) even though W(η) ∉ A(I). φ₂ = ω∘β.

## 1. Task 1: the modular flow σ^{φ₂}

### (a) Boundedness of the mean functional

For f with supp f ⊂ Ī (canonical representative), the mean is μ(f) = c∫_I f = 2πc Σ_{k≠0} conj(χ̂_k) f̂_k with χ̂_k = (e^{−ikθ₋} − e^{−ikθ₊})/(2πik), so |χ̂_k| ≤ 1/(π|k|). Cauchy–Schwarz with weight |k|:

|μ(f)| ≤ 2π|c| (Σ_{k≠0}|χ̂_k|²/|k|)^{1/2} (Σ_{k≠0}|k||f̂_k|²)^{1/2}, Σ_{k≥1}|χ̂_k|²/k ≤ ζ(3)/π² < ∞.

So χ_I ∈ H^{−1/2} (coefficients ~1/k, dual norm Σ|χ̂_k|²/k ~ Σ1/k³ < ∞ — confirmed), and μ is a bounded real-linear functional on H(I). Meaning: φ₂ is a bounded coherent (mean-shift) perturbation of ω on A(I); normality and faithfulness are consistent with this (here they are anyway manifest since φ₂ = restriction of the vector state ⟨W(η)Ω, · W(η)Ω⟩). One zero-mode caveat: μ(f) = c∫_I f is not defined on labels mod constants globally; the honest functional is f ↦ −σ(η,f) (well defined mod constants because ∫_{S¹}η′ = 0). On H(I), with supported representatives, the two agree.

### (b) Riesz representer vs. coherent implementer — the reconciliation

Real Riesz on (H, Re⟨·,·⟩) gives a unique h_μ ∈ H with μ = Re⟨h_μ, ·⟩; its Re-orthogonal projection onto the closed real subspace H(I) represents μ|_{H(I)}. So a representing vector for the FUNCTIONAL exists inside H(I). No contradiction so far.

But Ad W(g) shifts Weyl generators by the SYMPLECTIC pairing: Ad W(g)(W(f)) = e^{−iσ(g,f)}W(f), and σ(g,f) = −2Im⟨g,f⟩ = Re⟨−2ig, f⟩. Hence a local coherent implementer g ∈ H(I) with σ(g,·)|_{H(I)} = −μ exists iff the Riesz representer lies in iH(I) — an i-rotation condition which the real subspace H(I) does not respect (H(I) ∩ iH(I) = {0}, H(I)+iH(I) only dense; equivalently the correspondence "bounded functional ↦ σ-representer in H(I)" involves Δ^{1/2} and is unbounded/densely defined in type III). Concretely: σ(g,f) = −∫g′f = −c∫_I f for all f ∈ C_c^∞(I) forces g′ = c on I; combined with supp g ⊂ Ī this forces g = truncated ramp η_in (mod constants), which has at least one endpoint jump — the two jump sizes differ by Q = c|I| ≠ 0, so no additive constant kills both — and a jump gives f̂_k ~ 1/k, hence ‖·‖² ~ Σ 1/k divergent. So:

- μ bounded on H(I): TRUE.
- Real-Riesz representer of μ in H(I): EXISTS.
- Coherent (Weyl) implementer of the state shift inside A(I): DOES NOT EXIST (i-rotation obstruction; concretely the log-divergent jump).

This is exactly the expected type-III phenomenon: H(I) + H(I′) dense but not closed, and the ramp-primitive sits "at infinity" of H(I).

### (c) Explicit σ^{φ₂}: closed form EXISTS

Since φ₂ = ω∘β with β ∈ Aut(A(I)), the standard rule σ^{ψ∘α}_t = α^{−1}σ^ψ_t α gives σ^{φ₂}_t = β^{−1}∘σ^ω_t∘β. On generators (supp f ⋐ I):

σ^{φ₂}_t(W(f)) = e^{−iσ(η,f)+iσ(η,δ_t f)} W(δ_t f) = e^{iσ(η∘λ_t − η, f)}W(δ_t f) = e^{−iσ(ζ_t,f)}W(δ_t f),

using Möbius invariance of σ (σ(η, f∘λ_t^{−1}) = σ(η∘λ_t, f)). Since supp f ⊂ I, only ζ_{t,in} pairs, and σ(ζ_{t,in}, f) = σ(k_t, δ_t f) with k_t := δ_t ζ_{t,in} = (η∘λ_t^{−1} − η)·χ_Ī = −ζ_{−t,in} ∈ H(I). Hence, boxed:

**σ^{φ₂}_t = Ad W(k_t) ∘ σ^ω_t on A(I), k_t = (η∘λ_t^{−1} − η)χ_Ī ∈ H(I);**
**equivalently σ^{φ₂}_t(W(f)) = exp( i c ∫_I (1 − λ_t′(θ)) f(θ) dθ ) · W(f∘λ_t^{−1}).**

(The scalar form of the phase uses ζ_t′ = c(1−λ_t′) on I, from (∗).) Group law check: k_{t+s} = k_t + δ_t k_s (telescoping, χ_Ī flow-invariant), and Ad W(k_t)σ^ω_t · Ad W(k_s)σ^ω_s = Ad W(k_t + δ_t k_s)σ^ω_{t+s} — the Weyl phase is killed by Ad. t = 0 gives identity. So a closed form exists; the subtlety of (b) obstructs a coherent trivializer of the STATE, not of the FLOW, because ζ_t vanishes at the fixed points (kinks only) while η_in does not.

[GAP-1] Extension of the generator formula from f ∈ C_c^∞(I) to Weyl operators with symbols in the closed subspace H(I), and the fact W(h) ∈ A(I) for all h ∈ H(I): standard second-quantization continuity (W(f_n) → W(h) strongly when f_n → h in H); asserted, not re-proved.

Supplement (standard-subspace toolkit, derived): the cutting projection of H(I) — the projection P onto K := H(I) along iK′ (K′ = H(I′)) on the dense domain K + iK′ — satisfies, with S = JΔ^{1/2} the Tomita operator of K: for ξ = k + ik′, Sk = k and JΔ^{1/2}k′ = Δ^{−1}k′ (from JΔ^{−1/2}k′ = k′ and JΔ^{1/2} = Δ^{−1/2}J), hence ξ + ΔSξ = (1+Δ)k, i.e.

P = (1+Δ)^{−1}(1 + Δ^{1/2}J) on H(I) + iH(I′).

[GAP-2] Closability/core statements for P asserted. P is not needed for the boxed results; it is the tool that would compute S(φ₂‖ω) à la Longo's coherent-state entropy formula — not rederived here.

Also for reference (needed nowhere below, flagged): the Connes cocycle against the vacuum, [Dφ₂:Dω]_t, has the form e^{iϑ_t}W(k_t) with ϑ_t determined up to a character e^{iλt} by the σ^ω-cocycle equation; pinning λ requires the relative KMS/analyticity condition. [GAP-3] I could not pin ϑ_t: the natural regularization η_in^ε (smoothing the jumps at scale ε) fails, because δ_t rescales the smearing scale at ∂I by e^{±2πt}, leaving a boundary "vortex" of ε-independent norm ~|η(ξ±)|²·2π|t|/2π; the regularized cocycles converge only weakly to a non-unitary. This is why Task 2 is done strictly in-algebra, where no such ambiguity arises.

## 2. Task 2: explicit c′_t(γ)

Set z := −ζ_in ∈ H(I). By the established transport identity and the inner-perturbation formula, c′_t(γ) = W(z)* σ^{φ₂}_t(W(z)). Using the boxed flow (extended per [GAP-1]) and Weyl relations W(−z)W(δ_t z) = e^{iσ(z,δ_t z)/2}W(δ_t z − z):

**c′_t(γ) = e^{iΘ_t} W(ρ_t), with**
**ρ_t = (1 − δ_t)ζ_in = ζ_in − ζ_in∘λ_t^{−1} ∈ H(I),**
**Θ_t = σ(ζ_t, ζ_in) + ½ σ(ζ_in, δ_t ζ_in).**

Fully explicit via (∗) (θ = original circle coordinate; γ, λ_t = Möbius actions; γ and λ_t commute, same one-parameter group):

ρ_t(θ) = c[(θ − γθ) − (λ_t^{−1}θ − γλ_t^{−1}θ)]·χ_Ī(θ);

Θ_t = c² [ ∫_I (θ − λ_tθ)(1 − γ′(θ)) dθ + ½ ∫_I (θ − γθ) · d/dθ(λ_t^{−1}θ − γλ_t^{−1}θ) dθ ].

Both integrals are elementary (Möbius rational functions; closed forms exist but are chart-dependent and messy — not evaluated further; finite, since all integrands are bounded on Ī). Dependence extracted: ρ_t is linear in c; Θ_t is quadratic in c; the ℓ-dependence enters through γ = Λ_I(ℓ) (e.g. in the (0,1) chart γu = ue^{−ℓ}/(1−u+ue^{−ℓ}), γ′(u) = e^{−ℓ}/(1−u+ue^{−ℓ})²).

ℤ-cocycle identity. With w_n(t) := c′_t(γⁿ) built from ζ^{(n)}_in: general Connes chain rule [Dψ:Dφ] = [Dψ:Dχ][Dχ:Dφ] plus covariance [D(ψ∘α):D(φ∘α)]_t = α^{−1}([Dψ:Dφ]_t) (α = Ad U(γ^m) preserves A(I)) give

w_{m+n}(t) = Ad U(γ^{−m})(w_n(t)) · w_m(t).

Symbol-level verification with my formulas: ζ^{(m+n)} = ζ^{(m)} + ζ^{(n)}∘γ^m, truncation and δ_t commute with γ-transport (same one-parameter group, ∂I fixed), so ρ^{(m+n)}_t = ρ^{(m)}_t + (ρ^{(n)}_t)∘γ^m, matching Ad U(γ^{−m})W(g) = W(g∘γ^m) and Weyl addition. [GAP-4] The scalar-phase bookkeeping of this identity holds automatically by the abstract chain rule (the cocycles exist and are unique); the direct Weyl-algebra verification of the phases was not carried out.

## 3. Task 3: winding / divergence-rate invariant

Trivializer uniqueness. A local coherent trivializer of the n-step cocycle is g ∈ H(I) with σ(g − ζ^{(n)}_in, f) = 0 for all f ∈ C_c^∞(I), i.e. g − ζ^{(n)}_in locally constant on I and supported in Ī; any nonzero such difference is a step function with jumps, hence ∉ H^{1/2}. So ζ^{(n)}_in is the UNIQUE coherent trivializer in H(I), and "minimal norm" = ‖ζ^{(n)}_in‖.

Growth. Exact model (I = (0,1), γu = uq/(1−u+uq), q = e^{−ℓ}):

ζ^{(n)}(u)/c-analogue f_n(u) = u − γⁿu = (1−q_n)·u(1−u)/(1−u+uq_n), q_n = e^{−nℓ}.

f_n is the ramp u minus the exact correction h_n(u) = −u q_n/(1−u+uq_n): a smeared jump of height ~1 at ξ₊ at scale q_n. Fourier profile of ζ^{(n)}_in on the circle: jump-like plateau of height Q smoothed at scale ε_n ≍ e^{−nℓ}, so |ĝ_k|² ≈ Q²/(4π²k²) for 1 ≲ k ≲ e^{nℓ}, faster decay beyond (kinks only). Hence with ‖·‖² = 2πΣ_{k≥1}k|ĝ_k|²:

Σ_{k≤e^{nℓ}} k·Q²/(4π²k²) = (Q²/4π²)·nℓ + O(1) ⇒ ‖ζ^{(n)}_in‖² = (Q²/2π)·nℓ + O(1).

Independent confirmation A (Gagliardo, exact leading term): the cross-region pairs (u ∈ I, v ∈ I′) give G_cross ≈ 2∫_I f² (1/d₊ + 1/d₋) du = 2Q²·nℓ + O(1) (the model integral ∫₀¹ s ds/(s+q_n)² = log(1/q_n) + O(1) = nℓ + O(1)); all other regions (within-I transition, attracting endpoint, diagonal) are O(1) — the smooth scale-q_n transition has scale-invariant finite Ḣ^{1/2} energy. Then ‖·‖² = G/4π ⇒ same coefficient Q²ℓ/2π per step.

Independent confirmation B (spectral density): ζ^{(n)}_in = Σ_{k=0}^{n−1} u_γ^{−k}ζ_in; ‖Σ u^k v‖² ~ n·(2π/ℓ)·ρ_v(0), where ρ_v is the spectral density of v for the dilation generator; the truncated-jump amplitude ~ Q/(2π|x|) times the factor |1 − e^{iℓx}|² ~ ℓ²x² from ζ = (1 − u_γ)η-structure gives ρ_{ζ_in}(0) = Q²ℓ²/4π², so rate = (2π/ℓ)(Q²ℓ²/4π²) = Q²ℓ/2π. Consistent.

Modular-time version: for fixed t and n → ∞, ‖(1−δ_t)ζ^{(n)}_in‖² → Q²·|2πt|/(2π)·(1+o(1)) — i.e. rate Q²/2π per unit of translation length, whether the length is spent in γ-steps (ℓ per step) or modular time (2π|t|). So it is LINEAR in n (not log n), linear in ℓ, quadratic in the charge:

**Divergence-rate invariant: D(c,ℓ) := lim_{n→∞} ‖ζ^{(n)}_in‖²/n = Q²ℓ/(2π), Q = c|I| = ∫_I η′ dθ.**

("charge² × geodesic translation length", in the normalization ⟨f,g⟩ = 2πΣ_{k≥1}k conj(f̂_k)ĝ_k, ω(W(f)) = e^{−‖f‖²/2}; rescaling ‖·‖² by κ rescales D by κ.) [GAP-5] The O(1) terms and the interchange of limits in confirmations A/B are estimated, not proved with uniform constants; the leading linear term is however forced by the exact model integral. [GAP-6] The expected identification of D (up to a factor 1/2 or 1/4) with relative-entropy production per γ-step via Longo's coherent-state entropy formula is asserted as plausible, not derived.

## 4. Sanity checks

(a) c = 0: η constant on I ⇒ ζ_s|_Ī = 0 for all s ⇒ ζ_in = 0, k_t = 0, ρ_t = 0, Θ_t = 0 (∝ c²) ⇒ σ^{φ₂} = σ^ω and c′_t(γ) ≡ 1; also φ₂ = ω on A(I) directly. Passes.
(b) Fiber-valuedness: ζ_{t,in}, k_t, ζ_in, ρ_t all vanish at ξ± with kinks only ⇒ lie in H(I) ⇒ W(ρ_t) ∈ A(I) (modulo [GAP-1]). Passes.
(c) t = 0: ρ₀ = 0, Θ₀ = 0 ⇒ c′₀ = 1. Connes identity: c′_t(γ) = v*σ^{φ₂}_t(v) with v = W(−ζ_in) unitary gives c′_{t+s} = v*σ_{t+s}(v) = v*σ_t(v)·σ_t(v*σ_s(v)) = c′_t·σ^{φ₂}_t(c′_s) identically; at symbol level ρ_{t+s} = ρ_t + δ_t ρ_s checks. Passes.
Consistency of the transport identity with conventions: φ₂∘AdU(γ)(W(f)) = ω(W(f))e^{−iσ(η∘γ,f)} and φ₂∘AdW(−ζ_in)(W(f)) = ω(W(f))e^{iσ(ζ_in,f)−iσ(η,f)} agree iff σ(ζ − ζ_in, f) = 0 for supp f ⊂ I — true since ζ_out pairs trivially. Passes.

## Boxed results

1. σ^{φ₂}_t = Ad W(k_t)∘σ^ω_t, k_t = (η∘λ_t^{−1} − η)χ_Ī ∈ H(I); scalar form σ^{φ₂}_t(W(f)) = e^{ic∫_I(1−λ_t′)f dθ} W(f∘λ_t^{−1}).
2. c′_t(γ) = e^{iΘ_t}W(ρ_t), ρ_t = (1−δ_t)ζ_in = c[(id−γ) − (id−γ)∘λ_t^{−1}]χ_Ī, Θ_t = σ(ζ_t,ζ_in) + ½σ(ζ_in,δ_tζ_in) = c²[∫_I(θ−λ_tθ)(1−γ′)dθ + ½∫_I(θ−γθ)d(λ_t^{−1}θ−γλ_t^{−1}θ)] (∝ c²; ℓ enters through γ = Λ_I(ℓ)). ℤ-cocycle: w_{m+n}(t) = AdU(γ^{−m})(w_n(t))·w_m(t).
3. D(c,ℓ) = lim_n ‖ζ^{(n)}_in‖²/n = Q²ℓ/(2π), Q = c|I| — linear in n and ℓ, quadratic in charge; equivalently rate Q² per unit modular time 2πt.

## Honest summary

Proven at the level of rigorous computation (given the stated standard inputs): the automorphism identity β = AdW(η)|_{A(I)}, the closed form of σ^{φ₂}_t and its group law; the in-algebra formula for c′_t(γ) with explicit ρ_t and Θ_t and all of Task 4's checks; boundedness of the mean functional (χ_I ∈ H^{−1/2}); the nonexistence of a local coherent implementer (jump obstruction) and its precise reconciliation with real-Riesz representation (the i-rotation/iH(I) criterion); uniqueness of the coherent trivializer ζ^{(n)}_in in H(I); the exact model integral forcing linear-in-n growth; and the cutting-projection formula P = (1+Δ)^{−1}(1+Δ^{1/2}J) modulo domain statements. Asserted/standard-but-not-reproved: continuity extension of Weyl calculus to closed-subspace symbols ([GAP-1]), closability details for P ([GAP-2]), the exact scalar phase of the vacuum-relative cocycle [Dφ₂:Dω] — genuinely obstructed, with the boundary-vortex mechanism identified ([GAP-3]) but irrelevant to the boxed results — phase bookkeeping in the ℤ-cocycle identity beyond the abstract chain rule ([GAP-4]), uniform O(1) control in the asymptotics ([GAP-5]), and the entropy interpretation of D ([GAP-6]). The coefficient Q²ℓ/2π was obtained three ways (circle Fourier, Gagliardo cross-term with the exact Möbius model, spectral density of the dilation unitary) which agree; its normalization is convention-tied as stated.

---

## Amendment (2026-07-24, same session) — combined referee verdict entered

*Report verbatim in `reviews/REPORTS-phase104-JOIN4a-prime-referee-2026-07-24.md`.*

**All four claim groups CORRECT [now derived, refereed]:** (D1-a) the modular flow σ^{φ₂}_t = AdW(k_t)∘σ^ω_t with sign, direction, group law, and H(I)-membership all verified; (D1-b) the explicit cocycle c′_t(γ) = e^{iΘ_t}W(ρ_t) verified including the CCR phase collection; (D1-c) **the invariant D = Q²ℓ/2π confirmed with the constant independently re-derived in circle and line frames** (the referee specifically confirmed the single-near-jump structure that fixes the coefficient — a two-edge model would have doubled it); (D1-d) uniqueness of the coherent trivializer verified.

**One scope demotion, entered honestly (from the same referee's D2-f finding):** D's advertised role as a *dynamical obstruction* is void — the twisted quantity ‖(1−δ_t)ζ^{(n)}_in‖² is bounded (exact coboundary identity; see the nontriviality document's amendment). **D survives as a refereed norm asymptotic — the growth rate of the coherent-erasure cost — not as an obstruction to general erasure.** The "charge × length" pairing is real mathematics; what it obstructs is coherent operations only.

**Errata:** the companion document's e^{−¼‖·‖²} should be e^{−½‖·‖²} under the stated Weyl-state convention; the log-frame spectral heuristic used in places is invalid for the Möbius-invariant norm (log is not a Möbius chart) — the line-frame computation is the correct one and is what the referee verified.
