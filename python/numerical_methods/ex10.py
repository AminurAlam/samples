### Runge Kutta Method

step_size = 0.01
rate = 0.05
pop = 1000

for t in range(int(10 / step_size)):
    k1 = step_size * rate * (pop)
    k2 = step_size * rate * (pop + k1 / 2)
    k3 = step_size * rate * (pop + k2 / 2)
    k4 = step_size * rate * (pop + k3)

    pop += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    print(f"{(t+1)*step_size:.1f}: {pop:.2f}")
