import unittest

from day21.solution import LongestPalindromeSubstring


class LongestPalindromeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual("bab", LongestPalindromeSubstring("babad").get())

    def test_2(self):
        self.assertEqual("bb", LongestPalindromeSubstring("cbbd").get())
