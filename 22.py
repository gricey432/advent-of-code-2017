"""
http://adventofcode.com/2017/day/22
"""
from typing import Dict, Tuple
from collections import defaultdict


def turn(dx, dy):
    # Turns right. Can turn left by just inverting x and y before passing in
    if dx == 1:
        return 0, 1
    elif dx == -1:
        return 0, -1
    elif dy == 1:
        return -1, 0
    elif dy == -1:
        return 1, 0
    raise ValueError


# Part 1
# True for infected
grid = defaultdict(lambda: False)  # type: Dict[Tuple[int, int]: bool]
x = y = None  # Scopefix
with open('22.in', 'r') as f:
    for y, l in enumerate(f):
        for x, c in enumerate(l.strip()):
            grid[(x, y)] = c == '#'

x, y = x // 2, y // 2  # Start in the middle of the grid
dx, dy = 0, -1  # Facing north
infection_counter = 0
for _ in range(10000):
    if grid[(x, y)]:
        # Infected
        dx, dy = turn(dx, dy)
    else:
        # Clean
        dx, dy = turn(-dx, -dy)
        infection_counter += 1
    grid[(x, y)] = not grid[(x, y)]
    x += dx
    y += dy
print(infection_counter)


# Part 2
STATE_CLEAN = 0
STATE_WEAKENED = 1
STATE_INFECTED = 2
STATE_FLAGGED = 3

grid = defaultdict(lambda: STATE_CLEAN)  # type: Dict[Tuple[int, int]: int]
x = y = None  # Scopefix
with open('22.in', 'r') as f:
    for y, l in enumerate(f):
        for x, c in enumerate(l.strip()):
            grid[(x, y)] = STATE_INFECTED if c == '#' else STATE_CLEAN

x, y = x // 2, y // 2  # Start in the middle of the grid
dx, dy = 0, -1  # Facing north
infection_counter = 0
for _ in range(10000000):
    state = grid[(x, y)]
    if state == STATE_CLEAN:
        dx, dy = turn(-dx, -dy)
    elif state == STATE_WEAKENED:
        infection_counter += 1
    elif state == STATE_INFECTED:
        dx, dy = turn(dx, dy)
    elif state == STATE_FLAGGED:
        dx, dy = turn(*turn(dx, dy))
    grid[(x, y)] = (state + 1) % 4
    x += dx
    y += dy
print(infection_counter)
