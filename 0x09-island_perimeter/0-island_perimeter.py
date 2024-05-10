#!/usr/bin/python3
"""
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]):
        A list of lists of integers representing the grid.

    Returns:
        int: The perimeter of the island
"""


def island_perimeter(grid):
    """
    Function for the island perimeter
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
