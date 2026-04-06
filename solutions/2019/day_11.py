from advent_of_code_ocr import convert_6
from aocd import get_data
from intcode import IntcodeComputer

aoc_input = get_data(day=11, year=2019)

# WRITE YOUR SOLUTION HERE
N, S, E, W = (0, 1), (0, -1), (1, 0), (-1, 0)
DIRS = [N, E, S, W]


def print_registration_identifier(grid: dict):
    white = [pos for pos, color in grid.items() if color]
    Xs, Ys = zip(*white, strict=False)
    min_x, max_x = min(Xs), max(Xs)
    min_y, max_y = min(Ys), max(Ys)
    return "\n".join(
        "".join("#" if (x, y) in white else "." for x in range(min_x, max_x + 1)) for y in range(max_y, min_y - 1, -1)
    )


def solve(lines, part="part_1"):
    pc = IntcodeComputer(lines)
    screen_state = {(0, 0): (0 if part == "part_1" else 1)}
    px, py = 0, 0
    direction = 0
    while True:
        output_buffer = pc.run([screen_state.get((px, py), 0)])
        if not output_buffer:
            break
        panel_color, turn = output_buffer
        screen_state[(px, py)] = panel_color
        direction = (direction + 1) % 4 if turn else (direction - 1) % 4
        dx, dy = DIRS[direction]
        px, py = px + dx, py + dy

    if part == "part_1":
        return len(screen_state)
    else:
        return convert_6(print_registration_identifier(screen_state))


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(aoc_input)}")
print(f"My answer is {part_2(aoc_input)}")
