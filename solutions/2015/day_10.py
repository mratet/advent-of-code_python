import itertools

from aocd import get_data

input = get_data(day=10, year=2015)


def next_step(sequence):
    return "".join(str(len(list(v))) + k for k, v in itertools.groupby(sequence))


def solve(input, step):
    for _ in range(step):
        input = next_step(input)
    return len(input)


def part_1(input):
    return solve(input, 40)


def part_2(input):
    return solve(input, 50)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
