import unittest

from day14.solution import Trader


class TraderTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Trader([7, 1, 5, 3, 6, 4]).predict(), 5)

    def test_2(self):
        self.assertEqual(Trader([7, 6, 4, 3, 1]).predict(), 0)
