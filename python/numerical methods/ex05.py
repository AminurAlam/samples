import numpy as np


def lagrange_interp(x_data, y_data, x_interp):
    n = len(x_data)
    y_interp = 0

    for i in range(n):
        l_i = 1
        for j in range(n):
            if i != j:
                l_i *= (x_interp - x_data[j]) / (x_data[i] - x_data[j])
        y_interp += y_data[i] * l_i

    return y_interp


def div_diff(x_data, y_data):
    n = len(x_data)
    dd = np.zeros((n, n))
    dd[:, 0] = y_data

    for i in range(1, n):
        for j in range(n - i):
            dd[j, i] = (dd[j + 1, i - 1] - dd[j, i - 1]) / (x_data[j + i] - x_data[j])

    return dd


def newton_interp(x_data, y_data, x_interp):
    n = len(x_data)
    dd = div_diff(x_data, y_data)
    y_interp = dd[0, 0]
    product = 1

    for i in range(1, n):
        product *= x_interp - x_data[i - 1]
        y_interp += product * dd[0, i]

    return y_interp


x_data = np.array([1, 2, 3, 4])
y_data = np.array([1, 4, 9, 16])
x_interp = 2.5
lagrange_result = lagrange_interp(x_data, y_data, x_interp)
newton_result = newton_interp(x_data, y_data, x_interp)
print("Lagrange interpolation result:", lagrange_result)
print("Newton's divided difference interpolation result:", newton_result)
