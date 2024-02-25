import unittest

from day19.solution import LinkedListPro
from day8.solution import LinkedList


class LinkedListProTest(unittest.TestCase):
    def test_1(self):
        linkedLists = LinkedListPro([2, 4, 3], [5, 6, 7])
        resultantList = LinkedList(list(reversed(linkedLists.sum(linkedLists.first_list.head, linkedLists.second_list.head, 0)[:-1])))
        self.assertEqual(resultantList.traverse(), "1 -> 1 -> 0 -> 7")