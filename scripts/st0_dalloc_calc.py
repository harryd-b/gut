# ST-0 + D-alloc arithmetic (phase 71), 2026-07-18.
# All formulas source-verified before running (Seiberg-Shih hep-th/0312170 §5.1;
# Rasmussen hep-th/0405257 §3.2; counts derived from confirmed Kac data and
# spot-checked on TIM = SM(3,5)). Existence: p'-p even AND gcd((p'-p)/2, p) = 1.
# Counts (superprimaries under (r,s)~(p-r,p'-s)):
#   both odd:  total (p-1)(p'-1)/2, NS = (p-1)(p'-1)/4
#   both even: total ((p-1)(p'-1)+1)/2, NS = [(p/2)(p'/2)+(p/2-1)(p'/2-1)]/2
# Unitary N=1 series: (m, m+2), m >= 3; first member SM(3,5) = tricritical Ising.

from math import gcd

def super_ok(p, pp):
    d = pp - p
    return d > 0 and d % 2 == 0 and gcd(d // 2, p) == 1

def sm_total(p, pp):
    if p % 2 == 1 and pp % 2 == 1: return (p - 1) * (pp - 1) // 2
    if p % 2 == 0 and pp % 2 == 0: return ((p - 1) * (pp - 1) + 1) // 2
    return None  # mixed parity excluded by existence

def sm_NS(p, pp):
    if p % 2 == 1 and pp % 2 == 1: return (p - 1) * (pp - 1) // 4
    if p % 2 == 0 and pp % 2 == 0:
        return ((p // 2) * (pp // 2) + (p // 2 - 1) * (pp // 2 - 1)) // 2
    return None

# --- ST-0: super scaffold, census count 2g-1 vs superprimary counts ---
print("ST-0 SUPER scaffold: census count = 2g-1 vs superprimary counts")
for g in range(2, 9):
    tgt = 2 * g - 1
    tot_sols, ns_sols = [], []
    for p in range(2, 60):
        for pp in range(p + 2, 120):
            if not super_ok(p, pp): continue
            if sm_total(p, pp) == tgt: tot_sols.append((p, pp, pp == p + 2))
            if sm_NS(p, pp) == tgt: ns_sols.append((p, pp, pp == p + 2))
    f = lambda L: ", ".join(f"({a},{b})" + ("*U*" if u else "") for a, b, u in L) or "NONE"
    print(f"  g={g}: total-alloc: {f(tot_sols)} | NS-alloc: {f(ns_sols)}")

# --- The parity theorem behind the total-allocation emptiness ---
# both odd: (p-1)(p'-1) = even*even == 0 mod 4  =>  total even.
# both even: p=2a, p'=2b; total = 2ab - a - b + 1; existence forces b-a odd
#            => a+b odd => total even.
# 2g-1 is odd. Hence NO solutions, any genus. Check exhaustively:
bad = [(p, pp) for p in range(2, 200) for pp in range(p + 2, 400)
       if super_ok(p, pp) and sm_total(p, pp) % 2 == 1]
print(f"\nParity theorem check (p<200, p'<400): odd totals found = {len(bad)} (expect 0)")

# --- Unitary super series: which genera can match at all? ---
print("\nunitary super series (m,m+2): NS-count matches (NS = (m/2)^2 for even m):")
for m in range(3, 60):
    n = sm_NS(m, m + 2)
    if n and n % 2 == 1:
        print(f"  m={m}: NS={n} -> g={(n + 1) // 2}")

# --- D-alloc (allocation A, BOSONIC): k=0 rank at g=2 is 6 ->
#     degenerate count (p-1)(p'-1)/2 = 6, i.e. (p-1)(p'-1) = 12 ---
print("\nD-alloc (allocation A, bosonic): (p-1)(p'-1) = 12, gcd(p,p')=1:")
for p in range(2, 15):
    for pp in range(p + 1, 30):
        if gcd(p, pp) == 1 and (p - 1) * (pp - 1) == 12:
            u = "  *UNITARY* = tricritical Ising" if pp == p + 1 else ""
            print(f"  ({p},{pp}){u}")

# Anti-numerology note: NS-alloc both-odd at g=2 solves (p-1)(p'-1)=12 too
# (NS = X/4 = 3 vs D-alloc X/2 = 6 -> same X). (3,7) in both menus is
# arithmetic necessity, not convergence.
