from aocd import get_data

input = get_data(day=6, year=2022)


def solve(signal, N):
    return next(i + N for i in range(len(signal)) if len(set(signal[i : i + N])) == N)


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return solve(lines, 4)


def part_2(lines):
    return solve(lines, 14)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
