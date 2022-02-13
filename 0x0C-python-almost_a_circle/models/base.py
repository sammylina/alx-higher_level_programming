#!/usr/bin/python3
"""base module"""


class Base:
    """Base class for other shapes

    Attributes:
        __nb_objects (int): number of objects created from thsi class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id with given value

        Args:
            id (int): id of the obj, if it is None
                id will be __nb_objects + 1.

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
