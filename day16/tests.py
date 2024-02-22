import unittest

from day16.solution import MergeBinaryTree


class MergeBinaryTreeTest(unittest.TestCase):
    def test_1(self):
        traversed_values = []
        merge_tree = MergeBinaryTree([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7])
        merge_tree.merge()
        merge_tree.traverse(merge_tree.merged_tree_node, traversed_values)
        self.assertEqual(traversed_values, [5, 4, 4, 3, 5, 7])
