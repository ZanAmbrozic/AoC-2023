
#  Part 1

total = 0
colors = {"red": 12, "green": 13, "blue": 14}

for line in open("input.txt"):
    game_id, attempts = line.split(": ")
    game_id = int(game_id[5:])
    attempts = attempts.replace(";", ",").replace("\n", "").split(", ")

    if all(colors[attempt.split()[1]] >= int(attempt.split()[0]) for attempt in attempts):
        total += game_id
#print(total)


#  Part 2

total = 0

for line in open("input.txt"):
    colors = {"red": 0, "green": 0, "blue": 0}

    *_, attempts = line.split(": ")
    attempts = attempts.replace(";", ",").replace("\n", "").split(", ")
    for attempt in attempts:
        num, clr = attempt.split()
        if colors[clr] < int(num):
            colors[clr] = int(num)

    res = 1
    for val in colors.values():
        res *= val
    total += res


print(total)



