#!/usr/bin/python3
"""A square module"""


class Square:
    """Square class with only one attribute

    Attributes:
        __size (int): size of the square
        must be >0 and default value 0.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
