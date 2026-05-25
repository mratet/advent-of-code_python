import itertools

from aocd import get_data

input = get_data(day=4, year=2024).splitlines()

# WRITE YOUR SOLUTION HERE
DIRECTIONS = [d for d in itertools.product(range(-1, 2), repeat=2) if d != (0, 0)]


def find_xmas(graph, pos):
    i, j = pos
    return [
        "".join(
            graph[i + n * di][j + n * dj]
            for n in range(4)
            if 0 <= i + n * di < len(graph) and 0 <= j + n * dj < len(graph[0])
        )
        for di, dj in DIRECTIONS
    ].count("XMAS")


def find_x_mas(graph, pos):
    i, j = pos
    return "".join(
        graph[i + di][j + dj]
        for di, dj in ((1, 1), (1, -1), (-1, -1), (-1, 1))
        if 0 <= i + di < len(graph) and 0 <= j + dj < len(graph[0])
    ) in ("MMSS", "SMMS", "SSMM", "MSSM")


def solve(lines, part="part_1"):
    if part == "part_2":
        target, check = "A", find_x_mas
    else:
        target, check = "X", find_xmas

    return sum(check(lines, (i, j)) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == target)


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
