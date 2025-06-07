from aocd import get_data
import re

input = get_data(day=4, year=2022).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    s1 = 0
    for line in lines:
        x1, x2, y1, y2 = map(int, re.findall(r"\d+", line))
        p1, p2 = range(x1, x2 + 1), range(y1, y2 + 1)
        if set(p1).issubset(p2) or set(p2).issubset(p1):
            s1 += 1
    return s1


def part_2(lines):
    s2 = 0
    for line in lines:
        x1, x2, y1, y2 = map(int, re.findall(r"\d+", line))
        p1, p2 = range(x1, x2 + 1), range(y1, y2 + 1)
        if len(set(p1) & set(p2)) > 0:
            s2 += 1
    return s2


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
