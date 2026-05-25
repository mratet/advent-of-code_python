from aocd import get_data

input = get_data(day=3, year=2022).splitlines()


# WRITE YOUR SOLUTION HERE
def compute_priority(c):
    return ord(c) - ord("a") + 1 if c.islower() else ord(c) - ord("A") + 27


def solve(groups):
    return sum(compute_priority(set.intersection(*map(set, group)).pop()) for group in groups)


def part_1(lines):
    return solve([(line[: len(line) // 2], line[len(line) // 2 :]) for line in lines])


def part_2(lines):
    return solve(zip(lines[::3], lines[1::3], lines[2::3], strict=False))


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
