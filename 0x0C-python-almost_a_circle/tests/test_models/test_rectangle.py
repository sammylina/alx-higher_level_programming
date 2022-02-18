#!/usr/bin/python3
"""test_rectangle module"""

import unittest
from unittest.mock import patch
import io
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
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, False, 3, 4)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 'four', 5)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -3)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 0, 0, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -1, 0, 4)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 0, -1, 3)
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

    def test_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        r = Rectangle(3, 4)
        result = "###\n###\n###\n###\n"
        r.display()
        self.assertEqual(mock_stdout.getvalue(), result)

    def test_str_(self):
        r = Rectangle(3, 4, 0, 0, 11)
        r_str = '[Rectangle] (11) 0/0 - 3/4\n'
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            print(r)
        self.assertEqual(mock_stdout.getvalue(), r_str)
