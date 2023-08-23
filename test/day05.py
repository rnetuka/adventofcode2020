import unittest
import src.day05 as day5


class Day5Tests(unittest.TestCase):

    def setUp(self):
        with open('../res/day05.txt') as file:
            descriptions = file.read().splitlines()
        self.seat_ids = [day5.seat_id(description) for description in descriptions]

    def test_max_seat_id(self):
        seat_id = max(self.seat_ids)
        self.assertEqual(seat_id, 991)

    def test_find_my_seat(self):
        seat_id = day5.find_my_seat(self.seat_ids)
        self.assertEqual(seat_id, 534)
