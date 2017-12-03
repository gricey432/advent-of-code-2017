"""
http://adventofcode.com/2017/day/3
"""
from __future__ import division

square = 361527  # My personal input

# Figure out which layer it's on
layer = 0
while (1 + (layer * 2)) ** 2 < square:
    layer += 1

# Work out the start value of that layer
layer_end = (1 + (layer * 2)) ** 2
layer_size = layer * 2 + 1

# Add up the movements needed to the last element of that layer (positive is down and right)
x = y = layer

defecit = layer_end - square
if defecit:
    diff = min(defecit, layer_size - 1)
    x -= diff
    defecit -= diff
if defecit:
    diff = min(defecit, layer_size - 1)
    y -= diff
    defecit -= diff
if defecit:
    diff = min(defecit, layer_size - 1)
    x += diff
    defecit -= diff
if defecit:
    diff = min(defecit, layer_size - 1)
    y += diff
    defecit -= diff

res = abs(x) + abs(y)
print(str(res))
