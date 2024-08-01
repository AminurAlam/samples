import numpy as np


def fwd_diff(x, y):
    n = len(x)
    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            delta[i, j] = delta[i + 1, j - 1] - delta[i, j - 1]

    return delta


def bwd_diff(x, y):
    n = len(x)
    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j, n):
            delta[i, j] = delta[i, j - 1] - delta[i - 1, j - 1]

    return delta


def newton_fwd(x, y, x_interp):
    n = len(x)
    h = x[1] - x[0]
    p = (x_interp - x[0]) / h
    delta = fwd_diff(x, y)
    term = 1
    result = delta[0, 0]

    for i in range(1, n):
        term *= p / i
        result += term * delta[0, i]

    return result


def newton_bwd(x, y, x_interp):
    n = len(x)
    h = x[1] - x[0]
    p = (x_interp - x[n - 1]) / h
    delta = bwd_diff(x, y)
    term = 1
    result = delta[n - 1, 0]

    for i in range(1, n):
        term *= (p + i - 1) / i
        result += term * delta[n - 1, i]

    return result


# example

x = [0, 1, 2, 3]
y = [1, 2, 5, 10]
x_interp = 1.5

y_interp = newton_fwd(x, y, x_interp)
print(y_interp) # 4.75
