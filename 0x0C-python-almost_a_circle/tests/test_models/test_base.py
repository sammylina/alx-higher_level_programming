#!/usr/bin/python3
"""test_base module, test cases for base module"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test cases for Base class"""

    def test_id_none(self):
        b = Base()
        self.assertIsNotNone(b.id)
        self.assertNotEqual(b.id, 0)
        self.assertEqual(b.id, 1)



