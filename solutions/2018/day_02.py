from aocd import get_data
from itertools import combinations
from collections import Counter

input = get_data(day=2, year=2018).splitlines()


def compare_box_ids(box1, box2):
    diffs = [i for i, (c1, c2) in enumerate(zip(box1, box2)) if c1 != c2]
    if len(diffs) != 1:
        return ""
    i = diffs[0]
    return box1[:i] + box1[i + 1 :]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    two = sum(2 in Counter(box_id).values() for box_id in lines)
    three = sum(3 in Counter(box_id).values() for box_id in lines)
    return two * three


def part_2(lines):
    for b1, b2 in combinations(lines, 2):
        if S := compare_box_ids(b1, b2):
            return "".join(S)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
