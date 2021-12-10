import os
from typing import Deque

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
braks = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}
weights = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
scores = []

for l in data.splitlines():
    q = Deque()
    complete = True

    for c in list(l):
        if c in braks:
            q.append(c)
        elif braks[q.pop()] != c:
            break
    # didn't notice that I was counting illegal sequences as well
    # took ~10 to find it out
    else: # else executes if the loop completes normally (no break statement)
        acc = 0
        while q:
            c = q.pop()
            acc = acc * 5 + weights[braks[c]]
        scores.append(acc)

scores.sort()
mid = len(scores) // 2

print(scores[mid])
