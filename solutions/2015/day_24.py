import itertools
import math

from aocd import get_data

input = get_data(day=24, year=2015).splitlines()


def find_best_qe(nums, k):
    target = sum(nums) // k
    # We test the first group of combinations
    for n in range(1, len(nums)):
        good = [x for x in list(itertools.combinations(nums, n)) if sum(x) == target]
        if good:
            return min(math.prod(x) for x in good)


def solve(input, N):
    nums = list(map(int, input))
    return find_best_qe(nums, N)


def part_1(input):
    return solve(input, 3)


def part_2(input):
    return solve(input, 4)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
