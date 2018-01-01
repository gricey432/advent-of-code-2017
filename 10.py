"""
http://adventofcode.com/2017/day/10
"""
from operator import xor
from functools import reduce

from aoccommon import CircularList

# Part 1
with open('10.in', 'r') as f:
    lengths = [int(n) for n in f.read().split(',')]

rope = CircularList(range(256))
pointer = 0
skip = 0
for length in lengths:
    section = rope[pointer:pointer + length]
    rope[pointer:pointer + length] = reversed(section)
    pointer += length + skip
    skip += 1

print(str(rope[0] * rope[1]))


# Part 2
with open('10.in', 'r') as f:
    lengths = [ord(c) for c in f.read().strip()]
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

dense_hash = [reduce(xor, rope[n*16:n*16+16]) for n in range(16)]
res = ''.join(hex(h)[2:] for h in dense_hash)
print(res)
