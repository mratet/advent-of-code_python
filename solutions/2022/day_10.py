from advent_of_code_ocr import convert_array_6
from aocd import get_data

input = get_data(day=10, year=2022).splitlines()


# WRITE YOUR SOLUTION HERE
def run_program(lines):
    x = 1
    yield x
    for line in lines:
        if line == "noop":
            yield x
        else:
            _, v = line.split()
            yield x
            yield x
            x += int(v)


def solve(lines, part="part_1"):
    state = list(run_program(lines))
    if part == "part_1":
        return sum(cycle * state[cycle] for cycle in range(20, 221, 40))
    w, h = 40, 6
    pixels = [1 if abs((i % w) - x) <= 1 else 0 for i, x in enumerate(state[1:])]
    return convert_array_6([pixels[i * w : (i + 1) * w] for i in range(h)], fill_pixel=1, empty_pixel=0)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
