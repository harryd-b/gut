# Dictionary part I arithmetic (phase 80), 2026-07-18.
# Circle-bundle partition function from surgery data, ranks-level:
#   Z(Y(g,n)) = sum_a theta_a^n * S_{0a}^{2-2g}
# [derived in-room: Z(Sigma_g x S^1) = Verlinde sum of S_{0a}^{2-2g}; the
#  n-twist surgery on a fiber inserts T^n. Overall framing-anomaly phase
#  e^{2 pi i (...) c/24} NOT tracked — magnitudes and vanishing are robust,
#  phases are not. Flagged accordingly.]

import cmath, math

def Z_circle_bundle(anyons, g, n):
    return sum((th ** n) * (S0 ** (2 - 2 * g)) for th, S0 in anyons)

# (a) Bosonic U(1)_k at the matching level k = n = 2g-2:
#     anyons a in Z/k, theta_a = e^{i pi a^2 / k}, S0a = 1/sqrt(k).
#     Z reduces to k^{g-1} * sum_a e^{i pi a^2} = k^{g-1} * sum_a (-1)^a = 0 (k even).
#     => The matching-level bosonic abelian theory VANISHES identically on the
#        carrier: it is not wrong but undefined-without-spin — the carrier
#        forces the fermionic refinement.
print("Bosonic U(1)_{2g-2} on T^1 Sigma_g:")
for g in range(2, 8):
    k = 2 * g - 2
    anyons = [(cmath.exp(1j * math.pi * a * a / k), 1 / math.sqrt(k)) for a in range(k)]
    print(f"  g={g}: |Z| = {abs(Z_circle_bundle(anyons, g, k)):.2e}  (exact 0 by Gauss-sum parity)")

# (b) Ising TQFT (1, sigma, psi): theta = (1, e^{i pi/8}, -1), S0 = (1/2, 1/sqrt2, 1/2):
#     Z = 2*4^{g-1}  (bulk: 1 and psi, since n = 2g-2 is even)
#       + e^{i pi (2g-2)/8} * 2^{g-1}   (the sigma / spin sector)
print("\nIsing on T^1 Sigma_g: bulk + sigma decomposition:")
for g in range(2, 8):
    n = 2 * g - 2
    anyons = [(1, 0.5), (cmath.exp(1j * math.pi / 8), 1 / math.sqrt(2)), (-1, 0.5)]
    Z = Z_circle_bundle(anyons, g, n)
    print(f"  g={g}: Z = {Z:.4f}; bulk = {2 * 4 ** (g - 1)} = 2^(2g-1); |sigma| = {2 ** (g - 1)} = 2^(g-1)")

# (c) Comparison data (carrier side, phases 75-77): sectors 2g-2;
#     towers Lambda*(F^{2g}) rank 2^{2g} per sector; protected: rank 1 in [g-1].
# (d) Self-conjugate fusion elements of Z/(2g-2): {0, g-1} — matches the
#     carrier's two self-conjugate spin-c classes (tautologically: both are
#     the order-<=2 elements; no evidential weight).
# (e) Theta characteristics on Sigma_g: total 2^{2g}; even 2^{g-1}(2^g+1);
#     odd 2^{g-1}(2^g-1); even - odd = 2^g. Note: the ODD count is EVEN —
#     naive mod-2 sums over thetas cannot give the Floer side's rank 1;
#     the matching must be per-spin-structure (question M-Theta, phase 80 §5).
print("\nTheta characteristics:")
for g in range(2, 6):
    ev, od = 2 ** (g - 1) * (2 ** g + 1), 2 ** (g - 1) * (2 ** g - 1)
    print(f"  g={g}: even {ev}, odd {od}, diff {ev - od} = 2^{g}; odd mod 2 = {od % 2}")
