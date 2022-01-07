#!/usr/bin/python3

"""``0-add_integer`` module
    The ``0-add_integer module provides ``add_integer()`` function

    add_integer(2, 3) returns 5.

"""


def add_integer(a, b=98):
    """Add two numbers and return the sum.

    Args:
        a (int, float): first parameter
        b (int, float): second parameter. Default value 98.

    Returns:
        int: sum of a and b

    Raises:
        TypeError: is type of a and b is not int or float

    """
    if type(a) is float:
        a = int(a)
    elif type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not int:
        raise TypeError('b must be an integer')
    return a + b
