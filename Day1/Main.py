import re

file = open("input.txt")
all_lines = file.read().splitlines()
file.close()

#  Part 1
sum = 0
for line in all_lines:
    digits = "".join(char for char in line if char.isdigit())
    number = int(digits[0] + digits[-1])
    sum += number
print(sum)


#  Part 2
sum2 = 0
words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

test = """two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen"""
#all_lines = test.split()
for line in all_lines:
    for word, val in words.items():
        line = line.replace(word, word[0] + str(val) + word[-1])

    digits = "".join(char for char in line if char.isdigit())
    #print(line, "\t", line, "\t")
    number = int(digits[0] + digits[-1])
    sum2 += number
print(sum2)