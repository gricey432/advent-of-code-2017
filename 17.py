"""
http://adventofcode.com/2017/day/17
"""
from collections import deque
from builtins import range  # Py2 compat.


steps = 380  # Puzzle input


def spinlock(n):
    buffer = deque([0])
    for n in range(1, n + 1):
        buffer.append(n)
        buffer.rotate(-1 * (steps % len(buffer)))
    buffer.rotate(-1 * buffer.index(0))  # Put 0 back at the start
    return list(buffer)


# Part 1
res = spinlock(2017)
print(res[res.index(2017) + 1])

# Part 2
res = spinlock(50000000)
print(res[1])
