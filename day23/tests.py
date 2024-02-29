import unittest

from day23.solution import TopKFrequentElements


class TopKFrequentElementsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 2], TopKFrequentElements([1, 1, 1, 2, 2, 3]).get(2))

    def test_2(self):
        self.assertEqual([1], TopKFrequentElements([1]).get(1))
