import unittest
import src.day08 as day8


class Day8Tests(unittest.TestCase):

    def setUp(self):
        with open('../res/day08.txt') as file:
            self.code = day8.read_instructions(file.read())

        self.console = day8.HandheldConsole()

    def test_force_halt(self):
        try:
            self.console.run(self.code)
        except day8.ForceHaltError:
            pass
        self.assertEqual(self.console.accumulator, 1801)

    def test_repaired_code(self):
        self.console.run(day8.repaired(self.code))
        self.assertEqual(self.console.accumulator, 2060)
