# Phase 30 — Gravisolitons: the geometric dark sector meets the constructive core

*Working session, 2026-07-11. Source: Asselmeyer-Maluga & Król, "Dark Matter as gravitational solitons in the weak field limit," arXiv:2012.05358 (read in full; also Ch. 7.6 of the 2025 book). This session (i) catalogs what the paper establishes, (ii) upgrades ledger item P4, and (iii) records a new on-framework conjecture joining the dark sector to the monopole-Floer core of §5 — the first place the program's mathematics touches its phenomenology.*

---

## 1. What the paper establishes (AMK's, to credit)

- **Gravisolitons**: dark matter modeled (partly) as gravitational solitons of the weak-field Einstein equations for the Einstein–Rosen-type metric ds² = f(t,z)(dz²−dt²) + g_ab dx^a dx^b with *non-diagonal* 2-metric g_ab; via inverse scattering the invariant reduction is the **sine-Gordon equation**, solitons carry topological charge ±1 (gravisoliton 𝒮 / anti-gravisoliton 𝒜); 𝒮𝒮/𝒜𝒜 scatter repulsively, 𝒮𝒜 attractively (breathers); 2-gravisolitons on Minkowski background are equivalent to Kerr–NUT/Schwarzschild.
- **Existence condition = Plank IV's object**: the spatial 3-manifold must admit a codim-1 foliation with **GV ≠ 0** (Thurston/PSL(2,ℝ) type; the non-orthogonal frame forces the non-diagonal g_ab; local form η∧dη = κ²(τ + l_T(N,Z))ω∧η∧ξ). det(g_ab) = const is supplied by **Mostow rigidity** of the hyperbolic pieces.
- **Generation mechanism**: couple a spinor to the 1-form η read as a U(1) gauge field; the **Dirac–Chern–Simons functional** S_DCS = ∫(ψ̄D_η^Σψ + η∧dη) has critical points **D_η^Σψ = 0, dη = τ(ψ,ψ)** and its gradient flow "is equivalent to the Seiberg–Witten equations for Σ×I" (via Morgan–Szabó–Taubes); nontrivial solutions (ψ≠0, η≠0) ⟺ nontrivial GV ⟺ a gravisoliton is generated; necessary condition for exotic smoothness of the 4-spacetime.
- **Observational content**: lensing profile ρ ∼ 1/r² (singular isothermal sphere — indistinguishable from matter by lensing, deflection δ = 4πσ²); equation of state **w_DM = 0 exactly, at all epochs** (Mostow rigidity fixes the soliton volume ⇒ ρ ∼ a⁻³) — consistent with Sartoris et al. 2014 and Kopp et al. PRL 2018 (w = 0 across eight redshift bins, z = 10⁵ → 0); **conjectured discriminator: circular polarization of gravitationally lensed light** (the foliation carries torsion); DM spatial distribution predicted **fractal**; no non-gravitational couplings.

## 2. Ledger upgrade — P4 (geometric dark matter), from bare null to prediction set

P4 previously: "permanent non-gravitational null; weak, degenerate." Now four components, in decreasing strength:

- **P4a [forced, tested, ongoing]: w_DM = 0.000 exactly, at every epoch.** Same Mostow-rigidity logic as P1's w_DE = −1 — no adjustable parameter. Already tested (Kopp et al. 2018: consistent); every future tightening (DESI/Euclid growth + lensing tomography) is a test. **Falsification: any confirmed epoch-dependence or w_DM ≠ 0.** (Weakly distinctive vs CDM, which also sits at w = 0 — but *forced* here, and jointly with P1 the framework requires the rigid pair (w_DE, w_DM) = (−1, 0) with zero freedom: one combined falsification target.)
- **P4b [AMK conjecture; distinctive]: circular polarization of lensed light.** Particle DM produces none; the torsion-carrying foliation should. Testable with radio/optical polarimetry of strongly lensed images (cluster arcs, lensed quasars, lensed FRBs). Needs a quantitative estimate before it is a sharp number — flagged as the natural companion to the κ-from-GV target.
- **P4c [AMK, forthcoming claim]: fractal DM distribution** — small-scale structure signature; degenerate with other small-scale physics but stackable with P4b.
- **P4d [null, retained]: no non-gravitational detection, ever** — unchanged.

Scattering phenomenology (𝒮𝒮 repulsive, 𝒮𝒜 attractive) may interface with self-interacting-DM constraints (Bullet-Cluster-type); no cross-section is computed in the paper — logged as open.

## 3. NEW [conjecture, this program]: the dark sector = the reduced monopole Floer sector

The join AMK does not make (he never mentions Floer homology; the SW equivalence is used only as a PDE fact): his critical-point system **is the Chern–Simons–Dirac functional of monopole Floer theory** — the very functional whose Morse homology is HM(Σ) (§5). His gravisoliton-existence condition — a nontrivial (irreducible: ψ ≠ 0) solution — is the existence of an irreducible critical point. Therefore, at the level of the protected content:

> **Conjecture (dark-sector dictionary).** Gravisoliton-carrying universes are exactly those with HM_red(Σ) ≠ 0; the protected dark-sector content per flux sector is HM_red(Σ,𝔰), and the internal dictionary's clause "irreducibles = charged-matter bound states" acquires the physical face "irreducibles = gravisolitons = dark matter."

Immediate consequences, all computable (phase 28 table):

| Σ | HM_red rank | dark-sector verdict |
|---|---|---|
| S³, Σ(2,3,5) (PSC homology spheres) | 0 | **no gravisolitons — dark-matter-free universes** |
| Σ(2,3,7), Σ(2,3,11) | 1 | one protected gravisoliton class |
| Σ(2,3,13) | 2 | two |
| S¹×Σ_g, sector k | rank H*(Sym^{g−1−|k|}Σ) | graded gravisoliton content, **Bradlow-truncated** (only finitely many flux sectors carry dark matter) |

Consistency checks that make this non-vacuous: (i) PSC ⟹ no irreducible SW solutions (Weitzenböck) ⟹ AMK's mechanism yields nothing — the two sides agree on the empty case for free; (ii) the phase-28 parity-purity theorem now says all protected gravisoliton classes in a Seifert universe carry uniform statistics; (iii) the Gauss-law/Bradlow structure of phase 28 gives the dark sector a *finite flux budget* when b₁ > 0. Caveats, stated: AMK's construction is weak-field and on Σ×I with translational invariance (HM counts flow lines of the same functional, but the identification of *homology classes* with *stable solitons* needs an argument — the natural route is via the phase-15/16 localization); the conjecture inherits every open item of §5's bridge; and the abundance map (rank → Ω_DM) needs the modulus-to-density conversion that phase 25 flagged as the T2 dependency.

**Why this matters for the program's shape:** this is the first point where the constructive core (§5) *produces phenomenology* rather than consistency — the same HM_red that phase 28 computed now candidate-counts the dark sector, and P4a/P4b give it observational teeth. It also strengthens claim (b)'s outreach story: the Floer↔DHR join is not bare mathematics; it carries the dark sector on its reduced part.

## 4. Document updates applied

- phase27 P4 row replaced by P4a–P4d above; the "one live handle" summary now reads *two rigid targets* (w_DE, w_DM) = (−1, 0) plus one conditional (κ) and one distinctive conjecture (P4b).
- CORE §8B geometric-DM row upgraded correspondingly; §5 internal dictionary gains the dark-sector face with credit to arXiv:2012.05358 and the conjecture tagged as this program's.
- Scholarship note: the gravisoliton mechanism, w = 0, and circular-polarization conjecture are AMK's; the HM_red join is unclaimed anywhere per the phase-29 sweep ("Floer" + "superselection"/"dark matter" both empty) and becomes part of candidate-novel claim (b)'s scope.
