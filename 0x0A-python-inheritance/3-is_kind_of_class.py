#!/usr/bin/python3
"""is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is instance of a class or
    instance of a class that inherited from a_class

    Args:
        obj : instance of a class
        a_class : class

    Returns:
        True is obj is instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
