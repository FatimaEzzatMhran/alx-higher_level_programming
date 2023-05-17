#!/usr/bin/python3
"""
This is the "Matrix divided" module.

The matrix divided has one function that take
a list of lists(matrix) and divisor.
All valid elements are divided by the divisor and returned as new matrix.
"""


def matrix_divided(matrix, div):
    """Retrun a new matrix with all values divided by `div`.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (integer/float): The divisor.

    Raises:
        TypeError: If matrix contains elements of non-integers or non-floats.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the division result.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) > 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if isinstance(div, bool):
        raise TypeError("div must be a number")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
