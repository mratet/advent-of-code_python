import itertools, re, collections
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
    sues = []
    pattern = r"(\w+): (\d+)"
    for line in input:
        matchs = re.findall(pattern, line)
        sue_dict = {k: v for k, v in matchs}
        sues.append(sue_dict)
    return sues


def part_1(input):
    sues = _parse(input)
    for i, sue in enumerate(sues):
        sue_inter = {k: v for k, v in sue.items() if sue_informations[k] == int(v)}
        if len(sue_inter) == len(sue):
            return i + 1


def check(types, value):
    value = int(value)
    if types in ("cats", "trees"):
        return sue_informations[types] < value
    elif types in ("pomeranians", "goldfish"):
        return sue_informations[types] > value
    return sue_informations[types] == value


def part_2(input):
    sues = _parse(input)
    for i, sue in enumerate(sues):
        if all(list([check(k, v) for k, v in sue.items()])):
            return i + 1


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
