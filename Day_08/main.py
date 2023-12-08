import math
from functools import reduce

instructions = None
directions = dict(L=0, R=1)
map = {}

for line in open("input.txt"):
    if instructions is None:
        instructions = line.strip()
        continue

    if not line.strip():
        continue

    point, instruction = line.strip().split(" = ")
    l, r = instruction.strip("()").split(", ")
    map[point] = (l, r)

for k, e in map.items():
    print(k + ":", e)


#  Part 1

current = "AAA"
total = 0
i = 0
while True:
    instruction = instructions[i]
    total += 1
    current = map[current][directions[instruction]]
    if current == "ZZZ":
        break

    i += 1
    if i == len(instructions):
        i = 0

print(total)


#  Part 2

def get_first_value(c):
    current = c
    total = 0
    i = 0
    while True:
        instruction = instructions[i]
        total += 1
        current = map[current][directions[instruction]]
        if current[2] == "Z":
            break

        i += 1
        if i == len(instructions):
            i = 0
    return total


def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)


currentt = [x1 + x2 + x3 for x1, x2, x3 in map if x3 == "A"]
first_values = [get_first_value(current) for current in currentt]

total = lcm(first_values)

print(total)
