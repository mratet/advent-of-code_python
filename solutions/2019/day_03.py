from aocd import get_data

input = get_data(day=3, year=2019).splitlines()

DIRECTIONS = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}


# WRITE YOUR SOLUTION HERE
def get_wire_path(insts):
    x, y = 0, 0
    path = []
    for inst in insts:
        op, val = inst[0], int(inst[1:])
        dx, dy = DIRECTIONS[op]
        for _ in range(val):
            x, y = x + dx, y + dy
            path.append((x, y))
    return path


def get_paths(lines):
    path_1 = get_wire_path(lines[0].split(","))
    path_2 = get_wire_path(lines[1].split(","))
    crossed_pos = set(path_1) & set(path_2)
    return path_1, path_2, crossed_pos


def part_1(lines):
    _, _, crossed_pos = get_paths(lines)
    return min(abs(x) + abs(y) for (x, y) in crossed_pos)


def part_2(lines):
    path_1, path_2, crossed_pos = get_paths(lines)
    return min(path_1.index(pos) + path_2.index(pos) + 2 for pos in crossed_pos)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
