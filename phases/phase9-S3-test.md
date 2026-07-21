# Phase 9 — Running the $\Sigma = S^3$ test of the internal conjecture

**Where we are.** Phase 8 proved the *label* level of the monopole-Floer ↔ sector correspondence and conjectured the *internal* level (the graded module $HM(\Sigma,\mathfrak{s})$ = the state content of sector $\mathfrak{s}$, via a dictionary: reducible/$U$-tower = pure-flux vacuum, irreducibles = charged-matter bound states, Frøyshov $h$ = sector ground-state grading). It came with a cheap falsification test: $\Sigma=S^3$. This document runs it.

**Verdict (one line).** The test **passes — as a consistency check and a refinement, not a proof** — and it passes *for the right structural reason*. Both sides give a single sector whose content is a pure tower with **no charged-matter bound states**, and on the $HM$ side the absence of bound states is forced by **positive scalar curvature** (Weitzenböck), which has a clean physical reading. The payoff is a **sharpened dictionary**: the $U$-tower is not vaguely "Coulombic content" but precisely the **representation tower of the residual global $U(1)$** (the total-charge ladder), arising as the equivariant cohomology of the reducible's stabilizer. The honest limit: $S^3$ is too simple to *positively* test the irreducible ↔ bound-state half — that needs a $\Sigma$ with $HM_{red}\neq 0$, which is the decisive next test.

---

## 1. The two sides for $\Sigma = S^3$

### Physics side — Maxwell sectors on $M=\mathbb{R}\times S^3$

- $H^2(S^3;\mathbb{Z}) = 0$ ⟹ **one** magnetic sector (only the trivial $U(1)$ bundle; no flux). Label theorem (Phase 8): a single $\mathrm{Spin}^c$ structure, the trivial one. ✓
- $H^1(S^3;\mathbb{Z}) = 0$ ⟹ no harmonic 1-forms, no flat-connection moduli, no Aharonov–Bohm ($\pi_1=0$) sectors.
- The residual gauge symmetry of this single sector is the group of **constant** gauge transformations, $U(1)$ — i.e. the global charge symmetry. Its representation theory labels states by integer total charge $n\in\mathbb{Z}$. So the *predicted content* of the one sector is a **ladder of total-charge eigenstates** indexed by $n\in\mathbb{Z}$, with a charge-raising/lowering step, and (since there is no nontrivial topology or curvature defect to bind matter) **no localized charged-matter bound states** beyond this global-charge ladder.

### $HM$ side — monopole Floer homology of $S^3$

Computed by Kronheimer–Mrowka with the round metric:
$$
\overline{HM}_*(S^3) \cong \mathbb{F}[U,U^{-1}], \qquad
\widecheck{HM}_*(S^3) \cong \mathbb{F}[U^{-1},U]/\mathbb{F}[U], \qquad
\widehat{HM}_*(S^3) \cong \mathbb{F}[U]\langle -1\rangle .
$$
Key facts:
- There is **exactly one reducible solution** (the trivial connection, zero spinor) and — because the round $S^3$ has **positive scalar curvature** — **no irreducible solutions** (Weitzenböck: $s>0$ forces the spinor to vanish). Hence $HM_{red}(S^3)=0$.
- The entire homology is therefore the **$U$-tower** built on the single reducible. Its origin: the reducible's stabilizer is the constant gauge group $U(1)$, and the tower is its equivariant cohomology
$$
H^*_{U(1)}(\mathrm{pt}) = H^*(BU(1)) = H^*(\mathbb{CP}^\infty) = \mathbb{Z}[U],\qquad \deg U = 2 .
$$
- The **two-sided** $\overline{HM}=\mathbb{F}[U,U^{-1}]$ is indexed by *all* integers; the one-sided $\widehat{HM},\widecheck{HM}$ are its bounded truncations.

---

## 2. The comparison

Lay the two ladders side by side:

| | physics (one Maxwell sector on $\mathbb{R}\times S^3$) | $HM(S^3)$ |
|---|---|---|
| number of sectors | 1 (since $H^2=0$) | 1 $\mathrm{Spin}^c$ structure | 
| internal ladder | total-charge eigenstates $n\in\mathbb{Z}$ under global $U(1)$ | $\overline{HM}=\mathbb{F}[U,U^{-1}]$, indexed by $\mathbb{Z}$ |
| step operator | charge raise/lower | $U$ (degree $\pm 2$) |
| origin of the ladder | residual global $U(1)$ (constant gauge group) | equivariant cohomology of the reducible's $U(1)$ stabilizer |
| charged-matter bound states | none (no topology/defect to bind) | $HM_{red}=0$ (no irreducibles — PSC) |

**Two matches, both nontrivial:**

1. **The tower matches the charge ladder — with the same origin.** Both the $HM$ $U$-tower and the physics charge ladder are the representation tower of the *same* group, the residual global $U(1)$: on the $HM$ side as $H^*_{U(1)}(\mathrm{pt})=\mathbb{Z}[U]$, on the physics side as the total-charge eigenspaces of the vacuum sector. This is *more* than "two $\mathbb{Z}$-indexed towers"; the generators are the same object (the constant-gauge $U(1)$). This refines Phase 8's loose "Coulombic content" into a precise statement.

2. **The absence of bound states matches — for the right reason.** $HM_{red}(S^3)=0$ ⟺ no irreducibles ⟺ (by the dictionary) no charged-matter bound states; and physically the single Maxwell vacuum sector on $S^3$ has no mechanism to bind localized charged matter. Moreover the *reason* on the $HM$ side, **positive scalar curvature forbids irreducible SW solutions** (Weitzenböck), reads cleanly in physics terms: a positively curved compact space provides no potential well to support a normalizable bound charged mode — the curvature term in the coupled Dirac equation is the same Weitzenböck term. The dictionary and the geometry agree on *why* there are no bound states, not just *that* there are none.

**So the test passes.** The internal conjecture's predictions for $S^3$ — one sector, a charge ladder, no bound states, with the no-bound-states condition curvature-controlled — all hold.

---

## 3. What this does and does not establish (the honest accounting)

**Establishes (positive):**
- The dictionary's **vacuum-tower clause is correct and sharpened** on the simplest case: $U$-tower $=$ residual global-$U(1)$ charge ladder $=$ equivariant cohomology of the reducible's stabilizer. This is now a precise identification, not an analogy.
- The dictionary's **bound-state clause is consistent and mechanistically right** in the negative direction: no irreducibles ⟺ no bound states, with positive scalar curvature as the shared cause.

**Does not establish (the limit of $S^3$):**
- $S^3$ has $HM_{red}=0$, so it can only confirm the *absence* of bound states. It **cannot positively test** the core claim "irreducible solutions = charged-matter bound states," because there are no irreducibles to match. The interesting half of the dictionary is untested here.
- The signature gap (Euclidean Floer vs. Lorentzian sectors, Phase 8 obstruction 1) is *not* closed by this test; the match is at the level of graded structures, and the identification "homological degree / 2 ↔ charge" remains a (well-motivated) choice, not a derived equality.

So: a real pass, correctly the *cheap consistency-plus-refinement* outcome promised in Phase 8 — strong enough to keep the conjecture alive and improve it, not strong enough to confirm its substantive half.

---

## 4. The decisive next test (now precisely specified)

To positively test "irreducibles = charged-matter bound states," run the same comparison on a $\Sigma$ with **$HM_{red}\neq 0$** — i.e. a 3-manifold whose round-ish metrics admit irreducible SW solutions (no positive-scalar-curvature metric, or nontrivial Frøyshov data). Cleanest candidates:

- **The Poincaré homology sphere $\Sigma(2,3,5)$** (Brieskorn sphere): still a single $\mathrm{Spin}^c$ ($H^2=0$, so one sector) but with **nontrivial reduced Floer homology / nonzero Frøyshov invariant** $h\neq 0$. This isolates the test: *same trivial label as $S^3$, but now $HM_{red}\neq 0$* — so any extra states are unambiguously the "bound-state" content, and $h$ should appear as the predicted **sector ground-state grading offset**. **This is the ideal next experiment:** it changes exactly one variable (presence of irreducibles) relative to $S^3$.
- **A hyperbolic $\Sigma$** or $\Sigma_g\times S^1$: richer $HM_{red}$ and (for $\Sigma_g\times S^1$) nontrivial $H^2$ giving *multiple* sectors — tests label and internal structure together, but with more moving parts.

**Prediction to check on $\Sigma(2,3,5)$:** one sector (as for $S^3$), but its content $=$ vacuum charge tower **plus** a finite set of bound states counted by $HM_{red}(\Sigma(2,3,5))$, shifted by the Frøyshov grading $h$. A match would be the first *positive* evidence for the substantive (bound-state) half of the dictionary; a mismatch would falsify it.

---

## 5. Verdict and status

The internal conjecture survived its first contact with an explicit calculation and came out **sharper**: the vacuum-tower half is now a precise group-theoretic identification (residual $U(1)$), and the bound-state half is consistent and curvature-explained in the one direction $S^3$ can probe. The conjecture is not confirmed — its substantive half is literally untested by $S^3$ — but it is alive, improved, and faces a clean, single-variable decisive test ($\Sigma(2,3,5)$).

For the program: this is the first time a *conjecture* (not just a structural identity) has been put to an explicit check and passed. Combined with the proved label theorem (Phase 8), the Planks-2∩4 bridge now stands on a proved fragment **and** a positively-tested (if partially) conjecture. Still no Plank 3 (this whole corner is non-exotic by Phase 7). The grand bet's odds are unchanged; its best-supported corner is now genuinely load-bearing.

---

## 6. Methodological note

The right outcome for a first test of a fresh conjecture is rarely "confirmed" or "refuted" — it is "passes the easy case, for a reason you can articulate, and tells you exactly which harder case decides it." That is what happened. The temptation to call the $S^3$ pass a confirmation of the whole dictionary was the trap; the discipline was to notice that $S^3$'s very simplicity ($HM_{red}=0$) makes it blind to the claim that actually matters, and to name the manifold ($\Sigma(2,3,5)$) that isn't. The program continues to convert each result into the next sharply-posed experiment.

---

## Sources
- $HM(S^3)$ explicit ($\overline{HM}=\mathbb{F}[U,U^{-1}]$, $\widehat{HM}=\mathbb{F}[U]\langle-1\rangle$, $\widecheck{HM}=\mathbb{F}[U^{-1},U]/\mathbb{F}[U]$); round metric has positive scalar curvature ⟹ one reducible, no irreducibles; $U$-tower from the reducible: [F. Lin, "Lectures on monopole Floer homology" (arXiv:1605.03140)](https://arxiv.org/pdf/1605.03140); [Manolescu, "Floer theory and its topological applications" (arXiv:1508.00495)](https://arxiv.org/pdf/1508.00495); Kronheimer–Mrowka, *Monopoles and Three-Manifolds* (CUP 2007).
- Positive scalar curvature ⟹ only reducible SW solutions (Weitzenböck/Lichnerowicz), spinor vanishes: [Seiberg–Witten invariants — Wikipedia](https://en.wikipedia.org/wiki/Seiberg%E2%80%93Witten_invariants); [Nicolaescu, "Notes on Seiberg–Witten theory" / lectures (arXiv:alg-geom/9510012 and related)](https://arxiv.org/pdf/alg-geom/9510012).
- Frøyshov invariant $h(Y)$ nonzero for Brieskorn spheres such as $\Sigma(2,3,5)$; reduced Floer homology nontrivial: [Frøyshov / "Monopole Floer homology for rational homology 3-spheres" (arXiv:0809.4842)](https://arxiv.org/pdf/0809.4842).
- Equivariant cohomology $H^*_{U(1)}(\mathrm{pt})=\mathbb{Z}[U]$ as origin of the tower: standard; see the Lin lectures above.
