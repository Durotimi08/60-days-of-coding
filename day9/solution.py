class Solution:
    def run(self, floors_count):
        if floors_count in [1, 2]:
            return floors_count

        last_floor_steps = 2
        second_last_floor_steps = 1
        total_steps = 0
        for floor in range(2, floors_count):
            total_steps = last_floor_steps + second_last_floor_steps
            second_last_floor_steps = last_floor_steps
            last_floor_steps = total_steps

        return total_steps