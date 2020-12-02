import unittest
import src.day02 as day2
from src.day02 import count_if


class Day2Tests(unittest.TestCase):

    def setUp(self):
        with open('../res/day02.txt') as file:
            self.passwords = file.readlines()

    def test_valid_passwords(self):
        count = count_if(self.passwords, day2.is_password_valid)
        self.assertEqual(count, 398)

    def test_valid_passwords_reworked(self):
        count = count_if(self.passwords, day2.is_password_valid_reworked)
        self.assertEqual(count, 562)
