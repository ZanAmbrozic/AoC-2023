from collections import OrderedDict, defaultdict

file = open("input.txt")
line = file.readline()
file.close()


#  Part 1

total = 0
current_value = 0
for char in line.replace("\n", ","):
    if char == ",":
        total += current_value
        current_value = 0
        continue

    current_value += ord(char)
    current_value *= 17
    current_value %= 256

print(total)


#  Part 2

def hash_string(string):
    c = 0
    return [c := ((c + ord(char)) * 17) % 256 for char in string][-1]


boxes = defaultdict(OrderedDict)
for step in line.strip().split(","):
    c = "=" if "=" in step else "-"
    label, *num = step.split(c)
    hash_val = hash_string(label)

    if c == "=":
        num = int(num[0])
        boxes[hash_val][label] = num

    else:
        boxes[hash_val].pop(label, None)

print(boxes)


total = 0

for box_num, box in boxes.items():
    total += sum((box_num + 1) * item_index * int(item)
                 for item_index, item in enumerate(box.values(), start=1))


print(total)


