#!/usr/bin/python3
"""add_attribute module
"""


def add_attribute(obj, key, value):
    """Add attributes to obj

    Args:
        obj (obj): instance of a class
        key (string): key used to refere the value in obj
        value (obj,int): value assigned for key in obj

    Raises:
        TypeError: if it can't add new attribute to the obj
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
