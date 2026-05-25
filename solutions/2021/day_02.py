from aocd import get_data

input = get_data(day=2, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def parse(line):
    move, x = line.split()
    return move, int(x)


def part_1(lines):
    depth, horizontal_pos = 0, 0
    deltas = {"forward": (1, 0), "down": (0, 1), "up": (0, -1)}
    for line in lines:
        move, x = parse(line)
        dh, dd = deltas[move]
        horizontal_pos += dh * x
        depth += dd * x
    return depth * horizontal_pos


def part_2(lines):
    depth, horizontal_pos, aim = 0, 0, 0
    for line in lines:
        move, x = parse(line)
        if move == "forward":
            horizontal_pos += x
            depth += aim * x
        elif move == "down":
            aim += x
        elif move == "up":
            aim -= x
    return depth * horizontal_pos


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
