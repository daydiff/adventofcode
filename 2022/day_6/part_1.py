import os

from collections import deque

## read input
result = 0
q = deque()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        for i in range(len(line)):
            q.append(line[i])
            if len(q) == 4:
                if len(set(q)) == 4:
                    print(i + 1)
                    exit
                else:
                    q.popleft()
        
