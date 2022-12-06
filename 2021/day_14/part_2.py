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
pmap = {}
for l in rules.splitlines():
    rule, ins = l.split(" -> ")
    pmap[rule] = ins

pairs = {}

for i in range(len(poly) - 1):
    pairs.append(poly[i:i + 2])



min_t = float("Inf")
max_t = 0


print("END")

# NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# 