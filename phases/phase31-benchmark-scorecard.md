# Phase 31 — The reconciliation scorecard: what the framework must output, and what it currently outputs

*Working session, 2026-07-11. Question addressed: how is an attempt to reconcile GR and quantum theory measured? Answer: against the field's de facto benchmark suite — the correspondence limits, the semiclassical overlap results, and the internal-consistency demonstrations. The metric is not "does the framework have a story about X" but "can it OUTPUT the mathematics of X," graded **DERIVED** (in-house, from the framework's own primitives) / **IMPORTED** (cited from others; consistent but not produced) / **CONJECTURED** (mechanism named, derivation absent) / **MISSING**. Progress = items moving left. Rigor sub-grades follow the program's tags: math-theorem / constructive-QFT / physics-level.*

---

## 0. The structural position (read this first)

This framework does **not modify quantum theory**: the net, Hilbert space, Born rule, and linear evolution are standard (that is exactly why P3 predicts κ = 0). Consequence: **benchmark class I (recover QM/QFT) is passed by construction**, which is a real structural advantage over Born-rule-modifying approaches (BHMM) that must also explain why nonlinearity hides. The price: the *entire* reconciliation burden falls on the gravity side — the framework must output GR and the semiclassical overlap results from its own primitives (Σ, foliation/GV, the modular structure), or it is a reinterpretation, not a reconciliation.

## 1. The benchmark suite and the current scorecard

| # | Benchmark | What must be output | Status here | Notes |
|---|---|---|---|---|
| I.1 | QM/QFT recovery | Hilbert space, Born rule, unitarity, standard dispersion | **DERIVED (trivially — never abandoned)** | The framework's cleanest asset; state it prominently. |
| I.2 | The AQFT net itself | The local net from the geometry, not assumed | **MISSING** | Phase-4 gap (iii), restored in CORE §2.1: the net is presupposed. Honest scope: "geometry organizes the net's sectors," not "geometry produces the net." |
| II.1 | Einstein equations / EH action at large scale | Field equations from the primitives | **IMPORTED (physics-level)** | AMK: GV action → RG/Ricci flow → EH + Holst (1601.06436 §§7–8). In-house route (entanglement first law) = **CONJECTURED**, gated on T1-core. Two independent routes must agree — a stated consistency check (§4.1(iii)). |
| II.2 | Newtonian limit + **Donoghue coefficients** | The universal, parameter-free O(Gℏ) corrections to the Newtonian potential that ANY theory with GR+QFT infrared limit must reproduce | **DERIVED (structural) — phase 35 (M2); conditional on the II.1 import; audits D1–D3** | Passes because of L1: the GV/Holst structure adds no light modes and no two-derivative shift, so the EFT universality theorem applies verbatim — 3G(m₁+m₂)/rc² and (41/10π)Gℏ/r²c³ reproduced exactly. Computational completion logged as **M2b**. |
| II.3 | Unruh temperature | T = a/2π from the framework's clock | **DERIVED — assembled in phase 33 (M1); conditional on V.7; audits B1–B4 pending** | Two in-house lemmas do the work: L1 ("the fold is locally invisible" — GV is a secondary invariant with no local density, so local physics is exactly standard) + L2 (Connes cocycle ⇒ the clock is a unique state-independent outer class) join to the imported BW theorem. Failure mode closed: the GV clock *cannot* disagree with boost time locally. Hawking temperature κ/2π follows via Kay–Wald (II.4's temperature half). |
| II.4 | Hawking radiation + **S = A/4G with the ¼ derived** | The field's "hydrogen atom" (cf. Strominger–Vafa; LQG isolated horizons) | **IMPORTED** (Susskind–Uglum, Jacobson) | The reconciliation of §4.1(iii) asserts the area term in units of the curvature modulus; *deriving the coefficient* from GV/modular data is the full T1 target. **Milestone M3.** |
| II.5 | QFT in curved spacetime | Standard curved-space QFT in the appropriate regime | **IMPORTED / consistent** | Inherited if II.1 holds; no in-house derivation needed beyond consistency. |
| II.6 | Cosmological perturbations | n_s, r from the framework | **IMPORTED, flagged non-distinctive** | Starobinsky via AMK topology-change; the program's own audit (§8B) already refuses to count this. Correct discipline — keep it. |
| III.1 | Problem of time, *demonstrated* | Ordinary Schrödinger evolution recovered w.r.t. the framework's time in a lab regime | **CONJECTURED** | The physical half of T1: thermal time → lab time with the GV-pinned flow (Connes–Rovelli did special cases; the GV version is the program's own). **Milestone M4.** |
| III.2 | Arrow of time | Directionality derived, not assumed | **CONJECTURED (candidate-novel)** | The KMS route is the program's unclaimed territory (phase 29: absent in AMK, absent in Bertozzini). A derivation here is both a benchmark item AND the novelty claim. |
| III.3 | Graviton sector | Two polarizations, correct propagator, no ghosts | **IMPORTED / consistent** | Follows from II.1's EH limit; P2's zero-anomaly commitments are the observational face. |
| III.4 | Background independence / covariance | No fixed background smuggled in | **PARTIAL** | 3D-fundamental ontology is background-free in spirit; the fiducial structures in the constructions (fixed Σ, fixed foliation) should be audited once T1 exists. |
| III.5 | Measurement/decoherence account | At least consistency with decoherence theory | **IMPORTED / adjacent** | AMK offers a gravitational-decoherence account (T_dec ≈ 10⁻²⁴ s, 1601.06436 §11) — adjacent, not adopted. The framework, being standard-QM, needs nothing beyond the standard account. |
| IV | New predictions beyond both parents | Falsifiable outputs neither parent makes | **DONE (ledger)** | Phase 27/30: the rigid pair (w_DE, w_DM) = (−1, 0); GW zero-anomaly commitments; κ-null; P4b polarization; HM_red dark-sector census. This class is ahead of class II — unusual for a young framework, and worth saying. |

## 2. The four "output the maths" milestones, ordered by feasibility

- **M1 — EXECUTED (phase 33):** the GV-pinned clock reduces to Bisognano–Wichmann on wedges — *necessarily*, via L1 (fold locally invisible: GV has no local density) + L2 (Connes cocycle: one outer clock class) + imported BW; T = a/2π and T_H = κ/2π (Kay–Wald) obtained; new named principle L1 explains the entire null-prediction family; T1 re-posed as a *selection* problem (pin the global representative), a genuine simplification.
- **M2 — EXECUTED at structural level (phase 35):** the framework passes the Donoghue check — L1 guarantees no light modes and no two-derivative shift from the GV/Holst structure, so the universal coefficients (incl. 41/10π) follow verbatim from the EFT theorem; falsification direction preserved (a light mode or kinetic shift would have failed it). Computational completion = **M2b** (one-loop expansion of the spectral action), well-posed, does not gate the pass.
- **M3 (the hydrogen atom): the ¼.** Derive S = A/4G — coefficient included — from the entanglement first law with H_mod the GV-pinned modular Hamiltonian. This IS T1 + §4.1(iii) stated as a benchmark; success simultaneously completes the stiffness reconciliation and puts the framework on the Strominger–Vafa/isolated-horizons shelf.
- **M4 (the demonstration that "time is modular" is physics, not philosophy):** recover the lab Schrödinger equation w.r.t. thermal time for a localized nonrelativistic system, with corrections estimated (and shown unobservably small — consistent with P3's nulls).

## 2b. Class V — Quantumness derived (Plank II, strong form): the track the first draft undersold

The thesis was never "accept QM, geometrize gravity": Plank II's strong form is that quantum theory itself is geometry's shadow. Corrected here: this track exists, and **more of its links are theorems than on the gravity track.** The chain, graded link by link:

| Link | Statement | Status |
|---|---|---|
| V.1 | Foliation → holonomy groupoid → C*-algebra; noncommutative because the geometry has holonomy | **THEOREM** (Connes) |
| V.2 | GV ≠ 0 ⇒ type III component | **THEOREM** (Hurder–Katok) |
| V.3 | Type III ⇒ no pure normal states, no dispersion-free states ⇒ **statisticality is forced by the geometry** (and every state is KMS-thermal w.r.t. the modular flow — the same GV that makes the clock makes the chance) | **DERIVED — assembled in phase 32 (M0c), pending expert-audit items A1/A4–A6** |
| V.4 | **Born rule forced**: on a von Neumann algebra with no type I₂ summand, every (even finitely) additive probability measure on the projection lattice is a state — completely additive ⇒ normal (Gleason; Christensen/Yeadon/Paszkiewicz; Bunce–Wright); type III qualifies | **DERIVED — assembled in phase 32 (M0b), pending expert-audit items A1–A3**. The program's first fully in-house derived benchmark. |
| V.5 | Hilbert space + superposition: GNS on the geometric algebra | **THEOREM** |
| V.6 | Quantization map: Poisson algebra of holonomies → Kauffman skein algebra, t = e^{h/4} (Turaev; BFK); AMK's overlay: the deformation is *forced by exotic smoothness* — tame → wild embedding IS quantization ("the world is quantum because smoothness is exotic") | **DERIVED — assembled in phase 34 (M0a); theorem core + overlay at audited-physics-level (pivot: audit C2 = AMK 1211.3012); ħ's *value* remains the T2-type scale gap** |
| V.7 | The foliation/skein algebra IS the physical observable algebra (the net) | **CONJECTURE — the shared bottleneck: the same identification gates the gravity track (§4.1). Both tracks converge on one join.** |
| V.8 | Residue: tensor structure for composites; complex vs real; measurement weights | **MISSING (Level-3 foundations; open for every program).** AMK's Casson-tower decoherence is a candidate for measurement. |

**Class-V milestones:**
- **M0b — EXECUTED (phase 32):** Born-rule theorem-assembly written, hypotheses audited, six-item expert-audit table attached; conclusion: quantum probability is the unique (even finitely) additive probability calculus on the folded geometry's event lattice.
- **M0a — EXECUTED (phase 34):** the quantization chain assembled — Goldman Poisson algebra of leaf holonomies → Kauffman skein algebra K_t, t = e^{h/4} (Turaev/BFK theorems; classical limit exact by Bullock/Przytycki–Sikora) — with the AMK overlay (tame→wild = classical→quantum; "ħ ≠ 0 ⟺ exotic smoothness") explicit, its load-bearing claim isolated (audit C2), and the honest residue logged (ħ's value = the T2-type scale gap; uniqueness; sector scope).
- **M0c — EXECUTED (phase 32):** statisticality package assembled: no dispersion-free states at all (simplicity of type III factors), no pure normal states, intrinsic KMS thermality, and (III₁, caveated) Connes–Størmer state-space homogeneity; the "one fold makes the chance and the clock" statement is now theorem-backed on the chance side.
- **M0d:** the join (V.7) — now upgraded in priority: it gates BOTH the quantum and gravity tracks. T1-core and M0d are two faces of one problem.
- **M0e:** the residue (V.8) — logged, not promised.

**Scoring rule going forward:** the program's reconciliation progress is measured by this table's left-migrations, and by nothing else — not by new interpretive sections, not by additional adjacent-framework comparisons. The prediction ledger (phase 27/30) measures its physics; this scorecard measures its reconciliation. Both are now part of the record.

## 3. Honest current summary (corrected 2026-07-11, same day — the first version undersold Plank II)

One benchmark class passed by construction (I.1); one class ahead of schedule (IV — the ledger); **class V (quantumness derived) newly recognized as the track with the most theorem-backed links** — three of its links are theorems awaiting assembly (M0a–M0c) and its single conjectural join (V.7) is the *same* join that gates the gravity track; zero class-II items yet derived in-house, with two feasible promotions posed (M1 Unruh, M2 Donoghue); the hard targets (M3, M4, M0d/T1) all point at one bottleneck. The framework's honest self-description for outsiders: *"a program to derive both parents of physics from one geometric primitive — the quantum side (noncommutativity, statisticality, Born rule) via a chain that is mostly theorems plus one conjectural identification; the gravity side (Einstein equations, Unruh/Hawking, emergent time) currently imported at physics level, with the same identification as bottleneck; distinctive falsifiable predictions already on record."*
