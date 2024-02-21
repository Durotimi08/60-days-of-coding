import unittest

from day15.solution import LinkedListReversal


class LinkedListReversalTes(unittest.TestCase):
    def test_1(self):
        list = LinkedListReversal([1, 2, 3, 4, 5])
        list.reverse()
        self.assertEqual(list.traverse(), "5 -> 4 -> 3 -> 2 -> 1")
