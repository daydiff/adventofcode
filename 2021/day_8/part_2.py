import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
digits = []
sum = 0

def calcmap(digits: list) -> map:
    global m
    m = {}

    def getbylen(l: int, digits: list) -> list:
        r = []
        for i in digits:
            if l == len(i): r.append(i)
        return r
    
    one = getbylen(2, digits).pop()
    seven = getbylen(3, digits).pop()
    four = getbylen(4, digits).pop()
    eight = getbylen(7, digits).pop()
    m["a"] = set(seven).difference(set(one)).pop()
    print(one, seven, four, eight, m)

    for digit in getbylen(6, digits):
        i = set(digit).intersection(set(one))
        if 1 == len(i):
            six = digit
            m["f"] = i.pop()
            m["c"] = set(one).difference(set(m["f"])).pop()
            break
    diff = set(four).difference(set(one))
    print(diff)
    for digit in getbylen(6, digits):
        if 1 == len(diff.difference(set(digit))):
            m["d"] = diff.difference(set(digit)).pop()

    # m["d"] = diff.pop()
    m["b"] = set(four).difference(m.values()).pop()

    for digit in getbylen(6, digits):
        diff = set(digit).intersection(m.values())
        if 5 == len(diff):
            m["g"] = set(digit).difference(m.values()).pop()
            m["e"] = set("abcdefg").difference(m.values()).pop()
            break
    print("m", m)
    omap = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }

    nmap = {}

    x = lambda s: "a"


    for i in range(0, 10):
        arr = list(map(lambda x: m[x], list(omap[i])))
        arr.sort()
        print("arr", arr)
        digit = "".join(arr)
        nmap[digit] = str(i)

    return nmap

for line in data.splitlines():
    l, r = line.split(" | ")
    nmap = calcmap(l.split())
    
    number = ""
    for d in r.split():
        dig = list(d)
        dig.sort()
        print("dig", dig)
        number += nmap["".join(dig)]
    sum += int(number)

print(sum)