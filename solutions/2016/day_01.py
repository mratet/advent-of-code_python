import itertools, re, collections
from aocd import get_data

input = get_data(day=1, year=2016).split(", ")

N, S, E, W = (0, 1), (0, -1), (1, 0), (-1, 0)
dirs = [N, E, S, W]


def follow_instructions(input, part):
    dir = 0
    pos = (0, 0)
    visited = set()
    visited.add(pos)

    for line in input:
        rot, num = line[0], line[1:]
        if rot == "R":
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

        dx, dy = dirs[dir]
        for _ in range(int(num)):
            pos = (pos[0] + dx, pos[1] + dy)
            if part == "part_2" and pos in visited:
                return pos
            visited.add(pos)

    return pos


def part_1(input):
    last_pos = follow_instructions(input, "part_1")
    return abs(last_pos[0]) + abs(last_pos[1])


def part_2(input):
    last_pos = follow_instructions(input, "part_2")
    return abs(last_pos[0]) + abs(last_pos[1])


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
