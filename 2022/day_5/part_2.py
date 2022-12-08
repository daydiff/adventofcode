import os

## read input
result = 0
size = 0
stacks = []
indices = [] 

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        line = line.strip("\n")

        if size == 0:
            size = (len(line) + 1) // 4
            idx = 1
            for i in range(size):
                stacks.append([])
                indices.append(idx)
                idx = idx + 4
        
        if line == '':
            for k, v in enumerate(stacks):
                stacks[k].reverse()
            continue
        if line[1] == '1':
            continue
        
        if line[0] == 'm':
            moves = line.split(' ')
            cnt = int(moves[1])
            src = int(moves[3]) - 1
            dst = int(moves[5]) - 1
            stacks[dst] = stacks[dst] + stacks[src][-cnt:]
            stacks[src] = stacks[src][:-cnt]
        else:
            for k, v in enumerate(indices):
                if line[v] != ' ':
                    stacks[k].append(line[v])

result = []
for i, v in enumerate(stacks):
    result.append(v.pop())

print(''.join(result))