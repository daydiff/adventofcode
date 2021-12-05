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
            elif abs(vec[0][0] - vec[1][0]) == abs(vec[0][1] - vec[1][1]):
                x1 = vec[0][0]
                x2 = vec[1][0]
                x_op = 1 if x1 < x2 else -1
                stop = x2+1 if x1 < x2 else x2-1
                y1 = vec[0][1]
                y2 = vec[1][1]
                y_op = 1 if y1 < y2 else -1

                while x1 != stop:
                    d[x1][y1] += 1
                    x1 += x_op
                    y1 += y_op
                
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
