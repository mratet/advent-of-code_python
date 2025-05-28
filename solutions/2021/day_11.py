from aocd import get_data
from itertools import product

input = get_data(day=11, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    return grid


def solve(grid, part="part_1"):
    flash_count = 0
    step = 0
    while True:
        for node in grid:
            grid[node] += 1
        processed_node = set()
        while True:
            flash_node = {node for node in grid if grid[node] > 9}
            flash_node -= processed_node
            if not flash_node:
                break
            for node in flash_node:
                x, y = node
                for dx, dy in product((-1, 0, 1), repeat=2):
                    neigh_node = x + dx, y + dy
                    if neigh_node in grid:
                        grid[neigh_node] += 1
            flash_count += len(flash_node)
            processed_node = processed_node.union(flash_node)
        for node in processed_node:
            grid[node] = 0

        step += 1
        if part == "part_1" and step == 100:
            return flash_count
        if part == "part_2" and len(processed_node) == 100:
            return step


def part_1(lines):
    grid = parse_input(lines)
    return solve(grid, "part_1")


def part_2(lines):
    grid = parse_input(lines)
    return solve(grid, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
