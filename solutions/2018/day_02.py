from collections import Counter
from itertools import combinations

from aocd import get_data

input = get_data(day=2, year=2018).splitlines()


def compare_box_ids(box1, box2):
    diffs = [i for i, (c1, c2) in enumerate(zip(box1, box2, strict=False)) if c1 != c2]
    if len(diffs) != 1:
        return ""
    i = diffs[0]
    return box1[:i] + box1[i + 1 :]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    counts = [Counter(box_id).values() for box_id in lines]
    return sum(2 in c for c in counts) * sum(3 in c for c in counts)


def part_2(lines):
    for b1, b2 in combinations(lines, 2):
        if S := compare_box_ids(b1, b2):
            return S


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
