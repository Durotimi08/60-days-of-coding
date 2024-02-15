import unittest

from day9.solution import Solution


class Day9Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().run(2), 2)

    def test_2(self):
        self.assertEqual(Solution().run(3), 3)

    def test_3(self):
        self.assertEqual(Solution().run(4), 5)
