#!/usr/bin/python3
"""test_base module, test cases for base module"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test cases for Base class"""

    def test_id_isnone(self):
        b = Base()
        self.assertIsNotNone(b.id)
        self.assertNotEqual(b.id, 0)
        self.assertEqual(b.id, 1)
    def test_id_isnumber(self):
        b = Base(6)
        self.assertIsNotNone(b.id)
        self.assertNotEqual(b.id, 1)
        self.assertNotEqual(b.id, 0)
        self.assertEqual(b.id, 6)


