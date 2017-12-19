"""
http://adventofcode.com/2017/day/19
"""
from string import ascii_uppercase

with open('19.in', 'r') as f:
    maze = [
        [
            c if c != " " else None
            for c in l
        ]
        for l in f
    ]


def directions(maze, x, y, current_dx, current_dy):
    # TODO I think this just happens to work for my particular input case. Code probably needs to check which direction is correct
    # Currently I think it could just turn onto a passing path on the wrong side
    if maze[y][x] == '+':
        if current_dx:
            yield 0, 1
            yield 0, -1
        else:
            yield 1, 0
            yield -1, 0
    else:
        yield current_dx, current_dy


x, y = next(i for i, c in enumerate(maze[0]) if c), 0  # Start at the first non-blank
dx, dy = 0, 1  # Start moving downward
seen = []
steps = 1  # Stepping onto the diagram
while True:
    for dx, dy in directions(maze, x, y, dx, dy):
        c = maze[y + dy][x + dx]
        if not c:
            continue
        elif c in ascii_uppercase:
            seen.append(c)
        x += dx
        y += dy
        steps += 1
        break
    else:
        break

print(''.join(seen))
print(steps)
