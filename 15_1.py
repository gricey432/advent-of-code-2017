"""
http://adventofcode.com/2017/day/15
"""
from builtins import range
from typing import Generator
from itertools import izip


def generator(start, factor):
    # type: (int, int) -> Generator[str]
    n = start
    while True:
        n = (n * factor) % 2147483647  # Magic number from spec
        n_b = str(bin(n))[2:]
        yield n_b.zfill(32)[-16:]


# Input data
generator_a = generator(289, 16807)
generator_b = generator(629, 48271)


res = sum(
    1
    for _ in range(40000000)
    if next(generator_a) == next(generator_b)
)

print(str(res))
