### Newton-Raphson Method

import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x**2 - 2
df = lambda x: 2 * x
root: float = 1.5

while f(root) / df(root) > 1e-6:
    root -= f(root) / df(root)

print(f"Root: {root}")

x_vals: np.typing.NDArray[np.floating] = np.linspace(0, 2, 100)

plt.plot(x_vals, f(x_vals), label="f(x)")
plt.plot(x_vals, x_vals * df(root) - root**2 - 2, label="tangent")
plt.scatter(root, 0, label="root")
plt.legend()
plt.show()
