from aocd import get_data
from collections import Counter
import re
import numpy as np

input_data = get_data(day=3, year=2018)
GRID_SIZE = 1000


def parse_claims(text):
    return [tuple(map(int, re.findall(r"\d+", line))) for line in text.splitlines()]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    fabric = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

    for claim_id, left, top, width, height in parse_claims(lines):
        fabric[top : top + height, left : left + width] += 1

    return np.count_nonzero(fabric > 1)


def part_2(lines):
    fabric = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    fabric_claims = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    claim_areas = {}

    for claim_id, left, top, width, height in parse_claims(lines):
        fabric[top : top + height, left : left + width] += 1
        fabric_claims[top : top + height, left : left + width] = claim_id
        claim_areas[claim_id] = width * height

    unique_claims = Counter(fabric_claims[fabric == 1])
    for claim_id, count in unique_claims.items():
        if count == claim_areas.get(claim_id):
            return claim_id


# END OF SOLUTION

print(f"My answer is {part_1(input_data)}")
print(f"My answer is {part_2(input_data)}")
