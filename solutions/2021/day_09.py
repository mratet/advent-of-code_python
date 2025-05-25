from aocd import get_data
from math import prod

NEIGHBOORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

input = get_data(day=9, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(input):
    return [[int(n) for n in line] for line in input]


def detect_low_points(grid):
    H, W = len(grid), len(grid[0])
    low_points = []
    for h in range(H):
        for w in range(W):
            height_cand = [
                grid[h + dh][w + dw]
                for dh, dw in NEIGHBOORS
                if 0 <= h + dh < H and 0 <= w + dw < W
            ]
            if all(neigh_height > grid[h][w] for neigh_height in height_cand):
                low_points.append((h, w))
    return low_points


def compute_risk_level(grid, low_points):
    return sum(grid[h][w] + 1 for h, w in low_points)


def measure_basin_size(grid, low_points):
    basin_sizes = []
    H, W = len(grid), len(grid[0])
    for low_point in low_points:
        current_cand = [low_point]
        seen = set()
        while len(current_cand) > 0:
            h, w = current_cand.pop()
            if (h, w) in seen:
                continue
            seen.add((h, w))
            for dh, dw in NEIGHBOORS:
                if (
                    (0 <= h + dh < H and 0 <= w + dw < W)
                    and grid[h + dh][w + dw] != 9
                    and grid[h + dh][w + dw] > grid[h][w]
                ):
                    current_cand.append((h + dh, w + dw))
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
