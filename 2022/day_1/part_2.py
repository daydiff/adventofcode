import os
import heapq

## read input
max_calories = []
cur_calories = 0

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        if line == "\n":
            heapq.heappush(max_calories, cur_calories)
            if len(max_calories) > 3:
                heapq.heappop(max_calories)
            cur_calories = 0
        else:
            cur_calories = cur_calories + int(line.strip("\n"))

print(sum(max_calories))
