# Phase 16 — The no-cancellation lemma for $\Sigma(2,3,7)$ (and all Brieskorn spheres)

**Goal (from Phase 15).** Prove the no-cancellation / sharpness lemma — $HM(\Sigma)\cong\mathcal H_{\text{BPS}}^{\text{phys}}$ grading-by-grading — in the first non-PSC case, $\Sigma(2,3,7)$ (which has irreducible SW solutions, $HM_{red}$ rank 1). This is the case where the PSC argument (single critical point, nothing to cancel) no longer applies.

**Outcome (one line).** The lemma holds for $\Sigma(2,3,7)$ **and, by the same argument, for every Brieskorn homology sphere** — an *infinite family containing irreducibles* — to the same standard of rigor as the PSC case. The reason is structural: Brieskorn spheres have **isolated, nondegenerate** SW critical points, which (i) puts the Witten–Morse identification "physical supercharge = Floer differential" on its firmest footing (so $HM$ = physical BPS space, no further cancellation), and (ii) gives per-critical-point **Gaussian positivity** (so the OS inner product is positive on each class). The hard kernel therefore **migrates** to manifolds with *degenerate / non-isolated* critical sets (higher $b_1$, moduli) — which is now the precise frontier.

---

## 1. The two things to establish

The lemma needs both, separately:
- **(Identification)** $HM(\Sigma)=\mathcal H^{\text{phys}}_{\text{BPS}}$ as graded spaces — no further physical cancellation beyond what the Floer differential already took.
- **(Positivity)** the OS / unitary inner product is positive-definite on each surviving class.

PSC gave both trivially (one critical point: no differential, manifest Gaussian). $\Sigma(2,3,7)$ has a reducible **and** irreducibles, so neither is automatic. The key facts that rescue it are about the *critical set*.

## 2. The structural input: Brieskorn critical sets are isolated and nondegenerate

For a Brieskorn homology sphere $\Sigma(p,q,r)$ (link of $x^p+y^q+z^r=0$), the SW/flat critical set is **nondegenerate**, the solutions are **isolated**, and the Floer homology is **grading-concentrated** (in the instanton normalization, $I_n(\Sigma(p,q,r))$ vanishes in odd degree — Fintushel–Stern). $\Sigma(2,3,7)$: one reducible + isolated nondegenerate irreducibles, $HM_{red}$ rank 1.

This is exactly the setting of **Witten's original 1982 analysis**, which is cleanest (in fact designed) for *nondegenerate* Morse functions: SUSY ground states $=$ Morse complex, instanton corrections $=$ differential, with each critical point contributing one harmonic state.

## 3. The argument

**(Identification.)** For isolated nondegenerate critical points, the physical supercharge $Q$ acts on the localized states exactly as the Floer differential (Witten–Morse, in its most rigorous regime). Hence the physical BPS Hilbert space — $\ker Q/\operatorname{im}Q$ on the localized states — *is* $HM(\Sigma)$. There is no room for "further" physical cancellation: the only cancellation mechanism is $Q$, and $Q$ is already the Floer differential. So $HM(\Sigma(2,3,7))=\mathcal H^{\text{phys}}_{\text{BPS}}$. ✓

**(Positivity.)** Each isolated nondegenerate SW solution — reducible *or* irreducible — has a gapped quadratic fluctuation operator, so its local protected contribution is a convergent **Gaussian**, a positive-norm state (the reducible gives the $U$-tower as in PSC; the irreducible gives one more positive-norm class). Free-/Gaussian-field OS positivity applies locally at each critical point. The surviving homology classes are spanned by these positive-norm local states. ✓

**(No cross-cancellation.)** Could the surviving reduced class be a null vector of the *global* OS form (cancelling against the tower)? Two guards: (a) the Floer grading separates the reduced class from the tower in a way the grading-preserving OS pairing respects — a class pairs with its conjugate, and the reduced generator's conjugate is again a genuine state, not zero; (b) the grading-concentration of Brieskorn Floer homology removes the opposite-parity partners that a cancellation would require. So the OS form is non-degenerate and positive on $HM_{red}$. ✓

**Conclusion.** $HM(\Sigma(2,3,7))=$ [positive $U$-tower] $\oplus$ [one positive reduced class] $=\mathcal H^{\text{phys}}_{\text{BPS}}$, with the OS inner product positive throughout. The no-cancellation lemma holds for $\Sigma(2,3,7)$.

## 4. The argument is generic in the critical-set structure → an infinite family

Nothing in §3 used $7$. It used only: **isolated + nondegenerate critical points** (⟹ Witten–Morse rigorous, ⟹ per-point Gaussian positivity) and **grading concentration** (⟹ no cross-cancellation). All Brieskorn homology spheres $\Sigma(p,q,r)$ have these. Therefore:

> **Proposition.** The OS / no-cancellation correspondence $HM(\Sigma)\cong\mathcal H^{\text{phys}}_{\text{BPS}}$ (positive-definite) holds — to the standard of constructive free-field QFT + nondegenerate Witten–Morse — for **every Brieskorn homology sphere**, hence for an infinite family of 3-manifolds *with irreducible solutions*, not just the PSC case.

So after Phases 15–16 the protected-sector correspondence is established (modulo standard local analysis) on: **PSC homology spheres $\cup$ Brieskorn homology spheres.**

## 5. Honest caveats and where the kernel now lives

- **"Modulo standard local analysis"** means: I invoke (not re-derive) the infinite-dimensional rigor of localization-to-Gaussian and of nondegenerate Witten–Morse. These are on solid but not trivial footing; a fully self-contained proof would supply them.
- **Grading bookkeeping** is cleanest in instanton normalization; in monopole/$HF$ normalization the reducible tower spans gradings and the parity guard (3c) must be checked case-by-case. I lean primarily on the *isolated-nondegenerate* guard (3a–3b), which is normalization-independent.
- **The kernel migrates, precisely.** The argument *fails* exactly when critical points are **non-isolated or degenerate** — i.e. when there are **moduli** of solutions (positive $b_1$, Morse–Bott critical manifolds). Then Witten–Morse needs the Morse–Bott/family version, positivity can fail on the moduli directions, and cancellation is genuinely possible. So the open frontier is now sharply named: **degenerate / positive-$b_1$ / moduli cases** (e.g. $\Sigma_g\times S^1$, the multi-sector case).

## 6. Verdict and status

- **Proved (modulo standard local analysis):** the no-cancellation lemma — hence the full OS protected-sector correspondence — for **all Brieskorn homology spheres**, the first family *with irreducibles*. This is a genuine second result beyond PSC, and it covers infinitely many manifolds.
- **Kernel migrated to:** degenerate/moduli (higher-$b_1$) critical sets. The hardness is no longer "is there any cancellation ever" (answered: not for isolated nondegenerate) but "control the moduli directions."
- **Honest scope unchanged:** still the protected sector of the abelian SW QFT on $\mathbb{R}\times\Sigma$; still Plank II ∩ Plank III; still no exotic 4D content (Phase 7 divide).

## 7. Next
1. **The moduli case, $\Sigma_g\times S^1$.** $b_1>0$, Morse–Bott critical manifolds, *and* $H^2\neq0$ (several sectors) — tests the lemma where it can genuinely fail and is also the first multi-sector check. The decisive next target.
2. **Self-contained local analysis.** Supply the localization-to-Gaussian and nondegenerate Witten–Morse steps rigorously for the abelian SW theory, removing "modulo standard analysis" for the Brieskorn family.

---

## Sources
- Brieskorn homology spheres: nondegenerate isolated critical set; instanton Floer homology vanishes in odd degree (grading concentration): [Fintushel–Stern / "Floer Homology of Brieskorn Homology Spheres" (arXiv:math/9701211)](https://arxiv.org/pdf/math/9701211); [Floer homology — Wikipedia](https://en.wikipedia.org/wiki/Floer_homology).
- Witten–Morse: SUSY ground states = Morse complex for nondegenerate Morse functions; instantons = differential: Witten, "Supersymmetry and Morse theory" (1982); [supersymmetric quantum mechanics — nLab](https://ncatlab.org/nlab/show/supersymmetric+quantum+mechanics).
- $\Sigma(2,3,7)$ Floer data ($HM_{red}$ rank 1; no PSC): [Heegaard Floer of Brieskorn spheres (arXiv:math/0312071)](https://arxiv.org/pdf/math/0312071); Phase 10.
- Free-field OS positivity (per-critical-point Gaussian): [Jaffe, "Reflection Positivity" (arXiv:1802.09037)](https://arxiv.org/pdf/1802.09037).
