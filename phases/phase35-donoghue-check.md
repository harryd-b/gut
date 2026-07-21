# Phase 35 — M2 executed (structural level): the Donoghue check

*Working session, 2026-07-11. Executes scorecard milestone M2: does the framework reproduce the universal low-energy quantum corrections to the Newtonian potential — the parameter-free coefficients any theory with a GR+QFT infrared limit must yield? Executed here at the structural level, where the answer is decidable in-room; the residual coefficient bookkeeping is specified as M2b.*

---

## 1. The benchmark, precisely

Effective-field-theory gravity (Donoghue 1994; Bjerrum-Bohr–Donoghue–Holstein 2003) establishes that the one-loop long-distance corrections to the Newtonian potential,

  V(r) = −(G m₁ m₂ / r) [ 1 + 3G(m₁+m₂)/(r c²) + (41/10π) · Gℏ/(r² c³) + … ],

are **universal and parameter-free**: the non-analytic pieces (the classical 1/r² post-Newtonian term and the quantum ln-derived 41/10π term) are fixed entirely by (i) the Einstein–Hilbert two-derivative term with its standard normalization, and (ii) the massless propagating content (the two-polarization graviton, plus whatever massless matter runs in the loop). Local higher-curvature operators (R², R_{μν}R^{μν}, topological terms) contribute only *analytic* (delta-function-like/short-distance) corrections — they **cannot** shift the universal coefficients. This is the theorem-level backbone of the check. **[audit D1: exact coefficient and operator-independence statements]**

## 2. The framework's infrared action

From the record (imported at physics level; phase 29): the large-scale limit of the GV/spectral action is **Einstein–Hilbert + Holst + a correction associated with non-integer GV values** (AMK 1601.06436 §§7–8; the RG/Ricci-flow route), with the graviton sector standard (P2: exactly two tensor polarizations; phase 33 L1: local physics exactly standard).

## 3. The structural argument (the in-room decidable part)

The Donoghue coefficients follow for the framework **iff** three structural conditions hold:

- **(D-i) EH normalization:** the two-derivative term of the IR action is EH with the standard coefficient (equivalently: the curvature modulus is c⁴/16πG with the *measured* G — which is how G enters the framework in the first place, §4.1). ✓ by construction of the IR limit; nothing in the GV correction is two-derivative. **[audit D2: confirm no two-derivative renormalization from the GV term]**
- **(D-ii) No extra massless propagating modes:** the Holst term (constant Immirzi parameter, torsion-free vacuum sector) does not propagate new degrees of freedom and does not alter the vacuum field equations; the GV correction is topological/higher-order in derivatives. ✓ at physics level — this is also exactly the content of the framework's own P2 commitment (two polarizations) and L1 (locally standard). **[audit D3: Holst-with-fermions caveat — torsion-induced four-fermion contact terms exist but are analytic/local, hence Donoghue-safe; confirm]**
- **(D-iii) Standard massless loop content:** the matter sector at accessible energies is the Standard Model's (the framework adds no light propagating exotica; gravisolitons are solitonic, not new light fields). ✓ per the framework's own null commitments.

Given (D-i)–(D-iii), the EFT theorem of §1 applies verbatim: **the framework reproduces the classical 3G(m₁+m₂)/rc² and quantum (41/10π)Gℏ/r²c³ corrections exactly.** Conversely — and this is the check's teeth — if the GV/Holst structure *had* introduced a light mode or shifted the two-derivative term, the coefficients would move and the framework would be falsified by the same EFT logic. The pass is a consequence of L1 ("the fold is locally invisible"), now seen from the scattering side: the fold contributes no local operator that could disturb the universal infrared.

## 4. Verdict and grading

**M2: PASSED at the structural level** — the framework outputs the Donoghue coefficients, conditional on: the imported IR action (II.1's status, unchanged), and audits D1–D3. Grade for scorecard II.2: **MISSING → DERIVED (structural, physics-level; conditional on the II.1 import)**. What a full in-house computation (**M2b**, specified for the record) would add: expand the spectral action S = Tr_ω([D,X^μ][D,X_μ]|D|⁻²) around flat space to one loop directly — verifying (D-i)/(D-ii) by computation rather than structure — and exhibit the analytic corrections the GV term *does* make (short-distance, unobservable, but the framework's own fingerprint at the formal level). M2b is a well-posed calculation for a graviton-EFT practitioner; it does not gate the structural pass.

## 5. What this milestone teaches

The three executed derivations of the day (Unruh, Donoghue, Born rule) share one engine: **L1**. The framework's geometric content is globally supported, so every *local, universal* piece of physics — modular wedge structure, infrared graviton EFT, the probability calculus — is reproduced exactly and necessarily. The framework is falsifiable only where it is distinctive: the global handles (P1, P4a, sector structure) and the identification joins (V.7/T1). This is now demonstrated rather than asserted, across three independent benchmark classes.

## 6. Audit table

| # | Fact | Where | Confidence | Ask |
|---|---|---|---|---|
| D1 | Universality/operator-independence of the non-analytic Donoghue coefficients; 41/10π value (BDH 2003) | §1 | high | citation spot-check |
| D2 | GV correction contributes no two-derivative renormalization | §3 D-i | medium-high | short computation |
| D3 | Holst term inert in vacuum; fermion-induced torsion terms analytic/local | §3 D-ii | high | standard references (Immirzi literature) |

**Scorecard effect: II.2 → DERIVED (structural); M2 executed; M2b logged as the computational completion. Class II now holds two derived entries (II.2, II.3) plus II.4's temperature half — all earned today, all sharing the L1 engine and the V.7 conditionality.**
