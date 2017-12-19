"""
http://adventofcode.com/2017/day/10
"""
from operator import xor
from functools import reduce


class CircularList(list):
    """
    Lets a list loop back on itself
    Doesn't support some slice stuff like [5:], where it wouldn't make sense on an 'infinite' list
    """
    def __getslice__(self, i, j):
        # Py2 compat
        return self.__getitem__(slice(i, j))

    def __getitem__(self, key):
        size = self.__len__()
        if isinstance(key, int):
            key %= size
        elif isinstance(key, slice):
            # Forgive this code, wow
            return [self.__getitem__(i) for i in range(key.start or 0, key.stop, key.step or 1)]
        return super(CircularList, self).__getitem__(key)

    def __setitem__(self, key, o):
        size = self.__len__()
        if isinstance(key, int):
            key %= size
        elif isinstance(key, slice):
            # Forgive this code, wow
            for oi, i in zip(o, range(key.start or 0, key.stop, key.step or 1)):
                self.__setitem__(i, oi)
            return
        return super(CircularList, self).__setitem__(key, o)


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
