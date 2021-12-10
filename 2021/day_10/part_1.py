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
        if c in braks:
            q.append(c)
        elif braks[q.pop()] != c:
            score += weights[c]
            break

print(score)