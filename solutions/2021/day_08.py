from aocd import get_data
from collections import defaultdict

input = get_data(day=8, year=2021).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    count = 0
    for display in lines:
        _, digit_output = display.split(" | ")
        count += sum(1 for digit in digit_output.split() if len(digit) in (2, 3, 4, 7))
    return count


def get_reversed_mapping(signal_patterns):
    signal = signal_patterns.split()
    signal_dict = defaultdict(list)
    for s in signal:
        signal_dict[len(s)].append(s)
    all_letters = set(signal_dict[7][0])
    one_letters = set(signal_dict[2][0])
    seven_letters = set(signal_dict[3][0])
    four_letters = set(signal_dict[4][0])
    a = (seven_letters - one_letters).pop()
    cde = {(all_letters - set(s)).pop() for s in signal_dict[6]}
    f = (one_letters - cde).pop()
    c = (one_letters - set(f)).pop()
    d = ((four_letters - one_letters) & cde).pop()
    e = (cde - set(c) - set(d)).pop()
    b = (four_letters - one_letters - set(d)).pop()
    g = (all_letters - four_letters - set(a) - set(e)).pop()
    return {a: "a", b: "b", c: "c", d: "d", e: "e", f: "f", g: "g"}


digit_mapping = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def part_2(lines):
    score = 0
    for display in lines:
        signal_patterns, digit_output = display.split(" | ")
        reversed_mapping = get_reversed_mapping(signal_patterns)
        clean_digit = ""
        for digit in digit_output.split(" "):
            new_digit = "".join(sorted([reversed_mapping[d] for d in digit]))
            clean_digit += digit_mapping[new_digit]
        score += int(clean_digit)
    return score


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
