import re

from aocd import get_data

input = get_data(day=4, year=2020).split("\n\n")

MANDATORY_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

REQUIREMENTS = [
    ("byr", lambda x: 1920 <= int(x) <= 2002),
    ("iyr", lambda x: 2010 <= int(x) <= 2020),
    ("eyr", lambda x: 2020 <= int(x) <= 2030),
    (
        "hgt",
        lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    ),
    ("hcl", lambda x: re.fullmatch(r"#[0-9a-f]{6}", x)),
    ("ecl", lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    ("pid", lambda x: re.fullmatch(r"[0-9]{9}", x)),
]


def parse_passport(line):
    return {field.split(":")[0]: field.split(":")[1] for field in line.split()}


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(MANDATORY_FIELDS.issubset(parse_passport(line)) for line in lines)


def part_2(lines):
    return sum(
        all(req(passport[key]) for key, req in REQUIREMENTS)
        for line in lines
        if MANDATORY_FIELDS.issubset(passport := parse_passport(line))
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
