#!/usr/bin/python3
"""function that divides a matrix by a given number"""


def matrix_divided(matrix, div):
    """Creating the function by defining and naming it matrix_divided"""

    new_matrix = []
    for row in matrix:
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        elif not isinstance(div, int) or isinstance(div, float):
            raise TypeError('div must be a number')
        elif not isinstance(matrix, list) or matrix == [] or not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        else:
            new_list = []
            for n in row:
                if not isinstance(n, int) or isinstance(n, float):
                    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
                new_list.append(round(n / div, 2))
            new_matrix.append(new_list)
    return new_matrix

