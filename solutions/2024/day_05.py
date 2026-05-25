from collections import defaultdict
from functools import cmp_to_key

from aocd import get_data

input = get_data(day=5, year=2024).split("\n\n")


# WRITE YOUR SOLUTION HERE
def parse_input(lines):
    dict_rule = defaultdict(list)
    for line in lines[0].split():
        a, b = map(int, line.split("|"))
        dict_rule[a].append(b)
    pages = [list(map(int, line.split(","))) for line in lines[1].split()]
    return dict_rule, pages


def solve(lines, part="part_1"):
    dict_rule, pages = parse_input(lines)
    cmp = lambda a, b: -1 * int(b in dict_rule[a])
    total = 0
    for page in pages:
        sorted_page = sorted(page, key=cmp_to_key(cmp))
        if part == "part_2" and sorted_page != page:
            total += sorted_page[len(sorted_page) // 2]
        elif part == "part_1" and sorted_page == page:
            total += page[len(page) // 2]
    return total


def part_1(lines):
    return solve(lines)


def part_2(lines):
    return solve(lines, part="part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
