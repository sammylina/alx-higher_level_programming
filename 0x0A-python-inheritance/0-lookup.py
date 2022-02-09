#!/usr/bin/python3
"""lookup module

"""


def lookup(obj):
    """return list of attributes, methods and object in the
    given object name space

    Args:
        obj (object): instance of a class

    """
    return dir(obj)
