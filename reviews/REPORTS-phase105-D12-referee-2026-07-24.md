# REPORT — phase 105 D₁₂ cross-invariant referee pass (2026-07-24, verbatim)

*Context-free adversarial referee on the D₁₂ derivation (phases/phase105-D12-cross-invariant.md), run per standing pre-verdict policy. Summary: Items 1–4 and 6 CORRECT with refinements (δ read as min over all four anchors; error bound provable with constant 1; the nested configuration gives ONE-SIDED inadmissibility with σ = 0, making "mutual" load-bearing in the triple equivalence; discreteness alone suffices for the four-point distinctness fact). Item 5: one GAP — diagonal consistency (same axis ⟹ σ = 0) requires a regularization convention at common atoms; the symmetric/midpoint convention repairs it. One typo flagged in the refereeing brief's setting (the |k| weight was dropped from the norm formula in the brief; the derivation document itself states the H^{1/2} norm correctly). Verdicts entered in the derivation document's amendment. Report verbatim below; standing AI-referee caveat applies.*

---

## Referee Report: Crossing Axes and the Symplectic Pairing

No files read; verified analytically per instructions.

---

### Item 1 — Lemma 1 + Proposition 1: **CORRECT** (with one caveat correctly satisfied)

**Stieltjes evaluation.** ds₂ is purely atomic: +Q₂ at a₂ (ccw entry into P₂), −Q₂ at b₂ (exit). Hence ∫s₁ds₂ = Q₁Q₂[1_{P₁}(a₂) − 1_{P₁}(b₂)]. Correct — *provided* s₁ is continuous at the atoms of ds₂, i.e. {a₁,b₁} ∩ {a₂,b₂} = ∅. This holds here (Item 4 group fact), so the evaluation is unambiguous. If atoms coincided, the integrand value at the atom would be convention-dependent; the lemma should state this hypothesis explicitly.

**Four-case analysis.** Both anchors of pair 2 in P₁ (nested either way): 1 − 1 = 0. Both outside (disjoint, or P₂ ⊇ closure(P₁)): 0 − 0 = 0. a₂ ∈ P₁, b₂ ∉: +Q₁Q₂; the ccw order is then (a₁,a₂,b₁,b₂) — matches the stated sign convention. b₂ ∈ P₁, a₂ ∉: −Q₁Q₂, order (a₁,b₂,b₁,a₂). Exhaustive and correct; interlacing ⟺ exactly one anchor of each pair in the other's arc ⟺ σ = ±Q₁Q₂.

**Antisymmetry on BV.** For BV f,g on the circle with no common discontinuities, ∫f dg + ∫g df = ∫d(fg) = 0 (no boundary); the discrete Leibniz correction Σ ΔfΔg vanishes because no atom is shared. Verified. Note σ is also well-defined mod constants on the step extension since ∫dg = 0 on S¹.

**Jump heights ±Qᵢ.** A single-valued BV function on S¹ has total signed variation (continuous + atomic) zero around the loop; for a pure two-jump step this forces jumps +Qᵢ and −Qᵢ. Correct — this is exactly the "honest function vs. multivalued winding profile" distinction.

---

### Item 2 — Theorem 1 (exactness) + error bound: **CORRECT** (bound is correct *as stated*, with mᵢ read as leaked derivative mass; the dimensional worry raised in the brief is unfounded)

**Exact case.** With ε < δ/2 (δ = min *pairwise distance among all four anchors* — the proof needs this cross-pair reading, not merely within-pair; flag for precision), B_ε(a₂) and B_ε(b₂) are disjoint from supp η₁′, each lies in a single complementary component where η₁ sits at a plateau equal to s₁'s value there. Then σ(η₁,η₂) = Σ over the two balls of (plateau of η₁)·(∫η₂′) = Q₂[η₁(a₂) − η₁(b₂)] = Q₁Q₂[1_{P₁}(a₂) − 1_{P₁}(b₂)] = Q₁Q₂·î. Exact, no error term. Correct, assuming (implicitly, should be stated) that ηᵢ has the same plateau values as sᵢ.

**Error bound.** Interpret mᵢ = ∫_{S¹∖N_ε(anchors of i)}|ηᵢ′|dθ (derivative mass leaked outside the windows). Decompose σ − Q₁Q₂î into (i) the tail integral ∫_{tail}η₁η₂′, bounded by ‖η₁‖_∞·m₂; (ii) oscillation of η₁ on the near-balls, bounded by m₁·‖η₂′‖_{L¹}; (iii) mass defect of η₂ in each ball times the plateau, bounded by ‖η₁‖_∞·m₂. Since σ is invariant under adding constants, choose min η₁ = 0; on a circle sup − inf ≤ TV/2, so ‖η₁‖_∞ ≤ ‖η₁′‖_{L¹}/2. Total: |σ − Q₁Q₂î| ≤ m₁‖η₂′‖_{L¹} + m₂‖η₁′‖_{L¹} — i.e. the stated bound holds with a factor of 2 to spare (constant 1 suffices).

**Dimensions.** m ~ charge, ‖η′‖_{L¹} ~ charge, product ~ charge² = units of σ. Sensible. The suggested "m₁·‖η₂‖_∞-type" alternative is equivalent up to the sup ≤ TV/2 inequality (and is *worse*, being non-invariant under constants). No fix needed; the conclusion σ → Q₁Q₂î as mᵢ → 0 with ‖ηᵢ′‖_{L¹} bounded survives trivially.

---

### Item 3 — Task 2(a), Weyl algebra: **CORRECT** (one typo in the setting flagged)

**Factor of 2.** W(f)W(g) = e^{−iσ(f,g)/2}W(f+g) and W(g)W(f) = e^{+iσ(f,g)/2}W(f+g) (antisymmetry), so W(f)W(g) = e^{−iσ(f,g)}W(g)W(f). Two half-phases compose; correct.

**Phase-redefinition invariance.** Under W̃(f) = e^{iφ(f)}W(f), the group commutator W(f)W(g)W(f)⁻¹W(g)⁻¹ = e^{−iσ(f,g)}·1 is unchanged (all φ's cancel). Correct.

**Ad remark.** Ad W(f)∘Ad W(g) = Ad(W(f)W(g)) = Ad(e^{−iσ/2}W(f+g)) = Ad W(f+g), symmetric in f,g since central phases die under Ad. So the automorphisms always commute; the statistics phase is invisible at the automorphism level. Correct, and the standard reason mutual statistics lives in the phase, not the map.

**Honesty remark.** Sensible — sharp steps have f̂_k ~ 1/k and infinite H^{1/2}-norm, so W(step) does not exist in the representation; only smoothed approximants do, which is precisely what Theorem 1 licenses. **Typo in the setting:** as written, ‖f‖² = 2πΣ_k|f̂_k|² is the L² norm, under which jumps are *finite*. The parenthetical "jumps divergent, kinks fine" shows the intended norm is 2πΣ_k|k||f̂_k|² (H^{1/2}). Fix the formula; the remark then stands.

---

### Item 4 — Task 2(b) + Theorem 2 (geometry dictionary): **CORRECT**, caveats properly flagged

**Distinctness of the four points.** Two hyperbolics in a discrete subgroup of PSL(2,ℝ) sharing exactly one fixed point violate discreteness (standard: conjugates γ₁ⁿγ₂γ₁⁻ⁿ, or the commutator sequence, accumulate at a nontrivial parabolic-like limit; cf. Beardon-type "no mixed fixed points in discrete groups"). Sharing both fixed points means equal axes, excluded by hypothesis. So all four endpoints are distinct. Verified — note discreteness alone suffices; torsion-free and cocompact are not needed for this step (harmless surplus hypotheses).

**Interlacing ⟺ exactly one anchor in the open arc.** With four distinct points, alternation around S¹ is equivalent to "exactly one of {a₂,b₂} in (a₁,b₁)", and is manifestly symmetric in the pairs. Correct.

**Crossing ⟺ mutual inadmissibility ⟺ σ ≠ 0.** Interlacing puts one anchor of each profile in the other's *open* axis arc ⟹ inadmissible both ways (trichotomy, assumed). Non-interlacing splits into: nested (both anchors of one pair inside the other's arc — inadmissibility is then *one-sided only*: the outer profile's anchors avoid the inner's open arc, landing it in the admissible-invisible class) and disjoint (neither inadmissible). So *mutual* inadmissibility is exactly interlacing, which by Prop. 1 is exactly σ ≠ 0. The word "mutual" is load-bearing and correctly used. Correct.

**Caveats.** (i) The *operator* phase e^{−iσ} = e^{∓iQ₁Q₂} trivializes when Q₁Q₂ ∈ 2πℤ, so "crossing ⟺ nontrivial commutation phase" needs the charge caveat while "crossing ⟺ σ ≠ 0" does not — correctly separated. (ii) The trichotomy is a per-arena statement (relative to each M_γ separately); any joint-arena assertion is indeed unproven — honest to mark GAP.

---

### Item 5 — Task 3 sanity checks: **mostly CORRECT; diagonal consistency is a GAP as stated**

**Antisymmetry of î.** Convention î(i,j) = +1 for ccw cyclic order (aᵢ,a_j,bᵢ,b_j). Given (a₁,a₂,b₁,b₂), compute î(2,1) directly: P₂ = (a₂,b₂) contains b₁ but not a₁, so î(2,1) = 1_{P₂}(a₁) − 1_{P₂}(b₁) = −1. Equivalently the cyclic rotation (a₂,b₁,b₂,a₁) is the (aᵢ,b_j,bᵢ,a_j) pattern = −1. Antisymmetry verified; consistent with σ's antisymmetry.

**Bilinearity.** σ(Q₁1_{P₁}, Q₂1_{P₂}) = Q₁Q₂σ(1_{P₁},1_{P₂}); linear in each charge. Trivially correct (bilinearity in *profiles* is inherited from σ; on the two-parameter step family only charge-bilinearity is meaningful).

**Diagonal consistency — GAP.** "Same axis ⟹ σ = 0" is *not* unconditional, because same-axis profiles have **common atoms**, exactly where the Stieltjes extension is ill-defined and Item 1's antisymmetry proof fails. Concretely: smooth η₁, η₂ with the same anchors {a,b}, with η₂'s transition preceding η₁'s at a but following it at b, give σ(η₁,η₂) ≈ −Q₁Q₂ ≠ 0. The result σ = 0 holds under any of: (i) proportional profiles / identical smoothing shape (then σ(η,cη) = 0 by antisymmetry); (ii) midpoint (symmetric) regularization convention at shared atoms (contributions +Q₁Q₂/2 at a and −Q₁Q₂/2 at b cancel). **Corrected statement:** "For same-axis profiles, σ is regularization-dependent; it vanishes under the symmetric convention or for commonly-smoothed profiles." The document should state a convention. (Note the naive formula also gives 0 for γ₂ = γ₁⁻¹, but that case has the same common-atom ambiguity.)

**Metric vs topological note.** Fair: σ/Q₁Q₂ = î depends only on the cyclic order of endpoints — a topological (chord-intersection) datum — with no dependence on translation lengths or axis distances, in contrast to the metric invariant D = Q²ℓ/2π refereed earlier. Fair and worth keeping.

---

### Item 6 — Task 4 calibration: **CORRECT / honest**

The identification with chiral-boson vertex-operator mutual statistics (commutation phase e^{iπq₁q₂·(intersection sign)}, monodromy e^{2πiq₁q₂}) matches e^{−iσ} = e^{∓iQ₁Q₂} only after fixing conventions: normalization of σ (∫fg′dθ vs (1/2π)∫), charge units / compactification radius (Q ↔ √(2π)q-type rescaling), and half- vs full-monodromy. Framing this as convention-dependent is correct — asserting an exact 2π match without fixing these would be wrong. The novelty statement is honest: anyonic commutation of chiral vertex operators is textbook; what is new here is only the indexation of step profiles by geodesic axes of Fuchsian elements and the theorem that axis-crossing (a hyperbolic-geometric relation) is equivalent to the interlacing that switches the statistics phase on, routed through the admissibility trichotomy.

---

### Summary (5 lines)

1. Lemma 1/Prop. 1 CORRECT: Stieltjes evaluation, four-case interlacing analysis, BV antisymmetry (no common atoms — guaranteed by the group fact), and zero-sum jumps all check.
2. Theorem 1 CORRECT: exactness proof sound (read δ as min over *all four* anchors); the error bound is dimensionally sensible and provable even with constant 1; conclusion survives.
3. Task 2(a) CORRECT: factor 2, phase invariance, and Ad-commutation all verified; honesty remark stands, but the setting's norm formula needs |k| inserted (H^{1/2}, not L²).
4. Theorem 2 CORRECT including the group fact (discreteness alone suffices) and both caveats; "mutual" inadmissibility is essential since nesting gives one-sided inadmissibility with σ = 0.
5. One GAP: diagonal consistency (same axis ⟹ σ = 0) fails without a regularization convention at common atoms — fix by adopting the symmetric/midpoint convention or proportional smoothings; Item 6's calibration and novelty claims are honest.
