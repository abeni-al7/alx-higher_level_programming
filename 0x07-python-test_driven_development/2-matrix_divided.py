#!/usr/bin/python3
"""
A module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix"""

    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
            )
        for j in matrix[i]:
            if not isinstance(j, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats'
                )
        if i == 0:
            continue
        if len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            new_row.append(round(j / div, 2))
        new_matrix.append(new_row)
    return new_matrix
