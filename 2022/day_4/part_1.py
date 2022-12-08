import os

## read input
result = 0
prev = []

def fully_contains(a: list, b: list) -> int:
    size_a = a[1] - a[0]
    size_b = b[1] - b[0]

    if size_b > size_a:
        a, b = b, a

    if a[0] <= b[0] and a[1] >= b[1]:
        return 1
    else:
        return 0

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        line = line.rstrip("\n")
        pair = line.split(',')
        a, b = pair[0].split('-'), pair[1].split('-')
        a = [ int(a[0]), int(a[1]) ]
        b = [ int(b[0]), int(b[1]) ]

        result = result + fully_contains(a, b)

print(result)
