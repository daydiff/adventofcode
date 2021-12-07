import os

## read input
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)
with open(os.path.join(__location__, "input"), "r") as file:
    data = file.read()

## solve
pack = list(map(int, data.split(",")))
days = 256
cnt = len(pack)
memo = {}

def calc(timer: int, days: int) -> int:
    if 0 == days: return 0
    if (timer, days) in memo: return memo[(timer, days)]

    # made a stupid mistake here which I couldn't spot for hours
    # it was days = days - (timer + 1) and as a result I was storing incorrect number to memo
    ldays = days - (timer + 1)
    cnt = ldays // 7

    for i in range(0, cnt):
        idays = ldays - i * 7
        icnt = calc(8, idays)
        memo[(6, idays)] = icnt # another mistake was here (7 instead of 6) - but I spotted it fairly quickly today
        cnt += icnt

    memo[(timer, days)] = cnt + 1
    
    return cnt + 1


for timer in pack:
    cnt += calc(timer, days)

print(cnt)
