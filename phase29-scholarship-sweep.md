# Phase 29 — Scholarship gate, part 1: the web literature sweep

*Executed 2026-07-11 by four parallel search passes (~45 queries, ~140 tool calls) over Google/web, arXiv (abstracts + full texts via ar5iv), INSPIRE-HEP, and Semantic Scholar. NOT covered: MathSciNet / zbMATH (paywalled — run there the MSC intersections 57R57×81T05, 57R30×46L36, 46L60×83C45, plus the quoted phrases below). Classification discipline: for every hit the question is whether it states the IDENTIFICATION/JOIN, or merely puts the objects in one paper (co-occurrence). Empty results are logged deliberately — they are the evidence a novelty claim needs.*

---

## 0. Executive verdict

**Claim (b) — the monopole-Floer ↔ DHR join: candidate-novel, sweep-clean.** The literal intersection "Floer homology" + "superselection" is empty on the open web. The AQFT topological-sector line stops at degree 1 (π₁/H¹: Brunetti–Ruzzi; Ruzzi–Vasselli; Dappiaggi–Ruzzi–Vasselli), and its entire forward-citation cone contains no H² extension. Three near-misses must be read in full (§3) — most urgently **Casini–Magán, Nov 2025** (higher-form DHR).

**Claim (a) — GV stiffness = modular protection = clock: NARROWED.** The sweep found that the algebraic core — *GV ↔ type III₁ ↔ modular generator*, up to and including the sentence **"the modular generator … is given by the Godbillon-Vey invariant, i.e. this invariant is the Hamiltonian of the theory"** — is **already published by Asselmeyer-Maluga** (arXiv:1601.06436, §6.1.1, Springer chapter 2016), with the foliation↔factor-III chain in AMK 2009–2012 and restated in AMK–Wilms 2022 (arXiv:2209.08056, citing Connes–Rovelli). What the sweep did NOT find anywhere: (i) the modular flow read as *emergent physical/thermal time* in this GV setting (no thermal-time language in the AMK corpus); (ii) the **"rigidity = protection = clock"** framing (GV as *protecting structure*); (iii) any **GV ↔ entanglement-first-law ↔ Einstein equations** link (zero literature); (iv) the explicit **GV → Λ** weld (AMK's own Λ papers run through Chern–Simons/embedding curvature and their review keeps GV and Λ "mathematically separate"). Claim (a)'s candidate-novel content is henceforth exactly (i)–(iv). **Credit line required:** the GV = modular-generator identification is AMK's, not this program's.

**Framing terms — clear.** "Protected stratum," "geometry fixes physics," the folding-rigidity metaphor, "Kaluza–Klein without the extra dimension": no collisions. One hazard: "geometry-first" will be read against Giddings' well-known "quantum-first" program (arXiv:1805.06900, 1803.04973) — position it deliberately.

**Bonus finding on the program's own record:** phase 25's overstatement "the flow of weights is *determined by* the GV class" traces to AMK's own phrasing in 1601.06436 ("the flow of weights mod(M) was determined by Connes to be the Godbillon-Vey invariant") — i.e., the strong reading is AMK's gloss on Connes, and the phase-25 correction note stands against both.

---

## 1. Claim (a) catalog — GV / modular / thermal time

### Prior art that OWNS pieces of the claim (all free on arXiv unless noted)

| Paper | What it already contains | Access |
|---|---|---|
| **Asselmeyer-Maluga, "Smooth quantum gravity" (arXiv:1601.06436, 2016)** | **The core identification**: Hurder–Katok cited (GV≠0 ⇒ factor III); Connes' flow of weights; verbatim: modular generator "given by the Godbillon-Vey invariant, i.e. this invariant is the Hamiltonian of the theory"; Tomita–Takesaki splitting used "to introduce the dynamics." NO thermal-time/emergent-time language, NO protection framing, NO entanglement/first-law. **Must-read §§6–7, 12.** | arXiv free; Springer chapter version NEEDS-ACCESS: https://link.springer.com/chapter/10.1007/978-3-319-31299-6_15 |
| AMK, "Abelian gerbes… foliations of small exotic R⁴" (arXiv:0904.1276) | The dictionary: exotic-R⁴ radial family ↔ codim-1 foliations of S³ classified by GV; factor III₁ link in full text. | free |
| AMK, "Constructing a QFT from spacetime" (arXiv:1107.3458) + "Exotic R⁴ and QFT" (arXiv:1112.4885) | Foliation W*-algebra W(S³,F) ⊃ factor III; KMS stated; "type III₁ factor lying at the heart of any observable algebra of QFT." No time reading. | free |
| **AMK–Wilms, "Big Bang and Topology" (arXiv:2209.08056, 2022)** | Restates GV≠0 ⇒ type III ⇒ modular dynamics; reads modular operator as "the action or the Hamiltonian multiplied by the time"; **cites Connes–Rovelli thermal time** — the closest the corpus comes to (i). No protection framing, no first-law. **Must-read.** | free |
| **Asselmeyer-Maluga, *The Wild Fractal Nature of Spacetime* (World Scientific book, 2025)** | UNKNOWN — the one place AMK may already have taken the modular-flow-=-time step. **Highest-priority NEEDS-ACCESS.** | https://www.worldscientific.com/worldscibooks/10.1142/14188 |
| Bertozzini–Conti–Lewkeeratiyutkul, "Modular theory, NCG and QG" (arXiv:1007.4094; + 2023 Handbook chapter) | The programmatic "spacetime geometry from modular flow" idea (no GV anywhere); notably already cites AMK's type-III work. Differentiate from it. | arXiv free; Handbook chapter NEEDS-ACCESS (grey copies: ResearchGate/Academia) |

### Mathematical bedrock (cite at theorem strength)
Hurder–Katok, Publ. IHES 72 (1990) — free at Numdam; Hurder's 2002 survey "Dynamics and the Godbillon-Vey classes" — free at author page; Connes, *Noncommutative Geometry* (1994) — free at alainconnes.org; Connes, "The von Neumann algebra of a foliation" (1978) — free scan.

### Adjacent, non-threatening (log and move on)
Armas et al., GV invariants of non-Lorentzian spacetimes (arXiv:2304.12722 — no algebras); Ebisu–Honda–Nakanishi, fracton field theories from GV (arXiv:2408.05048 — no modular theory); Martinetti, thermal time as emergent time (arXiv:1203.4995 — no foliations); Chua, "The Time in Thermal Time" (arXiv:2407.18948 — philosophy); Requardt, crossed products & type III→II∞ in QG (arXiv:2507.01419 — no foliations); I.Y. Park, foliation-based QG (arXiv:1902.03332 — no GV); Jacobson, entanglement equilibrium (arXiv:1505.04753 — the first-law leg, zero GV content).

### Logged empties (claim a)
`"modular Hamiltonian" "Einstein equations" foliation` · `"codimension one foliation" "arrow of time"` · `"Godbillon-Vey" entanglement "first law" gravity` · GV+thermal-time as a substantive join · GV+flow-of-weights outside pure math. **The GV ↔ first-law channel has zero literature.**

---

## 2. Claim (b) catalog — monopole Floer ↔ DHR

### Near-misses (all must-reads are marked)

| Paper | Why it's close / why it isn't the claim | Access |
|---|---|---|
| **Casini–Magán, "A generalization of the DHR theorem for higher form symmetries" (arXiv:2511.21810, Nov 2025)** | The AQFT community's nearest approach to magnetic (degree-2) sectors in DHR style — order/disorder parameters, 't Hooft loops, abelian labels. No H²(Σ;ℤ), no Spin^c, no Floer, no protected-content statement. **MUST READ IN FULL — top residual risk for claim (b).** | free |
| Ciolli–Ruzzi–Vasselli, "Where charged sectors are localizable" (arXiv:2306.08449, CMP 2023) | Covariant-cohomology charge transporters generalizing Roberts; abstract shows no degree-2 content. **Must-skim full text for degree-2 remarks.** | free |
| Riello–Schiavina, "Hamiltonian gauge theory with corners: … flux superselection" (arXiv:2207.00568) | Classical flux superselection as symplectic reduction; "road map to quantum superselection"; no DHR category, no H² labeling, no Floer. **Must-skim.** | free |
| Vasselli, "Presheaves of superselection structures in curved spacetimes" (arXiv:1211.1812; CMP 2015) | C*-gerbes — a degree-2 structural gesture — but built from projective π₁-reps, not H² magnetic classes. | arXiv free (journal paywalled) |
| Brunetti–Ruzzi (arXiv:0801.3365); Ruzzi–Vasselli (arXiv:1811.12121); Dappiaggi–Ruzzi–Vasselli (arXiv:1912.05297) | The claim's stated baseline: topological sectors at degree 1 (π₁/H¹). Forward-citation cone checked: **nobody has pushed to H².** | free |
| Bais–Schroers (hep-th/9708004) | Magnetic charge lattice in YMH (the phase-13 "label content is known" source); no DHR, no 3-manifold functoriality, no Floer. Citation cone (35 papers, INSPIRE) contains no join. | free |
| Strocchi–Wightman, "Superselection rule for magnetic charges" (Phys. Lett. B 1972) | The historic ancestor: magnetic charge superselects — no cohomological lattice, no category. | NEEDS-ACCESS: https://www.sciencedirect.com/science/article/abs/pii/0370269272907496 |

### Logged empties (claim b)
`"monopole Floer" superselection` · `"Seiberg-Witten Floer" "superselection sectors"` · `"Heegaard Floer" "algebraic quantum field theory"` · `"spin-c structures" superselection` · `"wall-crossing invariant" superselection` · `"Floer homology" "superselection"` (sole hit: an AMS sectional program, checked — no join) · Manolescu-SWF-as-physical-sectors. **The join is unstated on the open web.**

---

## 3. Cross-cutting catalog

- **"Protected stratum"** — free (only standard gauge-orbit stratification uses the word "stratum": Rudolph–Schmidt–Volobuev, CMP 2002, journal NEEDS-ACCESS https://link.springer.com/article/10.1007/s002200000286, companion free at hep-th/9404059; cite to disambiguate).
- **"Geometry-first"** — unused as a program name, but semantically collides with Giddings' "quantum-first" (arXiv:1805.06900, 1803.04973, both free): position as the deliberate opposite.
- **Doplicher–Roberts originals** (the §2.1 bedrock): CMP 131 (1990) and Invent. Math. 98 (1989) — NEEDS-ACCESS at Springer (https://link.springer.com/article/10.1007/BF02097680, https://link.springer.com/article/10.1007/BF01388849); Project Euclid scans of the CMP paper circulate.
- **New adjacent items for §8C-adjacent cataloguing:** Giné, quantum-from-multifractal-geometry (arXiv:2602.16219, 2026); Takayanagi, emergent holographic spacetime from quantum information (arXiv:2506.06595, 2025); Chua, "Physical Coherence and Time's Emergence" (arXiv:2605.24970, 2026 — philosophy). None is a 3D-manifold-fundamental competitor beyond BHMM and Chishtie.
- **Logged empties:** `"geometry fixes physics" Tannaka` · `"Kaluza-Klein without the extra dimension"` · `"charge quantization" "first Chern class" "superselection"` · `"emergent time" + Floer` (both variants) · folding/rigidity metaphor.

---

## 4. The NEEDS-ACCESS list (for Harry)

Priority order — items the sweep could not download; links for institutional access:

1. **Asselmeyer-Maluga, *The Wild Fractal Nature of Spacetime* (World Scientific, 2025)** — https://www.worldscientific.com/worldscibooks/10.1142/14188 — the single item that could change claim (a)'s verdict.
2. Doplicher–Roberts 1990 (CMP 131) — https://link.springer.com/article/10.1007/BF02097680 — and Doplicher–Roberts 1989 (Invent. Math. 98) — https://link.springer.com/article/10.1007/BF01388849.
3. Asselmeyer-Maluga–Król, Phys. Dark Universe 19:66 (2018) published version of arXiv:1709.03314 (check for post-arXiv changes re GV→Λ).
4. Strocchi–Wightman 1972 — https://www.sciencedirect.com/science/article/abs/pii/0370269272907496.
5. Springer-chapter version of 1601.06436 (*At the Frontier of Spacetime*) — https://link.springer.com/chapter/10.1007/978-3-319-31299-6_15 (check §6 differences vs arXiv).
6. Bertozzini, "Modular Algebraic Quantum Geometries for QG," Handbook of Quantum Gravity (Springer, ~2023) — grey copies on ResearchGate/Academia.
7. Rudolph–Schmidt–Volobuev, CMP 2002 (low priority — disambiguation citation only).
8. MathSciNet/zbMATH: run `57R57×81T05`, `57R30×46L36`, `46L60×83C45` and the §1–§2 quoted phrases (I have no access).

## 5. Full-text must-read queue (all free)

1. arXiv:1601.06436 §§6–7, §12 (AMK — the GV = modular-generator passages, exact scope).
2. arXiv:2209.08056 (AMK–Wilms — how far the Connes–Rovelli citation goes).
3. arXiv:2511.21810 (Casini–Magán — whether higher-form DHR contains an H²/3-manifold remark).
4. arXiv:2306.08449 (Ciolli–Ruzzi–Vasselli) and arXiv:2207.00568 (Riello–Schiavina) — degree-2 skims.
5. arXiv:1007.4094 (Bertozzini et al. — differentiate the modular-spacetime program).

## 6. Consequences for the CORE document (applied)

§6.4's candidate-novel item (a) is narrowed to: **(a′) the protection/clock reading of the AMK GV↔modular identification (which is theirs and must be credited), its thermal-time/emergent-time interpretation, the GV↔entanglement-first-law weld (zero prior literature), and the GV→Λ→1/G reconciliation chain.** Item (b) stands as candidate-novel, sweep-clean, gated on the §5 must-reads. The expert-outreach list gains a sharpened rationale: AMK are no longer just "adjacent" — they are the owners of the core identification and the first email should acknowledge exactly that.

*Sweep records: four agent reports, 2026-07-11; ~45 queries; empties logged verbatim above. Residual risk register: the 2025 AMK book (item 4.1); MathSciNet/zbMATH (item 4.8); full texts in §5.*

---

# Part 2 — The AMK 2025 book, front matter read (2026-07-11, same day)

*Harry obtained the preface + introduction + full table of contents of Asselmeyer-Maluga, "The Wild Fractal Nature of Spacetime" (World Scientific, 2025; single-author — Król thanked, not coauthor). This was the §4 top-risk item. Findings:*

## What the book claims (from preface, principles §1.4, and ToC)

1. **GV → dynamics is now AMK's, in print.** Stated result: "The quantum action is an expression on the operator algebra (the leaf space), defined by the flow of weights to express the Godbillon-Vey invariant (as invariant of the foliation). This action is shown to have the correct scaling behavior" — with Ch. 6.3 titled "The flow of weights as quantum action" and Ch. 6.4.1 recovering the Einstein–Hilbert action at long scales. His derivation route is **scaling/conformal-invariance** (he says explicitly he uses the string-theory beta-function connection for the long-scale limit) — **not** the entanglement first law.
2. **Codim-1 foliation as the origin of the space/time split is his principle (2):** "Locally, one has a decomposition of the spacetime into space and time, i.e. there is a codimension-1 foliation"; "The division into space and time is only locally possible … it is the codimension-1 foliation which is responsible for this property." Ch. 4 constructs the foliation on exotic S³×ℝ "which can be used to construct a Lorentz structure"; Ch. 3.2.4 "Time function in exotic S³×ℝ"; **Ch. 6.6 "The structure of time"** — content unknown, the one remaining pin for the thermal-time question.
3. **Entanglement is treated topologically** ("wildly embedded 3-spheres … Entanglement is realized topologically. The transition to a tame embedding can be seen as decoherence") — no Jacobson/Casini/first-law content anywhere in the front matter.
4. **Ch. 4.6 "Charge quantization without magnetic monopoles"** (Dirac quantization via S¹-gerbes on S³) — directly adjacent to CORE §2.2; must be cited there.
5. Also confirmed in the book: Mostow-rigidity Λ (Ch. 7.5), dark matter as gravitational solitons (7.6), Starobinsky inflation from topology change with parameter determined (7.4), neutrino masses via seesaw (7.7), fermions as knot complements / bosons as torus bundles (Ch. 8) — all already credited in §8B.

## Updated novelty verdict for claim (a)

AMK now owns, in print: GV ↔ type III₁ ↔ modular generator ("Hamiltonian of the theory," 1601.06436); **GV/flow-of-weights as the quantum action with Einstein–Hilbert at large scale (2025 book, scaling route)**; and the codim-1-foliation origin of the local space/time split. What the front matter shows NO trace of, and which therefore remains candidate-novel for this program: **(i) the "rigidity = protection" reading** (GV as *protecting structure* / the protected-stratum principle — absent from his four principles); **(ii) the thermal-time/KMS reading of emergent time and its arrow** (pending Ch. 6.6 — the single remaining pin); **(iii) the entanglement-first-law route to the Einstein equations from GV** (his route is scaling/conformal; the first-law weld remains zero-literature); **(iv) the elastic-modulus reconciliation (§4.1(iii))**; **(v) T1-core as a stated open problem**; and all of claim (b). Note the two routes to "GV → Einstein equations" (his scaling vs our conjectured first-law) are *complementary, not duplicative* — if both work they should agree, which is itself a checkable consistency statement.

## Remaining access request
**Chapter 6 (especially 6.3, 6.5, 6.6) and Ch. 4.6** are the decisive reads. Ch. 6.6 "The structure of time" determines whether item (ii) survives.

---

# Part 3 — Full read of arXiv:1601.06436 (must-read #1: DONE, 2026-07-11)

*Harry supplied the full 52-page text. Read: §6.1.1 (modular intermezzo), §6.2–6.3 (states/skein), §7 (quantum action), §8 (scaling), §10–13 (fluctuations, decoherence/entanglement, cosmology, conclusions). Corrections and additions to Parts 1–2:*

## Corrections to the earlier record

1. **The GV → Einstein–Hilbert result is already in the 2016 paper, not first in the 2025 book.** §7 defines the quantum action S = Tr_ω(GV_HC) (Dixmier trace of the Godbillon–Vey cyclic-cohomology class), states "S is the action or the Hamiltonian multiplied by the time," gives the spectral-action-like form S = Tr_ω([D,X^μ][D,X_μ]|D|⁻²) (his eq. 15), and notes integer GV → Euler class, rational → Pontrjagin, yielding "the Einstein–Hilbert and the Holst action but also a correction given by irrational values of the Godbillon-Vey number." §8.1 then runs GV = r² through a nonlinear-sigma-model RG flow → Ricci flow → constant-curvature geometries at large scale. The 2025 book consolidates this; priority is 2016.
2. **Connes–Rovelli is cited but not developed.** The introduction says §7 uses the Tomita–Takesaki splitting "to introduce the dynamics (see Connes and Rovelli [44] with similar ideas)" — a pointer, no more. The body never interprets the modular flow as *physical/thermal time*: §11's time is "one coordinate along the Casson handle as time axis," and the conclusions' first open question is verbatim **"What is the Hamiltonian of the theory? In principle we constructed this operator but have a problem connecting to Loop quantum gravity."** So the thermal-time/KMS reading, the arrow, and the protection framing remain unclaimed — and the program's **T1-core is essentially AMK's own first open problem, sharpened**. (Outreach framing gift.)

## New findings from the full text

3. **The Chern–Simons gradient-flow bridge (research lead for CORE §6 item 5).** §8.1 states his large-scale flow equation "is equivalent to the (anti-)self-dual curvature (or instantons) by using the gradient flow of the Chern–Simons functional." That is *literally the flow whose Morse homology is instanton Floer homology* — i.e., AMK's classical dynamics is the gradient flow underlying the Floer complexes this program uses as protected sector content. Neither he nor anyone else joins the two: a concrete connective thread between claim (a)'s owner and claim (b)'s machinery, unclaimed on both sides.
4. **An adjacent falsifiable number:** §11 computes a *minimal gravitational decoherence time* T_dec ≈ 10⁻²⁴ s (from a 5-stage Casson tower: CS(Σ₁) = 5/8, vol(Σ₁) ≈ 18.319, θ ≈ 87.93, T_dec = T_Planck·e^{θ/2}) — "the collapse of the wave function is caused by a gravitational interaction." Adjacent-framework testable (gravitational-decoherence experiments); log for the phase-27 ledger's adjacent list, not as this program's prediction.
5. **§12 confirms** the inflaton-as-Morse-function construction (Starobinsky with λ = √(2/3), ρ = 3M²), Λ from 4-manifold Mostow rigidity, dark sector from exotic smoothness — all as credited in §8B.

## Updated claim-(a) verdict (final for this source)
Unchanged from Part 2, with sharpened boundaries: AMK owns *GV = modular generator = "Hamiltonian"* (2016), *GV as quantum action → EH/Holst at large scale via RG/Ricci flow* (2016, consolidated 2025), and the *codim-1 space/time split* (2025 principles). Unclaimed and still candidate-novel here: the thermal-time/KMS reading of emergent time + its arrow (his own open problem list confirms the Hamiltonian's physical interpretation is open); the rigidity = protection / protected-stratum framing; the entanglement-first-law route (his EH derivation is RG/spectral, not entropic); the elastic-modulus reconciliation; T1-core (= his open problem #1, made precise); and all of claim (b). Must-read queue: 1601.06436 ✅ DONE; remaining: 2209.08056, 2511.21810, 2306.08449, 2207.00568, 1007.4094, and the book's Ch. 6.6.

---

# Part 4 — Final consolidation: all must-reads closed (2026-07-11)

*Casini–Magán read directly (abstract + full-text term-sweep) after the agent run stalled; Bertozzini, AMK–Wilms, CRV, Riello–Schiavina by full-read agents; the AMK 2016 paper and 2025 book read directly (Parts 2–3 + the book's §6.6, Ch. 4.6). Final verdicts:*

## Casini–Magán (arXiv:2511.21810) — threat: NONE; value as tool: HIGH

Their setting is **flat space E = ℝ^d** ("The set E is 'the space'… rather than spacetime"), with all topology carried by the *shape of regions* (rings, knots, links), not by the Cauchy surface. Terms "3-manifold," "Cauchy surface," "H²," "Spin-c," "Floer," "monopole" are **absent from the full text**; magnetic objects appear only as 't Hooft loops in flat space. **Claim (b) is untouched.** But the machinery is exactly what §2.1's scope limit 2 needs: they reformulate DHR through **Haag-duality violations (HDV) for topologically nontrivial regions** — precisely the mechanism (Maxwell nets violating Haag duality on nontrivial regions) that made magnetic sectors non-DHR in the classical framework — and prove the HDV categories for regions with nontrivial πᵢ (0 < i < D−2) are classified by **abelian groups**, with a Hermiticity constraint in D = 4n for middle-dimensional loops, and knot parameters classified by unknot parameters with commutators given by **linking numbers**. Adaptation program (3 concrete steps): (i) transplant their HDV analysis from ℝ³ to a closed Σ, where nontrivial region-topology is *sourced by H*(Σ)*; (ii) identify the resulting abelian label group with H²(Σ;ℤ) (dual: the program's Ĝ) — this would convert CORE §2.1's "[conjecture that DR-type reconstruction extends]" into a corollary of their theorem; (iii) their linking-number commutator should reproduce, on Σ, the flux-sector commutation the program's §5 dictionary expects. **Recommended: cite as the admissibility framework; add Casini–Magán to the §6.4 expert list** (Casini already on it for the entanglement side — now doubly relevant).

## Final novelty verdicts (stable across all seven must-reads)

**Claim (a), final scope.** AMK own in print: GV↔type III↔modular generator ("the Hamiltonian of the theory," 2016); GV as quantum action → EH+Holst via RG/Ricci flow (2016); the **thermal-time reading** — "the time flow is determined by the Godbillon–Vey invariant of the foliation, defining the physical time flow" — plus a **topological-complexity arrow** (open-tree-of-CTC-resolutions) and the codim-1 space/time split (2025 book §6.6, principles); the GV↔3D-SW/Spin^c bridge (book Ch. 4.6); gravisolitons with w = 0 and the polarization conjecture (2012.05358). Bertozzini et al. own the programmatic "geometry from modular flow" (no GV, no arrow — their modular generator is spectrum-symmetric, structurally arrowless). **Remaining candidate-novel for this program:** (a1) the "rigidity = protection" / protected-stratum framing (absent everywhere); (a2) the **KMS-monotonicity arrow** (AMK's arrow is complexity-based — a *different derivation*; the KMS route is unclaimed); (a3) the **entanglement-first-law route** to the Einstein equations from GV (zero literature; complementary to AMK's RG route — agreement of the two routes is itself a checkable claim); (a4) the elastic-modulus reconciliation; (a5) **T1-core as a precise problem** (AMK's identifications remain assertion-level; the program's corrections — type III component vs III₁, "relates" vs "determines" — apply to the book as well); (a6) the class-V assembly (phase 32: Gleason-forced Born rule + statisticality from the GV fold — the sweep found no prior "GV foliation ⇒ Gleason" chain anywhere).

**Claim (b), final scope: CLEAN.** Seven full reads plus the sweep: nobody joins Floer theory to DHR/superselection; the AQFT line stops at degree 1 (CRV: strictly degree-1 covariant cohomology on simply connected spacetimes); Riello–Schiavina: classical degree-0 corner fluxes; Casini–Magán: flat-space region-topology, no H²(Σ), no Floer. The join — **H²(Σ;ℤ) magnetic sectors with HM(Σ) as protected content, now including the phase-30 dark-sector arm (HM_red ↔ gravisolitons)** — is unclaimed, with Casini–Magán supplying the missing admissibility machinery rather than competing. Residual risk: MathSciNet/zbMATH pass (Harry) and expert replies.

**The outreach order, finalized:** (1) Asselmeyer-Maluga — collegial: the program independently arrived at, corrected (III₁/determined-by), and extended (protection, KMS arrow, first law, Born-rule assembly, HM_red dark census) his line; his open problem #1 is T1-core. (2) Casini/Magán — their theorem is the requested admissibility tool; the H²(Σ) transplant is a well-posed question they could answer quickly. (3) Manolescu or another Floer expert — the phase-28 computations + the Σ_g×S¹ torsion question. (4) Rovelli (thermal time / KMS arrow), Vasselli–Ruzzi (degree-2 extension of their line), Bertozzini (modular geometry machinery for T1).
