from itertools import pairwise


def get_element(line, sum):
    if all(e == 0 for e in line):
        return 0
    return line[-1] + get_element([curr - prev for prev, curr in pairwise(line)], sum)


#  Part 1

total = 0
for line in open("input.txt"):
    int_list = list(map(int, line.split()))
    total += get_element(int_list, 0)

print(total)


# Part 2

total = 0
for line in open("input.txt"):
    int_list = list(reversed(list(map(int, line.split()))))
    total += get_element(int_list, 0)

print(total)
