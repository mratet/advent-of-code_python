from collections import defaultdict
from functools import reduce

from aocd import get_data

input = get_data(day=15, year=2023).strip().split(",")

# WRITE YOUR SOLUTION HERE


def char(acc, c):
    return (acc + ord(c)) * 17 % 256


def holiday_hash(s):
    return reduce(char, s, 0)


def part_1(steps):
    return sum(map(holiday_hash, steps))


def part_2(steps):
    boxes = defaultdict(dict)
    for step in steps:
        if "-" in step:
            label = step[:-1]
            boxes[holiday_hash(label)].pop(label, None)
        else:
            label, focal_length = step.split("=")
            boxes[holiday_hash(label)][label] = int(focal_length)
    return sum((i + 1) * (j + 1) * l for i in boxes for j, l in enumerate(boxes[i].values()))


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
