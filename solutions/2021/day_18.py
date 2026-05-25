from functools import reduce
from itertools import permutations

from aocd import get_data

input = get_data(day=18, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
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


def add_snailfish_pair(s1, s2):
    new_nums = s1.nums + s2.nums
    new_depths = s1.update_depths() + s2.update_depths()
    return reduce_snailfish_pair(SnailfishPair(new_nums, new_depths))


def reduce_snailfish_pair(s):
    while True:
        if any(d > 4 for d in s.depths):
            s = explode_snailfish_pair(s)
        elif any(n >= 10 for n in s.nums):
            s = split_snailfish_pair(s)
        else:
            return s


def split_snailfish_pair(s):
    idx = next(i for i in range(len(s.nums)) if s.nums[i] >= 10)
    n = s.nums[idx]
    ln, rn = n // 2, (n + 1) // 2
    new_nums = s.nums.copy()
    new_depths = s.depths.copy()
    new_nums[idx] = rn
    new_depths[idx] += 1
    new_nums.insert(idx, ln)
    new_depths.insert(idx + 1, new_depths[idx])
    return SnailfishPair(new_nums, new_depths)


def explode_snailfish_pair(s):
    idx = next(i for i in range(len(s.nums)) if s.depths[i] > 4)
    new_nums = s.nums.copy()
    new_depths = s.depths.copy()
    ln, rn = s.nums[idx], s.nums[idx + 1]
    new_nums.pop(idx + 1)
    new_depths.pop(idx + 1)
    new_nums[idx] = 0
    if idx > 0:
        new_nums[idx - 1] += ln
    if idx < len(s.nums) - 2:
        new_nums[idx + 1] += rn
    new_depths[idx] -= 1
    return SnailfishPair(new_nums, new_depths)


def part_1(lines):
    fish = [parse_snailfish_pair(line) for line in lines]
    return reduce(add_snailfish_pair, fish).compute_magnitude()


def part_2(lines):
    fish = [parse_snailfish_pair(line) for line in lines]
    return max(add_snailfish_pair(f1, f2).compute_magnitude() for f1, f2 in permutations(fish, 2))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
