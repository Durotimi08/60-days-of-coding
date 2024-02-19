import unittest

from day13.solution import MoneyHeist


class MoneyHeistTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(MoneyHeist([1, 2, 3, 1]).predict(), 4)

    def test_2(self):
        self.assertEqual(MoneyHeist([2, 7, 9, 3, 1]).predict(), 12)

    def test_3(self):
        self.assertEqual(MoneyHeist([2, 1, 2, 3, 1, 2]).predict(), 7)
