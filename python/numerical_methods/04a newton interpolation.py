### Newtons Forward and Backward Interpolation

import numpy as np

matrix = list[int]


def fwd(x: matrix, y: matrix, x_int: int | float) -> int | float:
    n: int = len(x)
    p = (x_int - x[0]) / (x[1] - x[0])
    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            delta[i, j] = delta[i + 1, j - 1] - delta[i, j - 1]

    term: int | float = 1
    result: int | float = delta[0, 0]

    for j in range(1, n):
        term *= p / j
        result += term * delta[0, j]

    return result


def bwd(x: list[int], y: list[int], x_int: int | float) -> int | float:
    n = len(x)
    p = (x_int - x[-1]) / x[1] - x[0]
    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(j, n):
            delta[i, j] = delta[i, j - 1] - delta[i - 1, j - 1]

    term = 1
    result: int | float = delta[-1, 0]

    for j in range(1, n):
        term *= (p + j - 1) / j
        result += term * delta[-1, j]

    return result


x = [0, 1, 2, 3]
y = [1, 2, 5, 10]
print(fwd(x, y, 1.5))  # 4.75
print(bwd(x, y, 1.5))
