### taylor's series method

import math


def taylor_series(x0, n, x):
    approx = math.exp(x0)

    for n in range(1, n + 1):
        approx += (1 / math.factorial(n)) * (x - x0) ** n

    return approx


x0 = 0
n = 5
x = 1

approximation = taylor_series(x0, n, x)
print(f"Taylor Series approximation of e^1: {approximation}")
