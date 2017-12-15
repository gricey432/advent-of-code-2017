"""
http://adventofcode.com/2017/day/15
"""
from builtins import range
from typing import Generator
from itertools import izip


def generator(start, factor, factor_filter):
    # type: (int, int) -> Generator[str]
    n = start
    while True:
        n = (n * factor) % 2147483647  # Magic number from spec
        if n % factor_filter == 0:
            n_b = str(bin(n))[2:]
            yield n_b.zfill(32)[-16:]


# Input data
generator_a = generator(289, 16807, 4)
generator_b = generator(629, 48271, 8)


res = sum(
    1
    for _ in range(5000000)
    if next(generator_a) == next(generator_b)
)

print(str(res))
