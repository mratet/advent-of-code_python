import re
from collections import Counter

from aocd import get_data

input = get_data(day=4, year=2016).splitlines()


def decrypt(name, n):
    return "".join(chr((ord(c) - ord("a") + n) % 26 + ord("a")) if c.isalpha() else c for c in name)


def real_rooms(input):
    for line in input:
        name, sector, checksum = re.findall(r"([a-z-]+)-(\d+)\[(\w+)]", line)[0]
        freq = sorted(Counter(name.replace("-", "")).items(), key=lambda x: (-x[1], x[0]))
        if "".join(c for c, _ in freq).startswith(checksum):
            yield name, int(sector)


def part_1(input):
    return sum(sector for _, sector in real_rooms(input))


def part_2(input):
    return next(sector for name, sector in real_rooms(input) if "north" in decrypt(name, sector))


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
