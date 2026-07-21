# Phase 51 — T-M1 executed: the shape of the moduli potential, and the derived w(z) class

*Working session, 2026-07-17. Executes T-M1 (phase 50) at single-scalar-model level, on source-verified inputs (K1–K4, all confirmed this session). Result: **the moduli potential is provably non-flat — regime 1 is excluded — and its shape is determined: a maximum at the maximally symmetric surface, descending to −∞ at the pinching boundaries, which sit at finite Weil–Petersson distance.** Under the coupling gap (still open, still the load-bearing conjecture), the derived cosmological class is **hilltop/thawing quintessence starting at w = −1 and terminating in a topology-change step** — and the three testable structural commitments this implies are pre-stated in §5, before any DR1 reconstruction exists. Per the phase 50 protocol, this earns the moduli route candidate-successor status; it revises nothing on the scoreboard.*

---

## 1. Verified inputs [all [verified-source] this session]

- **K1 (Zograf–Takhtajan / D'Hoker–Phong):** c₁(λ₀, Quillen) = +(1/12π²)·ω_WP; equivalently i∂∂̄ log(det′Δ₀/det Im Ω) = +(1/6π)·ω_WP — the Quillen potential is strictly plurisubharmonic. (Caveat kept: the *bare* log det′Δ₀ differs by the Hodge term and is not sign-definite — which is exactly what permits its interior maximum.)
- **K2 (pinching asymptotics):** as a geodesic pinches, det′Δ₀ → 0 with log det′Δ₀ ≈ −π²/(6ℓ) per pinched curve (convention flagged; π²/3ℓ oriented). One dissenting secondary paraphrase exists and is assessed as misattributed; the Selberg-zeta route is decisive. [load-bearing sign — double-checked via independent rederivation from the Euler-factor asymptotics]
- **K3 (extremal determinants):** Osgood–Phillips–Sarnak: within a conformal class, constant curvature *maximizes* det′Δ. Over moduli space (genus 2, Strohmaier–Uski numerics): det′Δ₀ ≈ 4.723 at the Bolza surface, the conjectured global maximum; symmetric surfaces are automatic critical points; det′Δ₀ extends continuously to the compactification boundary with value 0.
- **K4 (WP geometry):** Kähler (Ahlfors); geodesically incomplete with the pinching boundary at *finite distance* (Wolpert; Chu; completion Masur); sectional curvature negative (Wolpert; Tromba).

## 2. The potential's shape [derived, scalar model]

Take the one-loop free energy of a single scalar on the fold as the model potential on moduli space: V(τ) = +½ log det′Δ₀(τ) (additive constants and overall normalization deferred to the coupling gap). Then:

1. **V is not flat — regime 1 of phase 50 is excluded, outright.** Proof at a glance: det′Δ₀ = 4.723 at Bolza and 0 on the boundary — the function is nonconstant; K1 supplies the refined statement (definite Quillen Hessian ∝ ω_WP). **The framework cannot rederive exact w = −1 from flat moduli: whatever the fold's moduli do, they feel a force.**
2. **The shape:** V has its **maximum at the maximally symmetric surface** (K3), descends monotonically-in-effect toward every boundary, and **diverges to −∞ at pinching** (K2), which lies at **finite WP distance** (K4). A hilltop whose every downhill direction ends, after finite field-range, in a wall over the abyss — where "the abyss" is, geometrically, a topology change.
3. **The poised-at-symmetry structure [interpretation, worth its tag]:** EQ (phase 46) selects maximal symmetry; the maximally symmetric point is where V is *maximal* — the equilibrium point of the clock is the *unstable* top of the quantum potential. The natural initial condition and the instability coincide: the fold starts where EQ puts it and is destined to roll. "The universe rolls off its own symmetry" is the one-line reading; it is an interpretation of derived structure, not an extra assumption.

## 3. The derived cosmological class [conditional on the coupling gap — stated at every use]

If the fold's Teichmüller modulus is the cosmological dark-energy degree of freedom (the phase 50 §3.3 join — open), the sector is a 6g−6-field sigma model with WP kinetic term on a negatively curved, incomplete target, in a hilltop potential. The generic cosmology of that class:

- **Early times:** Hubble friction pins the modulus near the top ⟹ **w ≈ −1 to high accuracy at high redshift** — the framework's old prediction is recovered as the *early-time limit* rather than an exact law.
- **Late times:** the modulus thaws and rolls ⟹ **w departs from −1 at low redshift, monotonically at leading order** — the **thawing** class, not freezing, not tracker.
- **No genuine phantom:** a standard-kinetic scalar in this potential cannot cross w = −1. Any apparent phantom crossing in CPL fits must be a **parametrization artifact** — noting [analysis-level, hedged] that sharp late-time features forced into (w₀, wₐ) are a known source of exactly such artifacts.
- **The terminal step:** the roll reaches the finite-distance boundary ⟹ the smooth phase *ends in a discrete topology-change transition*. Smooth-then-step is one derived trajectory, not two rival scenarios — the phase 27 step fallback becomes the *terminal event* of the phase 51 roll.
- **Multi-field caveat:** 6g−6 fields on a negatively curved target generically produce turning trajectories (non-geodesic roll); the single-field statements above are the leading-order class, flagged accordingly.

**What is not derived: the magnitude.** The normalization of V and the modulus' effective Planck-units field range ride entirely on the coupling gap; in-room, the roll *rate* — hence quantitative (w₀, wₐ) — is not computable. The class is derived; the numbers are not. Phase 44's IR constraint stands unamended: the raw fold-scale potential is Planckian and must be diluted by whatever resolves the join.

## 4. Kill scoring and follow-ups

- **Regime 1: EXCLUDED** (V provably nonconstant) — the first of phase 50's kill conditions is resolved in the route's favor.
- **Roll-rate kill test: NOT YET SCORABLE** (needs the coupling gap). Honest status: the route cannot yet die by magnitude, only by shape.
- **T-M1b (opened):** the species-weighted potential. The ZT coefficient (6n²−6n+1) is *negative* at n = ½ — spinor determinants curve moduli space the other way — so the full potential is again a **signed species sum** (echo of phase 49). The single-scalar shape is the model; the SM-weighted shape is a defined computation, not done here.
- **T-M1c (opened):** numerics beyond genus 2 (Bolza-max is conjectured; higher-genus landscape unknown).

## 5. T-M2 — the pre-stated commitments (on record before any reconstruction)

If the moduli route is the true dark-energy sector, the binned w(z) reconstructions must show, per T-M2's discipline these are stated now, 2026-07-17, before DR1:

1. **Thawing shape:** w(z) → −1 at high z; departures grow toward low z. A freezing or tracker shape kills the route.
2. **No true phantom:** any reconstructed w < −1 must be demonstrably a parametrization artifact; robust, model-independent phantom behavior kills the route.
3. **Late-time steepening / step precursor:** the approach to the terminal transition implies late-time acceleration of the departure (steepening of w(z) at the lowest redshifts) rather than saturation; a demonstrated late-time *flattening* of the departure disfavors it.

These three, plus the standing P4a (w_DM = 0 must hold throughout — verified untouched by the moduli sector at T-M4 level: census and soliton volume are Teichmüller-blind [checked structurally; logged for the audit]).

## 6. Ledger

- Phase 50 protocol §5.3 condition met: **T-M1 has produced pre-stated structure before the reconstructions** — the moduli route holds candidate-successor status, with its discount and its open join both on its label.
- The scoreboard is untouched: P1 and the registered fallback stand exactly as before; §5's commitments are the *successor's* registration, filed separately.
- New open items: T-M1b (species-weighted ZT sum), T-M1c (higher-genus numerics), the coupling gap (unchanged, decisive), K-audit residues (Wolpert CMP 112 verbatim check — the K2 sign is load-bearing).

*Status line: T-M1 is executed at model level and the route survived its first kill condition with structure to spare — the potential is provably non-flat, shaped as a hilltop at the symmetry point with finite-distance topology-change walls, and the implied cosmology is thawing-from-−1 with a terminal step: three falsifiable commitments now on record ahead of the data. The framework's dark-energy story has, in one day, gone from "rigid or dead" to "poised at its own symmetry, rolling, and due to be scored" — with every conditional link named, and the scoreboard it must answer to left exactly where it was.*
