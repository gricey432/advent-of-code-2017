"""
http://adventofcode.com/2017/day/5
"""

with open('5.in', 'r') as f:
    instructions = [int(l.strip()) for l in f]

counter = 0
cursor = 0
while True:
    instr = instructions[cursor]
    instructions[cursor] += 1
    cursor += instr
    counter += 1
    if cursor < 0 or cursor >= len(instructions):
        break

print(str(counter))
