#!/usr/bin/python3
"""Maximum integer unit test module

"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case class"""

    def test_max_integer(self):
        max = max_integer([4, 2, 6, 3, 9, 2])
        self.assertEqual(max, 9)
        max = max_integer([5, 4, 3])
        self.assertEqual(max, 5)
        max = max_integer([-4, -5, -2])
        self.assertEqual(max, -2)
        max = max_integer([-3, -1, 6, 0, 4])
        self.assertEqual(max, 6)
        max = max_integer([])
        self.assertEqual(max, None)
        max = max_integer([8])
        self.assertEqual(max, 8)

        with self.assertRaises(TypeError):
            max_integer(False)
