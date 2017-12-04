"""
http://adventofcode.com/2017/day/4
"""

with open('4.in', 'r') as f:
    data = [l.strip().split(' ') for l in f]

res = sum(1 for l in data if len(l) == len(set(l)))
print(str(res))
