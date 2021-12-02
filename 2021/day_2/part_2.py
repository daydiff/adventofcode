import os

class Solution:
    def solve(self, commands: list) -> int:
        depth = 0
        pos = 0
        aim = 0

        for cmd in commands:
            command, step = cmd.split(' ')
            step = int(step)

            if 'forward' == command:
                pos += step
                depth += aim * step
            if 'down' == command:
                aim += step
            if 'up' == command:
                aim -= step

        return pos * depth

## read input
commands = []

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        commands.append(line)

s = Solution()
r = s.solve(commands)
print(r)
