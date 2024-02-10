def trapWater(elevations):
    trapped_water = 0
    max_left_elevation = [0] * len(elevations)
    max_right_elevation = [0] * len(elevations)

    for i in range(1, len(elevations)):
        max_left_elevation[i] = max(max_left_elevation[i - 1], elevations[i - 1])

    for i in range(len(elevations) - 2, -1, -1):
        max_right_elevation[i] = max(max_right_elevation[i + 1], elevations[i + 1])

    for i in range(len(elevations)):
        if min(max_left_elevation[i], max_right_elevation[i]) - elevations[i] > 0:
            trapped_water += min(max_left_elevation[i], max_right_elevation[i]) - elevations[i]

    return trapped_water


print(trapWater([0, 2, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
