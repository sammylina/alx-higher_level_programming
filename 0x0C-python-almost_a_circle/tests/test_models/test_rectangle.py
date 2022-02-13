#!/usr/bin/python3
"""test_rectangle module"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test cases for Rectangle class"""

    def test_rectangle_extends_base(self):
        r = Rectangle()
        self.assertTrue(isinstance(r, Base))
        
    def test_rectangle_id(self):
        r = Rectangle()
        self.assertEqual(r.id, 1)
        r = Rectangle(399)
        self.assertEqual(r.id, 399)
