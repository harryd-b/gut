# Phase 54 — The dictionary program: anomaly cancellation, four constraints, and the symmetric-orbifold candidate

*Working session, 2026-07-17. Answers "how do we get the dictionary" — the single item every open front queues behind. The session's finding, verified against primary sources including the original Belavin–Knizhnik JETP paper: **the framework's flatness sum rule is, coefficient for coefficient, the zero-central-charge (conformal anomaly cancellation) condition of two-dimensional chiral CFT** — the Zograf–Takhtajan index coefficient 6n²−6n+1 is the Mumford exponent and (times −2) the bc-system central charge, and the "moduli-independence ⟺ Σ±(6n²−6n+1) = 0 ⟺ c_total = 0" chain is explicit in BK 1986. Consequence: the dictionary stops being an open-ended construction and becomes a **four-constraint classification problem with known technology** — plus one candidate solution suggested by the framework's own census, and one named risk that must be swept before any celebration.*

---

## 1. The verified identification [all [verified-source] this session]

- **bc/βγ central charge:** c = −2ε(6λ²−6λ+1) (FMS Nucl. Phys. B271 (1986), eq. (75) verbatim; λ=2 → −26, λ=3/2 → +11, λ=½ → +1).
- **Mumford isomorphism:** λ_n ≅ λ_1^{⊗(6n²−6n+1)}; λ_2 ≅ λ_1^{13} (Mumford 1977).
- **The chain, in the original:** Belavin–Knizhnik (Sov. Phys. JETP 64 (1986) 214) carry the per-field moduli-anomaly coefficient 6j²−6j+1, state that at D = 26 "the conformal anomaly cancels," and invoke Mumford's theorem to trivialize λ_2 ⊗ λ_1^{−13}. **Moduli-anomaly cancellation = central-charge cancellation — the phase 53 sum rule is this statement.** (Caveats carried: hyperbolic-metric Quillen scheme; BGF corrections in other schemes.)

**Re-reading phase 53 in this light:** the "gravitino-shaped" solutions of the sum rule are *superghost-shaped* — the weight-3/2 content the flatness condition demands is the βγ-system structure of superstring perturbation theory. The framework's lightness mechanism requires its boundary system to be anomaly-free in exactly the sense that defines critical string vacua. This is either a deep convergence or a rediscovery — §4 refuses to let it be left ambiguous.

## 2. The dictionary, reformulated: a four-constraint classification problem

The dictionary = a **chiral boundary system on ∂H² = S¹** (fields = weight-n systems; species = its primaries; the toy join of phases 44/49 supplies the container). It must satisfy:

1. **(Anomaly) c_total = 0** — the flatness sum rule, now with its correct name. [required for the phase 52 mechanism at one loop]
2. **(Automorphy) Γ-consistency** — the system must be coherent under the twist by Γ = π₁(Σ_g) ⊂ PSL(2,ℝ) (phase 49's construction): partition-function-level automorphy for a cofinite Fuchsian group, the surface analogue of modular invariance. [the constraint that makes the problem rigid]
3. **(Sectors) category matching** — the boundary system's superselection structure must reproduce the framework's *derived* sector category: the H² flux ladder, the π₁-representation sectors (phase 49 row 4), and the protected census with its parity table (phase 40). [the framework's own data as boundary conditions]
4. **(Cross-anomaly) 4D/2D consistency** — the same content must satisfy P7's 4D heat-kernel accounting (+1, +1, −4; c_SM = +1 > 0) and the 2D ZT accounting simultaneously — two independent anomaly books that must balance for one spectrum. [the joint Diophantine system, T-M1b2, now with both books specified]

**The payoff structure, stated before the search:** if the constraint system has **no** solution, the framework dies a clean, honorable death at the dictionary. If it has a **unique** (or finitely-classified) solution, the species content is *forced* — and with it, per the constants discussion, the route to computing dimensionless couplings from geometric data opens. Either outcome is decisive; that is what makes this the right problem.

## 3. The candidate, from the framework's own census [conjecture — Route B]

The protected census *is* symmetric-product cohomology: H*(Sym^n Σ_g) with Macdonald generating function (1+qt)^{2g}/((1−q)(1−qt²)) (phases 28/40, [verified-source]). In CFT, symmetric-product structure is the signature of **symmetric-orbifold CFTs** (DMVV) — the universal class of holographic 2D CFTs. **Candidate: the boundary system is a symmetric-product orbifold of a sigma model with target (data of) Σ_g.** The test is sharp and computable: **do the Γ-twisted characters of the candidate reproduce the Macdonald generating function of the census?** — a character-matching computation (Route B), decidable without new physics. [If it matches: the dictionary's skeleton exists and constraint 3 is passed by construction; constraints 1, 2, 4 then become checks on this specific candidate. If it fails: back to Route A.]

**Routes, in order:** **B** (character matching against the census — cheapest, in-room-adjacent); **A** (systematic classification under constraints 1–4 — string-classification technology, partly specialist); **C** (the L1-aud/M-aud specialist items, unchanged, now with sharper questions to ask).

## 4. The string shadow [named risk; mandatory sweep before any claim]

The dictionary machinery — Mumford forms, BK anomaly cancellation, ghost-weight systems, symmetric orbifolds on the boundary of a hyperbolic space — **is the mathematics of string perturbation theory and AdS₃/CFT₂.** Two readings: (a) *convergence* — the fold's boundary system shares the anomaly algebra because the ZT/Mumford mathematics is universal, while the ontology differs (a boundary system on the fold's ∂H², not a worldsheet; the framework's spacetime is not emergent from the CFT); (b) *rediscovery* — the framework is reconstructing a known string/holographic corner, in which case the novelty claims shrink drastically and must be conceded at whatever scope the overlap dictates. **A phase-29-style scholarship sweep (logged S-sweep: AdS₃/CFT₂ on Γ\H², symmetric orbifolds and Anosov/geodesic-flow structures, "spacetime from worldsheet" corners) is mandatory before the dictionary program claims anything.** The B3c discipline, fourth invocation: the more elegant this looks, the harder it must be attacked.

## 5. Status

The dictionary is no longer "the missing input" — it is a posed problem: four constraints, one computable candidate, one decisive character-matching test, one named risk with its sweep, and a payoff (forced spectrum ⟹ computable constants) or a clean death (empty constraint set). Next actions in order: the Route B character match; the S-sweep; then the specialist packet with the sharpened asks.

*Status line: asked "how do we get the dictionary," the program discovered the dictionary problem already has a name in mathematics — anomaly cancellation over moduli space — a candidate solution suggested by its own census, and a risk that it has been walking, by its own internal logic, toward territory string theory mapped forty years ago. Whether that is convergence or rediscovery is now a scheduled computation and a scheduled sweep, not a mood.*
