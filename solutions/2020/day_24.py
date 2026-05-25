import re
from collections import Counter

from aocd import get_data

input = get_data(day=24, year=2020).splitlines()

DIRS = {"e": (1, 0, 0), "w": (-1, 0, 0), "ne": (0, 1, 0), "sw": (0, -1, 0), "se": (0, 0, 1), "nw": (0, 0, -1)}


# WRITE YOUR SOLUTION HERE
def get_hexa_coords(line):
    dirs = re.findall("e|se|sw|w|nw|ne", line)
    return tuple(sum(DIRS[d][i] for d in dirs) for i in range(3))


def transform_hex_coords(hex_coords):
    (y, x1, x2) = hex_coords
    north_contrib = x1 - x2
    east_contrib = x1 + x2
    return (north_contrib, east_contrib + 2 * y)


def get_black_tiles(lines):
    black_tiles = set()
    for line in lines:
        pos = transform_hex_coords(get_hexa_coords(line))
        black_tiles.symmetric_difference_update({pos})
    return black_tiles


def neighbour_coordinates(p):
    return [
        tuple(a + b for a, b in zip(p, t, strict=False)) for t in [(0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    ]


def part_1(lines):
    return len(get_black_tiles(lines))


def part_2(lines):
    black_tiles = get_black_tiles(lines)
    for _ in range(100):
        total_neighbours = Counter(p for coordinate in black_tiles for p in neighbour_coordinates(coordinate))
        black_tiles = {p for p, cnt in total_neighbours.items() if (p in black_tiles and cnt == 1) or cnt == 2}
    return len(black_tiles)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
