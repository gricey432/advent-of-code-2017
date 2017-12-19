"""
http://adventofcode.com/2017/day/12
"""
import re
from typing import Optional


pattern = r"(\d+) <-> (.+)"


data = {}
with open('12.in', 'r') as f:
    for l in f:
        match = re.match(pattern, l.strip())
        data[int(match.group(1))] = [int(d) for d in match.group(2).split(', ')]


def find_group(links, house, group=None):
    # type: (dict, int, Optional[set]) -> list
    group = group or set()

    if house not in group:
        group.add(house)

    for neighbour in links[house]:
        if neighbour not in group:
            group = group.union(find_group(links, neighbour, group))

    return group


# Part 1
res = find_group(data, 0, set())
print(str(len(res)))


# Part 2
n_sets = 0
remainders = set(data.keys())
while remainders:
    remainders.difference_update(find_group(data, next(iter(remainders))))
    n_sets += 1

print(str(n_sets))
