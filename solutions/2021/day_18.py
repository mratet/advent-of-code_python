import itertools

from aocd import get_data
import math
import re
from functools import reduce

input = get_data(day=18, year=2021).splitlines()


class SnailfishPair:
    def __init__(self, nums, depths):
        self.nums = nums
        self.depths = depths

    def update_depths(self):
        return [1 + d for d in self.depths]

    def compute_magnitude(self):
        nums, depths = self.nums.copy(), self.depths.copy()
        while any(d > 0 for d in depths):
            max_d = max(depths)
            while max_d in depths:
                idx = depths.index(max_d)
                lN, rN = nums[idx], nums[idx + 1]
                nums[idx] = 3 * lN + 2 * rN
                depths[idx] -= 1
                nums.pop(idx + 1)
                depths.pop(idx + 1)
        return nums[0]


def parse_snailfish_pair(line):
    nums, depths = [], []
    depth = 0
    for c in line:
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        elif c.isdigit():
            nums.append(int(c))
            depths.append(depth)
    return SnailfishPair(nums, depths)


def add_snailfish_pair(s1: SnailfishPair, s2: SnailfishPair):
    new_nums = s1.nums + s2.nums
    new_depths = s1.update_depths() + s2.update_depths()
    new_s = SnailfishPair(new_nums, new_depths)
    return reduce_snailfish_pair(new_s)


def reduce_snailfish_pair(s: SnailfishPair):
    if any(d > 4 for d in s.depths):
        exploded_pair = explode_snailfish_pair(s)
        return reduce_snailfish_pair(exploded_pair)
    elif any(n >= 10 for n in s.nums):
        split_pair = split_snailfish_pair(s)
        return reduce_snailfish_pair(split_pair)
    return s


def split_snailfish_pair(s: SnailfishPair):
    idx = next(i for i in range(len(s.nums)) if s.nums[i] >= 10)
    N = s.nums[idx]
    lN, rN = math.floor(N / 2), math.ceil(N / 2)
    new_nums = s.nums.copy()
    new_depths = s.depths.copy()
    new_nums[idx] = rN
    new_depths[idx] += 1
    new_nums.insert(idx, lN)
    new_depths.insert(idx + 1, new_depths[idx])
    return SnailfishPair(new_nums, new_depths)


def explode_snailfish_pair(s: SnailfishPair):
    idx = next(i for i in range(len(s.nums)) if s.depths[i] > 4)
    new_nums = s.nums.copy()
    new_depths = s.depths.copy()
    lN, rN = s.nums[idx], s.nums[idx + 1]
    new_nums.pop(idx + 1)
    new_depths.pop(idx + 1)

    new_nums[idx] = 0
    if idx > 0:
        new_nums[idx - 1] += lN
    if idx < len(s.nums) - 2:
        new_nums[idx + 1] += rN
    new_depths[idx] -= 1
    return SnailfishPair(new_nums, new_depths)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    fishs = [parse_snailfish_pair(l) for l in lines]
    current_fish = reduce(add_snailfish_pair, fishs)
    return current_fish.compute_magnitude()


def part_2(lines):
    fishs = [parse_snailfish_pair(l) for l in lines]
    magnitudes = [
        add_snailfish_pair(f1, f2).compute_magnitude()
        for f1, f2 in itertools.product(fishs, repeat=2)
    ]
    return max(magnitudes)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
