from day8.solution import LinkedList


class LinkedListPro(LinkedList):
    def is_circular(self):
        rabbit = self.head
        tortoise = self.head.child if self.head is not None else None

        while True:
            if rabbit is None or tortoise is None:
                return False

            if rabbit.value == tortoise.value:
                return True

            rabbit = rabbit.child
            tortoise = tortoise.child.child if tortoise.child is not None else None
