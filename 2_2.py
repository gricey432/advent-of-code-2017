"""
http://adventofcode.com/2017/day/2
"""
with open('2.in', 'r') as f:
    data = [
        [int(n) for n in row.strip().split('\t')]
        for row in f
    ]

res = sum(
    x / y
    for row in data
    for x in row
    for y in row
    if x % y == 0 and x != y
)

print(str(res))
