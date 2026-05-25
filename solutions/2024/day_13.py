import re

from aocd import get_data

input = get_data(day=13, year=2024).split("\n\n")


# WRITE YOUR SOLUTION HERE
def tokens(xa, ya, xb, yb, xc, yc):
    det = xa * yb - xb * ya
    v1 = xc * yb - xb * yc
    v2 = xa * yc - xc * ya
    if v1 % det == 0 and v2 % det == 0:
        return 3 * (v1 // det) + (v2 // det)
    return 0


def solve(lines, part="part_1"):
    offset = 10000000000000 if part == "part_2" else 0
    score = 0
    for block in lines:
        xa, ya, xb, yb, xc, yc = map(int, re.findall(r"(\d+)", block))
        score += tokens(xa, ya, xb, yb, xc + offset, yc + offset)
    return score


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
