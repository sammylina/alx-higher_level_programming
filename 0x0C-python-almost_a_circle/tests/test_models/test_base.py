#!/usr/bin/python3
"""test_base module, test cases for base module"""


import unittest
import Base
   

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id_none(self):
        base = Base()
        self.assertIsNotNone(base.id)
        self.assertNotEqual(base.id, 0)
        self.assertEqual(base.id, 1)

        
