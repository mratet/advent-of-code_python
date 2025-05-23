from aocd import get_data

input = get_data(day=9, year=2023).splitlines()


# WRITE YOUR SOLUTION HERE
def next_history_value(history):
    diffs = [b - a for a, b in zip(history, history[1:])]
    return history[-1] + next_history_value(diffs) if history else 0


def _parse(input):
    return [list(map(int, line.split())) for line in input]


def part_1(input):
    histories = _parse(input)
    return sum([next_history_value(history) for history in histories])


def part_2(input):
    histories = _parse(input)
    return sum([next_history_value(history[::-1]) for history in histories])


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
