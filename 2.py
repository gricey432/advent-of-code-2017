"""
http://adventofcode.com/2017/day/2
"""
from __future__ import division


with open('2.in', 'r') as f:
    data = [
        [int(n) for n in row.strip().split('\t')]
        for row in f
    ]


# Part 1
res = sum(max(vals) - min(vals) for vals in data)
print(str(res))


# Part 2
res = sum(
    x // y
    for row in data
    for x in row
    for y in row
    if x % y == 0 and x != y
)
print(str(res))
