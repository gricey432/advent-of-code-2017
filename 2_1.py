"""
http://adventofcode.com/2017/day/2
"""
with open('2.in', 'r') as f:
    data = [
        [int(n) for n in row.strip().split('\t')]
        for row in f
    ]

res = sum(max(vals) - min(vals) for vals in data)

print(str(res))
