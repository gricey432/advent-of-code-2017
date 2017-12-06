"""
http://adventofcode.com/2017/day/6

Part 1 and 2 are so similar here that I've just done 1 file with 2 outputs
"""
from __future__ import division

with open('6.in', 'r') as f:
    banks = tuple([int(n) for n in f.read().strip().split('\t')])

n_banks = len(banks)
history = []
counter = 0
while banks not in history:
    counter += 1
    history.append(banks)
    i_high = banks.index(max(banks))
    i_next = (i_high + 1) if i_high + 1 < n_banks else 0
    val_high = banks[i_high]

    add_all = val_high // n_banks
    rem = val_high % n_banks
    bonus = [0] + [1] * rem + [0] * (n_banks - rem - 1)
    bonus = bonus[-i_high:] + bonus[:-i_high]

    banks = tuple([
        (0 if i == i_high else banks[i]) + add_all + bonus[i]
        for i in range(n_banks)
    ])

print(str(counter))  # Part 1
print(str(counter - history.index(banks)))  # Part 2
