#!/usr/bin/python3
"""say_my_name module

"""


def say_my_name(first_name, last_name=""):
    """Print full name by combining first and last name

    Args:
        first_name (str): the first param(required)
        last_name (str): the second param

    Raises:
        TypeError: if first_name or last_name is not string

    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
