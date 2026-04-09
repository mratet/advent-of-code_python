from functools import reduce
from operator import xor

from aocd import get_data

input = get_data(day=10, year=2017)


# WRITE YOUR SOLUTION HERE
def knot_rounds(lengths, n=256):
    L = list(range(n))
    current_pos = 0
    for skip_size, length in enumerate(lengths):
        indices = [i % n for i in range(current_pos, current_pos + length)]
        values = reversed([L[i] for i in indices])
        for i, v in zip(indices, values, strict=False):
            L[i] = v
        current_pos = (current_pos + length + skip_size) % n
    return L


def knot_hash(word):
    length = [ord(c) for c in word] + [17, 31, 73, 47, 23]
    L = knot_rounds(64 * length)
    xor_hash = [reduce(xor, L[i : i + 16]) for i in range(0, 256, 16)]
    return "".join(f"{x:02x}" for x in xor_hash)


def part_1(lines):
    lengths = list(map(int, lines.split(",")))
    L = knot_rounds(lengths)
    return L[0] * L[1]


def part_2(lines):
    return knot_hash(lines)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
