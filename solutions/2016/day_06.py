import itertools, re, collections
from aocd import get_data

input = get_data(day=6, year=2016).splitlines()


def send_message(input, part="part_1"):
    col = zip(*input)
    t = ""
    for row in col:
        count = collections.Counter(row)
        c, _ = max(count.items(), key=lambda x: x[1])
        if part == "part_2":
            c, _ = min(count.items(), key=lambda x: x[1])
        t += c
    return t


def part_1(input):
    return send_message(input, "part_1")


def part_2(input):
    return send_message(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
