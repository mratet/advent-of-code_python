from aocd import get_data
from functools import lru_cache

input = get_data(day=22, year=2018).splitlines()


def parse_input(lines):
    depth = int(lines[0].split(": ")[1])
    X, Y = map(int, lines[1].split(": ")[1].split(","))
    return depth, X, Y


@lru_cache
def geological_index(region, depth, target):
    X, Y = region
    if region == (0, 0):
        return 0
    elif region == target:
        return 0
    elif Y == 0:
        return X * 16807
    elif X == 0:
        return Y * 48271
    else:
        return erosion_level((X - 1, Y), depth, target) * erosion_level(
            (X, Y - 1), depth, target
        )


@lru_cache
def erosion_level(region, depth, target):
    return (geological_index(region, depth, target) + depth) % 20183


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    depth, X, Y = parse_input(lines)
    return sum(
        erosion_level((x, y), depth, (X, Y)) % 3
        for x in range(X + 1)
        for y in range(Y + 1)
    )


def part_2(lines):
    return


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
# print(f'My answer is {part_2(input)}')
