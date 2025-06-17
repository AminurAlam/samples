### Gauss Elimination Method

import numpy as np

n = int(input("Enter number of unknowns: "))
a = np.zeros((n, n + 1))
x = np.zeros(n)

print("Enter Augmented Matrix Coefficients:")
for i in range(n):
    for j in range(n + 1):
        a[i][j] = float(input(f"a[{i}][{j}]="))

# applying gauss elimination
for i in range(n):
    if a[i][i] == 0.0:
        raise ZeroDivisionError
    for j in range(i + 1, n):
        ratio: float = a[j][i] / a[i][i]
        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# back substitution
x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
for i in range(n - 2, -1, -1):
    x[i] = a[i][n]
    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]
    x[i] = x[i] / a[i][i]

print("\nRequired solution is: ")
for i in range(n):
    print(f"{x[i] = :0.2f}", end="\t")
