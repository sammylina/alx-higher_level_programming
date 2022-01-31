#!/usr/bin/python3
"""Rectange module

"""


class Rectangle:
    """Rectange that has width and height
       also calcualtes the area and perimeter

    """
    def __init__(self, width=0, height=0):
        """Initialize a rectange with positive integer width and height values.

        """
        self.height = height
        self.width = width
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    print('#', end="")
                print()
            return "\033[F"

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

    def area(self):
        """Return the area of the Rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectange

        Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*self.__width + 2*self.__height
