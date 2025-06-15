from collections import Counter
from itertools import product

from aocd import get_data

input = get_data(day=23, year=2022).splitlines()

DIRECTIONS = {
    "NO": (0, 0),
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
    "NW": (-1, 1),
    "NE": (1, 1),
    "SW": (-1, -1),
    "SE": (1, -1),
}

DIRS_PROPOSAL = [
    (["N", "NE", "NW"], "N"),
    (["S", "SE", "SW"], "S"),
    (["W", "NW", "SW"], "W"),
    (["E", "NE", "SE"], "E"),
]


def parse_input(lines):
    return [
        (x, -y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#"
    ]


def is_surrounded(elve, directions, elf_positions):
    x, y = elve
    return all(
        (x + dx, y + dy) not in elf_positions
        for dir in directions
        for dx, dy in [DIRECTIONS[dir]]
    )


def propose_direction(elve, elf_positions, start_idx):
    if is_surrounded(elve, [d for d in DIRECTIONS if d != "NO"], elf_positions):
        return "NO"
    for offset in range(4):
        check_dirs, move_dir = DIRS_PROPOSAL[(start_idx + offset) % 4]
        if is_surrounded(elve, check_dirs, elf_positions):
            return move_dir
    return "NO"


def simulate_round(elves, round_number):
    proposed_moves = []
    elf_positions = set(elves)

    for elf in elves:
        move_dir = propose_direction(elf, elf_positions, round_number)
        dx, dy = DIRECTIONS[move_dir]
        proposed_moves.append((elf[0] + dx, elf[1] + dy))

    move_counts = Counter(proposed_moves)
    return [
        elf if move_counts[move] > 1 else move
        for elf, move in zip(elves, proposed_moves)
    ]


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    elves = parse_input(lines)
    for i in range(10):
        elves = simulate_round(elves, i)

    x_coords = [x for x, _ in elves]
    y_coords = [y for _, y in elves]
    area = set(
        product(
            range(min(x_coords), max(x_coords) + 1),
            range(min(y_coords), max(y_coords) + 1),
        )
    )
    return len(area - set(elves))


def part_2(lines):
    elves = parse_input(lines)
    round = 0
    while True:
        next_elves = simulate_round(elves, round)
        round += 1
        if elves == next_elves:
            break
        elves = next_elves
    return round


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
