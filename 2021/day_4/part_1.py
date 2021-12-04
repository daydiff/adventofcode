import os

class Board:
    def __init__(self) -> None:
        self.map = {}
        self.nums = [0] * 25
        self.board = [0] * 25
    
    def add(self, n: int, idx: int) -> None:
        self.map[n] = idx
        self.nums[idx] = n
    
    def draw(self, n: int) -> bool:
        if n not in self.map:
            return False

        idx = self.map[n]
        self.board[idx] = 1

        # check horizontal match
        for i in range(5):
            if self.board[i*5] == 1 and self.board[i*5+1] == 1 and self.board[i*5+2] == 1 and self.board[i*5+3] == 1 and self.board[i*5+4] == 1:
                return True
            if self.board[i] == 1 and self.board[i+5] == 1 and self.board[i+10] == 1 and self.board[i+15] == 1 and self.board[i+20] == 1:
                return True
        
        return False

    def score(self) -> int:
        score = 0
        
        for i in range(25):
            if self.board[i] == 0:
                score += self.nums[i]
        return score



class Solution:
    def solve(self, nums: list, boards: list) -> int:
        nb = len(boards)
        winners = set()

        for n in nums:
            for i in range(nb):
                if i in winners:
                    continue

                board = boards[i]
                if board.draw(n):
                    winners.add(i)
                if len(winners) == nb:
                    return n * board.score()

        return -1

## read input
items = []

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, "input"), "r") as file:
    for line in file:
        items.append(line.rstrip())

## parse input
nums = [int(n) for n in items.pop(0).split(",")]
boards = []

board = Board()
items.pop(0)
row = 0
for line in items:
    if "" == line:
        boards.append(board)
        board = Board()
        row = 0
    else:
        
        line = line.strip(" ").replace("  ", " ")
        line_nums = line.split(" ")
        for i in range(5):
            n = int(line_nums[i].strip(" "))
            board.add(n, row*5+i)
        row += 1

s = Solution()
r = s.solve(nums, boards)
print(r)
