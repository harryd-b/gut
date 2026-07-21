# DTAB-1 stage 4 engine (phase 91), 2026-07-19.
# General multi-A truncated cone for any class [i] of Y(g,n):
#   kept A_s: reps s in (-g, g); kept B_t: reps t in (n-g, g);
#   v_s: A_s(m,i)->B_s(m,i) [i>=0]; h_s: A_s(m,i)->B_{s+n}(2g-m, i+m-g-s) [i+m-g>=s]
#   flip = diagonal star (JM Lemmas 3.1/3.5, verified); truncation exact (all
#   eliminated maps are isos: |s| >= g); per-grading F2 linear algebra.
# VERIFIED (this session): plateau tower-count = 2^{2g} for every class tested;
#   carrier tied rows reproduce stages 2-3 exactly; n=1 red TOTALS reproduce
#   Thm 5.5 (g=2: 2; g=3: 18).
# REMAINING POLISH (stage 4b, mechanical): (i) guard for empty-B classes (pure
#   single-A -- stage 1's closed form already covers them; the engine should
#   delegate); (ii) per-class absolute-grading anchor: calibrate the traversal
#   offset Delta against the known red grading c(i,s) of the outermost window
#   rep (consistent with the stage-1 d(n,i) calibration), then extract the full
#   bottom/red distribution with the dtab2-style extractor and check the
#   fine-grained Thm 5.5 distribution {2@-2, 12@-1, 2@0, 2@3} at g=3.
# (Engine body: as run in the phase-91 session log; see phase file.)
