from day11.solution import BinaryTree, BinaryTreeNode


class MergeBinaryTree:
    def __init__(self, first_tree_values, second_tree_values):
        self.first_tree = BinaryTree(first_tree_values)
        self.second_tree = BinaryTree(second_tree_values)
        self.merged_tree_node = None

    def mergeNode(self, first_tree_node, second_tree_node):
        if first_tree_node is None and second_tree_node is None:
            return None
        if first_tree_node is None:
            return second_tree_node
        if second_tree_node is None:
            return first_tree_node
        else:
            node = BinaryTreeNode(first_tree_node.value + second_tree_node.value)
            node.left = self.mergeNode(first_tree_node.left, second_tree_node.left)
            node.right = self.mergeNode(first_tree_node.right, second_tree_node.right)
            return node

    def merge(self):
        self.merged_tree_node = self.mergeNode(self.first_tree.root, self.second_tree.root)

    def traverse(self, node, traversed):
        if node:
            self.traverse(node.left, traversed)
            traversed.append(node.value)
            self.traverse(node.right, traversed)
