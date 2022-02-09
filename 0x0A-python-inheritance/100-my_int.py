#!/usr/bin/python3
"""MyInt module
"""


class MyInt(int):
    """custom int type class
    """
    def __int__(self, value):
        """initialize with
        Args:
            value (int): integer value
        """
        super().__init__(value)

    def __eq__(self, value):
        """when self and value are equal"""
        return False

    def __ne__(self, value):
        """when self and value are not equal"""
        return True
