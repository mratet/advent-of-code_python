from aocd import get_data

input = get_data(day=6, year=2020).split("\n\n")
from string import ascii_lowercase


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    return sum([len(set(line.replace("\n", ""))) for line in lines])


def part_2(lines):
    cnt = 0
    for line in lines:
        form = set(ascii_lowercase)
        for ans in line.split():
            form &= set(ans)
        cnt += len(form)
    return cnt


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
