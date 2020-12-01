import unittest
import src.day01 as day1


class Day1Tests(unittest.TestCase):

    def setUp(self):
        with open('../res/day01.txt') as file:
            self.expense_report = [int(line) for line in file.readlines()]

    def test_1st_answer(self):
        a, b = day1.find_two_entries(self.expense_report)
        self.assertEqual(a * b, 1_006_176)

    def test_2nd_answer(self):
        a, b, c = day1.find_three_entries(self.expense_report)
        self.assertEqual(a * b * c, 199_132_160)
