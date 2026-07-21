# DTAB-1 stage 2 (phase 89), 2026-07-18.
# Tied classes [k] of Y(g, n=2k): truncated cone A_{-k} (+) A_k --(h,v)--> B_k over F2,
# diagonal-star model (graded ranks invariant under filtered-triangular corrections).
#
# RESULTS:
#  (1) OUTSIDE-WINDOW tied classes (k >= g): tower-bottom profile = exact binomial
#      C(2g,m) at relative grading m-g; palindromic (conjugation-symmetric); no red part.
#      Elimination corrections PROVABLY ABSENT here (the zig-zag isos have vanishing
#      kernels K_s = X(g,g-1-|s|) = 0 for |s| >= g)  =>  these rows are FINAL,
#      closing every stage-1 conjugation failure at n >= 2g. Combined with stage 1:
#      DTAB-1 is COMPLETE for all classes of all Y(g,n) with n >= 2g-1.
#  (2) CARRIER tied class (n = 2g-2, [g-1]): naive-truncation profile =
#      binomial with the single top (Lambda^{2g}) tower bottom LOWERED BY 2
#      (to relative grading g-2), plus the red class, rank 1, at the SAME relative
#      grading g-2 — red rank matches Thm 5.6 exactly. BUT the conjugation
#      diagnostic FAILS here, and correctly so: the elimination corrections are
#      active precisely when K_{±(g-1)} = X(g,0) ≠ 0. The profile is PROVISIONAL;
#      stage 3 = the zig-zag correction terms. The diagnostic has now located the
#      naive method's boundary twice, both times exactly.

from math import comb
from collections import defaultdict

def stage2(g, k, N=60):
    imin_Ak = lambda m: min(0, g + k - m)
    imin_Amk = lambda m: min(0, g - k - m)
    ker = defaultdict(int); cok = defaultdict(int)
    for m in range(2 * g + 1):
        mult = comb(2 * g, m)
        used = set()
        for i in range(0, N + 1):                       # B(m,i)
            srcs = [('Ak', m, i)]                        # v-source always exists (imin<=0)
            ip, mp = i + m - g - k, 2 * g - m
            if ip >= imin_Amk(mp) and (ip + mp - g) >= -k:
                srcs.append(('Amk', mp, ip))             # h-source
            lam = 2 * i + m - g
            if len(srcs) == 2: ker[lam] += mult          # one relation per doubly-hit target
            for s in srcs: used.add(s)
        for i in range(imin_Ak(m), 0):                   # A_k elements killed by v (i<0)
            ker[2 * i + m - g] += mult
        for ip in range(imin_Amk(m), N + 1):             # A_{-k} elements killed by the projection
            if (ip + m - g) < -k:
                ker[2 * ip + m - g + 2 * k] += mult
    return ker, cok

def bottoms(g, k):
    ker, cok = stage2(g, k)
    tot = defaultdict(int)
    for l, v in ker.items(): tot[l] += v
    for l, v in cok.items(): tot[l] += v
    lams = sorted(tot)
    out = {}
    red = {}
    for par in (0, 1):
        chain = [l for l in lams if (l - lams[0]) % 2 == (par - lams[0]) % 2 and l < lams[-1] - 6]
        prev = 0
        for l in chain:
            d = tot[l]
            if d > prev: out[l] = out.get(l, 0) + (d - prev)
            nxt = tot.get(l + 2, d)
            if nxt < d: red[l] = red.get(l, 0) + (d - nxt)   # finite classes dying at l
            prev = tot[l] - red.get(l, 0) + 0 if False else nxt if nxt < d else d
            prev = min(d, nxt)
    return out, red

if __name__ == "__main__":
    for (g, k, label) in [(2, 1, "CARRIER g=2"), (3, 2, "CARRIER g=3"),
                          (2, 2, "outside-window"), (3, 3, "outside-window")]:
        b, r = bottoms(g, k)
        print(f"g={g}, n={2*k}, [k={k}] ({label}): tower bottoms {dict(sorted(b.items()))}, red {dict(r)}")
        binom = {m - g: comb(2 * g, m) for m in range(2 * g + 1)}
        print(f"   binomial reference: {binom}")
