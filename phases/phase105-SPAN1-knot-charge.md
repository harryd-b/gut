# Phase 105 — SPAN-1: from defect topology to algebraic charge — the anchoring theorem and the KNOT-Q conjecture (derivation in-room; referee pass pending on §2; conjecture registered with kill in §4)

*Working session, 2026-07-24, continuing the phase-105 successor program. **Status: §2 [derived in-room; referee pass dispatched; no verdict entered]; §3 [established (others'), flagged]; §4 [conjecture, registered with kill]; §5 [gap statement].** This document begins the first span of the data dictionary: the map from a defect's TOPOLOGY to its ALGEBRAIC charge Q — the input side of the refereed pairing D = Q²ℓ/2π. The full span (Seifert genus / Bennequin budget → Q) is F-GAP-shaped and is NOT claimed; what is derived here is its π₁-shadow in the toy arena, which is small, forced, and already carries the physical dichotomy: **topologically trivial defects are chargeless and erasable (light-like); charge requires an essential loop, and an essential loop supplies exactly the geodesic length ℓ that the D-pairing consumes.***

---

## 1. The target and the two sides

The refereed dictionary entry D = Q²ℓ/2π takes as *input* a charged state (Q ≠ 0) anchored to a hyperbolic element γ (length ℓ). SPAN-1 asks what *geometry* produces that input. The framework's conjecture layer (phase 57) says: transverse knots decorated with quantized twist. The full claim — Seifert genus and the Bennequin budget determining realizable Q — requires the contact-topology-to-algebra functor that does not exist (F-GAP at span size). But the toy arena supports a complete answer to the *π₁-level* question: which free homotopy classes of defect loops can carry charge at all? The answer is derivable because the toy's charge-storage mechanism is now refereed: **charge lives in a jump of the defect profile's primitive, and jumps need anchor points.**

## 2. The anchoring theorem (toy arena) [derived in-room; to referee]

Setting as in JOIN-4a/4a′ (all refereed): U(1)-current net on S¹; defect automorphisms α_ρ(W(f)) = e^{i∫ρf}W(f) with real density ρ; charge = total winding Q = ∫ρ (up to normalization); the coupled arena M_γ for hyperbolic γ with fixed points ξ±, axis arc I, length ℓ.

**Claim S1-i (triviality ⟹ erasable) [established (BMT); assembly ours].** If ρ is smooth, compactly supported in an open interval, with **Q = ∫ρ = 0**, then α_ρ is *inner*: it is implemented by W(P) with P the compactly supported primitive of ρ (P exists as a legitimate one-particle vector because it is smooth and compactly supported — no jumps). Hence the defect state ω∘α_ρ is unitarily conjugate to the vacuum by a local Weyl operator: **erasable, chargeless, light-like** — the "flash" class of the JOIN-4a′ dichotomy, exactly.

**Claim S1-ii (charge needs an anchor) [derived; the JOIN-4a′ storage mechanism restated].** If Q ≠ 0, every primitive of ρ jumps by Q somewhere: there is at least one **anchor point** where the defect's phase winds. (Refereed already in the JOIN-4a amendment's B(3) and the JOIN-4a′ D1-d: the jump is the charge; it cannot be smoothed away, only moved.)

**Claim S1-iii (admissibility in M_γ forces the anchor onto the fixed points) [derived in-room; the new step — to referee].** For the defect state to couple *finitely* into M_γ — i.e., for the relative cocycle machinery of JOIN-4a′ to produce normal states and finite invariants — the transported difference ζ = η − η∘γ must lie in the local one-particle space after truncation, which requires ζ to **vanish at the anchor set**. If the anchor x₀ is *not* γ-fixed, then ζ carries two genuine jumps (height ±Q at x₀ and γx₀), each of logarithmically divergent H^{1/2}-norm: no truncation is finite, no relative Connes cocycle exists in the required class, and the defect does not define an admissible coupled state. Hence: **admissible charged defects in M_γ are anchored precisely on fix(γ) = {ξ±}.** [One-step derivation from the refereed jump-cost mechanism; the referee is asked to confirm the "two-jump ⟹ inadmissible" step and its exact formulation.]

**Claim S1-iv (the topological dichotomy) [assembly].** In the carrier's geometry, anchors-with-a-group-element exist exactly for **hyperbolic γ ≠ id**, and conjugacy classes of hyperbolic elements correspond exactly to **essential free homotopy classes** of loops (every essential class on a closed hyperbolic surface contains a unique geodesic, of length ℓ(γ) > 0; contractible loops contain none and stabilize no fixed points). Therefore, in the toy arena:

> **Contractible defect loop ⟹ no hyperbolic stabilizer ⟹ no admissible anchor ⟹ Q = 0 class ⟹ erasable (S1-i): light-like.**
> **Charged defect (Q ≠ 0) ⟹ anchored at fix(γ) for an essential class γ ⟹ pinned to a closed geodesic of length ℓ(γ) ⟹ the D-pairing D = Q²ℓ(γ)/2π is defined and nonzero.**

The domain of the dictionary's first entry is thereby characterized: **D pairs charge with length because charge cannot exist without a geodesic to be anchored to.** The "flash vs electron" dichotomy of JOIN-4a′ acquires its topological face: trivial loop = light; essential loop = the only possible home of matter.

*Scope statement, per house rules: S1 is the π₁-version of the span, proven (pending referee) in the toy arena only. It says nothing yet about Seifert genus, self-linking, or the Bennequin budget — that refinement is §4's conjecture. And it does not claim contractible defects exist as objects in the full framework — only that IF a defect's loop is contractible its boundary shadow is chargeless.*

## 3. The quantization clause [established (others'); flagged, not derived]

For the plain U(1)-current net the BMT charge Q is real-valued — a continuum, no quantization. Quantization of Q into a discrete lattice is exactly what the **compactified (lattice) extension** of the current net supplies: for the lattice net, the admissible sectors form ℤ (charge quantized in units set by the compactification radius). The record's phase-57 clause "quantized twist — an integer per knot" therefore corresponds on the algebra side to choosing the lattice extension, and the toy's Q ∈ ℝ is the decompactified shadow. [Established structure; the framework-forced choice of radius — if any — is not claimed and would be a scale-fixing statement of exactly the one-scale kind; flagged as a future connection, not asserted.]

## 4. KNOT-Q — the Seifert-genus refinement, registered as a conjecture with its kill

> **KNOT-Q [conjecture; registered 2026-07-24; kill attached].** In the framework's defect quantization (transverse knots K in the tight contact carrier with Lutz/Giroux twist data, per phase 57 §4), the induced boundary charge is forced by the knot data, with:
> (a) Q(K, twist) = 0 whenever K is transversely isotopic to a knot of **Seifert genus 0** (the Bennequin budget 2·0 − 1 = −1 admitting no positive twist);
> (b) Q ≠ 0 realizable at genus ≥ 1, with the trefoil class realizing the minimal twist quantum;
> (c) chirality of K mapping to the sign of Q, and the Arf invariant of K mapping to the ℤ/2 (statistics) grading of the induced sector, consistently with the record's Arf-graded census.
>
> **Kill condition (armed now):** if the defect quantization, once constructed, assigns **nonzero charge to a genus-0 (unknotted) defect**, or **zero charge to every knot class**, KNOT-Q is dead and with it the knot-topological reading of the matter dictionary. (Fitting escape forbidden in advance, per the AMK lesson: the assignment must be forced by the quantization, not chosen to make (a)–(c) true.)

Honest status: (a)–(c) currently have exactly the evidential standing of the alignment table — established structure on each side, no bridge. S1 (§2) is the bridge's π₁-floor. The gap between π₁ (essential vs contractible) and Seifert genus (the knot's own complexity in the 3-manifold) is real: closed geodesics in T¹Σ_g define knots whose Seifert genus is NOT determined by essentiality alone, and the Bennequin mechanism operates at that finer level. KNOT-Q stands or falls there.

## 5. What remains missing, named at span size

The derivation S1 lives entirely on the boundary-algebra side; KNOT-Q needs the map from *bulk contact data* (the knot, its twist decoration) to *boundary defect data* (ρ, the anchor structure) — a span-sized instance of F-GAP. Candidate route, logged not claimed: the framework's skein layer (V.6) assigns boundary data to knots via holonomy; the GV-T sharpening (phase 57 §5, still shelved for a defined target) would be the quantitative version. This document does not build it. What it does establish, if §2 survives refereeing: the *target* of that map is now fully characterized (anchored charge classes at fixed points of hyperbolic elements, paired by D), so the missing map has, for the first time, a precisely specified codomain.

---

*Status line: the dictionary's first number said what a particle costs; this span says where a particle is allowed to live. In the toy world the answer is now sharp — charge cannot float free, cannot sit on a shrinkable loop, and has exactly one kind of home: the fixed points of an essential geodesic, whose length is the same ℓ the cost formula charges for. Light is what a trivial loop can hold; matter is what only topology can pin down. The genus refinement is registered, armed, and waiting for the functor that would test it.*

---

## Amendment (2026-07-24, same session) — referee verdicts entered: S1 re-scoped to the locality theorem

*Report verbatim in `reviews/REPORTS-phase105-SPAN1-referee-2026-07-24.md`.*

**Confirmed [derived, refereed]:** S1-i (chargeless smooth compact defects are inner — implemented by a genuinely local Weyl operator; the light-like class) and S1-ii (charge forces jump anchors; total jump Q, splittable over finitely many points — a freedom the room's draft ignored and the corrected statements must carry, including the legitimate split q₊ + q₋ = Q between the two fixed points).

**Corrected — two room errors, both caught:**
- **C-S3 (the loophole the room flagged pre-verdict, confirmed exactly):** "anchors ⊂ fix(γ)" is WRONG — γ preserves *both* arcs, so a defect anchored entirely in the complementary arc I′ is admissible with arbitrary Q ≠ 0; but it is smooth near Ī and hence **invisible to M_γ** (vacuum-like from the I-side). The refereed trichotomy: anchors in open I — inadmissible (divergent); anchors at fix(γ) — admissible and visible; anchors in I′ — admissible and invisible. **Corrected S1-iii: the charge *visible to the coupling* must be anchored on fix(γ).**
- **C-S4 (a genuine room error):** "contractible ⟹ Q = 0" was a non sequitur — for the trivial class there is *no coupling at all* (no axis, no arc, no M_γ), so nothing forces Q = 0; a charged defect simply isn't coupled. The toy proves where charge can live *relative to a chosen γ*, not which γ a defect "chooses" — the bulk notion of a defect *loop* is not defined in the toy, and the draft conflated it with the algebraic input γ. The topology-selects-charge clause remains entirely at the KNOT-Q conjecture level.

**The theorem as it now stands [derived, refereed] — the LOCALITY theorem:**

> For each essential free homotopy class (equivalently each hyperbolic γ, via its unique geodesic of length ℓ(γ)): the coupling M_γ admits charged defects only with the coupling-visible charge anchored on fix(γ), making (Q_visible, ℓ(γ)) — hence D = Q²ℓ/2π — well-defined invariants of the coupled system. Charge anchored elsewhere is either inadmissible (inside the arc) or invisible (in the complementary arc). Chargeless smooth defects are locally erasable everywhere.

Physical reading, tagged [interpretation]: **each geodesic sees exactly the matter pinned to its own endpoints and prices it by its own length** — the dictionary is local, geodesic by geodesic. The room's grander reading ("charge requires essential topology") is NOT proven and is demoted into KNOT-Q, whose registration and kill are unchanged.

**Process note:** one loophole flagged by the room pre-verdict and confirmed; one error caught by the referee outright. The session's running totals: the pre-verdict pass has now corrected the room in six distinct instances across four documents; none reached the record as a claim.
