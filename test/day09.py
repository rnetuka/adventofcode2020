import unittest
import src.day09 as day9


class Day9Tests(unittest.TestCase):

    def setUp(self):
        with open('../res/day09.txt') as file:
            self.data = [int(line) for line in file.readlines()]

    def test_find_first(self):
        n = day9.find_first(self.data)
        self.assertEqual(n, 138_879_426)

    def test_find_encryption_weakness(self):
        w = day9.find_encryption_weakness(self.data)
        self.assertEqual(w, 23_761_694)
