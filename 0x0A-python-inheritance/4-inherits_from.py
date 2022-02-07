#!/usr/bin/python3
"""inhertis from module
"""


def inherits_from(obj, a_class):
    """obj is instance of a class that inhertied from specified
    class(a_class)

    Args:
        obj (object): instance from some class
        a_class (class): base class for the class that obj
            is instantiated from
    Returns: True is if obj is instance of the base class

    """
    return isinstance(obj, a_class) and obj.__class__ != a_class
