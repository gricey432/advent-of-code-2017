"""
http://adventofcode.com/2017/day/11
"""
from __future__ import division


with open('11.in', 'r') as f:
    steps = f.read().strip().split(',')


def distance(x, y):
    x, y = abs(x), abs(y)
    return y + ((x-y)//2 if x > y else 0)


x = y = 0  # Ascending is south east
furthest = 0
for step in steps:
    if step == 'n':
        x -= 2
    elif step == 's':
        x += 2
    else:
        if step.startswith('n'):
            x -= 1
        elif step.startswith('s'):
            x += 1
        if step.endswith('w'):
            y -= 1
        elif step.endswith('e'):
            y += 1

    furthest = max(furthest, distance(x, y))

print(str(distance(x, y)))
print(str(furthest))
