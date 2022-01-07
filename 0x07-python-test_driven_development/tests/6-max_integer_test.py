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
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([3, -1, 2, 1]), 3)
        self.assertEqual(max_integer([-5, -2, -4, -3]), -2)

    def test_value(self):
        """check when list is empity it returned None.
        """
        self.assertEqual(max_integer(), None)
