# Phase 105 — fifth entry: conjugation — antimatter as the modular mirror (REFEREED 2026-07-26; core CONFIRMED; Box 4a demoted to open lemma — see Amendment)

*Working session, 2026-07-24, continuing the phase-105 successor program. **Status: [refereed 2026-07-26 — core CONFIRMED with repairs; GAP-1 CLOSED (J flips charge); Box 4a UNPROVEN, demoted to the open lemma L-MIRROR; Box 5 repaired to the positive-cone definition. See Amendment §6.]** The proposed fifth entry: the action of the modular conjugation J on defects. Headline claims (pre-verdict): J acts as the orientation-reversing reflection fixing the geodesic's endpoints, JW(f)J = W(f∘r) (with the residual sign imported from free-field PCT — GAP-1, load-bearing: it decides the charge flip); the modular mirror of a charge-Q defect is a charge-(−Q) defect on the SAME geodesic, reflected to the complementary side, admissible-but-invisible per the refereed trichotomy; the transformation laws of all four prior entries close consistently (D invariant side-swapped; spin phase conjugated — by antilinearity AND independently by orientation reversal, agreeing; statistics parity invariant; D₁₂ sign-flipped via two distinct mechanisms with the same result); and the defect-plus-mirror vector is exactly the POSITIVE-CONE STANDARD-FORM PURIFICATION — J-invariant, defect on one side, charge-conjugate on the other, globally neutral yet locally un-annihilable — the thermofield-double shape, with the NOTE-1 record-tie flagged conjecture-level. Toy-PCT reading tagged; no dynamics. Goes to a context-free referee before any verdict.*

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

## Five-line summary (pre-verdict; superseded where the Amendment says so)

1. J acts as the orientation-reversing reflection r fixing the axis endpoints; JW(f)J = W(f∘r), with antilinearity and current parity signs cancelling ([GAP-1] on the residual sign).
2. The modular mirror of a charge-Q defect is a charge-(−Q) defect on the same geodesic, reflected to I′ — admissible but invisible per the trichotomy.
3. Entry laws: D invariant (side-swapped); spin phase conjugates, e^{iD_spin} → e^{−iD_spin}, consistently by antilinearity or orientation flip; statistics invariant; D₁₂ → −D₁₂ both for one-sided mirroring (charge) and full conjugation (orientation) — distinct mechanisms, same sign. *(Amendment: the one-sided claim is UNPROVEN — see §6.3.)*
4. ξ_η = W(η)*JW(η)*JΩ is the J-invariant positive-cone purification: defect on A(I), antimirror on A(I′), globally neutral yet locally un-annihilable — the thermofield-double shape; NOTE-1 record-tie flagged as conjecture. *(Amendment: formula literal only at Q = 0 — see §6.4.)*
5. This is toy-PCT (reflection × charge conjugation × antilinearity) with no time and no dynamics; the general chiral PCT theorem is others' and attributed.

---

## 6. AMENDMENT — referee verdicts entered (2026-07-26)

*Context-free adversarial referee pass completed 2026-07-26 (first dispatch 2026-07-24 was stopped mid-flight by session compaction and re-run with the same brief; report preserved verbatim in `reviews/REPORTS-phase105-Dconj-referee-2026-07-26.md`). The referee ran numerics for the Box 4a mandate (2^18-point grid, smoothed ramps, three branch conventions, six configurations), with the exact anti-symplecticity identity confirmed to machine precision as a code check. Verdicts and adopted corrections follow. Standing AI-referee caveat applies.*

### 6.1 Overall ruling

**The fifth entry ENTERS the dictionary: the conjugation entry is CONFIRMED in its core** — J is the orientation-reversing reflection fixing the axis, **it genuinely flips charge** (GAP-1 closed, see 6.2), the mirror of a charge-Q defect is a charge-(−Q) defect on the same geodesic reflected to I′ (admissible-but-invisible per the trichotomy), D and the statistics parity are invariant, the spin phase conjugates (both routes agree, exactly), full J-conjugation flips D₁₂ (exact theorem), and the mirror-pair purification stands in repaired form (6.4). **One headline claim is demoted:** the one-sided mirroring law D₁₂ → −D₁₂ (Box 4a) is UNPROVEN and is re-registered as the open lemma L-MIRROR (6.3), exported to the entry-6 arena build.

### 6.2 GAP-1 CLOSED [refereed]: f^J = +f∘r — the modular mirror flips charge; "antimatter" is earned

The referee closed the sign convention-free, replacing the free-field PCT import: Guido–Longo (modular covariance ⟹ the conjugate DHR sector is the J-reflected one, j∘ρ∘j) plus BMT sector composition (ρ_q∘ρ_{q′} ≃ ρ_{q+q′}, pairwise inequivalent, so the conjugate of charge q is −q) forces f^J = +f∘r: the alternative sign would make the J-reflected sector have charge +Q, contradicting conjugacy for Q ≠ 0. The imports are established theorems of the same standing as the BW input the entry already assumes. The derivation's weight-tracking argument is ruled internally consistent but only a heuristic; the sector argument is what closes the gap. Residual caveat noted for the record: the derivation tacitly assumed f^J ∈ {±f∘r}; the sector argument fixes the action on charge classes regardless, so the conclusion is unaffected. **Boxes 1 and 2 [refereed]. Charge conjugation is now a theorem of the toy, not a convention.**

### 6.3 Correction C-Dconj-1 — Box 4a demoted to UNPROVEN; open lemma L-MIRROR registered

The pre-flagged double-flip risk is real. The referee's direct computation of σ(η₁∘r₁, η₂) (smoothed ramps, three branch-charge conventions, crossing/nested/disjoint configurations) shows the raw commutator phase does **not** robustly flip under mirroring one defect: in the reflection-symmetric configuration it flips cleanly, but in convention (i) it is unchanged (0 → 0 — the two flips cancel), and in generic position it is not even ±σ (e.g. −1/4 → +3/4). The exact identity that does hold is σ(η₁∘r₁, η₂) = −σ(η₁, η₂∘r₁), which reduces to the claimed flip only when r₁ maps the configuration to an equivalent one. What survives as theorem: **mirroring BOTH defects flips D₁₂ (Box 4b [refereed], machine-precision numerics).** What is open:

> **L-MIRROR (open lemma).** Does the refereed E2 invariant D₁₂ = Q₁Q₂·î — defined through the C-D5 canonicalization — extend to profiles supported on the reflected side I₁′ with î unchanged? If yes, Box 4a's law D₁₂(mirror-1, 2) = −D₁₂ follows formally; if no, the one-sided law must be restated. The referee could not settle this without E2's exact bookkeeping (not transmitted in the context-free brief), and the raw σ of concrete profiles is genuinely not axes-and-charges-only.

**Export:** L-MIRROR is added to the entry-6 (joint two-geodesic arena) mandate, where the C-D5 bookkeeping will be on the table and D₁₂ is being re-derived internally anyway. GAP-2 is hereby ruled a real gap, not a formality; §5's classification of Box 4a among "theorems in the toy" is retracted.

### 6.4 Correction C-Dconj-2 — Box 5 repaired: the positive-cone definition; explicit formula is Q = 0 only

For Q ≠ 0 the defect automorphism α_η is **outer** on A(I) (the winding step has divergent H^{1/2} norm — no implementer exists in A(I)), so W(η)* ∉ A(I) and the literal formula ξ_η = A·JAJ·Ω with A = W(η)* ∈ A(I) is false for Q ≠ 0; GAP-3's gloss does not rescue it (the neutral-pair implementer does not factor through A(I)). **Repair (adopted):** define ξ_η as the unique natural-cone P^♮ representative of the normal state ω∘α_η|_{A(I)}. Every claimed property then survives and was verified by the referee: J-invariance (cone vectors are J-fixed), the A(I)-restriction is the defect state with the claimed ordering (AdW(η), not AdW(η)*), the A(I′)-restriction is the charge-(−Q) mirror state, uniqueness is Haagerup's theorem, and the global-neutrality/local-non-erasability discussion is consistent with E4. At Q = 0 the explicit formula is exactly right. The thermofield-double reading is ruled fair. **Box 5 [refereed, as repaired].** Pleasing consistency note from the report: the very outerness that breaks the naive formula is *why E1's erasure rate D > 0 is nontrivial* — the same divergence powers both.

### 6.5 Correction C-Dconj-3 — statistics parity statement tightened

"(−1)^{−q} = (−1)^q" is literal only for integer q. For anyonic q the correct statement: the statistics phase e^{iπq} conjugates to e^{−iπq}, which is the phase of charge −q — antiparticle statistics still match. Adopted.

### 6.6 Verdict table

| Item | Verdict |
|---|---|
| Box 1 (JW(f)J = W(f∘r); anti-symplecticity; isometry) | **CORRECT [refereed]**, GAP-1 **CLOSED** (6.2) |
| Box 2 (mirror = charge −Q, same geodesic, side I′) + trichotomy adjudication | **CORRECT [refereed]** |
| Box 3 (D invariant, side-swapped) | **CORRECT [refereed]** (given E1) |
| §2(b) (spin conjugation; two routes agree; statistics invariant) | **CORRECT [refereed]** (C-Dconj-3 tightening) |
| Box 4b (full conjugation: D₁₂ → −D₁₂) | **CORRECT [refereed]** — exact theorem, machine-precision numerics |
| Box 4a (one-sided mirroring: D₁₂ → −D₁₂) | **UNPROVEN** — demoted to open lemma **L-MIRROR** (6.3), exported to entry 6 |
| Box 5 (mirror-pair positive-cone purification) | **CORRECT WITH REPAIR [refereed, as repaired]** (6.4) |
| §4 CPT reading | **CORRECT** as tagged |
| §5 honest limits | **CORRECT WITH REPAIR** (Box 4a misclassification retracted; GAP-3 understatement noted) |

### 6.7 Dictionary status after this entry

Five entries refereed and standing: **D** (I-local erasure rate, Q²ℓ/2π) · **D₁₂** (crossing pairing, Q₁Q₂î) · **D_spin** (D-MS transport phase; statistics (−1)^q) · **D_fus** (totals-only fusion; binding = polarization; annihilation ⟺ Q_tot = 0 in A(I)) · **Dconj** (J-mirror: charge flips [refereed], same axis, reflected side, invisible; canonical purification pairs matter with its modular mirror). Open exports now standing: JOIN-4a″ (completeness), L-MIRROR (one-sided mirror law), C-F3 (branch–crossing sign correlation), KNOT-Q (geometry bridge), JOIN-4b/K-DATA (standing falsifier). Next per the adopted plan: entry 6, the joint two-geodesic arena, which inherits L-MIRROR and the internal re-derivation of D₁₂ as twin consistency mandates.
