# Phase 113 (continuation) — K-NONAB-1 and K-FRAC-1 executed: both kills do NOT fire (2026-07-26)

**Status: DRAFTED — awaiting referee. No verdict gates change until the referee pass completes.**
**Editorial header (operator):**
- Continuation of the NONAB-0 reconnaissance (phase113-NONAB0-scoping.md): roadmap items 1 and 3 executed. NOTE: the agent self-titled its report "Phase 114" — a label slip; phase 114 is the BIND2-GAP-1 stiffness round. Per house rules the verbatim text below is NOT edited; this header is the correction of record.
- Headline results (UNREFEREED): **K-NONAB-1 PASSES** — the Casimir transplantation D_λ = 2h_λℓ/2π agrees with the refereed abelian E1 at the SU(2)₁/self-dual-boson identification (ℓ/4π both sides); the refereed E1 derivation is verified integrality-free; kink and plateau descriptions of the level-1 simple current agree. **K-FRAC-1 does NOT fire** — NONAB-FRAC survives: triality ≡ charge mod 3 is a lattice-homomorphism identity in ℤ³; the index-3 statement (singlet charge lattice 3ℤ inside fermion lattice ℤ) is forced, with zero reassignment freedom.
- New gaps: **GAP-N7** — C-BRIDGE's integer image does not contain the self-dual point ±1/√2; the torsion-to-charge unit must become arena-dependent or the bulk datum is blind to non-abelian extensions (a real fork, undecided, joining GAP-N6 on the bridge's weak side). **GAP-N8** — the level-1 pass is structurally near-automatic; SU(2)₂ is the first discriminating test.
- Honest scope: the quark charge pattern (2/3, −1/3) is NOT reproduced — the mechanism yields a uniform 1/3 (baryon-number-like); the empirical pattern needs a second u(1) (hypercharge), outside this computation.
- Consequence if refereed: NONAB-1 registration ungated on the K-NONAB-1 side (K-NONAB-2 erasability still open); NONAB-FRAC becomes candidate-with-kill-survived (adoption = operator decision).

---

## CONSULTATION (VERBATIM)

Both computations are self-contained lattice/norm arithmetic; I have everything needed from the four record documents. Executing both mandates now.

# Phase 114 — K-NONAB-1 (SU(2)₁ bridge check) and K-FRAC-1 (u(3)₁ charge-lattice arithmetic)

**Status: [derived by context-free agent; NOT refereed]. Two kill-checks executed. Both verdicts: the kills do NOT fire.**

**Summary.**
- **K-NONAB-1: PASSES.** The candidate D_λ = 2h_λℓ/2π at SU(2)₁, j = ½ gives ℓ/4π; the refereed abelian E1 formula for the corresponding self-dual-radius boson defect (q = ±1/√2, h = q²/2 = ¼) gives Q²ℓ/2π = ℓ/4π. Equal. The refereed E1 derivation is verified integrality-free at the one step where quantization could have entered (the profile's jump height), and the simple-current kink description agrees with the abelian plateau description (h = ¼ both ways). Honest deflations: the level-1 pass is nearly automatic by construction [GAP-N8], and the fractional lattice point is **not in C-BRIDGE's image** — the bridge as adopted (Q = ±n) does not cover the self-dual point [GAP-N7].
- **K-FRAC-1: does NOT fire — NONAB-FRAC survives.** In ℤ³ the identity t ≡ Q mod 3 is a lattice homomorphism identity, not a convention; every su(3)-singlet vector of ℤ³ has Q ∈ 3ℤ, so with the u(1) unit normalized to the minimal triality-0 singlet charge, triality-t sectors carry charge in (t/3) + ℤ, and **no reassignment** keeping fermions at charge 1 can make the ratio integral. Full arithmetic shown in §2.

---

## §1 K-NONAB-1: the SU(2)₁ bridge check

**(a) The identification, with normalization made explicit.** [others': Frenkel–Kac; standard CFT — flagged per house rules, not re-derived.] The su(2)₁ net is the ℤ₂ lattice extension of the U(1) current net by the A₁ root lattice: currents J^± are vertex operators of momentum ±α with |α|² = 2 (h = |α|²/2 = 1, as currents must). In the E1 charge normalization of the record (phase 106 §1: abelian sector of charge q has h = q²/2 [others': BMT sectors + Sugawara — asserted, standard]), the root lattice is Q_root = √2·ℤ, the weight (sector) lattice is P = (1/√2)·ℤ, and the sector group of the extended net is P/Q_root ≅ ℤ₂: trivial sector = cosets q ∈ √2ℤ; the j = ½ sector = q ∈ ±1/√2 + √2ℤ. Minimal representative q = ±1/√2:

  h = q²/2 = (1/2)/2 = **1/4** = h_{j=½} = j(j+1)/(k+2) = (3/4)/3. ✓ (consistency of the identification)

So the abelian shadow of j = ½ is a plateau defect of charge **Q = ±1/√2** — half a root-lattice unit; equivalently half-integer winding in root-lattice units.

**(b) The refereed abelian D at Q = ±1/√2.** The refereed formula (phase 104, all four claim groups CORRECT): D = lim‖ζ⁽ⁿ⁾_in‖²/n = Q²ℓ/2π, norm ‖f‖² = 2πΣ_{k≥1}k|f̂_k|². **Integrality audit, executed as mandated.** The derivation nowhere uses Q ∈ ℤ: Q = c|I| with slope c ∈ ℝ arbitrary throughout; c = 0 and general real c are the only cases distinguished. The one step where integrality could conceivably enter is the profile's jump height, which fixes the coefficient: ζ⁽ⁿ⁾_in is a plateau of height Q smoothed at scale e^{−nℓ}, giving |ĝ_k|² ≈ Q²/4π²k² for 1 ≲ k ≲ e^{nℓ}, hence ‖ζ⁽ⁿ⁾_in‖² = (Q²/2π)nℓ + O(1); the Gagliardo cross-term confirmation is likewise polynomial in Q (2Q²·nℓ). Both are algebraic in the real number Q — no arithmetic input. Crucially, η is a real *function* on S¹ (phase 104 §1a: the honest functional is well defined because ∫_{S¹}η′ = 0); it is not a U(1)-valued map, so no winding quantization constrains c. And q = 1/√2 **is** a point of the extended net's sector lattice P, so the defect exists in the arena. Therefore:

  **D_abelian(q = ±1/√2) = Q²ℓ/2π = (1/2)·ℓ/2π = ℓ/4π.**

**(c) The comparison.** Candidate: D_λ = 2h_λℓ/2π = 2·(1/4)·ℓ/2π = **ℓ/4π**. Equal. **K-NONAB-1 does not fire; the Casimir transplantation survives its first kill.** The convention that makes it work, stated exactly: the E1 norm convention ‖f‖² = 2πΣk|f̂_k|² with ω(W(f)) = e^{−‖f‖²/2}, under which the abelian sector weight is h = Q²/2; rescaling ‖·‖² by κ rescales D and (via the same convention) Q² identically, so the agreement is convention-stable.

**Simple-current consistency check (mandated).** At level 1, j = ½ = k/2 is the simple current; its center-valued kink description (scoping §a(i)) is a loop 1 → −1 ∈ Z₂ = P/Q_root. Under Frenkel–Kac the Z₂ kink is the boson shift by the coset representative α/2, i.e. a plateau of charge |α|/2 = √2/2 = 1/√2, h = (1/√2)²/2 = ¼ — identical to the abelian plateau description of (a). The two descriptions agree. ✓

**Honest deflations, both barrels.** (1) [GAP-N8] The pass is close to automatic: the candidate was *built* to read 2h·ℓ/2π and the abelian side satisfies h = Q²/2 identically, so at level 1 the check's genuine content is only the three verifications above (integrality-freeness of E1; existence of the fractional defect in the arena; kink ≡ plateau). It would have killed if E1 had secretly used Q ∈ ℤ or if the two h's disagreed; neither fired — but level 1 has no genuinely non-abelian content (one nontrivial sector, abelian fusion). The first *discriminating* test remains SU(2)₂ (roadmap item 4). (2) [GAP-N7 — the C-BRIDGE tension, mandated flag] C-BRIDGE (phase 107 A.6) adopts Q = ±n, D = n²ℓ/2π: the bridge image is an integer lattice ℤ·(unit). The point q = ±1/√2 is not in ℤ, and no single rescaling reconciles both records: if the bridge unit is the record's abelian unit charge 1, the self-dual lattice (1/√2)ℤ meets its image only in even multiples of nothing — 1/√2 ∉ ℤ·1; if instead the unit is re-declared as the *generator of the extension's sector lattice* (1/√2), then sector-surjectivity (N) is restored but D = n²ℓ/4π on that arena, and the abelian record's D = n²ℓ/2π becomes the even-sublattice statement. Consequence for a non-abelian extension of the bridge: **either the torsion-to-charge unit becomes arena-dependent (fixed by the extension lattice, not universal), or the non-abelian sectors lie outside the bulk datum's image entirely** — the bulk (Giroux torsion ∈ ℤ) would be blind to the extension. This is a real fork; nothing here decides it. It is registered as the successor to the scoping's pre-flagged caveat (roadmap item 1) and joins GAP-N6 on the bridge's weak side.

---

## §2 K-FRAC-1: the u(3)₁ charge-lattice arithmetic

**(a) Setup and the √3 rescaling, fully shown.** Net: 3 free charged fermions ψ^i, each of diagonal charge 1. Sector lattice of u(3)₁ = ℤ³ ∋ v = (n₁,n₂,n₃) (fermion numbers), inner product standard, h(v) = |v|²/2. Diagonal u(1) charge Q(v) = n₁+n₂+n₃. Decompose orthogonally: v = (Q/3)(1,1,1) + w, w traceless. The unit u(1) direction is e = (1,1,1)/√3, so the **u(1) boson charge is q_b = v·e = Q/√3, living on the lattice (1/√3)ℤ** — the 1/√3 rescaling, explicitly. The su(3) part w lies in the A₂ weight lattice realized in {Σxᵢ = 0}. Check on the fermion v = (1,0,0): w = (2/3,−1/3,−1/3), |w|² = 6/9 = 2/3, h_su(3) = 1/3 = c₂(3)/(1+3) = (4/3)/4 ✓; h_u(1) = q_b²/2 = 1/6; total 1/3+1/6 = 1/2 = free fermion ✓. Pure-u(1) (su(3)-singlet) vectors: w = 0 ⟺ v = m(1,1,1), m ∈ ℤ ⟺ **Q ∈ 3ℤ**, q_b = m√3: the u(1) boson factor is compactified on **√3ℤ** (the √3 rescaling on the local side; check: h(e^{i√3φ}) = 3/2 = h(1,1,1) = 3·½ ✓). Its sector group: dual/lattice = (1/√3)ℤ / √3ℤ ≅ ℤ₃.

**Triality identity (the load-bearing line).** Root lattice of su(3) inside ℤ³: generated by e₁−e₂, e₂−e₃ (traceless, Q = 0). Triality t(v) := [w] ∈ P/Q_root ≅ ℤ₃ and Q mod 3 are both homomorphisms ℤ³ → ℤ₃ killing the roots; on the generators e₁, e₂, e₃ each gives 1 (each eᵢ's traceless part lies in the fundamental-weight coset: e₂−e₁ ∈ roots ⇒ same coset). Two homomorphisms agreeing on generators are equal:

  **t ≡ Q mod 3 identically on ℤ³.**

So the branching is v ↦ (su(3)₁ sector of triality t, u(1) sector q_b = Q/√3 with class Q mod 3 = t): the fermion net is precisely the diagonal ℤ₃ (simple-current) extension of su(3)₁ ⊗ u(1)_{√3ℤ}, containing exactly the pairs with matching ℤ₃ labels. (Spin check: sector (3, q_b = 1/√3): h = 1/3 + 1/6 = 1/2, correctly fermionic.)

**Normalized statement.** Normalize the u(1) charge so the minimal triality-0 singlet is unit: Q̃ := Q/3 (the minimal w = 0 vector (1,1,1) has Q̃ = 1). Then a triality-t sector has Q̃ = Q/3 with Q ≡ t mod 3, i.e. **Q̃ ∈ (t/3) + ℤ**; the fermion (t = 1) has Q̃ = 1/3. This is NONAB-FRAC's claimed mechanism, now explicit.

**(b) The reassignment question — does K-FRAC-1 fire?** Suppose an assignment of u(1) charges to the three su(3)₁ sectors {1, 3, 3̄} keeping the fermions at charge 1. Constraints: (i) any u(1) inside u(3) commuting with su(3) is a multiple of the diagonal (Schur, on the 3), and the fermion-at-charge-1 condition pins the multiple: Q = Σnᵢ is **forced**, not chosen; (ii) any additive reassignment δ (a character on sectors) with δ(fermion) = 0 vanishes on everything the fermions generate — which is *all* of ℤ³ — so there is **zero reassignment freedom**; (iii) the residual freedom is only which coset representative one calls "the" charge of a sector class: the 3 appears with Q ∈ 1 + 3ℤ (all integers in fermion units!), the singlet-side locals with Q ∈ 3ℤ. The normalization-independent content is the **ratio**: charge(fermion)/charge(minimal su(3)-singlet u(1) unit) = 1/3, because a t = 0 vector with Q ∈ {±1, ±2} would violate t ≡ Q mod 3 — no such lattice point exists. So integrality of all charges *with the singlet unit normalized to 1* is impossible: **K-FRAC-1 does not fire; NONAB-FRAC survives**, with the mechanism = the ℤ₃ homomorphism identity above. (Stated carefully: in raw fermion units every charge is an integer — the fractionality is exactly and only the forced factor-3 index of the singlet charge lattice 3ℤ inside the fermion charge lattice ℤ, distributed over triality classes. That index-3 statement is the theorem.)

**(c) What this does and does not say about quarks.** It says: whenever a diagonal u(1) is packaged with su(3) inside an integer-charged fermion net, charge-in-thirds correlated with triality is forced lattice arithmetic, and (per the scoping's locality observation, cited not extended) the fractionally-charged sectors are exactly the ones non-local with respect to the extension — a confinement-*shaped* statement about locality, with no dynamics. It does not say: anything about gauge dynamics, a confinement scale, a mass gap, or why nature selects su(3); and the physical quark charges (2/3, −1/3) are **not** reproduced — this mechanism yields a uniform 1/3 per fermion (baryon-number-like), and the empirical pattern additionally requires mixing with a second u(1) (hypercharge), which is outside this computation. No claim beyond the arithmetic is made.

---

## Ledger

- **Verdicts:** K-NONAB-1 **does not fire** (Casimir transplantation passes at level 1; D = ℓ/4π both sides, in the E1 norm convention with h = Q²/2). K-FRAC-1 **does not fire** (NONAB-FRAC survives; t ≡ Q mod 3 is a lattice identity; singlet-lattice index 3 forced).
- **[BOX B]** Verified program-side content of §1: E1's refereed derivation is integrality-free (jump height Q ∈ ℝ enters polynomially; η is a function, not a U(1)-map — no winding quantization); the fractional defect q = 1/√2 exists in the extended arena; kink and plateau descriptions of the level-1 simple current agree (h = ¼).
- **[others']:** Frenkel–Kac / self-dual-radius identification; BMT sector weight h = q²/2 via Sugawara; h_λ formula (Kac); u(3)₁ ≅ su(3)₁ ⊕ u(1) conformal embedding (standard); simple-current-extension locality (per scoping, attribution still (unverified) there). None re-derived; the lattice arithmetic in §2 is shown in full and stands independently.
- **New gaps:** **[GAP-N7]** C-BRIDGE's image ℤ does not contain the self-dual point q = ±1/√2: the torsion-to-charge unit must become arena-dependent (generator of the extension's sector lattice, whence D = n²ℓ/4π there) or the bulk datum is blind to non-abelian extensions — unresolved fork, joins GAP-N6 on the bridge's weak side. **[GAP-N8]** the level-1 pass is structurally near-automatic; the first discriminating test of the Casimir transplantation is SU(2)₂ (roadmap item 4). GAP-N1 (no non-abelian rate computation) is untouched by either result.
- **Consequences for the roadmap:** NONAB-1 registration is now ungated on the K-NONAB-1 side (K-NONAB-2, vacuum-channel erasability, still open); NONAB-FRAC upgraded from candidate-with-kill to candidate-with-kill-survived (still not adopted; adoption is an operator decision).
- **Scope guard:** neither result is refereed; both are finite verifications inside stated conventions; nothing here computes a genuinely non-abelian rate.

---

## Amendment section

### A.1 Referee verdict (2026-07-26)

Report preserved verbatim in reviews/REPORTS-phase113-NONAB-kills-referee-2026-07-26.md. **No arithmetic error found anywhere — every number independently re-derived and agreeing.** Verdicts:

- **K-NONAB-1 survival: REFEREED**, scoped exactly as stated — a level-1 formula-consistency check (the Casimir transplantation's first gate passes; no genuinely non-abelian rate computed, GAP-N1 untouched; GAP-N8 deflation ruled fair, no overclaim).
- **K-FRAC-1: arithmetic CONFIRMED; PARTIAL as registered (C-Z1).** The registered kill wording is literally satisfiable (in raw fermion units every charge is an integer), making the kill vacuous as worded. The survival is refereed ONLY as the normalization-independent statement: **charge(fermion)/charge(minimal triality-0 singlet) = 1/3 is forced** (Schur pins the u(1) up to scale; ratios are scale-free; the index-3 of 3ℤ in ℤ is the theorem). NONAB-FRAC must be re-registered with the singlet-unit normalization pinned or as the pure index/ratio statement before any adoption decision.
- **GAP-N7: CONFIRMED in substance** — the bridge misses every nonzero sector of the self-dual arena ((1/√2)ℤ ∩ ℤ = {0}); the fork (arena-dependent unit, D = n²ℓ/4π, vs bulk blindness) stands.

### A.2 Corrections ledger

- **C-Z1 (substantive).** NONAB-FRAC/K-FRAC-1 re-registration required: pin the u(1) unit to the minimal triality-0 singlet charge, or state the kill as the index/ratio claim. Entered as the binding form; the original wording is superseded.
- **C-Z2 (editorial).** GAP-N7's garbled clauses restated: (1/√2)ℤ ∩ ℤ·1 = {0}; the local (root/even-lattice) sectors are the even integers in generator units with D = m²ℓ/π (not "the even-sublattice statement" of n²ℓ/2π).
- **C-Z3 (wording).** Convention stability restated as κ-invariance of the ratio D/(2h); Q = ∫η′ itself is coordinate-invariant and does not rescale.

### A.3 Post-verdict status

The non-abelian program's two entry gates are now refereed-passed: the Casimir transplantation survives its first (weak) kill, and the fractional-charge mechanism is a refereed lattice theorem in its corrected (index-3) form. NONAB-1 registration remains gated on K-NONAB-2 (vacuum-channel erasability) and on the operator's decision; NONAB-FRAC awaits its corrected re-registration and the operator's decision. The first discriminating computation is SU(2)₂ (roadmap item 4). GAP-N7 (the bridge-unit fork) joins the open registry alongside GAP-N6.
