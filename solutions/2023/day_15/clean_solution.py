from aocd import get_data

input = get_data(day=15, year=2023).splitlines()

# WRITE YOUR SOLUTION HERE
from functools import reduce
from collections import defaultdict

char = lambda i, c: (i + ord(c)) * 17 % 256
hash = lambda s: reduce(char, s, 0)


def _parse(lines):
    return lines[0].split(",")


def part_1(lines):
    return sum(map(hash, _parse(lines)))


def part_2(lines):
    boxes = defaultdict(dict)
    for u in _parse(lines):
        if "-" in u:
            label = u[:-1]
            box_number = hash(label)
            boxes[box_number].pop(label, None)
        else:
            label, focal_length = u.split("=")
            boxes[hash(label)][label] = int(focal_length)

    return sum(
        (i + 1) * (j + 1) * l for i in boxes for j, l in enumerate(boxes[i].values())
    )


# END OF SOLUTION


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
