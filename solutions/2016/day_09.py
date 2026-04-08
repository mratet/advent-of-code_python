import re

from aocd import get_data

input = get_data(day=9, year=2016)

MARKER = re.compile(r"\((\d+)x(\d+)\)")


def compute_length(s, i=0, recursive=False):
    if i >= len(s):
        return 0
    m = MARKER.match(s, i)
    if not m:
        return 1 + compute_length(s, i + 1, recursive)
    subseq, repeat = int(m.group(1)), int(m.group(2))
    end = m.end()
    if recursive:
        return compute_length(s[end : end + subseq], 0, True) * repeat + compute_length(s, end + subseq, True)
    return subseq * repeat + compute_length(s, end + subseq, False)


def part_1(input):
    return compute_length(input)


def part_2(input):
    return compute_length(input, recursive=True)


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
