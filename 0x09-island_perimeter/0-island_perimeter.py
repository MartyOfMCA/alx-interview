#!/usr/bin/python3
"""
Defines a module that creates the island_perimeter
function
"""


def island_perimeter(grid):
    """
    Returns the perimeter of an Island
    from a grid

    Parameters
    grid : list
        A list of integers denoting
        the details of the island

    Return
        The perimeter for the Island
    """
    rows, cols = 0, 0
    perimeter = 0

    if (grid is None or grid == [] or len(grid) == 0 or len(grid[0]) == 0):
        return (0)

    rows = len(grid)
    cols = len(grid[0])
    for row in range(0, rows, 1):
        for col in range(0, cols, 1):
            if (grid[row][col] == 1):
                perimeter += 4
                if (row > 0 and grid[row - 1][col] == 1):
                    perimeter -= 2
                if (col > 0 and grid[row][col - 1] == 1):
                    perimeter -= 2

    return (perimeter)
