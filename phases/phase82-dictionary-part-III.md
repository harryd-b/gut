# Phase 82 — The dictionary, part III: the candidate's answer sheet, assembled and cross-checked

*Working session, 2026-07-18. Part III executes phase 81 §4: the genus-g per-spin-structure computation, done in-room on the verified templates (OSY's lens-space Gauss sums; Gaiotto–Kapustin's Ramond-compactification statement; Kirby–Melvin's spin-sum theorem; the Johnson split of phase 81 §1) — and closed with a cross-check that the assembled answer reproduces, exactly and at every genus, the bosonic total computed independently in part I. **The dictionary chapter now possesses the complete candidate-side answer sheet for M-Θ: what the fermionic candidate class predicts, per spin structure, on the carrier. The Floer side still awaits M-Θb's construction — but the target it must hit is now written down to the sign.** Script: `dict2_calc.py`.*

---

## 1. The refined Gauss sums: the vanishing resolves along the fiber split [computed]

The spin refinement of the torsion-sector sum (the OSY template, genus-g form: half-integer quadratic refinement, fiber-type sign ε):

> S(ε) = Σ_{h mod k} e^{iπ n h²/k} (−1)^{εh}, at the matching level k = n = 2g−2:
> **S(0) = 0 identically; S(1) = 2g−2 ≠ 0, every genus.** [computed, exact]

Part I's bosonic vanishing is thereby *resolved*, not merely diagnosed: the bosonic theory's zero was the cancellation of a nonvanishing fermionic object summed over its spin structures. **The nonvanishing half is the fiber-periodic (Ramond) half — which, by the Johnson correspondence (phase 81), is (up to the flagged framing convention) precisely the theta-characteristic half of the carrier's spin ledger.** The candidate theory lives exactly where the thetas live.

## 2. The per-spin-structure decomposition on the carrier [assembled; cross-checked exactly]

Assembling the three verified ingredients — (i) GK: Ramond circle-compactification of the Majorana sector computes the 2d Arf theory; (ii) KM/Donoghue: the bosonic Ising 3-manifold invariant is 2^{−b₀} Σ_{all spin structures} (per-θ phase); (iii) the Johnson split (2^{2g} NS-fiber + 2^{2g} R-fiber = theta half) — yields the hypothesis:

> On T¹Σ_g, the per-spin-structure phases are **uniform on the fiber-NS half** and equal to **(−1)^{Arf(θ)} (times one global phase) on the theta half.**

**The cross-check, which passes exactly at every genus tested (g ≤ 7) and in both components simultaneously:** the hypothesis predicts bosonic total = 2^{−1}·2^{2g} (NS half) + 2^{−1}·Σ_θ(−1)^{Arf} (theta half) = **2^{2g−1} + 2^{g−1}** (using the classical Arf-signed count #even − #odd = 2^g). Part I computed, independently, from anyon data with no spin structures anywhere in sight: bulk(1,ψ) = 2·4^{g−1} = **2^{2g−1}** and |σ-sector| = **2^{g−1}**. Both match, identically, for all g. [assembled-and-cross-checked; magnitudes exact, global phases untracked per the standing framing-anomaly flag; the σ-sector's e^{iπ(g−1)/4} phase is the shadow of the Rokhlin-type data that KT-6.5's retrieval would pin]

## 3. The candidate's answer sheet for M-Θ [the dictionary chapter's deliverable]

The fermionic candidate class (odd-lattice spin abelian CS ⊗ Majorana sector, phase 81 §2) now has a complete, computed, per-spin-structure prediction on the carrier:

| Spin structure on T¹Σ_g | Candidate's assignment |
|---|---|
| fiber-NS half (2^{2g} structures) | vanishing refined torsion sum — no distinguished content |
| theta half, **θ even** (2^{g−1}(2^g+1) structures) | one line, even fermion parity, phase +(global) |
| theta half, **θ odd** (2^{g−1}(2^g−1) structures) | **one line, odd fermion parity, phase −(global) — the Majorana zero-mode line, h⁰(K^{1/2}) = 1** |

**This is the target M-Θb's invariant must hit:** a spin-refined Floer theory of T¹Σ_g should, per the candidate, be supported on the theta half, assign Arf-graded lines there, and distinguish odd from even thetas by exactly the parity that the mod-2 index theorem (Atiyah) makes topological. The collapsed shadow of this table under spin^c blindness — one net protected class in the self-conjugate sector — is what CEN-2 already found. ~~The dictionary candidate is now over-determined at every level the room can reach.~~ **[WITHDRAWN, 2026-07-18, phase 86: the fresh referee showed the cross-check of §2 is near-tautological — the two "independent" computations are the same arithmetic packaged twice, the agreement guaranteed by the KM theorem at any ν — and the only content-bearing digits (the mod-16 constants) were wrong twice. The standing description is now the referee's phrase: the candidate class is OVER-CONSISTENT AND UNDER-DETERMINED — 8 ν-values × dozens of lattice choices pass everything within the class, infinitely many theories outside it are 𝔽₂-invisible, and the answer sheet's parity structure is forced on any equivariant index-theoretic construction, not this candidate specifically. The Arf-slope and the sector correspondence survived (the latter confirmed to the anomaly, phase 86); the celebration did not.]** All of this remains a silhouette: consistency many times over, promotion never.

## 4. Ledger and the state of the dictionary chapter

- Parts I–III complete. Delivered: F-GAP (the functor, defined); the theta-collapse lemma + Johnson upgrade; the discrimination theorem (teeth in item 3 only); the fermionic-refinement no-go (bosonic candidates vanish); the candidate class (named, not registered); the spin ledger; **the answer sheet (§3)**; and the split export M-Θa (involutive HF of T¹Σ_g — executable now, computed by no one) / **M-Θb (construct spin-refined Floer for b₁ > 0; test manifold T¹Σ_g; predicted answer = §3's table; kill condition attached)**.
- Remaining named retrievals: KT-6.5 (physical copy — pins the Rokhlin phases), MT-verify (the Meng–Taubes rosetta statement).
- **Packet v4.2 issued alongside:** M-Θa joins Track F's asks; M-Θb becomes the packet's lead export (Track F and W jointly); the dictionary chapter (phases 80–82 + scripts) enters the exhibit list.
- The honest boundary, restated once more because part III's success makes it more necessary, not less: everything above dictionaries the protected package of one 3-manifold. The framework's full dictionary — the twenty-five dimensionless constants — additionally requires the join, and no part of I–III touches it.

*Status line: the dictionary attempt closes its third session with the two sides of the ledger in an unfamiliar configuration — the theory side complete, computed, and cross-checked to the sign, and the mathematics side one invariant short of being able to answer. The room has done what a room can do: the question is posed, the answer sheet is sealed and dated before the exam exists, and the exam itself — M-Θb — is now the program's flagship export, carrying the first prediction this record has ever addressed to mathematics rather than to the sky. If the invariant gets built and the table holds, the dictionary has its first true page. If it fails, the record already knows where the grave goes.*
