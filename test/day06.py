import unittest
import src.day06 as day6


class Day6Tests(unittest.TestCase):

    def setUp(self):
        self.groups = day6.read_groups()

    def test_anyone_yes_count(self):
        count = sum(day6.anyone_yes(group) for group in self.groups)
        self.assertEqual(count, 6782)

    def test_everyone_yes_count(self):
        count = sum(day6.everyone_yes(group) for group in self.groups)
        self.assertEqual(count, 3596)
