#!/usr/bin/python3
"""Geometry module
"""


class BaseGeometry:
    """Base for geometrical shapes and calculations

    """
    def area(self):
        """calculate and returns the area of the shape
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate input to the class
        Args:
            name (str): key for the value
            value (int): positive integer

        Raises:
            TypeError: if value is not integer
            ValueError: if value is not postive

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
