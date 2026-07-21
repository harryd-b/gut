# Phase 48 — The B3c fusion test executed: the strong "level = stiffness" identification fails

*Working session, 2026-07-17. Runs the decidable test phase 47 §2 posed: is Bradlow truncation a fusion truncation at level ℓ = GV/4π² = 2g−2? Method: dimension comparison in-room + full literature verification of the candidate bridges (Thaddeus; Muñoz; Muñoz–Wang; Witten; Gukov–Pei). **Result, stated plainly per the honesty rules: the strong identification is refuted.** The count coincidence survives as an observation with one published stepping stone; the discreteness cascade keeps all its theorem links; the SU(2)_{2g−2} reading is dropped from the critical path. This phase also upgrades the framework's Floer census to [verified-source] (Muñoz–Wang Thm 1.7 confirmed verbatim).*

---

## 1. The dimension test [computed; negative]

| g | ℓ = 2g−2 | dim V_ℓ(Σ_g) (Verlinde) | Σ_sectors protected content (phase 40) |
|---|---|---|---|
| 2 | 2 | 10 | 8 |
| 3 | 4 | 329 | 48 |
| 4 | 6 | 42,048 | 256 |
| 5 | 8 | 15,130,225 | 1,280 |

No relation at any level tried (2g−2, 2g−1, 2g, g−1). The naive content-level identification of phase 47 — sectors ↔ primaries with matching state counts — **fails immediately**. (Expected from phase 47's own boundary; now on the record with numbers.)

## 2. The structural test [literature-verified; negative for the strong form]

Three findings from the source verification, each undermining a pillar of the strong identification:

1. **Thaddeus's level and degree are independent.** The wall-crossing proof of the Verlinde formula (Invent. Math. 117 (1994)) does run through flips centered on projective bundles over Sym^i Σ — the mechanism phase 47 hoped for — but the Verlinde level k enters as a line-bundle power and the degree d (which controls the Sym^i range) is an auxiliary parameter taken large; **no distinguished role for d = 2g−2 exists in the paper**. The hoped-for "canonical degree = level" mechanism is not there. [verified-source; also corrected: Thaddeus's pairs are rank-2-bundle + section, not line-bundle + section — the abelian vortex case is Bradlow's, one level down.]
2. **The published bridge stops one step short, and the step is obstructed.** What *is* in print: Muñoz–Wang Cor. 4.7 — **SW flux sector r ↔ α-eigenvalue sector r of QH*(N_g) ≅ instanton HF*(Σ×S¹)** [theorem, at associated-graded level], and the eigenvalue clusters number exactly 2g−1 = rank of V_{2g−2}(SU(2)) [verified arithmetic; **unclaimed in print** — the count coincidence of phase 47, one level up]. But: **QH*(N_g) is not semisimple** (Muñoz Prop. 20: γ nilpotent; Artinian local blocks), while every complex Verlinde algebra is semisimple — so no isomorphism on the nose, at best after semisimplification. And even then, **the eigenvalue spectra differ in kind**: the α-eigenvalues are equally spaced (0, ±4, ±8i, …, ±4(g−1)·(√−1)^g) where the Verlinde spin-½ eigenvalues are trigonometric (2cos(mπ/2g)). Under the natural dictionary there is no ring map. [Full no-go across *all* dictionaries not established — but the burden has flipped.]
3. **No direct SW↔Verlinde statement exists anywhere in the literature** (searched thoroughly; the closest structures are Gukov–Pei's equivariant-Verlinde-from-vortices, which lives in complex Chern–Simons/Higgs-bundle K-theory, not monopole Floer).

## 3. The verdict, and what survives

> **B3c strong form — "Bradlow truncation is fusion truncation at level GV/4π²" — is refuted** at dimension level (§1) and at ring level under the natural dictionary (§2). "The level is the stiffness" is **downgraded from conjecture to numerological observation** and removed from the critical path.

What survives, unchanged, because it never depended on the SU(2) reading: the discreteness cascade's theorem links — finite census [now **verified-source**: Muñoz–Wang Thm 1.7, confirmed verbatim, including the r = 0 exclusion the record already carried], GV quantized in 4π²·2ℤ [verified], skein center = classical shadows at any root of unity [verified], Goldman integrality. The original B3c pivot — that the finite census is implemented by a finite-level quantization *at some level, by some mechanism* — remains open but now without a candidate level, and with a precise obstruction ledger any future proposal must clear (the non-semisimplicity and the spectrum mismatch).

What is genuinely new and worth keeping from the exercise: (i) the **2g−1 eigenvalue-cluster count** of QH*(N_g) matching the V_{2g−2} rank is a real, verified, unpublished observation — logged at observation level, no claim attached; (ii) the **Muñoz–Wang Cor. 4.7 sector bridge** (abelian SW sectors = nonabelian eigenvalue sectors) is a published theorem the program was not previously using — it is the correct, honest anchor for any future fusion-side story, and it directly strengthens the phase-5/§2 sector narrative (the framework's abelian flux sectors are shadows of a nonabelian eigenvalue decomposition, by theorem).

## 4. Method note

This is the program's kill-test culture operating at full speed: phase 47 proposed the identification *with its test named in the same document*; phase 48 ran the test within a day; the identification failed; the failure is reported in the first line. The observation-level residue is retained without inflation. Three phases, one conjecture, one clean negative, two durable imports (Thm 1.7 verified; Cor. 4.7 adopted).

*Status line: B3c strong form dead; cascade intact; census now verified-source; one new published bridge adopted (Cor. 4.7); critical path shrinks to the Γ-twisted net and the species sum, with the expert packet (H5b/H6b) unchanged.*
