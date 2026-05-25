from math import prod

from aocd import get_data

input = get_data(day=9, year=2021).splitlines()

NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# WRITE YOUR SOLUTION HERE
def parse_input(data):
    return [[int(n) for n in line] for line in data]


def detect_low_points(grid):
    rows, cols = len(grid), len(grid[0])
    low_points = []
    for h in range(rows):
        for w in range(cols):
            neighbors = [grid[h + dh][w + dw] for dh, dw in NEIGHBORS if 0 <= h + dh < rows and 0 <= w + dw < cols]
            if all(n > grid[h][w] for n in neighbors):
                low_points.append((h, w))
    return low_points


def compute_risk_level(grid, low_points):
    return sum(grid[h][w] + 1 for h, w in low_points)


def measure_basin_size(grid, low_points):
    basin_sizes = []
    rows, cols = len(grid), len(grid[0])
    for low_point in low_points:
        stack = [low_point]
        seen = set()
        while stack:
            h, w = stack.pop()
            if (h, w) in seen:
                continue
            seen.add((h, w))
            for dh, dw in NEIGHBORS:
                if (
                    (0 <= h + dh < rows and 0 <= w + dw < cols)
                    and grid[h + dh][w + dw] != 9
                    and grid[h + dh][w + dw] > grid[h][w]
                ):
                    stack.append((h + dh, w + dw))
        basin_sizes.append(len(seen))
    return basin_sizes


def part_1(lines):
    grid = parse_input(lines)
    low_points = detect_low_points(grid)
    return compute_risk_level(grid, low_points)


def part_2(lines):
    grid = parse_input(lines)
    low_points = detect_low_points(grid)
    basin_sizes = measure_basin_size(grid, low_points)
    return prod(sorted(basin_sizes)[-3:])


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
