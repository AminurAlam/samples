### Runge Kutta Method

import numpy as np


def runge_kutta_4th_order(t0, P0, h, n, r):
    t = np.zeros(n + 1)
    P = np.zeros(n + 1)
    t[0] = t0
    P[0] = P0

    for i in range(n):
        k1 = h * (P[i] * r)
        k2 = h * (P[i] + k1 / 2) * r
        k3 = h * (P[i] + k2 / 2) * r
        k4 = h * (P[i] + k3) * r
        P[i + 1] = P[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t[i + 1] = t[i] + h

    return t, P


r = 0.05  # Growth rate
P0 = 1000  # Initial population
t0 = 0
tf = 10
h = 0.1  # Step size
n = int((tf - t0) / h)  # Number of steps
t, P = runge_kutta_4th_order(t0, P0, h, n, r)  # Solve the equation

for i in range(n + 1):
    print(f"Time: {t[i]:.2f}, Population: {P[i]:.2f}")
