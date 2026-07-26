# REPORT — phase 109 C-D5 upgrade referee pass (2026-07-26, verbatim)

*Context-free adversarial referee on the C-D5 upgrade derivation (phases/phase109-CD5-upgrade.md). The referee rederived the value formula and theorem by hand, reimplemented all numerics independently (different collar families, N = 8×10⁵, agreement ≤ 10⁻⁷), and repaired the counterexample rather than merely rejecting it. Editorial note: the referee's title says "JOIN-4a''" — a label slip; the report concerns the C-D5 upgrade.*

*Verdict summary: the VALUE FORMULA (σ = Q₁Q₂(w_a + w_b − 1), exact at every ε) and the H1+H2 THEOREM (charge-independence + J-equivariance force r-antisymmetric collars, w = 1/2, same-axis value 0) are both CONFIRMED, every step independently verified — with one bookkeeping repair (the −1 comes from the cross term ∫A₁B₂′ = 1, which does NOT vanish by disjointness) and one strengthening (w(δ)+w(−δ) = 1 holds for arbitrary common shapes, not just symmetric). The COUNTEREXAMPLE to "H2 alone suffices" is RIGHT IN SUBSTANCE, WRONG AS STATED on two independent grounds (the 3ε displacement exits the admissibility window; rigid displacement is not exactly Möbius-equivariant, O(δ²) mismatch measured) — and REPAIRED by the referee (define the negative-charge branch as the r-image of the positive branch: exactly equivariant by construction, admissible, σ = sgn(Q₁)Q₁Q₂ exactly). The refutation stands: H1 is genuinely load-bearing. Single-anchor analysis CONFIRMED including the delicate "consistency, no constraint" identity (verified analytically); H3 endorsed as a flagged independent axiom, with the referee's observation that H3 subsumes H2's role for the same-axis value; the half-integer diagonal is exact per-anchor, heuristic as a limit (the discontinuity blocks the limit reading). Re-registration language ruled ACCURATE contingent on the two repairs. C-D5 is hereby upgradeable: value-theorem under H1+H2. Verdicts entered in the phase-109 amendment and the E2 registration addendum. Report verbatim below; standing AI-referee caveat applies.*

---

# Referee report: JOIN-4a'' / C-D5 upgrade derivation

**Summary.** The core value formula (D1) and the H1+H2 theorem (D2) are correct; I rederived both by hand and confirmed all identities numerically (independent implementation, cubic/sin²/asymmetric collars, N = 8×10⁵ grid, agreement ≤ 10⁻⁷). One derivation-level bookkeeping trap in D1 must be stated correctly: the cross term ∫A₁B₂′ does **not** vanish — it equals 1 and is precisely the source of the "−1". The counterexample (D3) is **right in substance but wrong as stated**, on two independent grounds: the 3ε displacement violates the BOX 1 admissibility window, and rigid ±δ displacement is not exactly r-equivariant because r is Möbius, not a rigid reflection (mismatch O(δ²), measured 4.2×10⁻³ at δ=0.01). Both defects are repairable within the window, and the repaired scheme achieves exact equivariance with σ = sgn(Q₁)Q₁Q₂ exactly — the refutation stands. D4 checks out, including the nontrivial "consistency, no constraint" claim, which I verified is an exact identity. The re-registration language (D5) is accurate.

## 1. (D1) Value formula σ = Q₁Q₂(w_a + w_b − 1) — CORRECT WITH REPAIR (bookkeeping)

Cut the circle in the complement of (a,b); write hᵢ = Aᵢ − Bᵢ with Aᵢ rising at a, Bᵢ rising at b. A, B are non-periodic on the cut, but h₁, h₂ and the integrand h₁h₂′ are periodic, so the bookkeeping is valid. Expanding:

σ/Q₁Q₂ = ∫A₁A₂′ − ∫A₁B₂′ − ∫B₁A₂′ + ∫B₁B₂′.

**The trap:** the cross terms do *not* both vanish by collar disjointness. ∫B₁A₂′ = 0 (B₁ ≡ 0 on the a-collar), but ∫A₁B₂′ = 1 exactly (A₁ ≡ 1 on the b-collar; the integral is the total rise of B₂). Numerics: A₁B₂′ = 1.000000, B₁A₂′ = 0 in every trial. So m_a = w_a, m_b = w_b − 1 is correct **only if** the −1 is attributed to the cross term, not to disjointness. If the source text claims the cross terms vanish, that step is WRONG though the formula survives; as itemized here ("m_b = w_b − 1"), the arithmetic is consistent.

Verified numerically: worst |σ − Q₁Q₂(w_a+w_b−1)| = 8.7×10⁻⁸ over random ε ∈ [0.02, 0.15], shapes, displacements, charges. Exact at every ε (caveat: requires a- and b-collars disjoint and plateaus present, i.e., ε small relative to both arc lengths — implicit in admissibility). Corners confirmed: common collars → σ ≈ 10⁻⁸–10⁻¹¹ at ε = 0.02, 0.08, 0.2; fully ccw → +1.00000000; fully cw → −1.00000000. w ∈ [0,1] needs monotonicity (h₂′ ≥ 0) — used, and available.

**Strengthening:** w(δ) + w(−δ) = 1 holds for **any** common shape, not just symmetric ones: w(δ)+w(−δ) = ∫ d/dθ[h(θ)h(θ−δ)] dθ across the collar = 1. Confirmed with an asymmetric shape (sum = 1 to 5×10⁻⁹). The "symmetric shapes" hypothesis is superfluous.

## 2. (D2) H1+H2 theorem — CORRECT

(i) r fixes a, b and reverses orientation, so it **swaps** the two complementary arcs (reflection across the a–b geodesic; verified: r(2.0) = 5.865 ∉ (1, 3.5), r(0.2) = 1.638 ∈ (1, 3.5)). Hence 1_{(a,b)}∘r = 1_{(b,a)} = 1 − 1_{(a,b)} a.e., so Q·1∘r ≡ −Q·1 mod constants: r·C is the charge-negated C. Correct. Also verified r′(a) = −1.00000000 and σ(f∘r, g∘r) = −σ(f,g) to 3×10⁻⁹.

(ii) From (H1)+(H2): −Qᵢhᵢ ≡ Qᵢ(hᵢ∘r) mod constants ⟹ hᵢ∘r = cᵢ − hᵢ (needs Qᵢ ≠ 0; Qᵢ = 0 gives σ = 0 trivially — harmless gap, worth a footnote). Evaluating at a point deep outside (hᵢ = 0, r-image deep inside where hᵢ = 1) gives cᵢ = 1. Correct; requires exact 0/1 plateaus, guaranteed for admissible ε.

(iii) The double computation of J. The r-invariant U exists constructively: U := (r(a+δ), a+δ) satisfies r(U) = U exactly (r involutive), and since hᵢ∘r = 1−hᵢ forces each a-collar to be r-invariant as a set, U with δ ≈ 2ε contains both a-collars and avoids b for small ε. ∫_U h₂′ = 1 exactly (h₂ ≡ 0 at the cw end, ≡ 1 at the ccw end of U). Substitution: J = ∫_U (h₁∘r)(h₂∘r)′ = −∫_{r(U)} h₁h₂′ = −m_a (orientation-reversal sign correct). Alternatively J = ∫_U(1−h₁)(1−h₂)′ = −1 + m_a. Hence m_a = 1/2; identically w_b = 1/2, m_b = −1/2, σ = 0. **Numerically confirmed with two *different* r-antisymmetric collar shapes** (constructed via h ↦ (h + 1 − h∘r)/2, antisymmetry residual 10⁻⁸): w_a = 0.500000, m_b = −0.500000, σ = 1.2×10⁻⁹.

(iv) h(a) = 1/2 and collar r-antisymmetry follow immediately from h∘r = 1−h at the fixed point; confirmed (H(a) = 0.500000). Consistent with the refereed entry-6 fact.

(v) No hidden ε → 0; monotonicity unused in the theorem proper. "Forced: value + r-antisymmetry; not forced: common shape" — correct (my two-shape test exhibits distinct antisymmetric collars, both giving w = 1/2). Non-injectivity (value 0 ⟺ w_a + w_b = 1) — correct.

## 3. (D3) Counterexample S* — CORRECT WITH REPAIR (two genuine defects, both repairable; refutation stands)

**Defect 1 — admissibility.** BOX 1 confines each collar to the ε-window at its anchor ("collar within Iᵢ minus/plus its ε-collars"). A width-ε collar displaced by 3ε occupies up to ≈4ε from the anchor and leaves h₂ ≡ 0 on an O(ε) sub-arc of the *interior* — violating "1 inside/0 outside" relative to the ε-window. As stated, S* is inadmissible. (Note the D1 corners w = 1 are attainable admissibly: two width-ε/2 collars packed disjointly inside the window — verified, σ = ±Q₁Q₂ exactly.)

**Defect 2 — the equivariance claim itself.** r is a Möbius reflection, not θ ↦ 2a−θ; r(a+δ) = a − δ + O(δ²). So a rigid displacement by +3ε is *not* mapped to a rigid displacement by −3ε. Measured: sup|r-image(h₊) − h₋| = 4.2×10⁻³ (δ=0.01), 1.2×10⁻² (δ=0.02), 4.2×10⁻² (δ=0.04) — O(δ²) and nonzero. The stated S* is only approximately J-equivariant, so "exactly J-equivariant" is false as written.

**Repair (verified).** Define the scheme's Q₁<0 branch as the *r-image* of its Q₁>0 branch: h₂⁻ := 1 − h₂⁺∘r. Equivariance is then exact **by construction** (involution-consistent since r² = id; verified to 5.6×10⁻¹⁷), and admissibility holds: the r-image collar sits in [a−0.0227, a−0.0075], inside the ±ε window. With profile 1's collar narrow, r-antisymmetric, straddling a, and h₂⁺ fully ccw-displaced within the window: σ/Q₁Q₂ = +1.00000000 (Q₁>0 branch) and −1.00000000 (Q₁<0 branch), i.e., σ_reg = sgn(Q₁)Q₁Q₂ = |Q₁|Q₂ exactly, matching the claimed value. Even a mild δ = ε/2 partial displacement gives σ/Q₁Q₂ = 2w−1 = +0.881 ≠ 0. Consistency check: σ(r·C) = sgn(−Q₁)(−Q₁)(−Q₂) = −|Q₁|Q₂ = −σ(C) ✓. Q₁ = 0 stratum: sgn(0) = 0 assigns symmetric collars; r·C also has Q₁ = 0, equivariance holds and σ = 0 — no gap (the scheme is discontinuous in Q₁, but nothing in BOX 1 requires charge-continuity once H1 is dropped).

**Adjudication:** the refutation of "(H2) alone forces C-D5" is **sustained** after repair. H1 is genuinely load-bearing in the theorem; the "obstruction" diagnosis (r relates C to the different configuration r·C, so equivariance alone only forces the pair pattern σ(r·C) = −σ(C)) is correct. But the published S* must be re-stated with the r-image construction and in-window displacement.

## 4. (D4) Single shared anchor — CORRECT (with flags endorsed)

Value formula: rederived — for b₁ ∈ (a,b₂): σ/Q₁Q₂ = w_a − ∫A₁B₂′ − ∫B₁A₂′ + ∫B₁B₂′ = w_a − 1 − 0 + 1 = w_a; other ordering: w_a − 1. Numerically exact in three displaced trials (e.g., 0.181996 vs 0.181996; antisymmetric under profile swap ✓).

ρ exists and is unique: three conditions ρ(a)=a, ρ(b₁)=b₂, ρ(b₂)=b₁ determine an orientation-reversing Möbius map; ρ² fixes three points ⟹ ρ² = id; (ρ′(a))² = 1 with orientation reversal ⟹ ρ′(a) = −1. Constructed numerically: all conditions to 10⁻¹⁶, ρ′(a) = −1.000000, determinant < 0.

**"Consistency, no constraint" — verified analytically** (this was the step most likely to hide an error): equivariance + charge-independence give A₁ = 1 − A₂∘ρ near a (linking the a-collar of interval (a,b₁) to the ρ-image of the *other* interval's a-collar — not self-referential, unlike the same-axis case). Substituting into w_a = ∫A₁A₂′ and using the orientation-reversing substitution yields w_a = 1 + (w_a − 1) = w_a — an identity. The two relations A₁ = 1−A₂∘ρ and A₂ = 1−A₁∘ρ are equivalent (ρ² = id), so no constraint. Correct, and honestly reported. Label-symmetry functions as an axiom (assignment depends on interval geometry, not labels) — should be flagged as such, as should the fact that it piggybacks on charge-independence.

(H3) is principled in spirit (locality of the regulator in the anchor germ) but is a genuinely independent axiom; the derivation's flags (ρ not a modular conjugation; the b₂→b₁ discontinuity blocking any continuity substitute) are apt. Under H3 both profiles share the germ at a (both ccw from a), so A₁ = A₂ = A, the ρ-relation becomes self-referential (A = 1−A∘ρ), forcing A(a) = 1/2 and w_a = ∫AA′ = 1/2. Arithmetic ✓: σ = ±Q₁Q₂/2, î ∈ ½ℤ. **One observation the derivation should add:** H3 (+ charge-independence) makes H2 redundant for the same-axis value — identical germs at each anchor force common collars, hence w = 1/2 directly. The "+½ − ½ = 0" diagonal is exact as the per-anchor decomposition (m_a + m_b of D1), but as a b₂→b₁ limit of two single-anchor configurations it is heuristic — the flagged discontinuity (½ vs 0) shows the limit does not commute; BOX 5's framing is consistent only under the former reading.

## 5. (D5/E) Consistency with E2 and the record — CORRECT

The corners reproduce the prior referee's regularization-dependence exactly: cw offset ⟹ w_a = w_b = 0 ⟹ σ = −Q₁Q₂; ccw ⟹ +Q₁Q₂ (both verified to 10⁻⁸ at three ε). E2 (distinct anchors) is untouched: at four distinct anchors all four collar pairings are the constant-plateau type, giving the exact integer î. The re-registration language — value-theorem under H1+H2 for shared axes; H3 a convention-level extension only for configurations not arising in the discrete-group setting — is accurate, **provided** D3 is re-stated with the repaired S* (the record should not contain the inadmissible 3ε version) and D1's cross-term bookkeeping is stated correctly.

## Summary list

1. **D1 (value formula):** CORRECT WITH REPAIR — formula and corners exact (verified ≤10⁻⁷); but ∫A₁B₂′ = 1, not 0: the −1 comes from this cross term, and any "cross terms vanish by disjointness" phrasing must be fixed. w(δ)+w(−δ)=1 holds for arbitrary (not just symmetric) common shapes.
2. **D2 (H1+H2 theorem):** CORRECT — every step checks, including the r-invariant U construction and the J double-count; footnote Qᵢ = 0.
3. **D3 (counterexample):** CORRECT WITH REPAIR — as stated, inadmissible (3ε exits the window) *and* not exactly equivariant (Möbius r ≠ rigid reflection, O(δ²) mismatch measured); the r-image-branch scheme repairs both, is exactly equivariant, and yields σ = sgn(Q₁)Q₁Q₂ exactly. Refutation of "H2 alone suffices" stands.
4. **D4 (single anchor):** CORRECT — ρ exists uniquely with ρ′(a) = −1; the no-constraint identity verified analytically; H3 is a flagged independent axiom (note: it also subsumes H2's role for the same-axis value); diagonal reassembly exact per-anchor, heuristic as a limit.
5. **D5/E (record):** CORRECT — conditional upgrade language accurate, contingent on repairs 1 and 3.
