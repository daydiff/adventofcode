import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
digits = []
cnt = 0

for line in data.splitlines():
    _, l = line.split(" | ")
    for n in l.split():
        if len(n) in [2,3,4,7]:
            cnt += 1

print(cnt)