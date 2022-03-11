#!/usr/bin/python3
"""square test module
"""


from unittest import mock
import unittest

from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class
    """

    def test_inherit_from_base(self):
        s = Square(4)
        self.assertIsInstance(s, Rectangle)
        self.assertIs(type(s), Square)

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.width, s.height)

    def test_argument_validity(self):
        with self.assertRaises(TypeError):
            s = Square(False)
        with self.assertRaises(TypeError):
            s = Square(5, 'xvalue')
        with self.assertRaises(TypeError):
            s = Square(4, 0, 'yvalue')
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(ValueError):
            s = Square(1, -1)
        with self.assertRaises(ValueError):
            s = Square(1, 3, -4)

    def test__str__(self):
        s = Square(5, 0, 1, 55)
        output_str = "[Square] (55) 0/1 - 5"
        self.assertEqual(s.__str__(), output_str)
