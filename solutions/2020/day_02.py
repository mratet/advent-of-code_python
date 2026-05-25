import re
from typing import NamedTuple

from aocd import get_data

input = get_data(day=2, year=2020).splitlines()


class Policy(NamedTuple):
    lo: int
    hi: int
    letter: str
    password: str


def parse_line(line):
    m = re.match(r"(\d+)-(\d+) ([a-z]): (\w+)", line)
    assert m
    lo, hi, letter, password = m.groups()
    return Policy(int(lo), int(hi), letter, password)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum(p.lo <= p.password.count(p.letter) <= p.hi for line in lines if (p := parse_line(line)))


def part_2(lines):
    return sum(
        (p.password[p.lo - 1] == p.letter) ^ (p.password[p.hi - 1] == p.letter)
        for line in lines
        if (p := parse_line(line))
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
