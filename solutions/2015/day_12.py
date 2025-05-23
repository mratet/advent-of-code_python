from aocd import get_data

input = get_data(day=12, year=2015)

import re, json


def part_1(input):
    matchs = re.findall(r"([-\d]\d*)", input)
    return sum([int(match) for match in matchs])


def recsum(r):
    if isinstance(r, list):
        return sum(map(recsum, r))

    elif isinstance(r, dict):
        if "red" in r.values():
            return 0
        return sum(map(recsum, r.values()))

    elif isinstance(r, int):
        return r

    return 0


def part_2(input):
    d = json.loads(input)
    return recsum(d)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
