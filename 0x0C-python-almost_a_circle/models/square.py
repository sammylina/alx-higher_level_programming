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
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                                                       self.id,
                                                       self.x, self.y,
                                                       self.height)
