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
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_argument_validity(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square('size')
            Square(None)
            Square({"size": 4})
            Square((4,))
            Square([4])
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
            Square(-1)

    def test__str__(self):
        s = Square(5, 0, 1, 55)
        output_str = "[Square] (55) 0/1 - 5"
        self.assertEqual(s.__str__(), output_str)
