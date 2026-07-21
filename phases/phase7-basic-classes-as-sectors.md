# Phase 7 — Do Seiberg–Witten basic classes appear as superselection sectors?

**Where we are.** Phase 6 found that exotic smoothness is physical (it sources gravity, theorem) but exotic-*blind* to the charge spectrum (which is topological), and that the smooth structure is detected by an abelian $U(1)$ monopole gauge theory (Seiberg–Witten), selecting a distinguished subset of $H^2$ — the *basic classes*. The recommended next step, and the point where Planks 2, 3, 4 would fuse operationally: **can the SW basic-class pattern be reinterpreted as a preferred set of monopole superselection sectors / a preferred Spin$^c$ vacuum in the AQFT net of Phases 4–5?** This document tests that and finds a theorem-backed obstruction, a surviving partial bridge, and — most valuably — the recurring structural pattern of the whole bet.

**Verdict (one line).** The full three-plank bridge is **blocked by a theorem**: the AQFT superselection apparatus requires **global hyperbolicity**, which (Bernal–Sánchez) forces the spacetime to be smoothly $\mathbb{R}\times\Sigma$ — the *standard* structure with **no exotic smoothness**; conversely an exotic $\Sigma\times\mathbb{R}$ is **never globally hyperbolic** and must contain **naked singularities** (Asselmeyer-Maluga). So SW basic classes (the smooth fingerprint) and DHR sectors (the superselection apparatus) **cannot coexist on the same spacetime** under standard assumptions. What *survives* is a Planks-2∩4 bridge with **no** exotic content: the **monopole (Seiberg–Witten) Floer homology of the Cauchy 3-manifold $\Sigma$**, graded by $\mathrm{Spin}^c(\Sigma)\subset H^2(\Sigma;\mathbb{Z})$ — the very monopole-charge lattice — organizes the monopole sectors. The escape that would restore Plank 3 is to **drop global hyperbolicity**, which is the *same class of move* as Phase 3's dropping of the global S-matrix. That recurrence is the real finding.

---

## 1. The two objects and their cohomology homes

| | AQFT monopole sectors (Ph. 4–5) | SW basic classes (Ph. 6) |
|---|---|---|
| lives on | globally hyperbolic Lorentzian $M^4\cong\mathbb{R}\times\Sigma$ | **closed** Riemannian $X^4$, $b_2^+>1$ (or exotic open) |
| labeled by | $\mathrm{Spin}^c$ / charge in $H^2(\boldsymbol{\Sigma^3};\mathbb{Z})$ | $\mathrm{Spin}^c$ in $H^2(\boldsymbol{X^4};\mathbb{Z})$, $c\equiv w_2\,(2)$ |
| nature | kinematic: which charges can exist | smooth invariant: monopole moduli count |
| signature | Lorentzian | Euclidean |

Two mismatches stare back immediately: **dimension** ($H^2$ of the 3D slice vs. the 4D manifold) and **signature/compactness** (Lorentzian globally hyperbolic vs. closed Riemannian). The naive identification "basic class = preferred sector" silently assumes these line up. They do not — and the reason is a theorem, not a technicality.

---

## 2. The obstruction (theorem-backed): global hyperbolicity excludes exotic smoothness

**Bernal–Sánchez (2003–2005).** Every globally hyperbolic spacetime $M$ admits a smooth spacelike Cauchy hypersurface $\Sigma$ and is **diffeomorphic** (not merely homeomorphic) to the product $\mathbb{R}\times\Sigma$. So the *smooth structure* of a globally hyperbolic $M$ **is** the standard product structure.

**Consequence chain:**
$$
M \text{ globally hyperbolic} \;\xRightarrow{\text{B–S}}\; M \cong_{\text{diff}} \mathbb{R}\times\Sigma^3 \;\xRightarrow{\;\Sigma^3 \text{ smoothly unique (Moise)}\;} M \text{ has the standard smooth structure} \;\Rightarrow\; \textbf{no exotic smoothness.}
$$
(3-manifolds have unique smooth structures, and the smooth product $\mathbb{R}\times\Sigma$ is standard; exotic smoothness is a strictly 4-dimensional, *non-product* phenomenon.)

**Converse (Asselmeyer-Maluga).** An exotic $\Sigma\times\mathbb{R}$ (homeomorphic but not diffeomorphic to the product) **admits a Lorentz metric but is never globally hyperbolic**; one can choose the projection to $\mathbb{R}$ as a time function with no closed causal curves, but then the exotic spacetime **must contain naked singularities.** Exotic smoothness is itself an obstruction to global hyperbolicity.

**Therefore:**
> The DHR / curved-spacetime superselection framework (Phases 4–5) is built on **globally hyperbolic** spacetimes — which carry **no exotic smoothness**. Seiberg–Witten basic classes (Phase 6, the smooth fingerprint) require a **closed** $b_2^+>1$ manifold or an **exotic** open one — **neither globally hyperbolic**. The smooth-structure data and the superselection apparatus live on **disjoint classes of 4-manifolds.** The requested bridge (basic classes ⟶ preferred sectors) **cannot be built on a single spacetime** under standard assumptions.

This is a clean no-go, and it is the honest answer to the question as posed: *no — not because the analogy is shallow, but because the two structures provably cannot share a spacetime.*

### A striking corollary (where exotic smoothness physically lives)

The converse theorem says exotic smoothness forces **naked singularities** — i.e. its natural habitat is *exactly where causal regularity (and hence the standard superselection machinery, and the very notion of a global S-matrix) breaks down.* There is even a literature heading for this: "**cosmic censorship of smooth structures.**" So Phase 6's "exotic smoothness is physical" and Phase 7's obstruction combine into: *exotic smoothness is physical, and it is concentrated precisely at the causal pathologies that the nice frameworks exclude by assumption.* That is either the bet's deepest opportunity or its deepest trap — see §4.

---

## 3. The surviving bridge (Planks 2 ∩ 4, but not 3)

Drop the exotic ambition and a genuine, well-defined bridge remains — and it is the *right* object dimensionally:

**Seiberg–Witten (monopole) Floer homology of the Cauchy 3-manifold $\Sigma$** (Kronheimer–Mrowka). Take the 3D $\mathrm{Spin}^c$ structure $\mathfrak{s}$ on $\Sigma$; form the configuration space of $U(1)$-connection–spinor pairs $(A,\phi)$ mod gauge; the Chern–Simons–Dirac functional's Floer homology — gradient flows being solutions of the SW equations **on $\mathbb{R}\times\Sigma$** (i.e. the cylinder = the spacetime!) — is $\widehat{HM}(\Sigma,\mathfrak{s})$. It is:
- **graded by $\mathrm{Spin}^c(\Sigma)$**, an affine space over $H^2(\Sigma;\mathbb{Z})$ — *exactly the monopole-charge lattice that labels the superselection sectors in Phase 5*;
- a module over $\mathbb{Z}[U]\otimes\Lambda^*(H_1(\Sigma;\mathbb{Z})/\text{Tors})$ — the $H_1$ factor echoing the Aharonov–Bohm ($\pi_1$) sector data of Phase 5;
- built from the SW equations **on the physical cylinder $\mathbb{R}\times\Sigma$**, which *is* the globally hyperbolic spacetime.

So there is a real, dimensionally-correct candidate correspondence:
$$
\boxed{\ \text{monopole superselection sectors on } \mathbb{R}\times\Sigma \;\longleftrightarrow\; \text{generators/gradings of } \widehat{HM}(\Sigma) \text{ over } \mathrm{Spin}^c(\Sigma)\subset H^2(\Sigma;\mathbb{Z}).\ }
$$
The gauge-theoretic invariant of the *spatial slice* organizes the monopole sectors. This threads **Plank 2** (AQFT net) and **Plank 4** (gauge structure from geometry) cleanly.

**But — and this is the honest cost — it carries no Plank 3.** $\Sigma$ is a 3-manifold, smoothly unique; $\mathbb{R}\times\Sigma$ (globally hyperbolic) is the standard structure. There is **no exotic smoothness** anywhere in this bridge. The exotic content — the thing Phase 6 said was the bet's distinctive edge — is *exactly* what §2's obstruction excludes from the globally hyperbolic setting. The surviving bridge is good, but it is the two planks that were already compatible; the third remains walled off.

---

## 4. The real finding: the recurring sacrifice pattern

Step back across all seven phases and a structure appears. Every time the bet tries to make **two planks meet**, it is forced to **abandon a global regularity assumption**, and each abandonment lands the program in territory that is correct in principle but **unconstructed**:

| combination attempted | assumption that must be dropped | lands in |
|---|---|---|
| Plank 4 merger of spacetime+gauge (Ph. 3) | global **S-matrix** (Coleman–Mandula) | cosmological/confined AQFT (unconstructed for realistic gauge theory) |
| Planks 2+3+4 via basic classes (Ph. 7) | **global hyperbolicity** (Bernal–Sánchez) | non-globally-hyperbolic spacetimes with naked singularities (no superselection theory exists) |

These are not independent dodges — they are the *same kind* of move (give up an asymptotic/causal regularity that the rigorous machinery is built on), and they may even be the *same* move wearing two hats: no global S-matrix and no global hyperbolicity are both statements that the spacetime lacks the nice asymptotic/Cauchy structure. **The planks genuinely cohere on *what they sacrifice* — but the sacrifices compound into a single demand: the bet's true home is a 4-manifold that is neither asymptotically nice nor globally hyperbolic, possibly singular, where neither the S-matrix nor the standard superselection apparatus is available.**

That is the deepest honest statement the program has produced. It is simultaneously:
- *encouraging* — the bet is internally consistent; its escapes all point the same direction, which is not guaranteed and suggests a real (if exotic) regime rather than a grab-bag of excuses;
- *sobering* — that direction is precisely the regime where essentially none of the rigorous tools (S-matrix, DHR sectors, particle concept, Wigner classification) have been built, so the bet's payoff requires not one breakthrough but the *reconstruction of the whole apparatus* in a setting people have mostly avoided.

The exotic-smoothness/naked-singularity link (§2 corollary) is the same message a third time: the distinctive physics sits exactly at the causal pathologies the standard theory excludes.

---

## 5. Verdict and next sub-questions

**Direct answer to the Phase-7 question:** No — SW basic classes cannot be DHR superselection sectors on one spacetime, because global hyperbolicity (needed for the sectors) excludes exotic smoothness (where basic classes carry information). The honest *positive* residue is the monopole-Floer-of-$\Sigma$ bridge (Planks 2∩4, no exotic content).

**Next sub-questions, sharpened by this result:**

1. **(The bet's true frontier, now identified.)** Develop superselection / charge-sector theory on **non-globally-hyperbolic** 4-manifolds (with naked singularities / exotic ends). Does *any* sensible notion of charge sector survive there, and does it become exotic-smoothness-sensitive once global hyperbolicity is gone? This is where Plank 3 could re-enter — and it is almost entirely unbuilt. **Highest-leverage, highest-difficulty.**
2. **(Make the surviving bridge precise.)** State and test the conjecture of §3: that monopole superselection sectors on $\mathbb{R}\times\Sigma$ are classified/graded by $\widehat{HM}(\Sigma)$. This is a concrete, possibly-provable mathematical statement using existing machinery — a standalone result regardless of the grand bet.
3. **(Pin the meta-pattern.)** Are "no global S-matrix" and "no global hyperbolicity" *logically the same constraint* for this program, or merely similar? A precise statement of their relationship would tell the bet whether it faces one obstruction or two — and would consolidate Phases 3 and 7 into a single structural theorem about where the bet must live.

**Recommended next step:** sub-question 2. After two phases (6, 7) of obstructions, the program needs a *constructive* win, and the monopole-Floer/sector correspondence is the one concrete, buildable, theorem-shaped statement now in view. It also directly advances the Planks-2∩4 program that *did* survive — paying rent while the harder exotic frontier (sub-question 1) is scoped.

---

## 6. Methodological note

Phases 6 and 7 were both attempts to *confirm* the bet's most exciting claims and both returned obstructions — but obstructions that *located* the bet rather than killing it. That is the program working as designed: it now knows its true address (non-globally-hyperbolic, possibly-singular 4-geometry where exotic smoothness lives and the standard apparatus doesn't), which is far more than it knew at Phase 0. The grand bet remains a long shot, and Phase 7 added a specific reason it is hard (you must rebuild superselection theory off the globally-hyperbolic reservation). But "we found exactly which theorem stands in the way, and exactly which regime the bet must therefore inhabit" is the most a rigorous program can ask of a single phase.

---

## Sources
- Bernal–Sánchez smooth splitting: globally hyperbolic $\Rightarrow$ diffeomorphic to $\mathbb{R}\times\Sigma$, Cauchy surfaces smooth and unique up to diffeo: [Bernal & Sánchez, "On Smooth Cauchy Hypersurfaces and Geroch's Splitting Theorem," CMP 243 (2003) 461 (arXiv:gr-qc/0306108)](https://arxiv.org/abs/gr-qc/0306108); [Globally hyperbolic spacetime — Wikipedia](https://en.wikipedia.org/wiki/Globally_hyperbolic_spacetime).
- Exotic $\Sigma\times\mathbb{R}$ is never globally hyperbolic and must contain naked singularities; "cosmic censorship of smooth structures": [Asselmeyer-Maluga & Brans / related (arXiv:1006.2230)](https://arxiv.org/pdf/1006.2230); ["Cosmic censorship of smooth structures" (arXiv:1201.6070)](https://arxiv.org/pdf/1201.6070).
- Monopole (Seiberg–Witten) Floer homology of 3-manifolds, graded by $\mathrm{Spin}^c(Y)\subset H^2(Y;\mathbb{Z})$, gradient flows = SW on $\mathbb{R}\times Y$, module over $\mathbb{Z}[U]\otimes\Lambda^*(H_1/\text{Tors})$: Kronheimer–Mrowka, *Monopoles and Three-Manifolds* (2007); [overview "Floer theory and its topological applications" (arXiv:1508.00495)](https://arxiv.org/pdf/1508.00495); ["The equivalence of two Seiberg–Witten Floer homologies" (arXiv:1603.00582)](https://arxiv.org/pdf/1603.00582).
- 3-manifolds have unique smooth structure (Moise); exotic smoothness is 4D-only: standard low-dimensional topology.
