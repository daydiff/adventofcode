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

# maybe even better f = lambda n: n * (n + 1) // 2
def f(n: int) -> int:
    return n * (n + 1) // 2

for pos in range(min(numbers), max(numbers) + 1):
    s = sum(f(abs(n - pos)) for n in numbers)
    r = min(r, s)

print(r)
