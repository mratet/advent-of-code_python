from aocd import get_data
from intcode import IntcodeComputer, MAP_FROM_ASCII, MAP_TO_ASCII

aoc_input = get_data(day=17, year=2019)

N, S, E, W = (0, -1), (0, 1), (1, 0), (-1, 0)
DIRS = [N, E, S, W]

FACING = {"^": 0, "v": 2, ">": 1, "<": 3}


def parse_scaffold_view(camera_view):
    scaffolds, robot = [], None
    for y, line in enumerate(camera_view.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                scaffolds.append((x, y))
            if c in FACING:
                robot = (FACING[c], x, y)
    return scaffolds, robot


def get_full_program(lines):
    pc = IntcodeComputer(lines)
    camera_view = pc.run()
    scaffolds, robot = parse_scaffold_view(MAP_FROM_ASCII(camera_view))

    dir_id, px, py = robot
    path = []
    while True:
        cnt = 1
        dx, dy = DIRS[dir_id]
        while (px + dx, py + dy) in scaffolds:
            px, py = px + dx, py + dy
            cnt += 1
        path.append(cnt)

        right_turn = (dir_id + 1) % 4
        rx, ry = DIRS[right_turn]
        if (px + rx, py + ry) in scaffolds:
            dir_id = right_turn
            px, py = px + rx, py + ry
            path.append("R")
            continue

        left_turn = (dir_id - 1) % 4
        lx, ly = DIRS[left_turn]
        if (px + lx, py + ly) in scaffolds:
            dir_id = left_turn
            px, py = px + lx, py + ly
            path.append("L")
            continue

        return ",".join(map(str, path[1:]))


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    pc = IntcodeComputer(lines)
    camera_view = pc.run()
    scaffolds, _ = parse_scaffold_view(MAP_FROM_ASCII(camera_view))
    return sum(
        x * y
        for x, y in scaffolds
        if all(((x + dx, y + dy) in scaffolds) for dx, dy in DIRS)
    )


def part_2(lines):
    pc = IntcodeComputer(lines)
    pc.memory[0] = 2
    # Launch get_full_program if needed. Decomposition was made by hand
    decomposed_program = (
        "A,B,A,C,A,B,C,A,B,C\nR,12,R,4,R,10,R,12\nR,6,L,8,R,10\nL,8,R,4,R,4,R,6\nn\n"
    )
    *_, dust_collected = pc.run(MAP_TO_ASCII(decomposed_program))
    return dust_collected


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
