# Phase 53 — T-M1b executed: the wrong test, the right cancellation, and the flatness sum rule

*Working session, 2026-07-17. Executes T-M1b (phases 51/52): does the protected-stratum pairing cancel the moduli potential at one loop? The session's first result is a correction to its own assignment — the test as posed in phase 52 was the wrong test — and working out why converts the mechanism into something sharper than what was asked for: an exact bulk cancellation, a computable quantized residual, and a **Diophantine sum rule on the fold's spectrum** that decides one-loop flatness. The mechanism survives, refined; it is not yet confirmed, and the reason it can't yet be is named precisely.*

---

## 1. The wrong test, recorded first

Phase 52 proposed checking whether the signed species sum of ZT coefficients c(n) = 6n²−6n+1 cancels for paired content, with the natural "superpartner" guess (n, n+½). Computed: c(n) − c(n+½) = 3/2 − 6n ≠ 0 for every physical weight. Taken at face value this would kill the mechanism. **It is instead the wrong test**, and the reason is the actual structure:

**The bulk cancellation is exact and does not depend on ZT coefficients at all.** A supersymmetric pair on the fold is built from one operator: the partner Laplacians ∂̄ₙ*∂̄ₙ and ∂̄ₙ∂̄ₙ* are **isospectral away from their kernels** [established, elementary]. So the boson and fermion log-determinants cancel *pointwise on moduli space*, identically — not approximately, not coefficient-by-coefficient. The entire nonzero tower drops out of the free energy.

**What survives is the zero modes.** The Quillen metric factorizes as (L² metric on the index/zero-mode line) × (det′ factor); when the det′ factors cancel pairwise, the residual moduli dependence of the paired free energy is exactly the **curvature of the index bundle with its L² (Hodge) metric** — and by two applications of the ZT theorem, that residual is computable as the *difference* of ZT coefficients. The 3/2 − 6n that "failed" the naive test is not a failure: **it is the residual force coefficient — the protected states' own contribution, quantized.** [derived; audit item **M-aud1**: the factorization step written out for a specialist — the G1 discipline]

## 2. The structure that falls out

- **Bulk spectrum: exactly flat.** For any ∂̄-paired content, the one-loop force from the entire nonzero spectrum vanishes identically. The phase 52 mechanism's core is *better* than proposed: cancellation is exact by isospectrality, not approximate by coefficient tuning.
- **Residual force: quantized.** The surviving force on the modulus comes only from the protected (zero-mode) sector, with universal rational coefficients in units of ω_WP/12π²: per shifted-weight multiplet, 3/2 − 6n (= +3/2, −3/2, −9/2, −15/2 at n = 0, ½, 1, 3/2). *The protected states do exert a force, and its strength is a topological rational — not a tunable number.* [derived, modulo M-aud1; half-integer-weight ZT normalization flagged **M-aud2**]
- **The dichotomy.** Same-weight pairing (genuine SUSY doubling, QM-type — the Morse/Floer complex's internal pairing) ⟹ residual zero: **exact one-loop flatness**. Shifted-weight (geometric, spin-raising) pairing ⟹ the quantized residual above. Which pairing the fold's physical spectrum realizes is exactly the dictionary question (phase 52 §4's prerequisite) — undecidable in-room, now carrying the entire weight.

## 3. The flatness sum rule [the phase's main deliverable]

One-loop flatness of the full moduli potential is equivalent to:

> **Σ_bosons c(n_B) = Σ_fermions c(n_F), with c(n) = 6n²−6n+1.**

Computed structure of the solution space:

1. **Low-weight content cannot cancel.** With only the "ordinary" weights — bosons at n = 0, 1 (c = +1) and fermions at n = ½ — cancellation is *impossible*: c(½) = −½, so fermions at n = ½ contribute −c = +½ — **everything adds**. A fold spectrum of ordinary matter is necessarily non-flat at one loop.
2. **Cancellation requires same-weight doubling or high-weight fermions.** ~~Nontrivial solutions need fermions at n ≥ 3/2~~ **[ERRATUM, 2026-07-18, fresh round two (phase 79 FR2-5): FALSE as stated. The sum rule is c_total = 0, and the bosonic string solves it at integer weights: 26 weight-0 bosons against the anticommuting bc system at n = 2 — 26 = 2×13, precisely the Mumford exponent this record itself cites. Weight-1 fermionic first-order systems (c(1) = 1) likewise cancel scalars. The "n ≥ 3/2" conclusion smuggled in an unstated spin-statistics restriction on the fold spectrum. What survives: weight-3/2 content is *one solution class among several* (and, as phase 54 already conceded, it is superghost-shaped — present in type 0 strings with no spacetime fermions). The sentence "the sum rule is gravitino-shaped... demands supergravity-multiplet-like weight content" is WITHDRAWN; the sum rule demands nothing beyond c_total = 0. Downstream: CRITICAL-2's bosonic/super fork loses its "phase 53 demands superghosts" premise (the ST-0 arithmetic of phase 71 stands as arithmetic); SPIN-1's first thread (phase 78) is dead — see the phase 78 rewrite.]** The computed examples stand as examples (11 scalars + 2 weight-3/2 fermions → 0; graviton-weight + weight-3/2 → residual 3), stripped of the false necessity claim.
3. This is the fold-side sibling of P7: phase 49 constrained the *matter content* by induced-gravity positivity; the sum rule constrains the *fold spectrum* by moduli flatness. Two spectral constraints from two independent one-loop computations — the framework now has a small system of Diophantine conditions any candidate content must satisfy simultaneously. [The pair (P7, sum rule) as a joint constraint is logged as a target: does any realistic content satisfy both? — **T-M1b2**, a finite check once the dictionary exists.]

## 4. Kill scoring and the honest boundary

- **Mechanism: alive and sharpened, not confirmed.** The phase 52 kill condition ("cancellation fails ⟹ dead") is *not* triggered — cancellation is exact for the bulk and achievable for the residual — but confirmation requires the dictionary: which weights, and which pairing type, the physical content realizes on the fold. That is L1-aud territory (specialist) plus the phase 49 dictionary made determinant-level.
- **If the dictionary lands on shifted-weight with nonzero sum:** the potential is *reduced but nonzero with quantized strength* — the modulus mass becomes computable rather than tunable, which is a better outcome for falsifiability than exact flatness (exact flatness would reopen the "what lifts it at two loops" regress). Noted: the mechanism's most predictive branch is the one where it *partially* fails.
- **Beyond one loop: untouched.** The 10⁻⁶⁰ problem is addressed here only at one loop; the sum rule is a necessary structure, not a solution. Phase 52 §5's boundary stands word for word.
- New audit items: **M-aud1** (Quillen factorization/residual-curvature step), **M-aud2** (half-integer ZT normalization), **T-M1b2** (joint P7 + sum-rule satisfiability). The specialist packet grows by exactly these.

*Status line: T-M1b returned more structure than it was asked for — an exact isospectral bulk cancellation, a quantized residual force owned by the protected states themselves, and a flatness sum rule whose solutions are gravitino-shaped. The decisive problem now has a spectral criterion where it had a hope; the criterion's input (the dictionary) is the same one item everything else waits on; and the program has learned to distrust its own most elegant day twice in a row — this document's first section is the receipt.*
