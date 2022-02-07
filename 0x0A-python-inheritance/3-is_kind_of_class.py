#!/usr/bin/python3
"""module is_kind_of_class, check class in the inheritance chain
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is inherited from a_class or its base class

    Args:
        obj (obj): object instantiated from some class
        a_class (class): a class definition

    Returns: True if obj is instance of a_class or one of its base

    """
    return isinstance(obj, a_class)
