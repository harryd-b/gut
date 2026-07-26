# REPORT — phase 109 D-MS upgrade referee pass (2026-07-26, verbatim)

*Context-free adversarial referee on the D-MS upgrade derivation (phases/phase109-DMS-upgrade.md). The referee independently reran the locality numerics (2¹⁷ grid, three profile families; divergence coefficient = ∫ρ̃² to 8 digits) and adjudicated the flagged potential error (linear charge conjugation) in the derivation's favor.*

*Verdict summary: the theorem's skeleton is CONFIRMED — scheme space = one function F; covariance insufficient (counterexample λQ²ℓ stands); J insufficient; C-evenness + fusion-additivity ⟹ F ≡ 0 pointwise (the referee simplified the algebra: even + additive is 2F = 0 directly, no Cauchy/measurability needed). The C-symmetry worry is RESOLVED IN FAVOR: linear C (f ↦ −f) is a genuine unitary symmetry of the chiral theory (symplectic, norm-preserving, commutes with the complex structure, fixes the Sugawara stress tensor — chirality untouched); it coexists with, and differs from, the record's antiunitary J, and formula-evenness alone would NOT have sufficed. Fusion naturality ruled NOT circular. THE MAJOR REPAIR: "MS satisfies S4" at framing n ≠ 0 is UNPROVEN — it requires the mutual phase to contain a framing cross term nQ₁Q₂ beyond the refereed −Q₁Q₂; the counterterm μnQ² survives every axiom except S4-at-n≠0, so without the framing cross term the axioms select the framing-DELETED scheme D = ∓Q²/2, not D-MS. What is proven: UNIQUENESS OF THE S4-SCHEME; the identity of that scheme with D-MS pends ONE decisive computation — the mutual phase in a framing sector (registered below as M-FRAME). Additional repairs: define schemes via the ε→0 limit; write out the geodesic-transitivity and g ~ g⁻¹ closures; state the quadraticity-of-the-transport-functional bridge hypothesis (GAP-2 is a real joint); state the uniformity-of-E3-over-distorted-profiles premise; fix the F_unif sign/framing bookkeeping. Verdicts entered in the phase-109 amendment. Report verbatim below; standing AI-referee caveat applies.*

---

## Referee Report: SPAN-2 (scheme-uniqueness theorem for D-MS)

**Summary.** The theorem's skeleton — scheme space = one finite function F; covariance insufficient (K3); J insufficient (K4); C-evenness + fusion-additivity ⟹ F ≡ 0 (K7) — is essentially sound, and the flagged worry about C (adjudication E) is resolved in the derivation's favor: linear C is a genuine unitary symmetry of the chiral u(1) theory, not a formula accident. The algebra of K7 is correct but over-engineered (evenness + additivity kills F pointwise; no Cauchy/measurability needed). The serious problem is in the *n-dependence*: the counterterm μnQ² survives S2, S3 (it is C-even), covariance, and J-equivariance, and is killed **only** by S4 in framing sectors n ≠ 0. There, "MS satisfies S4" requires the mutual phase M = (n∓1)Q₁Q₂ — including a framing cross term nQ₁Q₂ that the refereed pair entry (which certifies only the −Q₁Q₂ cross of the −Q²/2 part) does not cover. If the physical M lacks the framing cross, S4 uniquely selects D = ∓Q²/2 (framing term deleted), *not* D-MS. So GAP-4 is materially understated: it is load-bearing for *which* scheme is unique, not merely for the rival's refutation. I reran the locality numerics independently (2¹⁷ grid, three profile families): all block-level claims confirmed. Verdicts follow.

---

### 1. K1 (Adjudication A) — Scheme space reduces to one function F. **CORRECT WITH REPAIR**

Shape-independence of F is trivially forced: subtracted value = (exactly shape-independent finite part) − F, so demanding shape-independence of the output forces it of F. Correct. Two repairs needed:

(a) *ε-sequence trick*: a scheme with ε-dependent finite part F_ε is only a scheme if the subtracted value has an ε → 0 limit; any convergent F_ε collapses to its limit, and non-convergent F_ε (e.g. log-periodic oscillation) fails to define a limit. This is fine, but only if the derivation *states* that a scheme's output is defined as the ε → 0 limit. Without that clause, bounded-oscillatory "schemes" exist and K1 fails. State it.

(b) *Other invariant data*: anchor-pair position is excluded because PSL(2,ℝ) acts transitively on geodesics (ordered boundary pairs); the conjugacy class of the hyperbolic transport element is exactly ℓ (g and g⁻¹ are conjugate in PSL(2,ℝ) via the π-rotation about a point of the axis), so no data survives beyond ℓ. Orientation of traversal must be declared as folded into (n, branch). These closures should be written out; they are true but not automatic.

Also note K1 implicitly restricts to *per-defect* (diagonal) schemes; configuration-dependent counterterms are excluded only once S1 is invoked. The dependency should be attributed to S1, not to K1.

### 2. K2 (Adjudication B) — Power vs. log. **CORRECT WITH REPAIR**

The adjudication is right in substance: subtracting a pure power a/ε introduces no reference scale (the subtracted value is invariant under ε → λε), whereas log(1/ε) subtraction forces a choice of μ and MS would be a μ-family, not a point. Good.

Repair: the frame-independence argument has an unaddressed O(1) subtlety. A Möbius map distorts the ramp profile by relative O(ε); this shifts c_ρ by O(ε), which multiplied by 1/ε is an **O(1)** contribution. Subtracting the transformed profile's *own* divergence handles this only if the E3 expansion Φ_ε = πc_ρQ²/ε + finite + o(1) holds *uniformly over the ε-dependent family* of distorted profiles. E3 was refereed at fixed shape. Uniformity is plausible (smooth compact family) but is an unproven analytic premise and must be flagged. For the pure ∫(f′)² block this is exact (finite part identically zero for any profile — confirmed numerically), but the full transport functional inherits no such exactness automatically.

### 3. K3 (Adjudication B) — Covariance counterexample. **CORRECT**

F = λQ²ℓ and λ′Q² are Möbius-invariant, scale-free, shape-independent: genuinely admissible under covariance alone. Does refereed structure secretly exclude λQ²ℓ pre-fusion? Only if J-equivariance is *imposed* on schemes — but the refereed mirror law is a property of D-MS, not an a priori constraint on the scheme space; a non-equivariant scheme is ugly, not contradictory. So the counterexample stands and the theorem's logical structure (covariance-only refuted by K3; J-equivariance then kills the J-even ones in K4) is correctly ordered. The additive structure of D-MS itself constrains nothing about F.

### 4. K4 (Adjudication C) — J-parity classification. **CORRECT** (minor bookkeeping)

With J: (Q, ℓ, n, ±) ↦ (Q, ℓ, −n, ∓) and the derived requirement F(Jd) = −F(d) (verified: D_F(Jd) = −D_F(d) ⟺ F(Jd) = −F(d), using the refereed odd law for D-MS): μnQ² ↦ −μnQ² is J-odd ✓; branch-odd λ(±)Q² with λ(∓) = −λ(±) is J-odd ✓; λQ², λQ²ℓ are J-even, killed ✓.

Uniform-background closure: setting all spins to zero at general n gives F_unif = ∓Q²/2 + nQ²/2 = (n∓1)Q²/2, **both** terms J-odd, hence J-equivariant — conclusion (J alone cannot decide) confirmed. Two nits: the brief's "F_unif = ±Q²/2" (i) drops the framing part (correct only at n = 0, or if the uniform closure keeps the framing term — specify which), and (ii) has the opposite branch sign from D_F = D_MS − F (should be ∓Q²/2); fix the convention or the sign.

### 5. K5 (Adjudication D) — Locality numerics and GAP-2. **CORRECT** (numerics) / **UNPROVEN as support for S1**

Independent rerun (2¹⁷ grid; linear, cosine, quadratic-bump ramp families, ∫ρ̃² = 1, π²/8, 1.2): divergence coefficient of ∫(f′)² fits a/ε + b with a = ∫ρ̃² to 8 digits (cos, quad; linear limited to ~10⁻³ by spectral ringing at the profile kinks — a numerical artifact, not a physics discrepancy). Cross terms between defects at fixed separation: H^{1/2} cross pairing shape-independent to 6 digits across all pairings at each ε and convergent in ε; σ(f₁, f₂) exactly positional (zero/combinatorial, shape- and ε-independent); energy cross exactly zero (disjoint supports). All block claims verified.

GAP-2 honest assessment: **this is one of the two weak joints.** The inference "blocks are local ⟹ full transport divergence is local" is valid **iff the transport functional is exactly quadratic in the profile** (as Weyl-cocycle phases are: Φ(f₁+f₂) = Φ(f₁) + Φ(f₂) + bilinear cross, and bilinear-cross finiteness follows from the block results). The refereed E3 result is a *value* formula, not a certificate of functional quadraticity; any non-bilinear ingredient (normal-ordering choice varying with configuration, branch-dependent non-quadratic phase) voids the inference. The derivation should state quadraticity as the explicit bridge hypothesis; with it, GAP-2 closes; without it, the numerics prove nothing about the transport phase.

### 6. K6/S3 (Adjudication E) — Is linear C a symmetry? **CORRECT**

This was flagged as a potential real error; it is not one. C: f ↦ −f is (i) symplectic (σ bilinear: σ(−f, −g) = σ(f, g)); (ii) norm-preserving; (iii) commuting with the complex structure (−id commutes with everything), hence unitarily implemented in the vacuum sector with trivial Bogoliubov content; (iv) an automorphism of the u(1) current algebra J ↦ −J fixing the Sugawara stress tensor T ∼ :J²: — so conformal structure and **chirality are untouched**. No reflection is needed: the antiunitary refereed J combines conjugation with reflection precisely because antiunitarity flips chirality; the linear C is a *different, coexisting* symmetry and needs no such compensation. C acts only on the field, fixing (γ, ℓ, n, branch) and sending Q ↦ −Q, so C-equivariance of the scheme legitimately forces F even. Crucially, "true of the formula" would **not** have sufficed (evenness of D-MS constrains D-MS, not F); the argument stands only because C is a genuine symmetry — the derivation should say so explicitly and distinguish C from the refereed antiunitary J. Note S3 is doing indispensable work: without it, additivity alone leaves F = κ(ℓ, n, branch)·Q alive.

### 7. K6/S4 (Adjudications E, F) — Fusion naturality. **CORRECT WITH REPAIR (major)** — not circular, but MS-satisfies-S4 is unproven at n ≠ 0

*Circularity check*: S4 is not disguised additivity of F. The counterterm-sum half follows from S1 + per-defect schemes; scheme-independence of M is then a theorem (per-defect counterterms cannot touch the UV-finite cross term); the genuine axiomatic content is identifying the merged pair with the single defect of charge Q₁+Q₂ (supported by the refereed totals-only entry, modulo the uncontrolled δ → 0 limit — GAP-3 correctly flagged). Given all that, subtracting the S4 relations for scheme F and for MS yields F(Q₁+Q₂) = F(Q₁) + F(Q₂). Clean.

*The hole*: this subtraction requires **MS itself to satisfy S4 in every sector**. At fixed (n, branch), D-MS(Q) = (n∓1)Q²/2, so MS satisfies S4 iff M_raw = (n∓1)Q₁Q₂ — i.e. the mutual phase must contain the **framing cross term nQ₁Q₂**. The refereed pair entry certifies only the −Q₁Q₂ cross of the −Q²/2 part. If the physical mutual phase at n ≠ 0 is only ∓Q₁Q₂ (framing being pure self-linking, with no mutual framing — a physically natural alternative), then solving the S4 constraint gives F(Q₁+Q₂) − F(Q₁) − F(Q₂) = nQ₁Q₂, i.e. F = nQ²/2 + (additive), and with S3 the S4-selected scheme is D = ∓Q²/2: **unique, but not MS**. Since μnQ² survives S2, S3 (C-even: μn(−Q)² = μnQ²), covariance, and J-equivariance (J-odd), and is killed *only* by S4 at n ≠ 0, the uniqueness of MS specifically — as opposed to uniqueness of *some* scheme — hangs entirely on the unrefereed framing cross term. GAP-4's description ("the value M = −Q₁Q₂ is used only against the rival closure") materially understates this.

### 8. K7 (Adjudication F) — Even + additive ⟹ F ≡ 0. **CORRECT** (with simplification)

The correct chain: additivity ⟹ F(0) = 0 and F(−Q) = −F(Q) (odd); S3 ⟹ F(−Q) = F(Q) (even); hence 2F(Q) = 0 for every Q — pointwise, on lattice or ℝ, **no Cauchy/measurability needed**. The text's lattice step F(mQ₀) = mF(Q₀) and the ℝ-case regularity apparatus are redundant (harmless, but they misrepresent where the strength lies). Kill-list verified: λQ², λQ²ℓ, ±Q²/2, μnQ² all quadratic in Q, killed by additivity at fixed (ℓ, n, branch); constants killed by F(0) = 0. But per §7, additivity at fixed n ≠ 0 rests on the unproven framing cross term.

### 9. K8 — Diagnosis of the uniform closure. **CORRECT**

F_unif = (n∓1)Q²/2 is C-even ✓, covariant ✓, J-odd ✓, quadratic hence non-additive ✓; equivalently: all spins zero while the scheme-independent mutual phase −Q₁Q₂ ≠ 0 violates the abelian spin–statistics relation θ(Q₁+Q₂) − θ(Q₁) − θ(Q₂) = M. It fails exactly S4 and nothing else. Sound, given refereed M ≠ 0 (which at the branch/n = 0 level *is* refereed).

### 10. K9 — Verdict box. **CORRECT WITH REPAIR**

"Not upgradable from covariance alone or J alone": correct (K3, K4 survivors). "Upgraded on {S1, S2, S3, S4}": the derivation is valid *given* (i) quadraticity of the transport functional (sharpens GAP-2), (ii) uniformity of E3 over distorted-profile families (new, from §2), and (iii) M_raw = (n∓1)Q₁Q₂ at n ≠ 0 (sharpens GAP-3/GAP-4). The dependency structure is otherwise accurately stated, but the box must be amended: without (iii) the theorem proves *uniqueness of the S4-scheme*, and its identity with D-MS (versus D = ∓Q²/2, framing deleted) is open.

---

## Summary

1. **K1** — CORRECT WITH REPAIR (define scheme as ε → 0 limit; write out geodesic-transitivity and g ∼ g⁻¹ closures).
2. **K2** — CORRECT WITH REPAIR (uniformity of E3 o(1) over ε-dependent distorted profiles is an unstated analytic premise; O(ε) shape shift × 1/ε = O(1)).
3. **K3** — CORRECT (λQ²ℓ admissible; mirror law does not pre-exclude it).
4. **K4** — CORRECT (parity classification verified; fix the ± sign and the dropped nQ²/2 in F_unif).
5. **K5** — numerics CORRECT (independently reproduced); as support for S1: UNPROVEN without explicit quadraticity of the transport functional (GAP-2 is a real joint).
6. **K6/S3** — CORRECT: linear C is a genuine unitary symmetry of the chiral theory (J ↦ −J fixes Sugawara T; no chirality obstruction); state that formula-evenness alone would not suffice.
7. **K6/S4** — CORRECT WITH REPAIR, not circular; but **MS-satisfies-S4 at n ≠ 0 is UNPROVEN**: it needs the framing cross term nQ₁Q₂ in M, beyond the refereed −Q₁Q₂.
8. **K7** — CORRECT; simplify (even + additive is pointwise zero; drop Cauchy/measurability).
9. **K8** — CORRECT.
10. **K9** — CORRECT WITH REPAIR: uniqueness-of-a-scheme stands on the axioms; **uniqueness-of-MS additionally requires the unverified framing cross term** — GAP-4 as stated understates its load; μnQ² is the counterterm that survives everything except S4-at-n ≠ 0.

Headline for the authors: verify M_raw in a framing sector n ≠ 0 (or prove mutual framing vanishes/equals nQ₁Q₂ from the transport construction). That single computation decides whether the unique scheme is D-MS or ∓Q²/2.
