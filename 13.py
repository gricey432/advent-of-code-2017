"""
http://adventofcode.com/2017/day/13
"""
import itertools
from collections import defaultdict
import re


def caught(scanners, layer, time):
    if scanners[layer]:
        return time % (2 * scanners[layer] - 2) == 0
    return False


pattern = r"(\d+): (\d+)"
scanners = defaultdict(lambda: None)
with open('13.in', 'r') as f:
    for l in f:
        match = re.match(pattern, l)
        scanners[int(match.group(1))] = int(match.group(2))

n_layers = max(scanners.keys())


# Part 1
print(sum(
    layer * scanners[layer]
    for layer in range(n_layers + 1)
    if caught(scanners, layer, layer)
))


# Part 2
# This is bad brute force, but whatever
delay = None  # Scopefix
for delay in itertools.count():
    for layer in range(n_layers + 1):
        time = layer + delay
        if caught(scanners, layer, time):
            break
    else:
        break
print(delay)
