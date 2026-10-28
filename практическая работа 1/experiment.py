import numpy as np
import matplotlib.pyplot as plt

T = 6
BASE_A = 0.45
BASE_K = 80000.0
BASE_N0 = 3000.0

def simulate(a, K, N0, T=T):
    N = np.zeros(T + 1)
    N[0] = N0
    for t in range(T):
        N[t+1] = N[t] + a*N[t]*(1-N[t]/K)
    return N

def t95(a, K, N0):
    N = simulate(a,K,N0,200)
    target = .95*K
    if N0 < target:
        idx = np.where(N >= target)[0]
        return int(idx[0]) if len(idx) else None
    if N0 == target:
        return 0
    return None

print("Серия 1: a =", [0.15,0.30,0.45,0.60,0.75,0.90,1.20])
for a in [0.15,0.30,0.45,0.60,0.75,0.90,1.20]:
    N=simulate(a,BASE_K,BASE_N0)
    print(f"a={a:.2f}; t95={t95(a,BASE_K,BASE_N0)}; N30={N[-1]:.3f}")

print("\nСерия 2: N0 =", [500,3000,10000,100000])
for N0 in [500,3000,10000,100000]:
    N=simulate(BASE_A,BASE_K,N0)
    print(f"N0={N0}; t95={t95(BASE_A,BASE_K,N0)}; N30={N[-1]:.3f}")

print("\nСерия 3: K =", [60000,80000,120000])
for K in [60000,80000,120000]:
    N=simulate(BASE_A,K,BASE_N0)
    print(f"K={K}; t95={t95(BASE_A,K,BASE_N0)}; N30={N[-1]:.3f}")
