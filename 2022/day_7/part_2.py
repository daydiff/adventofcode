import os

from collections import deque
from collections import defaultdict

## read input
result = 0
limit = 100000
dirs = defaultdict()
path = []

def process_cmd(line: str):
    global path

    if line[2:4] == 'ls':
        return
    
    _, _, dir = line.split(' ')
    
    if dir == '..':
        path.pop()
    else:
        path.append(dir)

def process_file(line: str):
    global dirs, path
    
    l, _ = line.split(' ')

    if l == 'dir':
        return
    
    curr = ''
    for dir in path:
        curr = curr + '/' + dir
        dirs[curr] = dirs.get(curr, 0) + int(l)


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        line = line.rstrip("\n")
        if line[0] == '$':
            process_cmd(line)
        else:
            process_file(line)

free_now = 70000000 - dirs.get('//')
req_more = 30000000 - free_now

smallest = 99999999

for size in dirs.values():
    if size >= req_more and size < smallest:
        smallest = size

print(smallest)
