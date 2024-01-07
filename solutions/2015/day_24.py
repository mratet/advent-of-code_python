import itertools, re, collections
from aocd import get_data
input = get_data(day=24, year=2015).splitlines()

from operator import mul
from functools import reduce

def find_best_qe(nums, k):
    aim = sum(nums) // k
    # We test the first group of combinations
    for n in range(1, len(nums)):
        good = [x for x in list(itertools.combinations(nums, n)) if sum(x) == aim]
        if len(good) > 0:
            break

    best_comb = min(good, key=lambda x: reduce(mul, x))
    return reduce(mul, best_comb)

def part_1(input):
    nums = list(map(int, input))
    return find_best_qe(nums, 3)

def part_2(input):
    nums = list(map(int, input))
    return find_best_qe(nums, 4)


print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
