import numpy as np


def gauss_elimination(A: np.ndarray, b: np.ndarray):
    n: int = len(A)
    augmented_matrix: np.ndarray = np.hstack((A, b.reshape(-1, 1)), dtype=np.float64)

    # Forward elimination
    for i in range(n - 1):
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, : n - 1], x)) / augmented_matrix[i, i]

    return x


# Example usage
A: np.ndarray = np.array(
    [
        [2, 1, -1],
        [1, -1, 1],
        [-1, 1, 2],
    ],
)
b: np.ndarray = np.array([1, 2, -1])

x = gauss_elimination(A, b)
print("Solution:", x)
