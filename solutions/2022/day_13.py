from aocd import get_data
from functools import cmp_to_key
import ast

input = get_data(day=13, year=2022)


def compare_packets(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right

    if isinstance(left, list) and isinstance(right, list):
        for l_item, r_item in zip(left, right):
            res = compare_packets(l_item, r_item)
            if res is not None:
                return res
        if len(left) != len(right):
            return len(left) < len(right)
        return None

    if isinstance(left, int):
        return compare_packets([left], right)
    else:
        return compare_packets(left, [right])


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    s = 0
    for idx, pair in enumerate(lines.split("\n\n"), start=1):
        p1, p2 = map(ast.literal_eval, pair.splitlines())
        if compare_packets(p1, p2):
            s += idx
    return s


def part_2(lines):
    divider_packets = [[[2]], [[6]]]
    packets = (
        list(map(ast.literal_eval, lines.replace("\n\n", "\n").splitlines()))
        + divider_packets
    )
    packets = sorted(
        packets,
        key=cmp_to_key(lambda l, r: 2 * (compare_packets(l, r) - 0.5)),
        reverse=True,
    )
    i1, i2 = packets.index(divider_packets[0]), packets.index(divider_packets[1])
    return (i1 + 1) * (i2 + 1)


# END OF SOLUTION

print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
