from aocd import get_data

input = get_data(day=24, year=2020).splitlines()

from collections import defaultdict
from collections import Counter
import re


# WRITE YOUR SOLUTION HERE
def get_hexa_coords(line):
    x, y, z = 0, 0, 0
    dirs = re.findall("e|se|sw|w|nw|ne", line)
    for d in dirs:
        if d == "e":
            x += 1
        elif d == "w":
            x -= 1
        elif d == "ne":
            y += 1
        elif d == "sw":
            y -= 1
        elif d == "se":
            z += 1
        elif d == "nw":
            z -= 1
    return (x, y, z)


def transform_hex_coords(hex_coords):
    (y, x1, x2) = hex_coords
    north_contrib = x1 - x2
    east_contrib = x1 + x2
    return (north_contrib, east_contrib + 2 * y)


def part_1(lines):
    state = defaultdict(int)
    for line in lines:
        cardinal_pos = transform_hex_coords(get_hexa_coords(line))
        state[cardinal_pos] += 1
    return sum([c % 2 for c in state.values()])


def neighbour_coordinates(p):
    return [
        tuple(a + b for a, b in zip(p, t))
        for t in [(0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    ]


def part_2(lines):
    black_tiles = set()
    for line in lines:
        hexa_coords = get_hexa_coords(line)
        pos = transform_hex_coords(hexa_coords)
        # Only max 2 flips in the init
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)

    n = 100
    for _ in range(n):
        total_neighbours = Counter(
            p for coordinate in black_tiles for p in neighbour_coordinates(coordinate)
        )
        black_tiles = {
            p
            for p, n in total_neighbours.items()
            if (p in black_tiles and n == 1) or n == 2
        }
    return len(black_tiles)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
