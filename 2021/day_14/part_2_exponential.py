import os
from collections import deque
from posixpath import abspath
from typing import DefaultDict, Generator

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
t = 0

poly, rules = data.split("\n\n")
rmap = {}
for l in rules.splitlines():
    rule, ins = l.split(" -> ")
    rmap[rule] = rule[0] + ins + rule[1]

def map_repl(poly: str) -> Generator:
    global rmap

    j = 0
    while j != len(poly) - 1:
        pair = poly[j:j + 2]

        if pair in rmap:
            poly = poly[0:j] + rmap[pair] + poly[j + 2:]
            j += 2
        else:
            j += 1
    yield poly

def repl(poly: str) -> Generator:
    global memo

    if len(poly) > 3:
        mid = len(poly) // 2
        l = repl(poly[0:mid])
        r = repl(poly[mid:])
        m = repl(poly[mid - 1:mid + 1])
        yield next(l) + next(m) + next(r)
    else:
        yield map_repl(poly)

for i in range(1, 41):
    poly = next(repl(poly))

    print("len(%d) => i(%d):" % (len(poly), i))

cnts = {}
for c in poly:
    cnts[c] = (cnts[c] if c in cnts else 0) + 1

min_t = float("Inf")
max_t = 0

for c in cnts:
    if cnts[c] > max_t:
        max_t = cnts[c]
    if cnts[c] < min_t:
        min_t = cnts[c]

print(max_t - min_t)

# NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
