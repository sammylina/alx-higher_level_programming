#!/usr/bin/python3
"""Rectange module

"""


class Rectangle:
    """Rectange that has width and height
       also calcualtes the area and perimeter

    Attr:
        number_of_instances (int): count of instances created from this class
        print_symbol (any): used as symbol for string representation

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectange with positive integer width and height values.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    print(self.print_symbol, end="")
                if h is not self.__height - 1:
                    print()
            return ""

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)

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
