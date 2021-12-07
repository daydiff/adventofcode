import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
pack = list(map(int, data.split(",")))

for i in range(256):
    for j in range(len(pack)):
        if pack[j] == 0:
            pack.append(8)
            pack[j] = 6
        else:
            pack[j] -= 1

print(len(pack))
