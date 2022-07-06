#!/usr/bin/python3
"""Square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class with its own area method

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate the area of a square"""
        return self.__size * self.__size
