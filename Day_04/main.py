import math


#  Part 1

total = 0

for line in open("input.txt"):
    winning, yours = line.split(":")[1].split("|")
    exp = len(set(winning.split()) & set(yours.split()))
    total += math.floor(pow(2, exp - 1))

print(total)


#  Part 2

total = 0
totals = {}
i = 1
for line in open("input.txt"):
    winning, yours = line.split(":")[1].split("|")
    exp = len(set(winning.split()) & set(yours.split()))
    totals[i] = totals.get(i, 0) + 1

    for e in range(1, exp + 1):
        totals[i + e] = totals.get(i + e, 0) + 1 * totals[i]

    i += 1

total = sum(totals.values())
print(total)
