"""
http://adventofcode.com/2017/day/7
"""
import re

pattern = r'(\w+) \((\d+)\) ?-?>? ?(.+)?'


class Program(object):
    name = None
    weight = None
    children = None

    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self.children = children or []


programs = []
with open('7.in', 'r') as f:
    for l in f:
        match = re.match(pattern, l)
        children_string = match.group(3)
        children = children_string.split(', ') if children_string else None
        programs.append(Program(match.group(1), int(match.group(2)), children))

# Topological sort
graph_sorted = []
graph_unsorted = programs[:]  # clone
while graph_unsorted:
    for node in graph_unsorted:

