import unittest

from day18.solution import BinaryTreePro


class BinaryTreeProTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(BinaryTreePro([3, 4, 5, 1, 2], [4, 1, 2]).is_subtree())

    def test_2(self):
        self.assertFalse(BinaryTreePro([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]).is_subtree())
