import os
from collections import deque
from posixpath import abspath
from typing import DefaultDict, List, Tuple

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve

def printm(matrix: List[str]):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][i], end="")
        print("")

def split(m: List[str], edge: str, fold: int):
    if edge == "x":
        return (m[:fold], m[fold + 1:])

    a = [["."] * fold for _ in range(len(m))]
    b = [["."] * (len(m[0]) - fold) for _ in range(len(m))]
    for i in range(len(m)): # another bug - used a manual copy and there's was a bug
        a[i] = m[i][:fold]
        b[i] = m[i][fold + 1:]
    return (a, b)

t = 0
matrix = []
coords = []
folds = []
xl = 0
yl = 0

for l in data.splitlines():
    if l == "":
        continue
    elif l.startswith("fold"):
        edge, coord = l.strip("fold along ").split("=")
        folds.append((edge, int(coord)))
    else:
        x, y = map(int, l.split(","))
        xl = max(xl, x)
        yl = max(yl, y)
        coords.append((x, y))
xl += 1
yl += 1

matrix = [["."] * yl for _ in range(xl)]

for x, y in coords:
    matrix[x][y] = "#"

for edge, coord in folds:
    a, b = split(matrix, edge, coord)
    if edge == "x":
        if len(a) < len(b):
            for i in range(len(a)):
                for j in range(len(a[0])):
                    if a[i][j] == "#":
                        sub = len(a) - 1
                        b[sub - i][j] = a[i][j] # first bug - used reminder % (a wrong formula calculated) (same for edege y)
            matrix = b
        else:
            for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j] == "#":
                        sub = len(a) - 1 # second bug - used len(b) (same for edge y)
                        a[sub - i][j] = b[i][j]
            matrix = a
    else:
        if len(a[0]) < len(b[0]):
            for i in range(len(a)):
                for j in range(len(a[0])):
                    if a[i][j] == "#":
                        sub = len(a[0]) - 1
                        b[i][sub - j] = a[i][j]
            matrix = b
        else:
            for i in range(len(b)):
                for j in range(len(b[0])):
                    if b[i][j] == "#":
                        sub = len(a[0]) - 1
                        a[i][sub - j] = b[i][j]
            matrix = a

printm("result")
printm(matrix)