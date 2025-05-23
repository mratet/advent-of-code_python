import re
from aocd import get_data

input = get_data(day=9, year=2016)

pattern = r"\((\d+)x(\d+)\).*"


def compute_length(s, part="part_1"):
    if not s:
        return 0
    elif s[0].isalpha():
        return 1 + compute_length(s[1:], part)
    else:
        _, s_trun = s.split(")", 1)
        match = re.search(pattern, s)
        subseq, repeat = int(match.group(1)), int(match.group(2))

        if part == "part_1":
            return subseq * repeat + compute_length(s_trun[subseq:], part)
        else:
            return compute_length(s_trun[:subseq], part) * repeat + compute_length(
                s_trun[subseq:], part
            )


def part_1(input):
    return compute_length(input)


def part_2(input):
    return compute_length(input, "part_2")


print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
