#!/usr/bin/python3
"""rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """This class represents a Rectangle and extended from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantialing Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): default value 0
            y (int): default value 0
            id (int): id of the instance inherited from Base class

        """
        if (id is not None) and (type(id) is not int):
            raise(TypeError)
        elif (id is not None) and (id <= 0):
            raise(ValueError)

        super().__init__(id)

        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def __str__(self):
        sf = "({:d}) {:d}/{:d} - {:d}/{:d}"
        return sf.format(self.id, self.__x, self.__y,
                         self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        """postive integer value"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        """positive integer value"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value
        return self.__height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """calcaulate area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display the rectangle using # """
        for row in range(self.__height):
            for column in range(self.__width):
                print("#", end="")
            print()
