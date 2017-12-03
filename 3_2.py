"""
http://adventofcode.com/2017/day/3
"""

target = 361527  # My personal input value


def spiral_generator():
    """
    Generates (x, y) coord tuples in a spiral starting at (0, 0)
    """
    layer = 0
    x = 0
    y = 0
    yield(0, 0)

    while True:
        layer += 1
        layer_size = layer * 2 + 1
        x += 1
        yield(x, y)
        for _ in range(layer_size - 2):
            y -= 1
            yield (x, y)
        for _ in range(layer_size - 1):
            x -= 1
            yield (x, y)
        for _ in range(layer_size - 1):
            y += 1
            yield (x, y)
        for _ in range(layer_size - 1):
            x += 1
            yield (x, y)


grid = {}
for x, y in spiral_generator():
    if x == y == 0:
        # Initial case
        val = 1
    else:
        val = sum(
            grid.get((x + d_x, y + d_y), 0)
            for d_x in range(-1, 2)
            for d_y in range(-1, 2)
        )

    if val > target:
        print(str(val))
        break

    grid[(x, y)] = val
