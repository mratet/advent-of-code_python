from aocd import get_data

input = get_data(day=4, year=2024).splitlines()
import itertools

# WRITE YOUR SOLUTION HERE
DIRECTIONS = list(itertools.product(range(-1, 2), repeat=2))


def look_for_XMAS(graph, pos):
    return [
        "".join(
            [
                graph[pos[0] + n * di][pos[1] + n * dj]
                for n in range(4)
                if 0 <= pos[0] + n * di < len(graph)
                and 0 <= pos[1] + n * dj < len(graph[0])
            ]
        )
        for di, dj in DIRECTIONS
    ].count("XMAS")


def part_1(lines):
    return sum(
        [
            look_for_XMAS(lines, (i, j))
            for i in range(len(lines))
            for j in range(len(lines[0]))
            if lines[i][j] == "X"
        ]
    )


def look_for_Xmas(graph, pos):
    return "".join(
        [
            graph[pos[0] + di][pos[1] + dj]
            for (di, dj) in ((1, 1), (1, -1), (-1, -1), (-1, 1))
        ]
    ) in ("MMSS", "SMMS", "SSMM", "MSSM")


def part_2(lines):
    return sum(
        [
            look_for_Xmas(lines, (i, j))
            for i in range(1, len(lines) - 1)
            for j in range(1, len(lines[0]) - 1)
            if lines[i][j] == "A"
        ]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
