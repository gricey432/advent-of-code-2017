"""
http://adventofcode.com/2017/day/16
"""
from string import ascii_lowercase

fist_16_alpha = list(ascii_lowercase[:16])

with open('16.in', 'r') as f:
    instructions = f.read().strip().split(',')

# Apply the movements until a loop is found
programs = fist_16_alpha.copy()
pattern = []
while True:
    pattern.append(''.join(programs))
    for instr in instructions:
        if instr.startswith('s'):
            n = int(instr[1:])
            programs = programs[-n:] + programs[:-n]
        else:
            f = int if instr.startswith('x') else programs.index
            a, b = map(f, instr[1:].split('/'))
            programs[a], programs[b] = programs[b], programs[a]
    if programs == fist_16_alpha:
        break

print(pattern[1])
print(pattern[1000000000 % len(pattern)])
