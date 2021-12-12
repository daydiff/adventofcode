import os
from collections import deque
from posixpath import abspath

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
t = 0
graph = {}
for line in data.splitlines():
    l, r = line.split("-")
    if None == graph.get(l):
        graph[l] = set()
    if None == graph.get(r):
        graph[r] = set()
    graph[l].add(r)
    graph[r].add(l)

def find_path(graph: map, node: str, curr_path: list, visi: set) -> None:
    global paths

    if node in visi: return

    if node.islower():
        visi.add(node)

    curr_path.append(node)
    
    if node == "end":
        paths.append(curr_path)
        return    

    if node not in graph: return

    for n in graph[node]:
        find_path(graph, n, curr_path.copy(), visi.copy())

paths = []

find_path(graph, "start", [], set())

print(len(paths))
