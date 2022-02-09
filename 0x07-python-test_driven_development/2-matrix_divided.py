#!/usr/bin/python3
"""matrix divided module
"""


def matrix_divided(matrix, div):
    """divide each elements of matrix by div value

    Args:
        matrix (list): a list of lists
        div (int/float): divisor for the matrix

    Returns:
        list: new matrix with the previous matrix divided by div.

    Raises:
        TypeError: if matrix is not list of lists of numbers/floats
        TypeError: if div is not interger/float
        ZeroDivisionError: if div is 0

    """
    merr_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    rerr_msg = 'Each row of the matrix must have the same size'

    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    else:
        if div == 0:
            raise ZeroDivisionError('division by zero')

    divided_matrix = []
    if type(matrix) != list:
        raise TypeError(merr_msg)
    else:
        for i in range(len(matrix) - 1):
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError(rerr_msg)

        for i, row in enumerate(matrix):
            if type(row) != list:
                raise TypeError(merr_msg)
            else:
                divided_matrix.append([])
                for elem in row:
                    if type(elem) != int and type(elem) != float:
                        raise TypeError(merr_msg)
                    else:
                        ans = round(elem / div, 2)
                        divided_matrix[i].append(ans)

    return divided_matrix
