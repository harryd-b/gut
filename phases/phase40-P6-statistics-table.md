# Phase 40 — The statistics-clause table: P6.2's quantitative prediction computed

*Acting-expert session, 2026-07-17. Executes the finite computation that phase 27 P6.2 / phase 28 issued as the discriminating quantitative prediction of the statistics clause: on S¹×Σ_g, per flux sector 0 < |k| ≤ g−1, the protected content is H*(Sym^{g−1−|k|}Σ_g) (Muñoz–Wang; established at label level in phase 28), and the clause predicts **fermionic multiplicity = b_odd(Sym^{g−1−|k|}Σ_g)** in each sector. This document computes the exact table. Method: Macdonald's formula for the Poincaré polynomial of symmetric products, Σ_n q^n P_t(Sym^n Σ_g) = (1+qt)^{2g}/((1−q)(1−qt²)) [established (Macdonald 1962)]; exact integer arithmetic; two independent sanity checks passed (known Betti numbers of Sym²Σ₂ = (1,4,7,4,1) and Sym²T² = (1,2,2,2,1); Euler characteristics against the generating function Σ χ(Sym^n Σ_g)q^n = (1−q)^{2g−2}, all g ≤ 6, exact match). Script `p6_f2_calc.py` (Part 1) archived.*

---

## 1. The table [proved, given the phase-28 identification]

Per sector: b_even = bosonic multiplicity, b_odd = predicted fermionic multiplicity, χ = b_even − b_odd (sign = which statistics dominates).

| g | \|k\| | n = g−1−\|k\| | b_even | b_odd | χ | total |
|---|---|---|---|---|---|---|
| 2 | 1 | 0 | 1 | 0 | +1 | 1 |
| 2 | 0* | 1 | 2 | 4 | −2 | 6 |
| 3 | 2 | 0 | 1 | 0 | +1 | 1 |
| 3 | 1 | 1 | 2 | 6 | −4 | 8 |
| 3 | 0* | 2 | 18 | 12 | +6 | 30 |
| 4 | 3 | 0 | 1 | 0 | +1 | 1 |
| 4 | 2 | 1 | 2 | 8 | −6 | 10 |
| 4 | 1 | 2 | 31 | 16 | +15 | 47 |
| 4 | 0* | 3 | 60 | 80 | −20 | 140 |
| 5 | 4 | 0 | 1 | 0 | +1 | 1 |
| 5 | 3 | 1 | 2 | 10 | −8 | 12 |
| 5 | 2 | 2 | 48 | 20 | +28 | 68 |
| 5 | 1 | 3 | 94 | 150 | −56 | 244 |
| 5 | 0* | 4 | 350 | 280 | +70 | 630 |
| 6 | 5 | 0 | 1 | 0 | +1 | 1 |
| 6 | 4 | 1 | 2 | 12 | −10 | 14 |
| 6 | 3 | 2 | 69 | 24 | +45 | 93 |
| 6 | 2 | 3 | 136 | 256 | −120 | 392 |
| 6 | 1 | 4 | 698 | 488 | +210 | 1186 |
| 6 | 0* | 5 | 1260 | 1512 | −252 | 2772 |

\* k = 0 rows are listed for completeness but carry the phase-28 caveat: the k = 0 clause must be rebuilt around the Jacobian dressing and the Jabuka–Mark 2-torsion before these entries count as predictions.

## 2. Structure worth stating [derived from the table]

1. **Maximal-flux sectors are purely bosonic** (n = 0: one protected class, even) — universal in g.
2. **Next-to-maximal sectors are maximally fermion-dominated** (n = 1: b_odd = 2g vs b_even = 2 — the fermions count the 2g one-cycles of Σ_g; the sector "is" H*(Σ_g) itself). The fermionic content of the first nontrivial flux sector *grows linearly in genus* — a clean, memorable slogan for the outreach: *one handle, one fermion pair, per the clause.*
3. **Statistics dominance alternates down the flux ladder:** sgn χ(Sym^n Σ_g) = (−1)^n (visible in the table; consistent with χ(Sym^n Σ_g) = (−1)^n·C(2g−2+... ) — the χ generating function (1−q)^{2g−2} has alternating signs for g ≥ 2). A framework with uniform statistics per sector would have no such alternation; this is a distinctive internal fingerprint.
4. The Bradlow truncation (phase 28) means the table is *finite* for each g — the framework predicts a complete, closed census per universe.

## 3. Falsification and status

The table is now the concrete content of P6.2: any Floer-theoretic computation of sector-wise protected parity content on S¹×Σ_g that disagrees with a row (for k ≠ 0) kills the statistics clause. Conversely each independently computed row is a passed test. The identification "protected content = H*(Sym^{g−1−|k|}Σ_g)" is Muñoz–Wang [established (others'); adopted in phase 28]; what this phase adds is the parity split and its structure, which is where the physics (the statistics clause) actually bites.

*Status line: P6.2's "finite, auditable computation" is done and its structure extracted; the desk-test ledger row moves from "prediction issued" to "prediction tabulated, awaiting independent Floer-side check (k ≠ 0 rows) and the k = 0 rebuild."*

**[SUPERSEDED, 2026-07-18, phases 75 & 77]:** this table is correct mathematics about **Σ_g×S¹ — the wrong manifold** (the carrier is T¹Σ_g; phase 75). On the carrier, OS08 Theorem 5.6 (source obtained, implemented, cross-checked — phase 77) gives **total reduced rank ONE, in the spin-type sector [g−1]**: the rich census, the parity clause in this form, the deficit column, and the "one handle, one fermion pair" slogan (in its census form) do not survive the migration. The table stands as the chain-level/moduli-level shadow (the MOY vortex components carry exactly these blocks, cancelled in homology by flow lines to the Jacobian — OS08's own gloss). See phase 77 for what replaces it.
