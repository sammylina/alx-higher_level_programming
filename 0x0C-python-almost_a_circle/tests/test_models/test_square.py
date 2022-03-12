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
        """test if the Square class inherites from Rectangle"""
        s = Square(4)
        self.assertIsInstance(s, Rectangle)
        self.assertIs(type(s), Square)

    def test_size(self):
        """set size(height, width) of the Square"""
        s = Square(5)
        self.assertEqual(s.width, s.height)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_argument_validity(self):
        """validate all arguments of Square"""
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
        """return str discription of the instance"""
        s = Square(5, 0, 1, 55)
        output_str = "[Square] (55) 0/1 - 5"
        self.assertEqual(s.__str__(), output_str)

    def test_size_setter(self):
        """set size of the Square"""
        s = Square(4)
        s.size = 5
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_update(self):
        """update attributes of Square class"""
        s = Square(100)
        s.update(10, 11, 12, 13, id=15, size=16, x=17, y=18)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.height, 11)
        self.assertEqual(s.width, 11)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 13)
        s.update(id=15, size=16, x=17, y=18)
        self.assertEqual(s.id, 15)
        self.assertEqual(s.height, 16)
        self.assertEqual(s.width, 16)
        self.assertEqual(s.x, 17)
        self.assertEqual(s.y, 18)

