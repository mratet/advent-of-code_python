from aocd import get_data

input = get_data(day=16, year=2017).splitlines()


# WRITE YOUR SOLUTION HERE
def parse(line):
    instructions = []
    for inst in line.split(","):
        if inst[0] == "s":
            instructions.append(("s", int(inst[1:])))
        elif inst[0] == "x":
            a, b = map(int, inst[1:].split("/"))
            instructions.append(("x", a, b))
        else:
            instructions.append(("p", inst[1], inst[3]))
    return instructions


def dance(programs, instructions):
    for inst in instructions:
        if inst[0] == "s":
            idx = 16 - inst[1]
            programs = programs[idx:] + programs[:idx]
        elif inst[0] == "x":
            programs[inst[1]], programs[inst[2]] = programs[inst[2]], programs[inst[1]]
        else:
            idx1, idx2 = programs.index(inst[1]), programs.index(inst[2])
            programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
    return programs


def solve(lines):
    programs = list("abcdefghijklmnop")
    instructions = parse(lines[0])

    initial = programs[:]
    programs = dance(programs, instructions)
    first_dance = "".join(programs)
    cycle = 1
    while programs != initial:
        programs = dance(programs, instructions)
        cycle += 1

    # It happens to be a perfect cycle so a modulo is enough
    for _ in range(1_000_000_000 % cycle):
        programs = dance(programs, instructions)
    return first_dance, "".join(programs)


def part_1(lines):
    p1, _ = solve(lines)
    return p1


def part_2(lines):
    _, p2 = solve(lines)
    return p2


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
