import unittest

from day10.solution import CoinDispenser


class Day10Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(CoinDispenser([1, 2, 5]).dispense(6), 2)

    def test_2(self):
        self.assertEqual(CoinDispenser([2]).dispense(3), -1)

    def test_3(self):
        self.assertEqual(CoinDispenser([1, 2, 5, 10]).dispense(33), 5)

    def test_4(self):
        self.assertEqual(CoinDispenser([2, 5]).dispense(8), 4)
