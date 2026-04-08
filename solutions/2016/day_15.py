import re

from aocd import get_data

input = get_data(day=15, year=2016)


def _parse(input):
    return [list(map(int, m)) for m in re.findall(r"(\d+) positions.*?position (\d+)", input)]


def find_perfect_button_push(disks):
    # Disk i reaches position 0 when: (N + i + 1 + start) % length == 0
    # Equivalent to: N ≡ -(i + 1 + start) (mod length)
    # This is a system of congruences solvable via the Chinese Remainder Theorem if a faster solution is needed
    n = 0
    while not all((n + i + 1 + start) % length == 0 for i, (length, start) in enumerate(disks)):
        n += 1
    return n


def part_1(input):
    disks = _parse(input)
    return find_perfect_button_push(disks)


def part_2(input):
    disks = _parse(input)
    disks.append([11, 0])
    return find_perfect_button_push(disks)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
