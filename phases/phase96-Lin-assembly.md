# Phase 96 — The Lin assembly: the carrier's Pin(2)-bar package — one class closed in full, one reduced to a single new differential

*Working session, 2026-07-19. The queue's next item: assemble the Pin(2)-monopole bar theory of the carrier from Lin's Rokhlin theorem (arXiv:1708.07879), whose precise machinery was extracted and cross-checked this session (his Theorem 1: HS̄ is determined by the triple cup form and the Rokhlin map up to overall shift; his Proposition 6: a spectral sequence with E¹ = ⊕_{spin lifts} R̃⟨−2μ+|I|⟩ over R = 𝔽[V,Q]/Q³, d¹ = Q² on Rokhlin-difference edges; his warning: d² is generally nonzero). Both inputs on our side were already settled: the triple cup product vanishes (Theorem A of the DTAB paper), and the Rokhlin invariants are the externally triple-derived μ-table. The assembly closes one of the carrier's two self-conjugate classes completely and reduces the other to one new, bounded computation.*

---

## 1. The Rokhlin maps, identified — with a consistency lock

Lin's theory needs μ_s: Spin(s) → ℤ/2 up to constant (only differences drive the differentials; the overall value is quotiented by his "up to shift"). From the μ-table: **on the NS class [0], the map is constant** (μ = 1 uniformly — the disk-bundle derivation); **on the theta class [g−1], the map is the Arf invariant** (slope 8 mod 16 ⟹ mod-2 reduction = Arf(θ)) — i.e., **the standard rank-g hyperbolic quadratic form** on the theta half's H¹(Σ;ℤ/2)-torsor (Johnson). And the lock: Lin's Proposition 1 says the Rokhlin map is cubic with cubic part = the triple cup form mod 2; the carrier's cup form vanishes, so the map must be (at most) quadratic — **Arf is quadratic. The externally-derived table and Lin's structural theorem confirm each other with no room to spare.**

## 2. The NS class: closed, final

Constant Rokhlin map + vanishing cup form is precisely Lin's **Pin(2)-standard** condition. Therefore, verbatim from his theorem:

> **HS̄(T¹Σ_g, [0]) ≅ R̃ ⊗ H_•(T^{2g}; 𝔽), up to overall grading shift** — the theory of #^{2g}(S²×S¹). [established (Lin) + the μ-table; final]

Gysin check: contribution 2 per R̃-summand gives HM̄-rank 2^{2g} ✓ (our Theorem A standardness). To our knowledge — and per the earlier verification agent's NOT-FOUND list — **this is the first complete Pin(2)-monopole computation on a b₁ > 0 manifold outside Lin's own examples.**

## 3. The theta class: a new twisted model, computed to E², pinned by Gysin, one differential from closed

The theta class realizes a case absent from Lin's worked examples: his are linear Rokhlin maps (S²×S¹-sums, trefoil surgeries) and the cubic T³ family — **the carrier is the first natural manifold whose Rokhlin map is genuinely quadratic.** The assembly [derived, per-pair, Künneth clean over the graded field 𝔽[V^{±1}] with Q primitive]:

- The E¹ complex factors over the g hyperbolic Arf pairs; per pair (μ = λ₁λ₂: values 0,0,0,1), d¹ fires on exactly two edges, and **E² = R̃ ⊕ [R̃ ⊕ I] ⊕ I** (V-ranks 12 → 10), with I Lin's twisted module (two V-towers, Q an isomorphism between them, Q² = 0).
- **The Gysin sequence forbids collapse at E²:** the E² page's HM̄-contribution is 8 per pair against the required 4 (= the standard HM̄ of Theorem A). **d² ≠ 0 is forced** — exactly the subtlety Lin flags as generally present, here proven present by rank count in a cup-zero case (itself a small observation: his d² caveat is usually attributed to cup products; the quadratic Rokhlin map produces it with no cup form at all).
- The Gysin-consistent candidate, unique at rank level with the available module types: **HS̄(pair) ≅ R̃ ⊕ I (up to shift), hence HS̄(T¹Σ_g, [g−1]) ≅ ⊗^g (R̃ ⊕ I) — V-rank 5^g — [conjecture]**, with the multiplicative Gysin check passing at every genus (4^g = HM̄ ✓, verified g ≤ 4).
- **LIN-d2 [registered]:** compute the d² of Lin's spectral sequence for the quadratic pair (a bounded, chain-level computation in his framework — the single step between the conjecture and a theorem). Until it runs, the ⊗^g(R̃ ⊕ I) formula carries its tag.

## 4. What this closes and opens

Closed: E1's program (Lin's formula on the carrier) is executed to its honest boundary — the [0]-class package final, the [g−1]-class pinned to one named differential; the carrier now has bar-level Pin(2) content on record at b₁ > 0, where the literature had none. Opened: **LIN-d2** (the quadratic-pair d², bounded, exportable to Track F/O as the cleanest possible "one differential" ask); and the observation, filed with the standing flag, that the theta class's conjectured answer ⊗^g(R̃ ⊕ I) — a free part and a twisted part per handle — is the bar-level shadow of exactly the per-handle structure the SRF answer sheet conjectured one level down. The aggregate theory keeps agreeing with the refinement's silhouette; the separation gate still decides whether that means anything.

*Status line: the program asked Lin's theorem a question it had never been asked — a quadratic Rokhlin map — and got back one finished computation, one forced differential, and one conjecture whose every checkable consequence checks. The carrier remains what it has been all week: the simplest manifold nobody had computed, sitting at the exact boundary of every tool aimed near it, returning something slightly new to each one.*
