import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
m = {}

for vec in data.splitlines():
    l, r = vec.split(" -> ")
    x1, y1 = map(int, l.split(","))
    x2, y2 = map(int, r.split(","))

    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                m[(x, y)] = m.get((x, y), 0) + 1
s = 0
for x in m.values():
    if x > 1:
        s += 1

print(s)
