#!/usr/bin/python3
"""Square module"""


class Square:
    """This class represents a Sqaure.

    Atttibutes:
        __size (int): size of the sqaure.
        must be >= 0, default value is 0
        __position (tuple): represent coordinate of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """initaialize sqaure with positive value

        Args:
            size (int): size of sqaure
            position (tuple): coordinate position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get __position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) is not tuple or len(position) != 2:
            print("position must be a tuple of 2 positive integers")
            return
        for p in self.__position:
            if type(p) is not int or p < 0:
                print("position must be a tuple of 2 positive integers")
                return
        self.__position = position

    def area(self):
        """calculate area of the square

        Returns:
            current square area
        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """print area of square using '#' to represent"""
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(self.__position[0] * " ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
