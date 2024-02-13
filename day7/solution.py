class Heap:
    def __init__(self, size):
        self.values = [0 for _ in range(size)]
        self.current_size = 0
        self.size = size

    def swap(self, index, another_index):
        self.values[index], self.values[another_index] = self.values[another_index], self.values[index]

    def add(self, value):
        # Add value at last index
        self.values[self.current_size] = value
        current_position = self.current_size
        self.current_size += 1

        # Keep leveling up until it's parent is not smaller than itself
        while self.current_size >= 1:
            parent_position = current_position // 2
            if self.values[current_position] < self.values[parent_position]:
                self.swap(current_position, parent_position)
            else:
                break

            current_position //= 2

    def min_heap(self):
        # Copy last element to first & drop last element
        self.values[0] = self.values[self.current_size - 1]
        self.current_size -= 1

        # Keep it pushing down until it's children are bigger than itself
        current_position = 0
        while current_position < self.current_size:
            left_child_position = current_position * 2
            right_child_position = current_position * 2 + 1

            if (left_child_position < self.current_size and self.values[current_position] > self.values[left_child_position]
            ) or (
                    right_child_position < self.current_size and self.values[current_position] > self.values[right_child_position]
            ):
                swappable_child_position = left_child_position
                
                if right_child_position < self.current_size and self.values[right_child_position] < self.values[left_child_position]:
                    swappable_child_position = right_child_position

                self.swap(current_position, swappable_child_position)
            else:
                break

            current_position = swappable_child_position

    def top(self):
        return self.values[0]


k = 4
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]

# Initialize min Heap of k elements
heap = Heap(k)

#  Add first k elements
for index in range(k):
    heap.add(nums[index])

# Add other elements which are large than than the smallest element of heap
for index in range(k, len(nums)):
    if heap.top() < nums[index]:
        heap.min_heap()
        heap.add(nums[index])

# Smallest element of heap is at top. Since it's Heap of k elements - it's k'th largest element
print(heap.top())
