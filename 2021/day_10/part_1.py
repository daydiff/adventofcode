import os
from typing import Deque

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
score = 0
illeg = {}
braks = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}
weights = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

for l in data.splitlines():
    q = Deque()

    for c in list(l):
        if c in braks.keys(): q.append(c)
        if c in braks.values():
            if braks[q.pop()] != c:
                illeg[c] = illeg.get(c, 0) + 1
                break
print(illeg)
for c in illeg.keys():
    score += illeg[c] * weights[c]

print(score)