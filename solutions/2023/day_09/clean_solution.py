import itertools

from aocd import get_data

input = get_data(day=9, year=2023).splitlines()


# WRITE YOUR SOLUTION HERE
def next_history_value(history):
    diffs = [b - a for a, b in itertools.pairwise(history)]
    return history[-1] + next_history_value(diffs) if history else 0


def parse_input(lines):
    return [list(map(int, line.split())) for line in lines]


def part_1(lines):
    return sum(next_history_value(history) for history in parse_input(lines))


def part_2(lines):
    return sum(next_history_value(history[::-1]) for history in parse_input(lines))


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
