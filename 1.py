"""
http://adventofcode.com/2017/day/1
"""
from __future__ import division


with open('1.in', 'r') as f:
    sequence = f.read().strip()

size = len(sequence)


# Part 1
res = sum(
    int(sequence[i])
    for i in range(size)
    if sequence[i] == sequence[(i + 1) % size]
)

print(str(res))


# Part 2
res = sum(
    int(sequence[i])
    for i in range(size)
    if sequence[i] == sequence[(i + size // 2) % size]
)

print(str(res))
