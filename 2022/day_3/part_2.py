import os

## read input
result = 0
group = []

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        line = line.rstrip("\n")
        group.append(line)

        if len(group) == 3:
            common = set(group[0]) & set(group[1]) & set(group[2])
            common = common.pop()
            
            if common.isupper():
                curr = (ord(common) - ord('A') + 27)
            else:
                curr = (ord(common) - ord('a') + 1)

            result = result + curr

            group = []
        
print(result)
