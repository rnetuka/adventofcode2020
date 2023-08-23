import unittest
from src.util import *


class UtilTest(unittest.TestCase):

    def test_matching_parenthesis_substring(self):
        string = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        expected = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6)'
        result = matching_parenthesis_substring(string)
        self.assertEqual(expected, result)
