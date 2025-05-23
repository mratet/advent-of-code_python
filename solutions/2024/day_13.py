from aocd import get_data

input = get_data(day=13, year=2024).split("\n\n")
import re


# WRITE YOUR SOLUTION HERE
def solve(Xa, Ya, Xb, Yb, Xc, Yc):
    det = Xa * Yb - Xb * Ya
    v1 = -(Xb * Yc - Xc * Yb)
    v2 = Xa * Yc - Xc * Ya
    if v1 % det == 0 and v2 % det == 0:
        i = v1 // det
        j = v2 // det
        return 3 * i + j
    return 0


def part_1(lines):
    score = 0
    for block in lines:
        Xa, Ya, Xb, Yb, Xc, Yc = map(int, re.findall(r"(\d+)", block))
        score += solve(Xa, Ya, Xb, Yb, Xc, Yc)
    return score


def part_2(lines):
    score = 0
    C = 10000000000000
    for block in lines:
        Xa, Ya, Xb, Yb, Xc, Yc = map(int, re.findall(r"(\d+)", block))
        score += solve(Xa, Ya, Xb, Yb, Xc + C, Yc + C)
    return score


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
