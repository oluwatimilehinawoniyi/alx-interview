#!/usr/bin/python3

"""
    Rotate a 2D matrix by 90 degrees clockwise.

    Args:
        matrix (List[List[int]]): The 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in-place.
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse rows
    for row in matrix:
        row.reverse()
