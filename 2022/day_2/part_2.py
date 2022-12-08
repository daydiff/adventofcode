import os

## read input
shape_weights = {
    'A': 1,
    'B': 2,
    'C': 3,
}

outcomes = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

transition = {
    'Y': {
        'A': 'A',
        'B': 'B',
        'C': 'C',
    },
    'Z': {
        'A': 'B',
        'B': 'C',
        'C': 'A',
    },
    'X': {
        'A': 'C',
        'B': 'A',
        'C': 'B',
    },
}

result = 0

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        l, r = line.rstrip("\n").split(' ')
        mine = transition[r][l]
        result = result + outcomes[r] + shape_weights[mine]

print(result)
