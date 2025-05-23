from aocd import get_data, submit

input = get_data(day=1, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def solve(input, n):
    measurements = [int(n) for n in input]
    return sum(
        measurements[i] < measurements[i + n] for i in range(len(measurements) - n)
    )


def part_1(lines):
    return solve(lines, 1)


def part_2(lines):
    return solve(lines, 3)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
