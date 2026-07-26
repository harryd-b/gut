# Phase 105 — SPAN-2 candidate: the two-defect cross-invariant D₁₂ = Q₁Q₂·î(γ₁,γ₂) (derivation record; referee pass pending; verdicts NOT entered)

*Working session, 2026-07-24, continuing the phase-105 successor program. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered].** The proposed second entry of the data dictionary: the mutual invariant of two charged defects anchored on two geodesics. Headline claims (pre-verdict): the cross-pairing is EXACTLY topological — σ(η₁,η₂) = Q₁Q₂ × the signed crossing number of the axes, attained (not approached) for ramp-disjoint profiles; operationally it is the order-of-creation commutator phase on implementers; and a triple equivalence ties it to the refereed locality theorem: axes cross ⟺ each defect breaks the other's single-geodesic ledger ⟺ nonzero pairing. Structural note flagged by the derivation itself: the diagonal entry D = Q²ℓ/2π is METRIC (carries length) while D₁₂ is TOPOLOGICAL (carries only crossing) — the dictionary has two entries of different kind, not one quadratic form. Attribution discipline: the phase is standard chiral-boson mutual statistics (BMT/vertex-operator sectors — established, others'); claimed novelty resides only in the geodesic-axis indexation and the match to the refereed admissibility trichotomy. No dynamics, no force law, no scattering is claimed. Goes to a context-free referee before any verdict.*

---

## The derivation, verbatim

# The Two-Defect Cross-Invariant D₁₂

## Notation

S¹ = ℝ/2πℤ, counterclockwise orientation; σ(f,g) = ∫_{S¹} f g′ dθ. For each hyperbolic γᵢ write aᵢ = ξᵢ₋ (repelling), bᵢ = ξᵢ₊ (attracting); the ordered pair (aᵢ, bᵢ) orients the axis. Sharp profile: sᵢ = Qᵢ·1_{Pᵢ}, where Pᵢ = (aᵢ, bᵢ) is the ccw plateau arc; distributionally sᵢ′ = Qᵢ(δ_{aᵢ} − δ_{bᵢ}). Adding a constant to either argument leaves σ unchanged (the other's jumps sum to zero), so the choice of base value 0 is immaterial. In a discrete torsion-free Fuchsian group, two hyperbolics sharing exactly one fixed point force non-discreteness, and sharing both means a common axis (powers of a common primitive); so for γ₁, γ₂ with distinct axes the four anchors are pairwise distinct — the pairings below never evaluate a step at its own jump.

---

## Task 1. The cross-pairing

**Lemma 1 (jump formula).** If η₁ is of bounded variation and continuous at every atom of dη₂ (η₂ BV), then

σ(η₁,η₂) = ∫ η₁ dη₂ = Σ_{y: Δη₂(y)≠0} η₁(y)·Δη₂(y) + ∫ η₁ dη₂^{cont}.

In the sharp limit dη₂ is purely atomic and the second term vanishes. (Standard Stieltjes decomposition; the continuity hypothesis holds by anchor distinctness.)

**Proposition 1 (sharp evaluation).**

σ(s₁,s₂) = Q₂[s₁(a₂) − s₁(b₂)] = Q₁Q₂[1_{P₁}(a₂) − 1_{P₁}(b₂)].

*(a) Interlaced* (axes cross): exactly one anchor of γ₂ lies in P₁, so σ(s₁,s₂) = ±Q₁Q₂. Explicitly, cyclic order (a₁, a₂, b₁, b₂) gives +Q₁Q₂; cyclic order (a₁, b₂, b₁, a₂) gives −Q₁Q₂. The sign is the signed crossing number î(γ₁,γ₂) ∈ {0, ±1} of the oriented chords (convention: î = +1 for cyclic order (a₁,a₂,b₁,b₂)).

*(b) Not interlaced:* both anchors of γ₂ lie in P₁ (giving Q₁Q₂ − Q₁Q₂ = 0) or both in its complement (giving 0 − 0 = 0). Either way σ = 0.

**Smooth case — honest split.** For general smooth η₁, η₂, σ(η₁,η₂) is **not** topological: it depends on the profiles. The correct statement:

**Theorem 1 (topological content, with error control).** Suppose ηᵢ is smooth and periodic with ηᵢ′ supported in Uᵢ(ε), the ε-neighborhoods of {aᵢ, bᵢ}, transporting charge +Qᵢ across the aᵢ-ramp and −Qᵢ across the bᵢ-ramp, constant elsewhere. Let δ = minimal cyclic distance among the four anchors. Then for **every** ε < δ/2 (so U₁ ∩ U₂ = ∅), **exactly, with zero error**:

**σ(η₁,η₂) = Q₁Q₂·î(γ₁,γ₂), î ∈ {0,±1} the signed crossing number.**

*Proof.* On supp η₂′, η₁ is locally constant at its plateau values; each ramp of η₂ contributes (value of η₁ there)·(charge transported), reproducing Proposition 1 verbatim. ∎

The limit is therefore **attained**, not merely approached: σ is locally constant on the class of ramp-disjoint profiles under all deformations preserving charges and interlacing. The topological part of σ is Q₁Q₂î; the profile-dependent part is **exactly the ramp-overlap contribution**, identically zero when supp η₁′ ∩ supp η₂′ = ∅. For profiles whose derivatives are merely concentrated (not supported) near the anchors, with tail masses mᵢ(ε) = ∫_{S¹∖Uᵢ(ε)}|ηᵢ′| dθ, a Stieltjes bookkeeping estimate using |σ(f,g)| ≤ min(‖f‖_∞ Var g, Var f ‖g‖_∞) gives

|σ(η₁,η₂) − Q₁Q₂î| ≤ 2(m₁‖η₂′‖_{L¹} + m₂‖η₁′‖_{L¹}) → 0 as ε → 0

(constant not optimized; the estimate is elementary). So the cleanest correct claim is: **σ itself, evaluated in the distinguished ramp-disjoint class, is the invariant** — no holonomy/difference construction is needed, because disjointness of ramps kills all regularization dependence exactly. No [GAP] in Task 1.

---

## Task 2. Operational meaning

**(a) Mutual phase.** From the Weyl relation W(f)W(g) = e^{−iσ(f,g)/2}W(f+g) applied both ways,

**W(η₁)W(η₂) = e^{−iσ(η₁,η₂)}·W(η₂)W(η₁); the commutator W₁W₂W₁⁻¹W₂⁻¹ = e^{−iσ(η₁,η₂)}·1.**

This is the order-of-application phase for the two defect creations, and (as a commutator) is invariant under phase redefinitions Wᵢ → λᵢWᵢ. By Theorem 1, in the ramp-disjoint class: **disjoint axes ⟹ the creations commute exactly; crossing axes ⟹ they commute up to e^{∓iQ₁Q₂}**. Two remarks for honesty: (i) the sharp steps sᵢ have divergent one-particle norm, so W(sᵢ) does not exist in the vacuum representation — but the phase depends only on σ, which stabilizes at ε < δ/2, so the statement holds for every admissible smooth pair and is limit-stable; (ii) the automorphisms Ad W(ηᵢ) always commute (phases cancel in Ad) — the mutual phase lives at the level of **implementers**, i.e., it is a 2-cocycle/mutual-statistics datum, exactly where anyonic phases live.

**(b) Consistency with the refereed locality theorem.**

*Disjoint axes:* both anchors of η₂ lie in the open complementary arc I₁′ (openness by anchor distinctness), so by the refereed trichotomy η₂ is admissible-but-**invisible** to M_{γ₁}, and symmetrically. The cross-pairing vanishes — invisibility matches zero mutual phase. ✔

*Crossing axes:* interlacing means exactly one anchor of η₂ lies in the **open** arc I₁, so by the trichotomy the combined state is **inadmissible** for the arena M_{γ₁}; by symmetry of interlacing, likewise inadmissible for M_{γ₂}. (Interlacing is symmetric, so mutual visibility can never be one-sided here.) And σ = ±Q₁Q₂ ≠ 0. ✔

**Theorem 2 (triple equivalence).** For Q₁Q₂ ≠ 0, distinct axes, anchors at fixed points, ramp-disjoint profiles, the following are equivalent:

**(i) axes cross ⟺ (ii) each defect is inadmissible for the other's arena ⟺ (iii) σ(η₁,η₂) ≠ 0.**

Status of each leg: (i)⟺(ii) is the refereed trichotomy plus the interlacing dictionary (given); (i)⟺(iii) is Theorem 1 (proved above). Two precision caveats. First, the equivalence holds for **σ**, not for the exponentiated phase: if Q₁Q₂ ∈ 2πℤ the phase e^{−iσ} trivializes even though the axes cross — "nonzero mutual phase" in the slogan must mean σ ∉ 2πℤ, generic in the charges. Second, "single-ledger breakdown" here means precisely *inadmissibility in each single-geodesic arena*; any stronger reading (obstruction to a joint two-geodesic ledger) presupposes a two-arena theory that has not been constructed — that interpretation is [GAP].

---

## Task 3. The dictionary entry

**D₁₂ = Q₁Q₂·î(γ₁,γ₂) = σ(η₁,η₂)|_{ramp-disjoint}; |D₁₂| = Q₁Q₂·ι(γ₁,γ₂), ι ∈ {0,1}.**

**Normalization fixed and stated:** σ(f,g) = ∫fg′dθ as in the refereed setting; Qᵢ = plateau height; axis orientation aᵢ → bᵢ by γᵢ's translation direction; î = +1 for cyclic order (a₁, a₂, b₁, b₂). Monodromy phase: e^{−iD₁₂} per Theorem 2's boxed commutator.

**Sanity checks.**
- *Antisymmetry resolved:* σ is antisymmetric and î is antisymmetric under 1↔2 (signed intersection of oriented curves on an oriented surface), while Q₁Q₂ and ι are symmetric. So: the **signed** entry D₁₂ = −D₂₁ (consistent); the **unsigned** magnitude Q₁Q₂ι is symmetric; the **phase** e^{−iσ(η₁,η₂)} for order (1 then 2 vs 2 then 1) inverts under swap — what is symmetric is |D₁₂| and the *set* {phase, phase⁻¹}; what is antisymmetric is σ, î, and the exponent.
- *Charge vanishing:* Qᵢ = 0 ⟹ D₁₂ = 0. ✔
- *Bilinearity:* σ is bilinear and the profile scales linearly in Q, so D₁₂ is bilinear in (Q₁, Q₂). ✔
- *Smoothing independence:* exact for all ε < δ/2 (Theorem 1). ✔
- *Diagonal consistency:* same axis ⟹ ι = 0 and σ(η,η) = 0; the diagonal dictionary entry remains the refereed D = Q²ℓ/2π. Structural note: the diagonal entry is **metric** (carries the length ℓ) while the off-diagonal entry is **topological** (no length) — so Q₁Q₂ι is *not* the polarization of Q²ℓ/2π; the dictionary has two entries of different kind, not one quadratic form.

---

## Task 4. Known-physics calibration [established — others' work; recorded for attribution discipline]

This is the standard mutual-statistics (half-monodromy/braiding) phase of charged sectors of the chiral boson / U(1) current algebra: Buchholz–Mack–Todorov sectors, vertex-operator charges, with mutual monodromy e^{2πiq₁q₂} at level 1 and e^{2πiq₁q₂/k}-type anyonic phases in compactified/lattice extensions. In our normalization (σ = ∫fg′dθ, Q = plateau height) the phase per signed crossing is e^{∓iQ₁Q₂}; this matches the standard convention under the rescaling Qᵢ = qᵢ√(2π/k) (level k; k = 1: Qᵢ = qᵢ√(2π)). This mapping is a convention statement, not a result. **Novelty, if any, resides solely in the geodesic-axis indexation** — the identification of the mutual phase with the interlacing number î(γ₁,γ₂) of Fuchsian axes and its match to the refereed admissibility trichotomy — not in the phase itself.

---

## Task 5. Honest limits

- **No dynamics.** No Hamiltonian coupling between defects is derived; no force law, no binding, no scattering. The entire "interaction" content is: (a) the order-of-creation commutator phase e^{−iD₁₂}, and (b) the visibility/admissibility dichotomy of Theorem 2. Nothing propagates.
- **No joint arena.** Theorem 2(ii) is a statement about each single-geodesic arena separately; a two-geodesic ledger accommodating a crossing pair does not exist in the refereed framework. [GAP]
- **Multiple crossings.** Closed geodesics with geometric intersection number n > 1 correspond, at the group level, to axis pairs (axis γ₁, axis gγ₂g⁻¹) over double cosets ⟨γ₁⟩\Γ/⟨γ₂⟩. Each element pair still crosses 0 or 1 times, so the entry above is complete for element pairs. The natural extension to conjugacy classes, D̄₁₂ = Q₁Q₂ Σ_{[g]} î(γ₁, gγ₂g⁻¹) = Q₁Q₂ · (algebraic intersection number of the closed geodesics), is flagged but **not established**: a "surface-level defect" would be a sum/product over infinitely many conjugate profiles, whose joint state and possible divergences are not analyzed here. [GAP]
- The phase-trivialization caveat (Q₁Q₂ ∈ 2πℤ) means the exponentiated phase is a coarser invariant than D₁₂; only σ itself carries the full equivalence of Theorem 2.

---

## Five-line summary

1. σ(η₁,η₂) = Q₁Q₂·î(γ₁,γ₂) **exactly** whenever the ramp supports are disjoint (ε < δ/2); the limit is attained, with explicit O(tail-mass) error otherwise — proved, no gap.
2. Operationally: defect creations commute iff the axes don't cross; crossing gives commutator phase e^{∓iQ₁Q₂} on implementers (the automorphisms always commute).
3. Triple equivalence proved (given the refereed trichotomy): crossing ⟺ mutual single-arena inadmissibility ⟺ σ ≠ 0; caveat — the *phase* trivializes on Q₁Q₂ ∈ 2πℤ, and "joint-ledger breakdown" beyond per-arena inadmissibility is [GAP].
4. Dictionary entry: D₁₂ = Q₁Q₂î (signed, antisymmetric; magnitude symmetric), topological in kind — deliberately unlike the metric diagonal entry Q²ℓ/2π; the phase is the standard chiral-boson mutual statistics (others'), novelty only in the geodesic-interlacing indexation.
5. No dynamics, no force, no scattering; conjugacy-class (multi-crossing) extension flagged as a double-coset sum, not computed [GAP].

---

## Amendment (2026-07-24, same session) — referee verdict entered: D₁₂ CONFIRMED with one convention adopted

*Report verbatim in `reviews/REPORTS-phase105-D12-referee-2026-07-24.md`.*

**Confirmed [now derived, refereed]:** the exact evaluation σ(η₁,η₂) = Q₁Q₂·î(γ₁,γ₂) for ramp-disjoint profiles (Theorem 1, with δ read as the minimum over all four anchors and the plateau-matching hypothesis made explicit); the error bound (provable with constant 1); the Weyl commutator phase and its invariances; the group fact (four distinct endpoints — discreteness alone suffices); and the triple equivalence — with the referee's sharpening that **"mutual" is load-bearing**: the non-crossing case splits into *disjoint* (mutual invisibility, σ = 0) and **nested** (one-sided inadmissibility — the inner defect breaks the outer geodesic's ledger while remaining invisible to it in return — and still σ = 0). The relationship taxonomy is therefore **three-fold: disjoint (mutual ignorance), nested (one-sided disturbance without phase), crossing (mutual breakdown with phase Q₁Q₂)**. Calibration and novelty framing ruled honest.

**One gap, closed by adopting a convention (C-D5):** "same axis ⟹ σ = 0" is regularization-dependent at common atoms (the referee exhibited offset smoothings giving −Q₁Q₂). **Adopted henceforth: the symmetric (midpoint) regularization convention at shared anchors**, under which the diagonal vanishes; equivalently, commonly-smoothed profiles. Logged as a convention of the dictionary, not a theorem.

*Addendum (2026-07-26): C-D5 UPGRADED to a theorem — under charge-independence (H1) and J-equivariance (H2) of the scheme, the same-axis value 0 and collar r-antisymmetry are FORCED, exactly at every ε (phases/phase109-CD5-upgrade.md, refereed; report in reviews/REPORTS-phase109-CD5-referee-2026-07-26.md). H2 alone is insufficient (repaired charge-dependent equivariant counterexample achieves |Q₁|Q₂). The convention label is retained only for the H3-dependent single-shared-anchor extension, which cannot occur for distinct axes of a discrete group.*

**Erratum (briefing, not document):** the refereeing brief dropped the |k| weight in the norm formula; the derivation document's H^{1/2} norm is correct as printed. Logged for the process ledger.

**Dictionary status after this amendment — two refereed entries:**

> **Existence (diagonal, metric): D = Q²ℓ/2π.** A defect's charge paired with its own geodesic's length — the coherent-erasure rate.
> **Relationship (off-diagonal, topological): D₁₂ = Q₁Q₂·î(γ₁,γ₂).** Two defects' charges paired with their axes' signed crossing — the order-of-creation phase, with the three-fold visibility taxonomy (disjoint/nested/crossing) matching the refereed locality trichotomy exactly.

Open, flagged, unchanged: the joint two-geodesic arena [GAP]; the conjugacy-class extension (Q₁Q₂ × total intersection number, via double cosets) [GAP]; no dynamics anywhere.
