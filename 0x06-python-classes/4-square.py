#!/usr/bin/python3
"""Square module"""


class Square:
    """This class represents a Sqaure.

    Atttibutes:
        __size (int): size of the sqaure.
        must be >= 0, default value is 0
    """

    def __init__(self, size=0):
        """initaialize sqaure with positive value

        Args:
            size (int): size of sqaure
        """
        self.size = size

    @property
    def size(self):
        """get __size attribute of the class"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """calculate area of the square

        Returns:
            current square area
        """
        area = self.__size * self.__size
        return area
