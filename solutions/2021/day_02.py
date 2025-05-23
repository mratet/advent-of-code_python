from aocd import get_data, submit

input = get_data(day=2, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    depth = 0
    horizontal_pos = 0
    for line in lines:
        move, X = line.split()
        X = int(X)
        if move == "forward":
            horizontal_pos += X
        elif move == "down":
            depth += X
        elif move == "up":
            depth -= X
    return depth * horizontal_pos


def part_2(lines):
    depth = 0
    horizontal_pos = 0
    aim = 0
    for line in lines:
        move, X = line.split()
        X = int(X)
        if move == "forward":
            horizontal_pos += X
            depth += aim * X
        elif move == "down":
            aim += X
        elif move == "up":
            aim -= X
    return depth * horizontal_pos


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
