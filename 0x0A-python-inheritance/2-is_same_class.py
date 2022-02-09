#!/usr/bin/python3
"""is_same module, check for object is instance of a class"""


def is_same_class(obj, a_class):
    """Check if obj is instance of class a_class

    Args:
        obj (obj): object to check
        a_class (class): class type we want to check
                if it obj is instantiated from it

    """
    return type(obj) == a_class
