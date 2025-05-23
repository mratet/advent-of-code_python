from aocd import get_data

input = get_data(day=3, year=2024)
import re


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(
        [
            int(x1) * int(x2)
            for (x1, x2) in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines)
        ]
    )


def part_2(lines):
    text = re.sub(r"don't\(\).*?(?:$|do\(\))", "", lines, flags=re.DOTALL)
    return sum(
        [
            int(x1) * int(x2)
            for (x1, x2) in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)
        ]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
