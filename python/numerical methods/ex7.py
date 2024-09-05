import numpy as np


def matrix_inversion(matrix):
    try:
        inverse = np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError:
        print("Matrix is singular or ill-conditioned. Inversion is not possible.")
        return None


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
inverse_matrix = matrix_inversion(matrix)
if inverse_matrix is not None:
    print("Inverse matrix:")
    print(inverse_matrix)
