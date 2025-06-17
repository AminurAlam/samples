### Lagranges and Newton’s Divided difference Interpolation
import numpy as np

matrix = list[int]


def lagrange(x: matrix, y: matrix, x_int: int | float):
    n = len(x)
    y_int: int | float = 0

    for i in range(n):
        l: float = 1
        for j in range(n):
            if i != j:
                l *= (x_int - x[j]) / (x[i] - x[j])
        y_int += y[i] * l

    return y_int


def newton(x: matrix, y: matrix, x_int: int | float):
    n = len(x)
    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            delta[i, j] = (delta[i + 1, j - 1] - delta[i, j - 1]) / (x[i + j] - x[i])

    term: int | float = 1
    y_int: int | float = delta[0, 0]

    for i in range(1, n):
        term *= x_int - x[i - 1]
        y_int += term * delta[0, i]

    return y_int


x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
x_int: float = 2.5

print(f"lagrange {lagrange(x, y, x_int)}")
print(f"Newton {newton(x, y, x_int)}")
