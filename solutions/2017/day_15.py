import re

from aocd import get_data

input = get_data(day=15, year=2017)

FACTOR_A = 16807
FACTOR_B = 48271
MOD = 2147483647
MASK = 0xFFFF


# WRITE YOUR SOLUTION HERE
def next_value(val, factor, multiple):
    val = val * factor % MOD
    while val % multiple:
        val = val * factor % MOD
    return val


def solve(lines, part="part_1"):
    A, B = map(int, re.findall(r"(\d+)", lines))
    N, mult_a, mult_b = (40_000_000, 1, 1) if part == "part_1" else (5_000_000, 4, 8)
    ans = 0
    for _ in range(N):
        A = next_value(A, FACTOR_A, mult_a)
        B = next_value(B, FACTOR_B, mult_b)
        ans += (A & MASK) == (B & MASK)
    return ans


def part_1(lines):
    return solve(lines, "part_1")


def part_2(lines):
    return solve(lines, "part_2")


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
