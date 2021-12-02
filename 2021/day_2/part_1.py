import os

class Solution:
    def solve(self, commands: list) -> int:
        depth = 0
        pos = 0

        for cmd in commands:
            command, step = cmd.split(' ')
            step = int(step)

            if 'forward' == command:
                pos += step
            if 'down' == command:
                depth += step
            if 'up' == command:
                depth -= step

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
