# Phase 114 — BIND2-GAP-1-Q: can the orphaned rigidities bound the framing sector n? (structural round, 2026-07-26)

**Status: DRAFTED — structural round, awaiting referee before any verdict enters the BIND-2 registration. The consultation below is preserved VERBATIM per house rules. Nothing has been edited.**

**Editorial header (operator):**
- Executed per the operator-approved BIND2-GAP-1 attack route (phase-112 B2-d addendum). Question: do the three pre-103 surviving rigidities — Milnor–Wood, Bennequin, Godbillon–Vey — bound the boundary dictionary's framing sector n?
- Headline verdicts (UNREFEREED): **Milnor–Wood CANNOT bound n** (caps a fixed carrier datum; the refereed homotopy-invisibility of torsion means the capped quantity never moves; and the bridge maps torsion to charge, not framing — no postulate reopens this route). **Godbillon–Vey CANNOT bound n** (real-valued, metric-attached, defect-blind; reduces to the shelved GV-T non-problem). **Bennequin is the unique live route, at NEEDS-POSTULATE:** candidate convention **C-SL** (transport framing = contact self-linking framing of the transverse carrier knot — NOT adopted) would give n ≤ 2g_s(K_γ) − 1 via tightness, sharp cap n ≤ 1 at minimum genus, consistent with every refereed n-dependent formula — but carries five named gaps (null-homology domain; rational-sl import; unregistered genus data; one-sidedness; representative-dependence) and the standing warning that the record's previous Bennequin deployment was refereed a category error.
- Structural finding worth its own line: **the framing sector n has NO bulk pre-image anywhere in the refereed record** — the bridge maps Giroux torsion to charge; any bulk cap on framing requires a new identification. That is the shape of the whole answer.
- Watch item logged: a strong-fillability reading of the carrier's protection would cap torsion (hence all charge) at ZERO (Gay) — a matter-sector kill, not a stiffness. The record's tightness reading caps nothing. No intermediate exists on that axis.
- Operator decision pending after referee: whether to register C-SL as a candidate convention (C-BRIDGE rank).

---

## CONSULTATION (VERBATIM)

# BIND2-GAP-1-Q: Can the three orphaned rigidities bound the framing sector n? (structural round, 2026-07-26)

**Summary and per-route verdicts.** The three surviving kinematic caps were checked against the boundary dictionary's framing sector n across the refereed bridge. **(ii) Milnor–Wood: CANNOT BOUND n.** MW caps the bundle Euler number, a *fixed* datum of the carrier (which sits at the maximum); the only defect-variable bulk winding integer — Giroux torsion — changes the Euler class by exactly zero (refereed, phase 107 round 2 Box 2), so the MW-capped quantity never moves when any winding integer moves; and under C-BRIDGE torsion maps to *charge*, not framing, so even a torsion cap would bound the wrong integer. **(iii) Bennequin: NEEDS-POSTULATE** — the only live route. If the carrier's transport framing is identified with the contact self-linking framing of the transverse carrier knot (an identification NOWHERE in the record; named below as candidate convention C-SL, *not adopted*), then tightness caps n ≤ 2g_s(K_γ) − 1, giving n ≤ 1 for minimum-genus defects — sharp, one-sided, and consistent with every refereed n-dependent formula; but the route carries two refereed warnings (the record's previous Bennequin deployment was refereed a category error; most carriers are not null-homologous, so the classical bound does not even apply without a rational-sl extension). **(i) Godbillon–Vey: CANNOT BOUND n — route honestly empty.** GV caps a real-valued functional of the metric/foliation (Mitsumatsu formula), saturated at the carrier; it attaches to no defect integer, and the record itself shelved the GV↔twist-budget connection (GV-T) as not yet a posed problem. A fourth cap noticed in passing (strong fillability + Gay's theorem) caps torsion at zero — a kill of the matter sector, not a stiffness — recorded as a watch item.

---

## (a) The objects, precisely

**The three rigidities [others']:**

1. **Milnor–Wood.** For a circle bundle E → Σ_g (g ≥ 2): E admits a flat structure iff |e(E)| ≤ 2g−2 [Milnor 1958 (linear case, bound 2g−2 up to convention); Wood 1971 (topological flat/foliated circle bundles, horizontal foliations iff |e| ≤ 2g−2)]; transverse contact structures iff e ≤ 2g−2 [Giroux, per REMARK-1 §4]; at equality the horizontal structure is rigid — maximal representations are Fuchsian [Goldman 1980s; Matsumoto–Ghys]. **What is bounded: the Euler number e(E) ∈ ℤ of the bundle — a topological datum of the total space, fixed once the carrier is fixed.** The carrier T¹Σ_g has e = ±(2g−2): AT the maximum (ledger item 3; REMARK-1 §§3–4: the last Euler number carrying reduced Floer homology, exactly one class).

2. **Bennequin.** In a tight contact 3-manifold, every *null-homologous* transverse knot K satisfies sl(K) ≤ 2g_s(K) − 1 = −χ(Σ_Seifert); Legendrian version tb + |r| ≤ −χ [Bennequin 1983 (S³); Eliashberg (tight case, via the tight/overtwisted dichotomy); phase 57 C5, with the loose-knot caveat absorbed]. **What is bounded: the self-linking number of each individual knot — a per-knot, per-representative integer, bounded above only** (stabilization lowers sl without bound).

3. **Godbillon–Vey.** For the weak-stable foliation of the geodesic flow of a negatively curved metric g on S: gv(g) = 4π²χ(S) − Def(g), Def(g) ≥ 0, with equality iff constant curvature [Mitsumatsu formula, per Hurder–Katok Publ. IHÉS 72 (1990) Thm 3.11; phase 45 §2; phase 46: "GV stiffness extremal at EQ"]. **What is bounded: a real-valued global functional of the metric/foliation**, saturated by the carrier. It survived phase 103 untouched (ledger item 1) because it is a statement about the fold, not about [R_Γ] orbits.

**The dictionary's framing n [record]:** in E3, D_spin = ∓Q²/2 + nQ²/2 (D-MS), n ∈ ℤ the framing sector of the *boundary transport construction* — refereed origin: per-defect crossing-offset prescriptions of the E3 family; rival refereed realization: global branch-section deck winding, Δa = nQ on the deck lattice Qℤ (M-FRAME; the two readings are exactly the open M-FRAME2 binary). BIND-2 (B2-c) registers *operator's twist count = this n*.

**The three winding-type integers are distinct:**

| Integer | Lives where | Varies with | Capped by |
|---|---|---|---|
| e(bundle) = ±(2g−2) | bulk topology of carrier | nothing (fixed) | MW — and sits AT the cap |
| Giroux torsion k ∈ ℤ₊ | bulk contact data on vertical tori | defect content | nothing in record (C-K1: all k tightness-compatible); ↦ **charge** Q = ±k under C-BRIDGE |
| framing n ∈ ℤ | boundary transport construction | defect content | **nothing — this is BIND2-GAP-1** |

**The structural fact that governs everything below: the refereed bridge maps torsion to charge, not to framing.** C-BRIDGE: one torsion unit over γ ↦ one charge unit at fix(γ), Q = ±n_tor. The framing sector n_fr has **no bulk pre-image anywhere in the refereed record** — the phase-109 bridge-uniqueness tower's n²/2 self-weight pairs torsion with the *lowest weight* q²/2, and its half-integer-framing ambiguity was identified as the bulk twin of what minimal subtraction *removes*. So a bulk cap can reach n_fr only through a *new* identification. That is the shape of the whole answer.

## (b) The Milnor–Wood route: CANNOT BOUND n

Three independent closures, the second already refereed:

1. **The MW-capped quantity is not a defect variable.** MW bounds e(E) of the bundle carrying the flat/foliated structure. The carrier's e = ±(2g−2) is fixed by choosing X = T¹Σ_g; no operation in the record's admissible class (torus torsion insertions, C-K1) changes the total space. The carrier sitting at the cliff protects the *arena's existence* (one more fold is nonexistence — Wood; at the max, Fuchsian rigidity — Goldman, Matsumoto–Ghys): it bounds *which carrier exists*, not *how much winding rides it*.

2. **The refereed round-2 result answers the descent question negatively.** Route (ii) would need torsion insertion to change some MW-capped quantity. It changes none: the relative Euler class of the inserted layer is exactly 0 (rigorous, via the ∂_t section — phase 107 round 2 §2, refereed with the C-M1 weakening: torsion is invisible to plane-field homotopy, so anything factoring through homotopy is n-independent). e(ξ) = e(ξ_can) after any number of insertions. **The MW inequality is therefore saturated before, during, and after arbitrary winding: it has zero slack and zero sensitivity — it cannot cap a quantity it cannot see.** This is the already-refereed fact the brief asked to check; it closes the route.

3. **Even a torsion cap would bound the wrong integer.** Under C-BRIDGE, capping torsion caps the *charge spectrum* — which would contradict sector-surjectivity (N, adopted) and the refereed use of arbitrary Q (pair formulas at Q = 2, the lattice net's full ℤ). It would say nothing about n_fr.

**Verdict (ii): CANNOT BOUND n.** No postulate repairs this: the obstruction is the refereed homotopy-invisibility of the winding datum, not a missing identification.

## (c) The Bennequin route: NEEDS-POSTULATE (the only live route)

**What the record actually contains.** Ledger item 4 ("defects Bennequin-capped, minimum Seifert genus 1") is a *conjecture-level, unregistered session derivation* from phase 57 C5. Its subsequent history is bad: the phase-107 campaign refereed KNOT-Q v1's Bennequin-budget mechanism as a **category error** — "Bennequin constrains sl, never twist admissibility" (Box 3, refereed); Lutz twists along knots are unrestricted at every genus and always overtwist (F1/F2, refereed). The tightness-compatible matter operations are *torus* torsions; knots and their Bennequin budgets were expelled from the charged-defect construction. So "defects are Bennequin-capped" is, as it stands, an orphaned slogan whose one deployment was refuted.

**What survives for re-aim: the carrier knot itself.** Charged defects are anchored on closed geodesics γ; the lift of γ is a closed Reeb orbit K_γ in (T¹Σ_g, ξ_can) — a *transverse knot* (Reeb orbits are positively transverse to ξ). Tightness of the carrier is refereed (C1, fillable ⟹ tight) and retained by torsion insertion (C-K1, Colin). So IF the transport framing n of the carrier's defect were a contact-geometric framing datum of K_γ, Bennequin would bite.

**The needed identification is not in the record.** I searched E3, D-MS, M-FRAME, KNOT-Q v1/v2, C-BRIDGE: n is a boundary-net transport datum (crossing offsets / deck winding); no statement identifies it with sl(K_γ), with a transverse push-off framing, or with any contact framing of any bulk knot. **[GAP-A]** Registrable candidate convention, on the C-BRIDGE pattern:

> **C-SL (candidate, NOT adopted).** The framing sector n of a charged defect anchored on γ equals the self-linking number (equivalently, the contact-framing defect) of a transverse representative of the carrier knot K_γ realizing the defect's transport loop.

**What C-SL would buy.** Tightness [Eliashberg] then gives **n = sl(K_γ) ≤ 2g_s(K_γ) − 1**. With ledger item 4's minimum Seifert genus 1: **n ≤ 1 for the simplest defects — a sharp cap**, and the operator's stiffness would be re-identified with the program's original protective rigidity (Plank IV: "folds only so far" = Bennequin, exactly as phase 57 §3 conjectured at the slogan level).

**What C-SL needs, over-flagged:**
- **[GAP-B] (domain).** Bennequin requires null-homologous knots. H₁(T¹Σ_g) = ℤ^{2g} ⊕ ℤ/(2g−2) [refereed, phase 107 A.1]; K_γ over non-separating γ is *not* null-homologous — and KNOT-Q v2 realizes charge precisely over essential simple geodesics. For separating γ, [K_γ] is at most torsion; the bound needed is the *rational* self-linking bound in tight manifolds [others'; Baker–Etnyre], with 2g_s replaced by a rational Thurston-norm quantity — imported, not checked here.
- **[GAP-C] (the genus).** g_s(K_γ) (or its rational surrogate) for Reeb orbits over simple closed geodesics is not established anywhere in the record; "minimum genus 1" is unregistered. Note also non-simple geodesics' orbits (Ghys: e.g. Lorenz/trefoil-type knots in T¹ of the modular orbifold) were refereed as the *wrong carrier* (trefoil-minimality struck) — genus data must be computed for this carrier, not imported from there.
- **[GAP-D] (one-sidedness).** Bennequin caps sl above only; stabilization makes sl arbitrarily negative. C-SL bounds positive winding only. Whether BIND-2's stiffness needs |n| capped or only the energy-increasing direction capped is not specified in (B2-d); flagged.
- **[GAP-E] (which representative).** sl is representative-dependent; C-SL must name the transverse representative (e.g. the Reeb orbit itself, whose sl is then a computable number per γ — arguably the honest sharpest form: n ≤ sl_max(K_γ), the maximal self-linking of the knot type).

**Consistency of the sharp cap n ≤ 1 against the refereed record:**
- E3/D-MS: D_spin = ∓Q²/2 + nQ²/2 is a formula valid at all n; no refereed entry asserts a physical state with n ≥ 2. No conflict.
- M-FRAME table rows at n = 2 (M = +Q₁Q₂ etc.): these are *scheme-decider evaluations* of the formula, not existence claims; under a cap they become counterfactual calibration rows. No contradiction, but the cap would render the n = 2 discriminating rows physically unrealizable — M-FRAME2's route (b) should then be run at n = 1. Noted.
- Phase-109 bridge tower (2n+1 tori, refereed C-Q2) and e-odd (e = 3 surviving parity): both concern the *torsion* integer and the *bridge normalization* e — different integers (table in §a). A cap on n_fr neither touches nor is touched by them. No conflict; also no support.
- J-mirror (n ↦ −n, refereed): compatible; the cap is one-sided, and J maps a capped-positive sector to an uncapped-negative one — consistent with [GAP-D]'s asymmetry, but worth a referee's eye if C-SL is ever registered.

**Verdict (iii): NEEDS-POSTULATE (C-SL), yielding n ≤ 2g_s(K_γ) − 1 (rational version for most carriers), sharp value n ≤ 1 at minimum genus; testable and consistent with everything refereed; carries GAP-A through GAP-E and the standing warning that the record's previous Bennequin deployment died as a category error.**

## (d) The GV route, a fourth cap noticed, and the verdict block

**GV.** The precise surviving statement is the Mitsumatsu formula [Hurder–Katok Thm 3.11]: gv(g) = 4π²χ(S) − Def(g), Def ≥ 0, zero iff constant curvature — GV is extremal at the carrier's geometry, and this survived phase 103 because it constrains the fold, not the orbit structure. But: GV is real-valued, metric-attached, and *defect-blind* — torsion insertion doesn't move it (the pre-insertion foliation is untouched outside the collar, and post-insertion there is no canonical foliation at all — refereed C-M3), and n_fr lives on the boundary net, which GV never touches. The only conceivable connection is exactly **GV-T** (GV vs twist budget of contact perturbations), which the record itself shelved as **not yet a posed problem** (type mismatch: ℝ vs ℕ; FR-6, phase 57 §5) — and which remains an exported open problem for mathematics, not a registrable convention. **Verdict (i): CANNOT BOUND n; route honestly empty.**

**Watch item (not one of the three, logged in passing).** The record contains one kinematic cap that *does* bite a defect integer: C1 (carrier tight because *exactly fillable*) + C6 (positive Giroux torsion obstructs **strong** filling [Gay], not weak [Ghiggini]). If the carrier's protection were read as strong fillability rather than tightness, torsion — hence, under C-BRIDGE, all charge — is capped at **zero**: a kill of the matter sector, not a stiffness. The record's tightness reading (C-K1) leaves torsion unbounded. Either the protection is tightness (no cap) or fillability (everything dead); no intermediate cap exists on this axis. Filed as a consistency observation for BIND-2's standing-oddity list.

**Verdict block (BIND2-GAP-1-Q):**
- **MW: CANNOT BOUND n** — caps a fixed carrier datum; refereed homotopy-invisibility of torsion (round-2 Box 2/C-M1) shows the capped quantity never moves; torsion maps to charge anyway.
- **Bennequin: NEEDS-POSTULATE (C-SL, named above)** — the unique live route; bound n ≤ 2g_s(K_γ) − 1 (rational-sl version for non-null-homologous carriers), sharp n ≤ 1 at minimum genus; consistent with all refereed n-dependent formulas.
- **GV: CANNOT BOUND n** — real-valued, defect-blind; reduces to the shelved, unposed GV-T.
- BIND2-GAP-1 therefore **remains open as a derivation**, with exactly one registrable closure candidate (C-SL) and its gap list.

## Gaps-and-boxes ledger

- **[BOX i]** MW route closed by refereed facts; no postulate can reopen it (§b).
- **[BOX ii]** The bridge maps torsion → charge; n_fr has no bulk pre-image in the refereed record — any bulk cap on n_fr requires a new identification (§a).
- **[GAP-A]** C-SL identification (transport framing = contact self-linking framing of the transverse carrier representative): candidate convention, not adopted, C-BRIDGE-rank if ever adopted.
- **[GAP-B]** Null-homology domain restriction; rational Bennequin [Baker–Etnyre] import needed for non-separating carriers.
- **[GAP-C]** g_s (or rational genus) of carrier Reeb orbits: not in the record; ledger item 4's "minimum genus 1" is unregistered.
- **[GAP-D]** Bennequin is one-sided; (B2-d) does not specify whether stiffness needs a two-sided cap.
- **[GAP-E]** Representative-dependence of sl; sharpest honest form n ≤ sl_max(K_γ).
- **Watch item:** strong-fillability reading caps torsion at 0 (Gay) — a matter-sector kill, not a stiffness; tightness reading caps nothing.
- **Attributions imported [others']:** Milnor 1958; Wood 1971; Goldman; Matsumoto–Ghys; Giroux (transverse structures at e ≤ 2g−2); Bennequin 1983; Eliashberg (tight/overtwisted dichotomy, tight Bennequin); Baker–Etnyre (rational sl); Gay (torsion vs strong filling); Ghiggini (weak filling); Colin (torsion preserves universal tightness); Hurder–Katok/Mitsumatsu (GV formula); Ghys (modular-carrier knots, already struck from this program's carrier).

---

## Amendment section

(Reserved for the referee verdict. Empty until the referee pass completes.)
