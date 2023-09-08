#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def text_max_integer(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_unordered(self):
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_max_integer_negative(self):
        result = max_integer([-1 -3, -4, -2])
        self.assertEqual(result, -1)

    def test_max_integer_mixed(self):
        result = max_integer([-1, 3, -4, 2])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()