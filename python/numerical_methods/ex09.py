### Newton-Raphson Method

import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x**2 - 2
df = lambda x: 2 * x
root = 1.5

while f(root) / df(root) > 1e-6:
    print(root)
    root = root - f(root) / df(root)

print(f"Root: {root}")

x_vals = np.linspace(0, 2, 100)

plt.plot(x_vals, f(x_vals), label="f(x)")
plt.plot(x_vals, x_vals * df(root) - root**2 - 2, label="tangent")
plt.scatter(root, 0, label="root")
plt.legend()
plt.show()

# def newton_raphson(x0):
#     x = x0
#     for i in range(100):
#         x_new = x - f(x) / df(x)
#         if abs(x_new - x) < 1e-6:
#             return x_new, i
#         x = x_new
#     raise ValueError("Method did not converge")
#
# root, iterations = newton_raphson(1.5)

# y_vals = f(x_vals)
# tangent_slope = df(root)
# tangent_intercept = f(root) - tangent_slope * root
# tangent_y_vals = tangent_slope * x_vals + tangent_intercept
