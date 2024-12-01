file = open("input.txt")
all_lines = file.read().splitlines()
file.close()


# Part 1

max_times = all_lines[0].split()[1:]
max_distances = all_lines[1].split()[1:]

total = 1
for max_time, max_distance in zip(max_times, max_distances):
    cnt = 0
    for time_held in range(0, int(max_time)):
        distance = (int(max_time) - time_held) * time_held
        if distance <= int(max_distance):
            continue
        cnt += 1
    total *= cnt

print(total)


# Part 2

max_time = all_lines[0].split(":")[1].replace(" ", "")
max_distance = all_lines[1].split(":")[1].replace(" ", "")

total = 1
# cnt = 0
"""for time_held in range(0, int(max_time)):
    distance = (int(max_time) - time_held) * time_held
    if distance <= int(max_distance):
        continue
    cnt += 1"""

total = sum(int(max_distance) < (int(max_time) - time_held) * time_held for time_held in range(0, int(max_time)))

#total = cnt
print(total)
