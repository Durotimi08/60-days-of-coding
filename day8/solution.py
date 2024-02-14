class Node:
    def __init__(self, _value):
        self.value = _value
        self.child = None

    def next(self):
        return self.child

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)


class LinkedList(list):
    def __init__(self, init_values):
        self.length = len(init_values)
        self.head = Node(init_values[0])
        self.current_node = self.head

        parent = self.head
        for value in init_values[1:]:
            parent.child = Node(value)
            parent = parent.child

    def __len__(self):
        return self.length

    def next(self):
        self.current_node = self.current_node.next()
        return self.current_node

    def traverse(self):
        node = self.head
        values = [node.value]

        while node.next():
            node = node.next()
            values.append(node.value)

        values = [str(value) for value in values]
        return " -> ".join(values)


def move_head(head, pos):
    for i in range(pos):
        head = head.next()
    return head


linked_list_1 = LinkedList([2, 6, 4])
linked_list_2 = LinkedList([1, 5])

size_of_A = len(linked_list_1)
size_of_B = len(linked_list_2)

min_size = min(size_of_A, size_of_B)

linked_list_1_node = move_head(linked_list_1.head, size_of_A - min_size)
linked_list_2_node = move_head(linked_list_2.head, size_of_B - min_size)

while linked_list_1_node is not None and linked_list_2_node is not None:
    if linked_list_1_node == linked_list_2_node:
        print("Intersection node : %s" % linked_list_1_node)
        break
    linked_list_1_node = linked_list_1_node.next()
    linked_list_2_node = linked_list_2_node.next()

print("No intersection node found")
