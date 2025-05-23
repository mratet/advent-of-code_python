from aocd import get_data

input = get_data(day=3, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
import re


def part_1(grid):
    def is_valid(r, s, e):
        for cr in [r - 1, r, r + 1]:
            for cc in range(s - 1, e + 1):
                if (
                    0 <= cr < len(grid)
                    and 0 <= cc < len(row)
                    and grid[cr][cc] not in ".01234556789"
                ):
                    return True
        return False

    total = 0
    for r, row in enumerate(grid):
        for match in re.finditer("\\d+", row):
            if is_valid(r, match.start(), match.end()):
                total += int(match.group())

    return total


def part_2(grid):
    gears = {}

    def scan(r, s, e, n):
        for cr in [r - 1, r, r + 1]:
            for cc in range(s - 1, e + 1):
                if 0 <= cr < len(grid) and 0 <= cc < len(row) and grid[cr][cc] == "*":
                    if (cr, cc) not in gears:
                        gears[(cr, cc)] = []
                    gears[(cr, cc)].append(n)

    for r, row in enumerate(grid):
        for match in re.finditer("\\d+", row):
            scan(r, match.start(), match.end(), int(match.group()))

    total = 0
    for array in gears.values():
        if len(array) == 2:
            total += array[0] * array[1]

    return total


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
