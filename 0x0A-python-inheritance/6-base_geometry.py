#!/usr/bin/python3
"""Geometry module
"""


class BaseGeometry:
    """Base for geometrical shapes and calculations

    """
    def area(self):
        raise Exception('area() is not implemented')
