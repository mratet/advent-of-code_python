import re

from aocd import get_data

input = get_data(day=3, year=2024)


# WRITE YOUR SOLUTION HERE
def sum_muls(text):
    return sum(int(a) * int(b) for (a, b) in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text))


def part_1(lines):
    return sum_muls(lines)


def part_2(lines):
    text = re.sub(r"don't\(\).*?(?:$|do\(\))", "", lines, flags=re.DOTALL)
    return sum_muls(text)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
