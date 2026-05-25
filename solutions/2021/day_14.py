from collections import Counter
from itertools import pairwise

from aocd import get_data

input = get_data(day=14, year=2021)


# WRITE YOUR SOLUTION HERE
def parse_input(data):
    polymer_template, pair_insertion = data.split("\n\n")

    current_polymer = Counter("".join(pair) for pair in pairwise(polymer_template))

    insertion_rules = {}
    for line in pair_insertion.splitlines():
        pair, letter = line.split(" -> ")
        c1, c2 = pair
        insertion_rules[pair] = (c1 + letter, letter + c2)
    return current_polymer, insertion_rules, polymer_template[-1]


def get_next_polymer(current_polymer, insertion_rules):
    next_polymer = Counter()
    for pair, count in current_polymer.items():
        for next_pair in insertion_rules[pair]:
            next_polymer[next_pair] += count
    return next_polymer


def count_letters(current_polymer, last_char):
    letters = Counter()
    for (c1, _), count in current_polymer.items():
        letters[c1] += count
    letters[last_char] += 1
    return letters.values()


def solve(data, n):
    current_polymer, insertion_rules, last_char = parse_input(data)
    for _ in range(n):
        current_polymer = get_next_polymer(current_polymer, insertion_rules)
    counts = count_letters(current_polymer, last_char)
    return max(counts) - min(counts)


def part_1(data):
    return solve(data, 10)


def part_2(data):
    return solve(data, 40)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
