"""
http://adventofcode.com/2017/day/8
"""
import re
from collections import defaultdict
from operator import gt, ge, lt, le, eq, ne


OPERATORS = {
    '==': eq,
    '!=': ne,
    '>=': ge,
    '>': gt,
    '<=': le,
    '<': lt,
}

pattern_instr = r"(\S+?) (\S+?) (\S+?) if (\S+?) (\S+?) (\S+?)$"


with open('8.in', 'r') as f:
    data = [l.strip() for l in f]


registers = defaultdict(lambda: 0)
highest_ever = 0  # Part 2
for line in data:
    match = re.match(pattern_instr, line)
    register = match.group(1)
    method = match.group(2)
    delta = int(match.group(3))
    condition_register = match.group(4)
    condition_operator = match.group(5)
    condition_value = int(match.group(6))

    condition_operation = OPERATORS[condition_operator]
    condition_register_value = registers[condition_register]

    if condition_operation(condition_register_value, condition_value):
        if method == "inc":
            registers[register] += delta
        else:
            registers[register] -= delta

        highest_ever = max(highest_ever, registers[register])

print(str(max(registers.values())))
print(str(highest_ever))
