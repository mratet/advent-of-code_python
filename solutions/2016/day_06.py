from collections import Counter

from aocd import get_data

input = get_data(day=6, year=2016).splitlines()


def send_message(input, part="part_1"):
    cols = zip(*input, strict=False)
    func = max if part == "part_1" else min
    return "".join([func(Counter(col).items(), key=lambda x: x[1])[0] for col in cols])


def part_1(input):
    return send_message(input, "part_1")


def part_2(input):
    return send_message(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
