from aocd import get_data

input = get_data(day=1, year=2020).splitlines()
from itertools import product


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    numb = [int(n) for n in lines]
    temp = set()
    for n in numb:
        if 2020 - n in temp:
            return (2020 - n) * n
        temp.add(n)


def part_2(lines):
    numb = [int(n) for n in lines]
    numb.sort()
    for n, m in product(numb, numb):
        if 2020 - n - m in numb:
            return n * m * (2020 - n - m)


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
