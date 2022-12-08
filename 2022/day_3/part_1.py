import os

## read input
result = 0

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        line = line.rstrip("\n")
        length = len(line) // 2
        l, r = set(line[:length]), set(line[length:])
        common = l & r
        
        if len(common) == 0:
            continue
        
        common = common.pop()

        if common.isupper():
            curr = (ord(common) - ord('A') + 27)
        else:
            curr = (ord(common) - ord('a') + 1)

        result = result + curr
        
print(result)
