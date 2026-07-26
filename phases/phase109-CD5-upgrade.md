# Phase 109 — convention upgrades, part 3: C-D5 (REFEREED 2026-07-26; UPGRADED to value-theorem under H1+H2 — see Amendment)

*Working session, 2026-07-26, executing the operator's instruction to attempt convention upgrades. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered; C-D5 remains an adopted convention until a referee rules].***

*Headline claims (pre-verdict): (1) the shared-anchor ambiguity reduces EXACTLY to one overlap parameter w ∈ [0,1] per shared anchor, with the same-axis value σ = Q₁Q₂(w_a + w_b − 1) exact at every ε — the scheme space is the square [0,1]², sweeping all of Q₁Q₂·[−1,1], with the prior referee's ±Q₁Q₂ counterexamples as the corners and C-D5 as the center; (2) the session's conjecture is REFUTED AS STATED: J-equivariance alone does not force C-D5 — an explicit charge-DEPENDENT scheme (displacement by sgn(Q₁)·3ε) is exactly J-equivariant with σ_reg = |Q₁|Q₂ ≠ 0; the exact obstruction is that r maps the configuration to the charge-negated configuration, so equivariance only LINKS two configurations; (3) UPGRADED as a theorem under (H1) charge-independence + (H2) J-equivariance: every collar is forced to satisfy h∘r = 1 − h (r-antisymmetry, value 1/2 at the anchor), whence w_a = w_b = 1/2 and σ = 0 EXACTLY at every ε — C-D5-as-VALUE is the theorem; C-D5-as-SCHEME is forced only up to the r-antisymmetric class (common shape not forced; scheme↦value non-injective two ways); (4) the single-shared-anchor case (impossible for discrete groups, well-posed abstractly) is honestly undecided by equivariance alone — the canonical swap-reflection yields only a consistency identity — and is resolved by an added anchor-locality axiom (H3) to w = 1/2, giving a HALF-INTEGER extension of the crossing number (î ∈ ½ℤ, same-axis diagonal = +½ − ½ = 0); (5) recommended dictionary update: C-D5 = theorem under H1+H2 for shared axes; convention only through H3 for configurations that do not occur in the discrete-group setting. Extensive numerics (12-row table) verify the value formula, both counterexample corners, the exact equivariance identities, and the half-integer values. Goes to a context-free referee before any verdict.*

---

## The derivation, verbatim

# C-D5 Upgrade Attempt: Is the Symmetric Regularization Forced by Reflection Equivariance?

**Five-line summary.** The shared-anchor ambiguity reduces exactly to one overlap parameter w ∈ [0,1] per shared anchor, with σ_reg = Q₁Q₂(w_a + w_b − 1) for the same-axis pair (numerically verified, both offset signs reproduced). J-equivariance **alone does not force C-D5**: an explicit charge-dependent equivariant scheme gives σ_reg = |Q₁|Q₂ ≠ 0 — the conjecture as literally stated is **refuted**. Adding charge-independence (homogeneity), J-equivariance forces every collar to be exactly r-antisymmetric, hence w_a = w_b = 1/2 and σ_reg = 0 **exactly at every ε** — C-D5-as-*value* is a theorem under (H1)+(H2); C-D5-as-*scheme* is forced only up to a class (scheme ↦ value is non-injective in two distinct ways). For a single shared anchor no reflection preserves the configuration; a canonical swap-reflection exists but decides the case only with an added locality axiom, yielding σ_reg = ±Q₁Q₂/2 — a half-integer extension of the crossing number. Verdict: **conditionally upgraded**, with the exact hypotheses and the exact obstruction stated in [BOX 6].

## 0. Setting (given, refereed)

σ(f,g) = ∫_{S¹} f g′ dθ on profiles mod constants; σ(f+c,g) = σ(f,g+c) = σ(f,g) by periodicity. Sharp profiles s = Q·1_{(a,b)}. E2: distinct anchors ⇒ σ = Q₁Q₂·î exactly, ramp-independent. E5: the modular reflection r of interval (a,b) is the unique orientation-reversing Möbius involution fixing a,b, r′ = −1 there; σ(f∘r, g∘r) = −σ(f,g). I use freely the elementary extension: this last identity holds for *any* orientation-reversing diffeomorphism ρ of S¹ (change of variables u = ρ(θ) reverses orientation), Möbius structure being needed only for the modular interpretation.

## 1. Regularization schemes and exact reduction to overlap parameters

**[BOX 1] (Definition: admissible smoothing and scheme.)** An *admissible smoothing* at scale ε of sharp data C = ((Q₁, I₁), (Q₂, I₂)), Iᵢ = (aᵢ, bᵢ), is a pair ηᵢ = Qᵢhᵢ with hᵢ smooth, hᵢ ≡ 1 on Iᵢ minus its ε-collars, hᵢ ≡ 0 outside Iᵢ plus its ε-collars, hᵢ monotone across each collar, and collars at *distinct* anchor points pairwise disjoint. A *regularization scheme* S assigns to each sharp configuration a family ε ↦ S_ε(C) of admissible smoothings such that σ_reg(C) := lim_{ε→0} σ(S_ε(C)) exists. Schemes with no limit (e.g. ε-oscillating collar orderings) are excluded by definition. [GAP-1: monotonicity is a genuine restriction; it is used only to bound the parameter range below, not in the equivariance theorem.]

**Reduction.** For the same-axis pair (I₁ = I₂ = (a,b)): σ(η₁,η₂) = Q₁Q₂ ∫ h₁h₂′ dθ. Since h₂′ is supported in the two collars, σ = Q₁Q₂(m_a + m_b) with local integrals m_x := ∫_{U_x} h₁h₂′ over a neighborhood U_x of collar x. Writing h = A − B in a cut coordinate (A, B monotone 0→1 steps at a, b), m_a = w_a := ∫A₁A₂′ ∈ [0,1] and m_b = w_b − 1, w_b := ∫B₁B₂′ ∈ [0,1]:

**[BOX 2] (Exact value formula, same axis.)** σ(η₁,η₂) = Q₁Q₂(w_a + w_b − 1), **exactly for every ε** (no limit needed), depending on the smoothing only through the two overlap parameters w_x = ∫(collar₁)(collar₂)′ ∈ [0,1]. Special values (all verified numerically, §4): common smoothing or any pair of collars each antisymmetric about its anchor ⇒ w_a = w_b = 1/2 ⇒ σ = 0. η₂'s collars displaced fully ccw of η₁'s (η₂ "lags" into the interval) ⇒ w_a = w_b = 1 ⇒ σ = +Q₁Q₂; fully cw ⇒ w = 0 ⇒ σ = −Q₁Q₂. The prior referee's −Q₁Q₂ is the cw ordering. For translation-related collars of a common symmetric shape with relative displacement δ, w(δ) + w(−δ) = 1 exactly (product rule), w(0) = 1/2.

So the scheme space, as seen by σ, is exactly the square (w_a, w_b) ∈ [0,1]², and σ_reg sweeps all of Q₁Q₂·[−1,1]. C-D5's midpoint convention is the point (1/2, 1/2).

## 2. J-equivariance: what it forces and what it does not

Let r be the modular reflection of the shared axis. r swaps the arcs (a,b) and (b,a), so on sharp data, mod constants: r·(Q₁, Q₂; (a,b)) = (−Q₁, −Q₂; (a,b)). Note r·C ≠ C: equivariance is a constraint *linking* the scheme's values at these two configurations, not automatically a constraint at C alone. This is the crux.

**(H2) J-equivariance:** S_ε(r·C) = S_ε(C)∘r, as profiles mod constants, for every C and ε. [GAP-2: I state equivariance at every ε, which is the strongest honest reading; a scaling-limit-only version forces the same value but weakens the scheme classification to an asymptotic statement.]

**(H1) Charge-independence:** the assigned smoothed indicators hᵢ depend only on the intervals and the profile slot i, not on (Q₁, Q₂). (Implied by requiring S to commute with scalar rescaling of each profile — natural, since sharp data is linear and σ bilinear; but it is a *separate axiom*, see [BOX 4].)

**[BOX 3] (Theorem: same-axis case.)** Assume (H1) and (H2). Then for each i, hᵢ∘r = 1 − hᵢ exactly; consequently each collar is r-antisymmetric about its anchor with hᵢ(a) = hᵢ(b) = 1/2, and w_a = w_b = 1/2 and σ(η₁,η₂) = 0 **exactly for every ε**. What is forced: (i) the *value* σ_reg = 0; (ii) the *scheme* only up to the class of r-antisymmetric collar pairs — φ₁ = φ₂ is **not** forced (offsets are forced to zero, common shape is not). The map scheme ↦ value is not injective: value 0 ⇔ w_a + w_b = 1, a strictly larger set than the equivariant class (e.g. offsets (+δ, −δ), or any common smoothing with a non-symmetric shape — both give 0 and are non-equivariant). So **C-D5-as-value is the theorem; C-D5-as-scheme is a distinguished class with the midpoint/common-smoothing scheme as one representative.**

*Proof.* By (H1), S assigns to r·C = (−Q₁, −Q₂; (a,b)) the same hᵢ as to C. (H2) then reads −Qᵢhᵢ ≡ Qᵢ(hᵢ∘r) mod constants, i.e. hᵢ∘r = cᵢ − hᵢ; evaluating deep in (b,a) (where hᵢ = 0 and r maps into (a,b) where hᵢ = 1) gives cᵢ = 1. For w_a: let U be an r-invariant neighborhood of a containing the a-collars. J := ∫_U (h₁∘r)(h₂∘r)′ dθ = −m_a by the orientation-reversing substitution; but also, using hᵢ∘r = 1 − hᵢ, J = ∫_U (1−h₁)(−h₂′) = −∫_U h₂′ + m_a = −1 + m_a. Hence m_a = 1/2. At b, ∫_U h₂′ = −1 gives m_b = −1/2. σ = Q₁Q₂(m_a + m_b) = 0. Note the proof needs neither monotonicity nor ε→0; r-antisymmetric collars exist (refereed entry 6), so the equivariant class is nonempty. ∎

**[BOX 4] (Counterexample: (H2) alone does not force C-D5 — the conjecture as stated is false.)** Drop (H1). Define S*: for the same-axis pair, use r-antisymmetric base collars, with η₂'s collars rigidly displaced by sgn(Q₁)·3ε (ccw if Q₁ > 0, cw if Q₁ < 0). Under r, displacements negate and (Q₁,Q₂) ↦ (−Q₁,−Q₂), so S*(r·C) = S*(C)∘r: **S\* is exactly J-equivariant**. Its value: σ_reg = sgn(Q₁)·Q₁Q₂ = |Q₁|Q₂ ≠ 0 (consistent with anti-equivariance of values: |−Q₁|(−Q₂) = −|Q₁|Q₂ ✓). Hence "C-D5 is the unique J-equivariant scheme" is **refuted** without a charge-independence/homogeneity hypothesis; equivariance alone constrains values only in the pattern σ_reg(r·C) = −σ_reg(C), which links C to the *different* configuration r·C and is satisfiable with nonzero diagonal. (H1) is exactly what collapses r·C onto C's scheme data. [GAP-3: one could try to replace (H1) by equivariance under a larger group; the Möbius stabilizer of the configuration (the axis's hyperbolic flow) rescales collars but preserves orderings, and does not kill S* — checked at the level of the offset sign, not exhaustively.]

## 3. Generality: shared single anchor

Take s₁ = Q₁1_{(a,b₁)}, s₂ = Q₂1_{(a,b₂)}, b₁ ≠ b₂ (impossible for distinct axes of a discrete group [others': refereed elsewhere], but well-posed for the abstract pairing). The b-collars are at distinct points (rigid, E2-type contributions); only w_a is scheme-dependent. Exact computation as in §1: if b₁ ∈ (a,b₂): σ = Q₁Q₂·w_a; if b₂ ∈ (a,b₁): σ = Q₁Q₂(w_a − 1). Both verified numerically.

*Which reflection?* No reflection preserves this configuration: the modular reflection r₁ of axis 1 fixes a, b₁ but moves b₂ (r₁·C is a different configuration — equivariance under r₁ relates two configurations and constrains neither alone). There **is** a canonical configuration-adapted reflection: the unique orientation-reversing Möbius involution ρ with ρ(a) = a, ρ(b₁) = b₂ (then ρ(b₂) = b₁ and ρ² fixes three points, hence ρ² = id; ρ′(a) = −1 since ρ′(a)² = 1 with orientation reversed). Numerically constructed and verified (involution to 3e-16, ρ′(a) = −1, σ-anti-invariance exact). But ρ·C swaps the two profiles' *roles* (mod constants: slot 1 becomes −Q₁ on (a,b₂), slot 2 becomes −Q₂ on (a,b₁)), so ρ-equivariance again links C to a different labeled configuration:

- With (H1) + label-symmetry only: ρ-equivariance demands w_a(ρ·C) = 1 − w_a(C), and label-symmetry *independently* gives w_a(ρ·C) = 1 − w_a(C) (swap antisymmetry of the overlap). The two conditions coincide: **consistency, no constraint — w_a is free. Honestly undecided at this level.**
- **(H3) Anchor locality:** the collar assigned to slot i at an anchor depends only on the germ of the sharp data there (which slots jump at that anchor and in which direction), not on the far endpoints. Then w_a(ρ·C) = w_a(C), and combined with ρ-equivariance's 1 − w_a: **w_a = 1/2 forced.** Equivalently: (H3) transports the same-axis theorem's r-antisymmetric collars (Box 3) to every shared anchor — the two routes agree.

**[BOX 5] (Half-integer extension.)** Under (H1)+(H2)+(H3), every shared anchor is resolved at w = 1/2 and contributes ±1/2: the single-shared-anchor pairing is σ_reg = ±Q₁Q₂/2 (sign = orientation of b₁ vs b₂; verified: +1/2 and −1/2 numerically, exactly at every ε), and E2 extends to σ_reg = Q₁Q₂·î with î ∈ ½ℤ, the same-axis diagonal being (+1/2) + (−1/2) = 0. The case of oppositely-oriented sharing (one interval *ends* where the other *begins*) likewise yields ±Q₁Q₂/2. Flags: [GAP-4] ρ is *not* a modular conjugation of either interval; calling ρ-equivariance "J-equivariance" is an extrapolation — the clean statement is equivariance under all configuration-adapted Möbius reflections. [GAP-5] Without (H3) the single-shared-anchor value is genuinely undecided by reflection equivariance; note also σ_reg jumps discontinuously (0 vs ±Q₁Q₂/2) as b₂ → b₁, so no continuity argument can substitute for (H3).

## 4. Numerics (grid N = 2¹⁸, quintic C² collars, analytic derivatives; Q₁ = 2, Q₂ = −3)

| Test | Result (σ/Q₁Q₂) | Expected |
|---|---|---|
| Same-axis, common symmetric smoothing | +9.7e−11 | 0 |
| η₂ collars rotated ccw / cw by 3ε | +1.000000 / −1.000000 | ±1 |
| Generic offsets: σ vs Q₁Q₂(m_a+m_b) | match to 6 d.p. (3 cases) | identity |
| Offsets (+0.8ε, −0.8ε) (non-equivariant) | −7.2e−11 | 0 (non-injectivity) |
| Common **non-symmetric** collar shape | −1.1e−11 | 0 (non-injectivity) |
| r (Möbius, fixes a,b): r′(a), r′(b) | −1.000000 | −1 |
| σ(η₁∘r, η₂∘r) + σ(η₁,η₂), offset scheme | 0 to 6 d.p. | 0 (exact identity) |
| r-image of (0.9ε, 0.3ε)-offset scheme vs (−0.9ε, −0.3ε) scheme | equal to ≤1.4e−9 at ε = 0.04…0.005 | equal (offset negation) |
| Single anchor, midpoint, both orderings | +0.500000 / −0.500000, ε-independent | ±1/2 |
| Single anchor, η₂ a-collar ±3ε | +1.000000 / −0.000000 | 1 / 0 |
| Swap reflection ρ: involution, ρ(b₁) = b₂, ρ′(a) | 3e−16, exact, −1.000000 | exists |
| σ anti-invariance under ρ | exact to 6 d.p. | −σ |

## 5. Verdict

**[BOX 6] (Verdict: C-D5 conditionally upgraded; conjecture-as-stated refuted.)**
1. **REFUTED as stated:** J-equivariance alone does *not* single out the symmetric scheme; the charge-dependent scheme S* (Box 4) is exactly J-equivariant with σ_reg = |Q₁|Q₂ ≠ 0. Exact obstruction: r maps the same-axis configuration to the charge-negated configuration, not to itself, so equivariance only links the two.
2. **UPGRADED with hypotheses (theorem, Box 3):** if the scheme is charge-independent (H1) and J-equivariant (H2), then each collar satisfies h∘r = 1 − h, forcing w_a = w_b = 1/2 and σ_reg(same axis) = 0 exactly at every ε. **Forced: the value, and the collar r-antisymmetry. Not forced: common shape φ₁ = φ₂.** C-D5-as-value is the theorem; C-D5-as-scheme is a canonical class containing the midpoint convention; scheme ↦ value is non-injective (value 0 ⇔ w_a + w_b = 1 ⊋ equivariant class).
3. **Single shared anchor:** undecided by equivariance alone (no configuration-preserving reflection; the canonical swap reflection ρ gives only a consistency identity). With anchor locality (H3) added: w = 1/2 at every shared anchor, σ_reg = ±Q₁Q₂/2, and E2's crossing number extends half-integrally (î ∈ ½ℤ).

**Recommended dictionary update:** replace "C-D5 (convention)" by "C-D5 (theorem under H1+H2 for shared axes; convention only through the choice of H3 for exotic single-shared-anchor configurations, which do not occur for discrete groups)."

---

## AMENDMENT — referee verdicts entered (2026-07-26)

*Context-free adversarial referee pass completed 2026-07-26; report verbatim in `reviews/REPORTS-phase109-CD5-referee-2026-07-26.md`. The referee rederived the formula and theorem by hand, reimplemented all numerics independently (≤10⁻⁷ agreement), and REPAIRED the counterexample rather than rejecting it. Standing AI-referee caveat applies.*

### A.1 Overall ruling — **C-D5 IS UPGRADED [refereed]**

> **C-D5 (theorem, superseding the 2026-07-24 convention).** For shared-axis configurations: under (H1) charge-independence and (H2) J-equivariance of the regularization scheme, every collar satisfies h∘r = 1 − h, forcing w_a = w_b = 1/2 and the same-axis value σ = 0 exactly at every ε. The VALUE and the collar r-antisymmetry are forced; the common shape is not (the equivariant schemes form a class containing the midpoint convention). H1 is genuinely load-bearing: the repaired charge-dependent scheme (referee's r-image-branch construction — exactly equivariant, admissible) achieves σ = |Q₁|Q₂ ≠ 0 under H2 alone. For single-shared-anchor configurations (which cannot occur for distinct axes of a discrete group): undecided by equivariance; resolved to ±Q₁Q₂/2 (î ∈ ½ℤ) only under the additional axiom (H3) anchor locality — which the referee notes subsumes H2's role for the same-axis value.

### A.2 Corrections adopted

- **C-R1 (bookkeeping):** the −1 in the value formula comes from the non-vanishing cross term ∫A₁B₂′ = 1, not from collar disjointness; stated correctly henceforth. Strengthening adopted: w(δ)+w(−δ) = 1 for arbitrary common shapes.
- **C-R2 (counterexample re-stated):** the original S* was inadmissible (3ε displacement exits the window) and only approximately equivariant (Möbius r ≠ rigid reflection; O(δ²) mismatch measured). The record's official counterexample is the referee's repaired version: negative-charge branch := r-image of the positive branch (exact equivariance by construction, verified to 10⁻¹⁷), in-window displacement, σ = sgn(Q₁)Q₁Q₂ exactly. The refutation of "H2 alone suffices" stands.
- **C-R3:** label-symmetry flagged as an axiom in the single-anchor analysis; the "+½ − ½ = 0" diagonal is exact as a per-anchor decomposition, heuristic as a b₂ → b₁ limit (discontinuity noted); Qᵢ = 0 footnote added.

### A.3 Consequence for the dictionary

The E2 registration's C-D5 clause is upgraded from convention to theorem-under-hypotheses (addendum entered in phases/phase105-D12-cross-invariant.md). Score for the phase-109 upgrade program: C-D5 fully upgraded; D-MS reduced to a binary decided by M-FRAME; C-BRIDGE reduced to faithfulness + parity-theorem + unit normalization.
