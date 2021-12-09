import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
sum = 0
i = []

for l in data.splitlines():
    i.append(list(map(int, list(l))))

rows = len(i)
cols = len(i[0])

for row in range(rows):
    for col in range(cols):
        # left
        if col > 0 and i[row][col - 1] <= i[row][col]:
            continue
        # top
        if row > 0 and i[row - 1][col] <= i[row][col]:
            continue
        # right
        if col < cols - 1 and i[row][col + 1] <= i[row][col]:
            continue
        # bottom
        if row < rows - 1 and i[row + 1][col] <= i[row][col]:
            continue
        sum += 1 + i[row][col]

print(sum)