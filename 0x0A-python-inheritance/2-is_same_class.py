#!/usr/bin/python3
"""is_same_class module
"""


def is_same_class(obj, a_class):
    """Check is obj is instance of class a_class
    Args:
        obj (object): instance of a class
        a_class (class): class
    Returns:
        True if obj is instance of class a_class, False otherwise.
    """
    return type(obj) == a_class
