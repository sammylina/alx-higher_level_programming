#!/usr/bin/python3
"""Rectange module

"""


class Rectangle:
    """Rectange that has width and height

    """
    def __init__(self, width=0, height=0):
        """Initialize a rectange with positive integer width and height values.

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        else:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
