# Phase 27 — The prediction ledger: what this framework tells the experiments

*Working session, 2026-07-11. Goal: extract every experimentally decidable statement the framework makes — forced, not fitted — each with a falsification criterion and a decision date. Ground rules inherited from the §8B audits: no fitted relation presented as a prediction; conditional predictions labeled with exactly what they are conditional on; null predictions count (they are falsifiable) but are graded honestly as nulls. Status tags as in the core document.*

---

## 0. What kind of predictor this framework is

After the 2026-07-11 review, the honest starting point: every *rigorous* result lives on the protected stratum and is SUSY/holomorphy-protected; the distinctive physics (Plank IV) is conjecture. So the framework's predictions divide into three classes:

- **Class A — forced now**: statements the framework cannot avoid making, decidable by running or imminent experiments.
- **Class B — conditional**: statements inherited if (and only if) a named open item is established; the condition is part of the prediction.
- **Class C — mathematical**: computations (not experiments) that would confirm or kill parts of the constructive core, decidable by a Floer theorist at a desk.

---

## 1. P1 [Class A] — Dark energy is exactly rigid: w₀ = −1.000, wₐ = 0.000

**Statement.** The cosmological-constant sector rides on Mostow rigidity: a hyperbolic 3-geometry admits no continuous deformation, so the dark-energy equation of state cannot evolve. The framework requires **w(z) = −1 identically** — not approximately, not on average: w₀ = −1, wₐ = 0.

**Status.** [conjecture at the mechanism level (AMK channel, phase 24); but the *rigidity* of the prediction is forced — there is no parameter to adjust. This is the framework's one live, unconditional, near-term handle (§8B).]

**Current tension.** DESI DR2 + CMB + SNe prefer *evolving* dark energy at up to ~4.2σ (combination-dependent; BAO+CMB alone ~3σ), with best-fit (w₀, wₐ) far from (−1, 0). If that preference is physical, this prediction is already dying.

**Decision.** Euclid DR1 (late 2026) + DESI full-survey cosmology (2027–28) + next-generation SNe compilations. **Falsification criterion:** combined, systematics-cross-checked evidence for (w₀, wₐ) ≠ (−1, 0) at ≥5σ kills the Mostow/exotic-cosmology channel outright. **Survival scenario:** if the DR2 preference collapses under Euclid cross-checks (SNe-calibration or BAO systematics), the channel survives and gains credit as the only framework here that *required* rigidity while the field entertained evolution.

**What it kills / doesn't.** Falsification kills the cosmological (AMK-side) sector, not the sector/HM constructive core.

---

## 2. P2 [Class A] — Gravitational waves: four zero-anomaly commitments

**Statement.** Plank IV's stiffness is topological (GV class — metric-blind, non-dissipative), and the reconciliation of §4.1 fixes spacetime's strain modulus at exactly zero and its curvature modulus at c⁴/16πG. This forces four propagation nulls, at all frequencies and distances:

1. **No anomalous damping**: GW amplitude falls exactly as GR's 1/d_L; a topological stiffness cannot absorb wave energy. (Contrast: any mechanical modulus Y dissipates E_d ∝ Y·h²·Δz — Melissinos eq. 14; current implicit bound Y < 2.5×10⁻¹⁷ c²f²/G from GW150914's ~400 Mpc propagation. We predict the effective Y_strain is not small but **zero**; improved bounds will tighten forever and never find a floor.)
2. **No dispersion**: ω = ck exactly; no frequency-dependent arrival times in multiband (LISA-band inspiral → LVK-band merger) observations of the same source.
3. **No birefringence**: both tensor polarizations propagate identically.
4. **Exactly two tensor polarizations** — shared with GR and with the program's own §8A torsion verdict (torsion-type theories add modes).

**Status.** [forced by the topological-stiffness reading; shared with GR (not a unique fingerprint), but *discriminating within the "spacetime as material" model class*: mechanical/elastic-spacetime programs (Tenev–Horstemeyer-type) naturally sit at nonzero moduli, and this framework is on the opposite side of that divide.]

**Decision.** LVK O5 (running), next-generation detectors, LISA (2030s) for multiband dispersion. **Falsification criterion:** any confirmed anomalous damping, dispersion, birefringence, or extra polarization kills the topological-stiffness reading of Plank IV (and would simultaneously *support* a mechanical-modulus reading — the two readings are now experimentally distinguishable, which is new).

---

## 3. P3 [Class A, derived here] — Sorkin triple-path interference: κ is unobservably small, so every current test must return null

**The in-room derivation.** Suppose the conditional route of §8B is eventually established: topology change induces a Born-rule nonlinearity of BHMM type, H_ψ = H + gψ. What size is κ? The nonlinearity's origin in this framework is *gravitational* (topology change of the geometry), so its dimensionless strength for a system probing energy E is set by the gravitational hierarchy. The most optimistic (least suppressed) estimate is first order in the ratio to the Planck energy:

  κ ~ E / E_P, with E_P ≈ 1.22 × 10²⁸ eV.

Platform by platform:

| Platform | Probe energy E | κ predicted (optimistic) | Current/planned sensitivity |
|---|---|---|---|
| Optical triple-slit (Sinha-type) | ~1.5 eV | ~10⁻²⁸ | ~10⁻² (achieved) |
| Liquid-state NMR (Park-type) | ~10⁻⁶ eV | ~10⁻³⁴ | ~3×10⁻³ (achieved) |
| Reactor ν's at JUNO (running, first data 2026) | ~4 MeV | ~3×10⁻²² | ~10⁻² level on κ-analogue |
| Optical-clock α (redshift anomaly) | — | same suppression | ~10⁻⁵ (achieved) |

Second-order suppression ((E/E_P)²), or Schrödinger–Newton-type estimates (Gm²/ħRc for the actual masses and separations involved), land *far lower still*. Even the most optimistic version sits **16+ orders of magnitude below every current and planned sensitivity**.

**Statement.** The framework — in *any* version in which the would-be nonlinearity has gravitational/topology-change origin — predicts **I₃ = 0 and α = 0 within errors in every currently feasible experiment**: JUNO's triple-path analogue, Pleinert-type multi-slit photonics, atom interferometry, optical-lattice clocks.

**Status.** [derived, conditional only on the gravitational origin of the nonlinearity — which is the framework's own premise. Loophole, stated: only a mechanism converting the dimensionless GV modulus into an O(1) *unsuppressed* prefactor could evade this; nothing in the program supplies one, and any proposal that did would need to explain why gravity's hierarchy doesn't apply to it.]

**Decision & falsification.** Running now (JUNO taking data; first oscillation results published 2026; photonic bounds standing). **Falsification criterion:** a confirmed detection of κ ≳ 10⁻⁶ at any platform falsifies this framework's gravitationally suppressed nonlinearity — in *either* version (with or without the conditional mechanism) — while supporting the unsuppressed corner of the nonlinear-QG class. Note the flip from the pre-review framing: detection at current sensitivities would now count *against* this framework, not for it.

---

## 4. P4 [Class A + B] — Dark matter as gravisolitons: four components (upgraded, phase 30)

Source: AMK arXiv:2012.05358 (gravisoliton mechanism — theirs) + the phase-30 HM_red join (ours).

- **P4a [forced, tested, ongoing]: w_DM = 0.000 exactly, at every epoch** — Mostow rigidity fixes the soliton volume (ρ ∼ a⁻³), zero free parameters; consistent with Kopp et al. PRL 2018 (eight redshift bins, z = 10⁵→0); every future lensing/growth tomography tightening is a test. Jointly with P1 the framework demands the rigid pair **(w_DE, w_DM) = (−1, 0)** — one combined falsification target. Falsified by any confirmed w_DM ≠ 0 or epoch-dependence.
- **P4b [AMK conjecture; distinctive vs particle DM]: circular polarization of gravitationally lensed light** (torsion-carrying foliation). Testable by polarimetry of lensed quasars/arcs/FRBs; needs a quantitative estimate — companion target to κ-from-GV.
- **P4c [AMK claim]: fractal DM spatial distribution** — stackable small-scale signature.
- **P4d [null, retained]: no non-gravitational detection, ever.** LZ/XENONnT/PandaX running; falsified by any confirmed non-gravitational detection.

**New on-framework conjecture (phase 30):** the dark sector *is* the reduced monopole Floer sector — gravisoliton existence = irreducible critical points of the Chern–Simons–Dirac functional = HM_red(Σ) ≠ 0, so PSC homology-sphere universes (S³, Σ(2,3,5)) are dark-matter-free, Σ(2,3,7) carries one protected class, Σ(2,3,13) two, and S¹×Σ_g has a Bradlow-truncated dark flux budget. First contact between the §5 constructive core and phenomenology; inherits the §5 bridge caveats.

---

## 5. P5 [Class B] — Conditional inheritances, with the condition named

**5a. From the Chishtie bridge (CORE §6 item 5).** *Condition:* the modular engine reproduces a loop-style kinetic coefficient with threshold structure. First consistency check, done here: Chishtie's A_ren = [V‴]²/(32π²[V″]²)·ln(V″/μ²) has dimensions of length² (V‴ ~ M, V″ ~ M², so [A] = M⁻²), and his threshold is A ≥ 1/M_P² = ℓ_P². Writing the modular-side ansatz A ~ GV·ℓ_tr² (GV dimensionless, ℓ_tr the foliation's transverse scale), the threshold becomes **GV ≥ (ℓ_P/ℓ_tr)²** — for Planckian folding (ℓ_tr ~ ℓ_P) this is GV ≳ 1, consistent with Plank IV's "any nonzero fold" up to O(1). **The dimensional bridge passes** [interpretation; necessary-not-sufficient]. *If* the full identification is established, the framework inherits Chishtie's sharp handles: **f_NL^local ∈ [0.8, 2.5]** (CMB-S4, 2030s; σ ~ 1) and a **LISA-band stochastic GW background** (Ω_GW h² ~ 10⁻⁶ at f ~ 10⁻⁴ Hz; LISA, mid-2030s). Falsifiable both ways once the condition is met; meaningless before.

**5b. From T1-core (CORE §6 item 1).** *Condition:* the GV → modular-flow → first-law chain is established. *Then* the framework predicts the Einstein equations *with a computable Newton constant* — G derived from the GV/modular data rather than measured (§4.1(iii)). The check would be parameter-free: the derived G must equal the measured G. This is the framework's highest-value potential prediction and is exactly what T1-core gates.

**5c. The Φ(Λ, m_H) = 0 relation (CORE §6 item 2).** *Condition:* AMK's Λ- and m_H-formulas recomputed from stated hypotheses (phase 25 dependency), eliminating the shared GV modulus. *Then* a parameter-free relation between two measured numbers — the cleanest possible test. Currently blocked on the recomputation; do not quote any AMK numbers until then.

---

## 6. P6 [Class C] — Mathematical predictions, decidable at a desk

These are predictions in the precise sense that a computation nobody has done could refute the framework. **All three were run on 2026-07-11 — see phase 28 for the full session.** Results:

1. **Σ_g × S¹ (the b₁ > 0 decider) — label level PASSED.** First multi-sector confirmation: for 0 < |k| ≤ g−1 the sectors carry distinct nonzero protected content H*(Sym^{g−1−|k|}Σ_g) (Muñoz–Wang). Two new structures logged: adjunction/Bradlow truncation (only finitely many flux sectors carry protected content) and Jacobian dressing + 2-torsion in the k = 0 sector (Jabuka–Mark) — the dictionary's k = 0 clause must be rebuilt around them. The b₁ > 0 OS-positivity bridge stays open and is now *provably* in need of a new mechanism (parity purity fails there by computation).
2. **The statistics clause — consistent; quantitative prediction issued.** On all Seifert ℤHS³ the protected content is parity-pure (theorem), so statistics are uniform per universe — safe axis. Discriminating arena located: on S¹×Σ_g the clause predicts fermionic multiplicity = b_odd(Sym^{g−1−|k|}Σ_g) per sector — a finite, auditable computation.
3. **The no-cancellation guard — PASSED, upgraded to a theorem.** OS math/0203265 Cor 1.4 gives parity purity for the entire Seifert class; the case-by-case requirement is deleted. Explicit deciders: Σ(2,3,11) (d = −2, HF_red rank 1, even), Σ(2,3,13) (d = 0, rank 2, even) — derived in phase 28 with Casson/instanton cross-checks.

**Standing:** the constructive core survived its cheapest decisive tests, gaining one theorem, one quantitative prediction, and two structural constraints. The gate to the §6.4 expert conversations is now open from the mathematics side.

---

## 7. The decision calendar

| When | What reports | Which prediction | Kill condition |
|---|---|---|---|
| **Now (running)** | JUNO (ν data live), LVK O5, LZ/XENONnT | P3 (κ null), P2 (GW nulls), P4 (DM null) | any κ ≳ 10⁻⁶ detection; any GW propagation anomaly; any non-grav DM detection |
| **Late 2026** | **Euclid DR1** | **P1 (w = −1)** — first big cross-check of the DESI evolving-DE preference | ≥5σ combined (w₀,wₐ) ≠ (−1,0) |
| 2027–28 | DESI full-survey cosmology | P1, decisively | same |
| Any time (desk) | Floer computations | P6 (three math tests) | any mismatch |
| 2030s | CMB-S4 | P5a f_NL (conditional) | condition first |
| Mid-2030s | LISA | P2 (multiband dispersion), P5a SGWB (conditional) | anomaly / condition first |

**The honest headline:** the framework makes **one unconditional prediction under active fire right now (P1)**, four zero-anomaly commitments that are cheap to state and impossible to walk back (P2), one derived null with real falsification power (P3), and three desk-decidable mathematical tests (P6) that should be run before the expert outreach. Everything sharper is Class B, and each Class-B item names its gate. The single highest-leverage move remains T1-core (5b): it converts the framework from "consistent with G" to "computes G."

---

*Cross-references: CORE §4.1 (reconciliation), §6 items 1–5 (gates), §8B (audit rows this ledger sharpens), §8C (Chishtie comparison). Sources for experimental status: DESI DR2 papers (2025–26); Euclid DR1 timeline (ESA, late 2026); JUNO first oscillation results (Nature, 2026); LVK polarization/dispersion bounds; Melissinos arXiv:1806.01133 for the GW-damping bound form.*

---

## 8. P1 contingency — PRE-REGISTERED 2026-07-11, before Euclid DR1

**If evolving dark energy is confirmed** (≥5σ, systematics-robust, DESI-full + Euclid + SNe): the Mostow dark-energy channel dies (the Λ-as-rigid-curvature identification, AMK-side import) and the "rigid pair" framing of P1+P4a dies with it. **Survives independently:** P4a (w_DM = 0 — separate application of Mostow to soliton volumes; the same Euclid data tightens its test), P4b–d, P2, P3, the entire constructive core, all five derived benchmarks, and claims (a)/(b) — none touch cosmology.

**Pre-registered successor prediction (Plan B, forced by the framework's own logic — logged now so it cannot be a post-hoc rescue):** Mostow rigidity permits w to change *only through discrete topology transitions, never smoothly*. Therefore, IF dark energy evolves, the geometric channel requires **w(z) piecewise-constant — a step function with jumps at transition epochs — not a smooth thawing/freezing (w₀, wₐ) track.** Discrimination: smooth evolution (a genuine quintessence-like track fitting w₀–wₐ better than steps) kills the geometric channel outright and permanently; step-like evolution supports topology-change cosmology against quintessence. Note the standard (w₀, wₐ) parametrization cannot distinguish these — the test needs non-parametric/binned w(z) reconstructions, which DESI-full and Euclid both enable. Either outcome is informative; there is no third reading under which the channel survives smooth evolution.

**Standing rule:** if P1 falls, the experimental face reorganizes around P4 (primary), P2/P3 (nulls), and the desk program; the outreach spine (claim (b), the five benchmarks, T1) is unaffected, and no document rewriting is required beyond status lines — this ledger was built for exactly this event.
