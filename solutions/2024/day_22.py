from collections import defaultdict
from itertools import pairwise

from aocd import get_data

input = get_data(day=22, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def next_secret(n):
    n = (n ^ n << 6) & 0xFFFFFF
    n = (n ^ n >> 5) & 0xFFFFFF
    return (n ^ n << 11) & 0xFFFFFF


def part_1(lines):
    ans = 0
    for n in map(int, lines):
        for _ in range(2000):
            n = next_secret(n)
        ans += n
    return ans


def part_2(lines):
    count_seq = defaultdict(int)
    for n in map(int, lines):
        bananas = [n % 10]
        for _ in range(2000):
            n = next_secret(n)
            bananas.append(n % 10)
        diff = [b2 - b1 for b1, b2 in pairwise(bananas)]
        seen = set()
        for j in range(4, len(diff) + 1):
            seq = tuple(diff[j - 4 : j])
            if seq not in seen:
                count_seq[seq] += bananas[j]
                seen.add(seq)
    return max(count_seq.values())


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
