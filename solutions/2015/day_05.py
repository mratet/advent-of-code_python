from aocd import get_data

input = get_data(day=5, year=2015).splitlines()

import re


def nice_string_part1(str):
    cond1 = re.search(r"([aeiou].*){3}", str)
    # deux parametres identiques consecutifs
    cond2 = re.search(r"(.)\1", str)
    cond3 = re.search(r"ab|cd|pq|xy", str)
    return cond1 and cond2 and not cond3


def nice_string_part2(str):
    # Sequences de deux parametres qui se repete
    cond1 = re.search(r"(..).*\1", str)
    # Recherche pattern de la forme a.a
    cond2 = re.search(r"(.).\1", str)
    return cond1 and cond2


def part_1(input):
    return sum([1 for str in input if nice_string_part1(str)])


def part_2(input):
    return sum([1 for str in input if nice_string_part2(str)])


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
