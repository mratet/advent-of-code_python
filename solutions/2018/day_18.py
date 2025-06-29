from collections import Counter

from aocd import get_data
from itertools import product

input = get_data(day=18, year=2018)


def parse_input(text: str) -> dict:
    return {
        (x, y): char
        for y, line in enumerate(text.strip().splitlines())
        for x, char in enumerate(line)
    }


def get_adjacent_positions(x: int, y: int) -> set:
    return {
        (x + dx, y + dy)
        for dx, dy in product((-1, 0, 1), repeat=2)
        if not (dx == 0 and dy == 0)
    }


def evolve(lumber: dict) -> dict:
    new_lumber = {}
    for point, tile in lumber.items():
        neighbors = Counter(
            lumber.get(pos, ".") for pos in get_adjacent_positions(*point)
        )

        if tile == ".":
            new_lumber[point] = "|" if neighbors["|"] >= 3 else "."
        elif tile == "|":
            new_lumber[point] = "#" if neighbors["#"] >= 3 else "|"
        elif tile == "#":
            new_lumber[point] = (
                "#" if neighbors["#"] >= 1 and neighbors["|"] >= 1 else "."
            )
    return new_lumber


def compute_resource_value(lumber: dict) -> int:
    counts = Counter(lumber.values())
    return counts["#"] * counts["|"]


# WRITE YOUR SOLUTION HERE
def part_1(lines, minutes=10):
    lumber = parse_input(lines)
    for _ in range(minutes):
        lumber = evolve(lumber)
    return compute_resource_value(lumber)


def part_2(lines):
    lumber = parse_input(lines)
    total_minutes = 1000000000
    seen = []
    while True:
        state = tuple(lumber.values())
        if state in seen:
            cycle_start = seen.index(state)
            cycle_length = len(seen) - cycle_start
            remaining = (total_minutes - cycle_start) % cycle_length
            return part_1(lines, cycle_start + remaining)
        seen.append(state)
        lumber = evolve(lumber)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
