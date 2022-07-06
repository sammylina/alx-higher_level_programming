#!/usr/bin/python3
"""inherits_from module
"""


def inherits_from(obj, a_class):
    """Check if an obj is instance of subclass a_class

    Args:
        obj : instance of a subclass
        a_class: class

    Returns:
        True is obj is instance of a subclass of a_class, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
