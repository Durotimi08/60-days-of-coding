import unittest

from day11.solution import RootToLeafNumbersSum


class RootToLeafNumbersSumTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(RootToLeafNumbersSum([1, 2, 3]).sum(), 25)

    def test_2(self):
        self.assertEqual(RootToLeafNumbersSum([4,9,0,5,1]).sum(), 1026)
