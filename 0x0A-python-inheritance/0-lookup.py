#!/usr/bin/python3
"""Python module
"""


def lookup(obj):
    """object lookup function

        Args:
            obj (object): a python object

        Returns:
            list: a list that contains all attributes and method that the
            object has
    """

    return dir(obj)
