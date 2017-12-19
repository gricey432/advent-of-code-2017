"""
http://adventofcode.com/2017/day/7
"""
import re
from collections import Counter
from typing import Optional


pattern = r'(\w+) \((\d+)\) ?-?>? ?(.+)?'


class Program(object):
    name = None
    weight = None
    children = None

    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self.children = children or []


programs = dict()
with open('7.in', 'r') as f:
    for l in f:
        match = re.match(pattern, l)
        children_string = match.group(3)
        children = children_string.split(', ') if children_string else None
        programs[match.group(1)] = Program(match.group(1), int(match.group(2)), children)


# Part 1
# Just have to find one with no children who itself isn't a child of anything
# Topological sort is overkill
potentials = set(programs.keys())
for program in programs.values():
    if not program.children:
        # This is a leaf node
        if program.name in potentials:
            potentials.remove(program.name)
    else:
        for child in program.children:
            if child in potentials:
                potentials.remove(child)

root = potentials.pop()
print(root)


# Part 2
def weight(program):
    # type: (Program) -> int
    return program.weight + sum(weight(programs[c]) for c in program.children)


def traverse(program, desired_total_weight):
    # type: (Program, Optional[int]) -> int
    """
    The tree is unbalanced, traverse down the unbalanced path until you find the culprit
    """
    child_weights = {
        child: weight(programs[child])
        for child in program.children
    }
    counted_weights = Counter(child_weights.values())
    if len(counted_weights.values()) > 1:
        # Unbalanced children
        desired_weight = counted_weights.most_common(1)[0][0]
        odd_weight = counted_weights.most_common()[-1:][0][0]
        for child, child_weight in child_weights.items():
            if child_weight == odd_weight:
                return traverse(programs[child], desired_weight)

    else:
        # This node has all balanced children (or no children), therefore it is has the wrong weight
        return desired_total_weight - sum(child_weights.values())


print(str(traverse(programs[root], None)))
