import unittest
import src.day07 as day7


class Day7Tests(unittest.TestCase):

    def setUp(self):
        with open('../res/day07.txt') as file:
            input = file.read()
            self.rules = day7.Rules.parse(input)

    def test_total_predecessors(self):
        count = self.rules.count_predecessors_of('shiny gold')
        self.assertEqual(count, 372)

    def test_total_contents(self):
        count = self.rules.count_total_contents_of('shiny gold')
        self.assertEqual(count, 8015)
