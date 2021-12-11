import os
from collections import deque

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
t = 0
grid = []
for l in data.splitlines():
    grid.append(list(map(int, list(l))))

while True:
    t += 1
    flashed = set()
    q = deque()

    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] += 1
            if grid[i][j] > 9:
                q.append((i, j))
                flashed.add((i, j))
    while q:
        i, j = q.pop()
        for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            x, y = i + di, j + dj
            if 0 <= x < len(grid) and 0 <= y < len(grid):
                if (x, y) in flashed: continue
                grid[x][y] += 1
                if grid[x][y] > 9:
                    q.append((x, y))
                    flashed.add((x, y))
    if 100 == len(flashed):
        break
    for i, j in flashed:
        grid[i][j] = 0
        

print(t)
