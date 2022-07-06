#!/usr/bin/python3
"""my_int module
"""


class MyInt(int):
    """This class has an inverted verions of equality
    == means != and viseversa
    """

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        """if they are equal return False"""
        return not self.value == other

    def __ne__(self, other):
        """if the two values are not equal return True"""
        return not self.value != other
