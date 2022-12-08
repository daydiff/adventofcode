import os

## read input
result = 0
prev = []

def does_overlap(a: list, b: list) -> int:
    if a[0] > b[0]:
        a, b = b, a

    if a[0] <= b[0] <= a[1]:
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

        result = result + does_overlap(a, b)

print(result)
