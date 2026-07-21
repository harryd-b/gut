# Phase 45 — G1–G4 and B3b discharged: one correction, one repair, and two structural finds

*Working session, 2026-07-17. Discharges the audit items G1–G4 (phase 44) and B3b (phase 43) by primary-source verification. This session contains the program's first *caught error in its own derivation* — reported first, per the honesty rules — followed by the repair, and then two finds that materially advance the mechanism (2A) and the sector story: **the stiffness functional is extremal exactly at constant-curvature geometry (Mitsumatsu), and the quantum algebra's superselection center at finite level is literally the classical geometry (Bonahon–Wong / Frohman–Kania-Bartoszynska–Lê).***

---

## 1. G1 — phase 44 §1a was wrong; the correction and the repair

**The error (mine, phase 44).** I claimed the modular flow of the canonical weight on W*(T¹Σ_g, F_ws) *is* the geodesic flow (σ_t = Ad λ(t)). The source audit refuted this on structural grounds: λ(t) ∈ M, so Ad λ(t) is **inner** — and a type III factor's modular flow is never inner (Takesaki VIII.3.14, audited in phase 39). The claim contradicted the very III₁ property the carrier was chosen for. An erratum is now filed in phase 44.

**The correct structure [verified: Takesaki, Acta Math. 131 (1973) Thm 4.5 + TOA II Ch. XII Thm XII.1.1; Kosaki's notes; Moriyoshi–Natsume §4, §8].** The continuous decomposition M = N ⋊_θ ℝ holds exactly as phase 44 §1b intuited: N = the II∞ horocycle (strong-stable) algebra with its Liouville trace, θ = the geodesic flow, trace-scaling (τ∘θ_s = e^{−s}τ), and **III₁ ⟺ N is a factor** — which is why the carrier is III₁. But the modular flow of the dual weight is the action **dual** to geodesic time: σ_t multiplies the contribution of holonomy γ by e^{i t s(γ)}, where s(γ) is the geodesic-time displacement cocycle. **Modular time and geodesic time are conjugate variables, not the same variable.** The geodesic flow lives one level down — as the flow on the core (the noncommutative flow-of-weights level) — and as inner automorphisms of M.

**What survives of the tick–fold link, honestly regraded.** The *identity* is withdrawn; the *scale statement* survives on different, still-solid grounds: (i) the modular generator is the geodesic-displacement operator s/R — its spectrum is geodesic length in curvature-radius units, so **R is still the only scale in the modular structure**, and the conversion 𝒯 must be built from R and c — 𝒯 ∝ R/c is *forced by dimensional uniqueness on the carrier* (the hyperbolic structure has exactly one length; Teichmüller moduli are shape, not scale) [derived-dimensional — weaker than "derived-identity," stronger than the generic ansatz phase 41 had]; (ii) the 2π is now fixed by G3/G4 below: **𝒯 = 2πR/c** in the physical (vacuum-state) normalization. The phase 44 "Planck-hot" tension (§1d) is correspondingly dissolved back into the M1 state-assignment question, where it belongs.

**A precise new remark [speculative, tagged].** Since the modular Hamiltonian's spectrum is the geodesic-length spectrum, modular partition functions on the carrier are Selberg-zeta-type objects: the framework's "energy spectrum of the clock" is the closed-geodesic length spectrum of the hyperbolic surface. Logged as a possible future bridge to spectral/trace-formula methods; no claim attached.

## 2. G2 — confirmed exactly, plus the find: the stiffness is extremal at rigid geometry

The literature value matches the phase 44 frame computation to the letter: **gv(F_ws) = 4π²χ(S)** (Hurder–Katok, Publ. IHÉS 72 (1990), pp. 22–23, verbatim, citing Roussarie; |GV| = 4π²(2g−2) = Vol(T¹Σ) ✓; sign convention-dependent). The quantization claim of phase 44 §1c stands as verified.

**The find — the Mitsumatsu formula [established (others'); Hurder–Katok Thm 3.11]:** for *any* C⁴ negatively curved metric g on S,

> **gv(g) = 4π²χ(S) − Def(g), with Def(g) ≥ 0 and Def(g) = 0 ⟺ g has constant curvature.**

Read as the program must read it: **the Godbillon–Vey functional, over the space of negatively curved metrics, is extremal precisely at the constant-curvature (rigid) geometry.** This is a proven variational characterization in exactly the shape Problem 2A has been seeking since the Tier-2 kickoff ("extremize GV subject to an equilibrium condition"): the stiffness functional *selects* the maximally symmetric, Mostow-rigid-type geometry as its critical point. What 2A still needs is the second half — that the extremality is enforced *dynamically* (a KMS/equilibrium condition making Def(g) = 0 the equilibrium) — but the variational half is no longer a hope; it is a theorem with a name. **The 2A ledger row moves from "no variational principle written" to "variational functional identified and its extremal locus proven; the equilibrium-enforcement half open."** [The interpretive step — Def as the "tension" the equilibrium relaxes — is flagged as ours.]

## 3. G3/G4 — the conformal-net side confirmed; the 2π fixed

All three G3 items verified: interval algebras of chiral nets are the unique hyperfinite III₁ factor (Gabbiani–Fröhlich CMP 155 (1993) Thm 2.13 — **with the honest caveat that hyperfiniteness needs their trace-class/nuclearity hypothesis**, satisfied in standard models; add this to the A2 checklist); Bisognano–Wichmann holds unconditionally for Möbius-covariant nets with the exact form **Δ_I^{it} = U(δ_I(−2πt))** (BGL CMP 156 (1993); GF Thm 2.19); Haag duality on the circle holds (GF Thm 2.19(ii)); and the dilation subgroup fixing ∂I is geometrically the hyperbolic translation along the geodesic subtending I — so the net-side statement "interval modular flow = translation along the subtending geodesic" is confirmed as written, *with* its 2π. **G4 is thereby resolved: the physical (vacuum-state) conversion is 𝒯 = 2πR/c** — one modular tick winds 2π of geodesic-translation parameter. The weight-side convention of §1 differs precisely by the state/weight distinction, now cleanly separated.

**[RE-TAG, 2026-07-18, fresh red team FR-5 (phase 74)]:** the fresh Track O referee's objection is accepted: the 2π above belongs to interval algebras of Möbius-covariant nets *with vacuum* (BGL/GF, as cited) — but the compact carrier has no vacuum state and no Möbius covariance, and the boundary net where BW holds is the *unquotiented* net; Γ-invariance destroys the covariance the transport needs. **"Resolved" is therefore downgraded: 𝒯 = 2πR/c is [convention, borrowed from the boundary/vacuum setting] — a consistent normalization choice, not a derivation — until the boundary-to-carrier transport is actually constructed (a named gap, T-2π). The dimensional statement 𝒯 ∝ R/c (§1) is unaffected.**

## 4. B3b — resolved, and it is the sector story

The roots-of-unity structure of the skein algebra is not an obstruction to the framework's superselection reading — it **is** the framework's superselection reading, by theorem:

- **Chebyshev–Frobenius [Bonahon–Wong, Invent. Math. 204 (2016)]:** at a root of unity ζ, the *classical* skein algebra — the coordinate ring of the SL(2,ℂ) character variety (Bullock; Przytycki–Sikora) — embeds into the **center** of K_ζ(Σ).
- **Unicity [Frohman–Kania-Bartoszynska–Lê, Invent. Math. 215 (2019)]:** K_ζ(Σ) is finite-rank over its center (Thm 5.1); the center is the Chebyshev–Frobenius image extended by peripheral elements (Thm 4.1); and irreducible representations are classified, generically uniquely, by their **classical shadow** — a point of the classical character variety (Zariski-dense Azumaya locus; finite multiplicity outside it).

Physics reading [ours, interpretation, but now riding on theorems]: **at finite level, the quantum algebra's superselection parameters are classical geometric data — flat-connection/holonomy points.** The classical world does not disappear inside the quantum algebra; it survives as the center, i.e., as exactly the label set of superselection sectors. This is the same shape as the program's phase-5 "charge quantization from topology" story, now with the correct mathematical carrier: **sectors = classical shadows.** Combined with phase 43's B3 corollary, the chain now reads: finite census (Bradlow) ⟶ finite level ⟶ discrete scale (Goldman integrality) ⟶ central/classical sector labels (Chebyshev–Frobenius) — one coherent structure, every link either theorem or a single flagged identification (finite census = finite level, still the open pivot, renamed **B3c**). Caveats carried verbatim from the audit: "generically" is load-bearing; peripheral data extends the label set; SL(2,ℂ), not PSL.

## 5. Ledger and critical path

- **Withdrawn:** phase 44 §1a (modular = geodesic identity). **Retained, regraded:** tick–fold as unique-scale forcing, 𝒯 = 2πR/c [derived-dimensional + G3-fixed normalization].
- **2A (the mechanism):** major advance — the variational functional and its extremal locus are now theorems (Mitsumatsu); open half: the equilibrium-enforcement (KMS ⟹ Def = 0). This is the sharpest formulation 2A has ever had, and it is the natural next hard target.
- **B3b closed; B3c opened** (finite census = finite level): a concrete, decidable pivot.
- **A2 checklist amended:** add the nuclearity hypothesis to row 3 (it is exactly the split-property row — the conformal net satisfies it in standard models).
- Audit meta-note: the G1 catch is the process working — the program's first self-correction of an in-room derivation at the source-audit stage, before it reached any outward document.

*Status line: one error caught and repaired with the scale conclusion surviving in honest, weaker form (𝒯 = 2πR/c); the stiffness-extremality theorem gives 2A its variational half for free; and the sector story acquires a theorem-backed core — the classical world as the center of the quantum algebra. Critical path: the 2A equilibrium half (KMS ⟹ constant curvature), B3c, and the Γ-twisted net verification.*
