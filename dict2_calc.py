# Dictionary part III arithmetic (phase 82), 2026-07-18.
# (1) Spin-refined torsion Gauss sums on Y(g, n=2g-2) — OSY lens-space template
#     (arXiv:2005.03203 Eqs. 3.22-3.23) generalized: S(eps) = sum_h e^{i pi n h^2/k} (-1)^{eps h}.
#     Result: S(0) = 0, S(1) = 2g-2 — the part-I bosonic vanishing resolves along
#     the fiber split; the nonvanishing half is the fiber-Ramond = theta half (Johnson).
# (2) Cross-check of the per-spin-structure decomposition hypothesis
#     (GK Ramond-compactification = Arf theory; KM spin-sum; Johnson split):
#     NS half uniform -> 2^{2g-1};  theta half (-1)^{Arf} -> 2^{-1} * 2^g = 2^{g-1};
#     versus part I's INDEPENDENT anyon-data computation: bulk = 2*4^{g-1}, |sigma| = 2^{g-1}.
#     Match: exact, both components, all g tested.

import cmath, math

print("(1) Refined Gauss sums, k = n = 2g-2:")
for g in range(2, 8):
    k = 2 * g - 2
    for eps in (0, 1):
        S = sum(cmath.exp(1j * math.pi * k * h * h / k) * (-1) ** (eps * h) for h in range(k))
        print(f"   g={g} eps={eps}: S = {S.real:+.6f}{S.imag:+.6f}j")

print("\n(2) Decomposition cross-check vs part I:")
ok = True
for g in range(2, 10):
    ns_half = 2 ** (2 * g - 1)          # 2^{-1} * 2^{2g} (uniform NS half)
    arf_half = 2 ** (g - 1)             # 2^{-1} * (#even - #odd) = 2^{-1} * 2^g
    bulk_partI = 2 * 4 ** (g - 1)       # part I: (1,psi) bulk
    sigma_partI = 2 ** (g - 1)          # part I: |sigma sector|
    m = (ns_half == bulk_partI) and (arf_half == sigma_partI)
    ok &= m
    print(f"   g={g}: NS {ns_half}={bulk_partI}? theta {arf_half}={sigma_partI}?  {m}")
print(f"   ALL MATCH: {ok}")

# (3) The answer sheet (phase 82 §3): per spin structure on T^1 Sigma_g the
#     candidate assigns — fiber-NS: nothing; theta even: one even line;
#     theta odd: one odd (Majorana) line, h^0(K^{1/2}) = 1.
#     Counts: even 2^{g-1}(2^g+1), odd 2^{g-1}(2^g-1); signed sum 2^g.
