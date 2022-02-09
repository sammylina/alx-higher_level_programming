#!/usr/bin/python3
"""custom setattr module"""


def add_attribute(self, key, value):
    """add attriute to self object"""
    if key and value:
        try:
            self.__setattr__(key, value)
        except AttributeError as e:
            raise TypeError("can't add new attribute") from None
