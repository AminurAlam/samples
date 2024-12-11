### matrix inversion

import numpy as np

matrix = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)
try:
    inverse_matrix = np.linalg.inv(matrix)
    print(inverse_matrix)
except np.linalg.LinAlgError:
    raise np.linalg.LinAlgError("Matrix is singular or ill-conditioned. Inversion is not possible.")
