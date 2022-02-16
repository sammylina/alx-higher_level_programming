#!/usr/bin/python3
"""test_rectangle module"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test cases for Rectangle class"""

    def test_valid_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1, '3')
        with self.assertRaises(TypeError):
            r = Rectangle('five', 1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 4, 0, 0, 'three')
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -3)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 0, 0, 0)
        r = Rectangle(1, 2, 0, 0)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        
    def test_rectangle_extends_base(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Base)
        
    def test_rectangle_id(self):
        r1 = Rectangle(1, 2, 3, 4 , 399)
        self.assertEqual(r1.id, 399)
        b1 = Base()
        r2 = Rectangle(1, 2)
        self.assertEqual(b1.id + 1, r2.id)
