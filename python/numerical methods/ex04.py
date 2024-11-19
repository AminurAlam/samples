### Newtons Forward and Backward Interpolation


import numpy as np


def newton_fwd(x, y, x_interp):
    n = len(x)  # lon
    h = x[1] - x[0]  # step
    p = (x_interp - x[0]) / h
    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            delta[i, j] = delta[i + 1, j - 1] - delta[i, j - 1]

    term = 1
    result = delta[0, 0]

    for j in range(1, n):
        term *= p / j
        result += term * delta[0, j]

    return result


def newton_bwd(x, y, x_interp):
    n = len(x)
    h = x[1] - x[0]
    p = (x_interp - x[n - 1]) / h

    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j, n):
            delta[i, j] = delta[i, j - 1] - delta[i - 1, j - 1]

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
# print(y_interp)  # 4.75


###


def fwd(x, y, x_interp):
    n = len(x)  # lon
    # h = x[1] - x[0] # comman difference
    p = (x_interp - x[0]) / (x[1] - x[0])
    delta = np.zeros((n, n))
    delta[:, 0] = y

    # print(delta)
    for j in range(1, n): # 1..2
        for i in range(n-j): # 0..
            print(i,j)
            delta[i, j] = delta[i + 1, j-1] - delta[i, j-1]

        print(delta)

    term = 1
    result = delta[0, 0]

    for i in range(1,n):
        term *= p / i
        result += term * delta[0, i]

    return result


print(fwd(x, y, x_interp))
