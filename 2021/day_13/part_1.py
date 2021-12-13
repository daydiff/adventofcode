import os
from collections import deque
from posixpath import abspath
from typing import DefaultDict

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
t = 0
coords = set()
folds = []
xs = 0
ys = 0

for l in data.splitlines():
    if l == "":
        continue
    elif l.startswith("fold"):
        edge, coord = l.strip("fold along ").split("=")
        folds.append((edge, int(coord)))
    else:
        x, y = map(int, l.split(","))
        xs = max(xs, x)
        ys = max(ys, y)
        coords.add((x, y))

edge, coord = folds[0]

for d in coords.copy():
    if edge == "x" and d[0] > coord:
        coords.remove(d)
        x, y = abs(xs - d[0]), d[1]
        if (x, y) in coords: continue
        else: coords.add((x, y))
    if edge == "y" and d[1] > coord:
        coords.remove(d)
        x, y = (d[0], abs(ys - d[1]))
        if (x, y) in coords: continue
        else: coords.add((x, y))

print(len(coords))
