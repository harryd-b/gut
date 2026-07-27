# Phase 120 (continuation): SU(2)₃ round 1 — the non-free gate

**Date:** 2026-07-27
**Status:** DRAFTED — awaiting referee. No verdict enters the phase-120 registration until the referee pass completes. The consultation below is preserved VERBATIM; nothing edited.
**Provenance:** Context-free derivation agent (SU(2)₃ mandate, registered in phases/phase120-OCC-SU23-FORK-registration.md §2, the C-AD6-corrected successor gate). The C-AD1/2/3/5 language disciplines and the UNIT-1 re-tag were binding on this round and were used.

**Editorial header (operator):**
- **KILL-LABEL INVERSION (to be confirmed by referee; substance unaffected):** the round's verdict box announces "K-SU23-1: KILL FIRES — no free realization." Per the REGISTERED kill wording (phase 120 §2: K-SU23-1 fires IF SU(2)₃ admits a free-field realization, killing the "first non-free gate" claim), the round's actual finding — no free realization exists — means **K-SU23-1 does NOT fire and the gate PASSES**. The agent used "kill" for the free-realization hypothesis, not for the registered kill. Recorded here per house rules (verbatim text untouched); the referee is instructed to confirm the substance under the registered wording.
- Headline substance (UNREFEREED): **SU(2)₃ has no free realization** — two independent, individually fatal obstructions: (i) quantum dimension d_{1/2} = d_1 = φ (golden ratio), irrational, outside the free-type set {2^{m/2}} ∪ {1}, and no free theory can even contain a φ-dimensional object; (ii) chiral central charge c = 9/5 ∉ ½ℤ (a stack of n Majoranas + m bosons has c = n/2 + m; 9/5 unreachable; the mod-8 refinement checked and the obstruction survives). The k = 2 Majorana evasion has NO analogue at k = 3. **The gate gap ("non-abelian ≠ non-free") is closed on both sides:** SU(2)₂ = non-abelian-but-free; SU(2)₃ = non-abelian-and-non-free, with the non-free core localized in the Fibonacci factor (SU(2)₃ ≅ Fib ⊠ anti-semion as MTCs, h mod 1 / c mod 8 only — carefully scoped, BOX-3).
- **K-SU23-2 passes at consistency level:** channel spectra for both splittings finite, distinct, multiplicity-free (all N^c ∈ {0,1}): ½⊗½ = 0⊕1 gives ΔD = {−3ℓ/5, +ℓ/5}; ½⊗1 = ½⊕3/2 gives ΔD = {−4ℓ/5, +2ℓ/5}; exponent-level monodromy correspondence exact in all four channels (C-AD2 discipline maintained: only the mod-1 part is monodromy-forced; BOX-4 honestly notes the exact real-lift agreement is arithmetically automatic under the candidate).
- **Structural discriminator found (per the C-AD3 mandate):** the categorical sum rule Σ d_c θ_c/(θ_aθ_b) = 𝒟·S_{½½} = **1 exactly — NONZERO** at k = 3, in contrast to k = 2's phase-level cancellation (S = 0 there). The k = 2 cancellation was special, not generic.
- Lattice observations convention-pinned under BOTH readings (C-AD5 discipline): Reading A — the k = 3 Cartan lattice (1/√6)ℤ is incommensurable with BOTH prior gates' lattices; Reading B — integer labels unchanged, only the quadratic form rescales (denominators 4/8/12), with h-spectra still intersecting only at 0. A clean coset localization: the non-Cartan remainder for j = ½ and j = 1 is exactly 1/15 in both cases — the ℤ₃-parafermion spin-field weight (c = 4/5 coset), mirroring the categorical Fibonacci localization. GAP-N7 untouched.
- Scope kept honest: everything rate-valued rides GAP-N1 (transplantation candidate) plus the strictly stronger pair extension (the round's GAP-2); the channel-defect spectra are falsifiable predictions of the candidate.

---

## CONSULTATION (VERBATIM)

# SU(2)₃ — the non-free gate: sector data, free-realization kill, channel spectra, lattice observations

## Summary of verdicts

**K-SU23-1 (non-free gate): KILL FIRES — no free realization.** SU(2)₃ admits no free-field realization in the sense defined below; the Majorana-type evasion that saved SU(2)₂ is closed off by two independent, individually fatal obstructions (quantum dimension d = φ irrational, not of free type; chiral central charge c = 9/5 ∉ ½ℤ). This is the program's first genuinely non-abelian AND non-free gate, closing the gap left standing after k = 2.

**K-SU23-2 (channel spectrum): PASSES at consistency level.** Both fusion splittings yield finite, distinct, one-dimensional channel spectra; every channel-defect exponent ΔD_c/2ℓ matches the monodromy exponent exactly (not merely mod 1) in all four channels checked; the categorical sum rule evaluates to a **nonzero** value (𝒟S_{½½} = 1 exactly), a structural difference from k = 2's phase-level cancellation, recorded per C-AD3.

All rates ride the transplantation candidate D_λ = 2h_λℓ (GAP-N1); nothing here derives it.

## 1. Sector data table (k = 3)

All entries are standard affine SU(2)₃ data [others']; each was verified numerically (16-digit agreement).

h_j = j(j+1)/(k+2) = j(j+1)/5 [others']:

| j | h_j | θ_j = e^{2πih_j} | d_j | D_j = 2h_jℓ (candidate, GAP-N1) |
|---|-----|------|-----|------|
| 0 | 0 | 1 | 1 | 0 |
| ½ | 3/20 | e^{3πi/10} | φ | 3ℓ/10 |
| 1 | 2/5 | e^{4πi/5} | φ | 4ℓ/5 |
| 3/2 | 3/4 | e^{3πi/2} = −i | 1 | 3ℓ/2 |

Central charge c = 3k/(k+2) = 9/5 [others']. Quantum dimensions d_j = sin((2j+1)π/5)/sin(π/5) [others']: d_{1/2} = sin(2π/5)/sin(π/5) = 2cos(π/5) = φ = (1+√5)/2; d_1 = sin(3π/5)/sin(π/5) = sin(2π/5)/sin(π/5) = φ (equal by sin(3π/5) = sin(2π/5)); d_{3/2} = sin(4π/5)/sin(π/5) = 1. So **d = (1, φ, φ, 1)**, confirming the brief's flagged standard result. Total dimension 𝒟² = 2 + 2φ² = 2(φ + 2) = 5 + √5 ≈ 7.2361, 𝒟 = √(5+√5) ≈ 2.6900, agreeing with 𝒟 = √((k+2)/2)/sin(π/(k+2)) [others'].

**Fusion rules** (affine truncation: c runs from |a−b| to min(a+b, k−a−b)) [others']: ½⊗½ = 0⊕1; ½⊗1 = ½⊕3/2; **1⊗1 = 0⊕1 only** — the naive spin-2 channel requires c ≤ k−a−b = 3−2 = 1, so 2 is excluded (note 1 itself survives at k = 3, unlike k = 2 where 1⊗1 = 0 only); 3/2⊗3/2 = 0 (min(3, 0) = 0). So j = 3/2 is an order-2 simple current (ℤ₂), d = 1, as claimed.

**Spin verification (C-AD1 discipline).** Each θ_j was recomputed from h_j and checked against the ribbon/modularity structure via the Gauss-sum anomaly identity Σ_j d_j²θ_j = 𝒟·e^{2πic/8} [others']: LHS = 1 + φ²e^{3πi/10} + φ²e^{4πi/5} − i = 0.42081 + 2.65688i = 𝒟e^{2πi(9/5)/8} to 9×10⁻¹⁶. [BOX-1: this confirms the spin assignments are mutually consistent with c = 9/5 mod 8 at ribbon level; it is a consistency check, not an independent derivation of the θ's.]

## 2. K-SU23-1 — the non-free gate

**Sense of "free" used (pinned):** realizable as (a stack of) finitely many free Majorana fermions and/or free compact bosons on even/self-dual charge lattices — i.e., theories with quadratic Hamiltonians, the exact class that furnished SU(2)₁'s lattice-boson realization and SU(2)₂'s three-Majorana so(3)₁ evasion.

**(i) Quantum-dimension obstruction.** Free-fermion sector categories are Ising-type stacks with all quantum dimensions of the form 2^{m/2}, m ∈ ℤ≥0 (so d ∈ {1, √2, 2, …}); lattice-boson (pointed) categories have all d = 1 [others']. In all free cases d² ∈ ℤ. Here d_{1/2} = d_1 = φ: φ² = φ + 1 is irrational, so d² ∉ ℤ; equivalently 2^{m/2} = φ would need m = 2log₂φ ≈ 1.3885 ∉ ℤ (verified). Moreover a fusion subcategory of a free theory's sector category inherits its objects' quantum dimensions, so no free theory can even *contain* an object of dimension φ. Fibonacci's d = φ is the canonical non-free quantum dimension [others']. **Scope:** this argument kills realization by free fermions/bosons and survives stacking (dimensions multiply, staying in the free-type set); it does not by itself address arbitrary interacting rewritings, which are outside the gate's sense of "free". [BOX-2: the classification "free ⇒ d ∈ {2^{m/2}} ∪ {1}" is imported, not rederived here.]

**(ii) Central-charge obstruction.** A stack of n Majoranas and m free bosons has chiral c = n/2 + m ∈ ½ℤ [others']. c = 9/5: 9/5 ∈ ½ℤ would require n + 2m = 18/5 ∉ ℤ — verified false. Contrast k = 2: c = 3/2 = 3·(1/2) ∈ ½ℤ, exactly the loophole the three-Majorana realization exploited. At k = 3 the loophole is arithmetically closed. [GAP-1: c alone constrains only *which* free stacks exist; combined with (i) the kill is doubly supported. Caveat: matching c mod 8 rather than c exactly is the invariant notion for chiral sector categories; 9/5 mod 8 is still not in ½ℤ mod 8's image, so the obstruction survives the mod-8 refinement.]

**(iii) Fibonacci subcategory and factorization.** The integer-spin sectors {0, 1} close under fusion (1⊗1 = 0⊕1) with d_1 = φ, h_1 = 2/5: this is the Fibonacci category [others'], the canonical universal-for-quantum-computation, provably non-free modular category. Factorization — stated carefully: as **modular tensor categories**, SU(2)₃ ≅ Fib ⊠ (anti-semion), where the pointed ℤ₂ factor is generated by the simple current 3/2 with θ = −i (h = 3/4 ≡ −1/4 mod 1). Verified: sector match (1,1)↔0, (τ,1)↔1, (1,s̄)↔3/2, (τ,s̄)↔½ with h_τ + h_{s̄} = 2/5 + 3/4 = 23/20 ≡ 3/20 = h_{1/2} **mod 1** (spins match only mod 1); dimensions (1,φ,1,φ) match; central charges match **mod 8**: c(Fib) + c(s̄) = 14/5 + 7 = 49/5 ≡ 9/5 (mod 8), verified. What does NOT follow: an exact chiral-algebra (VOA) isomorphism at c = 9/5 — the identification is categorical, with h mod 1 and c mod 8 only. [BOX-3: the factorization is used only to localize non-freeness in the Fib factor; the kill in (i)–(ii) stands independently of it.] The anti-semion factor alone would be abelian (pointed, SU(2)₁-type, free-realizable); the non-free core is entirely Fibonacci.

**Ruling: K-SU23-1 FIRES.** No free realization exists in the pinned sense; obstructions (i) and (ii) are independent and each fatal. SU(2)₃ is the program's first gate that is both genuinely non-abelian (non-pointed, d = φ non-invertible) and genuinely non-free. The standing "non-abelian ≠ non-free" gap is now populated on both sides: SU(2)₂ (non-abelian, free) vs SU(2)₃ (non-abelian, non-free).

## 3. K-SU23-2 — channel spectra

All rates below are candidate rates under GAP-N1 (transplantation D_λ = 2h_λℓ) and its strictly stronger pair extension (channel c on the carrier gets D_c = 2h_cℓ) [GAP-2: the pair extension is assumed, not derived — flagged as the load-bearing assumption of this entire section].

**Splitting A: ½⊗½ = 0⊕1.** D₀ = 0; D₁ = 2·(2/5)·ℓ = 4ℓ/5. Reference 2D_{1/2} = 3ℓ/5. Defects: **ΔD₀ = −3ℓ/5, ΔD₁ = +ℓ/5** (verified). Exponent check (C-AD2 discipline — exponent level only): ΔD₀/2ℓ = −3/10 vs h₀ − 2h_{1/2} = −3/10 ✓; ΔD₁/2ℓ = 1/10 vs h₁ − 2h_{1/2} = 2/5 − 3/10 = 1/10 ✓. The monodromy phases θ_c/θ_{1/2}² = e^{2πi(−3/10)}, e^{2πi(1/10)} determine these only mod 1; the rate values are the strict real lifts supplied by the candidate, per C-AD2.

**Splitting B: ½⊗1 = ½⊕3/2.** D_{1/2} = 3ℓ/10, D_{3/2} = 3ℓ/2. Reference D_{1/2} + D_1 = 3ℓ/10 + 4ℓ/5 = 11ℓ/10. Defects: **ΔD_{1/2} = −4ℓ/5, ΔD_{3/2} = +2ℓ/5** (verified). Exponents: −2/5 = h_{1/2} − h_{1/2} − h_1 ✓; +1/5 = 3/4 − 3/20 − 2/5 ✓. Four for four at exact (real-lift) level, though only the mod-1 part is monodromy-forced. [BOX-4: exact (not just mod-1) agreement is automatic given the candidate's definition, so it is a coherence check on the arithmetic, not independent evidence for the candidate.]

**Categorical sum rule (C-AD3).** Identity Σ_c N^c_{ab} d_c θ_c/(θ_aθ_b) = 𝒟S_{ab} [others'], with S_{ab} = √(2/5)·sin((2a+1)(2b+1)π/5) [others']. For (a,b) = (½,½): LHS numerically e^{−3πi/5} + φe^{πi/5} = **1 + 0i** (imaginary part < 3×10⁻¹⁶); RHS = 𝒟S_{½½} = 𝒟·√(2/5)sin(4π/5) = sin(4π/5)/sin(π/5) = **1 exactly**. So S_{½½} ≈ 0.37175 ≠ 0: **no phase-level cancellation at k = 3**, in structural contrast to k = 2 where S_{½½} ∝ sin(π) = 0 forced the two channel phases to cancel. Recorded: the d_c-weighted channel monodromy phases here sum to the *nonzero* real value 1 (= d_{3/2}, since sin(4π/5)/sin(π/5) is the j = 3/2 dimension formula). Bonus check for (a,b) = (½,1): LHS = −1 = 𝒟S_{½,1}, verified. Per C-AD3, this identity is quantified over the canonical nonnegative weighting N^c_{ab}d_c only; no claim is made for other weightings.

**Finiteness/distinctness/data-status (GAP-N5 discipline).** Finiteness: every fusion product has ≤ 2 channels. Multiplicities: all N^c_{ab} ∈ {0,1} at SU(2)₃ (level-1 truncated Clebsch–Gordan; no multiplicity ≥ 2 occurs for SU(2)_k at any k [others']) — all intertwiner spaces are one-dimensional, so a channel label is a pure superselection-type label with no internal degeneracy to suppress. Distinctness: within each splitting the candidate rates differ (0 ≠ 4ℓ/5; 3ℓ/10 ≠ 3ℓ/2), so the channel label is in-principle readable from the rate — admissible as DATA. Outcome-selection (which channel occurs, with what probability — the d_c²/𝒟-type weights) remains quarantined as dynamics, per the program thesis. **K-SU23-2: PASSES** as consistency structure.

## 4. Lattice/Cartan observations (convention-pinned per C-AD5; GAP-N7 untouched)

Cartan weights m ∈ ℤ (m = 2j₃; weight lattice of su(2), m ≡ 2j mod 2). The Cartan U(1) vertex operator at level k has h_Cartan = m²/(4k) = **m²/12** [others']. With the refereed conversions D = 2hℓ = q²ℓ (q = Q/√(2π), Q² = 4πh), the Cartan record charge is q = √(2h_Cartan) = **m/√6**.

**Reading A (lattice = Rℤ, physical q-space):** Cartan sublattice (1/√6)ℤ, spacing 1/√6 ≈ 0.40825; level-tagged comparison: k = 1 spacing 1/√2, k = 2 spacing 1/2, k = 3 spacing 1/√6. Ratios: (1/√6)/(1/√2) = 1/√3 (irrational), (1/√6)/(1/2) = √(2/3) (irrational) — both verified. Under this reading, adopting SU(2)₃ demands an **incommensurable** new charge lattice relative to both prior gates: neither a refinement nor an extension of either.

**Reading B (record-charge integers):** the data are the integer labels m ∈ ℤ with quadratic form m²/(4k); the label lattice ℤ is *unchanged* across levels and only the form normalization rescales (denominator 4 → 8 → 12). Under this reading adopting SU(2)₃ demands **neither** refinement nor incommensurability at the label level; the entire change sits in the form. Note the h-spectra {m²/12} and {m²/4} intersect only at 0 (m² = 3n² has no nonzero integer solutions), so even here the spectra are incommensurable while the labels are not.

The fork between readings is not resolved here (C-AD5; GAP-N7 stands). One pinned observation, valid under both readings: the simple current j = 3/2 satisfies h_{3/2} = 3/4 = 3²/12 exactly — it lies *on* the Cartan sublattice with zero coset remainder, consistent with its d = 1 abelian-like status. The non-Cartan remainder for j = ½ and j = 1 is h_j − m²/12 = 1/15 in both cases (3/20 − 1/12 = 2/5 − 1/3 = 1/15, verified), which is the ℤ₃-parafermion spin field weight in the coset SU(2)₃/U(1) at c = 9/5 − 1 = 4/5 [others'] — the non-free residue localizes in the parafermion coset, mirroring the categorical localization in the Fibonacci factor.

## 5. Scope statement

Every rate D_j and every channel rate/defect above rides the underived transplantation candidate GAP-N1 (D_λ = 2h_λℓ) and, for channel rates, its strictly stronger pair extension (GAP-2). This round establishes consistency structure — the candidate's channel-defect arithmetic is internally coherent, exponent-matched to monodromy, and sum-rule consistent — but derives nothing. The channel-defect spectra {−3ℓ/5, +ℓ/5} and {−4ℓ/5, +2ℓ/5} are falsifiable predictions of the candidate: any realization assigning different real lifts (same mod-1 exponents) would kill the pair extension without touching GAP-N1's mod-1 content.

## VERDICT BOX

1. **K-SU23-1: KILL FIRES — SU(2)₃ has NO free realization** (d = φ ∉ {2^{m/2}}; c = 9/5 ∉ ½ℤ; two independent fatal obstructions; Fibonacci factor is the non-free core).
2. **Gate-gap closed:** first genuinely non-abelian and non-free gate; k = 2's Majorana evasion has no analogue at k = 3.
3. **K-SU23-2: PASSES** — channel spectra finite, distinct, multiplicity-free (N^c ∈ {0,1}); labels admissible as superselection data; selection quarantined.
4. **Monodromy correspondence holds at exponent level in all four channels** (ΔD_c/2ℓ = h_c − h_a − h_b exactly; mod-1 part is the monodromy-forced content per C-AD2); sum rule Σd_cθ_c/(θ_aθ_b) = 𝒟S_{½½} = 1 ≠ 0 — no phase cancellation, unlike k = 2.
5. **All rates conditional on GAP-N1 + pair extension (GAP-2);** lattice fork (C-AD5/GAP-N7) recorded under both readings, unresolved: incommensurable (Reading A) vs form-rescaling only (Reading B).

## Gaps-and-boxes ledger

- **[GAP-N1]** (standing, program-level): transplantation candidate D_λ = 2h_λℓ underived; everything rate-valued here is conditional on it.
- **[GAP-2]**: the pair extension (channel c carries D_c = 2h_cℓ on the carrier) is strictly stronger than GAP-N1 and equally underived; load-bearing for all of §3.
- **[GAP-1]**: the c ∉ ½ℤ obstruction imports the classification of free-stack central charges; mod-8 caveat checked and survives.
- **[GAP-N7]** (standing): lattice-convention fork unresolved; both readings recorded, level-tagged, per C-AD5.
- **[BOX-1]**: Gauss-sum/anomaly identity used as the C-AD1 ribbon-level spin verification — consistency, not derivation.
- **[BOX-2]**: "free ⇒ quantum dimensions in {2^{m/2}}, pointed ⇒ d = 1" imported [others']; the kill's scope is exactly the pinned sense of "free".
- **[BOX-3]**: Fib ⊠ anti-semion factorization holds as MTCs with h mod 1 and c mod 8 only; used for localization, not for the kill itself.
- **[BOX-4]**: exact real-lift agreement of defects with exponents is arithmetically automatic under the candidate; only the mod-1 agreement is monodromy-forced.
- **[others']**: h_j, c, d_j, fusion truncation, S-matrix, Gauss-sum identity, sum-rule identity, Fibonacci category properties, free-theory sector classifications, parafermion coset weights — all standard imports, each numerically verified above where computable.

Word count: ~1980.

---

## Amendment section

### A.1 Referee verdict (2026-07-27): gate PASSES — K-SU23-1 DOES NOT FIRE (label inversion confirmed and corrected); rescue failed on all four routes

Report preserved verbatim in reviews/REPORTS-phase120-SU23-referee-2026-07-27.md. All modular data, sum rules, channel defects, coset remainders, and lattice arithmetic independently re-derived and confirmed; the rescue mandate executed on four routes. Verdicts:

- **Kill-label inversion CONFIRMED as a semantic error (C-AH1).** Under the registered wording (K-SU23-1 fires IF a free realization exists), the round's finding — no free realization — means **K-SU23-1 DOES NOT FIRE; the gate PASSES** as the program's first genuinely non-abelian AND non-free gate. The verdict of record is hereby corrected; the round's "KILL FIRES" label is superseded. Ledger note (binding, house-rule grade): future verdict boxes must quote the registered kill conditional VERBATIM before ruling — this kill was registered so that firing = gate escalation, not gate success.
- **The non-free substance CONFIRMED after a serious rescue.** All four routes failed: (a) the free-dimension classification is airtight in the corrected form d ∈ ℤ[√2] hence d² ∈ ℤ (C-AH3); φ ∈ ℚ(√5) escapes it; free parafermions/higher-d lattices/W-algebras all excluded from the pinned free class; (b) **the real pressure point — SU(2)₃ DOES embed in a free theory** (diagonal in SU(2)₁³, c = 3, commutant c = 6/5) — but the embedding reading would vacuously "free" EVERY SU(2)_k (including retroactively k = 1, 2), so "admits a free-field realization" is REFEREED-PINNED to isomorphism/MTC-equivalence with matching c mod 8 (C-AH2, binding going forward); a conformal (c-preserving) free embedding is impossible (9/5 ∉ ½ℤ); (c) E₈ stacking cannot help (c mod 8 invariant, dimensions unchanged); (d) non-chiral doubling destroys the invariants under test — irrelevant to the chiral record.
- **K-SU23-2: DOES NOT FIRE (confirmed)** — rates finite, pairwise distinct, pure data; outcome selection properly quarantined; conditional on the underived candidate (GAP-N1), as conceded.
- All structural claims verified: the k = 2 vs k = 3 sum-rule contrast (S = 0 special at k = 2); the Fib ⊠ anti-semion scoping ruled adequate; the parafermion localization (σ₁ weight 1/15 at c = 4/5, the 3-state Potts minimal model — itself φ-bearing and non-free, consistent) endorsed as a genuinely nice structural observation.

### A.2 Corrections ledger

- **C-AH1 (record-critical).** Verdict label corrected: K-SU23-1 DOES NOT FIRE; gate PASSES. Substance unchanged.
- **C-AH2 (binding).** "Admits a free-field realization" pinned to isomorphism/MTC-equivalence (c mod 8 matched); embedding with nontrivial commutant does not count (else vacuous for all SU(2)_k).
- **C-AH3 (precision).** Free-dimension classification restated as d ∈ ℤ[√2] (d² ∈ ℤ) for the pinned free class.
- **C-AH4 (typographical).** Garbled S_{½½} line; value 0.37175 correct; 𝒟S_{½½} = 1 exactly.

### A.3 Post-verdict status

**The SU(2)₃ gate is refereed-PASSED: the program now possesses a genuinely non-abelian, genuinely non-free sector structure**, closing the gap the SU(2)₂ referee named (non-abelian ≠ non-free). Registered: the sector table; the channel-defect spectra {−3ℓ/5, +ℓ/5} and {−4ℓ/5, +2ℓ/5} as candidate data (conditional on GAP-N1 + the pair extension); the nonzero sum rule 𝒟S_{½½} = 1 (the k = 2 phase cancellation refereed as special, not generic); the Fibonacci/parafermion localization of the non-free core; the level-tagged lattice observations under both readings (GAP-N7 untouched, feeding the FORK-1 decision list). The non-abelian program's ladder now reads: k = 1 abelian → k = 2 non-abelian/free → k = 3 non-abelian/non-free — with GAP-N1 (no non-abelian rate DERIVATION) still the load-bearing open problem, now carrying three levels of consistency structure it must eventually explain.
