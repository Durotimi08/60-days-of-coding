import unittest

from day17.solution import LinkedListPro


class LinkedListProTest(unittest.TestCase):
    def test_1(self):
        linkedList = LinkedListPro([3, 2, 0, -4])
        linkedList.head.child.child.child.child = linkedList.head.child
        self.assertTrue(linkedList.is_circular())

    def test_2(self):
        linkedList = LinkedListPro([1, 2])
        linkedList.head.child.child = linkedList.head
        self.assertTrue(linkedList.is_circular())

    def test_3(self):
        linkedList = LinkedListPro([1])
        self.assertFalse(linkedList.is_circular())
