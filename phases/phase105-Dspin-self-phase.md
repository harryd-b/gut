# Phase 105 — third entry candidate: D_spin = ∓Q²/2 + n·Q²/2 — the transport holonomy (spin/statistics) of a charged defect (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-24, continuing the phase-105 successor program. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered].** The proposed third entry of the data dictionary: the self-phase of a single defect, defined as the holonomy of transporting one anchor once around the circle. Headline claims (pre-verdict): the holonomy is EXACT — Φ = −Q²/2 + πc_ρQ²/ε — with the finite part universal (one crossing event, any ramp shape, any ε) and the divergent part identified as the framing/self-energy counterterm; renormalized D_spin = ∓Q²/2 + n·Q²/2 (n the framing integer); the spin–statistics identity holds IN-MODEL by crossing counting (1 crossing = spin = exchange, 2 crossings = monodromy = spin²); calibration |D_spin|/2π = q²/2 = h reproduces the chiral-boson conformal weight exactly under the already-fixed conversion Q = q√(2π), with zero remaining freedom; and on the charge lattice the exchange phase is (−1)^q — odd charge = fermion, even = boson — the ℤ/2 statistics grading. The same-axis regularization ambiguity of the D₁₂ referee (C-D5) is hereby reinterpreted: it is the framing dependence, a defining feature of spin for extended objects, made explicit rather than hidden. Arf and Bennequin readings flagged conjecture-only. Goes to a context-free referee before any verdict.*

---

## The derivation, verbatim

# SPAN-2: The Self-Phase (Transport Holonomy) of a Charged Defect

**Conventions.** S¹ = ℝ/2πℤ, ccw orientation; W(f)W(g) = e^{−iσ(f,g)/2}W(f+g), σ(f,g) = ∫ f g′ dx (x = spatial angle); ‖f‖² = 2πΣ_{k≥1} k|f̂_k|². Constants are **null**: σ(c,f) = 0 and ‖c‖ = 0, so W(c) is represented trivially in the vacuum GNS representation (this matters below). Ramp shape: ρ smooth, ρ(s)=0 for s≤0, ρ(s)=1 for s≥1; define c_ρ := ∫ ρ′(s)² ds > 0.

---

## 1. The transport holonomy

**The family.** η_θ = Q·(smoothed indicator of the ccw arc (m(θ), b)), m(θ) = a+θ, both ramps of fixed width ε. Concretely, near the moving anchor η_θ(x) = Q ρ((x−m)/ε) (rising ccw), near b it falls via −Qρ((x−b)/ε); through the crossing we use the **rigid superposition prescription**: the profile is the continuous sum of the two ramp steps at all θ (the symmetric/same-axis convention of the refereed record). With this prescription,

∂_θ η_θ(x) = −(Q/ε) ρ′((x−m(θ))/ε)  for **all** θ (a smooth bump, finite ‖·‖ — legitimate Weyl argument),

including through the crossing.

**Zero-mode bookkeeping.** Integrating: ∮ ∂_θη_θ dθ = −Q·**1** (constant). So the loop closes only modulo the null constant: η_{2π} = η_0 − Q·**1**. Continuity through the crossing forces this: just after m passes b the profile is 0 with a dip −Q on (b,m), i.e. the original plateau **minus the constant Q**. Since W(−Q·**1**) = 𝟙 in this representation, the transport operator is a pure phase.

**Product formula.** With T = lim W(Δ_N)⋯W(Δ_1), Δ_j = η_{θ_j} − η_{θ_{j−1}}, induction on W(f)W(g) = e^{−iσ(f,g)/2}W(f+g) gives T = exp(−(i/2)Σ_k σ(Δ_k, η_{θ_{k−1}} − η_0)) W(η_{2π}−η_0), and the η_0-term dies because σ(ΣΔ, η_0) = σ(−Q·**1**, η_0) = 0. Hence

**T = e^{iΦ}·𝟙,  Φ = ½ ∮₀^{2π} σ(η_θ, ∂_θη_θ) dθ**  (the symplectic area of the loop).

[GAP: the interchange of partition refinement with the phase sum is a standard Trotter-type estimate for norm-continuous symplectic paths with ∮‖∂_θη‖² dθ < ∞ (finite here for ε > 0); not spelled out.]

**Evaluation.** σ(η, ∂_θη) = −∫ η′ ∂_θη dx = (Q/ε) ∫ η′(x) ρ′((x−m)/ε) dx, and η′ = (Q/ε)ρ′((x−m)/ε) − (Q/ε)ρ′((x−b)/ε). Two pieces:

**(i) Generic transport (self term).** (Q²/ε²)∫ρ′((x−m)/ε)² dx = **Q² c_ρ/ε** — a θ-independent (geometric, constant-rate) contribution. It does **not** cancel and is not proportional to arc fractions: it is a pure translation rate of the moving ramp, independent of the plateau it sweeps over. Over the full loop: ½·2π·Q²c_ρ/ε = **π c_ρ Q²/ε**. This diverges as ε→0 and depends on the ramp shape through c_ρ: it is the **framing/self-energy term** (the writhe-like piece).

**(ii) Crossing event.** Cross term −(Q²/ε) G((m−b)/ε), G(t) := ∫ρ′(s)ρ′(s−t)ds ≥ 0. As θ runs over the loop, m passes b exactly once; substituting t = (m−b)/ε:

½ ∮ [−(Q²/ε) G] dθ = −½ Q² ∫_ℝ G(t) dt = **−Q²/2**,

because ∫G = (∫ρ′)² = 1 **for any ramp shape and any ε** — the crossing phase is universal under rigid transport (this is the transport-integrated realization of the "symmetric convention = Q²/2 per shared anchor" refereed fact). Reversing the transport orientation inverts the holonomy: −Q²/2 → +Q²/2.

**(iii) Framing.** The total raw holonomy is exact (no O(ε) remainders):

**Φ = −Q²/2 + π c_ρ Q²/ε.**

The divergent piece equals the holonomy Φ_free of the identical moving ramp transported around a circle with the spectator (fixed-anchor) charge deleted; it is the natural counterterm. Renormalized invariant: D_spin := Φ − Φ_free. Residual prescription dependence sits entirely at the crossing: rigid/symmetric passage gives −Q²/2; offset passings (resolving the shared-anchor moment by displaced smoothings, per the refereed same-axis dichotomy giving ±Q² there) shift the crossing contribution by integer multiples of Q²/2. [GAP: only shifts n ∈ {0, ±1} are exhibited via the refereed offset conventions; general n would require multiply-wound passages, not computed.]

**D_spin = ∓Q²/2 + n·Q²/2, n ∈ ℤ (framing integer; n = 0 for rigid transport), ∓ = transport orientation; raw counterterm Φ_free = πc_ρQ²/ε.**

---

## 2. Spin–statistics consistency

Refereed: two crossing-axis Q-defects have commutator/monodromy phase e^{−iσ(η₁,η₂)} = e^{∓iQ²}; exchange = half monodromy = e^{∓iQ²/2}.

My task-1 result: spin phase e^{iD_spin} = e^{∓iQ²/2} (n = 0). So

**spin phase = e^{∓iQ²/2} = exchange phase; monodromy = (spin phase)² = e^{∓iQ²}.**

**Adjudication of the loop normalization.** One might worry the full-circle transport is the *double* of the spin. It is not, and the model shows why: the topological content is carried entirely by **crossing events** (each anchor-passage contributes ∓Q²/2). The single-anchor full loop has exactly **one** self-crossing → ∓Q²/2 = exchange-level = spin. By contrast: (a) *rigid rotation* of the whole defect (both anchors moving together, η_θ(x) = η_0(x−θ)) has ∂_θη = −η′, giving σ(η,∂_θη) = ∫(η′)² = 2Q²c_ρ/ε — **zero crossings, pure framing, no universal phase**; (b) winding an anchor past *both* anchors of a second defect accumulates two crossings → Q², the monodromy. So the hierarchy "1 crossing = spin = exchange, 2 crossings = monodromy" is internally consistent, and the spin–statistics identity is **derived-in-this-model** for the coherent implementers. [GAP: the identification "single-anchor loop = 2π self-rotation" is adjudicated by this crossing-count consistency and the Section 3 calibration, not by an independent rotation-covariance (L₀) argument.]

---

## 3. Calibration against the chiral boson (established, others')

Established elsewhere: the charge-q vertex operator has h = q²/2, rotation eigenvalue e^{2πih} = e^{iπq²}, exchange phase e^{iπq²}. With the refereed level-1 conversion **Q = q√(2π)**:

D_spin = ∓Q²/2 = ∓πq², i.e.

**e^{iD_spin} = e^{∓iπq²}; |D_spin|/2π = q²/2 = h.**

The magnitude reproduces the conformal weight **exactly**: the holonomy per full transport is 2πh. The comparison with e^{2πih} = e^{+iπq²} is **convention-shifted** in general (the sign is the orientation of transport, tied to which crossing sign is declared î = +1), but **exact on the charge lattice**: for q ∈ ℤ, e^{∓iπq²} = (−1)^{q²} = e^{+iπq²}, so the match is orientation-independent exactly where the model is quantized. A one-unit framing shift n → n+1 multiplies the spin phase by e^{iQ²/2} = e^{iπq²} = e^{2πih}, the twist — the correct behavior of framing on a spin-h object.

---

## 4. The statistics bit

On the lattice Q = q√(2π), q ∈ ℤ:

**exchange phase = e^{iπq²} = (−1)^{q²} = (−1)^q: q odd ⟹ fermion, q even ⟹ boson**

(using q² ≡ q mod 2). This is the ℤ/2 statistics grading of the dictionary, invariant under framing shifts mod 2·(Q²/2) and under orientation reversal. Two flagged connections, **conjecture-level, NOT derived here**: (1) the record's Arf-graded census — the conjecture that this (−1)^q grading is the image of an Arf invariant on the quadratic refinement underlying the defect pairing — is untested by this computation; (2) the bulk reading of the framing integer n as a Bennequin/contact self-linking number of the defect's ribbon in a 3d completion is an attractive gloss with no derivation in this model.

---

## 5. Honest limits

- **Folium scope.** Our defect states W(η)Ω are **vacuum-folium coherent states** (η ∈ H^{1/2} thanks to smoothing), not genuine charged sectors; the L₀-spectrum statement h = q²/2 is a sector-theoretic result (established, others'). What this derivation supplies is strictly the **transport-holonomy realization** of the same phase inside the coherent toy, with the framing counterterm πc_ρQ²/ε and the prescription ambiguity n·Q²/2 made explicit rather than hidden in a normal-ordering convention.
- **Zero mode.** The loop closes only modulo the constant −Q·**1**, which is null here. In a compactified model where the zero mode is dynamical, W(−Q·**1**) is a nontrivial zero-mode translation and the holonomy would act on it; flagged, not analyzed.
- **Fixed-anchor location.** Confirmed irrelevant: the computation used only σ, the translation-invariance of the ramp overlap integrals, and ∫G = 1. No group element acts and no γ fixed point enters; b generic vs special changes nothing. ✓

---

## Summary (5 lines)

1. The full-circle single-anchor transport is a scalar: Φ = ½∮σ(η_θ, ∂_θη_θ)dθ = −Q²/2 + πc_ρQ²/ε, exactly.
2. Renormalized: D_spin = ∓Q²/2 + n·Q²/2; the ∓Q²/2 is universal (shape/ε-independent, one crossing), n is the framing integer (rigid = 0).
3. Spin = exchange = e^{∓iQ²/2}, monodromy = spin² — spin–statistics holds in-model; the single-crossing count adjudicates the loop as the 2π self-rotation.
4. Calibration Q = q√(2π): |D_spin|/2π = q²/2 = h exactly; on the lattice e^{iD_spin} = (−1)^q — odd q fermion, even q boson (ℤ/2 grading); Arf and Bennequin readings flagged as conjecture-only.
5. Scope: a coherent-state (vacuum-folium) realization of the sector phase, with framing dependence explicit; fixed-anchor position immaterial.
