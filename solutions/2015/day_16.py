import re

from aocd import get_data

input = get_data(day=16, year=2015).splitlines()

sue_informations = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def _parse(input):
    return [dict(re.findall(r"(\w+): (\d+)", line)) for line in input]


def check(key, value, part):
    value = int(value)
    if part == "part_2":
        if key in ("cats", "trees"):
            return sue_informations[key] < value
        if key in ("pomeranians", "goldfish"):
            return sue_informations[key] > value
    return sue_informations[key] == value


def solve(input, part):
    sues = _parse(input)
    for i, sue in enumerate(sues):
        if all(check(k, v, part) for k, v in sue.items()):
            return i + 1


def part_1(input):
    return solve(input, "part_1")


def part_2(input):
    return solve(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
