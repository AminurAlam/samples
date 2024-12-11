### Runge Kutta Method

step_size = 0.1
rate = 0.05
pop = 1000

for t in range(int(10 / step_size)):
    k1 = step_size * (pop * rate)
    k2 = step_size * (pop + k1 / 2) * rate
    k3 = step_size * (pop + k2 / 2) * rate
    k4 = step_size * (pop + k3) * rate

    pop += (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    print(f"{t/10 + step_size:.1f}: {pop:.2f}")
