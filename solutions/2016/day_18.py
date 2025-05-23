import itertools, re, collections
from aocd import get_data

input = get_data(day=18, year=2016)


def next_row(tiles):
    n = len(tiles)
    tiles = "." + tiles + "."
    row = ["^" if tiles[i] != tiles[i + 2] else "." for i in range(n)]
    return "".join(row)


def count_safe_tiles(input, N):
    cnt = 0
    for _ in range(N):
        cnt += sum([elt == "." for elt in input])
        input = next_row(input)
    return cnt


def part_1(input):
    return count_safe_tiles(input, 40)


def part_2(input):
    return count_safe_tiles(input, 400000)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
