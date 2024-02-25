from day8.solution import LinkedList, Node


class LinkedListPro:
    def __init__(self, first_list_values, second_list_values):
        self.first_list = LinkedList(first_list_values)
        self.second_list = LinkedList(second_list_values)

    def sum(self, first_node, second_node, carry):
        if first_node is None and second_node is None and carry == 0:
            return [None]

        value = (first_node.value if first_node else 0) + (second_node.value if second_node else 0) + carry
        values = [value % 10]
        carry = value // 10

        values.extend(self.sum(first_node.child if first_node else None, second_node.child if second_node else None, carry))

        return values
