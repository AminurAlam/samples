import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2 - 2


def df(x):
    return 2 * x


def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    raise ValueError("Method did not converge")


# Initial guess
x0 = 1.5
# Find the root using Newton-Raphson method
root, iterations = newton_raphson(x0)
# Print the result
print("Root:", root)
print("Number of iterations:", iterations)
# Plot the function and the tangent line at the root
x_vals = np.linspace(0, 2, 100)
y_vals = f(x_vals)
tangent_slope = df(root)
tangent_intercept = f(root) - tangent_slope * root
tangent_y_vals = tangent_slope * x_vals + tangent_intercept
plt.plot(x_vals, y_vals, label="f(x)")
plt.plot(x_vals, tangent_y_vals, label="Tangent line at root")
plt.scatter(root, 0, color="red", label="Root")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
