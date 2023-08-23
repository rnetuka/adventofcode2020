import unittest
import src.day04 as day4
from src.util import count_if


class Day4Tests(unittest.TestCase):

    def setUp(self):
        self.passports = day4.load_passports('../res/day04.txt')

    def test_valid_passports(self):
        count = count_if(self.passports, lambda x: x.is_valid())
        self.assertEqual(count, 213)

    def test_strictly_valid_passports(self):
        count = count_if(self.passports, lambda x: x.is_valid(strict=True))
        self.assertEqual(count, 147)
