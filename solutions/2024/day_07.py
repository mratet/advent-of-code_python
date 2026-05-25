from operator import add, mul

from aocd import get_data

input = get_data(day=7, year=2024).splitlines()


# WRITE YOUR SOLUTION HERE
def concat(x, y):
    return int(str(x) + str(y))


def solve(lines, op_list):
    cnt = 0
    for line in lines:
        target, first, *nums = map(int, line.replace(":", "").split())
        vals = [first]
        for num in nums:
            vals = [op(v, num) for v in vals for op in op_list if op(v, num) <= target]
        if target in vals:
            cnt += target
    return cnt


def part_1(lines):
    return solve(lines, (add, mul))


def part_2(lines):
    return solve(lines, (add, mul, concat))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
