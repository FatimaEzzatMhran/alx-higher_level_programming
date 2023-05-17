#!/usr/bin/python3
"""Contains Pascal's Triangle function."""


def pascal_triangle(n):
    """Pascal triangle function of size n.

    Returns: List of lists of integers representing triangle.
    """

    if n <= 0:
        return ([])

    p_triangle = [[1]]
    while len(p_triangle) != n:
        last_row = p_triangle[-1]
        temp = [1]
        for i in range(len(last_row) - 1):
            temp.append(last_row[i] + last_row[i + 1])
        temp.append(1)
        p_triangle.append(temp)

    return p_triangle
