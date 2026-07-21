# Tier 3 — Tackling the four unknowns, and the dark-sector question

*Planning document, 2026-07-17. Successor to TIER-2-KICKOFF (whose go/no-go is executed, phase 38) and the acting-expert sweep (phases 39–42). Honesty rules of the Tier-2 brief carry over verbatim. This plan covers: the attack on each of the four remaining unknowns, and the honest answer to "can the framework eliminate dark matter and dark energy" — with the work that answer requires.*

---

## 0. The strategic picture

The four unknowns are not equal. Unknown 3 (factoriality/III₁) is a *question* — answerable, possibly already answerable from known literature, by the right specialist. Unknown 4 (fold as *the* activator) is an *argument* — writable in-room. Unknowns 1 (the join) and 2 (the one scale) are *research problems* — but each now has a concrete first computation that would move it. The dark sector is not a fifth unknown: it is the framework's cosmological face, and its fate is mostly gated on unknowns 1–2 plus the sky.

## 1. Front A — the join (V.7): make it a theorem-shaped conjecture with a checklist

The join says: the laboratory's observable net is (a subnet of) the foliation algebra. Attack in three steps, easiest first.

**A1 [in-room].** Write V.7 as a precise conjecture with *necessary conditions* that are independently checkable, so it can fail cheaply: (i) the foliation algebra's local subalgebras must be hyperfinite type III₁ factors (the known universal local structure of physical nets — Buchholz–D'Antoni–Fredenhagen); (ii) they must admit the split/nuclearity property; (iii) Haag duality where the net has it, and its known violations (topological sectors) where the net doesn't — note this is a *positive* check: the framework's sector story needs those violations. Each condition is a desk item for an operator algebraist; any failure kills V.7 outright. This converts the bottleneck from an article of faith into a scorable list.

**A2 [in-room, then expert].** Attack the weak direction first (net ⊆ geometric algebra locally), which M1 already uses: exhibit, for a free field on ℝ×Σ, an explicit embedding of the wedge algebras into the foliation algebra's local structure. Even one worked example at free-field level would be the program's first constructive contact between the two sides.

**A3 [expert kernel].** The strong direction (the geometric algebra contains nothing unphysical) is the hard remainder — constructive-QFT territory. Package A1's checklist + A2's example as the ask.

**Kill test:** any A1 condition failing ⟹ V.7 false as stated ⟹ the framework's conditional claims (including the dark-sector reading) lose their route to physics.

## 2. Front B — the one scale: compute η, then confront the tick–fold link

Phase 41 reduced this to one link and one computation. The computation is attackable now:

**B1 [in-room, hard but concrete].** Compute the vacuum entanglement-entropy density η across a wedge horizon for a free field *with the foliation's transverse scale ℓ_tr as the physical cutoff*. The known free-field result diverges as (cutoff)⁻²; the framework's claim is precisely that the fold spacing is not a regulator artifact but a physical scale, giving η = f(GV)/ℓ_tr² with computable f. Getting f's structure — even at heat-kernel/brick-wall level — is the first quantitative content M3 has ever had. Then R2 reads: 4Għ/c³ = ℓ_tr²/f(GV).

**B2 [in-room].** Try to *derive* the tick–fold link (𝒯 = ℓ_tr/c) instead of assuming it: compute the modular-parameter advance per fold crossing from the Connes pairing (the GV-metered flow gives a preferred parametrization — phase 36 Layer 2; the question "how much modular time does one fold cost" is well-posed in it). If the answer is "one tick per crossing," the link is derived and the three scale gaps genuinely collapse to one.

**B3 [consistency, cheap].** Check the skein-ħ face: the deformation parameter of phase 34's quantization map and the ħ of R1 must coincide. A mismatch kills the one-scale claim; do this check before investing further in B1.

**Kill test:** if η comes out with a scale other than ℓ_tr⁻² (B1 contradicting B2), the collapse fails and the framework has three unrelated scale gaps — a major structural retreat, to be reported as such.

## 3. Front C — factoriality and III₁: possibly answerable from the literature

Two moves, in order:

**C1 [in-room / agent-level literature hunt].** The reference class may be wrong. The program fixed on Thurston-type foliations of S³ (chosen for the arbitrary-GV realization), whose ergodicity is unknown. But the *classic* GV ≠ 0 example — the weak-stable foliation of the geodesic flow on a hyperbolic manifold — has intensively studied transverse dynamics, and its von Neumann type may already be known or derivable from known ergodic theory (Connes' own treatment of Anosov foliations; the flow-of-weights machinery). Survey precisely: for which GV ≠ 0 foliation classes are factoriality and the subtype *known*? If a known-III₁ class exists, switch the framework's reference foliation to it — the framework needs *a* fold, not Thurston's specific one.

**C2 [expert].** If C1 finds no settled class, the isolated question from phase 39 goes to a foliation operator-algebraist as-is. It is publishable mathematics either way — a good carrot for the outreach.

## 4. Front D — "the fold is THE activator": write the uniqueness argument

E1 showed time-activation doesn't need the fold (type III with GV = 0 exists). The framework's honest position, writable in-room now: generic type III gives *a* clock but an anonymous one; only GV ≠ 0 makes the clock *geometrically metered* (the Connes pairing — audited verbatim in phase 39) and *canonically parametrized*. So the claim to defend is not "no fold, no time" but "no fold, no geometric clock — no way for geometry to fix dynamics." Write this as a short uniqueness argument [interpretation, honestly tagged], and note its physical bite: frameworks built on GV = 0 type III structures would have emergent time with no geometric handle — unfalsifiable by construction. Ours is falsifiable *because* of the meter. That reframing is the program's best available answer and costs one session.

## 5. The dark sector: what "eliminating dark matter and dark energy" honestly means

The framework's ambition is not to make the observations go away — the observations are real — but to **re-identify both as geometry**: no new particles, no new fields.

**Dark energy = rigidity.** The claim: Λ reflects the Mostow rigidity of hyperbolic 3-geometry — dark energy is what a rigid geometric residue looks like, hence w = −1 *exactly*, with no parameter. Status after phase 42: the *mechanism-level numerics* (AMK's exp(−1/CS) cascade) are retired as fitting; what survives is the structural claim plus its forced signature. So the honest statement is: **the framework requires dark energy to be exactly rigid, cannot currently compute its magnitude, and is under active fire on the rigidity itself** (DESI leans against; Euclid DR1 decides much, late 2026). New in-room task **E-Λ**: assess whether Λ can be tied to the one-scale structure of Front B (the Chishtie bridge already links GV, ℓ_P, ℓ_tr; whether a cosmological length enters through the foliation's *global* data is an open, speculative, but well-posed question — the only route the framework has left to a Λ *magnitude*). Flag: speculative until it produces an equation.

**Dark matter = protected geometry.** The claim (phase 30): the dark sector *is* the reduced monopole Floer sector — gravisolitons, i.e., self-sustaining geometric excitations, gravitationally coupled and nothing else. This yields now-standing predictions: w_DM = 0 exactly at every epoch (P4a, tested and passing); **no non-gravitational detection, ever** (P4d — every LZ/XENONnT null is a pass, any detection is a kill); a per-universe census (homology-sphere universes like S³ are dark-matter-free; Σ(2,3,7) carries one protected class; the phase 40 table now quantifies sector content); and candidate distinctive signatures (P4b lensing polarization — needs its quantitative estimate, task **E-DM1**). What it cannot do yet: compute the *abundance* (why Ω_DM ≈ 5×Ω_b). Task **E-DM2** [exploratory]: check whether the Bradlow-truncated flux budget (finitely many protected sectors per universe) can bound or fix an abundance ratio — the first idea in the record that could even in principle produce Ω_DM.

**So: can we eliminate them?** In principle — that is exactly what the framework is for, and unlike most "geometric dark sector" proposals it pays for the privilege with irreversible commitments (exact w = −1, exact w_DM = 0, eternal direct-detection nulls, GR-exact GW propagation). In practice, today: the *elimination is qualitative* — identities and rigidities, not magnitudes. Both magnitudes route through the same unknowns as everything else (the join gives the framework's states physical standing; the one scale gives it numbers). And one branch is out of our hands: **if Euclid confirms smoothly evolving dark energy, the dark-energy elimination is dead** regardless of theory progress — the pre-registered step-function fallback is the only geometric survival route.

## 6. Order of work and the calendar

1. **B3** (skein-ħ consistency — cheap, could kill the scale program early; do first).
2. **C1** (literature hunt for a known-III₁ GV ≠ 0 class — agent-level, cheap).
3. **A1** (the V.7 checklist — one session, converts the bottleneck to scorable items).
4. **D** (the uniqueness argument — one session).
5. **B2 → B1** (tick–fold derivation attempt, then the η computation — the hard core).
6. **A2** (free-field embedding example).
7. **E-DM1** (P4b estimate), **E-Λ**, **E-DM2** (exploratory).
8. **Expert outreach** (A3, C2, plus phase 39's flagged residues) — now with concrete, small asks.
9. **The sky**: Euclid DR1 (late 2026) adjudicates the dark-energy face; JUNO and LVK O5 keep scoring the nulls.

*Status line: Tier 3 is a convergence plan — every front either feeds the same two hard targets (join, scale) or writes down what the framework can already defend. The dark sector is its cosmological face: elimination-in-principle already on record and falsifiable; elimination-with-magnitudes gated on Fronts A and B; and one branch decided by Euclid within months.*
