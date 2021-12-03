import os

class Solution:
    def solve(self, items: list) -> int:
        l = len(items[0])
        counters = [0] * l
        size = len(items)

        for number in items:
            for i in range(l):
                counters[i] += int(number[i], 2)

        gamma = [0] * l
        for i in range(len(counters)):
            if counters[i] > size / 2:
                gamma[i] = 1

        gamma = int(''.join(str(n) for n in gamma), 2)
        epsilon = gamma ^ int('1' * l, 2)

        return gamma * epsilon

## read input
items = []

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        items.append(line.rstrip())

s = Solution()
r = s.solve(items)
print(r)
