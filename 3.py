"""
http://adventofcode.com/2017/day/3
"""
from __future__ import division

target = 361527  # My personal input


# Part 1
# Figure out which layer it's on
layer = 0
while (1 + (layer * 2)) ** 2 < target:
    layer += 1

# Work out the start value of that layer
layer_end = (1 + (layer * 2)) ** 2
layer_size = layer * 2 + 1

# Add up the movements needed to the last element of that layer (positive is down and right)
x = y = layer

defecit = layer_end - target
if defecit:
    diff = min(defecit, layer_size - 1)
    x -= diff
    defecit -= diff
if defecit:
    diff = min(defecit, layer_size - 1)
    y -= diff
    defecit -= diff
if defecit:
    diff = min(defecit, layer_size - 1)
    x += diff
    defecit -= diff
if defecit:
    diff = min(defecit, layer_size - 1)
    y += diff
    defecit -= diff

res = abs(x) + abs(y)
print(str(res))


# Part 2
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
