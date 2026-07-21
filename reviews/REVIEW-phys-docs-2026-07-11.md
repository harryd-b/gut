# Review of the `phys` folder
**Scope:** critical technical review + coherence/status check + editorial, with special attention to consistency of the final paper with arXiv:2203.17137 (Berglund–Hübsch–Mattingly–Minic, "Gravitizing the Quantum").
**Documents reviewed:** `CORE-geometry-first-FINAL.md` (= `CORE-final-v2.md`, byte-identical), the earlier CORE draft, `research-map-MASTER.md`, `torsion-U1-subquestion.md`, and phases 3–26. Reviewed by four independent passes (foundations 3–9, bridge 10–17, endgame 18–26, drafts + master map) plus a direct check of the CORE paper against the BHMM essay.
**Date:** 11 July 2026

---

## 0. Overall verdict

The working documents are, on the whole, unusually honest research notes: they refute their own headline claims when the evidence demands it (phases 6, 12, 13, 23), correct their own errors (phase 10's Σ(2,3,5) fix), and grade forced-vs-fitted with real discipline (phases 20, 24, 25). The problems concentrate at the **synthesis layer**: `CORE-geometry-first-FINAL.md` systematically preserves the *conclusions* of the optimistic phases while shedding the *caveats* of the skeptical ones. Each phase-to-phase step is locally honest, but the hedges do not propagate — so the CORE's status tags reflect the most optimistic simultaneous reading of every link in the chain. The paper is not ready to show to the experts named in §6.4 until the items in Part 1 and Part 2 below are fixed; most fixes are wording/tag changes, not new research.

The single most consequential item, given your stated priority: **as currently constructed, the framework does not inherit the experimental predictions of arXiv:2203.17137** — see §1.1.

---

## Part 1 — Consistency with arXiv:2203.17137 ("Gravitizing the Quantum")

### 1.1 The modular ↔ nonlinear identification is a category error (serious)
The essay's mechanism for higher-order interference is a **genuinely nonlinear** state-dependent Hamiltonian, H_ψ = H + gψ, arising from third-quantized topology change — an explicit relaxation of the Born rule; that nonlinearity is the *sole* source of I₃ ≠ 0. Phase 26 (§2, table row 1) and CORE §8B identify this with the modular Hamiltonian K = −log ρ, "itself state-dependent." These are different senses of state-dependence. Tomita–Takesaki modular flow depends on the *reference state/algebra* but generates **exactly linear, unitary, Born-rule-preserving** evolution: standard AQFT — the net, the type III factor, the modular flow, i.e. everything the program has actually built — predicts **I₃ = 0 identically and κ = 0**.

Phase 26 §4 admits this ("Standard modular flow is linear/unitary … unproven"), but phase 26 §3 and CORE §8B still call I₃ ≠ 0 "on-framework" and "**the best experimental handle** (distinctive, non-cosmological, currently testable)." CORE's table caveat ("shared with the whole nonlinear-QG class") understates the problem: it is not that the fingerprint is non-unique, it is that **no mechanism in the framework yet generates any nonzero κ**. Two further gaps: the program contains no *dynamical* topology change (the exotic/GV structure is fixed data, so "topology change as engine" is asserted, not present), and the "next target: predict κ from the GV stiffness" therefore requires a **new nonlinear mechanism**, not a computation inside the existing formalism.

*Fix:* re-grade the §8B row from "RETAINED — the best experimental handle" to something like "CONDITIONAL — inherited only if topology-change-induced nonlinearity is established (currently a conjectured analogy; the constructed framework predicts I₃ = 0)." Rewrite the "our modular = state-dependent evolution" parenthesis.

### 1.2 "Time emergent" is attributed to the essay, but is not in it
Plank I: "This aligns with *gravitizing the quantum* … the dynamical arena is the *quantum* geometry with time emergent." The essay does make quantum geometry dynamical, but it **nowhere claims time is emergent** — it treats time via a gauge-fixed clock variable and the Aharonov–Anandan relation 2ħ ds_FS = ΔE dt. Nothing in the essay concerns modular flow, Tomita–Takesaki, Godbillon–Vey, or foliations; those identifications are entirely this program's. "Aligns with" should be weakened to "is here conjecturally connected to," with the emergent-time gloss owned as yours.

### 1.3 Object mismatch, glossed
BHMM gravitize the geometry **of state space** (the Fubini–Study metric on ℂPⁿ, with a "quantum Einstein equation" G[g^FS] + Λg^FS = G_QG A(ψ)); Plank I makes **spacetime** geometry fundamental. These are different geometries, and the essay's picture is closer to the emergent-geometry side that CORE itself flags as in tension with Plank I in the Faulkner caveat (§2.4/§6.1). One explicit sentence acknowledging this would inoculate the paper.

### 1.4 What *is* consistent (verified directly against the PDF)
- κ numbers: CORE's "κ = 0.006±0.012 (photons), 0.007±0.003 (NMR)" matches the essay's 0.0064±0.0119 (Sinha et al.) and 0.007±0.003 (Park et al.). Rounding is fine. One nuance: these are null-consistent bounds (the NMR central value is ~2.3σ from zero); quote them as bounds, not as "currently measured" grounding.
- Optical-clock α ≲ 10⁻⁵ matches the essay ("bounded to the order of 10⁻⁵").
- JUNO neutrino triple-interference at comparable precision — matches.
- Author attribution (Berglund–Hübsch–Mattingly–Minic) and the Sorkin I₃ framing are correctly credited; CORE does not claim the prediction as its own.
- Genre note: the reference is a 10-page Gravity Research Foundation essay, not a detailed peer-reviewed construction; weight the reliance accordingly.

---

## Part 2 — Critical technical findings (CORE paper, ranked)

### 2.1 §2.1 "[proved here as a corollary of DR + Pontryagin duality]" — the DR machinery does not apply as stated
Doplicher–Roberts reconstruction applies to **DHR-localizable** sectors (transportable endomorphisms localizable in bounded regions, Haag duality, finite statistics). Magnetic/flux sectors are the classic **non-DHR** case: phase 8's own proof step argues superselection precisely *because* c₁ cannot be changed by any local operation — i.e. these sectors fail the DHR criterion (they are Buchholz–Fredenhagen/topological sectors; and Maxwell nets violate Haag duality on topologically nontrivial regions — the very Casini–Huerta–Magán–Pontello mechanism §2.4 cites). What is actually used is Pontryagin duality on a label set that is **input, not derived**. Phase 4 states three honest gaps (category is input; DR gives *a* compact group, not *the* SM group; the net itself is presupposed) — all three are dropped in CORE.

A clean internal reductio: for Σ = S³, H²(S³;ℤ) = 0, so §2.1's formula returns the **trivial group** — yet phase 9's S³ test needs a residual global U(1) on exactly that spacetime. "The gauge group is thus a functional of the geometry" returns the wrong answer on the program's own worked example; the U(1) is presupposed in choosing the bundle theory. Also note DR reconstructs the *global* symmetry group whose irreps label sectors, not the local gauge group.

*Fix:* tag as "[label-level statement; sector category as input; DR-admissibility of topological sectors open — cf. Buchholz–Fredenhagen, Brunetti–Ruzzi–Vasselli]" and restore phase 4's three gaps in §2.1 or §6.

### 2.2 Gauss law vs the U-tower ladder (§5, phase 9)
On a **closed** Cauchy surface Σ the total electric charge must vanish (the flux integral has no boundary) and physical states are singlets under constant gauge transformations. The "ladder of total-charge eigenstates indexed by n ∈ ℤ" that the U-tower is matched to is therefore not a physical state ladder of the theory on compact Σ. The celebrated clause "reducible/U-tower = the global-U(1) charge ladder" identifies HM with states Gauss's law forbids. Never addressed anywhere in the docs; CORE §5 inherits it. This needs either a noncompact/asymptotic-flux reformulation or an explicit resolution.

### 2.3 §5 bridge tag "[proved on the protected sector, PSC ∪ all Brieskorn spheres]" — overstates both halves
- Phase 15 proves the **PSC homology-sphere** case at "the standard of constructive free-field QFT," and says explicitly "**Not claimed:** the full theorem." CORE's bare "PSC" silently widens the class: a PSC manifold with b₁ > 0 (e.g. S²×S¹) has a torus of reducibles — exactly the "migrated kernel" phase 16 §5 names as open.
- Phase 16's Brieskorn result is self-tagged "**modulo standard local analysis**" (the master map keeps this qualifier; CORE drops it), and its no-cancellation guard has real problems: the "grading concentration" input is a **Fintushel–Stern instanton-Floer** fact used to control **monopole** Floer, and in monopole/HF normalization phase 10's own Σ(2,3,7) data (both parities present) violates guard 3(b) on the flagship example. Per-critical-point Gaussian positivity is also not reflection positivity (RP is a global property of the Euclidean measure; instanton cross-terms *are* the Floer differential).
- Phase 11's "OS restricted to the BPS sector" is circular (its RP justification assumes the positive-norm Hilbert space OS is supposed to produce), and phase 15 §2 effectively retracts it ("the positive-definite inner product is **not** available in the twisted theory") — but no doc flags that phase 15 falsifies phase 11's Step 3 rather than refining it.
- "Tested on … all Brieskorn homology spheres" conflates an *argued* lemma with a *test*: only Σ(2,3,5) and Σ(2,3,7) were computed. And phase 9's own verdict on S³ was "passes — as a consistency check …, **not a proof**; it **cannot positively test** the core claim" — CORE renders this as "confirmed."

*Fix:* "[proved for PSC homology spheres at constructive-free-field standard; argued modulo local analysis for Brieskorn spheres; b₁ > 0 open]".

### 2.4 §2.5 keeps an identification that phase 23 refuted, under an [established] tag
Phase 22's boxed claim conflated (i) SW *invariants* of a compact symplectic 4-manifold (Taubes SW = Gr: J-holomorphic curve counts) with (ii) the SW *spectral curve* of an N=2 gauge theory (a family over the Coulomb branch). Phase 23 §3 concedes exactly this ("wrong base … wrong weight") and its Hodge-weight result (weight-1/3 prepotentials vs weight-2 4-manifold periods) is the paper's own Glossary row. Yet CORE's abstract and §2.5 still assert the curve "is at once an integrable system and (by Taubes) the J-holomorphic-curve data of the symplectic 4-geometry **[established]**." Taubes SW=Gr is established; *the identification* is the refuted part. Internally inconsistent with the Glossary.

### 2.5 The Connes/Godbillon–Vey citations are inflated (§4.1, phases 24–25)
The sharp results: GV ≠ 0 implies no holonomy-invariant transverse measure and a nontrivial **type III component** of the foliation von Neumann algebra (Hurder; Hurder–Katok); Connes *relates* GV to the flow of weights. CORE and phase 25 upgrade this to "a type III₁ factor" (subtype and factoriality need extra hypotheses) and "the flow of weights **is determined by** the GV class" (not Connes' statement — and phase 25's one claimed advance, "the which-flow objection is removed," rests on this over-reading). Additionally the flow of weights is an outer invariant on a measure space, not a one-parameter automorphism group of the observable algebra — so even granting the over-reading, it is not yet a candidate Hamiltonian. T1-core is harder than stated, and the foliation W*-algebra is silently identified with the QFT net's algebra (different objects a priori; at least tagged conjecture in §5).

### 2.6 §4.3 "Why 3, not 2+2" is a choice, not a derivation
Godbillon–Vey has codimension-q generalizations (classes in H^{2q+1}); only the *classical* GV ∈ H³ is codim-1. So the argument runs: *if* the stiffness is the classical GV, *then* 3+1 — the split is built into the choice of invariant. State it as such.

### 2.7 §4.4 conflates two finiteness theorems
Cheeger finiteness (curvature + diameter + volume bounds ⇒ finitely many diffeo types) is not the theorem that fails in dimension 4 in the stated way; the n ≥ 5 finiteness of smooth structures on a compact topological manifold is Kirby–Siebenmann. And "4-manifolds admit *uncountably many* exotic structures" holds only for **noncompact** 4-manifolds (ℝ⁴); compact 4-manifolds have at most countably many. "4D folds without a finite limit" is not a theorem as stated. §4.4 has no support in any working doc.

### 2.8 §2.4 entanglement block — three problems
1. "Bell/Tsirelson forbids local fields carrying the *correlations*" is a category error: Bell excludes local *hidden-variable* models; local quantum **fields** (the type III₁ net) are precisely what carries the vacuum correlations — as the same sentence then says. Repeated in the Glossary.
2. The worked example "S²×S¹ ⇒ Ĝ = U(1), universal coefficient −1": for Ĝ = U(1) there are countably many sectors of dimension 1, so the Kitaev–Preskill total quantum dimension D = √(Σd²) **diverges**; γ = log D is not finite without a regularization the text doesn't state. Kitaev–Preskill is also a 2+1D result; its 3+1D transplantation is unjustified in the docs. Phase 21's numbers (γ = 1 + 1/45) do not match the standard Maxwell log-coefficient literature (−16/45 bulk vs −31/45 anomaly, edge-mode difference −1/3: Donnelly–Wall, Casini et al., Soni–Trivedi) — treat as unverified. Phase 17 explicitly deferred this computation.
3. The bulk-term headline ("also geometric — carried by stiffness … [established mechanism + interpretation]") reverses phase 17's split verdict (bulk term geometric only in the *weak* net-determined sense; strong form "**refuted (by theorem)**" per the master map) — and the Susskind–Uglum material has no provenance in any phase doc or the map. The 1/G = GV identification doing the work is conceded as conjecture only in a trailing parenthesis, while the word "stiffness" is used for three distinct things (GV class, 1/G, colloquial rigidity), letting the rhetoric outrun the tagged content.

### 2.9 §2.6 "[proved]" for exotic-smoothness-sources-gravity — least scrutinized, strongest tag
The Brans-conjecture results (Asselmeyer-Maluga compact; Sładkowski exotic ℝ⁴) all come from one school, are contested/not independently verified, and no working doc audits the proofs themselves (phase 24 audits *other* AMK claims and grades them cautiously). A referee will push back on the bare [proved]; suggest "[proved (Asselmeyer-Maluga; Sładkowski) — proofs not independently audited here]".

### 2.10 Smaller technical items
- **Spin^c torsor (§5, phase 8):** Spin^c(Σ) is an H²-*torsor*, not canonically H²; c₁(𝔰+a) = c₁(𝔰) + 2a introduces a factor of 2, and with 2-torsion in H², c₁ does not separate Spin^c structures — bundle labels and Spin^c labels then differ as sets.
- **Duality naming (phases 12/14):** the SW SU(2) monodromy group is Γ(2), not "SL(2,ℤ) duality"; "electric sectors = Pontryagin double-dual" is slogan-level (Gauss-constrained, IR-subtle).
- **Statistics threshold (phase 4 §3):** braided statistics in 2+1D applies to cone-localized charges; double-cone DHR sectors have permutation statistics already in 2+1D — "3+1 is the threshold" is off by the localization class.
- **torsion doc, requirement (3):** "F = dA closed ⇒ global A exists" is false (needs [F] = 0) and, as stated, *excludes the monopole configurations phases 5/8/9 are built on*. A live internal contradiction nobody reconciles.
- **Phase 5 §2:** "∃ monopole ⟺ compact U(1)" — Dirac runs one way; classifying bundles by c₁ already assumes compact U(1), so quantization follows from assumed compactness, not geometry alone (phase 5 §4 half-admits this; CORE drops the caveat).
- **Phase 10 internal inconsistency:** §3 claims Σ(2,3,7) is obstructed from PSC by "h(Y) ≠ 0," but the same doc's table gives d = 0 and §1 states d = −2h, so h = 0; the actual obstruction should run through HM_red ≠ 0. One of the two is wrong as written.
- **Phase 18:** "Hodge positivity ⇒ OS positivity" is a leap (a finite-dimensional inner-product fact vs reflection positivity of a QFT measure); and the stated critical set for Σ_g×S¹ (Jacobian T^{2g}) should be re-checked against Muñoz–Wang (b₁ = 2g+1; vortex/symmetric-product moduli in non-torsion Spin^c).
- **DESI row (§8B):** "3.8–4.2σ" is the top of the DR2 range (with DES-SN5YR/Union3); BAO+CMB alone was ~2.8–3.1σ. Say "up to ~4.2σ depending on data combination." Status as of mid-2026 remains a preference/hint, not a detection.
- **Sourcing:** several load-bearing citations are Wikipedia/Grokipedia (phase 11 OS source; phase 19 special geometry; phases 22–23). The underlying facts are mostly standard, but this is below the standard the program sets itself; swap for primary sources before showing experts.

---

## Part 3 — Coherence and status check

### 3.1 The FINAL contradicts itself on the fundamental ontology (the draft-diff finding)
The only substantive edit from the earlier draft to FINAL (besides adding §8/Appendix) flipped Plank I from "**geometry is fundamental, and 4-dimensional**" to "**fundamentally 3-dimensional, with emergent time**" — but nothing else was updated. The title/subtitle ("how four-dimensional geometry fixes physics"), the abstract ("the geometry of a single four-dimensional manifold"), the §1 one-liner, §4.2's own refinement note ("fundamental **Euclidean 4-geometry** + GV stiffness"), and §7 all still assert 4D-fundamental — now directly contradicting Plank I. It is the first thing a careful reader hits. Also: the 3D flip quietly invalidates phase 3's argument for the CM escape ("keep Poincaré, drop the S-matrix" presumed a fundamental Lorentzian tetrad), yet the phase-3 glossary line is kept unchanged.

### 3.2 The SUSY price is softened to the point of misrepresentation
Phase 19: geometry-first "when made rigorous, is inescapably SUSY-protected"; phase 21: the fully-non-SUSY form is "dead"; phase 23: pure-4D self-sourcing "structurally obstructed"; master map Result Q: the program's "honest form is necessarily SUSY." CORE's thesis line: "with no extra dimensions and **no fundamental supersymmetry**." CORE gets there by relocating the protection to modular/GV (Plank IV — a conjecture phase 24 grades "hypothesis-and-fit-dependent"), but never states the working docs' verdict that every *rigorous* result required SUSY/holomorphy. A reader of CORE alone cannot learn this.

### 3.3 Novelty: CORE §8B contradicts phase 13
CORE: the HM↔DHR label correspondence is "Not found in the literature … the one positive, achievable new result." Phase 13: the label theorem "is a **known fact** in Spin^c/HM clothing. **Nothing to claim there**" (citing hep-th/9708004); phase 20 grades the label half KNOWN/classical and only the join candidate-novel, gated on expert checks that (per the docs) haven't happened. The closing Status line should say "candidate-novel, pending the phase-20 scholarship gate," which is what the program's own audit concluded.

### 3.4 Two different "the handle" claims in one document
§8B calls I₃ ≠ 0 "the best experimental handle"; the closing Status line says "one live falsifiable handle (rigid w = −1)." Beyond the inconsistency, the I₃ handle is conditional on §1.1 above.

### 3.5 The phase-7 no-go vs the §5 "stiffness reading"
Phase 7's theorem (via Bernal–Sánchez): the sector apparatus (globally hyperbolic ℝ×Σ) and exotic smoothness **cannot share a spacetime**; phase 14 Part A: the rigorous corner is "the part where Plank I's exotic 4D content is structurally excluded"; master map Result F: "the bridge can't be built on one spacetime." CORE keeps this as one Glossary row but §5's "Stiffness reading [conjecture]" attaches the exotic-side GV structure to the sector-side Σ without saying how it evades the program's own theorem, and the codim-1 foliation on Σ is new data introduced nowhere in phases 3–9. Phase 13's Reutter no-go (semisimple 4D TQFTs cannot detect exotic smoothness) is silently dropped from CORE.

### 3.6 The master map is stale and internally inconsistent
- **Plank schemes disagree:** map merges to three planks (I/III merged) with 4D-fundamental Plank I and no stiffness plank; FINAL has four planks with "Plank IV" meaning GV stiffness and 3D-fundamental Plank I. "Plank 4" means different things in different eras of the docs; Results A–B use the old numbering.
- **Map's own contradictions:** "## 3. The four planks" heads a three-plank table; §4's open-fronts list forks into two merged numbering eras with mutually contradictory items; three different "current" moments coexist (June 2026 header / "through Phase 21" / index through Phase 25 / "Status after Phase 21 … every open front is now resolved-in-room" sitting above records of phases 22–25).
- **"Indexes everything" is false:** phase 26, the entire experimental-audit round, and the FINAL/v2 CORE files are absent; the map's description of the CORE doc's structure (§5.1, §7–§9) matches no existing version.
- **Caveats the map keeps that FINAL drops:** phase-4's three gaps (Results C/L), "modulo standard local analysis" (Result N), bulk-entanglement "refuted in strong form" (Result O), Result H's "S³ cannot positively test the substantive half."

### 3.7 The pattern to fix globally
Across all four review passes the same gradient appears: hedged working-doc verdicts ("consistency check, not a proof"; "modulo standard local analysis"; "conjecture/interpretation, not derived"; "hypothesis-dependent") acquire harder CORE tags ("confirmed"; "[proved …]"; "aligns with"; "[established]"). The program's self-audits (phases 10, 12, 13, 20, 24) are its best asset — the synthesis should inherit their language, not launder it.

---

## Part 4 — Editorial

1. **Duplicate file:** `CORE-final-v2.md` ≡ `CORE-geometry-first-FINAL.md` (byte-identical). Keep one canonical name; the master map indexes neither.
2. **Phase bookkeeping:** header/abstract say "25 working phases"; Appendix says "companion files `phase1`–`phase25`". The folder has phase3–phase26 (24 files), no phase1/phase2, plus `torsion-U1-subquestion.md` (the map's "Doc 1"). §8B materially depends on phase 26 while the Appendix claims provenance ends at 25. "This round's five audits" heads an 8-row table (and the Appendix repeats "five"). Align all counts and name the actual files.
3. **Status-tag vocabulary broken:** the header declares four tags ([proved] / [established (others')] / [conjecture] / [interpretation]); the text uses at least seven variants ("[established]" never once with "(others')", "[proved here as a corollary …]", "[established mechanism + interpretation]", "[conjecture; mapping established]", "[established + interpretation]", "[central new conjecture]", the long §5 bridge tag). A referee cannot map claims onto the declared scheme; §2.1 mixes [established] and [proved] in one paragraph. Pick the four tags and enforce them.
4. **Redundancy:** §2.4's mechanism half (Jacobson/FGHMV/Casini + holography caveat) is repeated nearly verbatim in §6.1 — cut one. The one-line thesis appears three times (abstract, §1, §7); §7 adds nothing. §3 is a single blockquote that could fold into §1 or §4.
5. **Dangling references:** §2.4 cites "§5.1" — no §5.1 exists (a fossil of an earlier layout the master map still describes); phase 26 cites "§5.2–§5.3 of the core document" — also nonexistent; Plank I says "see §8B" for the BHMM alignment but §8B is the audit table (the exposition is phase 26).
6. **Abstract:** one ~330-word paragraph, heavily bolded, with inline status tags, and it opens on the 4D claim that Plank I now contradicts (§3.1). Two paragraphs, half the bold, ontology consistent.
7. **"Plank" vs "Planck":** if the pun (planks of a platform) is intentional, footnote it at first use; in a physics paper it will otherwise read as a recurring typo — especially with "Planck-scale" appearing nearby and the file `phase17-plankII` in provenance.
8. **§2.5 scope:** "The *entire* low-energy effective action is the holomorphic prepotential [established]" — true for the N=2 SW theory specifically; say so in the sentence, since the paper's thesis is about physics generally.

---

## Part 5 — What holds up well

For balance: the route-elimination Glossary (§8A) is faithful to the record (the wall-crossing/BPS double-kill matches phase 12 exactly; the Bernal–Sánchez row matches phase 7); §2.2's core integrality statement is correct as mathematics; the forward program's item 3 (moduli/b₁ > 0, Σ_g×S¹, constructive OS) is exactly where phases 14–16 left the frontier; the DESI-tension candor and the fitted-vs-forced audit rows (§8B: knots, inflation, Koide, generations) are better than the genre norm; and phases 10, 12, 13, 20, 24, 25 are genuinely good skeptical practice. The κ/α numbers from BHMM are transcribed accurately. The paper's declared ethos — tag everything, credit others, gate novelty on scholarship — is right; the fixes above are mostly about making the tags obey the ethos.

---

## Part 6 — Recommended actions (in order)

1. **Resolve the 3D/4D contradiction** (title, abstract, §1 one-liner, §4.2, §7 vs Plank I) — one ontology, stated once.
2. **Rewrite the BHMM linkage** (§1 Plank I, §8B row, phase 26): analogy not alignment; conditional not inherited; framework-as-built predicts I₃ = 0; "predict κ from GV" requires a new nonlinear mechanism. Decide which of I₃/w = −1 is "the" handle and say it once.
3. **Re-tag the four inflated claims:** §2.1 (DR corollary → label-level, category-as-input), §5 bridge (PSC *homology spheres* + "modulo local analysis" + b₁ > 0 open), §2.5 (drop the curve-identification or move it to [conjecture]; keep Taubes as [established]), §2.6 (attribute, note not independently audited).
4. **Fix the outright errors:** Bell/local-fields sentence (×2), §4.4 finiteness paragraph, S²×S¹ γ example (recompute or cut), Gauss-law/U-tower clause, Σ(2,3,7) h-vs-d inconsistency in phase 10, torsion-doc requirement (3).
5. **Restate weakened claims honestly:** the SUSY-price verdict of phases 19/21/23 belongs in §6, not only implicitly; novelty per phase 13/20 ("candidate, pending scholarship gate"); §4.3 as choice-conditional; Connes/GV at actual theorem strength.
6. **Housekeeping:** delete the duplicate CORE file; fix phase counts/names, "five audits," dangling §5.1/§5.2 refs; unify status-tag vocabulary; deduplicate §2.4/§6.1; footnote "Plank"; upgrade Wikipedia/Grokipedia citations to primary sources.
7. **Update the master map** (or mark it superseded): index phase 26, the audit round, and the FINAL; reconcile the plank schemes; collapse the forked open-fronts list.
8. **Then run the §6.4 scholarship gate** — the expert-contact step is correctly identified as the prerequisite for any novelty claim, and the paper will read far stronger to Faulkner/Casini/Manolescu-adjacent readers with items 1–5 done first.
