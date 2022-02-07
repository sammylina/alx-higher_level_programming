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
