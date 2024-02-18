import unittest

from day12.solution import Permute


class NextPermutationTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Permute([1, 2, 3]).next(), [1, 3, 2])

    def test_2(self):
        self.assertEqual(Permute([3, 2, 1]).next(), [1, 2, 3])

    def test_3(self):
        self.assertEqual(Permute([1, 1, 5]).next(), [1, 5, 1])
