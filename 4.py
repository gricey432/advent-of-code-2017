"""
http://adventofcode.com/2017/day/4
"""

with open('4.in', 'r') as f:
    data = [l.strip().split(' ') for l in f]


# Part 1
res = sum(1 for l in data if len(l) == len(set(l)))
print(str(res))


# Part 2
data = [[''.join(sorted(w)) for w in l] for l in data]
res = sum(1 for l in data if len(l) == len(set(l)))
print(str(res))
