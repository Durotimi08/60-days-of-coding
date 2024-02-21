from day8.solution import LinkedList


class LinkedListReversal:
    def __init__(self, values):
        self.list = LinkedList(values)

    def reverse(self):
        if self.list.head is None or self.list.head.child is None:
            return self.list.traverse()

        reversed_list_head = self.list.head
        current_node = self.list.head.child
        reversed_list_head.child = None

        while current_node is not None:
            temp = current_node.child
            current_node.child = reversed_list_head
            reversed_list_head = current_node
            current_node = temp

        self.list.head = reversed_list_head

    def traverse(self):
        return self.list.traverse()
