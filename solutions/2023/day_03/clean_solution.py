import collections
import re

from aocd import get_data

input = get_data(day=3, year=2023).splitlines()

NUMBER = re.compile(r"\d+")

# WRITE YOUR SOLUTION HERE


def adjacent_cells(grid, row_idx, col_start, col_end, row):
    for adj_row in [row_idx - 1, row_idx, row_idx + 1]:
        for adj_col in range(col_start - 1, col_end + 1):
            if 0 <= adj_row < len(grid) and 0 <= adj_col < len(row):
                yield adj_row, adj_col, grid[adj_row][adj_col]


def part_1(grid):
    return sum(
        int(match.group())
        for row_idx, row in enumerate(grid)
        for match in NUMBER.finditer(row)
        if any(
            char not in ".0123456789" for _, _, char in adjacent_cells(grid, row_idx, match.start(), match.end(), row)
        )
    )


def part_2(grid):
    gears = collections.defaultdict(list)
    for row_idx, row in enumerate(grid):
        for match in NUMBER.finditer(row):
            num = int(match.group())
            for adj_row, adj_col, char in adjacent_cells(grid, row_idx, match.start(), match.end(), row):
                if char == "*":
                    gears[(adj_row, adj_col)].append(num)
    return sum(nums[0] * nums[1] for nums in gears.values() if len(nums) == 2)


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
