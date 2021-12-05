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
    dx = x2 - x1
    dy = y2 - y1
    
    if dx: dx = dx // abs(dx)
    if dy: dy = dy // abs(dy)

    x = x1
    y = y1
    while True:
        m[(x, y)] = m.get((x, y), 0) + 1
        if x == x2 and y == y2:
            break
        x += dx
        y += dy

s = 0
for x in m.values():
    if x > 1:
        s += 1

print(s)
