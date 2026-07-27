# Referee report — FORK-1 lattice-fork joint-satisfiability audit (phase 120)

**Date:** 2026-07-27
**Reviewed document:** phases/phase120-FORK1-lattice-audit.md (consultation section)
**Referee:** context-free adversarial agent (independent hand re-derivation of all arithmetic; adjudication of the kill ruling against the registered wording; scope-guard audit). Report preserved VERBATIM below; nothing edited.

---

# ADVERSARIAL REFEREE REPORT — Consistency-Audit Submission

## Verdict summary

All load-bearing arithmetic verifies. Two presentation defects (a citation overshoot on transcendence; a self-contradictory phrasing of the density lemma), zero substantive numerical errors. BOX-1's winding-nonexistence derivation is correct; its novelty is partial — the record's own "index R² when R² ∈ ℕ" caveat already circumscribed the failure set, but the record's unconditional "Rℤ ⊂ Λ_R" is an unflagged erratum the submission exposes without naming. The K-FORK-1 non-firing ruling is the faithful adjudication of the registered wording, with one rider: the arena-separation scheme is unregistered scaffolding and must be logged as provisional. The insufficiency corollary partially overreaches. Scope guards: clean.

## Per-claim analysis

**1. Q-lattice spacings.** Q-spacing = √(2π)/R. R=√(2π) → 1 (ℤ) ✓. R=√2 → √(2π)/√2 = √π ✓. R=√3 → √(2π/3) ✓. All three verified.

**2. Irrationality claims.** √π: if rational, π = (√π)² ∈ ℚ — contradiction. √(2π/3): if rational r, π = 3r²/2 ∈ ℚ — contradiction. Both need only *irrationality* of π (Lambert 1761); invoking Lindemann's transcendence is sufficient but unnecessary — a citation overshoot, not an error (C-AG1). √(3/2) = √6/2: check (√6/2)² = 6/4 = 3/2 ✓. Proof √6 ∉ ℚ: √6 = p/q reduced ⟹ p² = 6q² ⟹ 2|p ⟹ 4|6q² ⟹ 2|3q² ⟹ 2|q, contradicting reducedness. Verified algebraically, as claimed.

**3. (1/√2)ℤ ∩ ℤ = {0}.** n/√2 = m ⟹ n = m√2 ⟹ m = n = 0 ✓.

**4. Winding-existence criterion.** Rℤ ⊆ (1/R)ℤ ⟺ R·1 = n/R for some n ∈ ℤ ⟺ R² ∈ ℤ; conversely R² = n ⟹ Rk = nk/R ∈ (1/R)ℤ for all k. Derivation correct, and consistent with the record's index statement: Rℤ = R²·(1/R)ℤ, so [Λ_R : Rℤ] = R² when integral ✓.

**5. R² = 2π ∉ ℤ.** 6 < 2π < 7, and 2π is transcendental. ✓.

**6. Effective R² = 8π.** A factor-2 refinement of the Q-lattice halves spacing: (1/R_Q) → (1/(2R_Q)), so R → 2√(2π), R² = 4·2π = 8π ✓; 8π ∉ ℕ ✓; the refined Q-lattice is (1/2)ℤ ≠ ℤ, so the exact C-BRIDGE pin is indeed destroyed ✓.

**7. 2-vs-5 ratio.** (1/2)/(1/√2) = √2/2 = 1/√2, irrational ✓; both lattices stated in q-units, so convention-independence holds ✓.

**8. Density claim.** As phrased — "a lattice containing two incommensurable lattices is dense, not a lattice" — it is self-contradictory (a lattice, being discrete, cannot contain them; a dense subgroup is not a lattice). The correct statement: every subgroup of ℝ is either cyclic-discrete or dense; ℤa + ℤb with a/b ∉ ℚ is dense (Kronecker), hence no discrete common refinement exists. Substance correct, phrasing defective (C-AG4).

## Mandate 2 — BOX-1 stress

Derivation: correct (item 4). **Novelty:** partial. For R > 0, R² ∈ ℤ ⟺ R² ∈ ℕ, so the nonexistence set and the record's caveat set *coincide exactly*. The record implicitly conceded the failure set via its caveat — yet asserted "Rℤ ⊂ Λ_R" unconditionally, which is false off that set. The submission's genuine contributions are (i) converting an undefined-index caveat into a structural nonexistence statement, and (ii) implicitly exposing a record erratum it never names (C-AG3). "Strictly stronger than the known locality failures" is right about *failure mode* (structure absent vs. structure present but non-local) but wrong if read as a strictly larger R-set — the sets are identical (C-AG2). **Same-arena classification:** correct; the failure is internal to the bridge's own extension at its own pinned value; no cross-arena separation is available. **Conditionality:** honest, not a dodge. K-FORK-1 as registered quantifies over pairs of *refereed demands*; winding-existence/locality is a record property, never a registered demand, so no registered pair is implicated. Firing now would silently rewrite the kill's wording. Surfacing the bindingness question as an unregistered decision (its GAP-1) is the correct move.

## Mandate 3 — scope-separability ruling

The registered conjunct is "not scope-separable." The suffix is modal: the conjunct *fails* whenever a separation is available in principle, registered or not. The submission exhibits one — the cluster decomposition, under which each non-abelian demand pins R only in the record hosting its symmetry; read conditionally, the demands are then not even "genuinely jointly unsatisfiable" (they are vacuously co-satisfiable across models). Adjudicating the three candidate rulings: **FIRES** is unfaithful — it requires *established* inseparability, which is absent. **UNADJUDICABLE-PENDING-GAP-3** inverts the burden of proof: a registered kill fires when its conditions are established and remains unfired otherwise; an undecided ontology means inseparability is unestablished, which yields non-firing, not suspension — and "unadjudicable" would itself be an unregistered third verdict category. **DOES NOT FIRE** is the ruling most faithful to the registered wording, with the mandatory rider: the arena assignment is post-hoc, conceded by the submission's own GAP-3, and must be registered (its decision 3); a future single-arena registration reopens the kill. The submission's ruling therefore stands, but as provisional scaffolding, not settled adjudication (C-AG7).

## Mandate 4 — clusters, decisions, corollary

**Clusters:** membership verified; SU(2)₂'s homelessness holds even under C-AD5 reading A (the refinement destroys the exact pin, so it cannot join cluster A) ✓; ZM-1 as sole transportable core ✓. **Gaps:** the superseded R=1 demand is rightly excluded as not live, but its *disposition under multi-arena ontology* (does a superseded demand revive as its own arena?) is a missing decision; the registration of the record erratum (C-AG3) is another. ZM-1's transport license — precisely which cross-arena claims the R-independent core underwrites — deserves explicit listing rather than being folded into decision 3 (C-AG6). **Insufficiency corollary:** "insufficient" is refereed *for SU(2)₂ only*; the leap to all non-abelian material beyond level 1 is unrefereed extrapolation — motivated (lattice constructions yield level 1 per Frenkel–Kac) but not established by the record inputs. Worse, "necessary" is asserted, not derived, and sits in tension with the submission's own decision 5: if the registration variable becomes lattice-plus-coset, R is a *derived* coordinate, not a necessary one. Re-tag: theorem for SU(2)₂; conjecture beyond; drop or defend "necessary" (C-AG5).

## Mandate 5 — scope-guard audit

No value of R is selected anywhere; clusters are presented symmetrically with costs, no preference expressed. No fine-structure or coupling computation, estimate, or formula appears; the "where the question lives" re-tagging is meta-level. No unit anchors. The 8π figure is a conditional arithmetic consequence, not a pin. **COMPLIANT.**

## Corrections ledger

- **C-AG1** — Replace "by transcendence of π (Lindemann)" with "by irrationality of π"; transcendence is unnecessary for both π-ratios. Overshoot, no downstream effect.
- **C-AG2** — "Strictly stronger than the known locality failures": the affected R-set is identical (R² ∈ ℤ ⟺ R² ∈ ℕ for R > 0); restate as a deeper failure mode on the same set.
- **C-AG3** — Unflagged record erratum: the record's unconditional "Rℤ ⊂ Λ_R" is false whenever R² ∉ ℕ; register as a correction (add as decision 6).
- **C-AG4** — Density lemma misphrased; correct to: any subgroup of ℝ containing two incommensurable lattices is dense, hence non-discrete; no lattice refinement exists.
- **C-AG5** — Insufficiency corollary: refereed status restricted to SU(2)₂; level>1 generalization is conjecture; "necessary" conflicts with decision 5 — reconcile or drop.
- **C-AG6** — Decision list incomplete: add superseded-R=1 disposition under multi-arena ontology (decision 7) and an explicit ZM-1 transport-license item.
- **C-AG7** — The non-firing ruling rests on the modal reading of "scope-separable"; the separation scheme is unregistered — log as provisional pending decision 3, else the ruling is vulnerable to a single-arena registration.

## VERDICT BOX

1. **K-FORK-1: DOES NOT FIRE** — most faithful to registered wording; inseparability unestablished, separation available in principle; reopens if single-arena ontology is registered.
2. **BOX-1**: derivation VERIFIED; PARTIALLY NEW (sharpens record caveat; exposes erratum C-AG3); conditional-kill handling HONEST, not a dodge.
3. **Arithmetic**: ALL VERIFIED; two presentation defects (C-AG1, C-AG4), zero substantive errors.
4. **Clusters/decisions**: SOUND with additions (C-AG6); insufficiency corollary PARTIAL OVERREACH (C-AG5).
5. **Scope guards**: COMPLIANT — no pin, no couplings, no anchors.

Word count: ~1,480 (within the 2,000-word cap).
