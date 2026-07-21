# Phase 38 — Tier 2, Problem 2B executed: the κ go/no-go

*Working session, 2026-07-16. Executes TIER-2-KICKOFF §4 (Problem 2B, steps 1–3) and reaches the §5 decision point. Per kickoff §0.5, the existing record was read first: REVIEW-2026-07-11 §1.1, phase 27 (P3), phase 31 (§0), phase 32 (M0b), phase 33 (L1), phase 36 (T1 decomposition). Those documents already carry most of the go/no-go; what was missing — and is supplied here — is (i) the explicit leading-order I₃(g) computation with its coefficient (kickoff §4 step 1, never actually done; phase 27 only estimated κ ~ E/E_P), and (ii) a route-by-route closure of the GV-enhancement loophole (steps 2–3; phase 27 closed it in one sentence). Honesty rules of the kickoff §1 in force throughout. The verdict is reported plainly in §5, per the kickoff's standing instruction not to tune away a null.*

---

## 0. The question and the prior record

**Question (kickoff §4):** with a state-dependent Hamiltonian H_ψ = H + gψ (BHMM, arXiv:2203.17137), compute the Sorkin triple-path parameter κ = I₃/Σ|I₂| to leading order in g; then decide whether the GV stiffness can lift g from Planck-suppressed (κ ~ 10⁻²², dead) into the measurable window (κ ~ 10⁻²–10⁻³).

**What the record already said, consolidated:**

- **REVIEW §1.1 [established, in-house]:** the modular ↔ nonlinear identification of phase 26 is a category error — modular flow is exactly linear and unitary; *everything the program has actually constructed predicts I₃ = 0 identically*. Any κ ≠ 0 requires a **new nonlinear mechanism**, not a computation inside the existing formalism.
- **Phase 32 (M0b) [derived, pending audits A1–A3]:** the Born rule is *forced* on the folded geometry's event lattice (generalized Gleason on the type III algebra). In-house, κ = 0 is not an accident but a theorem-assembly.
- **Phase 33 (L1) [theorem-level structure]:** GV is a secondary, global invariant with **no local density**; the fold is locally invisible; no local experiment — and a tabletop/beamline interferometer is a local experiment — can see a GV-sourced coupling.
- **Phase 27 (P3) [derived, conditional]:** on the conditional BHMM route, gravitational origin gives κ ~ E/E_P ≲ 10⁻²², 16+ orders below every current and planned sensitivity; the loophole ("a mechanism converting GV into an O(1) unsuppressed prefactor") was stated but not systematically closed.

This phase completes the two open items and states the decision.

## 1. Step 1 — the leading-order I₃(g), computed [proved, in-model]

### 1.1 The model

BHMM's H_ψ = H + gψ is schematic; to compute anything, the nonlinearity must be specified. Minimal concrete realization: path Hilbert space ℂ³ with basis |A⟩, |B⟩, |C⟩; slit configuration S ⊆ {A,B,C} prepares ψ_S = Σ_{i∈S} α_i|i⟩ (blocking removes amplitudes, per the Sorkin protocol); interaction picture (free evolution absorbed into the α_i and the detector functional ⟨D| = Σ_i d_i*⟨i|); nonlinear evolution over traversal time τ:

  iħ ∂_t ψ = g N(ψ)ψ,  N(ψ) = Σ_i n_i(ψ)|i⟩⟨i|,  n_i(ψ) = |⟨i|ψ⟩|²/⟨ψ|ψ⟩.

This is the Gross–Pitaevskii-type **local-density nonlinearity** — the minimal member of the BHMM class that couples to *which-path* structure. Define the dimensionless nonlinearity **λ ≡ gτ/ħ**.

**A necessary structural fact first [proved]:** the "purest" reading of H + gψ — the projector nonlinearity N(ψ) = |ψ⟩⟨ψ|/⟨ψ|ψ⟩ — produces **exactly I₃ = 0**: N(ψ)ψ = ψ, so the entire nonlinearity is a global phase e^{−iλ} in every slit configuration. (Verified to machine precision at λ = 0.1.) *A state-dependent Hamiltonian is not sufficient for higher-order interference; the nonlinearity must couple to relative path densities.* This sharpens what any future 2A mechanism must deliver.

### 1.2 Exact solution and the coefficient

For the diagonal model the densities n_i(S) = |α_i|²/Σ_{j∈S}|α_j|² are constants of motion (only phases evolve), so the evolution is exactly solvable:

  ψ_S(τ) = Σ_{i∈S} α_i e^{−iλ n_i(S)}|i⟩,  A_S = Σ_{i∈S} β_i e^{−iλ n_i(S)},  β_i ≡ d_i*α_i = r_i e^{iφ_i}.

With a_i ≡ |α_i|², Δn³_ij ≡ (a_i−a_j)/(a_A+a_B+a_C), Δn²_ij ≡ (a_i−a_j)/(a_i+a_j):

  P_S = Σ_{i∈S} r_i² + Σ_{i<j∈S} 2r_i r_j cos(φ_i−φ_j − λΔn_ij(S)); single-slit terms are λ-independent, so the alternating Sorkin sum leaves only the mismatch between three-slit and two-slit nonlinear phases:

> **I₃ = λ · Σ_{i<j} 2 r_i r_j sin(φ_i−φ_j) (Δn³_ij − Δn²_ij) + O(λ²)**
>
> **κ ≡ I₃/Σ|I₂| = C·λ + O(λ²),  C = [Σ_{i<j} 2r_ir_j sin Δφ_ij (Δn³_ij − Δn²_ij)] / [Σ_{i<j} 2r_ir_j|cos Δφ_ij|].**

**Verification (numerical, exact nonlinear integration vs formula, this session):** I₃ = 0 at λ = 0 to machine precision (Sorkin); the O(λ) coefficient matches the exact integration with ratio 1.0000 as λ → 0 (1.004 at λ = 10⁻², 1.00004 at λ = 10⁻⁴); projector null confirmed. Script `i3_calc.py` archived with this document.

### 1.3 Corollaries of the coefficient [derived, in-model]

1. **C is O(10⁻¹), not O(1).** Over 5000 random configurations: median |C| = 0.06, 90th percentile 0.23, 99th 0.51. So κ ≈ 0.1·λ typically. This *worsens* the suppression by one order relative to the kickoff's "O(1) matrix-element ratio" expectation.
2. **Equal-intensity interferometers are blind to this nonlinearity.** If a_A = a_B = a_C, all n_i coincide within each configuration, the nonlinearity is a pure global phase per configuration, and **I₃ = 0 exactly (all orders in λ)** in the diagonal model. All-real relative phases likewise kill the O(λ) term (I₃ = O(λ²), verified). **Experiment-design consequence:** symmetric three-slit experiments (the Sinha-type geometry with equal openings) have suppressed or vanishing sensitivity to density-coupled nonlinearity; an optimal test uses *deliberately asymmetric* path intensities and a scanned relative phase near Δφ = π/2. This is a publishable methodological remark independent of the framework's fate. [derived here; model-dependence flagged: with path-mixing H ≠ 0 the exact null relaxes to O(λ²) suppression]
3. κ is linear in the traversal time τ through λ = gτ/ħ: long-coherence platforms (atom interferometry, τ ~ 1 s) beat fast ones (photon benches, τ ~ ns) by ~10⁹ for fixed g.

## 2. Step 2 — the scale of g [derived estimates; the ansatz g = g(GV) flagged throughout]

What κ = 10⁻² requires, taking the favorable |C| ~ 0.1 (so λ_req = 0.1):

| Platform | τ | g required for κ = 10⁻² |
|---|---|---|
| Photon bench | ~1 ns | ~7 × 10⁻⁸ eV |
| Atom interferometer | ~1 s | ~7 × 10⁻¹⁷ eV |

What gravitational/topology-change origin supplies:

- **Massive matter waves (Schrödinger–Newton scale):** g ~ Gm²/L. Cs atom, path separation L = 1 mm: g ≈ 2 × 10⁻³⁸ eV ⟹ λ(τ = 1 s) ≈ 3 × 10⁻²³ ⟹ **κ ~ 3 × 10⁻²⁴**.
- **Photons (E/E_P):** 1.5 eV/1.22 × 10²⁸ eV ⟹ **κ ≲ 10⁻²⁹**.
- **JUNO reactor neutrinos:** E/E_P ~ 3 × 10⁻²² ⟹ **κ ~ 10⁻²³** (before the |C| factor).

**Shortfall: 10²¹–10²⁷, platform-dependent.** Consistent with phase 27's table; the explicit coefficient makes it slightly worse (the |C| factor). An **independent, framework-free cross-check [established (others') — citation to be verified in audit]:** hyperfine spectroscopy bounds on generic Hamiltonian nonlinearities of Weinberg type are at the ~4 μHz ≈ 2 × 10⁻²⁰ eV level (Bollinger et al. 1989, ⁹Be⁺; comparable H-maser bounds). The g ~ 7 × 10⁻¹⁷ eV needed for κ = 10⁻² at τ = 1 s is **~4 × 10³ above that existing bound** — so even an unspecified mechanism delivering the required g is already excluded by 1989-era data *unless* it couples exclusively to spatial which-path densities and leaves internal-state superpositions untouched. Any surviving proposal owes an explanation of that selectivity.

## 3. Step 3 — the enhancement routes, closed one by one

The kickoff names three candidate evasions of Planck suppression. Each is assessed against the framework's own established structure.

**(i) "Large GV." [blocked — interpretation-level, two independent reasons]** Numerically, κ ~ GV·(E/E_P) would need GV ~ 10²¹–10²⁷. (a) *Structural:* by L1 (phase 33), GV is a secondary invariant with **no local density** — there is no local operator for a large global GV to multiply; the magnitude of a global invariant does not propagate into a local coupling in a lab-scale, locally-product region of the foliation. This is the near-theorem closure. (b) *Cross-observable:* the framework's own Chishtie-bridge consistency (phase 27 §5a) puts GV ≳ 1 with O(1) values for Planckian folding, and in the AMK channel the *same* modulus feeds Λ and m_H; a GV of 10²¹ would destroy those sectors. The framework cannot buy κ with GV without bankrupting its other accounts.

**(ii) "An IR-not-UV scale." [blocked — arithmetic]** The most generous IR scale available to the framework is cosmological: g ~ ħH₀ ≈ 1.4 × 10⁻³³ eV ⟹ λ(τ = 1 s) = H₀τ ≈ 2 × 10⁻¹⁸ ⟹ κ ~ 10⁻¹⁹. Even the Hubble scale falls short by 17 orders. The g required (≈10⁻¹⁶ eV) corresponds to a characteristic time ħ/g ~ 10 s — a mesoscopic scale that **nothing in the framework supplies**: its primitive scales are ℓ_P and cosmological, and the window between is empty. [derived]

**(iii) "Non-perturbative / topology-change-rate enhancement." [blocked — self-consistency]** If discrete topology-change events at rate Γ each impart O(1) nonlinear phase, κ ~ Γτ, and κ = 10⁻² needs Γτ ~ 10⁻¹ (with |C| ~ 0.1). But the same events perturb *ordinary two-path interference at the same order*: fringe-visibility stability in atom and photon interferometry is verified at the 10⁻³–10⁻⁴ level over the same τ, so (rate × strength) is already bounded at or below the current κ sensitivity — this route can never put I₃ *ahead* of what I₂ visibility already constrains. At the other extreme, AMK's own gravitational-decoherence estimate (T_dec ~ 10⁻²⁴ s, 1601.06436 §11) with O(1)-strength events would destroy all observed interference; consistency with observed I₂ forces each event's nonlinear effect to be tiny, which re-suppresses κ. [derived, order-of-magnitude]

**(iv) The in-house closure, restated (strongest).** Independently of all scale estimates: phase 32's M0b makes the Born rule a *theorem* on the framework's event lattice, and REVIEW §1.1 stands — the constructed framework contains no nonlinear dynamics at all. κ ≠ 0 is not suppressed in-house; it is **absent**. The conditional BHMM bridge (phase 26 §2) is the only route to κ ≠ 0, it remains a conjectured analogy with an identified category error at its center, and even granting it, (i)–(iii) close the magnitude.

## 4. The decision (kill test §5, row 1 — triggered)

> **NO-GO on the κ channel.** [derived, this phase + record]
>
> The framework as actually constructed predicts **κ = 0 exactly** (Gleason/M0b; linear modular dynamics). On the most favorable conditional reading (BHMM bridge granted, ansatz g = g(GV) granted), κ ≲ 10⁻¹⁹ under every enhancement route, with typical platform values 10⁻²³–10⁻²⁹ — at least 17 orders below the 10⁻² window, and each of the three named evasions independently blocked, one of them (large GV) by the framework's own locality principle L1. **Sorkin interference is not, and cannot become, this framework's measurable distinctive prediction.**

Per the kickoff's own kill table: *on this channel* the framework yields no measurable distinctive prediction. Stated without softening, as instructed — and the anticipated "most likely outcome" (kickoff's closing note) is confirmed, now with the explicit coefficient and the loophole closed rather than presumed.

**What this does *not* kill (per phase 27, unchanged):** the null itself is a falsifiable commitment — **P3: every current and planned I₃/α experiment must return null; any confirmed κ ≳ 10⁻⁶ (JUNO now taking data; photonics; atom interferometry; clocks) falsifies the framework** in both its in-house and conditional versions. The framework's live measurable physics remains where phase 27 put it: P1 (w₀, wₐ) = (−1, 0) under active fire (Euclid DR1, late 2026); P4a (w_DM = 0); P2 GW zero-anomaly commitments; P6 desk tests. The "is it physics or interpretation?" question is therefore *not* settled negatively overall — it has moved entirely onto the cosmological rigidities and the desk program, and phase 27's decision calendar is unaffected.

**Consequence for 2A (kickoff §3, per §7's ordering):** with 2B returning a no-go, the in-room case for pushing the full 2A variational principle now is void — its purpose was to justify a coupling whose observable consequence is unmeasurable. 2A's standing value is unchanged but re-scoped: it is the T1/M3 track (phase 36's two theorem layers + the single scale normalization), whose payoff is **deriving G and the ¼ in S = A/4G**, not κ. That is where the mechanism work should resume, and it already has a sharper statement than the kickoff's (phase 36 §3.1 supersedes kickoff §3's formulation).

**The expert kernel, updated:** unchanged from phase 36 ([E1] Hurder–Katok converse landscape; [E2] the Connes pairing i_δ(d/dt)[V/F] = GV; [E3] well-posedness of the two scale relations), *plus one item from this session:* **[F1]** verify the Weinberg-nonlinearity spectroscopy bound citation and its applicability class (Bollinger et al., PRL 63 (1989) 1031 — value quoted here from memory at order-of-magnitude confidence; the §2 cross-check argument needs the exact figure and scope).

## 5. Audit table (this phase)

| # | Item | Where | Confidence | Ask |
|---|---|---|---|---|
| F1 | Weinberg-nonlinearity bound ~2×10⁻²⁰ eV (Bollinger 1989; H-maser) — exact value and scope | §2 | medium (memory) | verify citation; does it constrain density-coupled (which-path-only) nonlinearities? |
| F2 | Model-dependence of the equal-intensity exact null (§1.3.2) under path-mixing H ≠ 0 | §1.3 | high for O(λ) suppression; exact null is diagonal-model-only | short calculation, any theorist |
| F3 | L1-based closure of route (i): formalize "no local density ⇒ no local effective coupling ∝ GV" | §3(i) | medium-high (structure clear; not a written theorem) | operator-algebraist / foliation geometer — same expert as E2 |

## 6. Sources

- TIER-2-KICKOFF.md (§4–5, the protocol executed here); phase 27 §3 (P3); phase 31 §0; phase 32 (M0b); phase 33 (L1, L2); phase 36 (T1 decomposition); REVIEW-phys-docs-2026-07-11 §1.1.
- BHMM, "Gravitizing the Quantum," arXiv:2203.17137 (`2203.17137v1.pdf` in folder).
- Sorkin, Mod. Phys. Lett. A 9 (1994) 3119; Sinha et al., Science 329 (2010) 418; Park et al., NJP 14 (2012) 113025; JUNO triple-path, arXiv:2105.14061.
- Weinberg nonlinear QM: Ann. Phys. 194 (1989) 336; precision bound: Bollinger et al., PRL 63 (1989) 1031 **[F1 — verify]**.
- Computation archive: `i3_calc.py` (symbolic/numeric verification, this session).

---

*Status line: Tier 2's Problem 2B is executed and decided — the fast go/no-go returns **no-go**, exactly as the kickoff's honest note anticipated, now with the leading-order coefficient computed (κ = C·gτ/ħ, |C| ~ 0.1, with an exact equal-intensity null carrying a genuine experiment-design corollary), the required g quantified against platforms, and all three enhancement loopholes closed — one by the framework's own L1. The κ channel is retired as a prospective fingerprint and retained as the theorem-backed null commitment P3. The mechanism work (2A) folds into T1/M3 per phase 36, aimed at G and the ¼, with the expert kernel E1–E3 + F1–F3.*
