"""
http://adventofcode.com/2017/day/15
"""
from builtins import range
from typing import Generator, Optional


def generator(start, factor, factor_filter=None):
    # type: (int, int, Optional[int]) -> Generator[str]
    n = start
    while True:
        n = (n * factor) % 2147483647  # Magic number from spec
        if not factor_filter or n % factor_filter == 0:
            n_b = str(bin(n))[2:]
            yield n_b.zfill(32)[-16:]


# Part 1
generator_a = generator(289, 16807)
generator_b = generator(629, 48271)

res = sum(
    1
    for _ in range(40000000)
    if next(generator_a) == next(generator_b)
)

print(str(res))


# Part 2
generator_a = generator(289, 16807, 4)
generator_b = generator(629, 48271, 8)

res = sum(
    1
    for _ in range(5000000)
    if next(generator_a) == next(generator_b)
)

print(str(res))
