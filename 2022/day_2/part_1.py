import os

## read input
shape_map = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

shape_weights = {
    'A': 1,
    'B': 2,
    'C': 3,
}

outcomes = {
    'A A': 3,
    'B B': 3,
    'C C': 3,
    'A B': 6,
    'A C': 0,
    'B A': 0,
    'B C': 6,
    'C A': 6,
    'C B': 0,
}

result = 0

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        l, r = line.rstrip("\n").split(' ')
        r = shape_map[r]
        round = l + ' ' + r
        result = result + outcomes[round] + shape_weights[r]

print(result)
