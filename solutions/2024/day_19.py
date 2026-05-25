from functools import cache

from aocd import get_data

input = get_data(day=19, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def solve(lines):
    patterns, designs = lines[0].split(", "), lines[2:]

    @cache
    def count_arrangements(design):
        if design == "":
            return 1
        return sum(count_arrangements(design[len(p) :]) for p in patterns if design.startswith(p))

    counts = [count_arrangements(d) for d in designs]
    return sum(c > 0 for c in counts), sum(counts)


def part_1(lines):
    return solve(lines)[0]


def part_2(lines):
    return solve(lines)[1]


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
