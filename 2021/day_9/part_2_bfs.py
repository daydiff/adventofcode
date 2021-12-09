import os
from collections import deque

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
lines = []
for l in data.splitlines():
    lines.append(list(map(int, list(l))))

rows = len(lines)
cols = len(lines[0])
basi = []
visi = set()

for r in range(rows):
    for c in range(cols):
        if lines[r][c] == 9: continue
        if (r, c) in visi: continue

        q = deque()
        q.append((r, c))
        visi.add((r, c))
        size = 1

        while q:
            i, j = q.popleft()
            for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= x < rows and 0 <= y < cols:
                    if (x, y) in visi: continue
                    if lines[x][y] != 9:
                        q.append((x, y))
                        visi.add((x, y))
                        size += 1
        basi.append(size)

basi.sort()

print(basi[-1] * basi[-2] * basi[-3])