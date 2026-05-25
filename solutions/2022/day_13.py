import ast
from functools import cmp_to_key

from aocd import get_data

input = get_data(day=13, year=2022)


# WRITE YOUR SOLUTION HERE
def compare_packets(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)
    if isinstance(left, int):
        return compare_packets([left], right)
    if isinstance(right, int):
        return compare_packets(left, [right])
    for a, b in zip(left, right, strict=False):
        if res := compare_packets(a, b):
            return res
    return (len(left) > len(right)) - (len(left) < len(right))


def part_1(lines):
    return sum(
        idx
        for idx, pair in enumerate(lines.split("\n\n"), 1)
        if compare_packets(*map(ast.literal_eval, pair.splitlines())) < 0
    )


def part_2(lines):
    dividers = [[[2]], [[6]]]
    packets = sorted(
        list(map(ast.literal_eval, lines.replace("\n\n", "\n").splitlines())) + dividers,
        key=cmp_to_key(compare_packets),
    )
    return (packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
