#!/usr/bin/python3
"""Square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square (special type of Rectangle
    """
    def __init__(self, size):
        """initialize size with positive integer"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calcaulate total are of the square"""
        return self.__size * self.__size
