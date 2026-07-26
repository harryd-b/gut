# Phase 105 — fifth entry candidate: conjugation — antimatter as the modular mirror (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-24, continuing the phase-105 successor program. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered].** The proposed fifth entry: the action of the modular conjugation J on defects. Headline claims (pre-verdict): J acts as the orientation-reversing reflection fixing the geodesic's endpoints, JW(f)J = W(f∘r) (with the residual sign imported from free-field PCT — GAP-1, load-bearing: it decides the charge flip); the modular mirror of a charge-Q defect is a charge-(−Q) defect on the SAME geodesic, reflected to the complementary side, admissible-but-invisible per the refereed trichotomy; the transformation laws of all four prior entries close consistently (D invariant side-swapped; spin phase conjugated — by antilinearity AND independently by orientation reversal, agreeing; statistics parity invariant; D₁₂ sign-flipped via two distinct mechanisms with the same result); and the defect-plus-mirror vector is exactly the POSITIVE-CONE STANDARD-FORM PURIFICATION — J-invariant, defect on one side, charge-conjugate on the other, globally neutral yet locally un-annihilable — the thermofield-double shape, with the NOTE-1 record-tie flagged conjecture-level. Toy-PCT reading tagged; no dynamics. Goes to a context-free referee before any verdict.*

---

## The derivation, verbatim

# Conjugation Entry of the Defect Dictionary: J-Mirrors, Charge Flip, and the Standard-Form Pair

## 1. The action of the modular conjugation J

**Convention.** Line frame: ξ₋ = 0, ξ₊ = ∞, I = (0,∞), I′ = (−∞,0). The reflection is r(x) = −x: the unique orientation-reversing involution of S¹ ≅ ℝ∪{∞} fixing ξ± pointwise and exchanging I ↔ I′. (For I = (−1,1) the conjugate form is r(x) = 1/x; nothing below depends on the frame.) By Bisognano–Wichmann for the chiral net, Δ^{it} implements the dilation subgroup δ_{−2πt} fixing {ξ±}; J = J_{A(I),Ω} is **antiunitary**, J² = 1, JΩ = Ω, and JA(I)J = A(I)′ = A(I′) (Haag duality).

**Weyl action.** Write W(f) = e^{iφ(f)}, φ hermitian, ℝ-linear in f. Antiunitarity gives J e^{iφ(f)}J = e^{−iJφ(f)J}, so JW(f)J = W(f^J) is again a Weyl operator (same, not adjoint, form) with f ↦ f^J ℝ-linear. Conjugating the Weyl relation:

  JW(f)J·JW(g)J = J e^{−iσ(f,g)/2}W(f+g) J = e^{+iσ(f,g)/2}W((f+g)^J),

so J forces **anti-symplecticity**: σ(f^J,g^J) = −σ(f,g). Since r is orientation-reversing, with (g∘r)′(x) = −g′(−x):

  σ(f∘r, g∘r) = ∫ f(−x)(−g′(−x))dx = −∫ f(u)g′(u)du = −σ(f,g),

so f∘r is anti-symplectic — but so is −f∘r (the sign squares out). Likewise ‖±f∘r‖ = ‖f‖ (on the circle, (f∘r)̂_k = f̂_{−k} = conj f̂_k for real f), so ω-invariance also fails to fix the sign. The residual sign is fixed by the one-particle modular theory: continuing Δ^{it} (dilation, weight-1 covariance for the current) to t = −i/2 rotates x ↦ e^{iπ}x = −x through the analyticity domain of positive-frequency functions and produces the weight factor e^{iπ} = −1; combining with S = JΔ^{1/2} yields J j(x) J = −j(−x) = r′(x)j(r(x)) — equivalently, this is the chiral restriction of the free-field PCT operator (the 2D massless scalar satisfies Θφ(x)Θ = φ(−x), whence its derivative current is reflection-odd). Then

  Jφ(f)J = ∫f(x)(−j(−x))dx = φ(−f∘r), so JW(f)J = e^{−iφ(−f∘r)} = W(f∘r).

The two minus signs — antilinearity and the current's weight-1 parity — cancel.

**[BOX 1]  J W(f) J = W(f∘r), f^J = f∘r; σ(f^J,g^J) = −σ(f,g), ‖f^J‖ = ‖f‖.**

[GAP-1] The sign of f^J is imported from the BW/PCT identification for the free field (others' theorem) plus a weight-tracking heuristic for Δ^{1/2}; a fully self-contained Mellin-transform derivation of the one-particle J was not redone here. Both signs pass every abstract check used above; entries quadratic in Q are insensitive, but the D₁₂ law and the "antimatter = charge flip" reading do depend on it (see §5).

**Defect transformation.** (J·AdW(η)·J)(A) := JW(η)(JAJ)W(η)*J = AdW(η^J)(A), a linear automorphism, with η^J = η∘r: density (η^J)′ = −η′∘r supported in I′, and charge

  Q[η^J] = ∫_{I′}(η∘r)′ dx = η(−x)|_{x=−∞}^{0} = η(0) − η(∞) = **−Q**.

**[BOX 2]  The modular mirror of a charge-Q defect on geodesic γ is a charge-(−Q) defect on the SAME geodesic — r fixes ξ± hence the axis — with profile reflected to I′.**

**Adjudication (trichotomy).** The mirror defect is anchored at the same fixed points ξ±, so it belongs to the same geodesic's ledger; but its density lies in I′, so per the refereed trichotomy it is **admissible but invisible** to the M_γ coupling: the I-local cocycle of the mirrored profile is trivial on A(I).

## 2. Transformation laws of the refereed entries

**(a) Erasure rate.** D depends on Q² and ℓ only: D(−Q) = (−Q)²ℓ/2π = D(Q). The mirror's rate is computed by the I′-local cocycle; since J carries the modular data of (A(I),Ω) onto (A(I′),Ω) and ℓ is the same axis-length,

**[BOX 3]  D^J = Q²ℓ/2π = D — same erasure rate, on the OTHER side (I′-local, invisible from A(I)).**

**(b) Spin phase.** D_spin = ∓Q²/2 + nQ²/2 is invariant under Q → −Q (quadratic). But J is antiunitary, so any refereed phase attached to a transport/rotation cocycle is complex-conjugated: e^{iD_spin} → e^{−iD_spin}. Geometrically consistent: r reverses orientation, flipping the transport winding n → −n and the chirality sign ∓ → ±, i.e., D_spin → −D_spin. Scalar conjugation (antilinearity) and orientation reversal (geometry) give the same answer — a nontrivial consistency check. Statistics parity: (−1)^{−q} = (−1)^q — antiparticles have the same statistics. ✓

**(c) Pair pairing D₁₂ = Q₁Q₂·î(γ₁,γ₂).** Two distinct operations, carefully distinguished:

(i) **Replace defect 1 by its mirror** (J of interval I₁; defect 2 untouched). The mirror stays on γ₁ (r₁ fixes ∂I₁, hence axis 1; axis 2 is not fixed by r₁, but nothing moves it — defect 2 is unchanged). Both axes and î(γ₁,γ₂) are what they were; only Q₁ → −Q₁:

**[BOX 4a]  D₁₂(mirror-1, 2) = (−Q₁)Q₂ î = −D₁₂  (charge flip, geometry fixed).**

[GAP-2] This uses the refereed axes-and-charges-only dependence of D₁₂ extended to a profile supported in I₁′; the commutator phase e^{−iσ(η₁∘r,η₂)} was not recomputed from scratch for reflected supports.

(ii) **Conjugate the whole relation**: J(W₁W₂W₁*W₂*)J. The commutator is the scalar e^{−iσ(η₁,η₂)}; J conjugates scalars, and indeed σ(η₁^J,η₂^J) = −σ(η₁,η₂) by anti-symplecticity. Charge bookkeeping: (−Q₁)(−Q₂) = +Q₁Q₂, but both profiles are reflected and r reverses orientation, so the signed crossing flips, î → −î:

**[BOX 4b]  J-conjugation of the pair relation: D₁₂ → Q₁Q₂(−î) = −D₁₂ — same sign flip as (i), but via orientation reversal, not charge.**

## 3. The mirror pair: standard-form purification

Define the pair vector (ordering chosen so the A(I)-restriction is the prompt's defect state):

  ξ_η := W(η)* · JW(η)*J · Ω.

(a) JW(η)*J ∈ JA(I)J = A(I′) by Haag duality, so the two factors commute exactly.

(b) **J-invariance**: Jξ_η = (JW(η)*J)·W(η)*·JΩ = JW(η)*J·W(η)*·Ω = ξ_η, using antiunitarity, J² = 1, JΩ = Ω, and commutation. ✓

(c) **Restrictions.** For A ∈ A(I): ⟨ξ_η, Aξ_η⟩ = ⟨Ω, W(η)AW(η)*Ω⟩ = (ω∘AdW(η))(A) — the original defect state. For B ∈ A(I′): ⟨ξ_η, Bξ_η⟩ = ω(W(η^J)BW(η^J)*) = (ω∘AdW(η^J))(B) — the mirror defect state, charge −Q on I′.

(d) **Total charge zero, yet not locally erasable.** Q_tot = Q + (−Q) = 0 on the circle — which is precisely why ξ_η exists in the vacuum Hilbert space at all (a single charge-Q ≠ 0 profile generates a vacuum-inequivalent sector; the pair automorphism is globally neutral, hence implementable). But erasability within A(I) requires, by the refereed dichotomy, Q_tot = 0 *inside I*; here the compensating charge sits in I′. So the pair is globally neutral but locally un-annihilable. ✓ Consistent.

(e) **Identification.** ξ_η = A·JAJ·Ω with A = W(η)* ∈ A(I): this is exactly an element of the natural positive cone P^♮ = closure{AJA JΩ : A ∈ A(I)} of the standard form (A(I), H, J, P^♮).

**[BOX 5]  ξ_η ∈ P^♮ is the unique positive-cone (standard-form) vector representative of the defect state ω∘AdW(η)|_{A(I)}. It is J-invariant (KMS-symmetric), restricts to the defect on A(I) and to its charge-conjugate mirror on A(I′): the thermofield-double-shaped canonical purification — matter paired with its modular mirror.**

[FLAG, conjecture-level] The framework record's NOTE-1 (Boyle–Turok involution as modular conjugation of a constructed standard form) is the framework-scale version of exactly this structure — a record-tie, not derived here.

[GAP-3] Winding/zero-mode: for Q ≠ 0, "W(η)" on the circle is shorthand for the refereed I-local cocycle implementer (η is multivalued globally); all statements above are made at the level of AdW(η) on A(I), which needs only the density η′, plus the neutral-pair implementer for ξ_η. Formal circle-Weyl manipulation with multivalued η is not used in any load-bearing step.

## 4. CPT reading (tagged)

In this toy, tasks 1–2 establish: J = (reflection r fixing the axis) × (charge conjugation Q → −Q) × (antilinearity) — a working realization of PCT for defects. The general PCT theorem for Möbius-covariant/chiral nets from modular covariance is established elsewhere (Bisognano–Wichmann; Borchers; Guido–Longo) — attributed, not re-proved. Not included: there is no time and no dynamics here — the "T" is the antilinearity of J, not time-reversal of any evolution.

## 5. Honest limits

- **Theorems in the toy** (given BW + Haag duality): anti-symplecticity of f ↦ f^J; JA(I)J = A(I′); Boxes 2–5 modulo the flags; J-invariance and positive-cone membership of ξ_η (Tomita–Takesaki standard-form facts, exact).
- **Convention-dependent**: the sign in f^J = ±f∘r ([GAP-1]). Reflection-odd current (our derivation) gives f^J = f∘r, Q → −Q; the opposite parity convention would give f^J = −f∘r, Q → +Q, killing the antimatter reading and flipping Box 4a while leaving D, D_spin-magnitude, and statistics untouched. The modular J is unique, so only one convention is correct; our identification rests on the free-field PCT import.
- **No dynamics**: "annihilation," "erasure," and "spin" are cocycle/ledger statements, not scattering.
- **Visibility**: the mirror defect is invisible to M_γ's ledger (density in I′) — "antimatter" here is a statement about the global algebra and the standard form, not a second visible particle.
- **Zero modes**: all Q ≠ 0 statements live at the automorphism/cocycle level ([GAP-3]).

## Five-line summary

1. J acts as the orientation-reversing reflection r fixing the axis endpoints; JW(f)J = W(f∘r), with antilinearity and current parity signs cancelling ([GAP-1] on the residual sign).
2. The modular mirror of a charge-Q defect is a charge-(−Q) defect on the same geodesic, reflected to I′ — admissible but invisible per the trichotomy.
3. Entry laws: D invariant (side-swapped); spin phase conjugates, e^{iD_spin} → e^{−iD_spin}, consistently by antilinearity or orientation flip; statistics invariant; D₁₂ → −D₁₂ both for one-sided mirroring (charge) and full conjugation (orientation) — distinct mechanisms, same sign.
4. ξ_η = W(η)*JW(η)*JΩ is the J-invariant positive-cone purification: defect on A(I), antimirror on A(I′), globally neutral yet locally un-annihilable — the thermofield-double shape; NOTE-1 record-tie flagged as conjecture.
5. This is toy-PCT (reflection × charge conjugation × antilinearity) with no time and no dynamics; the general chiral PCT theorem is others' and attributed.
