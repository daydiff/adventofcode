import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
numbers = list(map(int, data.split(",")))
r = float("inf")

dist = {}

cost = 0
for i in range(0, max(numbers) + 1):
    cost += i
    dist[i] = cost

for pos in range(min(numbers), max(numbers) + 1):
    s = 0
    for n in numbers:
        s += dist[abs(n - pos)]
    r = min(r, s)

print(r)
