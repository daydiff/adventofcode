import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
numbers = list(map(int, data.split(",")))
r = int("inf")

for g in range(min(numbers), max(numbers) + 1):
    s = 0
    for n in numbers:
        s += abs(n - g)
    r = min(r, s)

print(r)
