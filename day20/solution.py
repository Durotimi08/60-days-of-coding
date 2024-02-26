class IslandMapper:
    def __init__(self, values):
        self.values = values

    def get_surface_area(self, row, column, discovered_area):
        if 0 > row or row >= len(self.values) or 0 > column or column >= len(self.values[0]):
            return discovered_area

        if self.values[row][column] == 1:
            self.values[row][column] = -1
            discovered_area += 1
            return discovered_area + self.get_surface_area(row + 1, column, 0) + self.get_surface_area(row - 1, column, 0) + self.get_surface_area(row, column + 1, 0) + self.get_surface_area(row, column - 1, 0)
        else:
            return discovered_area

    def get_biggest_surface_area(self):
        biggest_surface_area = 0

        for row, values in enumerate(self.values):
            for column, value in enumerate(values):
                if value == 1:
                    biggest_surface_area = max(self.get_surface_area(row, column, 0), biggest_surface_area)

        return biggest_surface_area
