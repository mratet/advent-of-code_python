from aocd import get_data

input = get_data(day=6, year=2022)


# WRITE YOUR SOLUTION HERE
def solve(signal, n):
    return next(i + n for i in range(len(signal)) if len(set(signal[i : i + n])) == n)


def part_1(lines):
    return solve(lines, 4)


def part_2(lines):
    return solve(lines, 14)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
