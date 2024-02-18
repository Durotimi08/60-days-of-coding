import math


class Permute:
    def __init__(self, values):
        self.value = values

    def swap(self, source_index, destination_index):
        self.value[source_index], self.value[destination_index] = self.value[destination_index], self.value[source_index]

    def flip(self, start_index):
        end = math.ceil((len(self.value) - (start_index + 1)) / 2) + start_index
        for i in range(start_index + 1, end + 1):
            self.swap(i, len(self.value) - i + start_index)

    def next(self):
        first_decreasing_instance = -1
        for i in range(len(self.value)-1, 0, -1):
            if self.value[i] > self.value[i-1]:
                first_decreasing_instance = i-1
                break

        if first_decreasing_instance >= 0:
            next_higher_instance = first_decreasing_instance+1
            for i in range(first_decreasing_instance+2, len(self.value)):
                if self.value[first_decreasing_instance] < self.value[i]:
                    if self.value[i]-self.value[first_decreasing_instance] <= self.value[next_higher_instance]-self.value[first_decreasing_instance]:
                        next_higher_instance = i

            self.swap(first_decreasing_instance, next_higher_instance)

        self.flip(first_decreasing_instance)

        return self.value
