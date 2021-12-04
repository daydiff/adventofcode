import os

class Board:
    def __init__(self) -> None:
        self.map = {}
        self.brd = [0] * 25
    
    def add(self, n: int, idx: int) -> None:
        self.map[n] = idx
        self.brd[idx] = n
    
    def draw(self, n: int) -> bool:
        if n not in self.map:
            return False

        idx = self.map[n]
        self.brd[idx] = -1

        # check horizontal match
        for i in range(5):
            if self.brd[i*5] == -1 and self.brd[i*5+1] == -1 and self.brd[i*5+2] == -1 and self.brd[i*5+3] == -1 and self.brd[i*5+4] == -1:
                return True
            if self.brd[i] == -1 and self.brd[i+5] == -1 and self.brd[i+10] == -1 and self.brd[i+15] == -1 and self.brd[i+20] == -1:
                return True
        
        return False

    def score(self) -> int:
        score = 0
        
        for i in range(25):
            if self.brd[i] != -1:
                score += self.brd[i]
        return score



class Solution:
    def solve(self, nums: list, boards: list) -> int:
        nb = len(boards)
        winners = set()

        for n in nums:
            for i in range(nb):
                if i in winners:
                    continue

                b = boards[i]
                if b.draw(n):
                    winners.add(i)
                if len(winners) == nb:
                    return n * b.score()

        return -1

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## parse input
data = data.split("\n\n")
nums = list(map(int, data[0].split(",")))

boards = []
for b in data[1:]:
    board = Board()
    i = 0
    for line in b.splitlines():
        j = 0
        for n in list(map(int, line.split())):
            board.add(n, i*5+j)
            j += 1
        i += 1
    boards.append(board)

s = Solution()
r = s.solve(nums, boards)
print(r)