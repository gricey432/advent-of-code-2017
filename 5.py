"""
http://adventofcode.com/2017/day/5
"""

with open('5.in', 'r') as f:
    instructions = [int(l.strip()) for l in f]
n_instructions = len(instructions)


# Part 1
instructions_1 = instructions.copy()
counter = 0
cursor = 0
while 0 <= cursor < n_instructions:
    instr = instructions_1[cursor]
    instructions_1[cursor] += 1
    cursor += instr
    counter += 1

print(str(counter))


# Part 2
instructions_2 = instructions.copy()
counter = 0
cursor = 0
while 0 <= cursor < n_instructions:
    instr = instructions_2[cursor]
    instructions_2[cursor] += (-1 if instr >= 3 else 1)
    cursor += instr
    counter += 1

print(str(counter))
