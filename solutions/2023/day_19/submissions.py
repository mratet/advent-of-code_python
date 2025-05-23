lines = open("input.txt").read().splitlines()


# WRITE YOUR SOLUTION HERE
def mapping(instructions, entry):
    state = "in"
    while True:
        instruction = instructions[state]
        for cmd in instruction.split(","):
            next_state = cmd
            test = True
            if ":" in cmd:
                cond, next_state = cmd.split(":")
                if ">" in cond:
                    key, limit = cond.split(">")
                    test = entry[key] > int(limit)
                else:
                    key, limit = cond.split("<")
                    test = entry[key] < int(limit)

            if test:
                if next_state == "R":
                    return False
                if next_state == "A":
                    return True
                state = next_state
                break


def part_1(lines):
    i = 0
    instructions = {}
    while lines[i]:
        state, cond = lines[i].split("{")
        instructions[state] = cond[:-1]
        i += 1

    ans = 0
    for line in lines[i + 1 :]:
        line = line[1:-1]
        entry = {}
        values = line.split(",")
        for value in values:
            k, value = value.split("=")
            entry[k] = int(value)

        if mapping(instructions, entry):
            ans += sum([value for k, value in entry.items()])

    return ans


def part_2(lines):
    return 0


# END OF SOLUTION


test_input = open("input-test.txt").read().splitlines()
test_lines = []
for i, line in enumerate(test_input[3:]):
    if line and line[0] == "-":
        break
    test_lines.append(line)
solution = test_input[i + 4]

print(f"My answer on test set for the first problem is {part_1(test_lines)}")
print(solution)
print(f"My answer is {part_1(lines)}")

print(f"My answer on test set for the second problem is {part_2(test_lines)}")
print(f"My answer is {part_2(lines)}")
