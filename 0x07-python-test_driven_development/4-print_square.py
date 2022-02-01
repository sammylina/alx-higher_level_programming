#!/usr/bin/python3
"""Print square module

"""


def print_square(size):
    """Print a square using #.

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not integer
        ValueError: if size of < 0
    """
    if type(size) != int or type(size) == float:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size, end="")
        print()
    if size == 0:
        print("")
