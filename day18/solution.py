from day11.solution import BinaryTree


class BinaryTreePro(BinaryTree):
    def __init__(self, first_tree_values, second_tree_values):
        self.first_tree = BinaryTree(first_tree_values)
        self.second_tree = BinaryTree(second_tree_values)

    def find_first_similar_node(self, first_tree_node):
        if first_tree_node is None:
            return None

        if first_tree_node.value == self.second_tree.root.value:
            return first_tree_node

        return self.find_first_similar_node(first_tree_node.right) or self.find_first_similar_node(first_tree_node.left)

    def is_similar(self, first_tree_node, second_tree_node):
        if first_tree_node is None and second_tree_node is None:
            return True

        if first_tree_node is None or second_tree_node is None:
            return False

        if first_tree_node.value != second_tree_node.value:
            return False

        return self.is_similar(first_tree_node.left, second_tree_node.left) and self.is_similar(first_tree_node.right,
                                                                                                  second_tree_node.right)

    def is_subtree(self):
        first_similar_node = self.find_first_similar_node(self.first_tree.root)

        if first_similar_node is None:
            return False

        return self.is_similar(first_similar_node, self.second_tree.root)
