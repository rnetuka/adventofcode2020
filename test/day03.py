import unittest
import src.day03 as day3


class Day3Tests(unittest.TestCase):

    def setUp(self):
        self.toboggan = day3.Toboggan.from_file('../res/day03.txt')

    def test_encountered_trees_1(self):
        count = self.toboggan.encountered_trees()
        self.assertEqual(count, 270)

    def test_encountered_trees_2(self):
        a = self.toboggan.encountered_trees(slope=(1, 1))
        b = self.toboggan.encountered_trees(slope=(3, 1))
        c = self.toboggan.encountered_trees(slope=(5, 1))
        d = self.toboggan.encountered_trees(slope=(7, 1))
        e = self.toboggan.encountered_trees(slope=(1, 2))
        self.assertEqual(a * b * c * d * e, 2_122_848_000)
