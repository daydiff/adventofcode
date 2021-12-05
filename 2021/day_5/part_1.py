import os

class Solution:
    def solve(self, vecs: list) -> int:
        s = 0

        for vec in vecs:
            for p in vec:
                s = max(s, p[0], p[1])
        s += 1
        d = [[0]*s for _ in range(s)]

        for vec in vecs:
            if vec[0][0] == vec[1][0] or vec[0][1] == vec[1][1]:
                x1 = vec[0][0]
                x2 = vec[1][0]
                y1 = vec[0][1]
                y2 = vec[1][1]
                
                for i in range(min(x2, x1), max(x2, x1) + 1):
                    for j in range(min(y2, y1), max(y2, y1) + 1):
                        d[i][j] += 1

        cnt = 0
        for i in d:
            for j in i:
                if j > 1:
                    cnt += 1


        return cnt

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## parse input
data = data.splitlines()
data = [v.split(" -> ") for v in data]
vecs = []

for d in data:
    vecs.append([])
    for i in d:
        vecs[-1].append(list(map(int, i.split(","))))

s = Solution()
r = s.solve(vecs)
print(r)
