from collections import defaultdict
from itertools import pairwise
from math import ceil

from aocd import get_data

input = get_data(day=14, year=2021)


# WRITE YOUR SOLUTION HERE
def parse_input(input_data):
    polymer_template, pair_insertion = input_data.split("\n\n")

    current_polymer = defaultdict(int)
    for pair in pairwise(polymer_template):
        current_polymer["".join(pair)] += 1

    insertion_rules = {}
    for line in pair_insertion.splitlines():
        pair, letter = line.split(" -> ")
        c1, c2 = pair
        insertion_rules[pair] = (c1 + letter, letter + c2)
    return current_polymer, insertion_rules


def get_next_polymer(current_polymer, insertion_rules):
    next_polymer = defaultdict(int)
    for pair, count in current_polymer.items():
        for next_pair in insertion_rules[pair]:
            next_polymer[next_pair] += count
    return next_polymer


def count_letters(current_polymer):
    letters = defaultdict(int)
    for (c1, c2), count in current_polymer.items():
        letters[c1] += count
        letters[c2] += count
    return [ceil(count / 2) for count in letters.values()]


def solve(current_polymer, insertion_rules, n):
    for i in range(n):
        current_polymer = get_next_polymer(current_polymer, insertion_rules)
    letters_count = count_letters(current_polymer)
    return max(letters_count) - min(letters_count)


def part_1(lines):
    current_polymer, insertion_rules = parse_input(lines)
    return solve(current_polymer, insertion_rules, 10)


def part_2(lines):
    current_polymer, insertion_rules = parse_input(lines)
    return solve(current_polymer, insertion_rules, 40)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
