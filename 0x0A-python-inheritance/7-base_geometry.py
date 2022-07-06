#!/usr/bin/python3
"""BaseGeometry module
"""


class BaseGeometry:
    """BaseGeometry class that declares area method
    """
    def area(self):
        """calculate are of a Geometry
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validate argument value

        Args:
            name (string): name of the integer value
            value (int): integer value

        Raises:
            TypeError: if value is not integer type
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
