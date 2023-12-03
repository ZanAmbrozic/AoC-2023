import re

file = open("input.txt")
all_lines = file.read().splitlines()
file.close()


def numbers_from_line(line):
    return [(m.start(), m.end() - 1) for m in re.finditer(r"\d+", line)]


coordinates = {}
for index_line, line in enumerate(all_lines):
    numbers = numbers_from_line(line)
    coordinates |= {(index_line, x1, x2): line[x1:x2+1] for x1, x2 in numbers}

# print(coordinates)

#  Part 1
total = 0
for line_index, line in enumerate(all_lines):
    for index, symbol in enumerate(line):
        if symbol.isdigit() or symbol == '.':
            continue

        total += sum([int(num) for (y, x1, x2), num in coordinates.items()
                      if line_index + 1 == y and x1 - 1 <= index <= x2 + 1
                      or line_index - 1 == y and x1 - 1 <= index <= x2 + 1
                      or line_index == y and x2 + 1 == index
                      or line_index == y and x1 - 1 == index
                      ])
print(total)


#  Part 2
total = 0
for line_index, line in enumerate(all_lines):
    for index, symbol in enumerate(line):
        if not symbol == '*':
            continue

        numbers = [int(num) for (y, x1, x2), num in coordinates.items()
                   if line_index + 1 == y and x1 - 1 <= index <= x2 + 1
                   or line_index - 1 == y and x1 - 1 <= index <= x2 + 1
                   or line_index == y and x2 + 1 == index
                   or line_index == y and x1 - 1 == index
                   ]
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]

print(total)
