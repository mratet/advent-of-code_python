from aocd import get_data, submit

input = get_data(day=7, year=2024).splitlines()
from operator import add, mul


# WRITE YOUR SOLUTION HERE
def solve(lines, op_list):
    cnt = 0
    for line in lines:
        numb, x, *Y = map(int, line.replace(":", "").split())
        X = [x]
        for y in Y:
            X = [op(x, y) for x in X for op in op_list if op(x, y) <= numb]
        if numb in X:
            cnt += numb
    return cnt


def part_1(lines):
    return solve(lines, (add, mul))


def part_2(lines):
    return solve(lines, (add, mul, lambda x, y: int(str(x) + str(y))))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
