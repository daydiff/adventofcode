import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
i = []
for l in data.splitlines():
    i.append(list(map(int, list(l))))

rows = len(i)
cols = len(i[0])
basins = []

# dfs
def basin(r: int, c: int, graph: list, visited: set) -> int:
    if (r, c) in visited: return 0    
    if r < 0 or r == len(graph) or c < 0 or c == len(graph[0]): return 0    
    if graph[r][c] == 9: return 0
    
    visited.add((r, c))
    size = 1
    for i, j in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
        size += basin(i, j, graph, visited)

    return size


for r in range(rows):
    for c in range(cols):
        # left
        if c > 0 and i[r][c - 1] <= i[r][c]:
            continue
        # top
        if r > 0 and i[r - 1][c] <= i[r][c]:
            continue
        # right
        if c < cols - 1 and i[r][c + 1] <= i[r][c]:
            continue
        # bottom
        if r < rows - 1 and i[r + 1][c] <= i[r][c]:
            continue
        # calc basin size
        basins.append(basin(r, c, i, set()))

basins.sort()

print(basins[-1] * basins[-2] * basins[-3])