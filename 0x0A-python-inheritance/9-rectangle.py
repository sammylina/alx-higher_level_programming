#!/usr/bin/python3
"""Rectangle module, Inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry class and have width and
    height.

    Args:
        width (int): postive integer width of rectangle
        height (int): positive integer height of rectangle
    """
    def __init__(self, width, height):
        """initialize width and height with positive
        integers using super().integer_validator

        Args:
            __width (int): private width value for instance
            __height (int): private height for the instance
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return string that describes the Rectangle class"""
        return "[{:s}] {:d}/{:d}".format("Rectangle", self.__width, self.__height)

    def area(self):
        """calculate are of the rectangle"""
        return self.__width * self.__height
