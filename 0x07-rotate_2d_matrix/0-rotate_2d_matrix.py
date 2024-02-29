#!/usr/bin/python3
"""
Define a module that implements a funciton
to rotate a matrix by 90 degrees.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given array by 90 degrees.

    Parameters:
        matrix : list
        A list of lists containing
        the original matrix.
    """
    for counter in range(len(matrix)):
        matrix[counter].reverse()

    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], \
                    matrix[row][col]

    for counter in range(len(matrix)):
        matrix[counter].reverse()

    matrix.reverse()
