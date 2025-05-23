from aocd import get_data

input = get_data(day=19, year=2024).splitlines()
from functools import cache


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    patterns, cand = lines[0].split(", "), lines[2:]

    @cache
    def is_designable(l):
        if l == "":
            return True
        return any(
            [
                is_designable(l[len(pattern) :])
                for pattern in patterns
                if l.startswith(pattern)
            ]
        )

    return sum(is_designable(l) for l in cand)


def part_2(lines):
    patterns, cand = lines[0].split(", "), lines[2:]

    @cache
    def is_designable(l):
        if l == "":
            return 1
        return sum(
            [
                is_designable(l[len(pattern) :])
                for pattern in patterns
                if l.startswith(pattern)
            ]
        )

    return sum(is_designable(l) for l in cand)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
