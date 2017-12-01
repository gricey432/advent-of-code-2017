"""
http://adventofcode.com/2017/day/1
"""
with open('1.in', 'r') as f:
    sequence = f.read().strip()

size = len(sequence)
res = sum(
    int(sequence[i])
    for i in range(size)
    if sequence[i] == sequence[(i + size / 2) % size]
)

print(str(res))
