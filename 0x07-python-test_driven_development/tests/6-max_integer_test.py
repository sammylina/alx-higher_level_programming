#!/usr/bin/python3
"""Unit test for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the max_integer function

    """
    def test_max(self):
        """test if the function returns the maximum
        integer of a list

        """
        self.assertEqual(max_integer([4, 1, 3, 6, 4]), 6)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_value(self):
        """check when list is empity it returned None.
        """
        self.assertEqual(max_integer(), None)
