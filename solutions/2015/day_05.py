import re

from aocd import get_data

input = get_data(day=5, year=2015).splitlines()


def nice_string_part1(str):
    has_three_vowels = re.search(r"([aeiou].*){3}", str)
    has_double_letter = re.search(r"(.)\1", str)
    has_forbidden_pair = re.search(r"ab|cd|pq|xy", str)
    return bool(has_three_vowels and has_double_letter and not has_forbidden_pair)


def nice_string_part2(str):
    has_repeating_pair = re.search(r"(..).*\1", str)
    has_sandwich = re.search(r"(.).\1", str)
    return bool(has_repeating_pair and has_sandwich)


def part_1(input):
    return sum(nice_string_part1(str) for str in input)


def part_2(input):
    return sum(nice_string_part2(str) for str in input)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
