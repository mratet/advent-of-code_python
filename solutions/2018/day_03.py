import re

import numpy as np
from aocd import get_data

input_data = get_data(day=3, year=2018)
GRID_SIZE = 1000


def parse_claims(text):
    return [tuple(map(int, re.findall(r"\d+", line))) for line in text.splitlines()]


def build_fabric(lines):
    claims = parse_claims(lines)
    fabric = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

    for _, left, top, width, height in claims:
        fabric[top : top + height, left : left + width] += 1
    return claims, fabric


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    _, fabric = build_fabric(lines)
    return np.count_nonzero(fabric > 1)


def part_2(lines):
    claims, fabric = build_fabric(lines)

    for claim_id, left, top, width, height in claims:
        if np.all(fabric[top : top + height, left : left + width] == 1):
            return claim_id


# END OF SOLUTION

print(f"My answer is {part_1(input_data)}")
print(f"My answer is {part_2(input_data)}")
