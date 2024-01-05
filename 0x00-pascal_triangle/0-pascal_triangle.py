#!/usr/bin/env python3
"""
Define a module that has a function returning
Pascal's tiangle.
"""


def pascal_triangle(n):
    """
    Create the Pascal triangle of
    the given number.

    Parameters
    n : integer
        The number of rows in the
        triangle.

    Return
        A list made of a list of integers
        repersenting the Pascal's triangle
        of n.
    """
    triangle = []
    left, right = 1, 1

    if (n <= 0):
        return ([])

    for item in range(0, n):
        triangle.append([1] * (item + 1))

    for row in range(2, n):
        for col in range(1, row):
            left = triangle[row - 1][col - 1]
            right = triangle[row - 1][col]
            triangle[row][col] = left + right

    return (triangle)
