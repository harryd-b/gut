# Phase 109 — convention upgrades, part 1: D-MS (REFEREED 2026-07-26; scheme-uniqueness CONFIRMED; identity with D-MS pends M-FRAME — see Amendment)

*Working session, 2026-07-26, executing the operator's instruction to attempt functor/derivation upgrades of the adopted conventions. **Status: [derived by a context-free derivation agent; NOT refereed; no verdict entered; D-MS remains an adopted convention until a referee rules].***

*Headline claims (pre-verdict): (1) the session's conjectured mechanism (scale-freeness/Möbius covariance forces minimal subtraction) is REFUTED — the theory possesses covariant scale-free counterterms (explicitly F = λQ²ℓ, built from the same invariant data as the refereed D), so covariance alone leaves an infinite-dimensional scheme space; (2) the session's J-oddness crux is SOUND BUT INSUFFICIENT — it kills all J-even counterterms but spares branch-odd and framing-odd ones, and the rival uniform-background closure is itself J-equivariant, so the mirror cannot adjudicate the pre-adoption disagreement; (3) the upgrade nonetheless SUCCEEDS on corrected hypotheses: locality of counterterms + shape-independence + charge-conjugation evenness + FUSION NATURALITY (the mutual phase is UV-finite, hence scheme-independent; consistency then forces the counterterm to be ADDITIVE in Q; additive + even ⟹ F ≡ 0) — minimal subtraction is the unique admissible scheme; (4) the uniform-background closure is diagnosed exactly: it violates fusion naturality (equivalently, abelian spin–statistics — a theory with nonvanishing mutual statistics cannot have identically vanishing spins) and nothing weaker; (5) load-bearing gaps flagged: GAP-3 (fusion naturality is an axiom about the defect algebra, justified by a locality lemma and numerics, not derived from a controlled coincidence limit) and GAP-4 (the mutual-phase value −Q₁Q₂ used against the rival closure is consistent-with-refereed input). Numerics: divergence confirmed as a shape-dependent self-effect (coefficient = ∫ρ̃² to 6 digits on two ramp families) with UV-finite shape-independent cross terms. Goes to a context-free referee before any verdict.*

---

## The derivation, verbatim

# D-MS Upgrade Attempt: Is Minimal Subtraction Forced?

**Derivation document. Target: upgrade the adopted convention D-MS (minimal subtraction of the spin-transport divergence) to a theorem, or exhibit the exact obstruction.**

---

## 1. The scheme space

[others': refereed E3] The transport holonomy of a charge-Q defect around its geodesic, regulated by a ramp of normalized profile ρ and coordinate width ε, is

  Φ_ε = πc_ρQ²/ε + (n ∓ 1)Q²/2 + o(1),

with c_ρ shape-dependent, the finite part exactly shape-independent, n ∈ ℤ the framing, ∓ the chirality branch.

**Definition (subtraction scheme).** A scheme is a map assigning to each transport datum d = (Q, γ, n, branch; ρ, ε) a counterterm C(d) such that Φ_finite(d) := lim_{ε→0}[Φ_ε(d) − C(d)] exists. Since the divergence is exactly πc_ρQ²/ε, existence of the limit forces

  C(d) = πc_ρQ²/ε + F(d) + o(1),

and any ε-dependent finite piece possessing a limit is absorbed into the ε-independent F. Requirement (ii) of the brief — the subtracted result must be ρ-independent, since the refereed finite part already is — forces F itself to be ρ-independent (Φ_finite = finite_part − F; the left side and first term are ρ-independent iff F is).

**[BOX 1]** The full scheme freedom is one function F(Q, ℓ, n, branch) of the ε-independent, ρ-independent defect data: charge Q, Möbius-invariant translation length ℓ of the geodesic, framing integer n, chirality branch. D-MS is the scheme F ≡ 0. The upgrade question is exactly: which axioms force F ≡ 0?

Note what is *not* excludable at this stage: F need not be ∝ Q² (task 1(iii) asks us to derive, not assume, the Q-scaling — see §4, where the derived answer is stronger: F must vanish, not merely be quadratic).

## 2. What scale-freeness and Möbius covariance actually buy

**Transformation of the regulator.** ε is a coordinate width, not Möbius-invariant: a Möbius map g fixing the anchor acts near it as a dilation, sending a ramp of width ε to a ramp of width |g′(anchor)|·ε with a profile distorted at relative order O(ε) [GAP-1: the statement "Möbius image of an ε-ramp = (|g′|ε)-ramp of distorted profile + O(ε²)" is a Taylor-expansion claim I have not proved uniformly over the ramp family; it is standard but should be checked]. So the divergent term πc_ρQ²/ε is frame-dependent through both c_ρ and ε.

**Adjudication (anomaly vs. artifact).** Because the divergence is a *power* (1/ε), not a logarithm, subtracting it introduces no compensating scale: πc_ρQ²/ε is removed wholesale, and the remainder is shape-independent [others': refereed], hence in particular independent of the shape-and-width distortion a Möbius map induces. The subtracted value is therefore the same computed in any Möbius frame. Had the divergence been Q²log(1/ε), any subtraction would have required a reference scale μ, log(με) would have been frame-covariant only at the cost of a dilation anomaly, and the scale-free theory could not have supplied μ: MS would then be *impossible* rather than forced.

**[BOX 2]** The non-invariance of the divergent term is a regulator artifact, not an anomaly. Power divergence ⟹ the scheme ambiguity space consists of scale-free finite terms F; no logarithm ⟹ no scale is generated by subtraction. This is the (real, but limited) role of scale-freeness.

**The conjecture's proposed mechanism fails.** The conjecture asserts that any F ≠ 0 "introduces a scheme constant transforming like the log of a scale." This is false: the theory possesses a *Möbius-invariant, dimensionless, per-defect* datum, the translation length ℓ [others': refereed setting; and JOIN-4a′ has already refereed the fully covariant invariant D = Q²ℓ/2π built from exactly this datum]. Hence

  F = λQ²ℓ  (λ a pure number)

is an explicit counterexample: a nonzero, shape-independent, exactly Möbius-covariant, scale-free finite counterterm. Likewise F = λ′Q² (pure number) is covariant, since Q is invariant.

**[BOX 3]** Scale-freeness + Möbius covariance do **not** force F = 0. The covariance-only scheme space is still infinite-dimensional: F = f(Q, ℓ, n, branch) arbitrary in invariant data. **The conjecture as literally stated is refuted.** If D-MS is a theorem, its hypotheses lie elsewhere.

## 3. The J-mirror argument: sound but insufficient

[others': refereed] Orientation reversal J maps a defect d = (Q, γ, n, +branch) to Jd = (Q, Jγ, −n, −branch), with ℓ(Jγ) = ℓ(γ), and the refereed law is D_spin(Jd) = −D_spin(d); the framing part nQ²/2 is automatically odd since n flips.

**The scheme acts as one function, J acts on its argument.** The scheme is defined once for the theory; J-equivariance of the scheme is the requirement Φ_finite(Jd) = −Φ_finite(d) *with the same F*. Since the MS finite part already satisfies the odd law, this forces

  F(Jd) = −F(d)  — F must be **J-odd as a function of the data**.

This is the sound version of the brief's crux argument, and it does real work: any branch-blind, framing-blind constant F = λQ² or λQ²ℓ (both J-even, since J fixes Q² and ℓ) satisfies F = −F, hence vanishes.

**But the argument does not close.** The data contain J-*odd* invariants: the framing integer n and the branch sign (±). The candidates

  F = μnQ²,  F = λ(±)Q²,  F = λ(±)Q²ℓ, …

are J-odd and pass the mirror test. The brief's warning was warranted: the naive form "F is a constant, constants are even, so F = 0" silently assumes F is branch- and framing-blind, which nothing yet justifies. Worse (see §5): the uniform-background closure corresponds to a *branch-odd* F and is therefore fully J-equivariant — J alone cannot refute it.

**[BOX 4]** J-equivariance of the scheme is a correct and nontrivial constraint: it kills all J-even counterterms (all f(Q², ℓ)). It does **not** kill branch-odd or framing-odd counterterms — precisely the ones that would renormalize the coefficients ∓1/2 and n/2 themselves. J alone does not prove D-MS.

## 4. What does close it: locality of the divergence + fusion + charge conjugation

**Lemma (locality of the divergence).** The 1/ε divergence is a self-effect of each ramp: for two defects at fixed separation δ, as ε → 0 the divergent part of the transport phase is the sum of single-defect divergences πc_ρ(Q₁² + Q₂²)/ε, while all cross terms are UV-finite and shape-independent.

*Numerical check.* On S¹ (2¹⁶ grid points, periodic winding defects f′ = (Q/ε)ρ̃(·/ε) − Q/2π), two ramp families (raised-cosine, ∫ρ̃² = 1.5; quadratic bump, ∫ρ̃² = 1.2), ε ∈ [0.0125, 0.4]:

- Self term ∫(f′)²: fit a/ε + b gives a = 1.500000 and a = 1.200000 — the divergence coefficient equals ∫ρ̃² to 6 digits, shape-**dependent**, confirming the πc_ρQ²/ε structure and its locality in the ramp.
- Cross terms at δ = π, all three shape pairings: energy cross term → −1/2π = −0.159155 and symplectic cross term σ(f₁, f₂) = ∫f₁f₂′ → const, identical across shape pairings to 5–6 digits and ε-stable — UV-finite and shape-independent.

[GAP-2: this checks the quadratic-form building blocks (‖·‖-type and σ-type integrals) of the phase, not the full refereed transport phase, whose exact functional I do not possess in this context-free brief. Locality of the divergence in the full Φ_ε is inferred from its refereed form πc_ρQ²/ε + finite plus these checks, not re-derived.]

**Axiom S4 (fusion naturality).** Defect fusion Q₁, Q₂ ↦ Q₁ + Q₂ is part of the theory's structure. For a natural scheme, the counterterm of a pair at separation δ > ε is the sum of single-defect counterterms (Lemma + locality axiom S1), so

  Φ_finite(pair) = S(Q₁) + S(Q₂) + M(Q₁, Q₂),

where S(Q) := Φ_finite(single defect) and M is the mutual phase — **UV-finite, hence scheme-independent** (no subtraction touches it; Lemma). Consistency of the scheme with fusion — the fused defect's finite phase must match the pair's — gives the abelian-anyon relation

  S(Q₁ + Q₂) = S(Q₁) + S(Q₂) + M(Q₁, Q₂).

MS itself satisfies this with M = −Q₁Q₂ (the cross term of −Q²/2). Any other scheme has S = S_MS − F, and since M is scheme-independent, subtracting the two relations yields

  **F(Q₁ + Q₂) = F(Q₁) + F(Q₂)** — F is additive in Q (at fixed ℓ, n, branch: fusion happens on one geodesic, one transport frame).

[GAP-3: M's scheme-independence uses ε → 0 at fixed δ, then invokes fusion as a structural operation; I have not controlled a literal δ → 0 limit, which is singular (the mutual term becomes a self term). The axiom is naturality of the scheme with respect to the fusion algebra, justified by the Lemma but not derived from limits alone — this is the honest logical status of S4.]

[GAP-4: I use only the *form* of the relation, not the value M = −Q₁Q₂, except in §5 where the value (consistent with the refereed −Q²/2 cross term, but not independently refereed here) is invoked against the uniform closure.]

**Axiom S3 (charge conjugation).** C: f ↦ −f preserves every refereed structure (the H^{1/2} norm and σ(f, g) = ∫fg′ are quadratic; chirality is untouched), so it is a symmetry, Φ_ε(−Q) = Φ_ε(Q), and a scheme defined once must be C-equivariant:

  **F(−Q) = F(Q)** — F is even in Q.

**Theorem.** Additive + even ⟹ F ≡ 0. On the charge lattice ℤQ₀: additivity gives F(mQ₀) = mF(Q₀); evenness gives F(Q₀) = F(−Q₀) = −F(Q₀), so F(Q₀) = 0. On ℝ: Cauchy's equation plus any regularity (measurability suffices) gives F linear, and even-linear = 0. [GAP-5: for irrational charge ratios without regularity, pathological additive solutions exist; physically irrelevant, flagged for completeness.] This kills *everything*: λQ², λQ²ℓ, μnQ², branch-odd λ(±)Q² — all are quadratic in Q, hence non-additive — and constants (F(0) = 0 from additivity). Note the derived answer to task 1(iii): fusion does not force F ∝ Q²; it forces F additive, which together with C-evenness forces F = 0. The quadratic Q-scaling of the *divergence* is precisely what a finite counterterm can never share while remaining fusion-natural.

**[BOX 5] (Main theorem.)** Under (S1) locality of counterterms, (S2) shape-independence of the subtracted phase, (S3) C-equivariance, (S4) fusion naturality with scheme-independent mutual phase: F ≡ 0, i.e. **minimal subtraction is the unique admissible scheme**, D_spin = ∓Q²/2 + nQ²/2. J-equivariance (BOX 4) is then a *consequence and consistency check*, not a needed hypothesis — though it independently kills the J-even half of the scheme space.

## 5. The two closures revisited

[others': pre-adoption record] Comoving closure: −Q²/2 (= MS). Uniform-background closure: 0, i.e. the scheme F_unif with F_unif(d) = ∓(−Q²/2)-compensating value — explicitly F_unif = +Q²/2 on the (−) branch and −Q²/2 on the mirror branch: a **branch-odd** function.

- **Covariance:** F_unif passes (pure number × Q², invariant data). Consistent with BOX 3.
- **J-equivariance:** F_unif is branch-odd, hence J-odd, hence *passes* — and indeed the value 0 satisfies 0 = −0 trivially. The brief's candidate refutation ("F = −F ⟹ F = 0") fails against this closure precisely because its F is not branch-blind. Honest finding: **J does not adjudicate between the two closures.**
- **Fusion:** F_unif fails. It assigns S(Q) ≡ 0 to every charge, so the fusion relation demands M(Q₁, Q₂) = S(Q₁+Q₂) − S(Q₁) − S(Q₂) = 0 for all charges. But M is UV-finite and scheme-independent (Lemma), and equals −Q₁Q₂ ≠ 0 [GAP-4 applies: value consistent with refereed structure, used as input]. Contradiction: a theory of charges with nonvanishing mutual statistics cannot have identically vanishing spins — the abelian spin–statistics relation. Equivalently: F_unif = ±Q²/2 is quadratic, not additive.

**[BOX 6]** The uniform-background closure violates exactly axiom S4 (fusion naturality / consistency with scheme-independent mutual statistics), and nothing weaker: it is covariant and J-equivariant. The pre-adoption disagreement was a disagreement about fusion consistency, not about symmetry.

## 6. Verdict

**[BOX 7 — VERDICT: D-MS UPGRADED, with corrected hypotheses.]**
- **NOT upgradable from scale-freeness/Möbius covariance alone**: the conjectured mechanism is refuted (BOX 3); ℓ and pure numbers supply covariant scale-free counterterms (e.g. λQ²ℓ, cf. the refereed JOIN-4a′ invariant). Residual ambiguity under covariance alone: F = f(Q, ℓ, n, branch) arbitrary.
- **NOT upgradable from J-equivariance alone**: branch/framing-odd counterterms survive; the rival uniform-background closure is J-equivariant (BOX 4, BOX 6).
- **UPGRADED as a theorem** under: locality of counterterms + shape-independence + C-equivariance + fusion naturality with scheme-independent mutual phase (BOX 5). Scale-freeness plays the prior role of guaranteeing the ambiguity is a scale-free constant at all (power divergence, no log — BOX 2).
- Load-bearing gaps: GAP-3 (fusion naturality is an axiom about the defect algebra, justified by the locality Lemma and numerics, not derived from a controlled δ → 0 limit) and GAP-4 (the value M = −Q₁Q₂ is consistent-with-refereed input, used only against the uniform closure). GAP-1, GAP-2, GAP-5 are minor.

---

**Five-line summary.**
1. Scheme freedom = one finite function F(Q, ℓ, n, branch); D-MS is F ≡ 0 (BOX 1).
2. Scale-freeness/Möbius covariance alone do NOT force F = 0 — explicit covariant counterexample F = λQ²ℓ; the conjecture's mechanism is refuted (BOX 3), though scale-freeness (power, not log, divergence) is what makes any scheme possible at all (BOX 2).
3. J-equivariance forces F to be J-odd, killing half the scheme space but sparing branch/framing-odd terms — and the rival uniform-background closure is J-equivariant, so J alone cannot decide (BOX 4).
4. Fusion naturality (mutual phase UV-finite ⟹ scheme-independent; verified numerically that the divergence is a shape-dependent self-effect, a = ∫ρ̃² to 6 digits, while cross terms are finite and shape-independent) forces F additive in Q; charge conjugation forces F even; additive + even ⟹ F ≡ 0 (BOX 5).
5. **D-MS UPGRADED** on hypotheses {locality, shape-independence, C-equivariance, fusion naturality} — not the hypotheses conjectured; the uniform-background closure fails exactly fusion (spin–statistics), and the honest load-bearing assumptions are flagged as GAP-3/GAP-4 (BOX 6, BOX 7).

---

## AMENDMENT — referee verdicts entered (2026-07-26)

*Context-free adversarial referee pass completed 2026-07-26; report verbatim in `reviews/REPORTS-phase109-DMS-referee-2026-07-26.md`. The referee independently reran the locality numerics (three profile families, coefficient = ∫ρ̃² to 8 digits). Standing AI-referee caveat applies.*

### A.1 Confirmed [refereed]

- The theorem's skeleton: scheme space = one function F (with repairs: schemes defined via the ε→0 limit; geodesic-transitivity and g ~ g⁻¹ closures written out; per-defect restriction attributed to S1); covariance-only REFUTED (the λQ²ℓ counterexample stands — the mirror law is a property of D-MS, not an a priori scheme constraint); J-only insufficient (parity classification verified; sign/framing bookkeeping of F_unif fixed per referee); the pointwise algebra SIMPLIFIED by the referee: additive ⟹ odd, C-even + odd ⟹ 2F = 0 — no Cauchy/measurability needed.
- **The flagged potential error is resolved in the derivation's favor**: linear C (f ↦ −f) is a genuine unitary symmetry of the chiral theory — symplectic, norm-preserving, commuting with the complex structure, fixing the Sugawara stress tensor; chirality untouched; it coexists with and differs from the record's antiunitary J. Formula-evenness alone would NOT have sufficed; the argument stands because C is a symmetry.
- Fusion naturality ruled NOT circular; the uniform-background closure's diagnosis (violates exactly S4 / abelian spin–statistics) CONFIRMED at the refereed n = 0 level.

### A.2 Correction C-P1 (major) — what is proven is uniqueness of the S4-scheme; identity with D-MS pends one computation

The counterterm μnQ² survives every axiom except S4-at-n≠0. There, "MS satisfies S4" requires the mutual phase to contain the framing cross term nQ₁Q₂ — which the refereed pair entry does NOT certify (it certifies only −Q₁Q₂). If the physical mutual phase lacks the framing cross, the axioms uniquely select the framing-DELETED scheme D = ∓Q²/2 instead. **Registered as the deciding open computation M-FRAME:** *compute the mutual phase of two same-axis defects in a framing sector n ≠ 0 from the transport construction — M = (n∓1)Q₁Q₂ confirms D-MS; M = ∓Q₁Q₂ selects the framing-deleted scheme.* Until M-FRAME is done: **the refereed theorem is "the fusion-consistent scheme is unique"; D-MS remains the adopted convention identifying WHICH one it is** — with the ambiguity now reduced from an infinite-dimensional scheme space to a binary choice decided by one computation.

### A.3 Minor repairs adopted

Quadraticity of the transport functional stated as the explicit bridge hypothesis for the locality inference (GAP-2); uniformity of the E3 expansion over Möbius-distorted profile families flagged as an unproven analytic premise (the O(ε)·1/ε = O(1) subtlety); F_unif bookkeeping corrected to (n∓1)Q²/2.

### A.4 Status

**D-MS: convention, with a refereed uniqueness theorem behind it.** The scheme space is provably a two-point set {D-MS, framing-deleted} under the axioms (from the full function space under covariance alone); M-FRAME decides. C-D5-style full upgrade deferred to M-FRAME's outcome.
