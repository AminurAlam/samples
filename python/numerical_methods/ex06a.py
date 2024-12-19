### Gauss Elimination Method

import numpy as np


def gauss(A: np.typing.NDArray[np.float64]):
    n: int = len(A)

    for j in range(n - 1):
        for i in range(j + 1, n):
            A[i, :] -= A[i, j] / A[j, j] * A[j, :]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (A[i, -1] - np.dot(A[i, :n], x)) / A[i, i]

    return x


print(f"sol: ", gauss(np.array([[1, 1, 1, 4], [1, 4, 3, 8], [1, 6, 2, 6]], dtype=np.float64)))
