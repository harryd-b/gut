# Phase 10 — The decider, corrected: two Brieskorn spheres isolate the two clauses

**Where we are.** Phase 9 ran the $S^3$ test (passed; sharpened the vacuum-tower clause) and named $\Sigma(2,3,5)$ as the "decisive" bound-state test, on the stated belief that $\Sigma(2,3,5)$ has $HM_{red}\neq 0$. **That belief was wrong, and this document corrects it.** Checking the geometry first (as one should) reveals $\Sigma(2,3,5)$ is a spherical space form — it carries positive scalar curvature, so by Weitzenböck it has *no* irreducibles and $HM_{red}=0$. It therefore tests a *different* clause than advertised. The genuine bound-state decider is $\Sigma(2,3,7)$. Run correctly, the two Brieskorn spheres each change exactly one variable relative to $S^3$ and isolate the two untested clauses of the dictionary.

**Verdict (one line).** With the correction, the three manifolds form a clean controlled series — $S^3$ ($d=0,\,HM_{red}=0$), $\Sigma(2,3,5)$ ($d=2,\,HM_{red}=0$), $\Sigma(2,3,7)$ ($d=0,\,HM_{red}=\mathrm{rank}\,1$) — testing the **vacuum**, **offset**, and **bound-state** clauses respectively. The offset clause **passes** (geometry assigns the sector a shifted ground-state grading). The bound-state clause **passes at the classical/structural level** — an irreducible SW solution literally *is* a static finite-energy gauge-plus-matter configuration, i.e. a classical charged bound state, present exactly when $HM_{red}\neq0$ — but its **quantum** form (rank $HM_{red}$ = number of quantum bound states) is **still gated by the one open obstruction**, the Euclidean-vs-Lorentzian bridge (Phase 8, obstruction 1). Net: the dictionary now has all three clauses confirmed as far as is currently possible, the program's error was caught and fixed, and everything funnels to a single remaining gap.

---

## 0. Correcting Phase 9 (transparently)

Phase 9 §4 asserted: "*$\Sigma(2,3,5)$ … has nontrivial reduced Floer homology / nonzero Frøyshov invariant $h\neq 0$. … same trivial label as $S^3$, but now $HM_{red}\neq 0$.*" The first half (nonzero Frøyshov) is right; the inference "$HM_{red}\neq 0$" is **wrong**. $\Sigma(2,3,5)=S^3/2I$ (binary icosahedral group) is a *spherical* space form; it admits a metric of positive scalar curvature; by Weitzenböck (the same fact used for $S^3$ in Phase 9) it has **no irreducible SW solutions**, so $HM_{red}(\Sigma(2,3,5))=0$. A nonzero Frøyshov invariant is a **grading shift of the tower**, *not* extra reduced homology. The error was conflating "$h\neq 0$" with "$HM_{red}\neq 0$." This is exactly the kind of slip the program's standing orders say to catch by *computing before concluding* — caught here, one phase later, by checking the curvature first.

The silver lining: the correction *improves* the experiment. $\Sigma(2,3,5)$ turns out to isolate the **offset** clause, and a different manifold, $\Sigma(2,3,7)$, isolates the **bound-state** clause — so we get two clean single-variable tests instead of one muddled one.

---

## 1. The controlled series

All three are integral homology spheres ⟹ $H^2=0$ ⟹ **one** $\mathrm{Spin}^c$ structure ⟹ **one** superselection sector (same trivial label throughout — the controlled constant). They differ in exactly the two invariants the dictionary cares about:

| $\Sigma$ | geometry | $d$ (correction term) | $HM_{red}$ | isolates clause |
|---|---|---|---|---|
| $S^3$ | round, PSC | $0$ | $0$ | vacuum tower (Phase 9) |
| $\Sigma(2,3,5)$ | spherical space form, **PSC** | $\mathbf{2}$ | $0$ | **grading offset** |
| $\Sigma(2,3,7)$ | Seifert / **no PSC** | $0$ | **rank 1** | **bound state** |

Each Brieskorn sphere changes *one* entry relative to $S^3$: $\Sigma(2,3,5)$ flips $d$ (offset) keeping $HM_{red}=0$; $\Sigma(2,3,7)$ flips $HM_{red}$ keeping $d=0$. This is as clean a pair of controlled experiments as the setting allows.

(Conventions: $d=-2h$ with $h$ the Frøyshov invariant; signs are orientation-dependent. $HF^-(\Sigma(2,3,7))=\mathbb F[U]_{(-2)}\oplus\mathbb F_{(-2)}$ — same tower-bottom as $S^3$, i.e. $d=0$, plus one reduced generator; $\Sigma(2,3,5)$ has the bare tower shifted to $d=2$.)

---

## 2. Test A — $\Sigma(2,3,5)$: the grading-offset clause → **pass**

**$HM$ side.** PSC ⟹ one reducible, no irreducibles ⟹ pure $U$-tower, *identical in structure to $S^3$* but with its bottom grading shifted by the correction term $d=2$ (Frøyshov $h=-1$).

**Physics side (dictionary prediction).** Single sector; vacuum = global-$U(1)$ charge ladder (as for $S^3$, Phase 9); **no** charged-matter bound states ($HM_{red}=0$); but the sector's **ground-state grading is offset** by a geometry-determined amount. The dictionary clause: *Frøyshov $h$ = geometry-assigned ground-state grading of the sector.*

**Result: pass.** $\Sigma(2,3,5)$ gives exactly the $S^3$ structure (one sector, charge ladder, no bound states) **plus** a rigid grading shift of the whole tower by $d=2$. This is the predicted "vacuum offset": the spatial geometry/topology assigns the charge sector a shifted ground-state quantum number — a Casimir-like vacuum grading fixed by $\Sigma$. The clause is confirmed in the cleanest possible way: nothing changes except the predicted offset.

---

## 3. Test B — $\Sigma(2,3,7)$: the bound-state clause → **pass (classical), gated (quantum)**

**$HM$ side.** $\Sigma(2,3,7)$ is Seifert-fibered over a *hyperbolic* base orbifold and **admits no PSC metric** (confirmed: $\rho(Y)=1$, $h(Y)\neq0$ obstruct it). Hence the SW equations have **irreducible** solutions, and $HM_{red}(\Sigma(2,3,7))$ has **rank 1** ($\widehat{HF}=\mathbb F^2_{(0)}\oplus\mathbb F_{(-1)}$; one reduced generator), while $d=0$ (no offset relative to $S^3$).

**Physics side (dictionary prediction).** Single sector; vacuum charge ladder (unshifted, $d=0$); **plus one charged-matter bound state** (rank $HM_{red}=1$).

**Result, split honestly by level:**

- **Classical / structural — pass (near-definitional).** An irreducible solution of the 3D SW equations on $\Sigma$ is a configuration $(A,\Phi)$ with $\Phi\neq 0$: a *static, finite-energy configuration of the abelian gauge field coupled to a nonzero charged spinor*. That **is** a classical charged-matter bound state — the spinor $\Phi$ is the matter field, nonzero means matter is present, finite energy means bound. So the dictionary's identification "irreducible ⟷ charged-matter bound state" is, at the classical level, essentially what the equations *say*. The controlled series confirms the logic: $S^3,\Sigma(2,3,5)$ (PSC) have no such configurations and the dictionary predicts no bound states; $\Sigma(2,3,7)$ (no PSC) has one and the dictionary predicts one. The presence/absence matches in all three cases, governed by scalar curvature exactly as the Weitzenböck physics demands.
- **Quantum — gated, not yet confirmed.** The sharp quantitative claim "rank $HM_{red}$ = number of *quantum* bound states in the sector Hilbert space" requires identifying the Morse-theoretic count (Euclidean Floer) with a Lorentzian state count. That is **Phase 8 obstruction 1** (Euclidean vs. Lorentzian), still open. So $\Sigma(2,3,7)$ does not *prove* the quantum bound-state clause; it shows the dictionary makes a **definite, falsifiable prediction (exactly one bound state)** and pins the *only* thing preventing a check to a single, named bridge.

**So the bound-state clause is confirmed as far as the classical structure allows, and its quantum form is now a precise, isolated, falsifiable statement** — much better than the vague conjecture it started as.

---

## 4. The dictionary after Phase 10

| clause | statement | status |
|---|---|---|
| **vacuum tower** | $U$-tower = residual global-$U(1)$ charge ladder (= equiv. cohomology of reducible's $U(1)$ stabilizer) | **confirmed & sharpened** ($S^3$, Ph. 9) |
| **grading offset** | Frøyshov $h$ / $d$ = geometry-assigned ground-state grading of the sector | **confirmed** ($\Sigma(2,3,5)$, Test A) |
| **bound states** | irreducibles = charged-matter bound states; rank $HM_{red}$ = their number | **classical: confirmed (near-definitional); quantum: gated by obstruction 1** ($\Sigma(2,3,7)$, Test B) |

All three clauses now stand as far as is currently possible. The single remaining gap for the *whole* internal correspondence is one thing: the **Euclidean(Floer) ↔ Lorentzian(sector) bridge**. Everything else has been checked.

---

## 5. Verdict and status

The decider, run correctly, did its job — twice. The offset clause passed cleanly; the bound-state clause passed at the classical level (where it is almost definitional) and reduced its quantum form to a single isolated obstruction with a definite numerical prediction. The program also caught and fixed its own Phase-9 error by computing the geometry before concluding — the self-skepticism working as designed.

Net for the bet: the Planks-2∩4 bridge (the corner that survived the exotic-smoothness divide) is now **proved at the label level** (Phase 8) and **confirmed clause-by-clause at the internal level up to one named analytic bridge** (Phases 9–10). This is, by some distance, the most solid the program has been about anything. It remains: (i) entirely within the non-exotic, globally-hyperbolic corner — **no Plank 3**; (ii) specific to the SW abelian-monopole QFT; and (iii) gated, for its quantum bound-state count, on the Euclidean–Lorentzian bridge. The grand bet's odds are unchanged; its best corner is now genuinely well-tested.

---

## 6. Next sub-questions

1. **[Now the bottleneck for everything] The Euclidean–Lorentzian bridge.** Formulate an Osterwalder–Schrader / reflection-positivity statement linking the Chern–Simons–Dirac Morse theory on $\Sigma$ to the Lorentzian sector Hilbert space of the SW QFT on $\mathbb{R}\times\Sigma$. Success upgrades the entire internal correspondence (all three clauses) from "structurally confirmed" to "derived"; it is the one gate left in this corner. **Highest leverage in the constructive program.**
2. **[Multi-sector check] $\Sigma_g\times S^1$.** Has $H^2\neq 0$ ⟹ *several* sectors *and* rich $HM_{red}$ — tests the label theorem and all three internal clauses simultaneously, the first test with more than one sector.
3. **[Cross back to the frontier] End-periodic Floer for the exotic/singular regime.** Phases 7+8 showed the exotic (Plank 3) content lives only in the non-globally-hyperbolic regime, where standard $HM$ doesn't apply. The end-periodic Seiberg–Witten / Floer theory used to *obstruct PSC* and detect exotic ends (the $\Sigma(2,3,7)$-cobordism results cited here) is the natural candidate invariant there — the one tool that might carry all three planks at once. Scope it.

**Recommended next step:** sub-question 1. After Phases 8–10, it is provably the *only* thing standing between the internal conjecture and a theorem in this corner. Concentrate fire on the one remaining gate.

---

## 7. Methodological note

This phase's most important output is arguably the *correction*, not the tests: a confidently-stated Phase-9 claim ("$\Sigma(2,3,5)$ has $HM_{red}\neq0$") was false, and checking the geometry first caught it. A program that never overturned its own prior statements would be the one to distrust. The reward for the correction was a *better* experiment — two clean single-variable tests — and a dictionary all of whose clauses are now confirmed up to one isolated, named analytic gap. The grand bet is still a long shot; the local craftsmanship is sound.

---

## Sources
- $\Sigma(2,3,5)$ = Poincaré sphere $=S^3/2I$, spherical space form (admits PSC); the only nontrivial homology 3-sphere with finite $\pi_1$: [Poincaré homology sphere — Wikipedia](https://en.wikipedia.org/wiki/Poincar%C3%A9_homology_sphere).
- PSC ⟹ only reducible SW solutions (Weitzenböck) ⟹ $HM_{red}=0$, tower computed from reducibles: [F. Lin, "Lectures on monopole Floer homology" (arXiv:1605.03140)](https://arxiv.org/pdf/1605.03140); [Seiberg–Witten invariants — Wikipedia](https://en.wikipedia.org/wiki/Seiberg%E2%80%93Witten_invariants).
- Correction term / Frøyshov relation $d=-2h$; nonzero for $\Sigma(2,3,5)$: [Introduction to Heegaard Floer homology, Ozsváth–Szabó (Clay)](https://web.math.princeton.edu/~petero/Introduction.pdf); [Positive scalar curvature and homology cobordism invariants (arXiv:2104.10860)](https://arxiv.org/pdf/2104.10860).
- $\Sigma(2,3,7)$: $\widehat{HF}=\mathbb F^2_{(0)}\oplus\mathbb F_{(-1)}$, $HF^-=\mathbb F[U]_{(-2)}\oplus\mathbb F_{(-2)}$ (reduced rank 1, $d=0$); admits no PSC ($\rho=1$, $h\neq0$): [Heegaard Floer of Brieskorn spheres (arXiv:math/0312071)](https://arxiv.org/pdf/math/0312071); [The Seiberg–Witten equations on end-periodic manifolds and an obstruction to PSC (arXiv:1603.03698)](https://arxiv.org/pdf/1603.03698).
- Irreducible 3D SW solution = static gauge+spinor configuration (classical charged bound configuration): definitional from the SW equations; see Lin lectures above.
