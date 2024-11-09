import numpy as np


def population_growth(P, t, r):
    return r * P


def runge_kutta_4th_order(f, t0, P0, h, n, r):
    t = np.zeros(n + 1)
    P = np.zeros(n + 1)
    t[0] = t0
    P[0] = P0
    for i in range(n):
        k1 = h * f(P[i], t[i], r)
        k2 = h * f(P[i] + k1 / 2, t[i] + h / 2, r)
        k3 = h * f(P[i] + k2 / 2, t[i] + h / 2, r)
        k4 = h * f(P[i] + k3, t[i] + h, r)
        P[i + 1] = P[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t[i + 1] = t[i] + h
    return t, P


# Parameters
r = 0.05 # Growth rate
P0 = 1000 # Initial population
t0 = 0
tf = 10
h = 0.1 # Step size

# Number of steps
n = int((tf - t0) / h)

# Solve the equation
t, P = runge_kutta_4th_order(population_growth, t0, P0, h, n, r)

# Print the results
for i in range(n + 1):
    print(f"Time: {t[i]:.2f}, Population: {P[i]:.2f}")
