from aocd import get_data

input = get_data(day=2, year=2017).splitlines()
from itertools import product


# WRITE YOUR SOLUTION HERE
def part_1(lines):
    ans = 0
    for line in lines:
        numb = list(map(int, line.split()))
        ans += max(numb) - min(numb)
    return ans


def part_2(lines):
    ans = 0
    for line in lines:
        numb = list(map(int, line.split()))
        for n, m in product(numb, numb):
            if n == m:
                continue
            if n % m == 0:
                ans += n // m
    return ans


# END OF SOLUTION
print(f"My answer is {part_1(input)}")
print(f"My answer is {part_2(input)}")
