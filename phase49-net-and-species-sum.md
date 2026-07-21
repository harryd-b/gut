# Phase 49 — The Γ-twisted net advanced, and the species sum computed: a near-cancellation and a new constraint

*Working session, 2026-07-17. Opens the two remaining critical-path fronts. §1 advances the Γ-twisted net (join rows 2–5) by inheritance arguments and finds that the net's duality violations realize exactly the π₁-sector structure CORE §2.3 predicted — with one honest wildness flag. §2 computes the species sum with source-verified coefficients and finds: **the Standard Model's signed entanglement sum is +1 — a near-perfect cancellation** — which simultaneously (i) fixes the fold at essentially the Planck scale, (ii) forbids the framework from generating M_P at a low cutoff, and (iii) yields a new, distinctive, particle-content constraint: **induced-gravity positivity**, which the SM barely satisfies and which minimal SU(5) violates. One scheme correction to phase 44 is logged.*

---

## 1. The Γ-twisted net (join rows 2–5)

**Construction.** A Möbius-covariant chiral net {A(I)} on S¹ = ∂H² carries a unitary representation of all of PSL(2,ℝ) ⊃ Γ = π₁(Σ_g). The Γ-twisted object is not a net on a quotient (Γ acts minimally on S¹ — there is no Hausdorff quotient); it is the **same local net with the enlarged global algebra** M_Γ = (global chiral algebra) ∨ {U(γ) : γ ∈ Γ} — the crossed product by the discrete subgroup, whose vacuum survives (Möbius-invariant ⟹ Γ-invariant).

**Rows, assessed:**

- **Row 2 (isotony, locality): PASS by inheritance** — the local algebras are unchanged; only the global algebra grows. [derived]
- **Row 3 (split/nuclearity): PASS by inheritance** — local conditions on the unchanged A(I), granted the Gabbiani–Fröhlich trace-class hypothesis (standard models). [derived, conditional as before]
- **Row 4 (Haag-duality pattern): the right *shape* of failure.** In M_Γ, interval duality fails — the commutant of A(I) acquires contributions from the Γ-unitaries. The violation is *by the fundamental group*: precisely the topological mechanism the framework requires (CORE §2.1/§2.3 — duality violations on topologically nontrivial data as the source of sectors). Moreover the twist sectors of a crossed product/orbifold pair are labeled by Γ-data (conjugacy classes / representations, by DR-type covariant sector theory) — **the candidate net realizes CORE §2.3's "Aharonov–Bohm sectors = representations of π₁" concretely.** [derived-structural; the precise orbifold-DHR analysis is logged as **J1** — with the honest wildness flag: Γ is ICC (good: M_Γ is a factor) but **not type I**, so its full representation theory is wild; the physical expectation is that the *protected/finite-index* part of the sector structure is the tame, meaningful piece, exactly parallel to the protected-stratum philosophy. The G1 lesson applies: these crossed-product statements are structurally forced but must be transcribed and checked — J1 is now the top item of the specialist packet.]
- **Row 5 (covariance): PASSED** already (phase 44 §3 — interval modular flows = geodesic translations, verbatim verified in phase 45).

**Net status: the toy join is four-fifths verified, and its one open row (4/J1) fails in exactly the way the framework needs it to.**

## 2. The species sum [coefficients verified against primary sources]

**The verified scheme** (Solodukhin LRR eq. 28; Kabat NPB 453; consistency with 1/G-renormalization per Calmet–Hsu–Reeb; the Susskind–Uglum "S = A/4G_ren" consensus confirmed via Cooperman–Luty + Larsen–Wilczek + Donnelly–Wall): in the heat-kernel/conical scheme, S_div = (A/48πε²)·c_total with per-species weights **+1 (real minimal scalar), +1 (Weyl fermion), −4 (vector, Kabat contact term included — now understood as physical edge-mode structure, Donnelly–Wall)**. Graviton: no settled number — flagged **J2**. *Scheme correction to phase 44 §2: the 1/(360π) brick-wall coefficient used there is a different (proper-distance) scheme; the heat-kernel scheme above is the one that matches the renormalization of 1/G. Phase 44's structural conclusions (η ∝ ℓ_tr⁻², induced-gravity classification) are unaffected; its O(1) illustration numbers are superseded by the ones below.*

**The Standard Model arithmetic.**

> c_SM = N₀ + N_{1/2} − 4N₁ = 4 + 45 − 4·12 = **+1** (minimal SM); **+4** with three right-handed neutrinos.

**A near-perfect cancellation** — the signed sum of 118 degrees of freedom is one. Three consequences, in decreasing solidity:

1. **The fold is Planckian, with no wiggle room [derived, conditional on the Sakharov reading].** 1/G = c_total/(12π ℓ_tr²) ⟹ ℓ_tr = √(c/12π)·ℓ_P ≈ 0.16 ℓ_P (c = 1) to 0.33 ℓ_P (c = 4). The framework *cannot* generate M_P from a lower cutoff — a species sum of order one is the mathematical death of any "gravity is weak because of many species" reading within this framework, and the confirmation of phase 44's R ~ ℓ_P from an independent direction. (Dvali's N-species bound uses the *unsigned* count and answers a different question — the two must not be conflated; noted per the audit.)
2. **A new constraint — induced-gravity positivity [derived, conditional; candidate ledger entry P7].** The framework requires **c_total > 0** for the matter content living at the fold scale — otherwise induced G is negative and the framework is inconsistent. The SM satisfies this *barely* (+1), and right-handed neutrinos *improve* it (+4) — the first time the framework has had anything to say about particle content. Discriminating power is real: **minimal SU(5)** (24 vectors, 45 Weyl fermions, ~34 real scalars) gives c ≈ 34 + 45 − 96 = **−17 < 0** — inconsistent with the framework as matter-at-the-fold; vector-rich spectra generally are. [Honest boundaries: one-loop; graviton entry unsettled (J2); non-minimal scalar couplings shift weights; scalar-sector choices can rescue GUTs (e.g. SO(10) with large Higgs content comes out positive) — so this is a *constraint surface*, not a one-line exclusion. And the whole item is conditional on the framework's Sakharov reading, which is conditional on V.7.]
3. **The marginality is itself interesting [observation only].** c_SM = +1: the observed particle content sits just above the consistency boundary. The record notes this without attaching a claim — the B3c lesson about striking-looking numbers is one day old.

## 3. Ledger

- Join: rows 2, 3, 5 passed; row 4 = **J1** (orbifold-DHR for the Γ-twist, wildness flag), now the specialist packet's lead item alongside H6b/H5b.
- Scale: fold pinned at ~(0.2–0.3)ℓ_P; phase 44 scheme note filed.
- **P7 (candidate): induced-gravity positivity** — a distinctive, falsifiable-by-particle-content constraint; SM passes at +1, ν_R-extended SM at +4, minimal SU(5) fails. To be run past the J2/non-minimal-coupling caveats before entering the prediction ledger proper.
- Critical path now: J1 (specialist), J2 (graviton entry), and the standing expert packet. **In-room, the program has — for the first time since the kickoff — no obvious next computation that doesn't route through a specialist check.** That is itself a milestone: the in-room frontier is exhausted honestly rather than padded.

*Status line: the toy join stands at four-fifths with its open fifth failing in the framework's favor; the species sum turns the induced-gravity reading quantitative and yields the program's first particle-content constraint — the SM passing by one unit — while pinning the fold at the Planck scale and closing the low-cutoff escape. The in-room program is, for now, complete: what remains needs either a specialist (J1, H6b, H5b, E1/E2 residues), a theorem the world hasn't proven (Katok), or the sky (Euclid).*
