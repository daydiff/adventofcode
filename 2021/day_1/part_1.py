import os

class Solution:
    def countIncreases(self, measurements: list) -> int:
        cnt = 0
        j = 0

        for i in range(1, len(measurements)):
            if measurements[j] < measurements[i]:
                cnt += 1
            j += 1

        return cnt

## read input
measurements = []

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        measurements.append(int(line))

s = Solution()
r = s.countIncreases(measurements)
print(r)
