# Referee report — BIND-2(c) winding-data round (phase 119)

**Date:** 2026-07-27
**Reviewed document:** phases/phase119-BIND2c-winding-data.md (consultation section)
**Referee:** context-free adversarial agent (independent hand + symbolic re-derivation, faithful 3×3 nilpotent Heisenberg representation, 16/16 checks; split-adjudication stress; all-histories kill audit). Report preserved VERBATIM below; nothing edited.

---

# REFEREE REPORT — GAP-6 SPLIT ADJUDICATION (ADVERSARIAL)

## Verdict summary

Every computation in the submission is correct. I re-derived the full BCH block by hand and confirmed all of it in an independent symbolic check (sympy, faithful 3×3 nilpotent Heisenberg representation; 16/16 checks passed): centrality, both ordered central factors and their signs, the Weyl phase, the closed-loop delta, all three mutual terms, the first-applied-winding reading, the mean and span properties. BOX-2 (transport-difference = closed-loop change of the central c-number) is sound as used. The kill check is not only correct but under-claimed: I prove common-n immunity for ALL preparation histories (arbitrary interleaving schedules and mid-loop ordering swaps), not just the two orderings. K-B2C-1 DOES NOT FIRE.

The split adjudication survives the stress in structure but not in labeling. Two demotions are required: (1) the "spectral registration value" is a convention, not a physical datum — the submission's own justification for its canonicity entails this, and retaining the word "spectral" would make the odd-difference midpoint incoherent; (2) the identification of dressing-application order with defect braiding is suggestive, not derived — the numbers are theorems, the "braid class" semantics are not. GAP-6 adjudication: MODIFIED.

## Per-claim analysis

**Claim 1 — Commutator and centrality.** With [x₀, j̃₀] = i: [G₁,G₂] = −a₁Q₂[j̃₀,x₀] − a₂Q₁[x₀,j̃₀] = i(a₁Q₂ − a₂Q₁). Central (c-number), so BCH truncates exactly. Verified by hand and symbolically (CHK1). CORRECT.

**Claim 2 — Ordered central factors.** e^{iG₁}e^{iG₂} = e^{i(G₁+G₂)}e^{[iG₁,iG₂]/2} = e^{i(G₁+G₂)}e^{−(i/2)(a₁Q₂−a₂Q₁)} = e^{i(G₁+G₂)}e^{+(i/2)(a₂Q₁−a₁Q₂)}. The reversed order carries the conjugate factor; ratio e^{i(a₂Q₁−a₁Q₂)}. Signs verified symbolically (CHK2a, CHK2b). CORRECT.

**Claim 3 — Weyl phase Φ_W.** G₁+G₂ = (a₁+a₂)j̃₀ − (Q₁+Q₂)x₀ is a single displacement with section a₁+a₂ and charge Q₁+Q₂, so the refereed κ=½ theorem applies verbatim: Φ_W = ½Δ(a₁+a₂)·(Q₁+Q₂) = ½(n₁Q₁+n₂Q₂)(Q₁+Q₂) = ½n₁Q₁² + ½n₂Q₂² + ½(n₁+n₂)Q₁Q₂. This is a legitimate use of the refereed input, not a new assumption. I also independently re-derived the κ=½ increment itself: D(a+da)D(a)⁻¹ = e^{i·da·j̃₀}e^{iQda/2} (CHK6), confirming Φ = nQ²/2 for a single defect. CORRECT.

**Claim 4 — BOX-2 (mandate 2).** The three prescriptions differ by the time-dependent central phase e^{iφ(t)}, φ(t) = ±½(a₂(t)Q₁ − a₁(t)Q₂). For any closed family, multiplying the transported state by e^{iφ(t)} shifts the total accumulated (Pancharatnam) phase by exactly Δφ = φ(T) − φ(0). The submission uses exactly this — total transport phase, not geometric phase in isolation (where gauge invariance would hold only mod 2π; see C-AE4). The delta: φ is linear in a₁, a₂ with Q₁, Q₂ constant along the loop, so Δφ = ½(Δa₂Q₁ − Δa₁Q₂) = ½(n₂Q₂Q₁ − n₁Q₁Q₂) = ½(n₂−n₁)Q₁Q₂. No cross terms exist to miss (CHK3). CORRECT.

**Claim 5 — Ordered mutual terms and first-applied reading (mandate 1 sign audit).** Ordering "12" = e^{iG₁}e^{iG₂} acting on the state, so dressing 2 is applied first. Its mutual term: ½(n₁+n₂)Q₁Q₂ + ½(n₂−n₁)Q₁Q₂ = n₂Q₁Q₂ — the FIRST-applied dressing's winding. I verified this by a second, independent route: in fixed ordering D₁D₂|0⟩, transporting a₂ requires conjugating the a₂-increment through D₁, which yields D₁e^{i·da₂·j̃₀}D₁⁻¹ = e^{i·da₂·j̃₀}e^{iQ₁da₂} — a FULL (not half) extra phase per increment (CHK7). Accumulated: mutual = ½Q₂Δa₂-part aside, cross term = Q₁Δa₂ = n₂Q₁Q₂. The two routes agree; the braid-class assignments are NOT swapped. Ordering 21 gives n₁Q₁Q₂; Weyl is the exact mean; span is the full (n₁−n₂)Q₁Q₂ with the ½ appearing only as each ordering's offset from Weyl (CHK4b–e). CORRECT.

**Claim 6 — Split adjudication (mandate 3).**

*(i) Does the ray argument prove too much?* The worry: the braid phase is also a central phase, so "central ⟹ unphysical" would kill the interference datum too. The submission does NOT commit this error. Its actual structure is the standard distinction: an overall central phase of a single preparation is unobservable (same ray); a relative central phase between two distinct preparation histories brought to interference is observable. The registration table implements exactly this — ray-invariant data prescription-free; inter-class interference phase (n₁−n₂)Q₁Q₂ registered as physical; braid label required only for interference data. The located circularity in strong-(A) is genuine and correctly placed: the symmetric Weyl map quantizes single generators and is silent on whether a pair dressing is one generator or a composition; since the refereed extension gives the pair separate dressing factors, "the symmetric map forces Weyl ordering" would assume the conclusion. Good.

However, the submission then trips over its own argument. It justifies the Weyl value's canonicity "BECAUSE for those data the choice is between physically identical descriptions." Correct — and that premise entails there is no physical fact of the matter about the mutual-term number at n₁ ≠ n₂. A number with no observable backing (energy conversion blocked by the scope guard; no history realizes it when n₁−n₂ is odd) is a convention, and the table's label "spectral registration value" smuggles in physicality the record cannot support. The submission half-concedes this by exiling the "operational meaning" to GAP-8 while keeping the word "spectral" in the table. That is the fudge component of the split: not in the logic, but in the bookkeeping. Demotion required (C-AE1).

*(ii) Braid identification.* Arithmetic: (n₁−n₂)Q₁Q₂ = (n₁−n₂) × Q₁Q₂ is an integer multiple of the refereed exchange unit, and each ordered mutual value n_iQ₁Q₂ is an integer multiple (CHK10; n_i ∈ ℤ by the deck lattice). Verified. But commensurability is not identification. The refereed exchange phase e^{∓iQ₁Q₂} arises from spatial exchange of two defects (half monodromy); the ordering c-number arises from the sequence in which dressing operators are composed in preparation. These live in different spaces: the phrase "braid phase of section a₁ against charge Q₂" describes a symplectic-area phase in the (x₀, j̃₀) zero-mode plane, not a homotopy class of paths in defect configuration space. No argument in the submission connects an application-order swap to a physical exchange path — no homotopy argument, no protocol (GAP-7 is open, and the submission itself flags "measurability asserted"). As it stands the identification is a pun with excellent numerology. Ruling on status: the per-class ordered VALUES and the inter-class interference PHASE are THEOREM (as functions of the operator ordering); the ordering-class label b ∈ {12, 21} as bookkeeping is ADJUDICATED (a legitimate discrete label closing the data); the claim that b IS a braid class in the refereed exchange sense — "the record rediscovering braiding" — is SPECULATIVE until an exchange-path derivation or the GAP-7 interference protocol grounds it (C-AE2).

*(iii) Odd-difference Weyl midpoint.* When n₁−n₂ is odd, the Weyl value sits at a half-integer number of exchange units, realized by no ordered history. Is "convention point only" coherent? Yes — but only after C-AE1. A convention needs no realizing history. If the "spectral" (physical-datum) reading were retained, the column would break precisely here: a purportedly physical value that no preparation realizes and that no allowed observable (energies blocked) could exhibit. So the odd case does not merely tolerate the demotion; it forces it. The submission's GAP-8 registration is the correct instinct, incompletely executed.

**Claim 7 — Kill check (mandate 4).** At n₁ = n₂ = n: all three mutual terms equal nQ₁Q₂ and δ₁₂ = 0, while the instantaneous c-number ½(a₂Q₁ − a₁Q₂) is generically nonzero mid-loop, exactly as the submission states (CHK9, CHK9b). The mandate demands more: immunity under ALL histories. Proven, in three steps, each verified symbolically:

1. *Fixed ordering, arbitrary schedule.* In ordering D₁D₂|0⟩, every a₂-increment conjugated through D₁ picks up e^{iQ₁da₂} (CHK7). The mutual accrual is Q₁∫da₂ = Q₁Δa₂ = n₂Q₁Q₂ regardless of the interleaving schedule of the two windings. Symmetrically, ordering 21 gives Q₂Δa₁ = n₁Q₁Q₂. Schedule dependence is exactly zero.
2. *Symmetric splitting.* e^{iG₁/2}e^{iG₂}e^{iG₁/2} = e^{i(G₁+G₂)} identically — the interleaved midpoint history reproduces Weyl exactly, central factor zero (CHK5).
3. *Mid-loop ordering swaps.* A history that swaps 12→21 at s₁ and back at s₂ inserts the instantaneous commutator phases ∓(a₂Q₁−a₁Q₂)|_{s_k}; these cancel the re-attributed accrual exactly, leaving the start-ordering value n₂Q₁Q₂ with all swap-time values dropping out (CHK8). Odd-swap histories connect the two classes; their relative phase is the interference datum (n₁−n₂)Q₁Q₂.

By centrality every history's phase is Weyl plus a c-number functional; steps 1–3 show that functional closes, for every history, to one of {n₁Q₁Q₂, n₂Q₁Q₂} minus the Weyl mutual. At n₁ = n₂ the set collapses to a point and the inter-class phase vanishes: immunity is exact, all histories, all schedules. K-B2C-1 DOES NOT FIRE — and this is now a theorem, not a two-case check (C-AE3).

## Corrections ledger

- **C-AE1 (demotion, required).** Rename "spectral registration value ½(n₁+n₂)Q₁Q₂" to "canonical convention value." The submission's own canonicity argument (choice among physically identical descriptions) entails it is not a physical datum; no spectral/energy reading exists (scope guard), and at odd n₁−n₂ no history realizes it. The registration table's physicality claim for this column at n₁ ≠ n₂ is withdrawn; everything else in the table stands.
- **C-AE2 (status downgrade, required).** "Ordering class = braid class" is not derived. Grade: ordered values and inter-class interference phase — THEOREM; discrete label b ∈ {12,21} as data-closing bookkeeping — ADJUDICATED; identification with refereed defect exchange ("rediscovering braiding") — SPECULATIVE pending an exchange-homotopy argument or the GAP-7 protocol. The integer-commensurability with e^{∓iQ₁Q₂} is verified but is consistency, not derivation.
- **C-AE3 (strengthening).** Common-n kill immunity upgraded from asserted to proven for all histories: schedule-independence within a fixed ordering (conjugation gives the full e^{iQ₁da₂} per increment), exact Weyl reproduction by symmetric splitting, and exact cancellation of swap-time contributions in swap histories.
- **C-AE4 (precision, no numerical consequence).** "κ=½ machinery covariant under central phases" should read: the TOTAL closed-transport phase shifts by the closed-loop change of the central c-number. For the geometric phase in isolation the statement would hold only mod 2π; the submission's usage (total phase) is the correct one.

## VERDICT BOX

1. All computations verified independently (hand + 16/16 symbolic checks, faithful 3×3 rep); no sign or swap errors; first-applied-winding reading confirmed by two routes.
2. BOX-2 sound: total-phase shift = closed-loop Δ of the central c-number; δ₁₂ = ½(n₂−n₁)Q₁Q₂ exact, no missing cross terms.
3. K-B2C-1: DOES NOT FIRE — common-n immunity exact under all histories (interleavings and swaps), proven, stronger than submitted.
4. GAP-6 adjudication: MODIFIED — split logic confirmed (standard overall-vs-relative phase distinction, circularity correctly located), but "spectral" column demoted to convention (C-AE1) and braid identification demoted to SPECULATIVE (C-AE2).
5. Net: registration closes with the discrete label b; physical content = ray data (prescription-free) + per-class ordered values + inter-class interference phase; the Weyl midpoint is a convention, nothing more.

Word count: ~1750.
