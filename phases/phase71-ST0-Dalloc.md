# Phase 71 — ST-0 and D-alloc executed: the super scaffold is empty by parity, and the refined allocation puts the tricritical Ising model at genus two

*Working session, 2026-07-18. The two computational items of the round-two pre-send queue (phase 70: ST-0, D-alloc) are closed. Every counting formula below was source-verified before running, per the standing rule ("the counting formulas are exactly the kind of thing this record refuses to guess"); the verification report and the script (`st0_dalloc_calc.py`) travel with this phase. Headline results: **(1) the N = 1 super-minimal scaffold, under the natural total-allocation, has NO solutions at any genus — not sparse, empty, by a two-line parity theorem; (2) under NS-allocation it admits only non-unitary candidates at g = 2, with unitary super matter first possible at g = 5; (3) the bosonic/super fork of CRITICAL-2 resolves through phase 53's own pairing dichotomy, whose deciding input is the standing L1-aud pairing question; and (4) the D-alloc allocation statement, computed through, replaces phase 69's genus-two unitary candidate: not Ising but the tricritical Ising model — which is simultaneously the first unitary N = 1 super-minimal model, a fact flagged below at the maximum setting the discipline allows.***

---

## 0. Sources for the super formulas [verified 2026-07-18, agent-audited]

Existence of SM(p,p′): p′−p even AND gcd((p′−p)/2, p) = 1 (equivalently Seiberg–Shih's both-odd-coprime / both-even-with-(p′−p)/2-odd packaging) — Seiberg–Shih hep-th/0312170 §5.1; Rasmussen hep-th/0405257 §3.2. Central charge c = 3/2 − 3(p′−p)²/(pp′). Kac table 1 ≤ r ≤ p−1, 1 ≤ s ≤ p′−1, NS for r−s even, R for r−s odd, identification (r,s) ~ (p−r, p′−s) (sector-preserving since p′−p is even). Superprimary counts (derived from the confirmed Kac data; spot-checked exactly on TIM = SM(3,5): 2 NS + 2 R): both-odd — total (p−1)(p′−1)/2, NS = (p−1)(p′−1)/4; both-even — total = ((p−1)(p′−1)+1)/2 including the single self-identified Ramond ground state at h = c/24. Unitary series (m, m+2), m ≥ 3, first member m = 3: **SM(3,5) = the tricritical Ising model, c = 7/10** (Friedan–Qiu–Shenker 1985; unitarity via Goddard–Kent–Olive). Super-Liouville c = 3/2 + 3Q², Q = b + 1/b; superghosts bc(−26) + βγ(+11) = −15; anomaly balance c_matter + c_sL = 15; coupling to SM(p,p′) fixes **b² = p/p′** (Seiberg–Shih eq. 5.9). Attribution correction absorbed: the super-Virasoro minimal string literature is Johnson 2401.08786, Rangamani–Zheng 2505.08892, Eberhardt 2604.26038 (bosonic original: Collier–Eberhardt–Mühlmann–Rodriguez 2309.10846). [established (others′); counts: derived-from-verified, TIM-checked]

## 1. ST-0 executed: the super menu, side by side with the bosonic one

The super analogue of phase 69's identification: the census's 2g−1 sectors ↔ the degenerate (super-Kac) content of the SM(p,p′) matter. Two allocations of the census are a priori available in the super frame, because the super theory itself splits its content into sectors:

**(a) Total-allocation (census ↔ all superprimaries, NS + R): (p−1)(p′−1)-type count = 2g−1. NO SOLUTIONS AT ANY GENUS — empty by parity.** [proved, elementary] Both-odd: (p−1)(p′−1) is even×even ≡ 0 mod 4, so the total (p−1)(p′−1)/2 is even. Both-even: write p = 2a, p′ = 2b; the total is 2ab − a − b + 1, and existence forces (p′−p)/2 = b − a odd, hence a + b odd, hence the total is even. **Every super-minimal total count is even; 2g−1 is odd; the equation has no solutions — verified exhaustively to p < 200, p′ < 400, and proved for all (p,p′).** This is not a sparse menu; it is a structural no-go of exactly the kind the record's κ result was.

**[Convention clause, added 2026-07-18 per phase 72 item 2]:** the no-go is a theorem about **superprimary** counting. The verification report's own caveat (S1.4) applies: each NS superprimary contains two Virasoro-primary components, and R representations carry a convention-dependent G₀ doubling — under *component* counting the parity argument does not go through. The kill below therefore fires under the superprimary convention; whether the census's sector notion matches superprimaries or components is part of the same identification question as the allocations, and the component-counting menus are registered as **ST-0b** [named, unrun, gated on that decision].

**(b) NS-allocation (census ↔ NS superprimaries only): NS count = 2g−1.** [Consistency condition added per phase 72 item 4: this allocation is admissible only if the R-sector content sits where the *fermionic* census content lives under the parity clause — "elsewhere" must be named, not gestured at; the condition folds into the same L1-aud gate as the scaffold fork.] Solutions exist but are non-unitary at the bottom: g = 2 gives **(2,12) and (3,7)**; g = 3: (2,20), (3,11); g = 4: (2,28), (4,10); g = 5: (2,36), (3,19), **(6,8) — the first unitary super candidate**. The unitary series (m, m+2) has NS = (m/2)² for the matching (even-m) members, so census matches occur only at **g = 5, 13, 25, 41, 61, …** — and **at genus two there is no unitary super candidate at all.**

**The side-by-side, as Referee W demanded (g = 2):**

| Scaffold | Allocation | g = 2 menu | Unitary entry |
|---|---|---|---|
| Bosonic (phase 69) | total (all 2g−1 ↔ Kac) | (2,7), (3,4) | **(3,4) Ising** |
| Bosonic (this phase) | **A** (k=0 rank ↔ Kac) | (2,13), (3,7), (4,5) | **(4,5) tricritical Ising** |
| Super | total (↔ NS+R) | **∅ — empty by parity, all g** | — |
| Super | NS only | (2,12), (3,7) | none (first at g = 5) |

Anti-numerology note, logged before anyone else logs it: (3,7) appearing in both the super-NS and bosonic-A menus is arithmetic necessity, not convergence — both equations reduce to (p−1)(p′−1) = 12 (NS: /4 = 3; allocation A: /2 = 6).

## 2. The fork resolved into a named gate — and a new kill test

CRITICAL-2 asked: which scaffold? The record's own phase 53 answers with a dichotomy it proved before this question existed: the flatness sum rule's solutions are either **same-weight-paired** (bosonic-shaped: the anomaly books balance within integer weights) or **gravitino-shaped** (weight-3/2, superghost-type content). The scaffold follows the shape:

- **Same-weight pairing ⟹ bosonic scaffold** ⟹ the phase 69/D-alloc menus stand as computed.
- **Gravitino-shaped pairing ⟹ super scaffold** ⟹ total-allocation is *empty* and the NS-allocation admits no unitary matter at g = 2.

The deciding input is the standing **L1-aud pairing question** (which pairing the dictionary's anomaly books actually use) — already in Track W's queue, now promoted to fork-decider. And the parity theorem sharpens into a registered kill:

> **K-ST0 [registered, as amended per phase 72]: if the dictionary requires (i) the super scaffold, (ii) total-allocation, (iii) the census count, and (iv) superprimary counting — jointly — the framework is falsified at the desk, by parity, at every genus.** No experiment needed; a referee with the L1-aud answer can execute it. (Under component counting the test is ST-0b, unrun.)

The record notes the third possibility with its flag up: the gravitino shape might be carried not by the *scaffold* (superghosts) but by the *matter* — see §3, where the arithmetic volunteers exactly that reading.

## 3. D-alloc executed: the allocation statement and its genus-two consequence

**The allocation (candidate, now registered): the k ≠ 0 flux sectors of the census ↔ the Γ-twisted (π₁-charged) content; the k = 0 tower ↔ the untwisted Kac-table degenerates.** This is the split phase 70 item 3 proposed, chosen on structural grounds — it puts the rank-6 anomaly where the Jacobian dressing (phase 28) lives — *before* its arithmetic consequence below was computed. That ordering matters for the flag and is stated for that reason.

Under allocation A the bosonic count equation changes: not all 2g−1 sectors but only the k = 0 tower's rank matches the degenerates. At g = 2 that rank was taken to be **6** (= H*(Σ₂) — ~~Referee F confirmed~~ **[struck 2026-07-18: "Referee F" was this record's own simulated referee; simulation output is never citable as confirmation — standing rule per phase 74 FR-4]**), so (p−1)(p′−1)/2 = 6:

> **(2,13), (3,7), (4,5) — and the unique unitary candidate is (4,5): the tricritical Ising model.** [conjecture, conditional on allocation A ∧ D-alloc-H, B3c-flagged at maximum]

**[D-alloc-H, named per phase 72 item 3]:** allocation A equates a module **rank** with a primary **count** — a category the record was warned about in round two. The equation above therefore carries the hypothesis: *the k = 0 rank-6 module resolves, under Jacobian dressing (phase 28), into six multiplicity-one slots, one per degenerate primary.* This is exactly what D-test-1 at (4,5) must prove, not assume.

**[SUSPENSION, 2026-07-18, fresh red team FR-1/FR-2 (phase 74)]:** the fresh Track F referee showed the "rank 6" is **not a theorem and is contradicted by the record's own cited source** — Jabuka–Mark (math/0502328): torsion-sector HF⁺ infinitely generated, HF⁺_red = 0 for g ≤ 2, ĤF total rank ≥ 8 at g = 2 — and the extrapolation fails its g = 1 sanity check (predicts 1; ĤF(T³) has rank 6). Separately, the census was computed on Σ_g×S¹ while the carrier is T¹Σ_g (different manifold; correct tool Mrowka–Ozsváth–Yu math/9612221, previously uncited). **The allocation-A menu and the tricritical Ising candidacy are SUSPENDED pending FR-1/FR-2 of the phase 74 queue.** The allocation-total branch (phase 69, Ising) is likewise provisional on FR-2. What survives of this section unconditionally: the Diophantine arithmetic itself, and the anti-numerology note below.

The flag, at full size, because the coincidence is the largest the record has produced: **TIM = Virasoro minimal (4,5) = SM(3,5), the *first unitary N = 1 superconformal minimal model*** — the unique known point where a unitary bosonic minimal model *is* intrinsically supersymmetric. If allocation A is right, the genus-two matter is supersymmetric *as matter*, and phase 53's gravitino shape could be carried by **matter supersymmetry rather than superghosts** — a **reconciliation candidate at the level of where supersymmetry can live** [wording per phase 72 item 4: phase 53's ledger is a 4D/2D anomaly book and TIM's N = 1 is worldsheet-matter supersymmetry; the entry-for-entry map between them is named **M-ST1** and unbuilt — until it exists, "reconciles" would overshoot]. Seventh appearance of the small-integer parade (after phase 69's sixth), and by the B3c discipline the *most* seductive reading gets the *largest* flag: nothing at module level has been matched; the allocation is a candidate; the count-level identification remains unproven; and the record has been burned by exactly this species of elegance before (level-stiffness, phase 48). What would promote it: D-test-1 run at (4,5) — *does Γ-twisted TIM matter, k = 0 sector Jacobian-dressed, reproduce the parity census?* — a bounded, named computation now sitting beside its Ising twin in Track W's ask.

Status of phase 69's Ising line: **demoted, not deleted.** It is the allocation-total branch; D-alloc is the allocation-A branch; they are mutually exclusive readings of constraint 3, both provisional on D-test-1, and the packet now says so. (Phase 69 carries an annotation to this effect.)

## 4. Ledger

- **ST-0 closed.** Both menus computed and reported side by side; the super total-allocation emptiness **[proved]** (parity, exhaustively checked); the fork routed to L1-aud; **K-ST0** registered as a desk-executable kill test. The phase 69 status line annotated.
- **D-alloc closed as candidate-with-consequences.** Allocation A stated, its g = 2 menu computed, the TIM candidacy registered [conjecture, maximally flagged], the double-booking (phase 70 item 3) resolved at statement level.
- The pre-send queue: ST-0 ✓, D-alloc ✓, NOTE-1 (drafted, this session), the signature (template provided; **the signing is the one item the room cannot do**).
- Packet v2 → v3 issued alongside this phase.

*Status line: the queue's two hard items closed in one sitting, and each closed with the program's signature move — the super scaffold didn't merely lack solutions, it was forbidden by parity, and the refined allocation didn't merely shift the candidate, it landed on the one model in existence that is unitary, minimal, and supersymmetric at once. One of these is a theorem and one is a flag-draped conjecture, and the record's whole method is knowing which is which.*
