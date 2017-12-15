"""
http://adventofcode.com/2017/day/9
"""

with open('9.in', 'r') as f:
    data = f.read().strip()

score = 0
depth = 0
garbage_count = 0
in_junk = False
ignored = False

for c in data:
    if ignored:
        ignored = False
    elif c == '!':
        ignored = True
    elif in_junk:
        if c == '>':
            in_junk = False
        else:
            garbage_count += 1
    elif c == '<':
        in_junk = True
    elif c == '{':
        depth += 1
    elif c == '}':
        if depth:
            score += depth
            depth -= 1

print(str(score))
print(str(garbage_count))
