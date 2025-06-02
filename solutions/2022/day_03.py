from aocd import get_data
from string import ascii_lowercase

input = get_data(day=3, year=2022).splitlines()


def compute_priority(item_type):
    return (
        ascii_lowercase.index(item_type.lower())
        + 1
        + (26 if item_type.isupper() else 0)
    )


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    priority = 0
    for line in lines:
        n = len(line)
        item_type = (set(line[: n // 2]) & set(line[n // 2 :])).pop()
        priority += compute_priority(item_type)
    return priority


def part_2(lines):
    priority = 0
    for g1, g2, g3 in zip(lines[::3], lines[1::3], lines[2::3]):
        item_type = (set(g1) & set(g2) & set(g3)).pop()
        priority += compute_priority(item_type)
    return priority


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
