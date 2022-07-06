#!/usr/bin/python3
"""Rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Class represents a rectangle shape

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """calculate are of a rectangle

        Returns:
            area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format('Rectangle',
                                         self.__width,
                                         self.__height)
