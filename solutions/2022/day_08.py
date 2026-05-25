from math import prod

from aocd import get_data

input = get_data(day=8, year=2022).splitlines()
X, Y = len(input), len(input[0])


# WRITE YOUR SOLUTION HERE
def get_views(tree):
    xt, yt = tree
    return [
        [(xt - x, yt) for x in range(1, X) if (xt - x) >= 0],
        [(xt + x, yt) for x in range(1, X) if (xt + x) < X],
        [(xt, yt - y) for y in range(1, Y) if (yt - y) >= 0],
        [(xt, yt + y) for y in range(1, Y) if (yt + y) < Y],
    ]


def check_tree_visibility(tree, grid):
    views = get_views(tree)
    return any(not view or all(grid[neigh_tree] < grid[tree] for neigh_tree in view) for view in views)


def compute_scenic_score(tree, grid):
    views = get_views(tree)
    scenic_view = []
    for view in views:
        count = 0
        for neigh_tree in view:
            count += 1
            if grid[neigh_tree] >= grid[tree]:
                break
        scenic_view.append(count)
    return prod(scenic_view)


def solve(lines, part="part_1"):
    grid = {(x, y): int(c) for y, row in enumerate(lines) for x, c in enumerate(row)}
    if part == "part_1":
        return sum(1 for tree in grid if check_tree_visibility(tree, grid))
    return max(compute_scenic_score(tree, grid) for tree in grid)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
