# Phase 92 — DTAB-1, stage 4b: the acceptance suite passes, the carrier table is doubly confirmed, and one honest unit refuses to balance

*Working session, 2026-07-19 (morning). The bookkeeping pass, done in daylight as promised. The extractor was rebuilt canonically (towers = the tail-minimum envelope; red = the excess; the per-class absolute anchor calibrated against the known red gradings, with constancy of the shift as its own internal check). Script: `dtab4b_calc.py`; full run in the session log.*

---

## 1. What passed

- **The flagship acceptance test (Thm 5.5 at g = 3, through the five-A cone):** red total 18, full graded distribution {2, 12, 2} + {2} matching with a *constant* anchor shift — the strongest fine-grained verification available below threshold, passed exactly. (g = 2 likewise, shift constant, distribution exact.) En route the data itself pinned OS08's internal X-grading convention (the "centered" normalization) — the computation disambiguated the source's convention rather than assuming it.
- **The carrier rows, doubly confirmed in absolute terms:** anchoring the tied-class cones lands the red class at exactly **(4g−9)/4** — the value known independently from the c(i,s) formula — with the displaced volume tower at the same grading (−1/4 at g = 2 with profile 1,4,7,4; 3/4 at g = 3 with 1,6,15,20,16,6). Two fully independent routes to the same absolute row; the program's most important table entry is now as verified as anything it owns.
- **New below-threshold rows produced and anchored:** g = 3 (n = 2 class [0], n = 3 classes [1],[2]) and g = 4 (n = 2 class [0], n = 3 class [1]) — red totals 2, 1, 1, 20, 10 respectively, every distribution matching prediction with constant shift.

## 2. The one unit that would not balance — TIE-1 [registered, open, no claim issued]

At the **below-carrier tied classes** (n even < 2g−2, class [n/2]; first instance g = 3, n = 2, [1]): the cone computes red total **7** against the literal Theorem 5.6 reading's **8** — a one-unit interference at the tie, structurally the same mechanism that displaces the carrier's volume tower. Two hypotheses, deliberately left undecided tonight:

- **(a) Extractor blind spot:** a red death colliding with a tower birth at the same grading is invisible to dims-only extraction — decidable mechanically by tracking the U-module structure (stage 4c, small).
- **(b) A genuine tied-case subtlety in the literal reading of Thm 5.6** — whose displayed formula treats j generically, whose proof addresses the generic retraction, and whose tied case at the *carrier* does match (rank 1 ✓). If (b), this is a literature-grade observation about the theorem's boundary case — exactly the kind of claim this record has learned not to make from a dims table at the end of a long session.

The record notes the discipline explicitly: three days ago this discrepancy would have become a sentence with a flag on it; today it becomes a decision procedure with its outcome unprejudged.

## 3. DTAB-1 status after stage 4b

**Final and anchored:** all classes at n ≥ 2g−2 (the carrier complete, doubly confirmed); all single-A classes at every n; the n = 1 family through the deepest cones; the sampled below-threshold rows of §1. **Open:** TIE-1 (one unit, one decision procedure) and the residual mechanical sweep of remaining below-threshold classes, which runs unattended once TIE-1 fixes the extractor. The paper's content is whole; TIE-1 is either its last checkbox or its most interesting footnote.

*Status line: the table asked for an hour of daylight and used it well — the acceptance suite passed at full grain, the carrier's absolute rows closed from two directions at once, and the day's single anomaly was caught, named, sized at exactly one unit, and handed to a procedure instead of a hunch. Ninety-two phases in, the program can finally say of its central manifold: every number we print about it has either a theorem, a calibration, or an open ticket attached — and there is exactly one ticket.*
