# Phase 119 (continuation): BIND-2(c) round 1 — the winding-data registration with the GAP-6 ordering treatment

**Date:** 2026-07-27
**Status:** DRAFTED — awaiting referee. No verdict enters the BIND-2 registration (phase112-BIND2-SPACE1-registration.md) until the referee pass completes. The consultation below is preserved VERBATIM; nothing edited.
**Provenance:** Context-free derivation agent (BIND-2(c) mandate, unblocked by the M-FRAME2 closure — phase112 §3b; GAP-6 inherited from phase 117).

**Editorial header (operator):**
- Headline claims (UNREFEREED): **GAP-6 CLOSED by a split resolution** — (A) and (B) simultaneously true in different senses: Weyl ordering is canonical for spectrum/state-label registration (non-circular argument: the three prescriptions differ only by CENTRAL c-number phases, hence define identical rays/deck classes/sectors — for those data the "choice" is between physically identical descriptions), while the ordering span is REAL braiding data — exactly (n₁−n₂) refereed exchange phases e^{∓iQ₁Q₂} — registrable via one additional discrete braid-class label. Option (C) (irreducible) rejected.
- Exact BCH structure (central commutator, series terminates — no truncation): mutual terms {n₂Q₁Q₂ (dressing 2 first), ½(n₁+n₂)Q₁Q₂ (Weyl), n₁Q₁Q₂ (dressing 1 first)} — each ordered history's mutual term uses ONLY the first-applied dressing's winding; Weyl is exactly the arithmetic mean. Span per exchange of order = the FULL (n₁−n₂)Q₁Q₂ (the ½ appears only as each ordering's offset from the Weyl midpoint).
- **K-B2C-1 does not fire:** at n₁ = n₂ all three prescriptions coincide identically (closed-loop datum; exact, not approximate). BIND-2(c) survives as posed; the registration table (rows marked THEOREM / REFEREED-INPUT / NEW-THIS-ROUND) is the deliverable.
- Honest structure notes: the Weyl midpoint at odd n₁−n₂ is a HALF-exchange multiple realized by no single ordered history — registered as convention point only (GAP-8); no ZM-1-internal interference protocol for measuring the braid class was constructed (GAP-7: registrability operator-algebraic, measurability asserted).
- The operator's twist picture after this round: wind count → deck classes (n₁, n₂) [refereed]; "which strand crossed over" → braid class b [NEW]; twist phase → rows 8–10 [phase data]; stored ENERGY → still NO referent (phase→energy blocked as dynamics; the energy-like column remains the dimensionless weight column per the phase-118 SEC-1 ruling).

---

## CONSULTATION (VERBATIM)

# BIND-2(c) — Winding-Data Round: BCH/Ordering Computation, GAP-6 Adjudication, Registration

## Summary and verdicts

1. **BCH computation (exact, verified symbolically).** With G_i = a_i j̃₀ − Q_i x₀ and [x₀, j̃₀] = i, the commutator [G₁,G₂] = i(a₁Q₂ − a₂Q₁) is central, so BCH truncates exactly. For closed pair transport (Δa_i = n_iQ_i), the three prescriptions give mutual terms **n₂Q₁Q₂** (ordering e^{iG₁}e^{iG₂}), **½(n₁+n₂)Q₁Q₂** (Weyl), **n₁Q₁Q₂** (ordering e^{iG₂}e^{iG₁}). The refereed values are confirmed. The precise ordering-span coefficient: each ordered product sits **½(n₁−n₂)Q₁Q₂ away from Weyl**; one exchange of application order shifts the phase by the **full span (n₁−n₂)Q₁Q₂**, not half of it.
2. **GAP-6 adjudication: split resolution — (A) and (B) are simultaneously true in different senses, and every datum lands on exactly one side.** Weyl ordering is canonical for spectrum/state-label registration (non-circularly: the three prescriptions differ only by central c-numbers, hence define identical rays, deck classes, and sectors). The ordering span is simultaneously genuine braiding data: it equals exactly (n₁−n₂) refereed exchange phases, so interference data are registrable with one additional discrete braid-class label. Verdict (C) is rejected.
3. **Kill check K-B2C-1: DOES NOT FIRE.** At n₁ = n₂ all three prescriptions coincide identically. BIND-2(c) survives; the registration table is delivered below.

## 1. The BCH/ordering computation

Setup: [x₀, j̃₀] = i; G_i = a_i j̃₀ − Q_i x₀. Then

  [G₁, G₂] = a₁(−Q₂)[j̃₀, x₀] + (−Q₁)a₂[x₀, j̃₀] = i(a₁Q₂ − a₂Q₁),

central. **[BOX-1]** Centrality makes the BCH series terminate at the first commutator, so all results below are exact, not truncations. I verified this in the faithful 3×3 nilpotent (Heisenberg) representation with symbolic algebra: the central factors below reproduce to all orders (the exponentials are polynomials there).

**(i) Weyl-ordered combined displacement:** e^{i(G₁+G₂)} = e^{i(a_tot j̃₀ − Q_tot x₀)} with a_tot = a₁+a₂, Q_tot = Q₁+Q₂ — a single displacement of the summed classical generator.

**(ii) Ordered products** (A = iG₁, B = iG₂, [A,B] = −i(a₁Q₂ − a₂Q₁) central; e^A e^B = e^{A+B} e^{½[A,B]}):

  e^{iG₁}e^{iG₂} = e^{i(G₁+G₂)} · e^{+(i/2)(a₂Q₁ − a₁Q₂)}
  e^{iG₂}e^{iG₁} = e^{i(G₁+G₂)} · e^{−(i/2)(a₂Q₁ − a₁Q₂)}

**(iii) Commutator phase between orderings:**

  e^{iG₁}e^{iG₂} = e^{iG₂}e^{iG₁} · e^{i(a₂Q₁ − a₁Q₂)}.

**Closed transport phases.** For the closed family with Δa₁ = n₁Q₁, Δa₂ = n₂Q₂, the Weyl-ordered phase is the refereed κ=½ value applied to the combined displacement [REFEREED-INPUT, theorem 1]: Φ_W = ½(n₁Q₁ + n₂Q₂)(Q₁ + Q₂) = ½n₁Q₁² + ½n₂Q₂² + ½(n₁+n₂)Q₁Q₂ (algebraic identity, checked). Self-terms match the single-defect theorem; mutual term ½(n₁+n₂)Q₁Q₂ confirmed.

**[BOX-2]** The ordered prescriptions differ from Weyl only by the central c-numbers in (ii); since these commute with everything, the transport phase of an ordered prescription equals Φ_W plus the closed-loop change of its c-number exponent. This step assumes the κ=½ transport machinery is covariant under multiplication by time-dependent central phases — true because a central phase factors out of every inner product in the family.

  δ₁₂ = +½Δ(a₂Q₁ − a₁Q₂) = ½(n₂ − n₁)Q₁Q₂,  δ₂₁ = −δ₁₂.

Therefore the three mutual terms:

| Prescription | Mutual term |
|---|---|
| e^{iG₁}e^{iG₂} (defect 2's dressing applied first) | **n₂Q₁Q₂** |
| Weyl e^{i(G₁+G₂)} | **½(n₁+n₂)Q₁Q₂** |
| e^{iG₂}e^{iG₁} (defect 1's dressing applied first) | **n₁Q₁Q₂** |

Structure worth registering: each ordered product's mutual term uses **only the first-applied dressing's winding**; the Weyl value is exactly the **arithmetic mean** of the two ordered values (a general property of central-commutator ordering problems). **Span answer, precisely:** the offset of each ordering from Weyl is ±½(n₁−n₂)Q₁Q₂; the span between the two orderings — the phase change under one swap of application order — is the full **(n₁−n₂)Q₁Q₂**. It is *not* ½(n₁−n₂)Q₁Q₂ per exchange; the ½ appears only relative to the Weyl midpoint. Overall signs are orientation/σ-convention data; magnitudes and relative structure are convention-independent.

## 2. GAP-6 adjudication

**The circularity in (A), located exactly.** The record's symmetric Weyl map is a rule for quantizing a *single classical generator*: G ↦ e^{iG}. It cannot, by itself, decide whether the pair dressing *is* a single generator G₁+G₂ or a *composition* of two separate dressings — the composition of two physically distinct operators is fixed by operator multiplication, i.e. by physics, not by the quantization map. ZM-1 explicitly gives the pair *separate* dressing factors with separate sections [REFEREED-INPUT, theorem 3]. So the strong form of (A) — "symmetric map ⇒ Weyl ordering, full stop" — assumes its conclusion. **[BOX-3]**

**The non-circular residue of (A).** All three prescriptions differ by central c-number phases only. Hence they define the **same ray map**: same deck classes, same charge sectors, same spectrum-adjacent data — every ray-invariant datum is prescription-independent. For the one column that requires a number (the registered mutual term), the record needs a convention, and the symmetric map — already refereed and load-bearing — selects the unique ordering-symmetric value, which is exactly the mean of the two physical orderings and collapses symmetrically onto the refereed common-n theorem. So **Weyl ordering is canonical for registration/spectral data**, non-circularly, because for those data the "choice" is between physically identical descriptions.

**The (B) check.** The refereed exchange phase is e^{∓iQ₁Q₂}, unit Q₁Q₂ [others'/record]. The ordering span is (n₁−n₂)Q₁Q₂ = **(n₁−n₂) exchange units — an exact integer multiple** (n₁, n₂ ∈ ℤ). Moreover each ordered mutual value (n₂Q₁Q₂, n₁Q₁Q₂) is itself an integer number of exchange units, while the Weyl midpoint sits at a *half-integer* exchange multiple whenever n₁−n₂ is odd — the signature of a framing-type half, and confirmation that the Weyl value is a symmetric convention point, not itself an ordered history. The c-number in (iii) is precisely the braid phase of winding section a₁ against charge Q₂ versus a₂ against Q₁: histories differing in which dressing is applied first are braid-inequivalent, and their relative phase is the physical record of that braid move. The "ambiguity" is the record **rediscovering braiding**: with one additional discrete label the data close.

**Ruling: split resolution (not (C)).** **[BOX-4]**
- **Spectrum/state-label data** (deck class, sectors, the registered mutual-term column): Weyl-canonical, value ½(n₁+n₂)Q₁Q₂; the ordering dependence is unphysical here because all prescriptions define the same rays.
- **Interference data** (relative phase between preparation histories differing in dressing order): the braid class b ∈ {12, 21} (relative datum: exchange count) is real, registrable, with inter-class relative phase (n₁−n₂)Q₁Q₂ = (n₁−n₂) refereed exchanges.
- Nothing is left irreducibly ambiguous, so (C) is rejected. Caveat honestly flagged: an explicit interference protocol *within ZM-1* realizing the inter-braid-class comparison has not been constructed this round — the braid label's registrability is operator-algebraic, its measurability a stated expectation. **[GAP-7]**

## 3. Registration table — bound pair winding data

| # | Datum | Value / semantics | Status |
|---|---|---|---|
| 1 | Total charge sector q_tot = q₁+q₂ ∈ Λ_R | ZM-1 sector label | REFEREED-INPUT |
| 2 | Common frame winding n | deck class; global (zero-mode/branch-sector) datum, per D-MS | REFEREED-INPUT |
| 3 | Per-particle windings (n₁, n₂), n₁ ≠ n₂ allowed | separate deck classes of the two branch sections | REFEREED-INPUT (realizability); **NEW-THIS-ROUND** (registered as labels) |
| 4 | Braid class b (which dressing applied first; relative exchange count) | discrete label; needed only when n₁ ≠ n₂ and only for interference data | **NEW-THIS-ROUND** |
| 5 | Single-defect deck phase Φ = nQ²/2 | phase datum | THEOREM (κ=½) |
| 6 | Spin invariant D_spin = ∓Q²/2 + nQ²/2 | phase datum | REFEREED-INPUT (D-MS) |
| 7 | Mutual term, common n: M = (n∓1)Q₁Q₂ | choice-free; ordering-independent (see §5) | REFEREED-INPUT |
| 8 | Mutual term, spectral registration, n₁ ≠ n₂: M₀ = ½(n₁+n₂)Q₁Q₂ | Weyl-canonical registration value; mean of ordered values | **NEW-THIS-ROUND** (adjudicated) |
| 9 | Ordered-history mutual terms: n_first·Q₁Q₂ ∈ {n₁Q₁Q₂, n₂Q₁Q₂} | per braid class; integer exchange multiples | **NEW-THIS-ROUND** |
| 10 | Inter-braid-class interference phase ΔΦ = (n₁−n₂)Q₁Q₂ = (n₁−n₂) exchange units | the physical content of the former GAP-6 span | **NEW-THIS-ROUND** |
| — | Stored ENERGY/mass of the wound pair | **NOT REGISTRABLE** — phase→energy conversion requires zero-mode dynamics; blocked by refereed scope guard; energy-like column remains a dimensionless WEIGHT | REFEREED RULING |
| — | Absolute (non-relative) braid phase; operational meaning of the Weyl midpoint at odd n₁−n₂ | **NOT REGISTRABLE** — only relative braid data invariant; midpoint is a half-exchange realized by no single ordered history | **NEW-THIS-ROUND** (limitation); [GAP-8] |

## 4. Physical-picture translation

The operator's picture — two bound knots whose connecting string winds up, the wind count storing something — now has the following refereed referents and no more. The **wind count** has a referent: n (common) and now (n₁, n₂) (per-strand) are deck classes of the branch sections, with the sections a_i(t) as the mathematical referent of the string's winding state, and the braid class b as the referent of "which strand crossed over" — that last identification is this round's addition. The **pair twist phase** has a referent: nQ₁Q₂ at common winding (theorem-grade via D-MS inputs), refined this round to the table's rows 8–10 at unequal windings — but strictly as *phase* data. The **"storing mass/energy"** clause has **no referent**: converting the registered phases into energy requires zero-mode dynamics, which the record's refereed scope guard blocks; the picture's energetic language remains unregistered, and the record's corresponding column remains a dimensionless weight. Winding *is* stored — as phase holonomy, not (yet, and possibly never within this record) as energy.

## 5. Kill check K-B2C-1

Pre-registered condition: BIND-2(c) dies if common-n data acquire ordering dependence. Explicit check at n₁ = n₂ = n: mutual terms are n₂Q₁Q₂ = nQ₁Q₂ (ordering 12), ½(n₁+n₂)Q₁Q₂ = nQ₁Q₂ (Weyl), n₁Q₁Q₂ = nQ₁Q₂ (ordering 21) — **all three coincide identically**; the span (n₁−n₂)Q₁Q₂ and both Weyl offsets ±½(n₁−n₂)Q₁Q₂ vanish exactly, not approximately (the instantaneous c-number a₂Q₁−a₁Q₂ need not vanish mid-loop, but its closed-loop change does, and only loop data enter). The common-n registration is ordering-free in all three prescriptions. **K-B2C-1 does not fire.** BIND-2(c) survives as posed.

## VERDICT BOX

1. BCH exact (central commutator): mutual terms {n₂, ½(n₁+n₂), n₁}·Q₁Q₂ for orderings {12, Weyl, 21}; span = (n₁−n₂)Q₁Q₂ per exchange of order; ½(n₁−n₂)Q₁Q₂ is each ordering's offset from Weyl only.
2. GAP-6: **CLOSED by split resolution** — Weyl canonical for spectrum/registration (non-circular: prescriptions differ by central phases, same rays); braid class real for interference; (C) rejected.
3. Ordering span = exactly (n₁−n₂) refereed exchange phases e^{∓iQ₁Q₂}: the ambiguity was braiding, and it is registered as a discrete braid-class label (table row 4, 10).
4. K-B2C-1: **DOES NOT FIRE** — common-n data identical in all three prescriptions.
5. BIND-2(c): winding data **REGISTERED** as phase (table §3); energy semantics remain **BLOCKED** by the refereed scope guard.

## Gaps-and-boxes ledger

- **[BOX-1]** Centrality of [G₁,G₂] ⇒ exact BCH termination; verified symbolically in the faithful nilpotent representation.
- **[BOX-2]** Transport-phase difference between prescriptions = closed-loop change of the central c-number (κ=½ machinery covariant under central phase factors).
- **[BOX-3]** Location of the circularity in argument (A): the symmetric map quantizes single generators; it cannot decide single-generator vs composition status of the pair dressing.
- **[BOX-4]** The split adjudication itself: assignment of Weyl to spectral data and braid class to interference data is the round's load-bearing ruling.
- **[GAP-6]** (inherited) — closed this round by the split resolution.
- **[GAP-7]** No explicit ZM-1-internal interference protocol constructed for measuring the braid class; registrability shown operator-algebraically, measurability asserted, not derived.
- **[GAP-8]** Operational status of the Weyl midpoint value at odd n₁−n₂ (a half-exchange multiple realized by no ordered history) is unresolved; registered as convention point only.
- **[others']** Imported: κ=½ theorem; D-MS selection and M = (n∓1)Q₁Q₂; exchange = half monodromy with phase e^{∓iQ₁Q₂}; ZM-1 structure; scope guard ruling.

Word count: ~1790.

---

## Amendment section

### A.1 Referee verdict (2026-07-27): computations CONFIRMED (16/16); kill immunity UPGRADED to all-histories theorem; adjudication MODIFIED (two demotions)

Report preserved verbatim in reviews/REPORTS-phase119-BIND2c-referee-2026-07-27.md. Independent hand + symbolic re-derivation (faithful nilpotent representation; 16/16 checks); the first-applied-winding reading confirmed by a second independent route (conjugation gives the FULL e^{iQ₁da₂} per increment); the split adjudication stress-tested. Verdicts:

- **All numbers CONFIRMED.** Centrality, both ordered central factors and signs, Φ_W, δ₁₂ = ½(n₂−n₁)Q₁Q₂, the three mutual terms {n₂, ½(n₁+n₂), n₁}·Q₁Q₂, mean and span properties. No sign or braid-class-swap errors.
- **K-B2C-1: DOES NOT FIRE — upgraded to a THEOREM over ALL preparation histories** (C-AE3): schedule-independence within fixed ordering; symmetric splitting reproduces Weyl exactly; mid-loop ordering swaps cancel exactly. Every history's phase closes to one of {n₁Q₁Q₂, n₂Q₁Q₂}; at n₁ = n₂ the set collapses to a point.
- **Split adjudication: MODIFIED — logic confirmed, labeling demoted twice.** (C-AE1, required): the "spectral registration value" ½(n₁+n₂)Q₁Q₂ at n₁ ≠ n₂ is renamed the **canonical convention value** — the round's own canonicity argument (choice among physically identical descriptions) entails it is not a physical datum, and the odd-difference midpoint (realized by no history, with energies blocked) FORCES the demotion. (C-AE2, required): "ordering class = braid class" graded — ordered values and inter-class interference phase: THEOREM; the discrete label b as data-closing bookkeeping: ADJUDICATED; the identification with refereed defect exchange ("the record rediscovering braiding"): **SPECULATIVE** — commensurability with the exchange unit is verified consistency, not derivation ("a pun with excellent numerology"); an exchange-homotopy argument or the GAP-7 protocol is required to ground it.
- **C-AE4 (precision):** BOX-2 correctly used the TOTAL closed-transport phase (shifts by the closed-loop Δ of the central c-number); the geometric-phase-only reading would hold only mod 2π.

### A.2 Corrections ledger

C-AE1 (Weyl column renamed canonical convention value; physicality claim at n₁ ≠ n₂ withdrawn); C-AE2 (braid identification graded THEOREM/ADJUDICATED/SPECULATIVE as above); C-AE3 (kill immunity proven for all histories); C-AE4 (total-phase precision). All entered; the registration table of §3 is adopted WITH these demotions applied.

### A.3 Post-verdict status

**BIND-2(c) winding data REGISTERED (refereed), with the demoted labels.** Refereed physical content: ray data (deck classes (n₁, n₂), sectors — prescription-free); per-ordered-history mutual values n_first·Q₁Q₂ (theorem); the inter-class interference phase (n₁−n₂)Q₁Q₂ (theorem); the discrete history label b (adjudicated bookkeeping); common-n data M = (n∓1)Q₁Q₂ immune to ordering under all histories (theorem). Convention entries: the Weyl midpoint value (canonical convention, physicality withdrawn at n₁ ≠ n₂). NOT registered: energy semantics (blocked, standing); the braiding INTERPRETATION of b (speculative, pending GAP-7 protocol or exchange-homotopy derivation — the named successor round if wanted). GAP-6 is closed as a computational ambiguity; its interpretive residue lives on as the C-AE2 grading. Entered into the BIND-2 registration (phase112 §3c). The operator's twist picture status after refereeing: wind counts and twist phases — refereed referents; "which strand crossed first" — a real discrete label whose braiding interpretation is not yet earned; stored energy — still no referent.
