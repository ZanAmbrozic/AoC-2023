
instructions = {}
parts = []

found_seperator = False
glb = globals()
A, R = "AR"
for line in open("test.txt"):
    if not line or line == "\n":
        found_seperator = True
        continue

    if found_seperator is False:
        instruction, conditions = line.replace("}", "").strip().split("{")
        conditions = conditions.split(",")

        for i, condition in enumerate(conditions[:-1]):
            l, r = condition.split(":")
            conditions[i] = r + ":" + l

        conditions = " else ".join(conditions).replace(":", " if ")
        instructions[instruction] = conditions
        glb[instruction] = str(instruction)

        continue

    parts.append(line.strip("\n").strip("{}").replace(",", "\n"))


for i1, i2 in instructions.items():
    print(i1, " : ", i2)


#  Part 1

def test_instructions(instructions, xmas):
    instruction, conditions = "in", instructions["in"]
    x, m, a, s = xmas
    while True:
        jump = eval(conditions)

        if jump == "A" or jump == "R":
            return jump

        (instruction, conditions) = jump, instructions[jump]


total = 0
for part in parts:
    exec(part)
    evaluated = test_instructions(instructions, (x, m, a, s))
    if evaluated == "R":
        continue

    total += x + m + a + s

print(total)