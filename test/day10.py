import unittest
import src.day10 as day10


class Day10Tests(unittest.TestCase):

    def setUp(self):
        with open('../res/day10.txt') as file:
            self.adapters = sorted(int(n) for n in file.readlines())

    def test_differences(self):
        differences = day10.joltage_differences(self.adapters)
        result = differences[1] * differences[3]
        self.assertEqual(result, 2475)

    def test_distinct_ways(self):
        ways = day10.distinct_ways(self.adapters)
        self.assertEqual(ways, 442_136_281_481_216)
