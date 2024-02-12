def is_paintable(i, j):
    return (0 <= i < len(map)) and (0 <= j < len(map[0])) and map[i][j] == '1'


def color_it(i, j):
    if is_paintable(i, j):
        map[i][j] = "COLORED"
        color_it(i, j + 1)
        color_it(i + 1, j)
        color_it(i - 1, j)
        color_it(i, j - 1)


count = 0
map = """11000
11001
00100
00011""".split()
map = [list(row) for row in map]

for i, row in enumerate(map):
    for j, cell in enumerate(row):
        if is_paintable(i, j):
            count += 1
            color_it(i, j)

print(count)
