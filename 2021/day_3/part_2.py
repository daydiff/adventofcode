import os

class Solution:
    def solve(self, items: list) -> int:

        def mostcommon(items: list, start_bit: int):
            l = len(items[0]) - start_bit
            counters = [0] * len(items[0])
            size = len(items)

            for number in items:
                for i in range(l):
                    j = i + start_bit
                    counters[j] += int(number[j], 2)

            gamma = [0] * len(items[0])
            for i in range(len(counters)):
                if counters[i] >= size / 2:
                    gamma[i] = 1

            gamma = ''.join(str(n) for n in gamma)
            epsilon = int(gamma, 2)  ^ int('1' * l, 2)

            return gamma, format(epsilon, '012b')

        def common_number(items: list, direction: int, bit: int) -> str:
            most, least = mostcommon(items, bit)
            if 0 == direction:
                return most
            return least

        def reduce(items: list, direction: int) -> str:
            bit = 0
            while 1:
                if 1 == len(items):
                    return items[0]

                common = common_number(items, direction, bit)

                new_items = []
                for item in items:
                    if common[bit] == item[bit]:
                        new_items.append(item)
                items = new_items
                bit += 1

            return ''

        oxygen = reduce(items, 0)
        co2 = reduce(items, 1)

        return int(oxygen, 2) * int(co2, 2)

## read input
items = []

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

with open(os.path.join(__location__, 'input'), "r") as file:
    for line in file:
        items.append(line.rstrip())

s = Solution()
r = s.solve(items)
print(r)
