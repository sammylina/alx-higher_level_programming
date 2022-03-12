#!/usr/bin/python3
"""Square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class represents a Square and inherits from
    Rectangle class

    Arguments:
            size (int): height and width of the Square
            x (int): defualt value 0
            y (int): default value 0
            id (int): unique identifier of the instance

    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square as Rectangle class only with
        the same height and width

        Args:
            size (int): height and width of the Square
            x (int): defualt value 0
            y (int): default value 0
            id (int): unique identifier of the instance
        """

        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """Return the string representation of the Sqaure
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                                                       self.id,
                                                       self.x, self.y,
                                                       self.height)

    @property
    def size(self):
        """Return the size of the Square
        """
        return self.height

    @size.setter
    def size(self, new_size):
        """Set new value to the height and width of a Square
        """
        self.width = new_size
        self.height = new_size

    def update(self, *args, **kwargs):
        """update id, size, x and y value of instance"""
        if args and len(args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.height = args[1]
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        if not args and kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

