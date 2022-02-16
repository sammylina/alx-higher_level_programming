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
            raise(TypeError)
        elif value <= 0:
            raise(ValueError)
        self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        """positive integer value"""
        if type(value) is not int:
            raise(TypeError)
        elif value <= 0:
            raise(ValueError)
        self.__height = value
        return self.__height

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y
