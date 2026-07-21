# Phase 84 — E1, the in-room half: the Rokhlin table of the carrier, derived and predicted

*Working session, 2026-07-18. Phase 83 left E1 (evaluate Lin's formula on the carrier) blocked on the Kirby–Taylor Thm 6.5 retrieval. This phase executes everything E1 needs that does NOT require the book — one derived result and one two-step conjecture — so that when KT-6.5 is in hand, E1 reduces to reading off a comparison. The deliverable is a complete predicted μ-table for all 2^{2g+1} spin structures of T¹Σ_g, with each row's epistemic status tagged.*

---

## 1. The NS half: μ = 1, derived

The disk bundle D(g, 2g−2) is spin (w₂ = (χ + n) mod 2 = 0), its intersection form is ⟨2g−2⟩ on H₂ ≅ ℤ (the zero section, positive self-intersection), so sign(D) = 1; its spin structures restrict to exactly the 2^{2g} extendable (projectable/NS-fiber) structures of Y = ∂D. Hence:

> **μ(T¹Σ_g, θ) = 1 mod 16, uniformly, for all 2^{2g} NS-half spin structures.** [derived — Rokhlin's theorem + the disk bundle; clean]

This confirms, at Rokhlin level, phase 82's "uniform phase on the NS half," and is the first entry of Lin's E1 formula computed for this manifold.

## 2. The theta half: μ = 1 + 6(g−1) + 8·Arf(θ) mod 16, conjectured in two derived steps

**Step one — the Arf coefficient is 8 [derived-consistency].** Kirby–Melvin/Donoghue write the bosonic Ising invariant as 2^{−b₀} Σ_θ ζ^{μ(θ)/2}, ζ = e^{3πi/4}. An 8·Arf term contributes ζ^{4·Arf} = e^{3πi·Arf} = (−1)^{Arf} — exactly the Arf-weighting that phase 82's decomposition hypothesis requires and whose magnitude consequences (2^{g−1} from the signed count 2^g) were already cross-checked against part I at every genus. Any Arf coefficient other than 8 (mod 16) breaks that verified match.

**Step two — the constant is pinned by the relative phase [derived-with-care; ERRATUM applied, see below].** Absolute phases carry the untracked framing anomaly, but the *relative* phase between the two components of one surgery sum is anomaly-free. ~~Equating ζ^{(c₀−1)/2} with e^{iπ(g−1)/4} gives c₀ = 1 + 6(g−1) mod 16.~~ **[ERRATUM, 2026-07-18 (same day), phase 85: that equation paired Kirby–Melvin's spin-sum weight — which belongs to SU(2)₂, central charge 3/2, the ν = 3 member of the 16-fold way — with part I's surgery phases, computed for the c = 1/2 Ising theory (ν = 1). Mixing the two ν's is inconsistent. The corrected chain, run consistently within each odd ν (and verified identical across ν = 1,3,5,7): ν(c₀−1) ≡ 2ν(g−1) mod 16 ⟹ c₀ = 1 + 2(g−1) mod 16. The corrected table: NS half 1; theta even 1+2(g−1); theta odd 9+2(g−1) mod 16 (g=2: 1/3/11; g=3: 1/5/13; g=4: 1/7/15). The error was caught in-room by generalizing the check to all ν before trusting it — the B3c method working as designed. §3's table is superseded by phase 85 §1.]** The sector-correspondence assumption (NS ↔ {1,ψ}; theta ↔ σ) stands as before; the constant remains [conjecture], the Arf-slope 8 the sturdier claim.

## 3. The predicted table [the E1 answer sheet, sealed before the book is opened]

| g | NS half (2^{2g} structures) | theta even (2^{g−1}(2^g+1)) | theta odd (2^{g−1}(2^g−1)) |
|---|---|---|---|
| 2 | 1 | 7 | 15 |
| 3 | 1 | 13 | 5 |
| 4 | 1 | 3 | 11 |
| 5 | 1 | 9 | 1 |
| 6 | 1 | 15 | 7 |
| g | **1 [derived]** | **1+6(g−1) mod 16 [conjecture]** | **9+6(g−1) mod 16 [conjecture]** |

Kill conditions, pre-registered: KT-6.5 returning a *non-constant* μ on the NS half kills §1's bookkeeping (and would indicate a spin-extension error); a theta-half μ that is not affine in Arf kills the phase-82 decomposition hypothesis outright (and with it the candidate class's per-θ structure); an affine μ with slope ≠ 8 breaks the verified magnitude match and would signal a convention error to be resolved before any interpretation. A confirmed table completes E1's input, upon which **Lin's theorem yields the full Pin(2)-bar theory of the carrier with triple cup ≡ 0 — the first computed Pin(2)-monopole package at b₁ > 0 in the literature**, assembled entirely from published results plus one book lookup.

## 4. Ledger

- E1 split: E1a (this phase — done, one derived row, one conjectured row with named assumptions), E1b (the KT-6.5 lookup — human/physical item, now a pure comparison against §3).
- The predictions ledger gains its **class M (predictions about mathematics)**, amended alongside: M1 = the SRF answer sheet (phase 82 §3); M2 = the μ-table above; M3 = DTAB-1's implicit content; each with its kill condition and its "referee" (whoever computes).
- CORE v6 issued alongside this phase, consolidating phases 74–84.

*Status line: E1 is now a sealed-envelope experiment with a one-afternoon referee — the room has written down, in advance, the sixteen-adic values a 1990 theorem should assign to the carrier's spin ledger, derived one row from a disk bundle and conjectured the other from the requirement that two independent computations already performed agree. The program's newest predictions are integers mod 16, and the instrument that tests them is a library.*
