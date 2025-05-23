from aocd import get_data, submit

input = get_data(day=5, year=2024).split("\n\n")
from collections import defaultdict
from functools import cmp_to_key


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    dict_rule = defaultdict(list)
    for line in lines[0].split():
        a, b = map(int, line.split("|"))
        dict_rule[a].append(b)

    pages = [list(map(int, line.split(","))) for line in lines[1].split()]
    return dict_rule, pages


def part_1(lines):
    dict_rule, pages = parse_input(lines)
    cmp = lambda a, b: -1 * int(b in dict_rule[a])
    return sum(
        [
            page[len(page) // 2]
            for page in pages
            if (page == sorted(page, key=cmp_to_key(cmp)))
        ]
    )


def part_2(lines):
    dict_rule, pages = parse_input(lines)
    cmp = lambda a, b: -1 * int(b in dict_rule[a])
    return sum(
        [
            sorted_p[len(sorted_p) // 2]
            for page in pages
            if (sorted_p := sorted(page, key=cmp_to_key(cmp))) != page
        ]
    )


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
