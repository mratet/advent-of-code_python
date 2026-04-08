import re

import numpy as np
from advent_of_code_ocr import convert_array_6
from aocd import get_data

input = get_data(day=8, year=2016).splitlines()


def _parse(input):
    instructions = []

    for line in input:
        if line.startswith("rect"):
            A, B = map(int, line.split()[1].split("x"))
            instructions.append(("r", A, B))
        else:
            pattern = r"rotate .* (.)=(\d+) by (\d+)"
            rot_axes, A, B = re.findall(pattern, line)[0]
            instructions.append((rot_axes, int(A), int(B)))
    return instructions


def generate_screen(instructions):
    W, H = 50, 6
    screen = np.zeros((H, W), dtype=np.uint8)
    for c, A, B in instructions:
        match c:
            case "r":
                screen[:B, :A] = 1
            case "y":
                screen[A, :] = np.roll(screen[A, :], B)
            case "x":
                screen[:, A] = np.roll(screen[:, A], B)
    return screen


def part_1(input):
    instructions = _parse(input)
    screen = generate_screen(instructions)
    return np.sum(screen)


def part_2(input):
    instructions = _parse(input)
    screen = generate_screen(instructions)
    return convert_array_6(screen, fill_pixel=1, empty_pixel=0)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
