#!/usr/bin/python3
"""Add module"""


def add_integer(a, b=98):
    """Add two integers and return the sum.

    Args:
        a (int): first argument
        b (int): second argument

    Returns:
        int: sum of a and b.

    Raises:
        TypeError: if a or b is not int
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    elif type(b) != int and type(a) != float:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
