"""
http://adventofcode.com/2017/day/14
"""
from functools import reduce
from operator import xor
from typing import List

from aoccommon import CircularList


KEY = "hfdlxzhv"  # My input

grid = []  # type: List[List[bool]]
for row_n in range(128):
    lengths = [ord(c) for c in "{}-{}".format(KEY, row_n)]
    lengths += [17, 31, 73, 47, 23]  # Magic numbers from spec
    rope = CircularList(range(256))
    pointer = 0
    skip = 0
    for _ in range(64):  # 64 rounds from spec
        for length in lengths:
            section = rope[pointer:pointer + length]
            rope[pointer:pointer + length] = reversed(section)
            pointer += length + skip
            skip += 1

    dense_hash = [reduce(xor, rope[n * 16:n * 16 + 16]) for n in range(16)]
    res = ''.join(bin(h)[2:].zfill(8) for h in dense_hash)
    grid.append([c == '1' for c in res])

# Part 1
count_used = sum(
    1 if grid[y][x] else 0
    for y in range(128)
    for x in range(128)
)
print(count_used)


# Part 2
queue = [
    (x, y)
    for y in range(128)
    for x in range(128)
]
region_count = 0
while queue:
    region = []
    region_queue = [queue.pop()]
    while region_queue:
        cx, cy = region_queue.pop()
        if grid[cy][cx]:
            region.append((cx, cy))
            for x, y in [(cx, cy-1), (cx, cy+1), (cx-1, cy), (cx+1, cy)]:
                if 0 <= x < 128 and 0 <= y < 128:
                    if (x, y) not in region_queue and (x, y) not in region and (x, y) in queue:
                        region_queue.append((x, y))
                        queue.remove((x, y))
    if region:
        region_count += 1
print(region_count)
