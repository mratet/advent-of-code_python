import re

from aocd import get_data

input = get_data(day=2, year=2020).splitlines()


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    cnt = 0
    for line in lines:
        m = re.match(r"(\d+)-(\d+) ([a-z]): (\w+)", line)
        assert m
        l, h, letter, password = m.groups()
        cnt += int(l) <= password.count(letter) <= int(h)
    return cnt


def part_2(lines):
    count = 0
    for line in lines:
        m = re.match(r"(\d+)-(\d+) ([a-z]): (\w+)", line)
        assert m
        l, h, letter, password = m.groups()
        count += (password[int(l) - 1] == letter) ^ (password[int(h) - 1] == letter)
    return count


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
