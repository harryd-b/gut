# Referee report — BIND-2 round 1, two-arc rate computation (phase112-BIND2-round1-two-arc-rate.md)

**Date:** 2026-07-26
**Referee:** context-free adversarial agent (line-by-line audit of the E1 attributions against phase104-JOIN4a-prime-derivation.md; independent numerics at different modulus ℓ₁ = 0.7, different grid, different edge model, different fit window; targeted truncation-boundary attack).
**Editorial note (operator):** Preserved VERBATIM below. Verdicts: **K-BIND2-1 CONFIRMED-DOES-NOT-FIRE** — the pair rate D = (Q₁+îQ₂)²ℓ₁/2π is refereed; **[BOX-B] RATIFIED** with a strengthening (derivable from the record's charge reading, not calibration alone; no ambiguity infects E1). Corrections C-W1..C-W4 entered in the phase file's Amendment.

---

## REPORT (VERBATIM)

# REFEREE REPORT — Phase 112 round 1 (K-BIND2-1, the two-arc line-frame computation)

**Referee:** context-free adversarial agent. Independent record audit (phase 104 line-by-line against the submission's attributions; phases 105, 106, 108, 111) and fully independent numerics (own script, own grid du = 0.02, own edge model tanh log-width 0.4, own kernel discretization, **different modulus ℓ₁ = 0.7 and different fit window n ∈ [20,45]** vs the submission's ℓ₁ = 0.5, [15,35]). Scripts deleted.

---

## (A) Audit of the E1 attributions — ALL CORRECT; one micro-erratum

I checked every convention the submission attributes to phase104-JOIN4a-prime-derivation.md against the file:

- **Functional and normalization.** §0: "⟨f,g⟩ := 2π Σ_{k≥1} k conj(f̂_k) ĝ_k" and the Gagliardo identity "= 8π² Σ_{k≥1} k|f̂_k|² = 4π‖f‖²" — so ‖f‖² = G/4π. ✔ D as claimed: "D(c,ℓ) := lim_{n→∞} ‖ζ^{(n)}_in‖²/n = Q²ℓ/(2π)". ✔
- **Truncation.** §0, verbatim: "Truncations: for a function g vanishing at ξ±, g_in := g·χ_Ī ∈ H(I) (kinks only)." Exactly as the submission states, including the vanishing-at-fixed-points precondition. ✔
- **Task-3 uniqueness.** §3, verbatim: "g − ζ^{(n)}_in locally constant on I and supported in Ī; any nonzero such difference is a step function with jumps, hence ∉ H^{1/2}. So ζ^{(n)}_in is the UNIQUE coherent trivializer in H(I)". ✔ The submission paraphrases with σ(g − ζ^{(n)}, f); the record has σ(g − ζ^{(n)}_in, f) — equivalent for supp f ⊂ I (phase 104's own sanity check: "σ(ζ − ζ_in, f) = 0 ... ζ_out pairs trivially"), but the quote should be exact (C-W1).
- **Iterate-then-truncate.** Not smoothed over: the record's definitional chain is ζ^{(n)} := η − η∘γⁿ (global telescoping, §0) THEN g_in := g·χ_Ī; the object in D is (ζ^{(n)})_in, and the in-algebra cocycle c′_t(γ) lives on A(I) (Task 2 done "strictly in-algebra"). Truncate-then-iterate is not available in the record (η_in ∉ H^{1/2}, §1(b) jump obstruction). The order is forced, as claimed. ✔
- **Single near-jump / "two-edge model would have doubled it."** Amendment, verbatim: "the referee specifically confirmed the single-near-jump structure that fixes the coefficient — a two-edge model would have doubled it". ✔
- **Line-frame erratum.** Amendment errata, verbatim: "the log-frame spectral heuristic ... is invalid for the Möbius-invariant norm (log is not a Möbius chart) — the line-frame computation is the correct one and is what the referee verified". ✔
- **Dictionary line.** phase 106 §1 interlocks, verbatim: "globally compensated single-valued profiles have D = 0 (permanence is local)". ✔
- **C-D5 midpoint scope.** phase 105 amendment, verbatim: "the symmetric (midpoint) regularization convention **at shared anchors**". The submission's claim that midpoint governs shared anchors only, not own-anchor placement, is accurate. ✔
- **Phase-111 imports.** §5(3) of the kill report contains "∫_{I₁}(η₁+η₂)′ = Q₁+îQ₂" and the exactly-one-partner-anchor statement (a₂ for î=+1, b₂ for î=−1); the interlacing lemma is theorem-grade (C-V2/BOX-3 closed). ✔

**The C-V4 demand was met, not dodged.** §5(3) demanded: "the two-arc line-frame computation, the precise truncation bookkeeping of E1's I-local cocycle (which must kill the complementary-side structures — the same mechanism that makes refereed E1 equal Q²ℓ/2π rather than 2Q²ℓ/2π), and referee numerics of the actual growth rate." The submission delivers the first two and its own numerics; this report supplies the third. Notably the cancellation mechanism the submission found is the one the demanding referee itself predicted would have to operate.

## (B) Attacks on Lemma A and the cancellation — SURVIVES

**(i) î = −1 continuity.** The partner plateau covering a₁ (η₂ ≡ Q₂ on both sides of 0) is genuinely continuous at the fixed point; ζ₂^{(n)}(a₁) = Q₂ − Q₂ = 0 for every n. The in-leg inventory follows: the down-ramp at b₂ ∈ I₁ produces a +Q₂ box, giving swept charge Q₁ − Q₂ = Q₁ + îQ₂ — consistent with phase 111's î = −1 channel (order a₁,b₂,b₁,a₂, attracting partner anchor in leg). The rate is well-defined (my numerics below: î=−1 slopes exact).

**(ii) The truncation-boundary attack — my main assault, repelled.** The inner edges sit at x_p·e^{−nℓ₁} → 0⁺ = a₁, exactly the cut point. I verified the cross-boundary accounting independently: for f supported on x > 0, the opposite-side Gagliardo contribution is 2∫₀^∞ f(x)²[∫_{y<0}dy/(x−y)²]dx = 2∫f(x)²/x dx = 2∫f(u)²du in u = log x — **exact**, no approximation. The edges approaching the cut contribute through this term only via the O(1) tail below the innermost edge (fixed edge shape); the n-growth is the plateau between inner and outer edges, on which the box heights ADD: I re-derived the overlap identity independently: ∫f²du = (Q₁+Q₂)²(nℓ₁ − Δ) + (Q₁²+Q₂²)Δ = (Q₁+Q₂)²nℓ₁ + O(1), Δ = |u_a − u_ε|. The same-side sinh kernel is exponentially local, so it can carry **no** growth — and my numerics confirm this directly: the sinh part alone for the (1,1) pair saturates at 1.21030 by n = 25 with fitted slope 0.000000. No boundary artifact, no hidden divergence; the accumulation at a₁ IS the correctly-accounted growth mechanism, not an extra disease.

**(iii)–(iv)** î = −1 swept charge well-defined (above); the single-carrier compensated mechanism verified: truncated compensated ≡ truncated single (the complementary-side boxes literally never meet χ_Ī₁'s support — γ₁ preserves both arcs, so this is identical annihilation for all n, not an asymptotic statement), and the global compensated run is bounded (below), matching phase 106's refereed line and the "would have doubled it" structure.

## (C) Independent numerics — CONFIRMED TO 5–6 DECIMALS

ℓ₁ = 0.7 (ℓ₁/2π = 0.111408), du = 0.02, tanh log-width 0.4, edge positions different from the submission's, fit n ∈ [20,45]:

| configuration | my slope | (Q₁+îQ₂)²ℓ₁/2π | max fit residual |
|---|---|---|---|
| single Q=1 | 0.11141 | 0.11141 | 2.2e-7 |
| î=+1 (1,1) | 0.44563 | 0.44563 | 1.4e-6 |
| î=+1 (1,−1) | −0.00000 | 0 | 5.1e-7 |
| î=+1 (2,−1) | 0.11141 | 0.11141 | 7.9e-7 |
| î=−1 (1,1) | −0.00000 | 0 | 2.9e-7 |
| î=−1 (1,−1) | 0.44563 | 0.44563 | 1.2e-6 |
| î=−1 (2,−1) | 1.00268 | 1.00268 | 2.6e-6 |
| î=+1 (1,1), C-D5 reshape (moved+narrowed) | 0.44563 | 0.44563 | 2.3e-6 |
| GLOBAL single compensated | 0.000000 (1.33038→1.33179, n=10→45) | bounded ✔ | |
| GLOBAL pair (1,1) | 0.000000 (3.948→3.955) | bounded ✔ | |
| GLOBAL opposite-side pairing piece | −0.891268 (= −2·(Q₁+Q₂)²ℓ₁/2π, both quadrants) | the O(n) disease, real, cancelling ✔ | |
| two-sided incoherent sum | 0.891268 (= 2×) | the "2Q²" disease ✔ | |

**Superlinear-drift hunt (the C-V4 predicted failure mode): negative.** Per-step increments for the (1,1) pair are 0.445634 constant to **6 decimals** from n = 30 to 45; fit residuals ≤ 2.6e-6 over [20,45]. No drift at a different ℓ₁, different grid, different edge model, different fit window. The î-flip, the asymmetric (2,−1) in both channels, the exact zeros at Q₂ = −îQ₁ (with the norm bounded, rate 0 — not ill-defined), and both excluded diseases all reproduce.

## (D) [BOX-B] ruling — RATIFY; does NOT infect E1

The finding is genuine: a representative with an own-anchor-straddling ramp has in-leg charge Q/2 (the ramp at the fixed point does not translate under γ₁ⁿ; its ζ-box has height ~Q/2), so D = (Q/2)²ℓ/2π — the rate is not a function of (Q, anchors) alone. But the record constrains this more tightly than the submission claims: (1) refereed E1 **defines** Q := ∫_I η′ (phase 104 §0) with η′ ≡ c across I — full charge inside; (2) the phase-111 kill referee's gate audit (iii) states "Q = ∫_I η′ over the carrier's leg is the refereed charge reading (dictionary §1 preamble)". Since Lemma A(iii) shows D factors through exactly ∫_{Ī₁}η′, a straddling representative simply has refereed charge Q/2 — it is not a charge-Q representative at all under the record's own charge reading. So the "convention" is derivable from the refereed charge reading plus calibration, and no ambiguity touches refereed E1 (whose profile is concrete). **RATIFIED** as the E2-class → rate bookkeeping rule: canonical representative carries its full charge inside its own leg; C-D5 midpoint remains a shared-anchor convention only. The registration should record the derivability note above, which strengthens the submission's calibration-only argument.

## (E) Kill bookkeeping and the sketch — CLEAN, with two citation corrections

K-BIND2-1's registered wording: fires if "the divergent cross-pairings do NOT cancel and no well-defined per-carrier rate exists," or "the coefficient comes out (Q₁)² (partner-blind)." What was tested matches the wording head-on: the cross-pairings never enter the I-local functional (annihilation exact for all n, exhibited globally), the rate exists and is linear, and the coefficient is partner-sensitive (Q₁+îQ₂)². Neither branch fires; the AMBIGUOUS-allowed clause is moot — this is a clean refereed positive. §(d)'s [SKETCH] stays within bounds: it claims criterion applicability plus the named obstruction functional (swept-charge difference îQ₂ as infrared zero-mode) and explicitly defers the orbit analysis and reference-state choice to a K-BIND2-2 round — no overclaim of K-BIND2-2 resolved. Citation nits: C-N1 proper says "only ĥ ∉ L² **near 0** is needed, which follows from sup_t‖k_t‖ = ∞" (one implication); the full equivalence with Q ≠ 0 is phase 108's mechanism/sanity-check line ("orbit membership ⟺ ... η ∈ H ⟺ Q = 0"). The î ≠ 0 anchor geometry of the difference profile also differs from phase 108's own-anchor setup — rightly flagged by the submission itself as open.

---

## VERDICT BOX

**K-BIND2-1: CONFIRMED-DOES-NOT-FIRE.** B2-b's analytic coefficient **D_{γ₁}(pair) = (Q₁+îQ₂)²ℓ₁/2π** is now refereed: derivation audited against the record's own truncation (attributions verified verbatim), the truncation-boundary attack repelled analytically and numerically, and fully independent numerics (different ℓ₁, grid, edge model, fit window) reproduce all coefficients to 5 decimals with increments constant to 6 decimals and no superlinear drift. The C-V4 demand was met in full.

**[BOX-B]: RATIFIED** (canonical representative: carrier's full charge inside its own leg), with the sharpening that it is derivable from the record's refereed charge reading Q = ∫_I η′ — the ambiguity does not infect E1.

**May enter the BIND-2 registration as refereed:** Lemma A (with its stated hypotheses); the forced iterate-then-truncate reading; the pair rate (Q₁+îQ₂)²ℓ₁/2π in both channels including the exact zero at Q₂ = −îQ₁; the pre-truncation O(n) disease as real-but-globally-cancelling and never entering the I-local functional; the ratified [BOX-B] convention. NOT refereed: §(d)'s K-BIND2-2 sketch (remains [SKETCH]); [BOX-A]/[BOX-D] uniformity (inherit E1's GAP-5 status, unchanged); GAP-1 physical reading.

**Corrections:**
- **C-W1.** §(a)'s Task-3 quote should read σ(g − ζ^{(n)}_in, f) per phase 104 §3; equivalence for supp f ⊂ I holds by the record's own ζ_out-pairs-trivially check, but quotes must be exact.
- **C-W2.** §(d)'s criterion citation: split into C-N1 proper (sup_t‖k_t‖ = ∞ ⟹ ĥ ∉ L² **near 0**) and phase 108's mechanism line (Q = 0 ⟺ orbit membership); "ĥ ∉ L² ⟺ nonzero swept charge per C-N1" conflates the two and drops "near 0".
- **C-W3.** The global-run "opposite-side pairing slope −0.31821" is single-quadrant normalized; the full opposite-side contribution is 2× that (my measurement: −0.891268 = −2(Q₁+Q₂)²ℓ₁/2π at ℓ₁ = 0.7). State the quadrant convention in the registration.
- **C-W4.** [BOX-B] ratification should record the derivability note: the canonical placement follows from the refereed charge reading (phase 104 §0; phase 111 gate audit (iii)), not calibration alone.

Standing AI-referee caveat applies.
